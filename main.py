"""on importe maths"""
import math
def isprime(p):
    """Vérifie si un nombre p est premier."""
# Gérer les cas triviaux
    if p < 2:
        return False
    if p in (2, 3):
        return True  # 2 et 3 sont premiers
    if p % 2 == 0 or p % 3 == 0:
        return False  # Exclure les multiples de 2 et 3

# Utilisation de math.isqrt pour calculer la racine carrée de p
    limit = math.isqrt(p) + 1

# Tester les nombres de la forme 6k ± 1
    for i in range(5, limit, 6):
        if p % i == 0 or p % (i + 2) == 0:
            return False

    return True

# Exemple d'utilisation
if __name__ == "__main__":
    # Affiche tous les nombres premiers jusqu'à 100
    print("Les nombres premiers jusqu'à 100 sont :")
    primes = [n for n in range(100) if isprime(n)]
    print(", ".join(map(str, primes)))



#### Fonction principale

def main():
    """appel fonction"""
# vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
