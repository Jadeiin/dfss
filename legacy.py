#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This script calls the legacy API for passing subject 1 registration requirements.
# Fill in the API_KEY and AUTH_TOKEN with your credentials.

import requests
import time

API_KEY = ""
AUTH_TOKEN = ""

HEADERS = {
    "apikey": API_KEY,
    "authtoken": AUTH_TOKEN,
    "Content-Type": "application/json"
}

LESSON_VIDEO_IDS = {
    1: [221, 126, 127, 128],
    2: [129, 130, 131, 132, 133, 134, 135],
    3: [136, 137, 138, 139],
    4: [141, 140, 142],
    5: [143, 144, 145, 146, 147],
    6: [148, 149, 150, 151],
    7: [152, 153, 154, 155, 156, 157, 158],
    8: [159, 160, 161, 162, 163],
    9: [164, 165, 166, 167, 168, 169, 170],
    10: [171, 172, 173, 174, 175, 176, 177, 178, 179],
    11: [180, 181, 182, 183, 184],
    12: [185, 186, 187, 188, 189],
}

START_STREAM_URL = "https://api.dfsstv.cn/api/v1/Stream/Start?videoId={}"
END_STREAM_URL = "https://api.dfsstv.cn/api/v1/Stream/End?streamId={}"
HEARTBEAT_URL = "https://api.dfsstv.cn/api/v1/Stream/HeartBeat?streamId={}"

def main():
    for lesson_num in sorted(LESSON_VIDEO_IDS.keys()):
        for video_id in LESSON_VIDEO_IDS[lesson_num]:
            start_url = START_STREAM_URL.format(video_id)
            try:
                response = requests.post(start_url, headers=HEADERS)
                print(f"lesson={lesson_num} videoId={video_id} status={response.status_code} response={response.text}")
                stream_id = None
                if response.status_code == 200:
                    try:
                        data = response.json()
                        stream_id = data.get("data", {}).get("streamId")
                    except Exception:
                        pass
                if stream_id:
                    # Heartbeat
                    try:
                        heartbeat_url = HEARTBEAT_URL.format(stream_id)
                        heartbeat_resp = requests.post(heartbeat_url, headers=HEADERS)
                        print(f"lesson={lesson_num} videoId={video_id} heartbeat status={heartbeat_resp.status_code} response={heartbeat_resp.text}")
                    except Exception as e:
                        print(f"lesson={lesson_num} videoId={video_id} heartbeat error: {e}")
                    # End stream
                    end_url = END_STREAM_URL.format(stream_id)
                    try:
                        end_resp = requests.post(end_url, headers=HEADERS)
                        print(f"lesson={lesson_num} videoId={video_id} end_stream status={end_resp.status_code} response={end_resp.text}")
                    except Exception as e:
                        print(f"lesson={lesson_num} videoId={video_id} end_stream error: {e}")
            except Exception as e:
                print(f"lesson={lesson_num} videoId={video_id} error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    main()
