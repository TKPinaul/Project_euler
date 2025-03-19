# Suite de fibonatie pour les nombres pairs
def pair_fibonatie(nombre_limite):
   a, b = 1, 2
   somme = 0
   while a < nombre_limite:
      if a % 2 == 0: # Si a est pair
         somme += a
      a, b = b, a + b
   return somme

# Trouver la somme de tous les multiples de 3 ou de 5 inférieurs à un nombre donné
def somme_multiple_3_ou_5(nbr):
   somme = 0
   for i in range(nbr):
      if i % 3 == 0 or i % 5 == 0:
         somme += i
   return somme

# Trouver le plus grand facteur premier d'un nombre
def plus_grand_facteur_premier(nbr):
   facteur = 2
   while facteur <= nbr**0.5: # <=> sqrt(nbr)
      if nbr % facteur == 0: # verifie si nbr est divisible par facteur
         nbr //= facteur # recupere la partie entiere (quotient) de la division de nbr par facteur
      else:
         facteur += 1
   return nbr