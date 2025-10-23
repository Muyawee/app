import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Chinese Period Series", page_icon="🎎", layout="wide")

# --- สไตล์ตกแต่งเพิ่มเติม (CSS) ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)), 
                      url("https://img.freepik.com/free-vector/chinese-new-year-golden-frame-red-background_1017-42167.jpg");
    background-size: cover;
    background-position: center;
}

h1, h2, h3 {
    font-family: "TH Sarabun New", sans-serif;
    color: #a30b0b;
}

.main-card {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
    border: 2px solid #d4af37;
    max-width: 900px;
    margin: auto;
}

a {
    color: #b22222;
    font-weight: bold;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- ส่วนหัว ---
st.markdown("<h1 style='text-align:center;'>🎎 รวมซีรีส์จีนพีเรียดยอดนิยมจากหลายแพลตฟอร์ม 🎎</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; font-size:20px;'>ยินดีต้อนรับเข้าสู่เว็บแนะนำซีรีส์จีนย้อนยุคสุดคลาสสิก<br>จากแพลตฟอร์มดังอย่าง <b>iQIYI</b>, <b>WeTV</b>, และ <b>Youku</b> 📺</p>", unsafe_allow_html=True)

st.markdown("---")

# --- เนื้อหา (กล่องกลาง) ---
st.markdown("""
<div class="main-card">
    <h3>🌸 ทำไมคนถึงหลงรักซีรีส์จีนพีเรียด?</h3>
    <ul style="font-size:18px; line-height:1.8;">
        <li>เนื้อเรื่องเข้มข้น ผสมประวัติศาสตร์กับแฟนตาซี</li>
        <li>ฉากอลังการ เครื่องแต่งกายงดงามระดับภาพยนตร์</li>
        <li>นักแสดงยอดฝีมือ ถ่ายทอดอารมณ์ได้ลึกซึ้ง</li>
        <li>มีให้ชมหลากหลายแนว ทั้งโรแมนติก ดราม่า แอ็กชัน และแฟนตาซี</li>
    </ul>
    <p style="font-size:18px;">เลือกชมซีรีส์จากแพลตฟอร์มที่คุณชอบได้เลยทางแถบเมนูด้านซ้าย 👈</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- ส่วนท้าย ---
st.markdown(
    """
    <div style='text-align:center; color:#555; font-size:16px; margin-top:40px;'>
    จัดทำโดยนักศึกษาผู้ชื่นชอบซีรีส์จีน ❤️<br>
    © 2025 My Chinese Series Hub
    </div>
    """,
    unsafe_allow_html=True
)
