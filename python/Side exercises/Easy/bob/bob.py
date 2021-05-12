import re


def response(hey_bob: str):
    hey_bob = re.sub("\s", "", hey_bob)  # I could use hey_bob.strip(" \n\t\r"). Is the regex cleaner ?
    if not hey_bob:
        answer = "Fine. Be that way!"
    else:
        question = hey_bob.endswith("?")  # Better than a slice ? Looks cleaner, but I don't know
        caps = hey_bob.isupper()
        # I could condense the conditions on one line, but isn't it more readable like that ?
        if question and caps:
            answer = "Calm down, I know what I'm doing!"
        elif question:
            answer = "Sure."
        elif caps:
            answer = "Whoa, chill out!"
        else:
            answer = "Whatever."
    return answer
