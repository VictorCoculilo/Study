def solution(text, ending):
    text=text[::-1]
    ending=ending[::-1]
    size=len(ending)
    if text[:size] == ending:
        return True
    else:
        return False