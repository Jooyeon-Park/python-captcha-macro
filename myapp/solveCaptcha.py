import sys
import os
from dotenv import load_dotenv
import capsolver
import base64
from pathlib import Path

def solveCaptcha():
    load_dotenv()

    api_key = os.getenv('APIKEY_CapSolver')

    if not api_key:
        sys.exit('APIKEY_2CAPTCHA is not set in the .env file.')

    with open("screenshot.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    try:
        capsolver.api_key = api_key
        solution = capsolver.solve({
                "type": "ImageToTextTask",
                "module": "common",
                "body": encoded_string
        })
        print(solution)
        return str(solution["text"])

    except Exception as e:
        print(e)
        return ""
        #sys.exit(e)