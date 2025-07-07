class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        wordqueue = []
        returnString = ""
        i = 0
        word = ""
        prev = ""
        while (i  < len(s)):
            if (s[i] == " "):
                if (prev != " "):
                    wordqueue.append(word)
                    returnString += " "
                    prev = " "
                    word = ""           
            else:
                word += s[i]
                prev = s[i]
            i += 1
        wordqueue.append(word)
        return " ".join(wordqueue[::-1])