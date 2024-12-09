import time
import matplotlib.pyplot as plt
from rapidfuzz import fuzz as rf_fuzz
from fuzzywuzzy import fuzz as fw_fuzz
import textdistance
import pandas as pd

# Sample Dataset
name_pairs = [
    ("John", "Jon"),
    ("Smith", "Smythe"),
    ("Michael", "Mike"),
    ("Robert", "Rob"),
    ("Elizabeth", "Elisabeth"),
    ("Chris", "Kris"),
    ("Aaron", "Aaran"),
    ("Matthew", "Mathew"),
    ("Catherine", "Katherine"),
    ("Jonathan", "Jon"),
]

# Algorithms to Benchmark
algorithms = {
    "FuzzyWuzzy (Ratio)": lambda x, y: fw_fuzz.ratio(x, y),
    "RapidFuzz (Ratio)": lambda x, y: rf_fuzz.ratio(x, y),
    "Levenshtein Distance": lambda x, y: textdistance.levenshtein.normalized_similarity(x, y) * 100,
    "Jaro-Winkler": lambda x, y: textdistance.jaro_winkler(x, y) * 100,
}

# Benchmark Function
def benchmark(algorithms, name_pairs):
    results = {alg: [] for alg in algorithms}
    timings = {alg: [] for alg in algorithms}

    for alg, func in algorithms.items():
        for name1, name2 in name_pairs:
            start_time = time.time()
            score = func(name1, name2)
            elapsed_time = time.time() - start_time

            results[alg].append(score)
            timings[alg].append(elapsed_time)

    return results, timings

# Run Benchmark
scores, times = benchmark(algorithms, name_pairs)

# Convert Results to DataFrames for Plotting
score_df = pd.DataFrame(scores, index=[f"{n1} vs {n2}" for n1, n2 in name_pairs])
time_df = pd.DataFrame(times, index=[f"{n1} vs {n2}" for n1, n2 in name_pairs])

# Plot: Similarity Scores
plt.figure(figsize=(12, 6))
score_df.plot(kind='bar', figsize=(12, 6))
plt.title("Fuzzy Matching Similarity Scores")
plt.ylabel("Similarity (%)")
plt.xlabel("Name Pair")
plt.legend(title="Algorithm")
plt.tight_layout()
plt.show()

