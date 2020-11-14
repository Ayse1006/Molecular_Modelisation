'''
# Strubi project's second file
# visualization of the mcell results
# Marlene Barus, Ayse Ergun , Caroline Meguerditchian
# 11 November 2020

'''

####### IMPORT #######
from pylab import *
import numpy as np
import matplotlib.pyplot as plt


##################################### FUNCTIONS #####################################

# Chargement des donnees
### CONDITION : GEOMETRIE MODIFIEE ###

# Neurotransmetteurs
xNt = np.genfromtxt("react_data/seed_00001/Neurotransmetteur.World.dat", dtype=float)[:, 0]
yNt_1 = np.genfromtxt("react_data/seed_00001/Neurotransmetteur.World.dat", dtype=float)[:, 1]
yNt_2 = np.genfromtxt("react_data/seed_00002/Neurotransmetteur.World.dat", dtype=float)[:, 1]
yNt_3 = np.genfromtxt("react_data/seed_00003/Neurotransmetteur.World.dat", dtype=float)[:, 1]
yNt_4 = np.genfromtxt("react_data/seed_00004/Neurotransmetteur.World.dat", dtype=float)[:, 1]
yNt_5 = np.genfromtxt("react_data/seed_00005/Neurotransmetteur.World.dat", dtype=float)[:, 1]
yNt_6 = np.genfromtxt("react_data/seed_00006/Neurotransmetteur.World.dat", dtype=float)[:, 1]
yNt_7 = np.genfromtxt("react_data/seed_00007/Neurotransmetteur.World.dat", dtype=float)[:, 1]
yNt_8 = np.genfromtxt("react_data/seed_00008/Neurotransmetteur.World.dat", dtype=float)[:, 1]
yNt_9 = np.genfromtxt("react_data/seed_00009/Neurotransmetteur.World.dat", dtype=float)[:, 1]
yNt_10 = np.genfromtxt("react_data/seed_00010/Neurotransmetteur.World.dat", dtype=float)[:, 1]

# Recepteurs fermes

xRf = np.genfromtxt("react_data/seed_00001/Recepteur_ferme.World.dat", dtype=float)[:, 0]
yRf_1 = np.genfromtxt("react_data/seed_00001/Recepteur_ferme.World.dat", dtype=float)[:, 1]
yRf_2 = np.genfromtxt("react_data/seed_00002/Recepteur_ferme.World.dat", dtype=float)[:, 1]
yRf_3 = np.genfromtxt("react_data/seed_00003/Recepteur_ferme.World.dat", dtype=float)[:, 1]
yRf_4 = np.genfromtxt("react_data/seed_00004/Recepteur_ferme.World.dat", dtype=float)[:, 1]
yRf_5 = np.genfromtxt("react_data/seed_00005/Recepteur_ferme.World.dat", dtype=float)[:, 1]
yRf_6 = np.genfromtxt("react_data/seed_00006/Recepteur_ferme.World.dat", dtype=float)[:, 1]
yRf_7 = np.genfromtxt("react_data/seed_00007/Recepteur_ferme.World.dat", dtype=float)[:, 1]
yRf_8 = np.genfromtxt("react_data/seed_00008/Recepteur_ferme.World.dat", dtype=float)[:, 1]
yRf_9 = np.genfromtxt("react_data/seed_00009/Recepteur_ferme.World.dat", dtype=float)[:, 1]
yRf_10 = np.genfromtxt("react_data/seed_00010/Recepteur_ferme.World.dat", dtype=float)[:, 1]

# Ions

xI = np.genfromtxt("react_data/seed_00001/Ion.World.dat", dtype=float)[:, 0]
yI_1 = np.genfromtxt("react_data/seed_00001/Ion.World.dat", dtype=float)[:, 1]
yI_2 = np.genfromtxt("react_data/seed_00002/Ion.World.dat", dtype=float)[:, 1]
yI_3 = np.genfromtxt("react_data/seed_00003/Ion.World.dat", dtype=float)[:, 1]
yI_4 = np.genfromtxt("react_data/seed_00004/Ion.World.dat", dtype=float)[:, 1]
yI_5 = np.genfromtxt("react_data/seed_00005/Ion.World.dat", dtype=float)[:, 1]
yI_6 = np.genfromtxt("react_data/seed_00006/Ion.World.dat", dtype=float)[:, 1]
yI_7 = np.genfromtxt("react_data/seed_00007/Ion.World.dat", dtype=float)[:, 1]
yI_8 = np.genfromtxt("react_data/seed_00008/Ion.World.dat", dtype=float)[:, 1]
yI_9 = np.genfromtxt("react_data/seed_00009/Ion.World.dat", dtype=float)[:, 1]
yI_10 = np.genfromtxt("react_data/seed_00010/Ion.World.dat", dtype=float)[:, 1]

