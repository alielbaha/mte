def metaphone(word):
    word = word.lower()
    result = []

    # Phonetic mappings
    phonetic_map = {
        'a': '0', 'e': '0', 'i': '0', 'o': '0', 'u': '0',
        'b': 'b', 'f': 'f', 'p': 'f', 'v': 'f',
        'c': 'k', 'g': 'k', 'j': 'y', 'k': 'k', 'q': 'k',
        's': 's', 'x': 's', 'z': 's', 'd': 't', 't': 't',
        'l': 'l', 'm': 'm', 'n': 'n', 'r': 'r',
        'w': 'w', 'y': 'y'
    }

    # Avoid unnecessary checks
    i = 0
    while i < len(word):
        char = word[i]

        # Skip if the current character is a vowel and it's the same as the previous one
        if char in 'aeiou' and (i == 0 or word[i - 1] not in 'aeiou'):
            result.append(phonetic_map.get(char, ''))

        # Handle consonants based on context
        elif char in phonetic_map:
            if char == 'c':
                # 'c' followed by 'e' or 'i' becomes 's', else 'k'
                result.append('s' if i + 1 < len(word) and word[i + 1] in 'ei' else 'k')
            elif char == 'g':
                # 'g' followed by 'h' becomes 'f', else 'k' or 'j' depending on next letter
                result.append('f' if i + 1 < len(word) and word[i + 1] == 'h' else ('j' if i + 1 < len(word) and word[i + 1] in 'ei' else 'k'))
            elif char == 'p':
                # 'ph' becomes 'f'
                result.append('f' if i + 1 < len(word) and word[i + 1] == 'h' else 'f')
            elif char == 's':
                # 'sh' becomes 's'
                result.append('s' if i + 1 < len(word) and word[i + 1] == 'h' else 's')
            elif char == 't':
                # 'th' becomes '0' (voiceless 'th')
                result.append('0' if i + 1 < len(word) and word[i + 1] == 'h' else 't')
            elif char == 'w':
                # 'w' is kept only if it's at the beginning or before a vowel
                if i == 0 or word[i - 1] not in 'aeiou':
                    result.append('w')
            elif char == 'y':
                # 'y' is kept only if it's at the beginning or before a vowel
                if i == 0 or word[i - 1] not in 'aeiou':
                    result.append('y')
            else:
                result.append(phonetic_map[char])

        i += 1

    return ''.join(result)


# Example Usage:
word = "philosophy"
encoded_word = metaphone(word)
print(f"Metaphone encoding of '{word}': {encoded_word}")
