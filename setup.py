#!/usr/bin/env python3
import os

print("\e[1;32mLinking...\e[0m")
os.system("ln -f " + os.getcwd() + "/main.py /usr/local/bin/pyset")
print("Chmodding")
os.system("chmod +x /usr/local/bin/pyset")