# Complexes

xCplx = np.genfromtxt("react_data/seed_00001/Cplx.World.dat", dtype=float)[:, 0]
yCplx_1 = np.genfromtxt("react_data/seed_00001/Cplx.World.dat", dtype=float)[:, 1]
yCplx_2 = np.genfromtxt("react_data/seed_00002/Cplx.World.dat", dtype=float)[:, 1]
yCplx_3 = np.genfromtxt("react_data/seed_00003/Cplx.World.dat", dtype=float)[:, 1]
yCplx_4 = np.genfromtxt("react_data/seed_00004/Cplx.World.dat", dtype=float)[:, 1]
yCplx_5 = np.genfromtxt("react_data/seed_00005/Cplx.World.dat", dtype=float)[:, 1]
yCplx_6 = np.genfromtxt("react_data/seed_00006/Cplx.World.dat", dtype=float)[:, 1]
yCplx_7 = np.genfromtxt("react_data/seed_00007/Cplx.World.dat", dtype=float)[:, 1]
yCplx_8 = np.genfromtxt("react_data/seed_00008/Cplx.World.dat", dtype=float)[:, 1]
yCplx_9 = np.genfromtxt("react_data/seed_00009/Cplx.World.dat", dtype=float)[:, 1]
yCplx_10 = np.genfromtxt("react_data/seed_00010/Cplx.World.dat", dtype=float)[:, 1]

# Recepteurs ouverts

xRo = np.genfromtxt("react_data/seed_00001/Recepteur_ouvert.World.dat", dtype=float)[:, 0]
yRo_1 = np.genfromtxt("react_data/seed_00001/Recepteur_ouvert.World.dat", dtype=float)[:, 1]
yRo_2 = np.genfromtxt("react_data/seed_00002/Recepteur_ouvert.World.dat", dtype=float)[:, 1]
yRo_3 = np.genfromtxt("react_data/seed_00003/Recepteur_ouvert.World.dat", dtype=float)[:, 1]
yRo_4 = np.genfromtxt("react_data/seed_00004/Recepteur_ouvert.World.dat", dtype=float)[:, 1]
yRo_5 = np.genfromtxt("react_data/seed_00005/Recepteur_ouvert.World.dat", dtype=float)[:, 1]
yRo_6 = np.genfromtxt("react_data/seed_00006/Recepteur_ouvert.World.dat", dtype=float)[:, 1]
yRo_7 = np.genfromtxt("react_data/seed_00007/Recepteur_ouvert.World.dat", dtype=float)[:, 1]
yRo_8 = np.genfromtxt("react_data/seed_00008/Recepteur_ouvert.World.dat", dtype=float)[:, 1]
yRo_9 = np.genfromtxt("react_data/seed_00009/Recepteur_ouvert.World.dat", dtype=float)[:, 1]
yRo_10 = np.genfromtxt("react_data/seed_00010/Recepteur_ouvert.World.dat", dtype=float)[:, 1]


# Fonction qui genere un tableau des moyennes des 10 simulations
def mean_list(dt, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10):
    new_list = []

    for i in range(len(dt)):
        y_mean = (y1[i] + y2[i] + y3[i] + y4[i] + y5[i] + y6[i] + y7[i] + y8[i] + y9[i] + y10[i]) / 10
        new_list.append(y_mean)
    return(new_list)


# Fonctions qui generent des tableaux des ecarts-types des 10 simulations
def addSd_list(dt, mean_list, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10):
    sd_list = []

    for i in range(len(dt)):
        temp = []
        temp.append(y1[i])
        temp.append(y2[i])
        temp.append(y3[i])
        temp.append(y4[i])
        temp.append(y5[i])
        temp.append(y6[i])
        temp.append(y7[i])
        temp.append(y8[i])
        temp.append(y9[i])
        temp.append(y10[i])
        sd = np.std(temp)
        sdMean = mean_list[i] + sd
        sd_list.append(sdMean)
    return(sd_list)

def substractSd_list(dt, mean_list, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10):
    sd_list = []

    for i in range(len(dt)):
        temp = []
        temp.append(y1[i])
        temp.append(y2[i])
        temp.append(y3[i])
        temp.append(y4[i])
        temp.append(y5[i])
        temp.append(y6[i])
        temp.append(y7[i])
        temp.append(y8[i])
        temp.append(y9[i])
        temp.append(y10[i])
        sd = np.std(temp)
        sdMean = mean_list[i] - sd
        sd_list.append(sdMean)
    return(sd_list)

