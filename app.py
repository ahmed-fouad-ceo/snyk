import re

def match_regex(regex, string):
    match = re.search(regex, string)
    if match:
        return match.group()
    else:
        return None

if __name__ == "__main__":
    regex = input("Enter a regular expression: ")
    string = input("Enter a string: ")
    match = match_regex(regex, string)
    if match:
        print(match)
    else:
        print("No match found")
