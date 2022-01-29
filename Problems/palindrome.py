class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.pal = 0
        self.original = x
        for i in range(len(str(x))):
            x1 = int(x % 10)
            self.pal = self.pal*10 + x1
            x = int(x/10)

        return self.original == self.pal
