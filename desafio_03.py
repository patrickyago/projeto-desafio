# 3) Descubra a lógica e complete o próximo elemento:

# a) 1, 3, 5, 7, ___
# b) 2, 4, 8, 16, 32, 64, ____
# c) 0, 1, 4, 9, 16, 25, 36, ____
# d) 4, 16, 36, 64, ____
# e) 1, 1, 2, 3, 5, 8, ____
# f) 2,10, 12, 16, 17, 18, 19, ____

def proximo_numero_a():
    return 7 + 2

def proximo_numero_b():
    return 64 * 2

def proximo_numero_c():
    return 7**2

def proximo_numero_d():
    return 8**2 + 4

def proximo_numero_e():
    return 8 + 5

def proximo_numero_f():
    return 19 + 2

print("a) Seguindo essa seguência 1, 3, 5, 7 o próximo é", proximo_numero_a())
print("b) Seguindo essa seguência 2, 4, 8, 16, 32, 64 o próximo é", proximo_numero_b())
print("c) Seguindo essa seguência 0, 1, 4, 9, 16, 25, 36 o próximo é", proximo_numero_c())
print("d) Seguindo essa seguência 4, 16, 36, 64 o próximo é", proximo_numero_d())
print("e) Seguindo essa seguência 1, 1, 2, 3, 5, 8 o próximo é", proximo_numero_e())
print("f) Seguindo essa seguência 2,10, 12, 16, 17, 18, 19 o próximo é", proximo_numero_f())