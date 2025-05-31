import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# OpenAI API Key
# os.environ["OPENAI_API_KEY"] = (
#     "your-api-key"
# )

os.environ["TAVILY_API_KEY"] = (
    "your-api-key"
)
prompt = ChatPromptTemplate.from_messages([("user", "{question}")])
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

chain = prompt | llm

result = chain.invoke(
    {"question": "2024년 한국 뮤지컬 시카고의 주연 배우들은 누구인가요?"}
)

print(result.content)