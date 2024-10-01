import streamlit as st
import numpy as np
import pandas as pd


st.header('BMIを計算しよう！')

st.write ('体重と身長を記入してね')

st.latex(r"計算式=体重(kg) ÷ 身長(m)^2")


def calculate_bmi(weight, height):
     """BMIを計算する関数"""
     height = height / 100  # 身長をメートルに変換
     bmi = weight / (height ** 2)
     return bmi
default_weight = 50
default_height = 160

weight = st.number_input('体重(kg)', min_value=0, max_value=200, value=50)
height = st.number_input('身長(cm)', min_value=0, max_value=200, value=160)

if weight > 0 and height > 0:
     bmi = calculate_bmi(weight, height)
     st.write(f"あなたのBMIは{bmi:.1f}です。")

if bmi < 18.5:
     st.write("低体重です。")
elif bmi < 25:
     st.write("正常範囲です。")
else:
     st.write("肥満の傾向があります。")
