def checkIfPangram(sentence: str) -> bool:
    uniqueBets = ""
    if len(sentence) < 26:
        return False
    for i in range(len(sentence)):
        if sentence[i] not in uniqueBets:
            uniqueBets += sentence[i]
    if len(uniqueBets) == 26:
        return True
    return False

print(checkIfPangram("uwqohxamknblecdtzpisgvyfjr"))