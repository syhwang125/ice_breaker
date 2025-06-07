from dotenv import load_dotenv
import os
# Load environment variables from a .env file

load_dotenv()

if __name__ == "__main__":
    print("Hello, LanChain! This is an ice breaker script.")
    print(os.environ.get('OPENAI_API_KEY', 'OPENAI_API_KEY not set'))        
    # launch.json 파일의 환경 변수 Python Debugger 의 .env에서 API 키를 가져옵니다.
    # 이 코드는 OpenAI API 키를 출력합니다.
    # 실행은 python debugger 로 가능합니다. 
    print(os.environ.get('COOL_API_KEY', 'COOL_API_KEY not set'))  # This line now handles missing variable gracefully

