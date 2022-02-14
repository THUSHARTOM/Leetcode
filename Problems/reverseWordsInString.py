s = "Let's take LeetCode contest"
s = s.split()
result = []
for i in range(len(s)):
    result.append(s[i][::-1])

result = " ".join(result)
print(result)
