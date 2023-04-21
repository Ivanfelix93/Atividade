print(" Seja muito bem vindo a atividade ")
answer_user = input(" Quer começar? (S/N) ")

if answer_user != "S":
    quit()

score = 0

print("Começando...")
print(" 1° Qual é o resultado da soma de 3 + 7? \n (A) 8 \n (B) 10 \n (C) 15 \n (D) 9 \n")
answer_1 = input("Resposta: ")

if answer_1 == "B":
    print("Correto!")
    score = score + 1.6
else:
    print("Incorreto!")

print(" 2° Quanto é 5 vezes 6? \n (A) 10 \n (B) 20 \n (C) 25 \n (D) 30 \n")
answer_2 = input("Resposta: ")

if answer_2 == "D":
    print("Correto!")
    score = score + 1.6
else:
    print("Incorreto!")

print(" 3° Se um livro custa R$ 20,00 e um caderno custa R$ 5,00, quanto custam 4 livros e 3 cadernos juntos? \n (A) R$ 60,00 \n (B) R$ 70,00 \n (C) R$ 95,00 \n (D) R$ 80,00 \n")
answer_2 = input("Resposta: ")

if answer_2 == "C":
    print("Correto!")
    score = score + 1.6
else:
    print("Incorreto!")

print(" 4° Qual é a medida do ângulo reto? \n (A) 45 graus \n (B) 90 graus \n (C) 135 graus \n (D) 180 graus \n")
answer_2 = input("Resposta: ")

if answer_2 == "B":
    print("Correto!")
    score = score + 1.6
else:
    print("Incorreto!")

print(" 5° Qual é a raiz quadrada de 16? \n (A) 7 \n (B) 4 \n (C) 8 \n (D) 3")
answer_2 = input("Resposta: ")

if answer_2 == "B":
    print("Correto!")
    score = score + 1.6
else:
    print("Incorreto!")

print(f"Quiz acabou... Pontuação: {score}")

resultado_formatado = "{:.1f}".format(score)

average_score = score /10
print("Sua média é:", "{:.1f}".format(average_score))

print(" Gabarito: 1 B, 2 D, 3 C, 4 B, 5 B ")
