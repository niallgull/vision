import streamlit as st
import json
import os
from datetime import date, datetime
import pandas as pd

# 데이터 저장 파일 경로
DATA_FILE = 'schedule_data.json'

# 데이터 불러오기
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

# 데이터 저장하기
def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 앱 제목
st.title("📅 간단한 일정 관리 앱")

# 날짜 선택
selected_date = st.date_input("날짜 선택", value=date.today())
date_str = selected_date.isoformat()

# 데이터 불러오기
data = load_data()

# 메모 입력 영역
memo = st.text_area("메모 입력", value=data.get(date_str, ""), height=150)

# 저장 버튼
if st.button("저장하기"):
    data[date_str] = memo
    save_data(data)
    st.success(f"{date_str} 메모가 저장되었습니다.")

# 오늘 메모 표시
if date_str in data and data[date_str].strip():
    st.subheader("📌 오늘의 메모")
    st.info(data[date_str])

# 이번 달 메모 목록
st.subheader("📆 이번 달 메모 목록")

this_month = selected_date.month
this_year = selected_date.year

# 이번 달에 해당하는 메모만 필터링
monthly_data = {
    d: m for d, m in data.items()
    if datetime.strptime(d, "%Y-%m-%d").year == this_year and datetime.strptime(d, "%Y-%m-%d").month == this_month
}

if monthly_data:
    # DataFrame으로 변환
    df = pd.DataFrame([{"날짜": d, "메모": m} for d, m in sorted(monthly_data.items())])
    st.dataframe(df)

    # CSV로 변환
    csv = df.to_csv(index=False, encoding="utf-8-sig")

    # 다운로드 버튼
    st.download_button(
        label="📥 이번 달 메모 CSV 다운로드",
        data=csv,
        file_name=f"{this_year}-{this_month:02d}-메모.csv",
        mime="text/csv"
    )
else:
    st.write("이번 달에는 작성된 메모가 없습니다.")
