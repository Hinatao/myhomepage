import streamlit as st


st.set_page_config(page_title="お仕事のご連絡・相談等",page_icon="💬")


st.write("お仕事のご連絡・ご相談はDMもしくは下記メールより")

email = "aoshanyangxiang96@gmail.com"
subject = "お問い合わせ"
body = "ここにメッセージ本文を入力してください。"

# シンプルなテキストリンク
st.markdown(
    f'<a href="mailto:{email}?subject={subject}&body={body}">aoshanyangxiang96@gmail.com</a>',
    unsafe_allow_html=True,
)