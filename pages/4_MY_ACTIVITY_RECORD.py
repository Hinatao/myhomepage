import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="活動記録",page_icon="📷️")
st.title("過去の活動記録")
st.write("個人情報保護のため、人が写っている写真にはモザイク処理がかかっています。ご了承ください")

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

#新関数定義------------
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
#サイズ変更コード------
    # ★2. 数値（例: 220）が渡された場合は "220px" の文字列に変換
    css_width = f"{width}px" if isinstance(width, (int, float)) else str(width)

    # ★3. 渡された width をCSSの max-width に適用して画像サイズをコントロール
    st.html(f"""
        <style>
        [data-testid="stHorizontalBlock"] {{
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            gap: 8px !important;
            justify-content: center !important;
        }}
        [data-testid="stHorizontalBlock"] > div {{
            min-width: 0 !important;
            display: flex !important;
            justify-content: center !important;
        }}
        /* width で指定されたサイズを上限にして中央配置 */
        [data-testid="stHorizontalBlock"] img {{
            max-width: {css_width} !important;
            width: 100% !important;
            height: auto !important;
            object-fit: contain;
        }}
        </style>
    """)
    #--------------------
    
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
    width="100%"
)
#--------------------------------
st.space("medium")
#アジア子ども会議---------------
display_images_2col(
    image_list=[
        "photo/asia_conf.jpg","photo/asia_conf_1.jpg"
    ],
    caption="アジアこども会議",
    width="100%"
)
#--------------------------------