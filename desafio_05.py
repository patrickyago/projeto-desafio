# 5) Escreva um programa que inverta os caracteres de um string.
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

def inverte_string(string):
    caracteres = list(string)
    tamanho = len(caracteres)
    indice = 0
    
    while indice < tamanho / 2:
        caracteres[indice], caracteres[tamanho - 1 - indice] = caracteres[tamanho - 1 - indice], caracteres[indice]
        indice += 1
    string_invertida = ''.join(caracteres)
    return string_invertida

string_original = input("Digite uma string para inverter: ")
string_invertida = inverte_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)


