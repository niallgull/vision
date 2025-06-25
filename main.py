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
    "오늘은 작은 행운이 따를 거예요. 기대해 보세요!",
    "예상치 못한 기회가 찾아올 수 있어요. 열린 마음으로 받아들이세요.",
    "조용히 집중하면 큰 성과가 있는 날이에요.",
    "사소한 말 한마디가 큰 힘이 될 수 있어요.",
    "오늘은 과감한 결정보다 신중함이 필요해요.",
    "소중한 사람과의 인연이 깊어질 수 있어요.",
    "마음의 여유를 가지면 좋은 일이 생겨요.",
    "새로운 것을 시작하기에 좋은 날입니다.",
    "오늘은 실수도 배움이 될 수 있어요.",
    "감정 조절이 중요한 하루예요. 차분하게 대처하세요.",
    "노력의 결실이 조금씩 보이기 시작합니다.",
    "하던 일을 멈추고 자신을 돌아보는 시간을 가져보세요.",
    "오늘은 재정적인 면에서 좋은 기회가 있을 수 있어요.",
    "주변 사람들과의 관계에 신경 쓰면 좋은 결과를 얻어요.",
    "직감이 잘 맞는 날이니 느낌을 믿어보세요.",
    "작은 실수는 금방 회복됩니다. 너무 걱정하지 마세요.",
    "당신의 성실함이 오늘 빛을 발할 거예요.",
    "가벼운 운동이나 산책이 행운을 불러올 수 있어요.",
    "자기 표현에 솔직하면 의외의 지지를 받게 될 수 있어요.",
    "의외의 사람에게서 도움을 받을 수 있는 하루예요.",
    "오늘은 속도보다 방향이 더 중요해요.",
    "감사하는 마음이 행운을 불러옵니다.",
    "하고 싶었던 일을 시작할 수 있는 좋은 기회예요.",
    "느림 속에서도 의미를 발견할 수 있는 날이에요.",
    "평소보다 더 신중한 선택이 필요할 수 있어요.",
    "소소한 즐거움이 큰 행복으로 이어질 수 있어요.",
    "과거보다 현재에 집중하세요. 오늘이 가장 소중합니다.",
    "마음먹기에 따라 하루가 달라질 수 있어요.",
    "그동안 쌓아온 노력에 대한 보답이 찾아와요.",
    "당신의 따뜻한 말 한마디가 누군가에게 큰 힘이 됩니다.",
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
