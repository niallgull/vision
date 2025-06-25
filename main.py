import streamlit as st
from datetime import datetime, date
import random

# 👉 스타일 추가
st.markdown("""
    <style>
    .stApp {
        background-color: white;
    }
    .main-block {
        background-color: rgba(255, 255, 255, 0.98);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        max-width: 700px;
        margin: 3rem auto;
    }
    </style>
""", unsafe_allow_html=True)


# 데이터 준비
zodiacs = ["🐭 쥐", "🐮 소", "🐯 호랑이", "🐰 토끼", "🐲 용", "🐍 뱀",
           "🐴 말", "🐑 양", "🐵 원숭이", "🐔 닭", "🐶 개", "🐷 돼지"]

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

# 운세 데이터 예시
fortune_data = {
    "전체 운세 🔮": {
        "messages": [
            "오늘은 행운의 기운이 가득해요. 작은 도전을 해보세요!",
            "뜻밖의 기회가 찾아올 수 있어요!",
            "마음의 여유를 가지면 좋은 일이 생겨요.",
            "감사하는 마음이 행운을 불러옵니다.",
            "새로운 시작에 좋은 날입니다.",
            "포기하지 않으면 예상치 못한 성과가 따라옵니다.",
            "당신의 노력이 빛을 발할 거예요.",
            "잠시 멈춰 돌아보는 여유를 가져보세요.",
            "운이 당신 편이에요. 망설이지 마세요.",
            "작은 친절이 큰 행운을 부를 수 있어요.",
        ],
        "colors": ["빨강", "파랑", "노랑", "초록", "보라", "검정", "하늘색"],
        "numbers": list(range(1, 100)),
        "items": {
            "차/음료": ["캐모마일 티", "아이스 아메리카노", "유자차", "홍차", "딸기 스무디", "레몬워터"],
            "음악": ["재즈", "클래식", "팝", "로파이", "힙합"],
            "아이템": ["향초", "행운의 동전", "손수건", "메모장", "책갈피"],
            "장소": ["공원", "서점", "카페", "강변", "도서관"]
        }
    },
    # 다른 분야들도 같은 구조로 추가 가능
}

# 앱 제목
st.title("🔮 오늘의 운세")

# 날짜 입력
birth_date = st.date_input("생년월일을 입력하세요", min_value=date(1900, 1, 1), max_value=date.today())

# 정보 계산
year, month, day = birth_date.year, birth_date.month, birth_date.day
zodiac_index = (year - 2020) % 12
zodiac = zodiacs[zodiac_index]
constellation = get_constellation(month, day)

# 분야 선택
category = st.selectbox("운세 분야를 선택하세요 👇", list(fortune_data.keys()))
data = fortune_data[category]
random.seed(f"{birth_date}-{date.today().isoformat()}-{category}")

# 운세 요소 추출
fortune = random.choice(data["messages"])
color = random.choice(data["colors"])
number = random.choice(data["numbers"])
drink = random.choice(data["items"]["차/음료"])
music = random.choice(data["items"]["음악"])
item = random.choice(data["items"]["아이템"])
place = random.choice(data["items"]["장소"])

# 결과 출력 (카드 안)
st.markdown('<div class="main-block">', unsafe_allow_html=True)

st.markdown(f"### 👤 생년월일: `{birth_date}`")
st.markdown(f"**띠**: {zodiac}")
st.markdown(f"**별자리**: {constellation}")

st.markdown(f"### 📌 {category}")
st.success(fortune)
st.markdown("---")
st.markdown(f"🎨 **오늘의 행운 색상:** `{color}`")
st.markdown(f"🔢 **행운의 숫자:** `{number}`")

st.markdown("### 🎁 추천 아이템")
st.markdown(f"🍹 차/음료: **{drink}**")
st.markdown(f"🎵 음악: **{music}**")
st.markdown(f"💐 아이템: **{item}**")
st.markdown(f"📍 장소: **{place}**")

st.markdown('</div>', unsafe_allow_html=True)
