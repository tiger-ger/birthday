import streamlit as st

# CSSスタイルの定義
st.markdown(
    """
    <style>
    .title {
        color: #FF69B4; /* ピンク色 */
    }
    .message {
        color: #FFA07A; /* サーモンピンク色 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# アプリのタイトル
st.markdown("<h1 class='title'>Happy Birthday!</h1>", unsafe_allow_html=True)

st.write('タイガちゃんお手製アプリだよ!!')

# ボタンを押すとメッセージを表示
if st.button("祝う!"):
    st.markdown("<h2 class='message'>ゆいな</h2>", unsafe_allow_html=True)
    st.subheader("誕生日おめでとう！")
    st.write("ゆうごと楽しんでね！")
    st.image("https://lh6.googleusercontent.com/proxy/bDo_YTdxpT0ZOUR8umwyCW4aAJgunnm_x9vOuxgYic3APp6YpYpnof_ZdLjT-CaIPHmhtjfsp1F4rG_YaoY9o_P_wlECDDDYHui3rOjgeTWUDjf0VqRQlal_EA", caption="Happy Birthday!")
