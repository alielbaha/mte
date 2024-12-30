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
Postprocessing:
Handle duplicate removal and zero-padding.


