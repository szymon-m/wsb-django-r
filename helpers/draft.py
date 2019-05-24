import math
import itertools
import numpy
import datetime


# ========================================================
# tablica możliwych kombinacji userow - baza MovieLens 100k posiada oceny 610 uzytkownikow

print("- Tablica kombinacji ( user_1, user_2) ")
seq = list(itertools.combinations((range(1,611)),2))

#print(seq[609][0])
print("- Liczba pozycji dla 610 uzytkownikow:")
print(len(seq))

# =========================================================
# przykladowi userzy ( user 1 = [ film1_rating = 4, film2_rating = 3 , film3_rating = 0 , ... film(n)_rating = 3 ] )

users = [range(0,610)]
for x in range(0, 610):

    users.append(numpy.random.rand(610, 1))

print(len(users[12])) # sprawdzamy czy jest tyle wygenerowanych wartosci np. dla usera #12
#print(users[12]) dluga lista -

# =========================================================
# tablica distance - liczymy dystanse ( user#1_id , user#2_id, dystans )
distances = []

#t1 = datetime.datetime.now()

for x in range(0, len(seq)):

    distances.append([
            seq[x][0], # z wygenerowanych kombinacji dla pobieramy user#1_id
            seq[x][1], # z wygenerowanych kombinacji dla pobieramy user#2_id
            numpy.linalg.norm(users[seq[x][0]]-users[seq[x][1]])  # liczymy dystans user#1 - user#2
    ]
    )
print("- Przykladowy wpis tablicy distance: (user_1_id, user_2_id, distance)")
print(distances[1])

print("- Liczba policzonych dystansow:")
print(len(distances))

#
# wybieramy użytkownika nr #1 i tworzymy - posortowaną od najmniejszego dystansu do największego

output = []
[output.append(a) for a in distances if a[0] == 1]


output = sorted(output, key=lambda output: output[2])

print("- Najblizszych 3 (TOP 3) userow względem (user #1) z najmniejszym dystansem :")
print(output[1:4])

print("\n============")
print("Funkcja wypełniająca pobierajaca dane z ratings.csv")
print("1. Ratingi poszczególnych filmów (np film_1,film_2) są w stałej kolejności")
print("   np. dla usera #1 tablica wygląda nastepująco user#1 = [5,4,3,2,1]")
print("   więc film #1 ma 5, film #2 ma 4 itd.")
print("2. Z pliku ratings.csv powstaną puste pola, które trzeba wypełnic zerami ")

print("\n============")
print("Funkcja licząca średnią dla filmu z uwzględnieniem wag ")
print("(wagi ratingow uzytkownika w zalezności od dystansu od wybranego uzytkownika - odwrotnie proporcjonalna, czyli 1 / dystans)")
print("1. Powinna zliczać tylko pełne ratingi - czyli bez zer")
print("2. Dla zliczenia średniej filmu (w kolumnie - wiersze to userzy) - iteracja dla każdej kolumny z wyłączeniem zer")

print("\n============")
print("Funkcja pobierajaca ID filmow, posortowane od najwiekszego sredniego ratingu, wybiera np. z tego TOP 5")
# inne
def silnia(x):

    result = 1
    for n in range(1,x+1,1):
        result *= n
    #print(result)
    return result


wariacja_bez_powtorzen = (silnia(610) / silnia(608))
#print(wariacja_bez_powtorzen)


kombinacja = silnia(610) / (silnia(2)*silnia(608))
#print(kombinacja)