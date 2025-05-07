# 🎵 BGen: BGM Generator for YouTubers
1인 유튜버들이 동영상의 특정 구간에 어울리는 BGM을 쉽게 선정할 수 있도록 도와주는 프로젝트입니다. 이 프로젝트는 Gen AI를 활용하여 사용자가 원하는 느낌의 BGM을 생성합니다.
## 🎬 사용 예시 및 데모
### 샘플 1
- 원본 영상 구간: 2초-6초
- 사용자 프롬프트: "밝고 즐거운 축제분위기"
- 결과물: 
#### 결과 영상 (원본은 무음 영상)
[![BGen 샘플 데모](https://img.youtube.com/vi/OungXXpJo4U/0.jpg)](https://youtu.be/OungXXpJo4U)
## 🚀 프로젝트 개요
동영상의 특정 구간에 어울리는 BGM을 Gen AI를 통해 생성해 낼 수 있습니다. 
## 🧑‍💻 팀원
이윤영
  - [@yunyounglee99](https://github.com/yunyounglee99)
이형원
  - [@hwstar-1204](https://github.com/hwstar-1204) 
## 📚 구현 기능
### 📌 동영상 구간 편집
- 사용자가 지정한 영상 구간을 저장 및 편집하기 위해 ffmpeg, MoviePy 라이브러리를 사용하여 구현
### 📌 동영상을 텍스트로 요약
- 사용자가 원하는 구간의 동영상을 이해하기 위해 Twelve Laps API를 사용하여 텍스트 요약 생성
- 과정: Video upload → Twelve Laps API → Text Summery
### 📌 사용자가 원하는 느낌의 BGM 생성
- 사용자의 요구사항을 파악하기 위해 User Prompt를 작성받아 audiocraft API를 사용하여 어울리는 BGM 생성
- 과정: AI와 User의 공동 Prompt → audiocraft API → Generate BGM
## 🛠 사용한 기술
-Django: full stack 웹 프레임워크 
- ffmpeg: 동영상 편집 및 처리
- MoviePy: 파이썬 기반의 동영상 편집 라이브러리
- Twelve Laps API: 동영상의 텍스트 요약을 위한 API
- audiocraft API: 요약된 동영상 프롬프트와 사용자 프롬프트 기반의 BGM 생성 API
## 📝 설치 및 실행 방법
1. 이 저장소를 클론합니다.
    bash
    git clone https://github.com/your-username/BGen.git
    cd BGen
    
2. 가상 환경을 설정하고 필요한 패키지를 설치합니다.
    bash
    python -m venv venv
    source venv/bin/activate  # Windows에서는 `venv\Scripts\activate`
    pip install -r requirements.txt
    
3. Twelve Laps API 키와 Hugging Face 인증 토큰을 환경 변수로 설정합니다.
    bash
    export TWELVE_LAPS_API_KEY='your_twelve_laps_api_key'
    export HUGGINGFACE_TOKEN='your_huggingface_token'
    
4. Django 서버를 실행합니다.
    bash
    python manage.py runserver
    
5. 웹 브라우저에서 http://localhost:8000을 열어 애플리케이션을 사용합니다.
## ⚠️ 주의 사항
- Twelve Laps API를 사용하기 위해서는 Twelve Laps API 키가 필요합니다.
- Hugging Face의 인증 토큰이 필요합니다.
## 📜 라이센스
이 프로젝트는 MIT 라이센스를 따릅니다. 자세한 내용은 [LICENSE](./LICENSE) 파일을 참고하세요.
