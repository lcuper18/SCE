# pip3 install langchain_openai
# python3 deepseek_v2_langchain.py
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model='deepseek-chat', 
    openai_api_key='sk-0e744d4661ee49489792adb2f50be149', 
    openai_api_base='https://api.deepseek.com',
    max_tokens=1024
)

response = llm.invoke("Hola, me puedes ayudar para aprender a programar!")
print(response.content)