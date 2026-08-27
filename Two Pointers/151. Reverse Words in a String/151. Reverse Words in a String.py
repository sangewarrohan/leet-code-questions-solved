# Problem: 151. Reverse Words in a String
# Runtime: 0 ms (Beats 100.00%)
# Memory: 12.6 MB (Beats 36.53%)

class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
        return " ".join(words)
        