# Plot: Computation Times
plt.figure(figsize=(12, 6))
time_df.plot(kind='bar', figsize=(12, 6), color=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title("Fuzzy Matching Computation Time")
plt.ylabel("Time (seconds)")
plt.xlabel("Name Pair")
plt.legend(title="Algorithm")
plt.tight_layout()
plt.show()



##################################################################################à
#runtime comparaison

import random
import string
import time
import matplotlib.pyplot as plt
from difflib import SequenceMatcher
from fuzzywuzzy import fuzz

# Define the algorithms for comparison
def levenshtein_similarity(a, b):
    return fuzz.ratio(a, b)

def jaro_similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def jaro_winkler_similarity(a, b):
    return fuzz.WRatio(a, b)

# Generate 100 pairs of random strings, each pair's total length increases by 1 character
random_pairs = []
base_length = 5  # Starting length for the strings
for i in range(100):
    length1 = base_length + i // 2  # Divide increment between two strings
    length2 = base_length + i - length1
    str1 = ''.join(random.choices(string.ascii_letters, k=length1))
    str2 = ''.join(random.choices(string.ascii_letters, k=length2))
    random_pairs.append([str1, str2])

# Measure runtime with respect to string length for the generated pairs
random_string_lengths = [len(pair[0]) + len(pair[1]) for pair in random_pairs]
runtime_levenshtein = []
runtime_jaro = []
runtime_jaro_winkler = []

for pair in random_pairs:
    name1, name2 = pair
    
    # Levenshtein runtime
    start_time = time.time()
    levenshtein_similarity(name1, name2)
    runtime_levenshtein.append(time.time() - start_time)
    
    # Jaro runtime
    start_time = time.time()
    jaro_similarity(name1, name2)
    runtime_jaro.append(time.time() - start_time)
    
    # Jaro-Winkler runtime
    start_time = time.time()
    jaro_winkler_similarity(name1, name2)
    runtime_jaro_winkler.append(time.time() - start_time)

# Plotting runtime comparison
plt.figure(figsize=(10, 6))
plt.plot(
    random_string_lengths,
    runtime_levenshtein,
    marker="o",
    label="Levenshtein",
)
plt.plot(
    random_string_lengths,
    runtime_jaro,
    marker="s",
    label="Jaro",
)
plt.plot(
    random_string_lengths,
    runtime_jaro_winkler,
    marker="^",
    label="Jaro-Winkler",
)

# Add labels, legend, and title
plt.title("Runtime of Fuzzy Matching Algorithms vs String Length (Random Strings)")
plt.xlabel("String Length (Sum of Pair Lengths)")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.grid()
plt.show()


##################################################################################################
#Recall


import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np


# Evaluate the algorithms for each pair
results = []
for pair in list_of_couples:
    name1, name2 = pair
    results.append({
        "Name 1": name1,
        "Name 2": name2,
        "Levenshtein Similarity": levenshtein_similarity(name1, name2),
        "Jaro Similarity": jaro_similarity(name1, name2) * 100,
        "Jaro Winkler Similarity": jaro_winkler_similarity(name1, name2)
    })

# Convert results to a DataFrame
df_results = pd.DataFrame(results)

# Calculate recall
def calculate_recall(predictions, ground_truth, threshold=80):
    return np.mean([1 if pred >= threshold else 0 for pred in predictions])

# Simulate ground truth matches (100% matches for demonstration)
ground_truth = [100] * len(list_of_couples)

# Calculate recall for each metric
levenshtein_scores = df_results["Levenshtein Similarity"].tolist()
jaro_scores = df_results["Jaro Similarity"].tolist()
jaro_winkler_scores = df_results["Jaro Winkler Similarity"].tolist()

recall_levenshtein = calculate_recall(levenshtein_scores, ground_truth)
recall_jaro = calculate_recall(jaro_scores, ground_truth)
recall_jaro_winkler = calculate_recall(jaro_winkler_scores, ground_truth)

# Time complexity analysis
algorithms = ["Levenshtein", "Jaro", "Jaro-Winkler"]
time_complexities = []

for algo in algorithms:
    start_time = time.time()
    for pair in list_of_couples:
        name1, name2 = pair
        if algo == "Levenshtein":
            levenshtein_similarity(name1, name2)
        elif algo == "Jaro":
            jaro_similarity(name1, name2)
        elif algo == "Jaro-Winkler":
            jaro_winkler_similarity(name1, name2)
    end_time = time.time()
    time_complexities.append(end_time - start_time)

# Plotting recall comparison
plt.figure(figsize=(8, 6))
plt.bar(algorithms, [recall_levenshtein, recall_jaro, recall_jaro_winkler], alpha=0.7)
plt.title("Recall Comparison of Fuzzy Matching Algorithms")
plt.ylabel("Recall")
plt.xlabel("Algorithm")
plt.ylim(0, 1)
plt.show()

# Plotting time complexity comparison
plt.figure(figsize=(8, 6))
plt.bar(algorithms, time_complexities, alpha=0.7)
plt.title("Time Complexity of Fuzzy Matching Algorithms")
plt.ylabel("Time (seconds)")
plt.xlabel("Algorithm")
plt.show()

#####################################################
#list of french names 
list_of_couples_with_boolean = [
    ["Jean Dupont", "Jeanne Dupon"],
    ["Marie-Claire Benoît", "Marianne Claire Benoi"],
    ["Julien Moreau", "Juliette Morel"],
    ["Céline Lambert", "Séline Lambaire"],
    ["Louis Martin", "Louise Martine"],
    ["Émile Durand", "Émilie Durant"],
    ["Antoine Lefèvre", "Antoinette Lefevre"],
    ["Chloé Petit", "Claudine Petie"],
    ["Pierre Garnier", "Perrine Garnie"],
    ["Camille Fontaine", "Camilla Fontin"],
    ["Philippe Gauthier", "Philippa Gautier"],
    ["Hélène Marchand", "Élena Marchande"],
    ["François Bernard", "Francine Bernarde"],
    ["Claire Olivier", "Clara Olivie"],
    ["Nicolas Beaulieu", "Nicole Beauleu"],
    ["Pauline Charpentier", "Paulette Charpent"],
    ["Jacques Rousseau", "Jacqueline Roussel"],
    ["Sophie Lefebvre", "Sophia Lefèvre"],
    ["Thomas Blanc", "Thomé Blanche"],
    ["Isabelle Durieux", "Isabeau Durié"],
    ["Laurent Renard", "Laurette Renarde"],
    ["Charlotte Perrot", "Charline Perron"],
    ["Alain Dupuis", "Aline Dupay"],
    ["Victor Fournier", "Violette Fournière"],
    ["Sandrine Girard", "Sandie Giraud"],
    ["Gilles Richard", "Gillian Richaud"],
    ["Elodie Noel", "Eloine Noël"],
    ["Hugo Vincent", "Hugon Vincente"]]


##########################################
#Soundex 2
import unicodedata
import re

def remove_accents(input_str):
    """
    Removes accents from a string.
    """
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii.decode('utf-8')

def french_soundex2(name):
    """
    Implementation of the French Soundex 2 algorithm.
    :param name: The name or word to encode
    :return: The encoded Soundex 2 value
    """
    # 1. Preprocessing: Remove accents, make uppercase, and remove non-alphabetic characters
    name = remove_accents(name.upper())
    name = re.sub(r'[^A-Z]', '', name)

    # 2. Replace 'Y' with 'I'
    name = name.replace('Y', 'I')

    # 3. Remove 'H' unless preceded by C, P, or S
    name = re.sub(r'([^CPS])H', r'\1', name)

    # 4. Replace 'PH' with 'F'
    name = name.replace('PH', 'F')

    # 5. Replace specific groups
    replacements = {
        'AI': 'Y', 'EI': 'Y', 'AU': 'O', 'EAU': 'O', 'OUA': '2',
        'OI': '2', 'OY': '2', 'OU': '3', 'EIN': '4', 'AIN': '4',
        'EIM': '4', 'AIM': '4', 'CH': '5', 'SCH': '5', 'SH': '5',
        'GN': 'N'
    }
    for key, value in replacements.items():
        name = name.replace(key, value)

    # 6. Handle nasal sounds
    name = re.sub(r'AN([^AEIOU])', r'1\1', name)
    name = re.sub(r'ON([^AEIOU])', r'1\1', name)
    name = re.sub(r'AM([^AEIOU])', r'1\1', name)
    name = re.sub(r'EN([^AEIOU])', r'1\1', name)
    name = re.sub(r'EM([^AEIOU])', r'1\1', name)

    # 7. Replace C followed by E/I with S
    name = re.sub(r'C([EI])', r'S\1', name)

    # 8. Replace remaining consonants
    consonant_replacements = {
        'C': 'K', 'Q': 'K', 'QU': 'K', 'GU': 'K', 'GA': 'KA',
        'GO': 'KO', 'GY': 'KY', 'B': 'F', 'V': 'F', 'D': 'T',
        'P': 'T', 'J': 'G', 'M': 'N'
    }
    for key, value in consonant_replacements.items():
        name = name.replace(key, value)

    # 9. Remove duplicate letters
    result = ''
    for i, char in enumerate(name):
        if i == 0 or char != name[i - 1]:
            result += char

    # 10. Remove trailing 'T' and 'X'
    result = re.sub(r'[TX]$', '', result)

    # 11. Format the result
    if len(result) < 4:
        result += '0' * (4 - len(result))  # Pad with zeros if shorter than 4 characters
    return result[:4]  # Ensure the result is exactly 4 characters

# Example usage
if __name__ == "__main__":
    word = "Brouard"
    soundex_code = french_soundex2(word)
    print(f"French Soundex 2 code for '{word}': {soundex_code}")
################################################################################################
#Phonex 
#!/bin/python
# -*- coding: UTF-8 -*-

# Origine : Algorithme Phonex de Frédéric BROUARD (31/3/99)
# Source : http://sqlpro.developpez.com/cours/soundex
# Version Python : Christian Pennaforte - 5 avril 2005
# Suite : Florent Carlier
# Adaptation Python 3: Ophir LOJKINE

import re
import unicodedata

def remove_accents(input_str):
    """
    >>> remove_accents("héhé")
    "hehe
    """
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii.decode("utf8")

def phonex(chaine):
    """Phonex est un algorithme de Soundex plus perfectionné encore que la version francisée de Soundex2.
    Sachez que Phonex est optimisée pour le langage français, sait reconnaître différents types de sons comme les sons
    ‘on’, ‘ai’, ‘ein’, etc...
    et place son résultat sous la forme d’un réel de type double précision (5.0 x 10-324 .. 1.7 x
    10308 sur 15 à 16 chiffres significatifs). Son temps de calcul est double de Soundex et 30% supérieure seulement
    à Soundex2.

    >>> phonex("PHYLAURHEIMSMET")
    0.29241361598339205

    :param chaine: La chaine de caractères à encoder
    :return: L'encodage sous forme de nombre à virgule flottante
    """
    # 0 On met la chaîne en majuscules, on vire les caractères parasites
    chaine = remove_accents(chaine)
    chaine = re.sub(r"[ \-.+*/,:;_']", "", chaine)
    chaine = chaine.upper()

    # 1 remplacer les y par des i
    r = chaine.replace('Y', 'I')

    # 2 supprimer les h qui ne sont pas précédées de c ou de s ou de p
    r = re.sub(r'([^PCS])H', r'\1', r)

    # 3 remplacement du ph par f
    r = r.replace(r'PH', r'F')

    # 4 remplacer les groupes de lettres suivantes :
    r = re.sub(r'G(AI?[NM])', r'K\1', r)

    # 5 remplacer les occurrences suivantes, si elles sont suivies par une lettre a, e, i, o, ou u :
    r = re.sub(r'[AE]I[NM]([AEIOU])', r'YN\1', r)

    # 6 remplacement de groupes de 3 lettres (sons 'o', 'oua', 'ein') :
    r = r.replace('EAU', 'O')
    r = r.replace('OUA', '2')
    r = r.replace('EIN', '4')
    r = r.replace('AIN', '4')
    r = r.replace('EIM', '4')
    r = r.replace('AIM', '4')

    # 7 remplacement du son É:
    r = r.replace('É', 'Y')  # CP : déjà fait en étape 0
    r = r.replace('È', 'Y')  # CP : déjà fait en étape 0
    r = r.replace('Ê', 'Y')  # CP : déjà fait en étape 0
    r = r.replace('AI', 'Y')
    r = r.replace('EI', 'Y')
    r = r.replace('ER', 'YR')
    r = r.replace('ESS', 'YS')
    r = r.replace('ET', 'YT')  # CP : différence entre la version Delphi et l'algo
    r = r.replace('EZ', 'YZ')

    # 8 remplacer les groupes de 2 lettres suivantes (son â..anâ.. et â..inâ..), sauf sâ..il sont suivi par une
    # lettre a, e, i o, u ou un son 1 Ã  4 :
    r = re.sub(r'AN([^AEIOU1234])', r'1\1', r)
    r = re.sub(r'ON([^AEIOU1234])', r'1\1', r)
    r = re.sub(r'AM([^AEIOU1234])', r'1\1', r)
    r = re.sub(r'EN([^AEIOU1234])', r'1\1', r)
    r = re.sub(r'EM([^AEIOU1234])', r'1\1', r)
    r = re.sub(r'IN([^AEIOU1234])', r'4\1', r)

    # 9 remplacer les s par des z sâ..ils sont suivi et précédés des lettres a, e, i, o,u ou dâ..un son 1 Ã  4
    r = re.sub(r'([AEIOUY1234])S([AEIOUY1234])', r'\1Z\2', r)
    # CP : ajout du Y Ã  la liste

    # 10 remplacer les groupes de 2 lettres suivants :
    r = r.replace('OE', 'E')
    r = r.replace('EU', 'E')
    r = r.replace('AU', 'O')
    r = r.replace('OI', '2')
    r = r.replace('OY', '2')
    r = r.replace('OU', '3')

    # 11 remplacer les groupes de lettres suivants
    r = r.replace('CH', '5')
    r = r.replace('SCH', '5')
    r = r.replace('SH', '5')
    r = r.replace('SS', 'S')
    r = r.replace('SC', 'S')  # CP : problème pour PASCAL, mais pas pour PISCINE ?

    # 12 remplacer le c par un s s'il est suivi d'un e ou d'un i
    # CP : à mon avis, il faut inverser 11 et 12 et ne pas faire la dernière ligne du 11
    r = re.sub(r'C([EI])', r'S\1', r)

    # 13 remplacer les lettres ou groupe de lettres suivants :
    r = r.replace('C', 'K')
    r = r.replace('Q', 'K')
    r = r.replace('QU', 'K')
    r = r.replace('GU', 'K')
    r = r.replace('GA', 'KA')
    r = r.replace('GO', 'KO')
    r = r.replace('GY', 'KY')

    # 14 remplacer les lettres suivante :
    r = r.replace('A', 'O')
    r = r.replace('D', 'T')
    r = r.replace('P', 'T')
    r = r.replace('J', 'G')
    r = r.replace('B', 'F')
    r = r.replace('V', 'F')
    r = r.replace('M', 'N')

    # 15 Supprimer les lettres dupliquées
    oldc = '#'
    newr = ''
    for c in r:
        if oldc != c: newr = newr + c
        oldc = c
    r = newr

    # 16 Supprimer les terminaisons suivantes : t, x
    r = re.sub(r'(.*)[TX]$', r'\1', r)

    # 17 Affecter à chaque lettre le code numérique correspondant en partant de la dernière lettre
    num = ['1', '2', '3', '4', '5', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'N', 'O', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']
    l = []
    for c in r:
        l.append(num.index(c))

    # 18 Convertissez les codes numériques ainsi obtenu en un nombre de base 22 exprimé en virgule flottante.
    res = 0.
    i = 1
    for n in l:
        res = n * 22 ** -i + res
        i = i + 1

    return res


#################################################
#Soundex 2
def soundex2(s_in: str) -> str:
    # Define constants
    Voyelle = ['E', 'I', 'O', 'U']
    Combin1 = [
        ('GUI', 'KI'), ('GUE', 'KE'), ('GA', 'KA'), ('GO', 'KO'), ('GU', 'K'),
        ('CA', 'KA'), ('CO', 'KO'), ('CU', 'KU'), ('Q', 'K'), ('CC', 'K'), ('CK', 'K')
    ]
    Combin2 = [
        ('ASA', 'AZA'), ('KN', 'NN'), ('PF', 'FF'), ('PH', 'FF'), ('SCH', 'SSS')
    ]
    
    # Helper function: SearchReplace
    def search_replace(string, old, new):
        return string.replace(old, new)

    # Step 0: Handle trivial case
    if not s_in:
        return '    '
    
    # Step 1-3: Prepare the string
    s_in = s_in.upper()
    s_in = s_in.replace('É', 'E').replace('È', 'E').replace('Ç', 'C').replace('À', 'A').replace('Ù', 'U')  # Convert accents
    
    l_sin = len(s_in)

    # Step 4: Handle single-character input
    if l_sin == 1:
        return s_in + '   '
    
    # Step 5: Replace primary consonants
    for old, new in Combin1:
        s_in = search_replace(s_in, old, new)
    
    # Step 6: Replace vowels except Y (and not the first letter)
    s_in2 = s_in[1:]
    for vowel in Voyelle:
        s_in2 = search_replace(s_in2, vowel, 'A')
    s_in = s_in[0] + s_in2
    
    # Step 7: Replace prefixes
    l_sin = len(s_in)
    if l_sin >= 2:
        prfx = s_in[:2]
        if prfx == 'KN':
            prfx = 'NN'
        if prfx in ['PH', 'PF']:
            prfx = 'FF'
        if l_sin == 2:
            s_in = prfx
        else:
            s_in = prfx + s_in[2:]
    if l_sin >= 3:
        prfx = s_in[:3]
        if prfx == 'MAC':
            prfx = 'MCC'
        if prfx == 'SCH':
            prfx = 'SSS'
        if prfx == 'ASA':
            prfx = 'AZA'
        if l_sin == 3:
            s_in = prfx
        else:
            s_in = prfx + s_in[3:]
    
    # Step 8: Replace complementary combinations
    s_in2 = s_in[1:]
    for old, new in Combin2:
        s_in2 = search_replace(s_in2, old, new)
    s_in = s_in[0] + s_in2
    
    # Step 9: Remove H except in CH or SH
    l_sin = len(s_in)
    s_in2 = ''
    for i in range(l_sin):
        if s_in[i] != 'H' or (i > 0 and s_in[i - 1] in ['C', 'S']):
            s_in2 += s_in[i]
    s_in = s_in2
    
    # Step 10: Remove Y except after A
    s_in2 = ''
    for i in range(len(s_in)):
        if s_in[i] != 'Y' or (i > 0 and s_in[i - 1] == 'A'):
            s_in2 += s_in[i]
    s_in = s_in2
    
    # Step 11: Remove endings A, T, D, S
    if s_in[-1] in ['A', 'T', 'D', 'S']:
        s_in = s_in[:-1]
    
    # Step 12: Remove all A except at the start
    s_in2 = s_in[0]
    for i in range(1, len(s_in)):
        if s_in[i] != 'A':
            s_in2 += s_in[i]
    s_in = s_in2
    
    # Step 13: Remove repeated letters
    s_in2 = s_in[0]
    for i in range(1, len(s_in)):
        if s_in[i] != s_in[i - 1]:
            s_in2 += s_in[i]
    s_in = s_in2
    
    # Step 14: Retain only 4 characters, pad if necessary
    s_in = s_in[:4]
    s_in = s_in.ljust(4)
    
    return s_in



#############################################################################
#Soundex 2 corrected



import unicodedata
import re

def remove_accents(input_str):
    """
    Removes accents from the input string and converts 'Ç' to 'C'.
    """
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)]).replace('Ç', 'C')

