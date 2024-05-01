class Solution:
    def minimumSum(self, num: int) -> int:
        
        stringNum = str(num)
        listStringNum = list(stringNum)
        listStringNum.sort()

        x = listStringNum[0] + listStringNum[2]
        y = listStringNum[1] + listStringNum[3]

        return int(x) + int(y)