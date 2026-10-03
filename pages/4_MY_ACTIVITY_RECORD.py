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

#関数定義----------------------------------------------
def display_images_2col(image_list, caption="", width=220):
    """
    ネット上・スマホ環境でも確実に画像を見つけ出し、横2枚ずつ配置する関数
    """
    # 実行中ファイルの位置からプロジェクトのルート（親フォルダ）まで探索
    current_file = Path(__file__).resolve()
    
    # 画像ファイルを探す関数（相対パス・絶対パス・pages階層ズレを吸収）
    def find_image(img_path_str):
        p = Path(img_path_str)
        if p.is_absolute() and p.exists():
            return p
        
        # 探す候補パスのリスト
        candidates = [
            current_file.parent / p,               # 同一フォルダ
            current_file.parent.parent / p,        # 1つ上の親フォルダ (pagesから見たルート)
            current_file.parent.parent.parent / p  # さらに上の階層
        ]
        
        for cand in candidates:
            if cand.exists():
                return cand
        return None

    # 2枚ずつペアにして表示
    for i in range(0, len(image_list), 2):
        pair = image_list[i:i+2]
        
        # 画面幅に合わせて綺麗に2列配置
        cols = st.columns(2, gap="small")
        
        for idx, img_path in enumerate(pair):
            found_path = find_image(img_path)
            
            with cols[idx]:
                if found_path:
                    st.image(str(found_path), width=width)
                else:
                    st.error(f"画像なし: {Path(img_path).name}")

    # 一番最後に1つだけキャプションを表示
    if caption:
        st.markdown(
            f"<p style='text-align: center; color: gray; font-size: 0.85em; margin-top: -5px;'>"
            f"{caption}"
            f"</p>",
            unsafe_allow_html=True
        )
#-----------------------------------------------

#ネイチャーキッズ---------------
display_images_2col(
    image_list=[
        "photo/nature_kids.jpg"
    ],
    caption="ネイチャーキッズ特派員",
    width=220
)
#--------------------------------

#アジア子ども会議---------------
display_images_2col(
    image_list=[
        "photo/asia_conf.jpg","photo/asia_conf_1.jpg"
    ],
    caption="アジアこども会議",
    width=220
)
#--------------------------------
