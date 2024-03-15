# 1) Observe o trecho de código abaixo:
# int INDICE = 13, SOMA = 0, K = 0;
# enquanto K < INDICE faça
# {
# K = K + 1;
# SOMA = SOMA + K;
# }
# imprimir(SOMA);

def somaIndice():
  indice = 13
  soma = 0
  k = 0

  while k < indice:
      k = k + 1
      soma = soma + k
  return soma

print(f"Ao final do processamento, qual será o valor da variável SOMA? {somaIndice()}")