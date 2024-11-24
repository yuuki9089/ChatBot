import streamlit as st
import llm as lm

# 変数の定義
USER_NAME = "user"
MAIN_BOT_NAME = "god"
SORCE_BOT_NAME = "sorcekun"

# アバターに画像つけようとしたけどstreamlitにはないらしい(時間かかりそうだから一旦パス)
# avatar_img_dict = {
#     MAIN_BOT_NAME: "C:/Ai/image/00040-3370343738.png",
# }

# セッションの初期化
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

# チャットのタイトル
st.title("RAG検証環境in自宅")

# 質問内容を入力するテキストエリアの作成
user_msg = st.chat_input(placeholder="回答を入力")

# メッセージが入力されたとき
if user_msg:
    # 前回までの会話をセッションを下にすべて表示 ← これがないと会話1回ごとに画面がリセットされる(上書きされる)
    for chat in st.session_state.chat_log:
        # avatar = avatar_img_dict.get(chat["name"], None)
        # with st.chat_message(chat["name"],avatar=avatar):
        with st.chat_message(chat["name"]):
            st.write(chat["msg"])
    
    # ユーザのアイコンを付けて入力内容を表示
    with st.chat_message(USER_NAME):
        st.write(user_msg)

    ans = lm.Generate_ans(user_msg)

    # メインチャットボットのアイコンを付けて入力内容を表示
    with st.chat_message(MAIN_BOT_NAME):
        # main_bot_msg = "ここで回答を出力"
        st.write(ans)
    # ソースボットのアイコンを付けて入力内容を表示
    with st.chat_message(SORCE_BOT_NAME):
        sorce_bot_msg = "ここにソースURLを表示"
        st.write(sorce_bot_msg)

    

    # 会話の内容をセッションに追加
    st.session_state.chat_log.append({"name":USER_NAME,"msg":user_msg})
    st.session_state.chat_log.append({"name":MAIN_BOT_NAME,"msg":ans})
    st.session_state.chat_log.append({"name":SORCE_BOT_NAME,"msg":sorce_bot_msg})

# ---【MEMO】---

# テキスト入力ボックスの生成
# st.text_input("入力", value=None, max_chars=100, type="default", help="聞きたいことをいれてね", on_change=None, placeholder="回答を入力")

# 数字の入力ボックスの生成
# input_num = st.number_input('Input a number', value=0)