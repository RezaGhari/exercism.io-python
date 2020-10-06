def is_pangram(sentence):
    sentence = sentence.lower()
    result = False
    for i in range(97, 123):
        if chr(i) not in sentence:
            break
    else:
        result = True
    return result