class Solution:
    def __init__(self):
        self.dictofVals = {"I": 1, "V": 5, "X": 10,
                           "L": 50, "C": 100, "D": 500, "M": 1000}

    def romanToInt(self, s: str) -> int:
        self.listofChar = self.split(s)
        self.result = 0
        print(self.listofChar)
        for i in range(len(self.listofChar)):
            if self.listofChar[i].upper() in self.dictofVals:
                self.result = self.result + \
                    self.dictofVals[self.listofChar[i].upper()]
                print(self.result)

            else:
                print("Char no to found")
        return self.result

    def split(self, word):
        return [char for char in word]


sl = Solution()
print(sl.romanToInt("MCMXCIV"))
