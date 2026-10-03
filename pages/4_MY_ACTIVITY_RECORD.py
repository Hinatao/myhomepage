import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="活動記録",page_icon="📷️")
st.title("過去の活動記録")
st.write("個人情報保護のため、人が写っている写真にはモザイク処理がかかっています。ご了承ください")

#関数定義------------
def display_images_2col(image_list, caption="", width="100%"):
    """
    ・画像が1枚の場合：全端末で画面中央に配置
    ・画像が2枚以上の場合：スマホでも横2列で並べる
    """
    
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
    
    # -------------------------------------------------------------
    # パターンA：画像が1枚だけの場合（中央寄せ表示）
    # -------------------------------------------------------------
    if len(image_list) == 1:
        found_path = find_image(image_list[0])
        
        # [左右の余白, 中央の画像枠, 左右の余白]
        # PC・スマホどちらでも中央にほどよいサイズで収まる比率 [1, 2, 1]
        cols = st.columns([1, 2, 1])
        with cols[1]:
            if found_path:
                st.image(str(found_path), use_container_width=True)
            else:
                st.error(f"画像なし: {Path(image_list[0]).name}")

    # -------------------------------------------------------------
    # パターンB：画像が2枚以上の場合（スマホでも横2列を維持）
    # -------------------------------------------------------------
    else:
        # 2列強制用のCSSを注入
        st.html("""
            <style>
            [data-testid="stHorizontalBlock"] {
                display: flex !important;
                flex-direction: row !important;
                flex-wrap: nowrap !important;
                gap: 8px !important;
            }
            [data-testid="stHorizontalBlock"] > div {
                width: 50% !important;
                min-width: 0 !important;
                flex: 1 1 50% !important;
            }
            [data-testid="stHorizontalBlock"] img {
                width: 100% !important;
                height: auto !important;
                object-fit: contain;
            }
            </style>
        """)

        for i in range(0, len(image_list), 2):
            pair = image_list[i:i+2]
            
            # もし奇数枚で最後の1枚になった場合は中央寄せにする処理
            if len(pair) == 1:
                cols = st.columns([1, 2, 1])
                target_col = cols[1]
            else:
                cols = st.columns(2)
                target_col = None

            for idx, img_path in enumerate(pair):
                found_path = find_image(img_path)
                col_to_use = target_col if target_col else cols[idx]
                
                with col_to_use:
                    if found_path:
                        st.image(str(found_path), use_container_width=True)
                    else:
                        st.error(f"画像なし: {Path(img_path).name}")

    if caption:
            st.markdown(
                f"<p style='text-align: center; color: gray; font-size: 0.85em; margin-top: 4px;'>"
                f"{caption}"
               f"</p>",
             unsafe_allow_html=True
         )

# ----------------------------


#ネイチャーキッズ---------------
display_images_2col(
    image_list=[
        "photo/nature_kids.jpg"
    ],
    caption="ネイチャーキッズ特派員",
    width=220
)
#--------------------------------

st.space("medium")

#アジア子ども会議---------------
display_images_2col(
    image_list=[
        "photo/asia_conf.jpg","photo/asia_conf_1.jpg"
    ],
    caption="アジアこども会議",
    width=220
)
#--------------------------------

st.space("medium")

#子ども国会----------------------
display_images_2col(
    image_list=[
        "photo/kids_diet.jpg"
    ],
    caption="こども国会",
    width=220
)
#---------------------------------

st.space("medium")

#English camp----------------------
display_images_2col(
    image_list=[
        "photo/english_camp.jpg"
    ],
    caption="Englisg Camp",
    width=220
)
#----------------------------------

st.space("medium")

#納口先生-------------------------
display_images_2col(
    image_list=[
        "photo/dr_nadarenjar.jpg","photo/earthquake_reserch.jpg"
    ],
    caption="納口先生の防災イベントの様子",
    width=220
)
#-----------------------------------

st.space("medium")

#自由研究---------------------------
display_images_2col(
    image_list=[
        "photo/independence_reserch_1.jpg","photo/independence_reserch.jpg","photo/independence_reserch_2.jpg"
    ],
    caption="茨城県児童生徒科学研究作品展",
    width=220
)
#-----------------------------------

st.space("medium")

#ミクロネシア----------------------
display_images_2col(
    image_list=[
        "photo/micronecis_1.jpg","photo/micronecia.jpg","photo/micronecia_2"
    ],
    caption="ミクロネシア諸島自然体験交流事業",
    width=220
)
#-------------------------------------

st.space("medium")

#中国------------------------------
display_images_2col(
    image_list=[
        "photo/chaina.jpg","photo/chaina_1.jpg","photo/chaina_2.jpg"
    ],
    caption="古河市国際友好交流都市交流会",
    width=220
)
#---------------------------------

st.space("medium")

#2021PVチーム-----------------
display_images_2col(
    image_list=[
        "photo/2021PV.jpg"
    ],
    caption="2021年PVチーム",
    width=220
)
#-----------------------------

st.space("medium")

#2022PVチーム-----------------

display_images_2col(
    image_list=[
        "photo/2022PV.jpg"
    ],
    caption="2022年PVチーム",
    width=220
)
#-----------------------------

st.space("medium")

#修学旅行----------------------
display_images_2col(
    image_list=[
        "photo/school_trip.jpg"
    ],
    caption="下妻第一高等学校修学旅行",
    width=220
)
#-------------------------------
