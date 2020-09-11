import requests
import sys

#### VARIABLE DECLARATION
target = None
wordlist = None
status_codes = [200,204,301,302,307,401,403]

#### ARGUMENT READING
args = sys.argv
i = 1
while i < len(args) - 1:

    # Following variable holds the argument
    next_var = args[i+1]

    # Set the target
    if (args[i] == '-t'):
        if next_var[len(next_var) - 1] == '/':
            next_var = next_var[:-1]
        target = next_var

    # Set the wordlist
    elif (args[i] == '-w'):
        wordlist = next_var
    
    # Set the desired status codes
    elif (args[i] == '-s'):
        status_codes = next_var.split(",")
        status_codes = [int(i) for i in status_codes]
    i += 1

#### OPEN FILE
wordlist = open(wordlist, "r")

#### SCAN SITE
count = 0
for item in wordlist:
    item = item.strip()
    response = requests.get(f'{target}/{item}')
    if response.status_code in status_codes:
        print(f'[*] {count} - /{item} ({response.status_code})')
        count += 1