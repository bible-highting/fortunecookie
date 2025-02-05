# 화면 구성 코드 입력
import streamlit as st
st.title("포춘쿠키 하나 먹어보세요!")
st.success(
  "시험 기간 지친 여러분을 위해 선생님이 포춘쿠키를 준비했어요." 
)

# study.csv에서 데이터 불러오기
import pandas as pd
messages = pd.read_csv("./messages/study.csv")
# st.write(messages) # 잘 불러와졌는지 확인하기

open_cookie = st.button("행운의 메시지 뽑기")  # 버튼 클릭 여부 저장

# 메시지 랜덤으로 뽑기
import random
import time

if open_cookie:
  placeholder = st.empty() # 이미지와 문구를 표시할 공간 예약
  # ➋ 이미지와 문구 표시
  with placeholder.container():
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7LpapIl8DITfz4_Y2z7pqs7FknPkjReAZCg&s", width=250)
    st.write("포춘 쿠키를 여는 중 입니다...")
  time.sleep(3) # ➌ 3초 동안 대기
  # ➍ 이미지를 제거하고 메시지 표시
  placeholder.empty()  # 이미지와 문구를 제거
  fortune = random.choice(messages.message)
  st.warning(fortune)

