import streamlit as st
from typing import Optional
from openai import  BadRequestError
from services.client import request_to_openai

# プロンプトと各パラメータを受取り、回答を返す関数
def generate_response(prompt: str, temperature_condition: float, top_p_condition: float):
    st.session_state['messages'].append({"role": "user", "content": prompt})
    response = None
    while len(st.session_state['messages']) > 7:
        st.session_state['messages'].pop(1)
    try:
        response = request_to_openai(temperature_condition, top_p_condition)
    except BadRequestError as e:
        response = """入力情報が多すぎます！　ページを更新してください。\n
        (頻繁にこのエラーが発生する場合は管理者に連絡するか、プランをグレードアップして許容トークン数を増やすことをおすすめします。)"""
    return response

# ボットの回答をステートに保存する関数
def store_response(bot_name: str, response: Optional[str]):
    if bot_name not in st.session_state:
        st.session_state[bot_name] = []
    with st.chat_message("assistant"):
        bot_response_area = st.empty()
        if response is None:
            bot_response_area.write(response)
        else:
            bot_message = f"{bot_name}: "
            for chunk in response:
                if chunk.choices:
                    if chunk.choices[0].finish_reason is not None:
                        break
                    bot_message += chunk.choices[0].delta.content
                bot_response_area.write(bot_message)
    st.session_state['messages'].append({"role": "assistant", "content": bot_message})
    st.session_state['conversations'].append({"role": "assistant", "content": bot_message})

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
