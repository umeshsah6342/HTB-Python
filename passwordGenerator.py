#!/usr/bin/env python3
"""
While Loop and List use case
"""
wordlist = ["root", "admin", "password", "P@ssw0rd1", "qwerty"]

for word in wordlist:
    counter = 0
    while counter < 100:
        print(f"Password:{counter} {word}")
        counter = counter + 1
