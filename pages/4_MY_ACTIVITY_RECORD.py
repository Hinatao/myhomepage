import streamlit as st

st.set_page_config(page_title="活動記録",page_icon="📷️")
st.title("過去の活動記録")
st.write("個人情報保護のため、人が写っている写真にはモザイク処理がかかっています。ご了承ください")

#ネイチャーキッズ特派員-------------------------------
st.image("photo/nature_kids.jpg",width=220)
caption_col, _ = st.columns([8, 5])
with caption_col:
    st.markdown(
     "<p style='text-align: center; color: gray; font-size: 0.85em; margin-top: -10px;'>"
     "ネイチャーキッズ特派員"
     "</p>",
     unsafe_allow_html=True
    )
#-----------------------------------------------------


#アジアこども会議-------------------------------------
col1, col2,_ = st.columns([2.5,2.5,3],gap="small")

with col1:
    st.image("photo/asia_conf.jpg",width=220)

with col2:
    st.image("photo/asia_conf_1.jpg",width=220)

caption_col, _ = st.columns([8, 5])
with caption_col:
    st.markdown(
     "<p style='text-align: center; color: gray; font-size: 0.85em; margin-top: -10px;'>"
     "第26回アジアこども会議"
     "</p>",
     unsafe_allow_html=True
    )
#---------------------------------------------------------

