import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="活動記録",page_icon="📷️")
st.title("過去の活動記録")
st.write("個人情報保護のため、人が写っている写真にはモザイク処理がかかっています。ご了承ください")

#関数定義------------
def display_images_2col(image_list, caption="", width="100%"):
    """
    ・1枚の時：画面中央に配置
    ・2枚以上の時：スマホでも横2列で並べる
    ・width: 220, 150 などの数値、または "180px", "80%" で確実にサイズ変更可能
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

    # 画像ファイルをHTML埋め込み用（Base64）に変換する関数
    def get_img_html(file_path, style_str=""):
        try:
            with open(file_path, "rb") as f:
                encoded = base64.b64encode(f.read()).decode()
            ext = file_path.suffix.lower().replace(".", "")
            ext = "jpeg" if ext in ["jpg", "jpeg"] else ext
            src = f"data:image/{ext};base64,{encoded}"
            return f'<img src="{src}" style="{style_str}" />'
        except Exception as e:
            return f'<span style="color:red;">画像読み込みエラー</span>'

    # --- width の指定（数値・文字列）を CSS 用の文字列に変換 ---
    if isinstance(width, (int, float)):
        css_w = f"{int(width)}px"
    else:
        css_w = width if (width.endswith("%") or width.endswith("px")) else f"{width}px"

    # 画像に適用する共通のスタイル（幅を固定し、親枠からはみ出さないように設定）
    img_style = f"width: {css_w}; max-width: 100%; height: auto; object-fit: contain; border-radius: 4px;"

    # -------------------------------------------------------------
    # パターンA：画像が1枚だけの場合（中央寄せ表示）
    # -------------------------------------------------------------
    if len(image_list) == 1:
        found_path = find_image(image_list[0])
        if found_path:
            img_tag = get_img_html(found_path, img_style)
            # 全体を中央寄せするHTML
            html_code = f"""
            <div style="display: flex; justify-content: center; align-items: center; width: 100%; margin: 8px 0;">
                {img_tag}
            </div>
            """
            st.markdown(html_code, unsafe_allow_html=True)
        else:
            st.error(f"画像なし: {Path(image_list[0]).name}")

    # -------------------------------------------------------------
    # パターンB：画像が2枚以上の場合（スマホでも横2列を維持）
    # -------------------------------------------------------------
    else:
        for i in range(0, len(image_list), 2):
            pair = image_list[i:i+2]
            
            # 2枚並べる行の描画
            if len(pair) == 2:
                img1_path = find_image(pair[0])
                img2_path = find_image(pair[1])
                
                tag1 = get_img_html(img1_path, img_style) if img1_path else f"画像なし: {Path(pair[0]).name}"
                tag2 = get_img_html(img2_path, img_style) if img2_path else f"画像なし: {Path(pair[1]).name}"
                
                # 2列均等配置のHTML（スマホでも折り返さず2列を維持）
                html_code = f"""
                <div style="display: flex; flex-direction: row; justify-content: center; align-items: center; gap: 12px; width: 100%; margin: 8px 0;">
                    <div style="flex: 1; display: flex; justify-content: center; min-width: 0;">{tag1}</div>
                    <div style="flex: 1; display: flex; justify-content: center; min-width: 0;">{tag2}</div>
                </div>
                """
                st.markdown(html_code, unsafe_allow_html=True)
                
            # 端数（最後の1枚）になった場合は中央寄せ
            else:
                img_path = find_image(pair[0])
                if img_path:
                    tag = get_img_html(img_path, img_style)
                    html_code = f"""
                    <div style="display: flex; justify-content: center; align-items: center; width: 100%; margin: 8px 0;">
                        {tag}
                    </div>
                    """
                    st.markdown(html_code, unsafe_allow_html=True)
                else:
                    st.error(f"画像なし: {Path(pair[0]).name}")

    # キャプション（共通）
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
        "photo/修学旅行/t1.jpg","photo/修学旅行/t2.jpg","photo/修学旅行/t3.jpg","photo/修学旅行/t4.jpg"
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

#R6姉妹都市交流会---------------
display_images_2col(
    image_list=[
        "photo/ダンデライオン/R6姉妹都市交流/d1.jpg","photo/ダンデライオン/R6姉妹都市交流/d2.jpg","photo/ダンデライオン/R6姉妹都市交流/d3.jpg"
    ],
    caption="R6年度姉妹都市交流会",
    width=300
)
#------------------------------

st.space("medium")

#夢あんどん-------------------
display_images_2col(
    image_list=[
        "photo/ダンデライオン/夢あんどん/d1.jpg","photo/ダンデライオン/夢あんどん/d2.jpg","photo/ダンデライオン/夢あんどん/d3.jpg","photo/ダンデライオン/夢あんどん/d4.jpg"
    ],
    caption="夢あんどんと夕涼み(ダンデライオン)",
    width=300
)
#-----------------------------------

st.space("medium")

#成人式------------------------
display_images_2col(
    image_list=[
        "photo/成人式/ac1.jpg","photo/成人式/ac2.jpg","photo/成人式/ac3.jpg","photo/成人式/ac4.jpg","photo/成人式/ac5.jpg","photo/成人式/ac6.jpg"
    ],
    caption="令和8年古河市二十歳のつどい",
    width=300
)
#--------------------------------

st.space("medium")

#R7姉妹都市交流会-----------------
display_images_2col(
    image_list=[
        "photo/ダンデライオン/R7姉妹都市交流/d1.jpg","photo/ダンデライオン/R7姉妹都市交流/d2.jpg","photo/ダンデライオン/R7姉妹都市交流/d3.jpg","photo/ダンデライオン/R7姉妹都市交流/d4.jpg","photo/ダンデライオン/R7姉妹都市交流/d5.jpg"
    ],
    caption="R7年度姉妹都市交流会",
    width=300
)
#-----------------------------------

st.space("medium")

#R8姉妹都市交流会-----------------
display_images_2col(
    image_list=[
        "photo/ダンデライオン/R8姉妹都市交流/d1.jpg","photo/ダンデライオン/R8姉妹都市交流/d2.jpg","photo/ダンデライオン/R8姉妹都市交流/d3.jpg","photo/ダンデライオン/R8姉妹都市交流/d4.jpg"
    ],
    caption="R8年度姉妹都市交流会",
    width=300
)
#---------------------------------

st.space("medium")

#親睦キャンプ---------------------
display_images_2col(
    image_list=[
        "photo/ダンデライオン/親睦キャンプ/d1.jpg","photo/ダンデライオン/親睦キャンプ/d2.jpg","photo/ダンデライオン/親睦キャンプ/d3.jpg","photo/ダンデライオン/親睦キャンプ/d4.jpg"
    ],
    caption="親睦キャンプ",
    width=300
)
#----------------------------------

st.space("medium")

#アクセルリンク--------------------
display_images_2col(
    image_list=[
        "photo/なせばなる秋祭り/f1.jpg","photo/なせばなる秋祭り/f2.jpg","photo/なせばなる秋祭り/f3.jpg","photo/なせばなる秋祭り/f4.jpg","photo/なせばなる秋祭り/f5.jpg"
    ],
    caption="Accel Link米沢(なせばなる秋祭り)",
    width=300
)