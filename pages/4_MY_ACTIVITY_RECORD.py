import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="活動記録",page_icon="📷️")
st.title("過去の活動記録")
st.write("個人情報保護のため、人が写っている写真にはモザイク処理がかかっています。ご了承ください")

#センタリング関数----------------------
def st_image_center(image, **kwargs):
    st.columns([1, 2, 1])[1].image(image, **kwargs)
#--------------------------------------

#ネイチャーキッズ特派員-------------------------------
st_image_center("photo/nature_kids.jpg",width=220)
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
    st_image_center("photo/asia_conf.jpg",width=220)

with col2:
    st_image_center("photo/asia_conf_1.jpg",width=220)

caption_col, _ = st.columns([8, 5])
with caption_col:
    st.markdown(
     "<p style='text-align: center; color: gray; font-size: 0.85em; margin-top: -10px;'>"
     "第26回アジアこども会議"
     "</p>",
     unsafe_allow_html=True
    )
#---------------------------------------------------------


#子ども国会----------------------------------------------------
st_image_center("photo/kids_diet.jpg",width=220)
caption_col, _ = st.columns([8, 5])
with caption_col:
    st.markdown(
     "<p style='text-align: center; color: gray; font-size: 0.85em; margin-top: -10px;'>"
     "こども国会"
     "</p>",
     unsafe_allow_html=True
    )
#-----------------------------------------------------------

#English camp---------------------------------------------
st_image_center("photo/english_camp.jpg",width=220)
caption_col, _ = st.columns([8, 5])
with caption_col:
    st.markdown(
     "<p style='text-align: center; color: gray; font-size: 0.85em; margin-top: -10px;'>"
     "English Camp"
     "</p>",
     unsafe_allow_html=True
    )
#-------------------------------------------------

#納口先生のイベント---------------------------------
col1, col2,_ = st.columns([2.5,2.5,3],gap="small")

with col1:
    st_image_center("photo/dr_nadarenjar.jpg",width=220)

with col2:
    st_image_center("photo/earthquake_reserch.jpg",width=220)

caption_col, _ = st.columns([8, 5])
with caption_col:
    st.markdown(
     "<p style='text-align: center; color: gray; font-size: 0.85em; margin-top: -10px;'>"
     "納口先生の防災イベントの様子"
     "</p>",
     unsafe_allow_html=True
    )
#------------------------------------------------------


#画像貼り付けの関数定義-------------------------------

def display_images_grid_2col(image_list, caption="", img_max_width="200px"):
    """
    st.columns を使用して HTML を一切使わずに2列配置する安全な関数
    """
    # 2枚ずつペアにして列を作る
    for i in range(0, len(image_list), 2):
        pair = image_list[i:i+2]
        
        # 1行を [余白, 画像1, 画像2, 余白] の4カラムに分割して中央寄せる
        cols = st.columns([1, 2, 2, 1])
        
        for idx, img_path in enumerate(pair):
            with cols[idx + 1]:
                if Path(img_path).exists():
                    st.image(str(img_path), use_container_width=True)
                else:
                    st.error(f"画像なし: {Path(img_path).name}")

    # 一番最後に1つだけキャプションを表示
    if caption:
        st.caption(f"<div style='text-align: center;'>{caption}</div>", unsafe_allow_html=True)
        
#------------------------------------------------------------

#ネイチャーキッズ----------------------------------------

BASE_DIR = Path("/home/hinata/myhomepage")

images = [
    BASE_DIR / "photo" / "nature_kids.jpg"
]

display_images_grid_2col(
    image_list=images,
    caption="ネイチャーキッズ特派員"
)
#--------------------------------------------------

#アジア子ども会議---------------------------

BASE_DIR = Path("/home/hinata/myhomepage")

images = [
    BASE_DIR / "photo" / "asia_conf.jpg",
    BASE_DIR / "photo" / "asia_conf_1.jpg"
]

display_images_grid_2col(
    image_list=images,
    caption="ネイチャーキッズ特派員"
)
