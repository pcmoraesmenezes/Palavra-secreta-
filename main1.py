"""
Faça um jogo de advinhação
Você ira forecer uma plavra secreta e o usuario tentara adivinhar qual é
Faça o usuario digitar apenas uma palavra
O usuario só poderá digitar letras
A palavra deve ficar borrada de forma que a cada palavra descoberta pelo usuario vai liberando a palavra aos poucos, exemplo
******
a
*a*a**
"""
import os
tentativa = 0
palavra = "abacate"
var = ''
secreta = len(palavra)
magica = '*'
magica = secreta * magica
advinhada = ''
print(magica)
print(f'A palavra mágica possuí {secreta} digitos')
while True:
    print(magica)
    print("Digite uma letra para tentar adivinhar")
    var = input()
    while len(var) > 1:
        print("Digite apenas uma letra!")
        var = input()
    i = 0
    if var in palavra:
        for i in range(len(palavra)):
                  if var == palavra[i]:
                        magica = magica[:i] + var + magica[i+1:]
    else:
        print("A letra não se encontra na palavra, tente novamente!")
        tentativa += 1
        var = input()
    if magica == palavra:
        break
os.system('cls' if os.name == 'nt' else 'clear')
print(f"Parabens!!! Você advinhou a palavra secreta que era {palavra} e você teve tentativas = {tentativa}")
