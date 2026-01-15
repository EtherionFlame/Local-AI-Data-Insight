import streamlit as st
import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_ollama import OllamaLLM

st.set_page_config(page_title="DataInsight Local", page_icon="📊")
st.title("📊 DataInsight Local")

st.sidebar.header("Data Input")
uploaded_file = st.sidebar.file_uploader("Upload your CSV", type="csv")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#main logic loop for program
if prompt := st.chat_input("Please ask me a question about your data"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
       st.markdown(prompt)

    if uploaded_file is not None:
       with st.chat_message("assisstant"):
           st_callback = st.container()
           df=pd.read_csv(uploaded_file, encoding='windows-1252')
           #Change later to let user decide the how to change the data
           df['Order Date']= pd.to_datetime(df['Order Date'])
           df['Ship Date'] = pd.to_datetime(df['Order Date'])

           llm = OllamaLLM(model="llama3")
           agent = create_pandas_dataframe_agent(llm, 
                                      uploaded_file, 
                                      verbose=True,
                                      allow_dangerous_code=True,
                                      handle_parsing_errors=True)
           response=agent.invoke(prompt)
           output_text=response['output']

           st.markdown(output_text)

           st.session_state.messages.append({"role": "assisstant", "content":output_text})
    
    else:
        st.error("Please Provide a CSV File First")

