import numpy as np
from fastdtw import fastdtw
from python_speech_features import mfcc
import scipy.io.wavfile as wav

# cette fonction permet de calculer le nombre des erreurs client et le nombre des erreurs imposteur pour le nombre de refference egal 3
def traitement1 (test,nomDossier,ref1,ref2,ref3):
    #on va lire la premier reference et appliquer la mfcc sur cette reference
    (rate, sig) = wav.read("audios/Ismail/"+nomDossier+"/I."+nomDossier+""+ref1+".wav")
    mfcc_feat = mfcc(sig, rate)
    # on va lire la deuxieme reference et appliquer la mfcc sur cette reference
    (rate, sig) = wav.read("audios/Ismail/"+nomDossier+"/I."+nomDossier+""+ref2+".wav")
    mfcc_feat1 = mfcc(sig, rate)
    # on va lire la troisieme reference et appliquer la mfcc sur cette reference
    (rate, sig) = wav.read("audios/Ismail/"+nomDossier+"/I."+nomDossier+""+ref3+".wav")
    mfcc_feat2 = mfcc(sig, rate)

    x = np.array(mfcc_feat).reshape(-1, 1)
    y = np.array(mfcc_feat1).reshape(-1, 1)
    z = np.array(mfcc_feat2).reshape(-1, 1)
    #on a appliqué la fastdtw entre ces trois reference.
    euclidean_norm = lambda x, y: np.abs(x - y)
    d, path = fastdtw(x, y, dist=euclidean_norm)

    euclidean_norm = lambda x, z: np.abs(x - z)
    d1, path = fastdtw(x, z, dist=euclidean_norm)

    euclidean_norm = lambda y, z: np.abs(y - z)
    d2, path = fastdtw(y, z, dist=euclidean_norm)
    liste = []
    liste.append(d)
    liste.append(d1)
    liste.append(d2)
    #on recupere le maximum de ces distence et l'utilise comme seuil
    seuil = max(liste)
    print("max seuil :")
    print(seuil)
    Erreurclient = 0
    Erreurimposteur = 0
    client=0
    imposteur=0
    # ici on va calculer la dtw entre l'ensemble de test et les trois reference
    for i in range(1, 27):
        # les enregistrement de 1 a 7 sont du client et les autres sont des imposteurs
        somme = 0
        chemin = "ensemble/" + str(test) + "/" + str(nomDossier) + "/" + str(i) + ".wav"

        (rate, sig) = wav.read(chemin)
        mfcc_featchemin = mfcc(sig, rate)

        x = np.array(mfcc_feat).reshape(-1, 1)
        y = np.array(mfcc_feat1).reshape(-1, 1)
        z = np.array(mfcc_feat2).reshape(-1, 1)
        w = np.array(mfcc_featchemin).reshape(-1, 1)

        euclidean_norm = lambda x, w: np.abs(x - w)
        d, path = fastdtw(x, w, dist=euclidean_norm)
        somme += d

        euclidean_norm = lambda y, w: np.abs(y - w)
        d1, path = fastdtw(y, w, dist=euclidean_norm)
        somme += d1

        euclidean_norm = lambda z, w: np.abs(z - w)
        d2, path = fastdtw(z, w, dist=euclidean_norm)
        somme += d2
        #ici on calcule la moyenne de ces distance et on va la comparer avec notre seuil
        moy = somme / 3
        if seuil > moy:
            print("client")
            client += 1
        else:
            print("imposteur")
            imposteur += 1
        if i > 7:
            if seuil > moy:
                Erreurimposteur += 1
        else:
            if seuil < moy:
                Erreurclient += 1
    return Erreurclient, Erreurimposteur, client, imposteur
