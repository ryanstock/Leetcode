class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        
        dict_of_substring = {}
        current_string_start = int(0)
        len_longest_substring = int(0)
        
        for current_char_index in range(0, len_s, 1):
            
            #if current character is in substring
            if s[current_char_index] in dict_of_substring:
                
                #find the index of the duplicate of the current char that is in the substring
                duplicate_index = dict_of_substring[ s[current_char_index] ]
                
                #delete all char entries in the substring that are before the duplicate, and the duplicate itself
                for delete_index in range(current_string_start, duplicate_index + 1, 1):
                    del dict_of_substring[s[delete_index]]
                #add the current char to the substring, and set the string start index to one step after the previously found and deleted duplicate
                dict_of_substring[s[current_char_index] ] = current_char_index
                current_string_start = duplicate_index + 1
            
            #if no duplicate then add the char to the substring
            else:
                dict_of_substring[s[current_char_index] ] = current_char_index
                
                #check substring length for being larger than previous maximum
                len_current_substring = current_char_index - current_string_start +1
                if len_longest_substring < len_current_substring:
                    len_longest_substring = len_current_substring
                    
        return len_longest_substring
                
        
        
 