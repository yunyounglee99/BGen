🎵 BGen: BGM Generator for YouTubers
A project that helps solo YouTubers easily select BGM that matches specific sections of their videos. This project uses Gen AI to create BGM with the mood desired by the user.
🎬 Usage Examples and Demo
Sample 1

Original Video Section: 2-6 seconds
User Prompt: "Bright and joyful festival atmosphere"
Result:

Result Video (original is silent)
[![BGen 샘플 데모](https://img.youtube.com/vi/OungXXpJo4U/0.jpg)](https://youtu.be/OungXXpJo4U)

🚀 Project Overview
You can generate BGM that suits specific sections of a video through Gen AI.
🧑‍💻 Team Members
Yunyoung Lee

@yunyounglee99

Hyungwon Lee

@hwstar-1204

📚 Implemented Features
📌 Video Section Editing

Implemented using ffmpeg and MoviePy libraries to save and edit video sections specified by the user

📌 Video to Text Summarization

Uses Twelve Laps API to generate text summaries to understand the user's desired video section
Process: Video upload → Twelve Laps API → Text Summary

📌 Generation of User-Desired BGM

Collects User Prompt to understand requirements and uses audiocraft API to generate matching BGM
Process: AI and User collaborative Prompt → audiocraft API → Generate BGM

🛠 Technologies Used

Django: full stack web framework
ffmpeg: video editing and processing
MoviePy: Python-based video editing library
Twelve Laps API: API for video text summarization
audiocraft API: BGM generation API based on summarized video prompts and user prompts

📝 Installation and Execution

Clone this repository.
bashgit clone https://github.com/your-username/BGen.git
cd BGen

Set up a virtual environment and install the required packages.
bashpython -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`
pip install -r requirements.txt

Set Twelve Laps API key and Hugging Face authentication token as environment variables.
bashexport TWELVE_LAPS_API_KEY='your_twelve_laps_api_key'
export HUGGINGFACE_TOKEN='your_huggingface_token'

Run the Django server.
bashpython manage.py runserver

Open http://localhost:8000 in your web browser to use the application.

⚠️ Precautions

A Twelve Laps API key is required to use the Twelve Laps API.
A Hugging Face authentication token is required.

📜 License
This project follows the MIT license. For more details, please refer to the LICENSE file.
