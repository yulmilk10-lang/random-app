import random
import streamlit as st

# 페이지 기본 설정 (탭 제목 및 아이콘)
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱")

# 앱 제목과 설명
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("결정 장애 해결! 아래 버튼을 눌러 오늘 먹을 점심을 추천받아 보세요.")

# 추천할 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정하세요)
lunch_menus = [
    "김치찌개 🍲",
    "된장찌개 🥘",
    "제육볶음 🥩",
    "돈가스 🍛",
    "짜장면 🍜",
    "짬뽕 🌶️",
    "초밥 🍣",
    "햄버거 🍔",
    "국밥 🍚",
    "비빔밥 🥗",
    "파스타 🍝",
    "쌀국수 🍲",
    "샌드위치 🥪",
    "떡볶이 🍢",
    "마라탕 🥘",
]

st.divider()  # 구분선

# 버튼을 생성하고, 클릭했을 때 실행될 동작 정의
if st.button("🎲 오늘의 메뉴 추천받기", type="primary", use_container_width=True):
    # random.choice()를 사용하여 리스트에서 무작위로 1개 선택
    selected_menu = random.choice(lunch_menus)

    # 결과 출력
    st.success(f"오늘의 추천 점심 메뉴는 **[{selected_menu}]** 입니다! 맛있게 드세요! 😋")
    st.balloons()  # 축하 풍선 애니메이션 효과
