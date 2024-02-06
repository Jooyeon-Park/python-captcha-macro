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
    # script_directory = os.path.dirname(os.path.abspath(__file__))
    # captcha_file = os.path.join(script_directory, 'screenshot.png')

    # # Check if 'test.png' is a valid file
    # if not os.path.isfile(captcha_file):
    #     print(f"'{captcha_file}' is not a valid file.")

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

    except Exception as e:
        print(e)
        return ""
        #sys.exit(e)

    else:
        # print("solved: " + str(result))
        # print("solved2: " + str(result["code"]))

        return str(solution["text"])
        #sys.exit('solved: ' + str(result))

solveCaptcha()