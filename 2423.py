import math

a, b, c = map(int, input().split())

# Pega o menor valor absoluto das divisões, sendo ele o tanto de bolos que da pra fazer

print(min(a//2, b//3, c//5))
