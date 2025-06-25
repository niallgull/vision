# app.py

import streamlit as st
import json
import os
from datetime import date

# 데이터 파일 경로
DATA_FILE = 'schedule_data.json'

# 초기 데이터 로드 또는 생성
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {}

# 데이터 저장
def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 앱 시작
st.title("📅 간단한 일정 관리 앱")

# 날짜 선택
selected_date = st.date_input("날짜를 선택하세요", value=date.today())

# 데이터 로드
data = load_data()
date_str = selected_date.isoformat()

# 메모 입력
memo = st.text_area("메모를 작성하세요", value=data.get(date_str, ""))

# 저장 버튼
if st.button("저장하기"):
    data[date_str] = memo
    save_data(data)
    st.success(f"{selected_date} 메모가 저장되었습니다.")

# 현재 메모 표시
if date_str in data and data[date_str].strip():
    st.subheader("📌 저장된 메모")
    st.info(data[date_str])