# Fonction qui genere le plot de la la fitted curve des moyennes et ecart-type en fonction du temps :
def makePlot(num, dt, meanList, addSd, substractSd, molecule):
    plt.subplot(num)
    plt.plot(dt, meanList, "orange", label="Moyenne")
    plt.plot(dt, addSd, "red", label="Ecart-type")
    plt.plot(dt, substractSd, "red")
    plt.legend()
    plt.xlabel('Temps (s)')
    plt.title(molecule)
    plt.fill_between(dt, addSd, substractSd, alpha = 0.2, facecolor = "red")
    plt.suptitle("Evolution du nombre de molecules au cours du temps")



##################################### MAIN #####################################

def __main__():
    # Neurotransmetteurs
    nt_list = mean_list(xNt, yNt_1, yNt_2, yNt_3, yNt_4, yNt_5, yNt_6, yNt_7, yNt_8, yNt_9, yNt_10)
    addSd_Nt = addSd_list(xNt, nt_list, yNt_1, yNt_2, yNt_3, yNt_4, yNt_5, yNt_6, yNt_7, yNt_8, yNt_9, yNt_10)
    substractSd_Nt = substractSd_list(xNt, nt_list, yNt_1, yNt_2, yNt_3, yNt_4, yNt_5, yNt_6, yNt_7, yNt_8, yNt_9, yNt_10)
    makePlot(231, xNt, nt_list, addSd_Nt, substractSd_Nt, "Neurotransmetteurs")
    plt.ylabel('Nombre de molecules')

    # Recepteurs fermes
    rf_list = mean_list(xRf, yRf_1, yRf_2, yRf_3, yRf_4, yRf_5, yRf_6, yRf_7, yRf_8, yRf_9, yRf_10)
    addSd_Rf = addSd_list(xRf, rf_list, yRf_1, yRf_2, yRf_3, yRf_4, yRf_5, yRf_6, yRf_7, yRf_8, yRf_9, yRf_10)
    substractSd_Rf = substractSd_list(xRf, rf_list, yRf_1, yRf_2, yRf_3, yRf_4, yRf_5, yRf_6, yRf_7, yRf_8, yRf_9, yRf_10)
    makePlot(232, xRf, rf_list, addSd_Rf, substractSd_Rf, "Recepteurs fermes")

    # Ions
    i_list = mean_list(xI, yI_1, yI_2, yI_3, yI_4, yI_5, yI_6, yI_7, yI_8, yI_9, yI_10)
    addSd_I = addSd_list(xI, i_list, yI_1, yI_2, yI_3, yI_4, yI_5, yI_6, yI_7, yI_8, yI_9, yI_10)
    substractSd_I = substractSd_list(xI, i_list, yI_1, yI_2, yI_3, yI_4, yI_5, yI_6, yI_7, yI_8, yI_9, yI_10)
    makePlot(233, xI, i_list, addSd_I, substractSd_I, "Ions")

    # Complexes
    cplx_list = mean_list(xCplx, yCplx_1, yCplx_2, yCplx_3, yCplx_4, yCplx_5, yCplx_6, yCplx_7, yCplx_8, yCplx_9, yCplx_10)
    addSd_Cplx = addSd_list(xCplx, cplx_list, yCplx_1, yCplx_2, yCplx_3, yCplx_4, yCplx_5, yCplx_6, yCplx_7, yCplx_8, yCplx_9, yCplx_10)
    substractSd_Cplx = substractSd_list(xCplx, cplx_list, yCplx_1, yCplx_2, yCplx_3, yCplx_4, yCplx_5, yCplx_6, yCplx_7, yCplx_8, yCplx_9, yCplx_10)
    makePlot(234, xCplx, cplx_list, addSd_Cplx, substractSd_Cplx, "Complexes")
    plt.ylabel('Nombre de molecules')

    # Recepteurs ouverts
    ro_list = mean_list(xRo, yRo_1, yRo_2, yRo_3, yRo_4, yRo_5, yRo_6, yRo_7, yRo_8, yRo_9, yRo_10)
    addSd_Ro = addSd_list(xRo, ro_list, yRo_1, yRo_2, yRo_3, yRo_4, yRo_5, yRo_6, yRo_7, yRo_8, yRo_9, yRo_10)
    substractSd_Ro = substractSd_list(xRo, ro_list, yRo_1, yRo_2, yRo_3, yRo_4, yRo_5, yRo_6, yRo_7, yRo_8, yRo_9, yRo_10)
    makePlot(235, xRo, ro_list, addSd_Ro, substractSd_Ro, "Recepteurs ouverts")

    plt.subplots_adjust(left=0.07, bottom=0.09, right=0.98, top=0.88, wspace=0.27, hspace=0.31)
    plt.show()

__main__()



