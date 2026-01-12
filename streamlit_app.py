import streamlit as st
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="2D 배열 시각화 및 계산 퀴즈",
    page_icon="📊",
    layout="wide"
)

# 세션 상태 초기화
if "num1" not in st.session_state:
    st.session_state.num1 = 3
if "num2" not in st.session_state:
    st.session_state.num2 = 4
if "visualization_type" not in st.session_state:
    st.session_state.visualization_type = "히트맵"
if "user_answer" not in st.session_state:
    st.session_state.user_answer = None
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "correct_answer" not in st.session_state:
    st.session_state.correct_answer = None
if "operation" not in st.session_state:
    st.session_state.operation = "곱셈"

st.title("📊 2D 배열 시각화 및 계산 퀴즈")
st.divider()

# ============================================================================
# 1단계: 숫자 입력 및 시각화 방식 선택
# ============================================================================
st.header("1️⃣ 단계 1: 숫자 입력 및 시각화 선택")

col1, col2, col3 = st.columns(3)

with col1:
    st.session_state.num1 = st.number_input(
        "첫 번째 숫자 입력 (행):",
        min_value=2,
        max_value=10,
        value=st.session_state.num1,
        key="input_num1"
    )

with col2:
    st.session_state.num2 = st.number_input(
        "두 번째 숫자 입력 (열):",
        min_value=2,
        max_value=10,
        value=st.session_state.num2,
        key="input_num2"
    )

with col3:
    st.session_state.visualization_type = st.selectbox(
        "시각화 방식 선택:",
        ["히트맵", "바 차트", "라인 차트", "산점도"],
        index=0,
        key="viz_select"
    )

st.info(f"📌 선택된 배열 크기: {st.session_state.num1} × {st.session_state.num2}")

st.divider()

# ============================================================================
# 2단계: 2D 배열 생성 및 시각화
# ============================================================================
st.header("2️⃣ 단계 2: 2D 배열 시각화")

# 2D 배열 생성 (랜덤)
np.random.seed(42)  # 재현성을 위해 시드 설정
array_2d = np.random.randint(1, 10, size=(st.session_state.num1, st.session_state.num2))
df = pd.DataFrame(array_2d)

# 시각화 방식에 따라 차트 생성
col1, col2 = st.columns([2, 1])

with col1:
    if st.session_state.visualization_type == "히트맵":
        st.write("**히트맵 시각화:**")
        st.write(df.style.background_gradient(cmap='YlOrRd'))
    
    elif st.session_state.visualization_type == "바 차트":
        st.write("**바 차트 시각화:**")
        st.bar_chart(df)
    
    elif st.session_state.visualization_type == "라인 차트":
        st.write("**라인 차트 시각화:**")
        st.line_chart(df)
    
    elif st.session_state.visualization_type == "산점도":
        st.write("**산점도 시각화:**")
        scatter_data = []
        for i in range(st.session_state.num1):
            for j in range(st.session_state.num2):
                scatter_data.append({"X": j, "Y": i, "값": array_2d[i, j]})
        scatter_df = pd.DataFrame(scatter_data)
        st.scatter_chart(scatter_df, x="X", y="Y", size="값", color="값")

with col2:
    st.write("**배열 데이터:**")
    st.write(df)

st.divider()

# ============================================================================
# 3단계: 계산 결과 입력 및 정답 확인
# ============================================================================
st.header("3️⃣ 단계 3: 계산 결과 입력 및 정답 확인")

# 연산 선택
st.session_state.operation = st.selectbox(
    "계산할 연산 선택:",
    ["곱셈 (num1 × num2)", "덧셈 (num1 + num2)", "뺄셈 (num1 - num2)", "배열의 합"],
    key="operation_select"
)

# 정답 계산
if st.session_state.operation == "곱셈 (num1 × num2)":
    st.session_state.correct_answer = st.session_state.num1 * st.session_state.num2
    question = f"**질문: {st.session_state.num1} × {st.session_state.num2} = ?**"

elif st.session_state.operation == "덧셈 (num1 + num2)":
    st.session_state.correct_answer = st.session_state.num1 + st.session_state.num2
    question = f"**질문: {st.session_state.num1} + {st.session_state.num2} = ?**"

elif st.session_state.operation == "뺄셈 (num1 - num2)":
    st.session_state.correct_answer = st.session_state.num1 - st.session_state.num2
    question = f"**질문: {st.session_state.num1} - {st.session_state.num2} = ?**"

else:  # 배열의 합
    st.session_state.correct_answer = array_2d.sum()
    question = f"**질문: 배열의 모든 원소의 합은? (합계: {st.session_state.correct_answer})**"

st.write(question)

# 사용자 답변 입력
col1, col2 = st.columns([2, 1])

with col1:
    st.session_state.user_answer = st.number_input(
        "답변을 입력하세요:",
        value=0,
        step=1,
        key="answer_input"
    )

with col2:
    if st.button("✅ 정답 확인", key="check_btn"):
        st.session_state.show_result = True

# 정답 여부 표시
if st.session_state.show_result:
    st.divider()
    if st.session_state.user_answer == st.session_state.correct_answer:
        st.success(
            f"🎉 **정답입니다!** \n\n"
            f"입력한 답: {st.session_state.user_answer}\n"
            f"정답: {st.session_state.correct_answer}"
        )
    else:
        st.error(
            f"❌ **틀렸습니다!** \n\n"
            f"입력한 답: {st.session_state.user_answer}\n"
            f"정답: {st.session_state.correct_answer}"
        )

st.divider()

# ============================================================================
# 4단계: 초기화 버튼
# ============================================================================
st.header("4️⃣ 단계 4: 초기화")

if st.button("🔄 초기화 (새로 시작)", key="reset_btn"):
    st.session_state.num1 = 3
    st.session_state.num2 = 4
    st.session_state.visualization_type = "히트맵"
    st.session_state.user_answer = None
    st.session_state.show_result = False
    st.session_state.correct_answer = None
    st.session_state.operation = "곱셈"
    st.rerun()

st.caption("💡 팁: 숫자를 변경하면 자동으로 배열이 갱신됩니다!")
