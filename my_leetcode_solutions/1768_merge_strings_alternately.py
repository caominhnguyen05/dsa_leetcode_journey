class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        j = 0

        word = 1

        while i < len(word1) and j < len(word2):
            if word == 1:
                result.append(word1[i])
                i += 1
                word = 2
            else:
                result.append(word2[j])
                j += 1
                word = 1
        while i < len(word1):
            result.append(word1[i])
            i += 1
        while j < len(word2):
            result.append(word2[j])
            j += 1
        return ''.join(result)