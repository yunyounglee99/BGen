from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError

from .twelveLabs import create_idx
from .audio_craft_api import gen_audio
from .utils import save_file, get_media_path
from .edit_video import VideoEditor


def index(request):
    return render(request, 'index.html')

@csrf_exempt
def handle_video_edit(request):
    if request.method == 'POST':
        try:
            action = request.POST.get('action')
            video_file = request.FILES.get('video')
            if not video_file:
                return HttpResponse("Video file is required.")

            video_editor = VideoEditor()

            if action == 'clip':
                start = int(request.POST.get('start'))
                end = int(request.POST.get('end'))
                context = {
                    'aiPrompt': request.POST.get('aiPrompt', ''),
                    'userPrompt': request.POST.get('userPrompt', ''),
                    'start': start,
                    'end': end,
                    'video_name': video_file.name,  # video_name,
                    'video_url': '',
                }
                # Save context to session
                request.session['context'] = context


                # 동영상 저장
                save_file(video_file)
                video_path = get_media_path('videos', context.get('video_name'))
                # 저장한 동영상을 해당 구간으로 자르기
                cut_video_path = video_editor.cut_video(video_path, start, end)

                summery = create_idx(cut_video_path)
                context['aiPrompt'] = summery
                print(context['aiPrompt'])
                return render(request, 'index.html', context)

            # 브금을 해당 동영상의 구간에 추가하는 경우
            elif action == 'add_bgm':
                context = request.session.get('context', {})
                start = context.get('start')
                end = context.get('end')

                video_editor.cut_audio(start, end)
                print("asd",start,end)
                video_editor.add_bgm_to_video()
                final_video_path = video_editor.insert_video(start, end)
                context['video_url'] = final_video_path

                return render(request, 'index.html', context)

        except MultiValueDictKeyError:
            return HttpResponse("Video file is required.")
        except Exception as e:
            print("An error occurred:", e)  # 오류 메시지 출력
    return render(request, 'index.html')

@csrf_exempt
def generate_audio(request):
    if request.method == 'POST':
        ai_prompt = request.POST.get('aiPrompt', '')
        user_prompt = request.POST.get('userPrompt', '')
        ai_checkbox = request.POST.get('aiCheckbox')
        use_ai_prompt = bool(ai_checkbox)  # AI prompt 사용 여부

        if use_ai_prompt:
            combined_prompt = ai_prompt + user_prompt
        else:
            combined_prompt = user_prompt

        gen_audio(combined_prompt)
        context = {
            'response_message': f"Prompt processed successfully! Combined Prompt: {combined_prompt}"
        }
        return render(request, 'index.html', context)
    return HttpResponse("Invalid request method", status=400)
