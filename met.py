def double_metaphone(word):
    word = word.lower()
    primary = []
    secondary = []

    # Consonant and vowel mappings for primary and secondary encoding
    phonetic_map = {
        'a': ('0', '0'), 'e': ('0', '0'), 'i': ('0', '0'), 'o': ('0', '0'), 'u': ('0', '0'),
        'b': ('b', 'b'), 'f': ('f', 'f'), 'p': ('f', 'p'), 'v': ('f', 'v'),
        'c': ('k', 's'), 'g': ('k', 'k'), 'j': ('y', 'j'), 'k': ('k', 'k'), 'q': ('k', 'k'),
        's': ('s', 's'), 'x': ('s', 'x'), 'z': ('s', 'z'), 'd': ('t', 't'), 't': ('t', 't'),
        'l': ('l', 'l'), 'm': ('m', 'm'), 'n': ('n', 'n'), 'r': ('r', 'r'),
        'w': ('w', 'w'), 'y': ('y', 'y')
    }

    # Helper function for handling specific cases for both primary and secondary encoding
    def apply_special_rules(i, char, primary, secondary):
        if char == 'c':
            if i + 1 < len(word) and word[i + 1] in 'ei':  # "ce", "ci" -> 's'
                primary.append('s')
                secondary.append('s')
            elif i + 1 < len(word) and word[i + 1] == 'h':  # "ch" -> 'x'
                primary.append('x')
                secondary.append('x')
            else:
                primary.append('k')
                secondary.append('k')

        elif char == 'g':
            if i + 1 < len(word) and word[i + 1] == 'h':  # "gh" -> 'f'
                primary.append('f')
                secondary.append('f')
            elif i + 1 < len(word) and word[i + 1] in 'ei':  # "ge", "gi" -> 'j'
                primary.append('j')
                secondary.append('j')
            else:
                primary.append('k')
                secondary.append('k')

        elif char == 'p':
            if i + 1 < len(word) and word[i + 1] == 'h':  # "ph" -> 'f'
                primary.append('f')
                secondary.append('f')
            else:
                primary.append('f')
                secondary.append('f')

        elif char == 's':
            if i + 1 < len(word) and word[i + 1] == 'h':  # "sh" -> 's'
                primary.append('s')
                secondary.append('s')
            elif i + 1 < len(word) and word[i + 1] == 'c':  # "sc" -> 's'
                primary.append('s')
                secondary.append('s')
            else:
                primary.append('s')
                secondary.append('s')

        elif char == 't':
            if i + 1 < len(word) and word[i + 1] == 'h':  # "th" -> '0'
                primary.append('0')
                secondary.append('0')
            elif i + 1 < len(word) and word[i + 1] == 'w':  # "tw" -> 't'
                primary.append('t')
                secondary.append('t')
            else:
                primary.append('t')
                secondary.append('t')

        elif char == 'w':
            if i == 0 or word[i - 1] not in 'aeiou':  # 'w' at the beginning
                primary.append('w')
                secondary.append('w')

        elif char == 'y':
            if i == 0 or word[i - 1] not in 'aeiou':  # 'y' at the beginning
                primary.append('y')
                secondary.append('y')

        elif char == 'h':
            # Handle 'h' depending on the letters before or after it
            if i == 0 or word[i - 1] not in 'aeiou':
                primary.append('')
                secondary.append('')

        else:
            primary.append(phonetic_map.get(char, ('', ''))[0])
            secondary.append(phonetic_map.get(char, ('', ''))[1])

    i = 0
    while i < len(word):
        char = word[i]

        # Handle vowels and special conditions (e.g., first character)
        if char in 'aeiou':
            if i == 0 or word[i - 1] not in 'aeiou':  # Avoid repeating vowels
                primary.append('0')
                secondary.append('0')

        else:
            apply_special_rules(i, char, primary, secondary)

        i += 1

    return ''.join(primary), ''.join(secondary)


# Example Usage:
word = "philosophy"
primary_key, secondary_key = double_metaphone(word)
print(f"Double Metaphone encoding of '{word}':")
print(f"Primary: {primary_key}")
print(f"Secondary: {secondary_key}")
