class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        string_num = str(num)

        if num == 0:
            return True
        
        for digit in range(len(string_num)):
            if string_num[-1] == '0':
                string_num = string_num[:-1]
            else:
                break

        reversed1 = string_num[::-1]

        reversed2 = str(int(reversed1[::-1]))

        return reversed2 == str(num)