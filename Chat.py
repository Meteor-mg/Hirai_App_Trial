import streamlit as st
from services.components import show_conversations, print_debug
from services.client import generate_response

#---------------------------------------------------------------------------------
# 画面設定
#---------------------------------------------------------------------------------

st.set_page_config(
    page_title = "アイデア壁打ちチャット Trial by Mogi",
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

temperature = 0.7
top_p = 0.7

#---------------------------------------------------------------------------------
# サイドバー
#---------------------------------------------------------------------------------

#サイドバーを追加する場合はここへ


#---------------------------------------------------------------------------------
# メイン画面
#---------------------------------------------------------------------------------

st.title("アイデア壁打ち用アプリ ver.1.0")
st.markdown("アイデアの壁打ちを行うAIチャットの試作品です。")

query = st.chat_input("メッセージを入力してください", key="chat_input")

if query:
    st.session_state['conversations'].append({"role": "user", "content": query})
    show_conversations()
    generate_response(prompt = query, temperature_condition=temperature, top_p_condition=top_p)

print_debug()
