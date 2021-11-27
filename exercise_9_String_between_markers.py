import re

def between_markers(text: str, begin: str, end: str) -> str:
    print(text)
    print(begin)
    print(end)

    if end in text.split(begin)[0] and begin in text.split(end)[1]:
        return ''
    elif begin in text and end in text:
        first = text.split(begin)
        print(f"first = {first}")
        second = first[1].split(end)
        print(f"second = {second}")
        return second[0]
    elif begin not in text and end in text:
        second = text.split(end)
        print(f"second = {second}")
        return second[0]
    elif end not in text and begin in text:
        first = text.split(begin)
        print(f"first = {first}")
        return first[1]
    elif end not in text and begin not in text:
        return text
    elif end not in text and begin not in text:
        return text

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
