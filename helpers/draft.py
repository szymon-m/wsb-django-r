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