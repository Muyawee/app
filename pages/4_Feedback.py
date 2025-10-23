import streamlit as st

st.title("💬 แสดงความคิดเห็นเกี่ยวกับซีรีส์จีน")

name = st.text_input("ชื่อของคุณ:")
platform = st.selectbox("แพลตฟอร์มที่คุณชอบที่สุด", ["iQIYI", "WeTV", "Youku"])
fav = st.text_input("ชื่อซีรีส์ที่คุณประทับใจที่สุด:")
rating = st.slider("ให้คะแนนความพึงพอใจ (1-5)", 1, 5, 3)
comment = st.text_area("รีวิวของคุณ:")

if st.button("ส่งความคิดเห็น"):
    st.success(f"ขอบคุณ {name}! สำหรับความคิดเห็นเกี่ยวกับ {fav} จาก {platform} ⭐ {rating}/5")
    st.write("รีวิวของคุณ:")
    st.write(comment)
