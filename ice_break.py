# from langchain_core.prompts import PromptTemplate
from langchain.prompts.prompt import PromptTemplate
# Ensure you have the required packages installed: # pip install python-dotenv langchain
from langchain_openai import ChatOpenAI
# Ensure you have the required packages installed: pip install python-dotenv langchain langchain-openai
from langchain_ollama import ChatOllama
# Ensure you have the required packages installed: pip install langchain-ollama
import os
from langchain_openai import ChatOpenAI 

information = """Nearly 200 people in Vienna, Austria, gathered recently to enjoy two fun activities at the same time.
They worked with needles and yarn. And they watched a movie together called The Devil Wears Prada.
It sounds a bit like a grandmother, but it's relaxing. And…what's wrong with letting the grandmother in us express herself, joked Austrian Alexander Koch. He is a 28-year-old who crochets.
Knitting or crocheting while watching movies has gained popularity in Europe
Luisa Palmer was one of the organizers of the event. Palmer said that, during the COVID-19 pandemic, 
A lot of people started knitting during the lockdown alone at home. Palmer launched the knitting evenings once a month at Votiv Kino, a place to watch movies in the center of the Austrian capital.
Now we need to find ourselves…" in real life, the 30-year-old told the French News Agency (AFP) before the event.
People are knitting, eating, or even breastfeeding babies while watching a movie. This movement is the latest attempt to add different things to the movie-watching experience, said Lisa Stolze. She is a spokesperson for Votiv Kino, the movie house.
"""
if __name__ == "__main__":
    print("Hello langchain!")

    # summary_template = """
    #     given the information about a person from I want you to create:
    #     1. a short summary
    #     2. two interesting facts about them 
    # """
    summary_template = """
        given the following information: {information}
        I want you to create:
        1. a short summary
        2. two interesting facts about them 
    """
    # summary_prompt_template = PromptTemplate(
    #     input_variables="information",
    #     template=summary_template
    # )

summary_prompt_template = PromptTemplate(
    input_variables=["information"],  # 리스트로 변경
    template=summary_template
)

if __name__ == "__main__":
    print("Hello langchain!")

    # llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # Create a chain with the prompt template and the LLM
    # Note: The input variable should match the one defined in the prompt template
    # summary_prompt_template = summary_prompt_template.bind(information=information)
    # Use the prompt template to create a chain with the LLM    

    llm = ChatOllama(model="llama3", temperature=0)
    # Create a chain with the prompt template and the LLM


    chain = summary_prompt_template | llm
    # Invoke the chain with the information
    res = chain.invoke(input={"information": information})
    print(res)

# .env 파일에 OpenAI API Key 를 저장하고 (OPENAI_API_KEY=your_api_key)
# launch.json 파일의 환경 변수 Python Debugger 의 .env에서 API 키를 가져옵니다. 
# 이 코드는 OpenAI API 키를 출력합니다.
# 실행은 python debugger 로 가능합니다.

# 실행 결과 response 는 다음과 같습니다. model=gpt 대신에 llama3 모델을 사용했기 때문에 response_metadata 에서 model 이름이 llama3 로 표시됩니다.
# { response_metadata={'model': 'llama3', 'created_at': '2025-05-31T07:27:00.9305394Z', 'done': True, 'done_reason': 'stop', 'total_duration': 48687631200, 'load_duration': 2399183100, 'prompt_eval_count': 290, 'prompt_eval_duration': 20883786600, 'eval_count': 168, 'eval_duration': 25402729000, 'model_name': 'llama3'} id='run--8500c0ee-0059-4afa-85c9-fc0a7c55b155-0' usage_metadata={'input_tokens': 290, 'output_tokens': 168, 'total_tokens': 458}
