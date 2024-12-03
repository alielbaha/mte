# search and replace a substring
def search_replace(s_in: str, mot1: str, mot2: str) -> str:
    
    if mot1 == mot2:
        return s_in

    # Handle replacement
    while mot1 in s_in:
        pos_mot = s_in.find(mot1)
        taille_sin = len(s_in)
        taille_mot = len(mot1)

        if pos_mot == 0:  # If the word to replace is at the start
            s_in = mot2 + s_in[taille_mot:]
        elif pos_mot + taille_mot == taille_sin:  # If the word to replace is at the end
            s_in = s_in[:pos_mot] + mot2
        else:  # If the word to replace is in the middle
            s_in = s_in[:pos_mot] + mot2 + s_in[pos_mot + taille_mot:]

    return s_in

# French soundex 
def soundex2(s_in: str) -> str:
    vowels = ['E', 'I', 'O', 'U']
    combin1 = [
        ('GUI', 'KI'), ('GUE', 'KE'), ('GA', 'KA'), ('GO', 'KO'), ('GU', 'K'),
        ('CA', 'KA'), ('CO', 'KO'), ('CU', 'KU'), ('Q', 'K'), ('CC', 'K'), ('CK', 'K')
    ]
    combin2 = [
        ('ASA', 'AZA'), ('KN', 'NN'), ('PF', 'FF'), ('PH', 'FF'), ('SCH', 'SSS')
    ]


    if not s_in:
        return '    '

    # Step 1, 2, 3: Prepare the string
    s_in = s_in.upper().replace('É', 'E').replace('È', 'E').replace('Ç', 'C')
    l_sin = len(s_in)

    # Handle single character strings
    if l_sin == 1:
        return s_in.ljust(4)

    # Step 5
    for old, new in combin1:
        s_in = search_replace(s_in, old, new)

    # Step 6
    s_in2 = s_in[1:]
    for vowel in vowels:
        s_in2 = search_replace(s_in2, vowel, 'A')
    s_in = s_in[0] + s_in2

    # Step 7
    if len(s_in) >= 2:
        prfx = s_in[:2]
        if prfx in ['KN']:
            prfx = 'NN'
        elif prfx in ['PH', 'PF']:
            prfx = 'FF'
        s_in = prfx + s_in[2:]
    if len(s_in) >= 3:
        prfx = s_in[:3]
        if prfx == 'MAC':
            prfx = 'MCC'
        elif prfx == 'SCH':
            prfx = 'SSS'
        elif prfx == 'ASA':
            prfx = 'AZA'
        s_in = prfx + s_in[3:]

 
    s_in2 = s_in[1:]
    for old, new in combin2:
        s_in2 = search_replace(s_in2, old, new)
    s_in = s_in[0] + s_in2

    s_in2 = ''
    for i, char in enumerate(s_in):
        if char == 'H' and (i == 0 or s_in[i - 1] not in ['C', 'S']):
            continue
        s_in2 += char
    s_in = s_in2

    s_in2 = ''
    for i, char in enumerate(s_in):
        if char == 'Y' and (i == 0 or s_in[i - 1] != 'A'):
            continue
        s_in2 += char
    s_in = s_in2


    if s_in[-1] in ['A', 'D', 'S', 'T']:
        s_in = s_in[:-1]

   
    s_in2 = s_in[0]
    for char in s_in[1:]:
        if char != 'A':
            s_in2 += char
    s_in = s_in2

   
    s_in2 = s_in[0]
    for char in s_in[1:]:
        if char != s_in2[-1]:
            s_in2 += char
    s_in = s_in2

    
    s_in = s_in[:4].ljust(4)

    return s_in





### Phonex dependecies 
def search_replace(s_in, mot1, mot2):
    # Handle the edge case where mot1 and mot2 are the same
    if mot1 == mot2:
        return s_in

    # Replace all occurrences of mot1 with mot2
    taille_mot = len(mot1)
    pos_mot = s_in.find(mot1)

    while pos_mot != -1:
        if pos_mot == 0:
            s_in = mot2 + s_in[taille_mot:]
        elif pos_mot + taille_mot == len(s_in):
            s_in = s_in[:pos_mot] + mot2
        else:
            s_in = s_in[:pos_mot] + mot2 + s_in[pos_mot + taille_mot:]

        pos_mot = s_in.find(mot1)

    return s_in

def sr_sauf_voyelle(s_in, mot1, mot2):
    voyelle = {'a', 'e', 'i', 'o', 'u', 'y', '1', '2', '3', '4'}

    if mot1 == mot2:
        return s_in

    taille_mot = len(mot1)
    pos_mot = s_in.find(mot1)

    while pos_mot != -1:
        if pos_mot + taille_mot < len(s_in):
            der_let = s_in[pos_mot + taille_mot]
            if der_let in voyelle:
                return s_in

        if pos_mot == 0:
            s_in = mot2 + s_in[taille_mot:]
        elif pos_mot + taille_mot == len(s_in):
            s_in = s_in[:pos_mot] + mot2
        else:
            s_in = s_in[:pos_mot] + mot2 + s_in[pos_mot + taille_mot:]

        pos_mot = s_in.find(mot1)

    return s_in

