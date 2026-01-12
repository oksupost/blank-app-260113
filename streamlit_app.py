import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date, time

# 페이지 설정 / Page Configuration
st.set_page_config(
    page_title="Streamlit UI 요소 예시",
    page_icon="🎈",
    layout="wide"
)

# ============================================================================
# 1. 텍스트 요소 / TEXT ELEMENTS
# ============================================================================
st.title("🎈 Streamlit UI 요소 전체 예시")

st.header("1. 텍스트 및 제목 요소")
# st.title - 가장 큰 제목 (페이지 최상단에 주로 사용)
st.subheader("1-1. 부제목 / Subheader")
st.write("일반 텍스트입니다. 마크다운을 지원합니다. **굵게**, *이탤릭*, `코드`")
st.caption("📌 작은 회색 텍스트 (캡션)")
st.text("순수 텍스트 (마크다운 미지원)")

# ============================================================================
# 2. 입력 요소 / INPUT ELEMENTS
# ============================================================================
st.header("2. 입력 요소")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("2-1. 버튼")
    if st.button("클릭하세요! 👆", key="btn1"):
        st.write("✅ 버튼이 클릭되었습니다!")

with col2:
    st.subheader("2-2. 체크박스")
    agree = st.checkbox("동의합니다", value=False)
    st.write(f"동의 상태: {agree}")

with col3:
    st.subheader("2-3. 라디오 버튼")
    choice = st.radio("선택하세요:", ["옵션1", "옵션2", "옵션3"])
    st.write(f"선택됨: {choice}")

# 행 분리
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("2-4. 셀렉트박스 (드롭다운)")
    selected = st.selectbox("항목을 선택하세요:", ["사과", "바나나", "포도", "딸기"])
    st.write(f"선택된 항목: {selected}")

with col2:
    st.subheader("2-5. 멀티셀렉트")
    multi_select = st.multiselect("여러 항목을 선택하세요:", ["Python", "JavaScript", "Java", "Go"])
    st.write(f"선택된 언어: {multi_select}")

st.divider()

st.subheader("2-6. 텍스트 입력")
name = st.text_input("이름을 입력하세요:", placeholder="예: 홍길동")
st.write(f"입력된 이름: {name}")

st.subheader("2-7. 텍스트 영역 (여러 줄)")
message = st.text_area("메시지를 입력하세요:", height=100)
st.write(f"입력된 메시지: {message}")

# ============================================================================
# 3. 숫자 입력 요소 / NUMBER INPUT ELEMENTS
# ============================================================================
st.header("3. 숫자 입력 요소")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("3-1. 슬라이더")
    slider_value = st.slider("값을 선택하세요:", 0, 100, 50)
    st.write(f"선택된 값: {slider_value}")

with col2:
    st.subheader("3-2. 숫자 입력")
    number = st.number_input("숫자를 입력하세요:", value=0, step=1)
    st.write(f"입력된 숫자: {number}")

with col3:
    st.subheader("3-3. 범위 슬라이더")
    range_values = st.slider("범위를 선택하세요:", 0, 100, (20, 80))
    st.write(f"선택된 범위: {range_values}")

# ============================================================================
# 4. 날짜/시간 요소 / DATE/TIME ELEMENTS
# ============================================================================
st.header("4. 날짜 및 시간 요소")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("4-1. 날짜 선택")
    selected_date = st.date_input("날짜를 선택하세요:", value=date.today())
    st.write(f"선택된 날짜: {selected_date}")

with col2:
    st.subheader("4-2. 시간 선택")
    selected_time = st.time_input("시간을 선택하세요:", value=time(12, 0))
    st.write(f"선택된 시간: {selected_time}")

with col3:
    st.subheader("4-3. 색상 선택")
    color = st.color_picker("색상을 선택하세요:", "#00f900")
    st.write(f"선택된 색상: {color}")

# ============================================================================
# 5. 파일 업로드 / FILE UPLOADER
# ============================================================================
st.header("5. 파일 업로드")
uploaded_file = st.file_uploader("파일을 업로드하세요:", type=["csv", "xlsx", "json", "txt"])
if uploaded_file is not None:
    st.write(f"업로드된 파일: {uploaded_file.name}")

# ============================================================================
# 6. 데이터 표시 요소 / DATA DISPLAY ELEMENTS
# ============================================================================
st.header("6. 데이터 표시 요소")

# 샘플 데이터 생성
df = pd.DataFrame({
    "이름": ["Alice", "Bob", "Charlie", "David"],
    "나이": [25, 30, 35, 28],
    "도시": ["서울", "부산", "대구", "인천"],
    "급여": [50000, 60000, 70000, 55000]
})