def french_soundex2(name):
    """
    Implements the French Soundex 2 algorithm as described in SQLPro's guide.
    :param name: The input string to encode
    :return: The Soundex 2 encoded string
    """
    # 1. Preprocessing: Remove accents, convert to uppercase, remove spaces and hyphens
    name = remove_accents(name.upper())
    name = re.sub(r'[^\w]', '', name)  # Remove non-alphanumeric characters

    if not name:
        return "0000"  # Return a default value for empty input

    # 2. Phonetic transformations
    # Replace specific letter groups
    replacements = {
        "GUI": "KI", "GUE": "KE", "GA": "KA", "GO": "KO", "GU": "KU",
        "MAC": "MCC", "KN": "NN", "PF": "FF", "SCH": "SS", "PH": "F"
    }
    for key, value in replacements.items():
        name = name.replace(key, value)

    # Replace vowels (except the first letter)
    vowels = "AEIOUY"
    first_letter = name[0]
    name = first_letter + re.sub(f"[{vowels}]", "A", name[1:])

    # Remove 'H' unless preceded by 'C' or 'S'
    name = re.sub(r'([^CS])H', r'\1', name)

    # Remove 'Y' unless preceded by 'A'
    name = re.sub(r'([^A])Y', r'\1', name)

    # Remove terminal 'A', 'T', 'D', 'S'
    name = re.sub(r'[ATDS]$', '', name)

    # Remove all 'A's except the initial one
    name = first_letter + name[1:].replace("A", "")

    # Eliminate consecutive duplicate letters
    result = name[0]
    for char in name[1:]:
        if char != result[-1]:
            result += char

    # 3. Finalization: Retain first four characters, pad with zeros if necessary
    return (result + "0000")[:4]

