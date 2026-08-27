# Problem: 344. Reverse String
# Runtime: 5 ms (Beats 25.18%)
# Memory: 19.8 MB (Beats 76.53%)

class Solution(object):
    def reverseString(self, s):
        i = 0
        j = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]

            i = i + 1
            j = j - 1
        