"""
Run this file to install dependencies for Chat bot project
"""

import os

print("ChatBot Setup Starting...")

#Update pip
print("Starting: ------Upgrade pip------")
os.system("python -m pip install --upgrade pip --user")
print("Finished: ------Upgrade pip------")

#wikipedia
print("Starting: ------Install wikipedia------")
os.system("python -m pip install wikipedia --user")
print("Finished: ------Install wikipedia------")

#googletrans
print("Starting: ------Install googletrans------")
os.system("python -m pip install googletrans --user")
print("Finished: ------Install googletrans------")

#currency_converter
print("Starting: ------Install CurrencyConverter------")
os.system("python -m pip install CurrencyConverter --user")
print("Finished: ------Install CurrencyConverter------")

#dictionary
print("Starting: ------Install dictionary------")
os.system("python -m pip install PyDictionary --user")
print("Finished: ------Install dictionary------")

#num2words
print("Starting: ------Install num2words------")
os.system("python -m pip install num2words --user")
print("Finished: ------Install num2words------")

#countryinfo
print("Starting: ------Install countryinfo------")
os.system("python -m pip install countryinfo --user")
print("Finished: ------Install countryinfo------")

#us
print("Starting: ------Install us------")
os.system("python -m pip install us --user")
print("Finished: ------Install us------")



print("Setup Completed.")
