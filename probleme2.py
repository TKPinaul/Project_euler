# Probleme 2: Trouver la somme des termes de valeur paire de la séquence de Fibonacci dont les valeurs ne dépassent pas quatre millions."""
def pair_fibonatie(nombre_limite):
   a, b = 1, 2
   somme = 0
   while a < nombre_limite:
      if a % 2 == 0: # Si a est pair
         somme += a
      a, b = b, a + b
   return somme

print(pair_fibonatie(4000000))

# valeur de a apres 3 iterations: 3, 5, 8
# valeur de b apres 3 iterations: 5, 8, 13