def sr_sauf_2_voyelle(s_in, mot1, mot2):
    voyelle = {'a', 'e', 'i', 'o', 'u', 'y', '1', '2', '3', '4'}

    if mot1 == mot2:
        return s_in

    taille_mot = len(mot1)
    pos_mot = s_in.find(mot1)

    while pos_mot != -1:
        if pos_mot > 0 and pos_mot + taille_mot < len(s_in):
            prem_let = s_in[pos_mot - 1]
            der_let = s_in[pos_mot + taille_mot]

            if not (prem_let in voyelle and der_let in voyelle):
                return s_in

        if pos_mot == 0:
            s_in = mot2 + s_in[taille_mot:]
        elif pos_mot + taille_mot == len(s_in):
            s_in = s_in[:pos_mot] + mot2
        else:
            s_in = s_in[:pos_mot] + mot2 + s_in[pos_mot + taille_mot:]

        pos_mot = s_in.find(mot1)

    return s_in

# Example usage
if __name__ == "__main__":
    example_string = "example test string test"
    print("SearchReplace:", search_replace(example_string, "test", "check"))

    example_string = "testa testa testa"
    print("SRSaufVoyelle:", sr_sauf_voyelle(example_string, "test", "check"))

    example_string = "atestb btesta atesta"
    print("SRSauf2Voyelle:", sr_sauf_2_voyelle(example_string, "test", "check"))


#Phonex algorithm

import math

def phonex(s_in):
    # Define constants
    son_aia = ['aina', 'eina', 'aima', 'eima']
    son_aie = ['aine', 'eine', 'aime', 'eime']
    son_aii = ['aini', 'eini', 'aimi', 'eimi']
    son_aio = ['aino', 'eino', 'aimo', 'eimo']
    son_aiu = ['ainu', 'einu', 'aimu', 'eimu']
    car_phon = ['1', '2', '3', '4', '5', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'n', 'o', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']

    # Edge case: empty string
    if not s_in:
        return 0.0

    # Convert to lowercase
    s_in = s_in.lower()

    # Replace 'y' with 'i'
    s_in = s_in.replace('y', 'i')

    # Replace accented letters
    accents = {
        'â': 'a', 'ä': 'a', 'à': 'a',
        'ç': 's',
        'ë': 'e', 'œ': 'e',
        'ï': 'i', 'î': 'i',
        'ô': 'o', 'ö': 'o',
        'ù': 'u', 'û': 'u', 'ü': 'u',
        'é': 'y', 'ê': 'y', 'è': 'y'
    }
    s_in = ''.join(accents.get(char, char) for char in s_in)

    # Remove silent 'h'
    while 'h' in s_in:
        pos = s_in.find('h')
        if pos == 0:
            s_in = s_in[1:]
        elif pos > 0 and (s_in[pos - 1] not in ['c', 's']):
            s_in = s_in[:pos] + s_in[pos + 1:]

    # Replace 'ph' with 'f'
    s_in = s_in.replace('ph', 'f')

    # Replace 'g' sounding 'k' before certain combinations
    replacements = {
        'gan': 'kan', 'gain': 'kain',
        'gam': 'kam', 'gaim': 'kaim'
    }
    for key, value in replacements.items():
        s_in = s_in.replace(key, value)

    # Replace AI sounds
    for i in range(4):
        s_in = s_in.replace(son_aia[i], 'yna')
        s_in = s_in.replace(son_aie[i], 'yne')
        s_in = s_in.replace(son_aii[i], 'yni')
        s_in = s_in.replace(son_aio[i], 'yno')
        s_in = s_in.replace(son_aiu[i], 'ynu')

    # Replace specific groups of letters
    group_replacements = {
        'eau': 'o', 'oua': '2', 'ein': '4', 'ain': '4',
        'ai': 'y', 'ei': 'y', 'er': 'yr', 'ess': 'yss', 'et': 'yt', 'ez': 'yz',
        'oe': 'e', 'eu': 'e', 'au': 'o', 'oi': '2', 'oy': '2', 'ou': '3',
        'ch': '5', 'sh': '5', 'ss': 's', 'sc': 's'
    }
    for key, value in group_replacements.items():
        s_in = s_in.replace(key, value)

    # Replace 'c' with 's' if followed by 'e' or 'i'
    s_in = s_in.replace('ce', 'se').replace('ci', 'si')

    # Replace other consonants
    consonant_replacements = {
        'c': 'k', 'q': 'k', 'qu': 'k',
        'ga': 'ka', 'go': 'ko', 'gu': 'ku', 'gy': 'ky',
        'g2': 'k2', 'g1': 'k1', 'g3': 'k3',
        'a': 'o', 'd': 't', 'p': 't', 'j': 'g',
        'b': 'f', 'v': 'f', 'm': 'n'
    }
    for key, value in consonant_replacements.items():
        s_in = s_in.replace(key, value)

    # Remove duplicate letters
    s_in2 = s_in[0] if s_in else ''
    for i in range(1, len(s_in)):
        if s_in[i] != s_in[i - 1]:
            s_in2 += s_in[i]
    s_in = s_in2

    # Remove endings
    if s_in and s_in[-1] in ['t', 'x', 's', 'z']:
        s_in = s_in[:-1]

    # Remove unauthorized characters
    s_out = []
    for char in s_in:
        if char in car_phon:
            s_out.append(car_phon.index(char))

    # Convert to float
    result = 0.0
    for i, value in enumerate(reversed(s_out)):
        result += value * math.pow(22, i)

    return result

# Example usage
if __name__ == "__main__":
    print(phonex("example string"))



