from openai import OpenAI, BadRequestError
import streamlit as st

openai_api_key = st.secrets["OPENAI"]["API_KEY"]
client = OpenAI(api_key = openai_api_key)
model = "gpt-4o-mini"

def generate_response(prompt: str, temperature_condition=float, top_p_condition=float):
    st.session_state['messages'].append({"role": "user", "content": prompt})
    response = None
    while len(st.session_state['messages']) > 7:
        st.session_state['messages'].pop(1)
    try:
        response=client.chat.completions.create(
            model=model,
            temperature=temperature_condition,
            top_p=top_p_condition,
            messages=st.session_state['messages'],
            max_tokens=600,
            stream=True
        )
    except BadRequestError as e:
        response = "入力情報が長すぎます！　「リセット」をクリックして会話をリセットしてください。"
    
    with st.chat_message("assistant"):
        bot_response_area = st.empty()
        if response is None:
            bot_response_area.write(response)
        else:
            bot_message = ""
            for chunk in response:
                if chunk.choices:
                    if chunk.choices[0].finish_reason is not None:
                        break
                    bot_message += chunk.choices[0].delta.content
                bot_response_area.write(bot_message)
    
    st.session_state['messages'].append({"role": "assistant", "content": bot_message})
    st.session_state['conversations'].append({"role": "assistant", "content": bot_message})