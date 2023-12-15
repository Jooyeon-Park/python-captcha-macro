import sys
import os
from dotenv import load_dotenv
from twocaptcha import TwoCaptcha

def solveCaptcha():
    load_dotenv()

    api_key = os.getenv('APIKEY_2CAPTCHA')

    if not api_key:
        sys.exit('APIKEY_2CAPTCHA is not set in the .env file.')
    script_directory = os.path.dirname(os.path.abspath(__file__))
    captcha_file = os.path.join(script_directory, '..', 'screenshot.png')

    # Check if 'test.png' is a valid file
    if not os.path.isfile(captcha_file):
        print(f"'{captcha_file}' is not a valid file.")

    try:
        solver = TwoCaptcha(api_key)
        result = solver.normal(captcha_file,caseSensitive=1)

    except Exception as e:
        print(e)
        return ""
        #sys.exit(e)

    else:
        # print("solved: " + str(result))
        # print("solved2: " + str(result["code"]))

        return str(result["code"])
        #sys.exit('solved: ' + str(result))