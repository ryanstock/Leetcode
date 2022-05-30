class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        longest_palindrome_length = int(0)
        longest_palindrome = str('')

        if len_s == int(1):
            return s

        #loop through the input string as a start position
        for central_character in range(0, len_s, 1):
           
            #loop through the rest of the string as an end position - odd s length only

            current_symmetry_index = int(0)

            while ((central_character - current_symmetry_index) >=0 and (central_character + current_symmetry_index)< len_s  ):

                if s[central_character - current_symmetry_index] != s[central_character + current_symmetry_index]:
                    break
                else:
                    length_current_palindrome =  (2* current_symmetry_index) + 1
                    if longest_palindrome_length < length_current_palindrome:
                            longest_palindrome_length =  length_current_palindrome
                            longest_palindrome = s[central_character - current_symmetry_index : central_character + current_symmetry_index +1 ]
                current_symmetry_index += 1

            # even s length
            # bring in the leftmost trailling comparison index by 1 because the string is of even size
            current_symmetry_index = int(0)
            
            while ((central_character - current_symmetry_index) >=0 and (central_character + current_symmetry_index +1) < len_s ):
                if s[central_character - current_symmetry_index] != s[central_character + current_symmetry_index + 1 ]:
                    break
                else:

                    length_current_palindrome =  (2* current_symmetry_index) + 2
                    if longest_palindrome_length < length_current_palindrome:
                            longest_palindrome_length =  length_current_palindrome
                            longest_palindrome = s[central_character - current_symmetry_index: central_character + current_symmetry_index + 2]
                current_symmetry_index += 1
        return longest_palindrome