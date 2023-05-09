# CAPTURE CTF TryHackMe Walkthrough

The main goal of the challenge is to gain access to a secured web application by utilizing skills and knowledge in the field of hacking and network security. The first step is to conduct an analysis of the application and identify any vulnerabilities. The creators have secured the application using a frequency limiter, which aims to prevent ***brute-force attacks***.

The next step is to find a way to bypass the frequency limiter and conduct a ***brute-force attack***. This requires knowledge of various techniques such as fuzzing or request smuggling. The goal is to obtain the correct login credentials, which will allow us to gain access to the application.

Difficulty: Easy



"_Error: The user 'username' does not exist_" suggests that the user with the specified name does not exist in the system. Brute-force technique can be used to test the existence of users in the system.

![image](https://user-images.githubusercontent.com/70896562/236875120-ee44b338-f0bc-4c2a-ad0e-85bfe574d32c.png)
|:--:| 
| *login page* |


The "Error: Invalid password for user '^^^'" message can be used by hackers as a valuable clue to launch a login attack. Users can use this information to run a brute-force or dictionary attack on the '^^^' user's account to find the correct password.
![image](https://user-images.githubusercontent.com/70896562/236879740-cd94372f-ff9b-44d7-a1a2-f8b9172f3baf.png)
|:--:| 
| *login page* |


## Dictionary attack

- Run the Python 3 code in the terminal (or command prompt):
```shell
  python3 dictionary_attack.py <IP_VICTIM>
```
![image](https://github.com/WojciechSkumajTo/THM-Capture/assets/70896562/7f4a9d27-26f5-47ce-a4a4-d6543d695d61)
|:--:| 
| *The result of the dictionary_attack.py* |


## Summary
Obtaining credentials led to gaining access to a protected web application and obtaining the flag.

![image](https://user-images.githubusercontent.com/70896562/236882142-f5155c1e-1b48-4c2b-b733-8c6ae2be112c.png)
|:--:| 
| *Login attempt* |


![image](https://user-images.githubusercontent.com/70896562/236882357-e9e7a213-07b7-4d39-99e7-5e9c6ee3c81b.png)
|:--:| 
| *Correct login* |
