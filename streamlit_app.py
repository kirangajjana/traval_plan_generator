import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
load_dotenv()

# Load API keys from Streamlit secrets
gemini_api_key = os.getenv("gemini")

# Initialize the Gemini LLM with the API key
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    api_key=gemini_api_key,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Define the prompt template
templates = """
You should act as an expert in travel planning.
1. You should plan the trip based on the {city}, {month}, and {budget}.
2. You should provide a budget breakdown and recommend places to visit based on the {travel} type.
3. Suggest must-try foods in {city}.
4. Provide a table listing types of foods that can be eaten in {city}.
5. Ensure all suggestions are budget-friendly.
6. Recommend languages spoken in {city}
7. you have to generate an image regarding the above
8. At the end, add a note saying: "This app was created by Kiran Gajjana."

### **Output Format**
- Use bullet points for clarity.
- Provide structured answers.
- If any information is unavailable, respond with: "As of now, I don't have specific details on that."
"""

prompttemplate = PromptTemplate(input_variables=["city", "month", "budget", "travel"], template=templates)

# Streamlit interface
st.title("Budget Travel Planner")

# Sidebar information
with st.sidebar:
    st.write('Welcome to the Travel Plan Generator')
    # st.image('images.jpg')  # Replace with your image path

st.subheader("Let’s plan your next trip! Please fill in the details below:")

# Inputs from the user
city = st.text_input("City Name:")
month = st.text_input("Month of Travel:")
budget = st.text_input("Your Travel Budget (in your preferred currency):")
options = ["High", "Medium", "Small"]
travel = st.selectbox("Select the type of trip:", options)

# Loading the response when the user presses "Submit"
if st.button("Generate Travel Plan"):
    if city and month and budget:
        with st.spinner('Generating your travel plan...'):
            # Generate travel plan based on user input
            response = llm.invoke(prompttemplate.format(city=city, month=month, budget=budget, travel=travel))
        
        # Display the response after generation
        st.write(response.content)
        st.balloons()  # Show a celebration when done
    else:
        st.write("Please fill in all the details to generate your personalized travel plan.")

