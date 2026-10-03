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
def display_images_2col(image_list, caption="", width=None):
    """
    スマホ画面でも縦にならず、絶対に横2枚で並べる関数
    """
    # --- CSSで st.columns のスマホ折り返し（縦並び）を無効化 ---
    st.html("""
        <style>
        /* columns の親要素を Flexbox 横並びで固定 */
        [data-testid="stHorizontalBlock"] {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            gap: 8px !important;
        }
        /* 各カラムが均等に幅50%を取るように強制 */
        [data-testid="stHorizontalBlock"] > div {
            width: 50% !important;
            min-width: 0 !important;
            flex: 1 1 50% !important;
        }
        /* 画像がカラム枠からはみ出ないように可変調整 */
        [data-testid="stHorizontalBlock"] img {
            width: 100% !important;
            height: auto !important;
            object-fit: contain;
        }
        </style>
    """)

    current_file = Path(__file__).resolve()
    
    def find_image(img_path_str):
        p = Path(img_path_str)
        if p.is_absolute() and p.exists():
            return p
        candidates = [
            current_file.parent / p,
            current_file.parent.parent / p,
            current_file.parent.parent.parent / p
        ]
        for cand in candidates:
            if cand.exists():
                return cand
        return None

    # 2枚ずつペアにして表示
    for i in range(0, len(image_list), 2):
        pair = image_list[i:i+2]
        
        cols = st.columns(2)
        
        for idx, img_path in enumerate(pair):
            found_path = find_image(img_path)
            
            with cols[idx]:
                if found_path:
                    # width=None (use_container_width=True) にすることでカラム幅いっぱいに収めます
                    st.image(str(found_path), use_container_width=True)
                else:
                    st.error(f"画像なし: {Path(img_path).name}")

    # すべての画像が表示し終わった後にキャプションを1つだけ出力
    if caption:
        st.markdown(
            f"<p style='text-align: center; color: gray; font-size: 0.85em; margin-top: 4px;'>"
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
st.space("midium")
#アジア子ども会議---------------
display_images_2col(
    image_list=[
        "photo/asia_conf.jpg","photo/asia_conf_1.jpg"
    ],
    caption="アジアこども会議",
    width=220
)
#--------------------------------
