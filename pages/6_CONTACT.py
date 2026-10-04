import streamlit as st


st.set_page_config(page_title="お仕事のご連絡・相談等",page_icon="💬")

st.title("お仕事のご連絡・相談等")

st.write("お仕事のご連絡・ご相談はDMもしくは下記メールより")
st.write("過去のイベント資料に関する問い合わせ等もこちらへお願いします。")

email = "aoshanyangxiang96@gmail.com"
subject = "お問い合わせ"
body = "ここにメッセージ本文を入力してください。"

# シンプルなテキストリンク
st.markdown(
    f'<a href="mailto:{email}?subject={subject}&body={body}">aoshanyangxiang96@gmail.com</a>',
    unsafe_allow_html=True,
)
st.space("large")

st.title("LINK")

st.write("奥山陽向のInstagram")
st.markdown(
    '<a href="https://www.instagram.com/hinata.o__0504/" target="_blank" rel="noopener noreferrer">Instagramを見る</a>',
    unsafe_allow_html=True
)