import base64
from collections import Counter

# Taken from the lecture slide.
UNIGRAM_FOR_ENGLISH = {
    "a": 0.080,
    "b": 0.015,
    "c": 0.030,
    "d": 0.040,
    "e": 0.130,
    "f": 0.020,
    "g": 0.015,
    "h": 0.060,
    "i": 0.065,
    "j": 0.005,
    "k": 0.005,
    "l": 0.035,
    "m": 0.030,
    "n": 0.070,
    "o": 0.080,
    "p": 0.020,
    "q": 0.002,
    "r": 0.065,
    "s": 0.060,
    "t": 0.090,
    "u": 0.030,
    "v": 0.010,
    "w": 0.015,
    "x": 0.005,
    "y": 0.020,
    "z": 0.002,
}


def perform_statistical_analysis(ciphertext):
    # Ciphertext is encoded as base64, so decode it first.
    ciphertext = base64.b64decode(ciphertext)

    freq = {k: v / len(ciphertext) for k, v in Counter(ciphertext).items()}

    correl = {}
    # There are 256 (2^8) possible keys from 0 to 255 because encyption algorithm uses bytearray
    # which stores each element as a byte (8 bits).
    for k in range(256):
        for c, f in freq.items():
            # Character we would get when `c` is decrypted with the key `k`. Encryption algorithm
            # uses "Stream Cipher".
            decrypted_char = chr(c ^ k)
            # For every possible key, calculate the correlation of frequency of letters in ciphertext
            # with corresponding letters in English. If the `decrypted_char` is not a English character,
            # use 0 as a default value for its frequency in English.
            correl[k] = correl.get(k, 0) + (
                f * UNIGRAM_FOR_ENGLISH.get(decrypted_char, 0)
            )

    # Sort correlation table in descending order based on correlation.
    return dict(sorted(correl.items(), key=lambda x: x[1], reverse=True))


def decipher(ciphertext, key):
    ciphertext = base64.b64decode(ciphertext)
    res = [chr(c ^ key) for c in ciphertext]
    return "".join(res)


def main():
    ciphertext = "OhVTChwGUxEBFhIYUwcbGgBTEBoDGxYBBxYLB19TGgdTHhYSHQBTBxsSB1MKHAZTEgEWUxIRHxZTBxxTEQEWEhhTAAYRAAcaBwYHGhwdUxAaAxsWAQBTBgAaHRRTFQEWAgYWHRAKUxIdEh8KABoAXVMkFh8fUzccHRZS"

    correlation_table = perform_statistical_analysis(ciphertext)

    print()
    print("=== Key and correlation table ===")
    print()
    # Correlation table is already sorted in descending order based on correlation.
    for key, correl in correlation_table.items():
        print(f"Key: {key:03d}, Correlation: {correl:.4f}")

    print()
    print("=== Deciphered Text and Key ===")
    print()
    for k in correlation_table:
        print(f"Key: {k} or '{chr(k)}'")
        print(f"Text: {decipher(ciphertext, k)}")
        # For this specific case, key with highest correaltion was able to decrypt the ciphered
        # text. But that might not always be the case.
        break


if __name__ == "__main__":
    main()
