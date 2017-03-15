def checkio(words):
    words = words.split(' ')
    isWord = True
    counter = 0
    for s in words:
        if isinstance(s, str):
                counter += 1
        if s.isdigit():
                isWord = False
                counter = 0
        if counter < 3:
            isWord = False
        if counter >= 3:
            isWord = True
            break
    return isWord


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12") == True, "3"
