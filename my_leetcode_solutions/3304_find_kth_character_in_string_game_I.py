class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            old_length = len(word)
            for i in range(old_length):
                this_char = word[i]
                if this_char == 'z':
                    word += 'a'
                else:
                    word += chr(ord(this_char)+1)
        return word[k-1]
        