# Example usage
if __name__ == "__main__":
    word = "Brouard"
    soundex_code = french_soundex2(word)
    print(f"French Soundex 2 code for '{word}': {soundex_code}")

    word2 = "Michel"
    soundex_code2 = french_soundex2(word2)
    print(f"French Soundex 2 code for '{word2}': {soundex_code2}")

################################################################################################



##########################################################
\documentclass{article}
\usepackage{pgfgantt}

\begin{document}

\section*{Gantt Chart Example}

\begin{ganttchart}[
    vgrid,
    hgrid,
    title/.append style={fill=blue!10},
    title label font=\bfseries\footnotesize,
    bar/.append style={fill=blue!50},
    bar label font=\footnotesize\textbf,
    milestone/.append style={fill=red},
    milestone label font=\footnotesize\textit
]{1}{12} % Timeline from month 1 to 12

% Define the chart title
\gantttitle{2024}{12} \\

% Months
\gantttitlelist{1,...,12}{1} \\

% Add tasks
\ganttbar{Task 1}{1}{3} \\
\ganttlinkedbar{Task 2}{4}{6} \\
\ganttlinkedbar{Task 3}{7}{10} \\

% Add a milestone
\ganttmilestone{Milestone 1}{11} \\

% Add a group
\ganttgroup{Project Phase 1}{1}{6}

\end{ganttchart}

\end{document}

