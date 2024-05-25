import os
from glob import glob
from twelvelabs import TwelveLabs
from twelvelabs import APIStatusError
from twelvelabs.models.task import Task
from decouple import config
# 2 create index
my_api_key = config('TWELVE_LABS_API_KEY')
my_index_name = 'pegasus1_index'

def create_idx(cut_video_path):

    try:
        client = TwelveLabs(api_key=my_api_key)

        existing_indexes = [index.name for index in client.index.list()]
        unique_index_name = my_index_name
        counter = 1
        while unique_index_name in existing_indexes:
            unique_index_name = f"{my_index_name}_{counter}"
            counter += 1

        index = client.index.create(
            name=unique_index_name,
            engines=[
                # {
                #     "name": "marengo2.6",
                #     "options": ["visual", "conversation", "text_in_video"],
                # },
                {
                    "name": "pegasus1",
                    "options": ["visual", "conversation"],
                },
            ],
        )
        print(f"Created index: id={index.id} name={index.name} engines={index.engines}")



        # 3 upload videos
        # video_files = glob(VIDEO_PATH)
        video_files = glob(cut_video_path)
        for video_file in video_files:
            print(f"Uploading {video_file}")
            task = client.task.create(index_id=index.id, file=video_file, language="en")
            print(f"Created task: id={task.id}")

            # (Optional) Monitor the video indexing process
            # Utility function to print the status of a video indexing task
            def on_task_update(task: Task):
                print(f"  Status={task.status}")
            task.wait_for_done(sleep_interval=50, callback=on_task_update)

            if task.status != "ready":
                raise RuntimeError(f"Indexing failed with status {task.status}")
            print(f"Uploaded {video_file}. The unique identifer of your video is {task.video_id}.")

        videos = client.index.video.list(index.id)
        for video in videos:

            print(f"Generating text for {video.id}")

        # 4 gen title, topics, hashtags
        #     res = client.generate.gist(video_id=video.id, types=["title", "topic", "hashtag"])
        #     print(f"Title: {res.title}\nTopics={res.topics}\nHashtags={res.hashtags}")

        # 5 gen sumerises, chapters or highlights
            res = client.generate.summarize(video_id=video.id, type="summary")
            print(f"Summary: {res.summary}")

            # print("Chapters:")
            # res = client.generate.summarize(video_id=video.id, type="chapter")
            # for chapter in res.chapters:
            #     print(
            #         f"  chapter_number={chapter.chapter_number} chapter_title={chapter.chapter_title} chapter_summary={chapter.chapter_summary} start={chapter.start} end={chapter.end}"
            #     )
            #
            # print("Highlights:")
            # res = client.generate.summarize(video_id=video.id, type="highlight")
            # for highlight in res.highlights:
            #     print(
            #         f"  Highlight={highlight.highlight} start={highlight.start} end={highlight.end}"
            #     )

        # # 6 gen open-ended text
        #     res = client.generate.text(video_id=video.id, prompt="Based on this video, I want to generate five keywords for SEO (Search Engine Optimization).")
        #     print(f"Open-ended Text: {res.data}")
            return res.summary

    except APIStatusError as e:
        print('API Status Error, 4xx or 5xx')
        print(e)
    except Exception as e:
        print(e)
