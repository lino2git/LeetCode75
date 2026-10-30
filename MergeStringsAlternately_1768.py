def mergeAlternately(word1: str, word2: str) -> str:
    merged = []
    i, j = 0, 0
    len1, len2 = len(word1), len(word2)

    # 1. Check word length
    if len1 < 1 or len2 < 1:
        print("Break: word1.length or word2.length < 1")
        return ""
    elif len1 > 100 or len2 > 100:
        print("Break: word1.length or word2.length > 100")
        return ""

    # 2. Check lowercase
    if not word1.islower() or not word2.islower():
        print("Break: word1 and word2 must consist of lowercase English letters.")
        return ""

    # 3. Ensures characters are purely alphabetic (A-Z, a-z)
    if not word1.isalpha()  or not word2.isalpha():
        print("Break: Strings must contain only English letters (no numbers or special characters like !, ?, %).")
        return ""

    # Alternate characters while both strings have remaining characters
    while i < len1 and j < len2:
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1
    
    # Append remaining characters from word1 (if any)
    if i < len1:
        merged.append(word1[i:])
        
    # Append remaining characters from word2 (if any)
    if j < len2:
        merged.append(word2[j:])
        
    return "".join(merged)

# Run manually
if __name__ == "__main__":
    print(mergeAlternately("abc", "pqr"))  # Expected: "apbqcr"
    print(mergeAlternately("ab", "pqrs"))  # Expected: "apbqrs"
    print(mergeAlternately("abcd", "pq"))  # Expected: "apbqcd"

    print(mergeAlternately("", "pqr"))  # Expected: "Break"
    print(mergeAlternately("abc", ""))  # Expected: "Break"
    print(mergeAlternately("ABC", "pqr"))  # Expected: "Break"
    print(mergeAlternately("ab!", "pqr"))  # Expected: "Break"
    print(mergeAlternately("abc!", "pq2"))  # Expected: "Break"