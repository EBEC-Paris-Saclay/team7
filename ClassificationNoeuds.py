def classnoeud(L):
    Classifie=[]
    for i in range(len(L)):
        c=len(Classifie)
        if len(Classifie)==0:
            Classifie.append(L[i])
        for j in range(len(Classifie)-1):
            if L[i][0]>Classifie[j][0] and L[i][0]<Classifie[j+1][0]:
                Classifie.insert(j+1,L[i])
        if len(Classifie)==c:
            Classifie.append(L[i])
    return Classifie