# cette fonction permet de calculer le nombre des erreurs client et le nombre des erreurs imposteur pour le nombre de refference egal 4
def traitement2(test,nomDossier,ref1,ref2,ref3,ref4):
    # on va lire la premier reference et appliquer la mfcc sur cette reference
    (rate, sig) = wav.read("audios/Ismail/"+nomDossier+"/I."+nomDossier+""+ref1+".wav")
    mfcc_feat = mfcc(sig, rate)
    # on va lire la deuxieme reference et appliquer la mfcc sur cette reference
    (rate, sig) = wav.read("audios/Ismail/"+nomDossier+"/I."+nomDossier+""+ref2+".wav")
    mfcc_feat1 = mfcc(sig, rate)
    # on va lire la troisieme reference et appliquer la mfcc sur cette reference
    (rate, sig) = wav.read("audios/Ismail/"+nomDossier+"/I."+nomDossier+""+ref3+".wav")
    mfcc_feat2 = mfcc(sig, rate)
    # on va lire la quatrieme reference et appliquer la mfcc sur cette reference
    (rate, sig) = wav.read("audios/Ismail/"+nomDossier+"/I."+nomDossier+""+ref4+".wav")
    mfcc_feat3 = mfcc(sig, rate)

    x = np.array(mfcc_feat).reshape(-1, 1)
    y = np.array(mfcc_feat1).reshape(-1, 1)
    z = np.array(mfcc_feat2).reshape(-1, 1)
    a = np.array(mfcc_feat3).reshape(-1, 1)
    # on a appliqué la fastdtw entre ces quatre reference.
    euclidean_norm = lambda x, y: np.abs(x - y)
    d, path = fastdtw(x, y, dist=euclidean_norm)

    euclidean_norm = lambda x, z: np.abs(x - z)
    d1, path = fastdtw(x, z, dist=euclidean_norm)

    euclidean_norm = lambda x, a: np.abs(x - a)
    d2, path = fastdtw(x, a, dist=euclidean_norm)

    euclidean_norm = lambda y, z: np.abs(y - z)
    d3, path = fastdtw(y, z, dist=euclidean_norm)

    euclidean_norm = lambda y, a: np.abs(y - a)
    d4, path = fastdtw(y, a, dist=euclidean_norm)

    euclidean_norm = lambda z, a: np.abs(z - a)
    d5, path = fastdtw(z, a, dist=euclidean_norm)

    liste = []

    liste.append(d)
    liste.append(d1)
    liste.append(d2)
    liste.append(d3)
    liste.append(d4)
    liste.append(d5)

    seuil = max(liste)
    print("max seuil :")
    print(seuil)
    Erreurclient = 0
    Erreurimposteur = 0
    client=0
    imposteur=0
    # ici on va calculer la dtw entre l'ensemble de test et les quatre reference
    for i in range(1, 26):
        #les enregistrement de 1 a 6 sont du client et les autres sont des imposteurs
        somme = 0
        chemin = "ensemble/" + str(test) + "/" + str(nomDossier) + "/" + str(i) + ".wav"

        (rate, sig) = wav.read(chemin)
        mfcc_featchemin = mfcc(sig, rate)

        x = np.array(mfcc_feat).reshape(-1, 1)
        a = np.array(mfcc_feat3).reshape(-1, 1)
        y = np.array(mfcc_feat1).reshape(-1, 1)
        z = np.array(mfcc_feat2).reshape(-1, 1)
        w = np.array(mfcc_featchemin).reshape(-1, 1)

        euclidean_norm = lambda x, w: np.abs(x - w)
        d, path = fastdtw(x, w, dist=euclidean_norm)
        somme += d

        euclidean_norm = lambda y, w: np.abs(y - w)
        d1, path = fastdtw(y, w, dist=euclidean_norm)
        somme += d1

        euclidean_norm = lambda z, w: np.abs(z - w)
        d2, path = fastdtw(z, w, dist=euclidean_norm)
        somme += d2

        euclidean_norm = lambda a, w: np.abs(a - w)
        d3, path = fastdtw(a, w, dist=euclidean_norm)
        somme += d3
        # ici on calcule la moyenne de ces distance et on va la comparer avec notre seuil
        moy = somme / 4
        if seuil > moy:
            print("client")
            client += 1
        else:
            print("imposteur")
            imposteur += 1
        if i > 6:
            if seuil > moy:
                Erreurimposteur += 1
        else:
            if seuil < moy:
                Erreurclient += 1
    return Erreurclient, Erreurimposteur, client, imposteur

