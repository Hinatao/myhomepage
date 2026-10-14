import streamlit as st
import time

# --- ① アプリのタイトルなどの基本設定 ---
st.set_page_config(page_title="マイホームページ", layout="centered")

# --- ② 起動時のカスタムメッセージ（ここを追加） ---
with st.spinner("ホームページを起動しています。少々お待ちください..."):
    # ※ここに重い処理（データベースへの接続やデータの読み込みなど）を書きます
    # 例として3秒待機するコードを入れています
    time.sleep(1)


#Title
st.title("奥山陽向のWeb Pageへようこそ")

st.set_page_config(page_title="ホーム",page_icon="🏠️")

st.write("ようこそ！奥山陽向の紹介ページへ")
st.write("左側のサイドバーからページを切り替えられます")
                