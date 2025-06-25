import streamlit as st
from datetime import datetime, date
import random

# ------------------------ 운세 데이터 ------------------------
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
        "colors": ["빨강", "파랑", "노랑", "초록", "보라", "주황"],
        "numbers": list(range(1, 100)),
        "items": {
            "차/음료": ["허브차", "아메리카노", "라떼", "녹차", "밀크티", "아이스티"],
            "음악": ["재즈", "클래식", "발라드", "팝", "Lo-fi", "힙합"],
            "아이템": ["노트북", "책갈피", "행운의 동전", "열쇠고리", "손목시계"],
            "장소": ["공원", "도서관", "카페", "집", "산책로"]
        }
    },
    # 나머지 분야들도 같은 형식으로 추가 가능
}

zodiacs = [
    "🐭 줄", "🐮 소", "🐯 호랑이", "🐰 토리", "🐲 용", "🐍 밀",
    "🐴 말", "🐑 양", "🐵 원숭이", "🐓 달공", "🐶 개", "🐷 도이지"
]

def get_constellation(month, day):
    signs = [
        ((1, 20), "♒ 미연자리"), ((2, 19), "♓ 물고기자리"),
        ((3, 21), "♈ 양자리"), ((4, 20), "♉ 황소자리"),
        ((5, 21), "♊ 쌍등이자리"), ((6, 22), "♋ 게자리"),
        ((7, 23), "♌ 사자리"), ((8, 23), "♍ 천척자리"),
        ((9, 23), "♎ 천치자리"), ((10, 24), "♏ 전가리"),
        ((11, 23), "♐ 사수자리"), ((12, 25), "♑ 여무소자리")
    ]
    for (start_month, start_day), sign in reversed(signs):
        if (month, day) >= (start_month, start_day):
            return sign
    return "♑ 여무소자리"

# ------------------------ Streamlit UI ------------------------
st.set_page_config(page_title="오늘의 운세", layout="centered")

# 스타일 정의 (흰색 배경 + 운세 카드)
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

st.markdown("<div class='main-block'>", unsafe_allow_html=True)

st.title("🔮 오늘의 운세")

birth_date = st.date_input("생년월일을 입력하세요", min_value=date(1900, 1, 1), max_value=date.today())

if birth_date:
    year, month, day = birth_date.year, birth_date.month, birth_date.day
    zodiac_index = (year - 2020) % 12
    zodiac = zodiacs[zodiac_index]
    constellation = get_constellation(month, day)

    category = st.selectbox("운세 분야를 선택하세요 👇", list(fortune_data.keys()))
    data = fortune_data[category]

    # 시드 고정으로 매일 같은 결과 제공
    random.seed(f"{birth_date}-{date.today().isoformat()}-{category}")

    fortune = random.choice(data["messages"])
    color = random.choice(data["colors"])
    number = random.choice(data["numbers"])
    drink = random.choice(data["items"]["차/음료"])
    music = random.choice(data["items"]["음악"])
    item = random.choice(data["items"]["아이템"])
    place = random.choice(data["items"]["장소"])

    # 결과 출력
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

st.markdown("</div>", unsafe_allow_html=True)
