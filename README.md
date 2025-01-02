Developed in the early 20th century by Robert C. Russell and Margaret K. Odell, the Soundex algorithm focuses on encoding names and words based on how they sound in English. Unlike traditional edit-distance metrics, Soundex prioritizes phonetic similarity, enabling it to handle variations in spelling that sound similar when spoken (e.g., "Smith" and "Smyth").



Soundex encodes words into a fixed-length alphanumeric code. The algorithm processes input strings as follows:
1. Retain the First Letter:
      - Keep the first letter of the word (converted to uppercase).

2. Encode the Remaining Letters using the following table




3.Remove Adjacent Duplicates

4. Exclude the letters A, E, I, O, U, H, W, and Y (unless they are the first letter)

5. Ensure the resulting code is exactly 4 characters by truncating digits or appending zeros.

Preprocessing:
Convert the input to uppercase.
Encoding Loop:
Iterate through the string to map and process each character.




# String Matching Algorithms Benchmark

This repository contains implementations, benchmarks, stress tests, and visualizations of famous string matching algorithms. These algorithms are widely used in various fields like text processing, natural language processing, and data deduplication. The repository aims to provide a comprehensive comparison of the algorithms in terms of efficiency and accuracy.

## Implemented Algorithms

1. **Hamming Distance**  
   Calculates the number of positions at which the corresponding characters of two equal-length strings differ.

2. **Damerau Distance (Transpositions Only)**  
   Extends the Hamming Distance by including transpositions, i.e., swapping two adjacent characters.

3. **Levenshtein Distance**  
   Measures the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into the other.

4. **Damerau-Levenshtein Distance**  
   An enhanced version of Levenshtein Distance that includes transpositions as valid edits.

5. **Jaro Similarity (Jaro Distance)**  
   A metric for comparing two strings based on character matching and transpositions, emphasizing their similarity.

## Benchmarks and Stress Tests

The repository includes detailed benchmarks and stress tests for the algorithms under various conditions:
- **Input Size:** Small to large strings.
- **Character Sets:** Different types of character distributions.
- **Performance Metrics:** Execution time, memory usage, and accuracy.

## Visualizations

Graphical representations of the results provide insights into:
- Algorithmic efficiency under different scenarios.
- The trade-offs between execution time and accuracy.

## Repository Structure

```plaintext
.
├── algorithms/
│   ├── hamming.py
│   ├── damerau.py
│   ├── levenshtein.py
│   ├── damerau_levenshtein.py
│   └── jaro.py
├── benchmarks/
│   ├── performance_tests.py
│   ├── stress_tests.py
│   └── visualization.ipynb
├── data/
│   └── sample_inputs.txt
├── results/
│   ├── benchmark_results.csv
│   └── visualizations/
├── README.md
└── LICENSE

Postprocessing:
Handle duplicate removal and zero-padding.


