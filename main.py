import streamlit as st
from datetime import datetime, date
import random

# 분야별 데이터
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
        "colors": ["빨강", "파랑", "노랑", "초록", "보라", "하늘색", "분홍", "검정", "흰색", "주황"],
        "numbers": [1, 3, 5, 7, 9, 11, 21, 24, 33, 42],
        "items": {
            "차/음료": ["녹차", "홍차", "아메리카노", "라떼", "자몽차", "레몬차", "유자차", "아이스티", "말차", "허브티"],
            "음악": ["클래식", "재즈", "로파이", "발라드", "인디", "팝", "힙합", "EDM", "뉴에이지", "록"],
            "아이템": ["책", "노트", "펜", "캔들", "손목시계", "지갑", "열쇠고리", "스티커", "헤어핀", "머그컵"],
            "장소": ["카페", "공원", "도서관", "강변", "산책로", "서점", "전시회", "영화관", "베란다", "옥상"]
        }
    },
    # 나머지 분야들도 같은 방식으로 복사해 넣으시면 됩니다
    # 위 코드에서는 "전체 운세 🔮"만 예시로 넣었습니다
}

zodiacs = [
    "🐭 쥐", "🐮 소", "🐯 호랑이", "🐰 토끼", "🐲 용", "🐍 뱀",
    "🐴 말", "🐑 양", "🐵 원숭이", "🐔 닭", "🐶 개", "🐷 돼지"
]

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

# 앱 시작
st.title("🔮 오늘의 운세")

birth_date = st.date_input("생년월일을 입력하세요", min_value=date(1900, 1, 1), max_value=date.today())

year, month, day = birth_date.year, birth_date.month, birth_date.day
zodiac_index = (year - 2020) % 12
zodiac = zodiacs[zodiac_index]
constellation = get_constellation(month, day)

category = st.selectbox("운세 분야를 선택하세요 👇", list(fortune_data.keys()))
data = fortune_data[category]
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

