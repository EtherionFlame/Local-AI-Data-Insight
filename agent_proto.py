import pandas as pd
from langchain_ollama import OllamaLLM
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

llm = OllamaLLM(model="llama3")
df=pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')
df['Order Date']= pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Order Date'])

agent = create_pandas_dataframe_agent(llm, 
                                      df, 
                                      verbose=True,
                                      allow_dangerous_code=True)

print("Model Thinking...")
response = agent.invoke("How many rows of data do we have? And what is the total Sales amount?")
                      
print(response['output'])

