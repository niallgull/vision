import streamlit as st
from datetime import datetime, date
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
    "조심은 미덕이에요. 오늘은 차분히 보내세요.",
    "뜻밖의 기회가 찾아올 수 있어요!",
    "주변 사람들과 좋은 대화가 생길 수 있는 날입니다.",
    "스스로에게 집중해 보세요. 자기 관리에 좋은 하루입니다.",
]

# 앱 UI
st.title("🔮 생년월일 운세 앱")

# 생년월일 입력 (1900년 ~ 오늘까지 가능)
birth_date = st.date_input(
    "당신의 생년월일을 선택하세요",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

# 날짜 정보 추출
year = birth_date.year
month = birth_date.month
day = birth_date.day

# 띠 계산 (쥐띠 기준: 2020년)
zodiac_index = (year - 2020) % 12
zodiac = zodiacs[zodiac_index]

# 별자리 계산
constellation = get_constellation(month, day)

# 운세 메시지 고정되게 랜덤 생성 (매일 같은 결과)
random.seed(str(birth_date) + date.today().isoformat())
fortune = random.choice(fortune_messages)

# 결과 출력
st.markdown(f"### 👤 생일: `{birth_date}`")
st.markdown(f"**띠**: {zodiac}")
st.markdown(f"**별자리**: {constellation}")
st.markdown("### 🧧 오늘의 운세")
st.success(fortune)
