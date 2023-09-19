import re

def match_regex(regex, string, max_backtrack_steps=10000):
    """Matches a regular expression against a string with a limited number of backtracking steps.

    Args:
        regex: The regular expression to match.
        string: The string to match the regular expression against.
        max_backtrack_steps: The maximum number of backtracking steps to perform.

    Returns:
        A match object if the regular expression matches the string, or None otherwise.
    """

    scanner = re.Scanner(regex)
    match = None
    while True:
        match = scanner.search(string)
        if not match or scanner.counters[0] > max_backtrack_steps:
            break
    return match

if __name__ == "__main__":
    regex = input("Enter a regular expression: ")
    string = input("Enter a string: ")
    match = match_regex(regex, string)
    if match:
        print(match)
    else:
        print("No match found")
