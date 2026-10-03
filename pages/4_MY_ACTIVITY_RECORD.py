import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="活動記録",page_icon="📷️")
st.title("過去の活動記録")
st.write("個人情報保護のため、人が写っている写真にはモザイク処理がかかっています。ご了承ください")

#関数定義------------
def display_images_2col(image_list, caption="", width="100%"):
    """
    ・大量の画像でもメモリを消費しにくい軽量版
    ・1枚の時：中央寄せ
    ・2枚以上の時：スマホでも横2列
    ・width: 220 などの数値指定でサイズ変更可能
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

    # 軽量化のためCSSスタイルを一度だけ注入
    st.markdown(f"""
        <style>
        /* 2列横並びを強制 */
        .img-grid-container {{
            display: flex !important;
            flex-direction: row !important;
            justify-content: center !important;
            align-items: center !important;
            gap: 10px !important;
            width: 100% !important;
        }}
        .img-grid-item {{
            flex: 1 !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            min-width: 0 !important;
        }}
        /* st.imageのサイズを上書き制御 */
        .img-grid-item [data-testid="stImage"] {{
            width: {css_w} !important;
            max-width: 100% !important;
        }}
        .img-grid-item [data-testid="stImage"] img {{
            width: 100% !important;
            height: auto !important;
            object-fit: contain !important;
        }}
        </style>
    """, unsafe_allow_html=True)

    # 画像の描画処理
    if len(image_list) == 1:
        found_path = find_image(image_list[0])
        if found_path:
            st.markdown('<div class="img-grid-container"><div class="img-grid-item">', unsafe_allow_html=True)
            st.image(str(found_path))
            st.markdown('</div></div>', unsafe_allow_html=True)
        else:
            st.error(f"画像なし: {Path(image_list[0]).name}")
    else:
        for i in range(0, len(image_list), 2):
            pair = image_list[i:i+2]
            
            if len(pair) == 2:
                img1 = find_image(pair[0])
                img2 = find_image(pair[1])
                
                st.markdown('<div class="img-grid-container">', unsafe_allow_html=True)
                
                # 1枚目
                st.markdown('<div class="img-grid-item">', unsafe_allow_html=True)
                if img1: st.image(str(img1))
                else: st.error(f"なし: {Path(pair[0]).name}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # 2枚目
                st.markdown('<div class="img-grid-item">', unsafe_allow_html=True)
                if img2: st.image(str(img2))
                else: st.error(f"なし: {Path(pair[1]).name}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                # 奇数枚目のラスト1枚
                img1 = find_image(pair[0])
                st.markdown('<div class="img-grid-container"><div class="img-grid-item">', unsafe_allow_html=True)
                if img1: st.image(str(img1))
                else: st.error(f"なし: {Path(pair[0]).name}")
                st.markdown('</div></div>', unsafe_allow_html=True)

    # キャプション
    if caption:
        st.markdown(
            f"<p style='text-align: center; color: gray; font-size: 0.85em; margin-top: 4px; margin-bottom: 12px;'>"
            f"{caption}"
            f"</p>",
            unsafe_allow_html=True
        )
# ----------------------------


#ネイチャーキッズ---------------
display_images_2col(
    image_list=[
        "photo/ネイチャーキッズ/nature_kids.jpg"
    ],
    caption="ネイチャーキッズ特派員",
    width=500
)
#--------------------------------

st.space("medium")

#アジア子ども会議---------------
display_images_2col(
    image_list=[
        "photo/アジアこども会議/asia_conf.jpg","photo/アジアこども会議/asia_conf_1.jpg"
    ],
    caption="アジアこども会議",
    width=300
)
#--------------------------------

st.space("medium")

#子ども国会----------------------
display_images_2col(
    image_list=[
        "photo/こども国会/kids_diet.jpg"
    ],
    caption="こども国会",
    width=300
)
#---------------------------------

st.space("medium")

#English camp----------------------
display_images_2col(
    image_list=[
        "photo/EnglishCamp/english_camp.jpg"
    ],
    caption="Englisg Camp",
    width=300
)
#----------------------------------

st.space("medium")

#ナダレンジャー-------------------------
display_images_2col(
    image_list=[
        "photo/ナダレンジャー/dr1.jpg","photo/ナダレンジャー/dr2.jpg"
    ],
    caption="納口先生の防災イベントの様子",
    width=300
)
#-----------------------------------

st.space("medium")

#自由研究---------------------------
display_images_2col(
    image_list=[
        "photo/自由研究/r1.jpg","photo/自由研究/r2.jpg","photo/自由研究/r3.jpg"
    ],
    caption="茨城県児童生徒科学研究作品展",
    width=300
)
#-----------------------------------

st.space("medium")

#ミクロネシア----------------------
display_images_2col(
    image_list=[
        "photo/ミクロネシア/m1.jpg","photo/ミクロネシア/m2.jpg","photo/ミクロネシア/m3.jpg","photo/ミクロネシア/m4.jpg","photo/ミクロネシア/m5.jpg","photo/ミクロネシア/m6.jpg","photo/ミクロネシア/m7.jpg","photo/ミクロネシア/m8.jpg"
    ],
    caption="ミクロネシア諸島自然体験交流事業",
    width=300
)
#-------------------------------------

st.space("medium")

#中国------------------------------
display_images_2col(
    image_list=[
        "photo/中国/c1.jpg","photo/中国/c2.jpg","photo/中国/c3.jpg","photo/中国/c4.jpg","photo/中国/c5.jpg","photo/中国/c6.jpg","photo/中国/c7.jpg"
    ],
    caption="古河市国際友好交流都市交流会",
    width=300
)
#---------------------------------

st.space("medium")

#2021PVチーム-----------------
display_images_2col(
    image_list=[
        "photo/2021PV/2021PV.jpg","photo/2021PV/pv2.jpg"
    ],
    caption="2021年PVチーム",
    width=300
)
#-----------------------------

st.space("medium")

#2022PVチーム-----------------

display_images_2col(
    image_list=[
        "photo/2022PV/2022PV.jpg"
    ],
    caption="2022年PVチーム",
    width=300
)
#-----------------------------

st.space("medium")

#修学旅行----------------------
display_images_2col(
    image_list=[
        "photo/修学旅行/t1.jpg","photo/修学旅行/t2.jpg","photo/修学旅行/t3.jpg","photo/修学旅行/t4.jpg","photo/修学旅行/t5.jpg"
    ],
    caption="下妻第一高等学校修学旅行",
    width=300
)
#-------------------------------

st.space("medium")

#文化祭----------------------
display_images_2col(
    image_list=[
        "photo/文化祭/f1.jpg","photo/文化祭/f2.jpg","photo/文化祭/f3.jpg","photo/文化祭/f4.jpg","photo/文化祭/f5.jpg","photo/文化祭/f6.jpg","photo/文化祭/f7.jpg","photo/文化祭/f8.jpg","photo/文化祭/f9.jpg","photo/文化祭/f10.jpg","photo/文化祭/f11.jpg","photo/文化祭/f12.jpg"
    ],
    caption="第54回下妻第一高等学校文化祭",
    width=300
)
#-------------------------------

st.space("medium")

#成人式------------------------
display_images_2col(
    image_list=[
        "photo/成人式/ac1.jpg","photo/成人式/ac2.jpg","photo/成人式/ac3.jpg","photo/成人式/ac4.jpg",,"photo/成人式/ac5.jpg","photo/成人式/ac6.jpg"
    ],
    caption="令和8年古河市二十歳のつどい",
    width=300
)
#--------------------------------

st.space("medium")

#ダンデライオン-----------------
display_images_2col(
    image_list=[
        "photo/ダンデライオン/R8姉妹都市交流/d1.jpg"
    ],
    caption="令和8年古河市二十歳のつどい",
    width=300
)
#---------------------------------

st.space("medium")

#アクセルリンク--------------------
display_images_2col(
    image_list=[
        "photo/なせばなる秋祭り/f1.jpg","photo/なせばなる秋祭り/f2.jpg","photo/なせばなる秋祭り/f3.jpg","photo/なせばなる秋祭り/f4.jpg","photo/なせばなる秋祭り/f5.jpg"
    ],
    caption="Accel Link米沢(なせばなる秋祭り)",
    width=300
)