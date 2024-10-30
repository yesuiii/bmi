import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("BMI Calculator")

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Age", "BMI"])

age = st.number_input("Enter your age:", min_value=0, step=1)
height = st.number_input("Enter your height in meters:", min_value=0.0, step=0.01)
weight = st.number_input("Enter your weight in kilograms:", min_value=0.0, step=0.1)

if st.button("Calculate BMI and Add to Data"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")
        
        new_data = pd.DataFrame({"Age": [age], "BMI": [bmi]})
        st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
    else:
        st.error("Please enter a valid height.")

st.write("### Collected Data")
st.dataframe(st.session_state.data)

if not st.session_state.data.empty:
    st.write("### Age vs. BMI Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(st.session_state.data["Age"], st.session_state.data["BMI"], color='blue')
    ax.set_xlabel("Age")
    ax.set_ylabel("BMI")
    ax.set_title("Age vs. BMI Scatter Plot")
    st.pyplot(fig)
else:
    st.write("No data to plot yet.")

#boloodohooch
