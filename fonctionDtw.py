from python_speech_features import mfcc
import scipy.io.wavfile as wav
from dtw import *

def traitement1 (test,nomDossier,ref1,ref2,ref3):
    (rate, sig) = wav.read("audios/Ismail/"+nomDossier+"/I."+nomDossier+""+ref1+".wav")
    mfcc_feat = mfcc(sig, rate)

    (rate, sig) = wav.read("audios/Ismail/"+nomDossier+"/I."+nomDossier+""+ref2+".wav")
    mfcc_feat1 = mfcc(sig, rate)

    (rate, sig) = wav.read("audios/Ismail/"+nomDossier+"/I."+nomDossier+""+ref3+".wav")
    mfcc_feat2 = mfcc(sig, rate)

    x = np.array(mfcc_feat).reshape(-1, 1)
    y = np.array(mfcc_feat1).reshape(-1, 1)
    z = np.array(mfcc_feat2).reshape(-1, 1)

    d = dtw(x, y)
    print(d)

    d1 = dtw(x, z)
    print(d1)

    d2 = dtw(y, z)
    print(d2)

    liste = []

    liste.append(d)
    liste.append(d1)
    liste.append(d2)

    seuil = max(liste)
    print("max seuil :")
    print(seuil)

    client = 0
    imposteur = 0

    for i in range(1, 27):
        print(i)
        somme = 0
        chemin = "ensemble/" + str(test) + "/" + str(nomDossier) + "/" + str(i) + ".wav"

        (rate, sig) = wav.read(chemin)
        mfcc_featchemin = mfcc(sig, rate)

        x = np.array(mfcc_feat).reshape(-1, 1)
        y = np.array(mfcc_feat1).reshape(-1, 1)
        z = np.array(mfcc_feat2).reshape(-1, 1)
        w = np.array(mfcc_featchemin).reshape(-1, 1)

        d = dtw(x, w)
        somme += d

        d1 = dtw(y, w)
        somme += d1

        d2 = dtw(z, w)
        somme += d2

        moy = somme / 3

        if seuil > moy:
            client += 1
        else:
            imposteur += 1
    return client, imposteur

def traitement2(test,nomDossier,ref1,ref2,ref3,ref4):

    (rate, sig) = wav.read("audios/Ismail/"+nomDossier+"/I."+nomDossier+""+ref1+".wav")
    mfcc_feat = mfcc(sig, rate)

    (rate, sig) = wav.read("audios/Ismail/"+nomDossier+"/I."+nomDossier+""+ref2+".wav")
    mfcc_feat1 = mfcc(sig, rate)

    (rate, sig) = wav.read("audios/Ismail/"+nomDossier+"/I."+nomDossier+""+ref3+".wav")
    mfcc_feat2 = mfcc(sig, rate)

    (rate, sig) = wav.read("audios/Ismail/"+nomDossier+"/I."+nomDossier+""+ref4+".wav")
    mfcc_feat3 = mfcc(sig, rate)

    x = np.array(mfcc_feat).reshape(-1, 1)
    y = np.array(mfcc_feat1).reshape(-1, 1)
    z = np.array(mfcc_feat2).reshape(-1, 1)
    a = np.array(mfcc_feat3).reshape(-1, 1)

    d = dtw(x, y)
    d1 = dtw(x, z)
    d2 = dtw(x, a)
    d3 = dtw(y, z)
    d4 = dtw(y, a)
    d5 = dtw(z, a)

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

    client = 0
    imposteur = 0
    for i in range(1, 26):
        print(i)
        somme = 0
        chemin = "ensemble/" + str(test) + "/" + str(nomDossier) + "/" + str(i) + ".wav"
        (rate, sig) = wav.read(chemin)
        mfcc_featchemin = mfcc(sig, rate)
        x = np.array(mfcc_feat).reshape(-1, 1)
        a = np.array(mfcc_feat3).reshape(-1, 1)
        y = np.array(mfcc_feat1).reshape(-1, 1)
        z = np.array(mfcc_feat2).reshape(-1, 1)
        w = np.array(mfcc_featchemin).reshape(-1, 1)
        d = dtw(x, w)
        somme += d
        d1 = dtw(y, w)
        somme += d1
        d2 = dtw(z, w)
        somme += d2
        d3 = dtw(a, w)
        somme += d3
        moy = somme / 4
        if seuil > moy:
            client += 1
        else:
            imposteur += 1
    return client, imposteur

