class Solution:
    def reverse(self, x: int) -> int:
        string_x = str(x)
        reversed_string_x = ""
        starter = int(1)
        if string_x[0]=="-":
            reversed_string_x += "-"
            starter = int(0)


        for i in range(1, len(string_x ) +starter, 1):
            reversed_string_x += string_x[-i]
        
        reversed_int_x = int(reversed_string_x)
        if reversed_int_x > (2**31 -1) or reversed_int_x < (-2**31):
            return 0
        return reversed_int_x