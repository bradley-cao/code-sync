class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = dict()
        i = 0
        maxlength = 0
        length = 0
        while i < len(s):
            if s[i] not in chars.keys():
                chars[s[i]] = i
                length += 1
            else:
                if chars[s[i]] < i - length:
                    chars[s[i]] = i
                    length += 1
                else:
                    length = i - chars[s[i]]
                    chars[s[i]] = i
            if length > maxlength:
                maxlength = length
            i += 1
        return maxlength