#!/usr/bin/env python3
list1 = ["Admin", "user", "password"]
secret = []

for x in list1:
    secret.append(x[:2])

print(''.join(secret))
