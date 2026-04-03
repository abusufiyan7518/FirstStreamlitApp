# import streamlit as st
# import pandas as pd

# # Set page configuration
# st.set_page_config(page_icon="🚀",page_title="First Streamlit App",layout="wide")
# st.title("Welcome to the App")

# #create tab
# tab1, tab2, tab3 = st.tabs(["input widgets", "output widgets", "columns"])

# with tab1:
#     st.subheader("input widgets")
#     name = st.text_input("Name :", placeholder="Enter your name")
#     pwd = st.text_input("Password :", type="password", placeholder="Enter your password")

#     content = st.text_area("Comment something about the app", placeholder="Enter your comment here")
#     age = st.number_input("Age :", placeholder="Enter your age", min_value=1, max_value=70)
#     st.slider("Rate the app", min_value=1, max_value=10, step=1, value=5)

# with tab2:
#     # st.subheader("output widgets")
#     # st.checkbox("I like this app")
#     # st.radio("How do you like the app?", ("Good", "Bad", "Average"))
#     # st.selectbox("Select your country", ("India", "USA", "UK", "Australia"))
#     # st.multiselect("Select your hobbies", ("Reading", "Traveling", "Cooking", "Sports"))
#     st.subheader("output widgets")
#     country = st.selectbox("Select your country", ("India", "USA", "UK", "Australia"))
#     gender = st.radio("Select your gender", ("Male", "Female", "Other"), horizontal=True) 
#     st.pills("Menu", ["Home", "About", "Contact"])
#     st.pills("Country", ["India", "USA", "UK", "Australia"],selection_mode="multi")
#     st.segmented_control("Fruit :", ["Pomogranate", "Apple", "Banana","strawberry"],)

#     page = st.segmented_control("Menu :", ["Home", "About", "Prediction", "analysis"],default="Home")
#     # if page == "Home":
#     #     st.write("Welcome to the Home page")
#     # elif page == "About":
#     #     st.write("Welcome to the About page")
#     # elif page == "Prediction":
#     #     st.write("Welcome to the Prediction page")
#     if st.button("Click me"):
#         st.text("this button was clicked to display this message")
    
#     if st.button("Display image"):
#         st.image("Images/image.png") 
#         st.image("Images/closeup-shot-beautiful-butterfly-with-interesting-textures-orange-petaled-flower_181624-7640.avif")
    
#     file = st.file_uploader("Upload a file", type=["csv", "xlsx"])
#     if file is not None:
#         df = pd.read_csv(file)
#         st.dataframe(df)
    
# with tab3:
    
#     col1, col2 ,col3, col4 = st.columns([2,1,2,1],border=True)
#     a1,a2,a3,a4 = st.columns([2,1,2,1],border=True)
#     with col1:
#         st.text_input("Name :",key="name") 
#         st.slider("age :", key="age")
#         st.pills("Country", [1,2,3,], key="country")

#     with col2:
#         gender=st.radio("Select your gender", ("M", "F", ), horizontal=True, key="gender")
#         if gender == "M":
#             st.image("Images/shah-rukh-khan-injured-during-king-shoot-in-mumbai-flies-to-us-for-treatment-report-when-will-srk-return.avif")
#         if gender == "F":
#             st.image("Images/8cfhv6q8_rashmika-mandanna_625x300_05_April_24.webp")
    
# with st.sidebar:
#     st.title("This is the sidebar")
#     st.image("Images/Spam.webp")
#     st.logo("images/Qspider.webp")
#     st.slider("age :", key = "slider_age")




#   changing the code to add a new page    #

import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_icon="🚀",page_title="First Streamlit App",layout="wide")
st.title("Welcome to the App")

tab1, tab2, tab3 ,tab4 = st.tabs(["Home", "About", "Prediction", "analysis"])

with tab1:
    st.subheader("Home widgets")
    name = st.text_input("Name :", placeholder="Enter your name")
    pwd = st.text_input("Password :", type="password", placeholder="Enter your password")

    content = st.text_area("Comment something about the app", placeholder="Enter your comment here")
    age = st.number_input("Age :", placeholder="Enter your age", min_value=1, max_value=70,step=1 , value=25)
    st.slider("Rate the app", min_value=1, max_value=5, step=1, value=3)

with tab2:
    st.subheader("About widgets")
    st.checkbox("I like this College")
    st.radio("Communication ?", ("Good", "Bad", "Average"))
    st.selectbox("Select your country", ("India", "USA", "UK", "Australia"))
    st.multiselect("Select your hobbies", ("Reading", "Traveling", "Cooking", "Sports"))
    # for st.pills another example
    st.pills("Currently Studiying", ["Python", "Data Science", "Machine Learning"], key="study")
    st.segmented_control("Fruit :", ["Pomogranate", "Apple", "Banana","strawberry"],)

with tab3:
    st.subheader("Student Details")
    col1, col2 ,col3, col4 = st.columns([2,1,2,1],border=True)
    with col1:
        st.text_input("Name :",key="name") 
        st.selectbox("Select your Course", ["BTECH", "MTECH", "BCA", "MCA"], key="course")
        st.slider("semester :", key="semester", min_value=1, max_value=6, step=1)
        st.pills ("Branch", ["CSE", "IT", "ECE", "EEE"], key="branch")
        st.pills("Passout Years", [2023,2024,2025,2026], key="passout_years")
    with col2:
        gender=st.radio("Select your gender ", ( "F","M"), horizontal=True, key="gender")
        if gender == "F":
            st.image("Images/8cfhv6q8_rashmika-mandanna_625x300_05_April_24.webp")
        if gender == "M":
            st.image("Images/shah-rukh-khan-injured-during-king-shoot-in-mumbai-flies-to-us-for-treatment-report-when-will-srk-return.avif  ")

    with col3:
        st.text_input("Email :", key="email")
        st.text_input("Phone number :+91", key="phone")
        st.selectbox("Select your city", ["Karnataka","Delhi", "Mumbai", "Bangalore", "Hyderabad"], key="city")

    with col4:
        st.text_input("LinkedIn profile :", key="linkedin")
        st.text_input("GitHub profile :", key="github")
        st.text_input("Portfolio link :", key="portfolio")
        
          
with tab4:
    st.subheader("Analysis widgets")

    
    col1, col2 = st.columns([2,2],border=True)
    with col1:
        file = st.file_uploader("Upload your Marksheets", type=["csv", "xlsx"])
    if file is not None:
        df = pd.read_csv(file)
        st.dataframe(df) 
    with col2:
        file = st.file_uploader("Upload your Resume", type=["csv", "xlsx"])
    if file is not None:
        df = pd.read_csv(file)
        st.dataframe(df)
    


       
    