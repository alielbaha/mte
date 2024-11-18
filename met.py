def metaphone(word):
    word = word.lower()
    result = []

    # Phonetic mappings using dictionary for simple consonants and vowels
    phonetic_map = {
        'a': '0', 'e': '0', 'i': '0', 'o': '0', 'u': '0',
        'b': 'b', 'f': 'f', 'p': 'f', 'v': 'f',
        'c': 'k', 'g': 'k', 'j': 'y', 'k': 'k', 'q': 'k',
        's': 's', 'x': 's', 'z': 's', 'd': 't', 't': 't',
        'l': 'l', 'm': 'm', 'n': 'n', 'r': 'r',
        'w': 'w', 'y': 'y'
    }

    # Step through the word and apply phonetic rules
    i = 0
    while i < len(word):
        char = word[i]

        # Vowel handling (vowels are generally replaced by '0')
        if char in 'aeiou':
            if i == 0 or word[i-1] not in 'aeiou':  # First vowel or after a consonant
                result.append(phonetic_map.get(char, ''))

        # Consonant handling (consonant rules and special cases)
        elif char in phonetic_map:
            # Handle specific letter combinations
            if char == 'c':
                if i + 1 < len(word) and word[i + 1] in 'ei':
                    result.append('s')  # "ce", "ci" -> 's'
                elif i + 1 < len(word) and word[i + 1] == 'h':  # "ch" -> 'x'
                    result.append('x')
                else:
                    result.append('k')
            elif char == 'g':
                if i + 1 < len(word) and word[i + 1] == 'h':  # "gh" -> 'f'
                    result.append('f')
                elif i + 1 < len(word) and word[i + 1] in 'ei':  # "ge", "gi" -> 'j'
                    result.append('j')
                else:
                    result.append('k')
            elif char == 'p':
                if i + 1 < len(word) and word[i + 1] == 'h':  # "ph" -> 'f'
                    result.append('f')
                else:
                    result.append('f')
            elif char == 's':
                if i + 1 < len(word) and word[i + 1] == 'h':  # "sh" -> 's'
                    result.append('s')
                else:
                    result.append('s')
            elif char == 't':
                if i + 1 < len(word) and word[i + 1] == 'h':  # "th" -> '0' (voiceless "th")
                    result.append('0')
                elif i + 1 < len(word) and word[i + 1] == 'w':  # "tw" -> 't'
                    result.append('t')
                else:
                    result.append('t')
            elif char == 'w':
                if i == 0 or word[i-1] not in 'aeiou':  # 'w' at the beginning, before a vowel
                    result.append('w')
            elif char == 'y':
                if i == 0 or word[i-1] not in 'aeiou':  # 'y' at the beginning, before a vowel
                    result.append('y')
            else:
                result.append(phonetic_map[char])
        
        i += 1

    return ''.join(result)


# Example Usage:
word = "philosophy"
encoded_word = metaphone(word)
print(f"Metaphone encoding of '{word}': {encoded_word}")
