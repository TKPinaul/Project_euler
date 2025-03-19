# Problème 1. Trouver la somme de tous les multiples de 3 ou de 5 inférieurs à 1000.
def somme_multiple_3_et_5(nbr):
   somme = 0
   for i in range(nbr):
      if i % 3 == 0 or i % 5 == 0:
         somme += i
   return somme

print(somme_multiple_3_et_5(1000))