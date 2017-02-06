def check_pangram2(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    check = ''
    isPanagram = True
    for i in text:
        if i.lower() in alphabet:
            check += i.lower()
            print(i)
    for j in alphabet:
        if j not in check:
            isPanagram = False
    return isPanagram
