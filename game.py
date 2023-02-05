from random import randint

def get_random_number():
  
  random_number = randint(1,10)
  
  chosen_number = 0
  
  while random_number != chosen_number:
    chosen_number = int(input("Digite um valor de 0 a 10: "))
    if (random_number == chosen_number):
      print("Parabéns. Você acertou!")
    else:
      print("Tente novamente.")
get_random_number()
