from copy import deepcopy

width = height = 5
grille = [[0 for i in range(width)] for j in range(height)]



# État initial de la grille
grille[1][2] = 1
grille[1][3] = 1
grille[2][3] = 1
grille[3][3] = 1
grille[3][2] = 1

# État n+1 de la grille

# Il faut créer une deuxième grille pour empêcher
# que les changements de l'état n+1 falsifient
# les comparaisons avec l'état n

new_grille = deepcopy(grille)

nb_tours = int(input("Nombre de tours: "))
while nb_tours < 1 :
    nb_tours = int(input("Nombre de tours: "))

tours = 0

while tours < nb_tours :
    print("Tour n°", tours)
    for i in range(height):
        for j in range(width):
            print("#" if grille[i][j] else " ", end=" ")
            count = 0
            if i != 0 :
                if grille[i-1][j] == 1 :
                    count += 1
                if j != 0 :
                    if grille[i-1][j-1] == 1 :
                        count += 1
                if j != width-1 :
                    if grille[i-1][j+1] == 1 :
                        count += 1

            if j != 0 :
                if grille[i][j-1] == 1 :
                    count += 1
            if j != width-1 :
                if grille[i][j+1] == 1 :
                    count += 1

            if i != height-1 :
                if grille[i+1][j] == 1 :
                    count += 1
                if j != 0 :
                    if grille[i+1][j-1] == 1 :
                        count += 1
                if j != width-1 :
                    if grille[i+1][j+1] == 1 :
                        count += 1
            if grille[i][j] == 1 and (count < 2 or count > 3)  :
                new_grille[i][j] = 0
            elif grille[i][j] == 0 and count == 3 :
                new_grille[i][j] = 1
        print()
    print()
    grille = deepcopy(new_grille)
    tours += 1


print("Etat finale de la grille :\n")
for i in range(height):
    for j in range(width):
        print("#" if grille[i][j] else " ", end=" ")
    print()