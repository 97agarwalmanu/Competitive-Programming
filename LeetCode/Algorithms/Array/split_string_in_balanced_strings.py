class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        current_char = ''
        cc_count = 0  #Current character count
        ncc_count = 0 #Not current character count
        for i in range(len(s)):
            if current_char == '':
                current_char = s[i]
            if s[i] == current_char:
                cc_count += 1
            else:
                ncc_count += 1
            if cc_count == ncc_count:
                count += 1
                current_char = '' 
                cc_count, ncc_count = 0, 0
        return count
            