import streamlit as st
from blockchain import Blockchain
import time

st.set_page_config(page_title="Blockchain Diary", layout="centered")
st.title("📝 Blockchain-Based Digital Diary")

diary = st.session_state.get("diary", Blockchain())
st.session_state.diary = diary

with st.form("entry_form"):
    entry = st.text_area("Write your diary entry:", height=150)
    submitted = st.form_submit_button("Add Entry")
    if submitted and entry:
        last = diary.get_last_block()
        diary.create_block(entry, last['hash'])
        st.success("Entry added to blockchain!")

st.subheader("📚 Diary Chain")
for block in reversed(diary.chain):
    st.markdown(f"""
    **Block {block['index']}**
    - Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(block['timestamp']))}
    - Entry: {block['entry']}
    - Hash: `{block['hash']}`
    - Previous Hash: `{block['previous_hash']}`
    """)

if st.button("Validate Blockchain"):
    if diary.is_valid():
        st.success("✅ Blockchain is valid and tamper-proof.")
    else:
        st.error("❌ Blockchain integrity compromised!")
