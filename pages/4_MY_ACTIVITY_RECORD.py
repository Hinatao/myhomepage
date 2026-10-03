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
    ・width: 220, 100 などの数値指定で確実にサイズ変更可能
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

    # --- width の解析 (数値なら px に変換) ---
    if isinstance(width, (int, float)):
        css_w = f"{int(width)}px"
    else:
        css_w = width if (width.endswith("%") or width.endswith("px")) else f"{width}px"

    # カラム全体の「強制100%幅」を打ち消し、指定した幅に固定するCSS
    st.html(f"""
        <style>
        /* スマホ対応：横並びを強制 */
        [data-testid="stHorizontalBlock"] {{
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            gap: 8px !important;
            justify-content: center !important;
            align-items: center !important;
        }}
        
        /* 画像を保持する要素・カラムのサイズを制限 */
        [data-testid="stHorizontalBlock"] > div {{
            min-width: 0 !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
        }}
        
        /* st.image 内部の画像サイズ指定を上書き強制 */
        [data-testid="stImage"] {{
            width: {css_w} !important;
            max-width: 100% !important;
            margin: 0 auto !important;
        }}
        [data-testid="stImage"] > img {{
            width: 100% !important;
            height: auto !important;
            object-fit: contain !important;
        }}
        </style>
    """)

    # -------------------------------------------------------------
    # パターンA：画像が1枚だけの場合（中央寄せ表示）
    # -------------------------------------------------------------
    if len(image_list) == 1:
        found_path = find_image(image_list[0])
        cols = st.columns([1, 2, 1])
        with cols[1]:
            if found_path:
                st.image(str(found_path))
            else:
                st.error(f"画像なし: {Path(image_list[0]).name}")

    # -------------------------------------------------------------
    # パターンB：画像が2枚以上の場合（スマホでも横2列を維持）
    # -------------------------------------------------------------
    else:
        for i in range(0, len(image_list), 2):
            pair = image_list[i:i+2]
            
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
                        st.image(str(found_path))
                    else:
                        st.error(f"画像なし: {Path(img_path).name}")

    # キャプション（共通）
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
    width=500
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
    width=180
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
        "photo/micronecia_1.jpg","photo/micronecia.jpg","photo/micronecia_2.jpg"
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
