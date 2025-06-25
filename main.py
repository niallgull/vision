import streamlit as st
from datetime import datetime, date
import random

# 분야별 운세 메시지 사전
fortunes_by_category = {
    "전체 운세 🔮": [
        "오늘은 행운의 기운이 가득해요. 작은 도전을 해보세요!",
        "뜻밖의 기회가 찾아올 수 있어요!",
        "마음의 여유를 가지면 좋은 일이 생겨요.",
        "감사하는 마음이 행운을 불러옵니다.",
    ],
    "연애 운세 💘": [
        "오늘은 사랑이 가까이에 있어요. 눈을 크게 떠보세요!",
        "오래된 인연이 다시 이어질 수 있는 날이에요.",
        "솔직한 표현이 상대에게 큰 감동을 줄 수 있어요.",
        "가벼운 대화에서 진심이 오갈 수 있어요.",
    ],
    "금전 운세 💰": [
        "작은 지출을 아끼면 큰 기쁨이 돌아옵니다.",
        "투자보다 저축에 더 집중해야 하는 날이에요.",
        "기대하지 않았던 수입이 생길 수 있어요.",
        "금전 문제에선 신중한 판단이 중요해요.",
    ],
    "건강 운세 💪": [
        "가벼운 운동이 기분 전환에 도움이 돼요.",
        "몸의 작은 신호에 귀를 기울이세요.",
        "스트레칭으로 컨디션을 회복해 보세요.",
        "잠을 충분히 자면 좋은 하루가 될 거예요.",
    ],
    "일/학업 운세 📚": [
        "작은 성취가 큰 동기를 줄 수 있는 날입니다.",
        "집중이 잘 되는 날이에요. 공부나 일에 몰입해 보세요.",
        "새로운 아이디어가 떠오를 수 있어요.",
        "계획한 일정을 지키는 것이 포인트입니다.",
    ],
    "인간관계 운세 🧑‍🤝‍🧑": [
        "친구와의 대화에서 힐링을 얻을 수 있어요.",
        "갈등보다 이해에 집중하면 관계가 좋아집니다.",
        "누군가의 조언이 큰 도움이 될 거예요.",
        "오늘은 인맥 확장에 좋은 기회가 있습니다.",
    ]
}

# 띠 목록
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

# --- 앱 시작 ---
st.title("🔮 분야별 운세 보기")

# 생년월일 입력
birth_date = st.date_input(
    "당신의 생년월일을 선택하세요",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

# 띠와 별자리 계산
year, month, day = birth_date.year, birth_date.month, birth_date.day
zodiac_index = (year - 2020) % 12
zodiac = zodiacs[zodiac_index]
constellation = get_constellation(month, day)

# 분야 선택
category = st.selectbox("보고 싶은 운세 분야를 선택하세요 👇", list(fortunes_by_category.keys()))

# 운세 선택 (seed 고정)
random.seed(f"{birth_date}-{date.today().isoformat()}-{category}")
fortune = random.choice(fortunes_by_category[category])

# 결과 출력
st.markdown(f"### 👤 생년월일: `{birth_date}`")
st.markdown(f"**띠**: {zodiac}")
st.markdown(f"**별자리**: {constellation}")
st.markdown(f"### 📌 {category} 운세")
st.success(fortune)

