def find_message(text):
    """Find a secret message"""
    find_message = lambda x: ''.join(filter(str.isupper, text))
    return find_message(text)


def find_message_second(text):
    text = [i for i in text if i.isupper()]
    secret = ''.join(text)
    return secret

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HdELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
