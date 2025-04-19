from openai import OpenAI
import streamlit as st

openai_api_key = st.secrets["OPENAI"]["API_KEY"]
client = OpenAI(api_key = openai_api_key)
model = "gpt-4o-mini"

# リクエストを送って回答responseを返す関数
def request_to_openai(temperature_condition=float, top_p_condition=float):
    try:
        response=client.chat.completions.create(
                model=model,
                temperature=temperature_condition,
                top_p=top_p_condition,
                messages=st.session_state['messages'],
                max_tokens=600,
                stream=True
            )
        return response
    except Exception as e:
        raise RuntimeError("""ランタイムエラーです。もう一度お試しください。\n
        (頻繁にこのエラーが発生する場合は管理者に連絡するか、プランをグレードアップして許容トークン数を増やすことをおすすめします。)""")
