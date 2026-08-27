# Problem: 344. Reverse String
# Runtime: 1 ms (Beats 57.44%)
# Memory: 23.4 MB (Beats 81.05%)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]

            i = i + 1
            j = j - 1