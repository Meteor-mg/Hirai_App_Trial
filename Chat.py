import streamlit as st
from services.components import generate_response, store_response, show_conversations, print_debug

#---------------------------------------------------------------------------------
# 画面設定
#---------------------------------------------------------------------------------

st.set_page_config(
    page_title = "アイデア壁打ちチャット Trial ver2.0",
    page_icon = "💡",
    layout = "wide",
    initial_sidebar_state = "expanded"
)

#---------------------------------------------------------------------------------
# 各ステートの初期化
#---------------------------------------------------------------------------------

system_prompt="""あなたは役に立つアシスタントです。
質問された事について答えを教えるのではなく、質問者の考えを深めるよう誘導してください。"""

if 'conversations' not in st.session_state:
    st.session_state['conversations'] = []
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": f"{system_prompt}"}]

# ここはあとで動的な値にします！！！
temperature_a = 0.3
top_p_a = 0.3
temperature_b = 0.9
top_p_b = 1.0

#---------------------------------------------------------------------------------
# サイドバー
#---------------------------------------------------------------------------------

#サイドバーを追加する場合はここへ


#---------------------------------------------------------------------------------
# メイン画面
#---------------------------------------------------------------------------------

st.title("アイデア壁打ちチャット Trial ver2.0")
st.markdown("アイデアの壁打ちを行うAIチャットの試作品です。")

user_input = st.chat_input("メッセージを入力してください", key="chat_input")

if user_input:
    st.session_state['conversations'].append({"role": "user", "content": user_input})
    show_conversations()
    
    # Bot Aからの回答を生成
    response_a = generate_response(prompt = user_input, temperature_condition=temperature_a, top_p_condition=top_p_a)
    store_response("1号", response_a)
    
    # Bot Bからの回答を生成
    response_b = generate_response(prompt = user_input, temperature_condition=temperature_a, top_p_condition=top_p_a)
    store_response("2号", response_b)
    

print_debug()
