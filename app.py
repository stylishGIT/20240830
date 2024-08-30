import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# 앱 제목
st.title("상담 예약 앱")

# 사용자 입력
st.header("상담 예약 정보 입력")

name = st.text_input("이름")
email = st.text_input("이메일")
date = st.date_input("상담 날짜", datetime.now() + timedelta(days=1))
time = st.time_input("상담 시간", datetime.now().time())

# 예약 버튼
if st.button("예약하기"):
    if name and email:
        # 예약 정보를 DataFrame에 저장 (예: CSV 파일로 변환)
        reservation_info = {
            "이름": [name],
            "이메일": [email],
            "상담 날짜": [date],
            "상담 시간": [time]
        }
        df = pd.DataFrame(reservation_info)

        # CSV 파일로 저장 (여기서는 로컬에 저장하는 예시)
        df.to_csv("reservations.csv", mode='a', header=False, index=False)

        st.success("예약이 완료되었습니다!")
    else:
        st.error("이름과 이메일을 입력해 주세요.")

# 예약 확인 버튼
if st.button("예약 확인"):
    try:
        reservations = pd.read_csv("reservations.csv")
        st.write(reservations)
    except FileNotFoundError:
        st.error("예약 내역이 없습니다.")
