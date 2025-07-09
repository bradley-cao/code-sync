class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tokens = list(pattern)
        words = s.split()

        hashmap = dict()

        if len(tokens) != len(words):
            return False

        i = 0
        while i < len(tokens):
            if tokens[i] not in hashmap.keys():
                if words[i] in hashmap.values():
                    return False
                hashmap[tokens[i]] = words[i]
            else:
                if hashmap[tokens[i]] != words[i]:
                    return False
            i += 1
        
        return True