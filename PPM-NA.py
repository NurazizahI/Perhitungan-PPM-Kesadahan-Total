import streamlit as st

st.title('Perhitungan Nilai PPM Kesadahan Total')
    
Molaritas = st.number_input('Masukan Nilai Molaritas Titran (mmol/ml)')
Volume1 = st.number_input('Masukan Nilai Volume Titran (ml)')
BM = st.number_input('Masukan Nilai BM (mg/mmol)')
FP = st.number_input('Masukan Nilai FP')
Volume2 = st.number_input('Masukan Nilai Volume Sampel (L)')
Hitung = st.button('Hitung Nilai PPM Kesadahan Total')
    
if Hitung:
    Nilai_PPM_Kesadahan_Total2 = (Molaritas*Volume1*BM*FP)/Volume2
    st.success(f'Nilai PPM Kesadahan Total Adalah {Nilai_PPM_Kesadahan_Total2} mg/L')