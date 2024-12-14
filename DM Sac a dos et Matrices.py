def sac_a_dos(poids_max, objets, nom):
    '''
    Pour prouver l'optimalité, supposons qu'il existe une solution alternative, notée A, qui diffère
    de la solution obtenue par l'algorithme itératif. Soit B la solution obtenue par l'algorithme.
    Si A et B diffèrent par les objets inclus, nous pouvons retirer les objets supplémentaires de B
    jusqu'à ce qu'il atteigne la même capacité que A. Cela n'augmente pas la valeur totale de B et maintient sa faisabilité.
    Si A et B diffèrent uniquement par les fractions des objets inclus, nous pouvons ajuster les fractions de B pour les
    rendre identiques à celles de A, tout en conservant la capacité totale. Cela n'augmente pas la valeur totale de B et maintient sa faisabilité.
    Dans les deux cas, nous avons montré que la solution B peut être transformée en une solution équivalente à A sans
    diminuer sa valeur totale. Par conséquent, la solution B est optimale.
    Ainsi, l'algorithme itératif du sac à dos fractionnaire donne une solution optimale en effectuant des choix optimaux à chaque étape.
    '''
    objets = sorted(objets, key=lambda x: x[0] / x[1], reverse=True)
    poids_total = 0
    valeur_totale = 0
    details = []
    for i, (val, poids) in enumerate(objets):
        # Si on peut prendre l'objet entier
        if poids_total + poids <= poids_max:
            poids_total += poids
            valeur_totale += val
            details.append((cailloux[i], poids, 1))
        else:
            # Sinon prendre une fraction de l'objet
            fraction = (poids_max - poids_total) / poids
            poids_total += fraction * poids
            valeur_totale += fraction * val
            details.append((cailloux[i], poids, fraction))
    return poids_total, valeur_totale, details


def produit_mat_opti(matrices):
    """
    Cette fonction prend comme paramètre une liste de tuple contenant les dimensions des matrices à étudier.
    Elle permet de calculer le cout le plus faible pour la multiplication de ces matrices.
    Elle appelle une fonction interne permettant d'avoir l'ordre le plus optimisé afin de multiplier ces matrices.
    Enfin, elle renvoie donc le cout minimum ainsi que l'ordre de multiplication optimal.
    """
    n = len(matrices)
    temp = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        temp[i][i] = 0
    ind = [[-1 for _ in range(n)] for _ in range(n)]
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                cout = matrices[i][0] * matrices[k][1] * matrices[j][1]
                if temp[i][j] > temp[i][k] + temp[k+1][j] + cout:
                    temp[i][j] = temp[i][k] + temp[k+1][j] + cout
                    ind[i][j] = k
    cout_min = temp[0][n - 1]
    ordre = []
    def ordre_produit(i, j):
        if i == j:
            ordre.append(i)
        else:
            ordre_produit(i, ind[i][j])
            ordre_produit(ind[i][j] + 1, j)
    ordre_produit(0, n - 1)
    return cout_min, ordre





poids_max = 40
objets = [(700, 13), (500, 12), (200, 8), (300, 10), (600, 14)]
cailloux = ['Diamant', 'Rubis', 'Or', 'Argent', 'Cuivre']
poids_total, valeur_totale, details = sac_a_dos(poids_max, objets, cailloux)

tailles_mat = [(1, 3), (3, 2), (2, 6)]
cout_min, ordre = produit_mat_opti(tailles_mat)


print('Exercice 1 : Sac à dos')
print("Poids total du sac :\t", poids_total, "kg\nButin maximum :\t\t", valeur_totale, "€")
print("Détails :")
for nom, poids, fraction in details:
    print(f"\t{nom}: Le voleur peut prendre\t {fraction * 100}% de {poids} kg")
print('\n-------------------------------------------------------\n')
print('Exercice 2 : Chaine de matrices\nCout minimum : \t\t', cout_min, "\nOrdre plus optimisé : \t", ordre)
