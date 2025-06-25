import streamlit as st
from datetime import datetime
import random

# 띠 정보
zodiacs = [
    "🐭 쥐", "🐮 소", "🐯 호랑이", "🐰 토끼", "🐲 용", "🐍 뱀",
    "🐴 말", "🐑 양", "🐵 원숭이", "🐔 닭", "🐶 개", "🐷 돼지"
]

# 별자리 계산 함수
def get_constellation(month, day):
    signs = [
        ((1, 20), "♒ 물병자리"), ((2, 19), "♓ 물고기자리"), ((3, 21), "♈ 양자리"),
        ((4, 20), "♉ 황소자리"), ((5, 21), "♊ 쌍둥이자리"), ((6, 22), "♋ 게자리"),
        ((7, 23), "♌ 사자자리"), ((8, 23), "♍ 처녀자리"), ((9, 23), "♎ 천칭자리"),
        ((10, 24), "♏ 전갈자리"), ((11, 23), "♐ 사수자리"), ((12, 25), "♑ 염소자리")
    ]
    for (start_month, start_day), sign in reversed(signs):
        if (month, day) >= (start_month, start_day):
            return sign
    return "♑ 염소자리"

# 운세 메시지 모음
fortune_messages = [
    "오늘은 행운의 기운이 가득해요. 작은 도전을 해보세요!",
    "조금은 조심스러운 하루. 중요한 결정은 잠시 미뤄보세요.",
    "뜻밖의 좋은 소식이 찾아올 수도 있어요!",
    "주변 사람들과의 대화가 중요한 날이에요.",
    "오늘은 나 자신을 위해 시간을 써보세요.",
]

# 앱 UI
st.title("🔮 생년월일 운세 앱")

# 생년월일 입력
birth_date = st.date_input("당신의 생년월일을 선택하세요")

# 생년 정보 추출
year = birth_date.year
month = birth_date.month
day = birth_date.day

# 띠 계산 (쥐띠 기준: 2020년)
zodiac_index = (year - 2020) % 12
zodiac = zodiacs[zodiac_index]

# 별자리 계산
constellation = get_constellation(month, day)

# 운세 메시지 선택
random.seed(str(birth_date) + datetime.today().strftime("%Y-%m-%d"))
fortune = random.choice(fortune_messages)

# 결과 출력
st.markdown(f"### 👤 생일: `{birth_date}`")
st.markdown(f"**띠**: {zodiac}")
st.markdown(f"**별자리**: {constellation}")
st.markdown("### 🧧 오늘의 운세")
st.success(fortune)
