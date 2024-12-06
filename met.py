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
