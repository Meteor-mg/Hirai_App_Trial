import streamlit as st

# 会話履歴を表示する関数
def show_conversations():
    st.markdown("## 会話履歴")
    for message in st.session_state["conversations"]:
        #system message以外を会話履歴として表示する
        if message['role'] == "system":
            continue
        with st.chat_message(message['role']):
            st.write(message['content'])

# デバッグ用に保持している会話履歴を出力する関数
def print_debug():
    print("\n-------------------------messages Debug-------------------------")
    for index, message in enumerate(st.session_state['messages']):
        print(f"index: {index}, role: {message['role']}, content: {message['content']}")
    
    print("\n-------------------------conversations Debug-------------------------")
    for index, message in enumerate(st.session_state['conversations']):
        print(f"index: {index}, role: {message['role']}, content: {message['content']}")
