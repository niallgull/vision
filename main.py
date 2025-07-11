import streamlit as st
from datetime import datetime, date
import random

# 띠 목록
zodiacs = [
    "🐭 쥐", "🐮 소", "🐯 호랑이", "🐰 토끼", "🐲 용", "🐍 뱀",
    "🐴 말", "🐑 양", "🐵 원숭이", "🐔 닭", "🐶 개", "🐷 돼지"
]

# 별자리 함수
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

# 운세 데이터
base_items = {
    "차/음료": ["녹차", "홍차", "아메리카노", "라떼", "자몽차", "레몬차", "유자차", "아이스티", "말차", "허브티"],
    "음악": ["클래식", "재즈", "로파이", "발라드", "인디", "팝", "힙합", "EDM", "뉴에이지", "록"],
    "아이템": ["책", "노트", "펜", "캔들", "손목시계", "지갑", "열쇠고리", "스티커", "헤어핀", "머그컵"],
    "장소": ["카페", "공원", "도서관", "강변", "산책로", "서점", "전시회", "영화관", "베란다", "옥상"]
}

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
    },
    "연애 운세 💘": {
        "messages": [
            "오늘은 사랑이 가까이에 있어요. 눈을 크게 떠보세요!",
            "오래된 인연이 다시 이어질 수 있는 날이에요.",
            "솔직한 표현이 상대에게 큰 감동을 줄 수 있어요.",
            "가벼운 대화에서 진심이 오갈 수 있어요.",
            "첫인상이 좋은 날입니다. 스타일에 신경 써보세요.",
            "감정 표현이 중요한 열쇠가 될 거예요.",
            "상대방의 말을 경청하는 것이 포인트예요.",
            "새로운 만남보다는 기존 관계에 집중해 보세요.",
            "당신의 진심이 통할 가능성이 높아요.",
            "짝사랑이 이루어질 수도 있는 행운의 날!",
        ],
    },
    "금전 운세 💰": {
        "messages": [
            "작은 지출을 아끼면 큰 기쁨이 돌아옵니다.",
            "투자보다 저축에 더 집중해야 하는 날이에요.",
            "기대하지 않았던 수입이 생길 수 있어요.",
            "금전 문제에선 신중한 판단이 중요해요.",
            "지출 계획을 다시 점검해 보세요.",
            "쓸데없는 소비를 줄이면 금전운이 좋아집니다.",
            "중고 거래나 재활용이 돈을 아껴줄 거예요.",
            "금전 관련 문서에 사인할 땐 두 번 확인하세요.",
            "좋은 절약 아이디어가 떠오를 수 있는 날이에요.",
            "작은 행운이 들어올 수 있는 날입니다.",
        ],
    },
    "건강 운세 💪": {
        "messages": [
            "가벼운 운동이 기분 전환에 도움이 돼요.",
            "몸의 작은 신호에 귀를 기울이세요.",
            "스트레칭으로 컨디션을 회복해 보세요.",
            "잠을 충분히 자면 좋은 하루가 될 거예요.",
            "면역력 관리를 위한 식단을 신경 써보세요.",
            "정신 건강도 챙겨야 할 때입니다.",
            "명상이 당신에게 큰 힘이 될 수 있어요.",
            "몸을 따뜻하게 해주는 음식이 좋습니다.",
            "건강검진을 예약해보는 것도 좋겠어요.",
            "햇빛을 쬐며 산책하면 활력이 생겨요.",
        ],
    },
    "일/학업 운세 📚": {
        "messages": [
            "작은 성취가 큰 동기를 줄 수 있는 날입니다.",
            "집중이 잘 되는 날이에요. 공부나 일에 몰입해 보세요.",
            "새로운 아이디어가 떠오를 수 있어요.",
            "계획한 일정을 지키는 것이 포인트입니다.",
            "작은 실수도 꼼꼼히 체크해보세요.",
            "협업보다는 혼자 작업이 더 효율적일 수 있어요.",
            "메모가 도움이 되는 날입니다.",
            "꾸준함이 좋은 결과를 가져올 거예요.",
            "휴식도 일정에 포함시키는 것이 중요해요.",
            "오늘의 노력은 곧 보상으로 돌아올 거예요.",
        ],
    },
    "인간관계 운세 🧑‍🤝‍🧑": {
        "messages": [
            "친구와의 대화에서 힐링을 얻을 수 있어요.",
            "갈등보다 이해에 집중하면 관계가 좋아집니다.",
            "누군가의 조언이 큰 도움이 될 거예요.",
            "오늘은 인맥 확장에 좋은 기회가 있습니다.",
            "진심 어린 사과가 문제를 풀어줄 수 있어요.",
            "가까운 사람일수록 배려가 필요합니다.",
            "팀워크가 성패를 좌우하는 날입니다.",
            "오랜 친구에게 연락해보는 것도 좋아요.",
            "타인의 입장에서 생각해보면 갈등이 줄어들 거예요.",
            "당신의 친절이 누군가의 하루를 밝게 할 거예요.",
        ],
    }
}

# 각 분야에 공통 색상, 숫자, 추천 아이템 추가
for cat in fortune_data.values():
    cat["colors"] = ["빨강", "파랑", "노랑", "초록", "보라", "하늘색", "분홍", "검정", "흰색", "주황"]
    cat["numbers"] = list(range(1, 46))
    cat["items"] = base_items

# 앱 시작
st.title("🔮 오늘의 운세")

birth_date = st.date_input("생년월일을 입력하세요", min_value=date(1900, 1, 1), max_value=date.today())
year, month, day = birth_date.year, birth_date.month, birth_date.day
zodiac_index = (year - 2020) % 12
zodiac = zodiacs[zodiac_index]
constellation = get_constellation(month, day)

category = st.radio("운세 분야를 선택하세요 👇", list(fortune_data.keys()))

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

