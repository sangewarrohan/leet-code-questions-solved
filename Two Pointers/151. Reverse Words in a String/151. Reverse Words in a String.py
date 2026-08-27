# Problem: 151. Reverse Words in a String
# Runtime: 0 ms (Beats 100.00%)
# Memory: 19.4 MB (Beats 10.93%)

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return " ".join(words)