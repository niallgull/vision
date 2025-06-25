import streamlit as st
import json
import os
from datetime import date, datetime
import pandas as pd

DATA_FILE = 'schedule_data.json'

# 데이터 로드/저장 함수
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 앱 시작
st.title("📅 간단한 일정 관리 앱")

# 날짜 선택
selected_date = st.date_input("날짜 선택", value=date.today())
data = load_data()
date_str = selected_date.isoformat()

# 메모 입력
memo = st.text_area("메모 작성", value=data.get(date_str, ""))

if st.button("저장하기"):
    data[date_str] = memo
    save_data(data)
    st.success(f"{selected_date} 메모가 저장되었습니다.")

# 오늘의 메모
if date_str in data and data[date_str].strip():
    st.subheader("📌 오늘의 메모")
    st.info(data[date_str])

# 이번 달 메모 필터링
st.subheader("📆 이번 달 작성된 메모")

this_month = selected_date.month
this_year = selected_date.year

monthly_data = {
    d: m for d, m in data.items()
    if datetime.fromisoformat(d).month == this_month and datetime.fromisoformat(d).year == this_year
}

if monthly_data:
    df = pd.DataFrame(
        [{"날짜": d, "메모": m} for d, m in sorted(monthly_data.items())]
    )
    st.dataframe(df)

    # ✅ CSV 다운로드 버튼
    csv = df.to_csv(index=False, encoding='utf-8-sig')
    st.download_button(
        label="📥 이번 달 메모 CSV 다운로드",
        data=csv,
        file_name=f"{this_year}-{this_month:02d}-메모.csv",
        mime='text/csv'
    )
else:
    st.write("이번 달에는 작성된 메모가 없습니다.")

    st.dataframe(df)
else:
    st.write("이번 달에는 작성된 메모가 없습니다.")

