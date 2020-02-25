class Solution:
    def toLowerCase(self, str: str) -> str:
        ascii_diff = ord('a') - ord('A')
        str1 = ""
        for i in str:
            if 65<= ord(i) < 91:
                str1+= chr(ord(i)+ascii_diff)
            else:
                str1+= i
        return str1
                