st.subheader("6-1. 데이터프레임 (테이블)")
st.dataframe(df, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("6-2. 메트릭 (KPI)")
    st.metric(label="총 판매액", value="$100,000", delta="+5%")

with col2:
    st.subheader("6-3. 프로그래스 바")
    progress = st.progress(65, text="완료도 65%")

# ============================================================================
# 7. 차트 요소 / CHART ELEMENTS
# ============================================================================
st.header("7. 차트 요소")

# 차트용 샘플 데이터
chart_data = pd.DataFrame({
    "월": ["1월", "2월", "3월", "4월", "5월"],
    "판매": [100, 200, 150, 300, 250],
    "비용": [80, 120, 100, 180, 160]
})

col1, col2 = st.columns(2)

with col1:
    st.subheader("7-1. 라인 차트")
    st.line_chart(chart_data.set_index("월"))

with col2:
    st.subheader("7-2. 바 차트")
    st.bar_chart(chart_data.set_index("월"))

col1, col2 = st.columns(2)

with col1:
    st.subheader("7-3. 에어리어 차트")
    st.area_chart(chart_data.set_index("월"))

with col2:
    st.subheader("7-4. 산점도")
    scatter_data = pd.DataFrame(
        np.random.randn(100, 2),
        columns=['X', 'Y']
    )
    st.scatter_chart(scatter_data)

# ============================================================================
# 8. 코드/JSON 표시 / CODE/JSON DISPLAY
# ============================================================================
st.header("8. 코드 및 JSON 표시")

col1, col2 = st.columns(2)

with col1:
    st.subheader("8-1. 코드 블록")
    st.code("""
def hello(name):
    return f"Hello, {name}!"

print(hello("Streamlit"))
    """, language="python")

with col2:
    st.subheader("8-2. JSON 표시")
    json_data = {
        "이름": "홍길동",
        "나이": 30,
        "도시": "서울"
    }
    st.json(json_data)

# ============================================================================
# 9. 컨테이너 요소 / CONTAINER ELEMENTS
# ============================================================================
st.header("9. 컨테이너 및 레이아웃")

st.subheader("9-1. 익스펜더 (토글 가능한 섹션)")
with st.expander("📖 더 보기를 클릭하세요"):
    st.write("숨겨진 콘텐츠입니다!")
    st.image("https://via.placeholder.com/400x200", caption="플레이스홀더 이미지")

st.subheader("9-2. 컨테이너")
container = st.container(border=True)
with container:
    st.write("테두리가 있는 컨테이너입니다")
    st.bar_chart({"데이터": [1, 2, 3, 4, 5]})

st.subheader("9-3. 탭")
tab1, tab2, tab3 = st.tabs(["탭1", "탭2", "탭3"])

with tab1:
    st.write("탭1의 콘텐츠입니다")
    st.button("탭1 버튼")

with tab2:
    st.write("탭2의 콘텐츠입니다")
    st.slider("탭2 슬라이더", 0, 100)

with tab3:
    st.write("탭3의 콘텐츠입니다")
    st.text_input("탭3 입력창")

# ============================================================================
# 10. 사이드바 / SIDEBAR
# ============================================================================
st.sidebar.header("⚙️ 사이드바 설정")
st.sidebar.write("사이드바에 위젯을 추가할 수 있습니다")

sidebar_option = st.sidebar.selectbox("옵션을 선택하세요:", ["옵션A", "옵션B", "옵션C"])
st.sidebar.write(f"선택된 옵션: {sidebar_option}")

sidebar_value = st.sidebar.slider("사이드바 슬라이더:", 0, 100, 50)
st.sidebar.metric("사이드바 메트릭", "75%")

# ============================================================================
# 11. 경고 및 상태 메시지 / ALERTS & STATUS
# ============================================================================
st.header("10. 경고 및 상태 메시지")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.success("✅ 성공 메시지")

with col2:
    st.info("ℹ️ 정보 메시지")

with col3:
    st.warning("⚠️ 경고 메시지")

with col4:
    st.error("❌ 에러 메시지")

# ============================================================================
# 12. 기타 유용한 요소 / MISCELLANEOUS
# ============================================================================
st.header("11. 기타 유용한 요소")

col1, col2 = st.columns(2)

with col1:
    st.subheader("11-1. 구분선")
    st.write("위의 구분선 ↑")
    st.divider()
    st.write("아래의 구분선 ↓")

with col2:
    st.subheader("11-2. Markdown")
    st.markdown("""
    ### 마크다운 제목
    - 리스트 항목1
    - 리스트 항목2
    1. 번호 항목1
    2. 번호 항목2
    """)

st.subheader("11-3. 이미지")
st.image("https://via.placeholder.com/600x200", caption="플레이스홀더 이미지")

st.subheader("11-4. 오디오/비디오")
st.write("오디오/비디오는 URL 또는 업로드된 파일로 재생할 수 있습니다")
# st.audio("audio.mp3")
# st.video("video.mp4")

# ============================================================================
# 13. 인터랙티브 예제 / INTERACTIVE EXAMPLE
# ============================================================================
st.header("12. 인터랙티브 예제")

st.write("아래 입력값을 변경하면 실시간으로 업데이트됩니다:")

col1, col2, col3 = st.columns(3)

with col1:
    x = st.number_input("X값:", value=10)

with col2:
    y = st.number_input("Y값:", value=5)

with col3:
    operation = st.selectbox("연산:", ["+", "-", "*", "/"])

if operation == "+":
    result = x + y
elif operation == "-":
    result = x - y
elif operation == "*":
    result = x * y
else:
    result = x / y if y != 0 else "오류"

st.success(f"결과: {x} {operation} {y} = {result}")

# ============================================================================
st.divider()
st.caption("📚 더 많은 정보는 [Streamlit 공식 문서](https://docs.streamlit.io/)를 참고하세요.")
