# 🎵 BGen: BGM Generator for YouTubers
A project designed to help solo YouTubers easily select BGM that matches specific sections of their videos. This project uses Gen AI to create BGM with the mood desired by the user.
## 🎬 Usage Examples and Demo
### Sample 1
- Original Video Section: 2-6 seconds
- User Prompt: "Bright and joyful festival atmosphere" (In Korean)
- Result:
#### Result Video (Click the image)
[![puripuri 샘플 데모](https://img.youtube.com/vi/OungXXpJo4U/0.jpg)](https://youtu.be/OungXXpJo4U)

## 🚀 Project Overview
You can generate BGM that suits specific sections of a video through Gen AI.
## 🧑‍💻  Team Members
Yun-young Lee
  - [@yunyounglee99](https://github.com/yunyounglee99)

Hyung-won Lee
  - [@hwstar-1204](https://github.com/hwstar-1204) 
## 📚 Implemented Features
### 📌 Video Section Editing
- Implemented using ffmpeg and MoviePy libraries to save and edit video sections specified by the user
### 📌 Video to Text Summarization
- Uses Twelve Laps API to generate text summaries to understand the video section desired by the user
- Process: Video upload → Twelve Laps API → Text Summary
### 📌 Generating BGM with User's Desired Mood
- 사User Prompt is created to understand the user's requirements, and audiocraft API is used to generate matching BGM
- Process: AI and User Collaborative Prompt → audiocraft API → Generate BGM
## 🛠 Technologies Used
-Django: full stack web framework
- ffmpeg: video editing and processing
- MoviePy: Python-based video editing library
- Twelve Laps API: API for video text summarization
- audiocraft API: BGM generation API based on summarized video prompts and user prompts
## 📝 Installation and Execution Method
1. Clone this repository.
    bash
    git clone https://github.com/your-username/BGen.git
    cd BGen
    
2. Set up a virtual environment and install the necessary packages.
    bash
    python -m venv venv
    source venv/bin/activate  # Windows에서는 `venv\Scripts\activate`
    pip install -r requirements.txt
    
3. Set the Twelve Laps API key and Hugging Face authentication token as environment variables.
    bash
    export TWELVE_LAPS_API_KEY='your_twelve_laps_api_key'
    export HUGGINGFACE_TOKEN='your_huggingface_token'
    
4. Run the Django server.
    bash
    python manage.py runserver
    
5. Open http://localhost:8000 in your web browser to use the application.
## ⚠️ Precautions
- A Twelve Laps API key is required to use the Twelve Laps API.
- A Hugging Face authentication token is required.
## 📜 License
This project follows the MIT license. For more details, please refer to the [LICENSE](./LICENSE) file.
