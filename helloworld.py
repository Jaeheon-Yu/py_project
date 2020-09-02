

ss = "http://naver.com"

n1 = ss.replace('http://', '')
print(n1)
n2 = n1[:n1.index(".")]
print(n2)

n3 = str(n2[:3]) + str(len(n2)) + str(n2.count("e")) + "!"
print(n3)