# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
def isSubsequence(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0; j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == len(s) else False

print(isSubsequence("abbccaab", "abbab")
