import streamlit as st
st.title("bmi calculator")
weight = st.number_input("Enter your Weight in kg",min_value = 1.0)
height = st.number_input("Enter your height in mt",min_value = 0.5)
if st.button("calculate bmi"):
  bmi = weight / (height * height)
  st.write("Your bmi is = ", round (bmi,2))
if bmi < 18.5:
  st.write("bmi category - Underweight")
elif bmi < 25:
  st.write ("bmi categoery - Normal")
elif bmi <30:
  st.write("bmi categoery - Overweight ")
else:
  st.write("bmi category - Obese")
