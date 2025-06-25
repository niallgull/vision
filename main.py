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
        ],
        "colors": ["파랑", "하늘색", "흰색"],
        "numbers": list(range(1, 10)),
        "items": {
            "차/음료": ["녹차", "아메리카노", "캐모마일", "유자차"],
            "음악": ["로파이 재즈", "클래식 피아노", "잔잔한 발라드"],
            "아이템": ["책", "아로마 캔들", "이어폰"],
            "장소": ["공원 벤치", "강가 산책로", "조용한 카페"]
        }
    },
    "연애 운세 💘": {
        "messages": [
            "오늘은 사랑이 가까이에 있어요. 눈을 크게 떠보세요!",
            "오래된 인연이 다시 이어질 수 있는 날이에요.",
            "솔직한 표현이 상대에게 큰 감동을 줄 수 있어요.",
            "가벼운 대화에서 진심이 오갈 수 있어요.",
        ],
        "colors": ["분홍", "빨강", "보라"],
        "numbers": [2, 6, 14, 22],
        "items": {
            "차/음료": ["딸기 라떼", "로즈티", "밀크티", "핑크 에이드"],
            "음악": ["달콤한 R&B", "러브송", "로맨틱 재즈"],
            "아이템": ["향수", "립밤", "사진첩"],
            "장소": ["전망 좋은 카페", "놀이공원", "산책길"]
        }
    },
    "금전 운세 💰": {
        "messages": [
            "작은 지출을 아끼면 큰 기쁨이 돌아옵니다.",
            "투자보다 저축에 더 집중해야 하는 날이에요.",
            "기대하지 않았던 수입이 생길 수 있어요.",
            "금전 문제에선 신중한 판단이 중요해요.",
        ],
        "colors": ["초록", "황금", "갈색"],
        "numbers": [4, 8, 18, 28],
        "items": {
            "차/음료": ["보리차", "두유", "블랙 커피", "미숫가루"],
            "음악": ["집중에 좋은 클래식", "조용한 기타곡"],
            "아이템": ["지갑", "저금통", "가계부 앱"],
            "장소": ["서점", "은행 근처 카페", "재테크 세미나"]
        }
    },
    "건강 운세 💪": {
        "messages": [
            "가벼운 운동이 기분 전환에 도움이 돼요.",
            "몸의 작은 신호에 귀를 기울이세요.",
            "스트레칭으로 컨디션을 회복해 보세요.",
            "잠을 충분히 자면 좋은 하루가 될 거예요.",
        ],
        "colors": ["흰색", "회색", "민트"],
        "numbers": [1, 5, 10, 21],
        "items": {
            "차/음료": ["생강차", "레몬워터", "허브티", "디카페인 녹차"],
            "음악": ["명상 음악", "자연의 소리", "힐링 피아노"],
            "아이템": ["물병", "스트레칭 밴드", "요가 매트"],
            "장소": ["헬스장", "산책로", "사우나"]
        }
    },
    "일/학업 운세 📚": {
        "messages": [
            "작은 성취가 큰 동기를 줄 수 있는 날입니다.",
            "집중이 잘 되는 날이에요. 공부나 일에 몰입해 보세요.",
            "새로운 아이디어가 떠오를 수 있어요.",
            "계획한 일정을 지키는 것이 포인트입니다.",
        ],
        "colors": ["파랑", "검정", "남색"],
        "numbers": [3, 9, 12, 24],
        "items": {
            "차/음료": ["아이스 아메리카노", "콜드브루", "청귤차"],
            "음악": ["집중력 향상 음악", "모차르트", "로파이"],
            "아이템": ["타이머", "형광펜", "노트"],
            "장소": ["도서관", "스터디카페", "집 책상"]
        }
    },
    "인간관계 운세 🧑‍🤝‍🧑": {
        "messages": [
            "친구와의 대화에서 힐링을 얻을 수 있어요.",
            "갈등보다 이해에 집중하면 관계가 좋아집니다.",
            "누군가의 조언이 큰 도움이 될 거예요.",
            "오늘은 인맥 확장에 좋은 기회가 있습니다.",
        ],
        "colors": ["노랑", "주황", "베이지"],
        "numbers": [7, 11, 17, 25],
        "items": {
            "차/음료": ["버블티", "망고 스무디", "자몽에이드"],
            "음악": ["밝은 팝", "K-POP", "친구와 공유한 플레이리스트"],
            "아이템": ["휴대폰", "사진첩", "선물 포장지"],
            "장소": ["모임 장소", "카페", "영화관"]
        }
    }
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

