
class Solution:
    def split(self, word):
        return [char for char in word]

    def isValid(self, s: str) -> bool:

        check = {"(": ")", "[": "]", "{": "}"}
        # s = self.split(s)
        print(s)
        buff_list = []
        # opening = check.keys()
        # closing = check.values()

        for char in s:
            print(char)
            if char in check:
                buff_list.append(char)
            else:
                if buff_list == [] or char != check[buff_list.pop()]:
                    return False

        return len(buff_list) == 0


sl = Solution()
print(sl.isValid("[()]"))
