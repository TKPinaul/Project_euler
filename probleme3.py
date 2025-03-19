# Probleme 3: Trouver le plus grand facteur premier de 600851475143
from math import sqrt


def plus_grand_facteur_premier(nbr):
   facteur = 2
   while facteur <= sqrt(nbr):
      if nbr % facteur == 0: # Si nbr est divisible par facteur 
         nbr //= facteur # => nbr = nbr // facteur
      else:
         facteur += 1
   return nbr

print(plus_grand_facteur_premier(600851475143))

# 5 // 2 = 2 verifie si 5 est divisible par 2 (la partie entiere de la division de 5 par 2) 
# 5 % 2 = 1 verifie si 2 est un diviseur de 5 (le reste de la division de 5 par 2) si oui = 0 sinon = 1