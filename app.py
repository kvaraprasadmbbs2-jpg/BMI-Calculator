import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter your weight in kg", min_value=1.0)
height = st.number_input("Enter your height in meters", min_value=0.5)

if st.button("Calculate BMI"):
    bmi = weight / (height * height)

    st.write("Your BMI is =", round(bmi, 2))

    if bmi < 18.5:
        st.write("BMI Category - Underweight")
    elif bmi < 25:
        st.write("BMI Category - Normal")
    elif bmi < 30:
        st.write("BMI Category - Overweight")
    else:
        st.write("BMI Category - Obese")
