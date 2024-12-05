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
