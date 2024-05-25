import requests
from prompt_video.utils import get_media_path
from decouple import config

API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
# API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-medium"
headers = {"Authorization": config('huggingface_token')}


def gen_audio(sum_text):
    print("audio_start: ",sum_text)
    def audio_query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content

    audio_bytes = audio_query({
        "inputs": sum_text,
    })
    bgm_path = get_media_path('audios', 'new_bgm.mp3')

    with open(bgm_path, "wb") as audio_file:
        audio_file.write(audio_bytes)

    print("Audio file saved as 'new_bgm.mp3'")
