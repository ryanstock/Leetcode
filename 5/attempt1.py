class Solution:
    def is_palindrome(self, s: str) -> bool:
        for char_sym_index in range(0, int(len(s)/2), 1):
            if s[char_sym_index] != s[- (1 + char_sym_index)]: #reverse indexing starts at 1 and not 0
                return False
        return True
        
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        longest_palindrome_length = int(0)
        longest_palindrome = str('')
        
        #loop through the input string as a start position
        for start_character in range(0, len_s, 1):
            
            #loop through the rest of the string as an end position
            for current_end_character in range(start_character , len_s, 1 ):
                if self.is_palindrome(s[start_character: current_end_character + 1 ]):
                        if longest_palindrome_length <= ( current_end_character + 1 - start_character  ):
                            longest_palindrome_length =  ( current_end_character + 1 - start_character  )
                            longest_palindrome = s[start_character: current_end_character + 1 ]

        return longest_palindrome