from working.data import fetch_video_info
from working.transcript import fetch_transcript
import json

def load_api_key_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data['youtube_api_key']

api_key = load_api_key_from_json('/home/devansh/Documents/ytube_data_and_transcript/testing/config.json')
video_id = 'H9dCIPzRfzo'
details = fetch_video_info(video_id, api_key)
transcript = fetch_transcript(video_id)

# print(details)
# print(transcript)        check for yourself
