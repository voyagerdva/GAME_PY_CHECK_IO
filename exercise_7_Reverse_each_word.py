def backward_string_by_word(text):
    i = 0
    j = 0
    newText = ""
    while j < len(text):
        if text[j] == " ":
            newText += text[j]
            j += 1
        else:
            newText += text.split()[i][::-1]
            j += len(text.split()[i][::-1])
            i += 1
    return newText


text = "  abc  def  "
print(backward_string_by_word(text))

if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
