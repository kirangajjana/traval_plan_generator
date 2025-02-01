import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import streamlit as st



load_dotenv()

apikey=os.getenv("gemini")

llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",api_key=apikey)
templates="""
you should act as an expert in travel planner
1.you should plan the trip based on the {city} and {month} and {budget}
2.you should plan the trip or give buged to the trip based on the {travel} type
3.you should also suggest best places to visit
4.you also need to suggest must try food in the {city} user as selected
5.you have to provide the types of food use can eat in the tabular form
6.make sure all the things you have given should be budget friendly and should be based on the {budget}
7.also suggest the langusge that user can speak on the {city}
8.at the end we can gice a small thig like this app was made by kiran gajjana in bold letters

### **output format **
-use bullet point for clarity
-provide structured answers
-if any information is unavilable,respond: '"As of now, i dont have specific details on that"'
"""

prompttemplate=PromptTemplate(input_variables=["city","month","budget","travel"],template=templates)

st.title("Budget Travel planner")


city=st.text_input("Please Enter the City Name you want to travel")
month=st.text_input("Please Enter the Month you wanted to Travel")
budget=st.text_input("Please Enter the Budget you want to Invest for the Travel")
options = ["High", "Medium", "Small"]

# Create a selectbox with the options list
travel = st.selectbox("Select travel size:", options)



if st.button("Submit"):
    response=llm.invoke(prompttemplate.format(city=city,budget=budget,month=month,travel=travel))
    st.write(response.content)
    st.balloons()