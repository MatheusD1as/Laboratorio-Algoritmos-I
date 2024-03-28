A = int(input("Digite o lado A do triângulo:"))
B = int(input("Digite o lado B do triângulo:"))
C = int(input("Digite o lado C do triângulo:"))
if A+B > C and C+A > B and C+B > A:
  print("O triângulo é verdadeiro")
  if (A == B) and (C == A) :
    print("É um triângulo verdadeiro e equilátero")
  elif (A != B) and (C != A) and (C != B):
    print("É um triângulo verdadeiro escaleno")
  else:
    print("é um triângulo isóceles")
else:
  print("não é um triângulo verdadeiro")
