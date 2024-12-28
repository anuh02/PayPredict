import streamlit as st
import pickle
import numpy as np



def load_model():
    with open('Salary_Prediction_app-main\saved_steps.pkl', 'rb') as file:
        da = pickle.load(file)
    return da

da = load_model()

regressor = da["model"]
le_country = da["le_country"]
le_education = da["le_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")


    #add select boxes
    countries = (
        "United States of America",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    country = st.selectbox('Country', countries)
    education = st.selectbox('Education Level', education)

    experience = st.slider('Years of Experience', 0,50,3)

    ok = st.button('Calculate Salary')
    if ok:
        x = np.array([[country, education, experience]])
        x[:,0] = le_country.transform(x[:,0])
        x[:,1] = le_education.transform(x[:,1])
        x = x.astype(float)

        salary = regressor.predict(x)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")

        
