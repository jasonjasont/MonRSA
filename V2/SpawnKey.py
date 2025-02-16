import random

# Algorithm: RSA


#Fonction pour vérifier si un nombre est premier
def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


#fonction pour trouver l'inverse modulaire
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

#fonction pour générer un nombre premier
def generate_prime_candidate(length):
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

#fonction pour générer un nombre premier
def generate_prime_number(length=10):
    p = 4
    while not prime(p):
        p = generate_prime_candidate(length)
    return p

#fonction pour générer une paire de clés
def generate_keypair(length=10):
 
    p = generate_prime_number(length)
    q = generate_prime_number(length)
    while q == p:
        q = generate_prime_number(length)
    
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(2, phi)
        g = gcd(e, phi)

    d = mod_inverse(e, phi)
    
    return ((n, d), (n, e))

#fonction pour trouver le pgcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a



def spawn_key() :
    public_key, private_key = generate_keypair()
    return public_key, private_key


