import os
import platform
import pytesseract
import streamlit as st
from PIL import Image  # <-- This fixes the error in image_ad96da.png

# Dynamically handle Windows vs. Linux paths for Tesseract
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )
else:
    # On Streamlit Cloud (Linux), it will find the global system binary automatically
    pytesseract.pytesseract.tesseract_cmd = "tesseract"


# ==========================================
# 2. WEB APP LAYOUT & DESIGN
# ==========================================
# Page ka title aur icon set karein
st.set_page_config(page_title="AI Image Text Extractor", page_icon="📝", layout="centered")

# Main Headings
st.title("📝 AI Image Text Extractor (OCR)")
st.write("Apni image upload karein aur usme se text extract karein!")

st.divider() # Ek khoobsurat line separate karne ke liye

# File Uploader Widget (Jahan user image drag & drop karega)
uploaded_file = st.file_uploader("Koi bhi image select karein (PNG, JPG, JPEG)...", type=["png", "jpg", "jpeg"])

# ==========================================
# 3. OCR PROCESSING
# ==========================================
if uploaded_file is not None:
    # 1. Image ko screen par dikhane ke liye open karein
    image = Image.open(uploaded_file)
    
    # Do columns banate hain: Ek taraf image, ek taraf text
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📸 Uploaded Image")
        st.image(image, use_container_width=True)
        
    with col2:
        st.subheader("🔍 Extracted Text")
        
        # Loader dikhayein jab tak Tesseract parh raha hai
        with st.spinner("Image se text read kiya ja raha hai..."):
            try:
                # Tesseract se text extract karein
                extracted_text = pytesseract.image_to_string(image)
                
                if extracted_text.strip():
                    # Text ko aik box mein display karein
                    st.text_area(label="Result:", value=extracted_text, height=300)
                    
                    # BONUS: Text download karne ka button
                    st.download_button(
                        label="📥 Download Text File",
                        data=extracted_text,
                        file_name="extracted_text.txt",
                        mime="text/plain"
                    )
                else:
                    st.warning("Image mein koi text nahi mila ya image saaf nahi hai.")
                    
            except Exception as e:
                st.error(f"Kuch masla hua hai: {e}")
