import collections
import math


# Problem 1a
def findAlphabeticallyLastWord(text):
    """
    Return the word that comes last alphabetically in the given text.
    """
    if not text or text.isspace():
        return ""
    return max(text.split())


############################################################
# Problem 1b
def euclideanDistance(loc1, loc2):
    """
    Return the Euclidean distance between two locations.
    """
    return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)


############################################################
# Problem 1c
def mutateSentences(sentence):
    """
    Return a list of all "similar" sentences.
    """
    words = sentence.split()
    if len(words) <= 1:
        return [sentence]

    # Create a dictionary of word pairs
    pairs = collections.defaultdict(list)
    for i in range(len(words) - 1):
        pairs[words[i]].append(words[i + 1])

    def generate_sentences(current, length):
        if len(current) == length:
            return [' '.join(current)]

        results = []
        last_word = current[-1]
        for next_word in pairs[last_word]:
            current.append(next_word)
            results.extend(generate_sentences(current, length))
            current.pop()

        return results

    all_sentences = set()
    for start_word in words:
        all_sentences.update(generate_sentences([start_word], len(words)))

    return list(all_sentences)


############################################################
# Problem 1d
def sparseVectorDotProduct(v1, v2):
    """
    Return the dot product of two sparse vectors.
    """
    return sum(v1[i] * v2[i] for i in set(v1.keys()) & set(v2.keys()))


############################################################
# Problem 1e
def incrementSparseVector(v1, scale, v2):
    """
    Perform v1 += scale * v2 for sparse vectors.
    """
    for key, value in v2.items():
        v1[key] += scale * value


############################################################
# Problem 1f
def findSingletonWords(text):
    """
    Return the set of words that occur exactly once.
    """
    word_count = collections.defaultdict(int)
    for word in text.split():
        word_count[word] += 1
    return {word for word, count in word_count.items() if count == 1}


############################################################
# Problem 1g
def computeLongestPalindromeLength(text):
    """
    Compute the length of the longest palindrome obtainable by deleting letters.
    """
    if not text:
        return 0

    n = len(text)
    # dp[i][j] represents the length of the longest palindrome
    # that can be formed from the substring text[i:j+1]
    dp = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    # Fill the dp table
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1

            if text[start] == text[end]:
                if length == 2:
                    dp[start][end] = 2
                else:
                    dp[start][end] = dp[start + 1][end - 1] + 2
            else:
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])

    return dp[0][n - 1]