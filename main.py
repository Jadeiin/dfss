#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

API_KEY = ""
AUTH_TOKEN = ""

HEADERS = {
    "ApiKey": API_KEY,
    "AuthToken": AUTH_TOKEN,
    "SchoolId": "1",
}

API_URL = "https://api.dfssclub.cn/api/v1/VideoTeaching/Edu/GetSubject?subjectId=1"

def main():
    raise NotImplementedError("This script is a placeholder and does not perform any actions.")

if __name__ == "__main__":
    main()
