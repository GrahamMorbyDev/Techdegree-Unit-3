def morse_code(word):
    morse_dict = {
        'a': 'dot-dash',
        'b': 'dash-dot-dot-dot',
        'c': 'dash-dot-dash-dot',
        'd': 'dash-dot-dot',
        'e': 'dot',
        'f': 'dot-dot-dash-dot',
        'g': 'dash-dash-dot',
        'h': 'dot-dot-dot-dot',
        'i': 'dot-dot',
        'j': 'dot-dash-dash-dash',
        'k': 'dash-dot-dash',
        'l': 'dot-dash-dot-dot',
        'm': 'dash-dash',
        'n': 'dash-dot',
        'o': 'dash-dash-dash',
        'p': 'dot-dash-dash-dot',
        'q': 'dash-dash-dot-dash',
        'r': 'dot-dash-dot',
        's': 'dot-dot-dot',
        't': 'dash',
        'u': 'dot-dot-dash',
        'v': 'dot-dot-dot-dash',
        'w': 'dot-dash-dash',
        'y': 'dash-dot-dash-dash',
        'z': 'dash-dash-dot-dot'

    }
    word = word.lower()
    encodedWord = ""
    for character in word:
        encodedWord += morse_dict[character] + "-"
    return encodedWord[:-1]


print(morse_code('graham'))
