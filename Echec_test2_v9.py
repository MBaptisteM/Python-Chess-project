from tkinter import *
from random import randrange
from PIL import Image, ImageTk
from tkinter import messagebox


########################################### changer les print d'erreur par des fenetres #################################################
########################################### choisir la piece que l'on veut avec le pion au bout #########################################
########################################### fix damme après le changement du pion #######################################################


"""
di on se met en echec
fix le bug
finir mat (add noir)

verif le tout
"""
### les noirs bugs completement au niveau du mat, à fic / mettre l'echec et mat avant le tour et pas à la fin, pion noir ne se transforme pas à la fin, tour (au moins noir) peut rock meme si c'est pas le roi
#Changer la taille du Terrain
taille_carre = 50
chemin = r'pieces/'

turn="blanc"

R_noir=False
R_blanc=False
gr_rockB=False
pt_rockB=False
gr_rockN=False
pt_rockN=False
M_ptn=False
M_grn=False
M_ptb=False
M_grb=False
M_rn=False
M_rb=False
Echec_try=False
ech=False


delnoir=0
delblanc=0
delall=0


board=[ [0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],
        [0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],
        [0,2],[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],
        [0,3],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],
        [0,4],[1,4],[2,4],[3,4],[4,4],[5,4],[6,4],[7,4],
        [0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],
        [0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6],[7,6],
        [0,7],[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7],]

#dico avec pieces et co
co_pio_blanc={"Bpio1":[0,6],"Bpio2":[1,6],"Bpio3":[2,6],"Bpio4":[3,6],"Bpio5":[4,6],"Bpio6":[5,6],"Bpio7":[6,6],"Bpio8":[7,6]}
co_tou_blanc={"Btou1":[0,7],"Btou2":[7,7]}
co_cav_blanc={"Bcav1":[1,7],"Bcav2":[6,7]}
co_fou_blanc={"Bfou1":[2,7],"Bfou2":[5,7]}
co_roi_blanc={"Broi":[3,7]}
co_dam_blanc={"Bdam":[4,7]}
co_blanc=[[0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6],[7,6],[0,7],[7,7],[1,7],[6,7],[2,7],[5,7],[3,7],[4,7]]

co_pio_noir={"Npio1":[0,1],"Npio2":[1,1],"Npio3":[2,6],"Npio4":[3,1],"Npio5":[4,1],"Npio6":[5,1],"Npio7":[6,1],"Npio8":[7,1]}
co_tou_noir={"Ntou1":[0,0],"Ntou2":[7,0]}
co_cav_noir={"Ncav1":[1,0],"Ncav2":[6,0]}
co_fou_noir={"Nfou1":[2,0],"Nfou2":[5,0]}
co_roi_noir={"Nroi":[3,0]}
co_dam_noir={"Ndam":[4,0]}
co_noir=[[0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],[0,0],[7,0],[1,0],[6,0],[2,0],[5,0],[3,0],[4,0]]
#on s'en fout
"""
co_all={"Bpio1":[0,6],"Bpio2":[1,6],"Bpio3":[2,6],"Bpio4":[3,6],"Bpio5":[4,6],"Bpio6":[5,6],"Bpio7":[6,6],"Bpio8":[7,6],"Btou1":[0,7],"Btou2":[7,7],"Bcav1":[1,7],"Bcav2":[6,7],"Bfou1":[2,7],"Bfou2":[5,7],"Broi":[3,7],"Bdam":[4,7],"Npio1":[0,1],"Npio2":[1,1],"Npio3":[2,6],"Npio4":[3,1],"Npio5":[4,1],"Npio6":[5,1],"Npio7":[6,1],"Npio8":[7,1],"Ntou1":[0,0],"Ntou2":[7,0],"Ncav1":[1,0],"Ncav2":[6,0],"Nfou1":[2,0],"Nfou2":[5,0],"Nroi":[3,0],"Ndam":[4,0]}
"""

life_all={"Bpio1":True,"Bpio2":True,"Bpio3":True,"Bpio4":True,"Bpio5":True,"Bpio6":True,"Bpio7":True,"Bpio8":True,"Btou1":True,"Btou2":True,"Bcav1":True,"Bcav2":True,"Bfou1":True,"Bfou2":True,"Broi":True,"Bdam":True,"Npio1":True,"Npio2":True,"Npio3":True,"Npio4":True,"Npio5":True,"Npio6":True,"Npio7":True,"Npio8":True,"Ntou1":True,"Ntou2":True,"Ncav1":True,"Ncav2":True,"Nfou1":True,"Nfou2":True,"Nroi":True,"Ndam":True}


co_liste=[[0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6],[7,6],[0,7],[7,7],[1,7],[6,7],[2,7],[5,7],[3,7],[4,7],[0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],[0,0],[7,0],[1,0],[6,0],[2,0],[5,0],[3,0],[4,0]]
co_nom=["Bpio1","Bpio2","Bpio3","Bpio4","Bpio5","Bpio6","Bpio7","Bpio8","Btou1","Btou2","Bcav1","Bcav2","Bfou1","Bfou2","Broi","Bdam","Npio1","Npio2","Npio3","Npio4","Npio5","Npio6","Npio7","Npio8","Ntou1","Ntou2","Ncav1","Ncav2","Nfou1","Nfou2","Nroi","Ndam"]


ligne_blanc=[[0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6],[7,6]]
ligne_noir=[[0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1]]

#regarde la piece à des co
def piece_on(co):
    for i in range (len(co_liste)):
        if co==co_liste[i] and life_all[co_nom[i]]==True:
            return co_nom[i]
    return "none"


#donner la piece à print
def get_png(co):
    a=piece_on(co)

    b="0"
    if a[1]=="p":
        b="pion"
    elif a[1]=="t":
        b="tour"
    elif a[1]=="c":
        b="cavalier"
    elif a[1]=="f":
        b="fou"
    elif a[1]=="r":
        b="roi"
    elif a[1]=="d":
        b="damme"
    else:
        return "none"
    if a[0]=="B":
        b=b+"1"
    elif a[0]=="N":
        b=b+"2"
    b=b+".png"
    return b

#recupères les co de la case cliquée par le joueur
def coord(position):

    # Récupérer la colonne sur laquelle le joueur clique
    a=[]
    colonne=10
    ligne=10

    if position.x>=0 and position.x<= taille_carre:
        colonne = 0
    elif position.x>taille_carre and position.x<=2*taille_carre:
        colonne = 1
    elif position.x>2*taille_carre and position.x<= 3*taille_carre:
        colonne = 2
    elif position.x>3*taille_carre and position.x<= 4*taille_carre:
        colonne = 3
    elif position.x>4*taille_carre and position.x<= 5*taille_carre:
        colonne = 4
    elif position.x>5*taille_carre and position.x<= 6*taille_carre:
        colonne = 5
    elif position.x>6*taille_carre and position.x<=7*taille_carre:
        colonne = 6
    elif position.x>7*taille_carre and position.x<= 8*taille_carre:
        colonne = 7
    a.append(colonne)


    # Récupérer la ligne sur laquelle le joueur clique

    if position.y>=0 and position.y<= taille_carre:
        ligne = 0
    elif position.y>taille_carre and position.y<=2*taille_carre:
        ligne = 1
    elif position.y>2*taille_carre and position.y<= 3*taille_carre:
        ligne = 2
    elif position.y>3*taille_carre and position.y<= 4*taille_carre:
        ligne = 3
    elif position.y>4*taille_carre and position.y<= 5*taille_carre:
        ligne = 4
    elif position.y>5*taille_carre and position.y<= 6*taille_carre:
        ligne = 5
    elif position.y>6*taille_carre and position.y<=7*taille_carre:
        ligne = 6
    elif position.y>7*taille_carre and position.y<= 8*taille_carre:
        ligne = 7
    a.append(ligne)
    return a


def coordE(position):
    a=[]
    colonne=10
    ligne=10

    if position[0]>=0 and position[0]<= taille_carre:
        colonne = 0
    elif position[0]>taille_carre and position[0]<=2*taille_carre:
        colonne = 1
    elif position[0]>2*taille_carre and position[0]<= 3*taille_carre:
        colonne = 2
    elif position[0]>3*taille_carre and position[0]<= 4*taille_carre:
        colonne = 3
    elif position[0]>4*taille_carre and position[0]<= 5*taille_carre:
        colonne = 4
    elif position[0]>5*taille_carre and position[0]<= 6*taille_carre:
        colonne = 5
    elif position[0]>6*taille_carre and position[0]<=7*taille_carre:
        colonne = 6
    elif position[0]>7*taille_carre and position[0]<= 8*taille_carre:
        colonne = 7
    a.append(colonne)

    if position[1]>=0 and position[1]<= taille_carre:
        ligne = 0
    elif position[1]>taille_carre and position[1]<=2*taille_carre:
        ligne = 1
    elif position[1]>2*taille_carre and position[1]<= 3*taille_carre:
        ligne = 2
    elif position[1]>3*taille_carre and position[1]<= 4*taille_carre:
        ligne = 3
    elif position[1]>4*taille_carre and position[1]<= 5*taille_carre:
        ligne = 4
    elif position[1]>5*taille_carre and position[1]<= 6*taille_carre:
        ligne = 5
    elif position[1]>6*taille_carre and position[1]<=7*taille_carre:
        ligne = 6
    elif position[1]>7*taille_carre and position[1]<= 8*taille_carre:
        ligne = 7
    a.append(ligne)
    return a



#verif si coup jouable
def verif(position):
    co=coord(position)
    if co[0]<=7 and co[0]>=0 and co[1]<=7 and co[1]>=0:
        if turn=="blanc":
            if coord(position) in co_blanc and life_all[piece_on(co)]==True:
                return True
            else:
                print("veuillez jouer sur une de vos pièce, ce sont les",turn,"qui jouent")
                return False
        elif turn=="noir":
            if coord(position) in co_noir and life_all[piece_on(co)]==True:
                return True
            else:
                print("veuillez jouer sur une de vos pièce, ce sont les",turn,"qui jouent")
                return False
    else:
        print("veuillez cliquer sur une case du damier")
        return False


def check_rock():
    li=[]
    global gr_rockB
    global pt_rockB
    global gr_rockN
    global pt_rockN
    if R_noir==False:
        if piece_on([1,0])=="none" and piece_on([2,0])=="none":
            pt_rockN=True
        if piece_on([4,0])=="none" and piece_on([5,0])=="none" and piece_on([6,0])=="none":
            gr_rockN=True
    if R_blanc==False:
        if piece_on([1,7])=="none" and piece_on([2,7])=="none":
            pt_rockB=True
        if piece_on([4,7])=="none" and piece_on([5,7])=="none" and piece_on([6,7])=="none":
            gr_rockB=True

    if pt_rockB==True:
        li.append("pt_rockB")
    if gr_rockB==True:
        li.append("gr_rockB")
    if pt_rockN==True:
        li.append("pt_rockN")
    if gr_rockN==True:
        li.append("gr_rockN")

    return li


phase=0
def getphase():
        return phase


def pion(co):
    case=coord(position)
    deplacement=[]

    if turn=="blanc":
        diagoG=[case[0]-1,case[1]-1]
        diagoD=[case[0]+1,case[1]-1]
        devant=[case[0],case[1]-1]


    elif turn=="noir":
        diagoG=[case[0]-1,case[1]+1]
        diagoD=[case[0]+1,case[1]+1]
        devant=[case[0],case[1]+1]

    if piece_on(devant)=="none":
        deplacement.append(devant)
        if turn=="blanc":
            if case in ligne_blanc:
                devant2=[case[0],case[1]-2]
                if piece_on(devant2)=="none":
                    deplacement.append(devant2)
        elif turn=="noir":
            if case in ligne_noir:
                devant2=[case[0],case[1]+2]
                if piece_on(devant2)=="none":
                    deplacement.append(devant2)

    if diagoG!="none" or diagoD!="none":
        if piece_on(diagoG)!="none":
            if turn == "noir" and piece_on(diagoG)[0]=="B":
                deplacement.append(diagoG)
            elif turn == "blanc" and piece_on(diagoG)[0]=="N":
                deplacement.append(diagoG)
        if piece_on(diagoD)!="none":
            if turn == "noir" and piece_on(diagoD)[0]=="B":
                deplacement.append(diagoD)
            elif turn == "blanc" and piece_on(diagoD)[0]=="N":
                deplacement.append(diagoD)
    return deplacement


def damme (co):
    global turn
    if Echec_try==True:
        if turn=="noir":
            turn="blanc"
        elif turn=="blanc":
            turn="noir"

    deplacement=[]
    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    a=False
    i=0
    while a==False:
        i=i+1
        co1[0]=co1[0]+1
        co1[1]=co1[1]+1
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)=="none":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+i,coord(position)[1]+i])
            else:
                deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]+i])
        elif turn =="blanc":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]+i,coord(position)[1]+i])
                else:
                    deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]+i])
            a=True
        elif turn=="noir":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]+i,coord(position)[1]+i])
                else:
                    deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]+i])
            a=True
        else :
            a=True
    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    a=False
    i=0
    while a==False:
        i=i+1
        co1[0]=co1[0]+1
        co1[1]=co1[1]-1
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)=="none":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+i,coord(position)[1]-i])
            else:
                deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]-i])
        elif turn =="blanc":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]+i,coord(position)[1]-i])
                else:
                    deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]-i])
            a=True
        elif turn=="noir":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]+i,coord(position)[1]-i])
                else:
                    deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]-i])
            a=True
        else :
            a=True
    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    a=False
    i=0
    while a==False:
        i=i+1
        co1[0]=co1[0]-1
        co1[1]=co1[1]+1
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)=="none":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-i,coord(position)[1]+i])
            else:
                deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]+i])
        elif turn =="blanc":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]-i,coord(position)[1]+i])
                else:
                    deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]+i])
            a=True
        elif turn=="noir":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]-i,coord(position)[1]+i])
                else:
                    deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]+i])
            a=True
        else :
            a=True
    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    a=False
    i=0
    while a==False:
        i=i+1
        co1[0]=co1[0]-1
        co1[1]=co1[1]-1
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)=="none":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-i,coord(position)[1]-i])
            else:
                deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]-i])
        elif turn =="blanc":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]-i,coord(position)[1]-i])
                else:
                    deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]-i])
            a=True
        elif turn=="noir":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]-i,coord(position)[1]-i])
                else:
                    deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]-i])
            a=True
        else :
            a=True

    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    a=False
    i=0
    while a==False:
        i=i+1
        co1[0]=co1[0]+1
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)=="none":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+i,coord(position)[1]])
            else:
                deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]])
        elif turn =="blanc":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]+i,coord(position)[1]])
                else:
                    deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]])
            a=True
        elif turn=="noir":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]+i,coord(position)[1]])
                else:
                    deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]])
            a=True
        else :
            a=True
    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    a=False
    i=0
    while a==False:
        i=i+1
        co1[0]=co1[0]-1
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)=="none":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-i,coord(position)[1]])
            else:
                deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]])
        elif turn =="blanc":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]-i,coord(position)[1]])
                else:
                    deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]])
            a=True
        elif turn=="noir":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]-i,coord(position)[1]])
                else:
                    deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]])
            a=True
        else :
            a=True
    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    a=False
    i=0
    while a==False:
        i=i+1
        co1[1]=co1[1]+1
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)=="none":
            if Echec_try==False:
                deplacement.append([coord(position)[0],coord(position)[1]+i])
            else:
                deplacement.append([coordE(position2)[0],coordE(position2)[1]+i])
        elif turn =="blanc":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
                if Echec_try==False:
                    deplacement.append([coord(position)[0],coord(position)[1]+i])
                else:
                    deplacement.append([coordE(position2)[0],coordE(position2)[1]+i])
            a=True
        elif turn=="noir":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
                if Echec_try==False:
                    deplacement.append([coord(position)[0],coord(position)[1]+i])
                else:
                    deplacement.append([coordE(position2)[0],coordE(position2)[1]+i])
            a=True
        else :
            a=True
    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    a=False
    i=0
    while a==False:
        i=i+1
        co1[1]=co1[1]-1
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)=="none":
            if Echec_try==False:
                deplacement.append([coord(position)[0],coord(position)[1]-i])
            else:
                deplacement.append([coordE(position2)[0],coordE(position2)[1]-i])
        elif turn =="blanc":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
                if Echec_try==False:
                    deplacement.append([coord(position)[0],coord(position)[1]-i])
                else:
                    deplacement.append([coordE(position2)[0],coordE(position2)[1]-i])
            a=True
        elif turn=="noir":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
                if Echec_try==False:
                    deplacement.append([coord(position)[0],coord(position)[1]-i])
                else:
                    deplacement.append([coordE(position2)[0],coordE(position2)[1]-i])
            a=True
        else:
            a=True


    if Echec_try==True:
        if turn=="noir":
            turn="blanc"
        elif turn=="blanc":
            turn="noir"
    return deplacement


def tour(co):
    global turn
    deplacement=[]
    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    a=False
    i=0

    if Echec_try==True:
        if turn=="noir":
            turn="blanc"
        elif turn=="blanc":
            turn="noir"

    while a==False:
        i=i+1
        co1[0]=co1[0]+1
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)=="none":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+i,coord(position)[1]])
            else:
                deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]])
        elif turn =="blanc":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]+i,coord(position)[1]])
                else:
                    deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]])
            a=True
        elif turn=="noir":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]+i,coord(position)[1]])
                else:
                    deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]])
            a=True
        else :
            a=True
    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    a=False
    i=0
    while a==False:
        i=i+1
        co1[0]=co1[0]-1
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)=="none":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-i,coord(position)[1]])
            else:
                deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]])
        elif turn =="blanc":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]-i,coord(position)[1]])
                else:
                    deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]])
            a=True
        elif turn=="noir":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]-i,coord(position)[1]])
                else:
                    deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]])
            a=True
        else :
            a=True
    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    a=False
    i=0
    while a==False:
        i=i+1
        co1[1]=co1[1]+1
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)=="none":
            if Echec_try==False:
                deplacement.append([coord(position)[0],coord(position)[1]+i])
            else:
                deplacement.append([coordE(position2)[0],coordE(position2)[1]+i])
        elif turn =="blanc":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
                if Echec_try==False:
                    deplacement.append([coord(position)[0],coord(position)[1]+i])
                else:
                    deplacement.append([coordE(position2)[0],coordE(position2)[1]+i])
            a=True
        elif turn=="noir":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
                if Echec_try==False:
                    deplacement.append([coord(position)[0],coord(position)[1]+i])
                else:
                    deplacement.append([coordE(position2)[0],coordE(position2)[1]+i])
            a=True
        else :
            a=True
    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    a=False
    i=0
    while a==False:
        i=i+1
        co1[1]=co1[1]-1
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)=="none":
            if Echec_try==False:
                deplacement.append([coord(position)[0],coord(position)[1]-i])
            else:
                deplacement.append([coordE(position2)[0],coordE(position2)[1]-i])
        elif turn =="blanc":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
                if Echec_try==False:
                    deplacement.append([coord(position)[0],coord(position)[1]-i])
                else:
                    deplacement.append([coordE(position2)[0],coordE(position2)[1]-i])
            a=True
        elif turn=="noir":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
                if Echec_try==False:
                    deplacement.append([coord(position)[0],coord(position)[1]-i])
                else:
                    deplacement.append([coordE(position2)[0],coordE(position2)[1]-i])
            a=True
        else:
            a=True

    if Echec_try==False:
        check_rock()

        if turn=="blanc":
            if R_blanc==False:
                if M_rb==False:
                    if M_grb==False:
                        if co==[7,7] and gr_rockB==True:
                            deplacement.append([3,7])
                    if M_ptb==False:
                        if co==[0,7] and pt_rockB==True:
                            deplacement.append([3,7])
        elif turn=="noir":
            if R_noir==False:
                if M_rn==False:
                    if M_grn==False:
                        if co==[7,0] and gr_rockN==True:
                            deplacement.append([3,0])
                    if M_ptn==False:
                        if co==[0,0] and pt_rockN==True:
                            deplacement.append([3,0])
    if Echec_try==True:
        if turn=="noir":
            turn="blanc"
        elif turn=="blanc":
            turn="noir"
    return deplacement

def fou(co):
    global turn
    if Echec_try==True:
        if turn=="noir":
            turn="blanc"
        elif turn=="blanc":
            turn="noir"

    deplacement=[]
    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    a=False
    i=0
    while a==False:
        i=i+1
        co1[0]=co1[0]+1
        co1[1]=co1[1]+1
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)=="none":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+i,coord(position)[1]+i])
            else:
                deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]+i])
        elif turn =="blanc":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]+i,coord(position)[1]+i])
                else:
                    deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]+i])
            a=True
        elif turn=="noir":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]+i,coord(position)[1]+i])
                else:
                    deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]+i])
            a=True
        else :
            a=True
    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    a=False
    i=0
    while a==False:
        i=i+1
        co1[0]=co1[0]+1
        co1[1]=co1[1]-1
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)=="none":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+i,coord(position)[1]-i])
            else:
                deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]-i])
        elif turn =="blanc":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]+i,coord(position)[1]-i])
                else:
                    deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]-i])
            a=True
        elif turn=="noir":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]+i,coord(position)[1]-i])
                else:
                    deplacement.append([coordE(position2)[0]+i,coordE(position2)[1]-i])
            a=True
        else :
            a=True
    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    a=False
    i=0
    while a==False:
        i=i+1
        co1[0]=co1[0]-1
        co1[1]=co1[1]+1
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)=="none":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-i,coord(position)[1]+i])
            else:
                deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]+i])
        elif turn =="blanc":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]-i,coord(position)[1]+i])
                else:
                    deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]+i])
            a=True
        elif turn=="noir":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]-i,coord(position)[1]+i])
                else:
                    deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]+i])
            a=True
        else :
            a=True
    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    a=False
    i=0
    while a==False:
        i=i+1
        co1[0]=co1[0]-1
        co1[1]=co1[1]-1
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)=="none":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-i,coord(position)[1]-i])
            else:
                deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]-i])
        elif turn =="blanc":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]-i,coord(position)[1]-i])
                else:
                    deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]-i])
            a=True
        elif turn=="noir":
            if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
                if Echec_try==False:
                    deplacement.append([coord(position)[0]-i,coord(position)[1]-i])
                else:
                    deplacement.append([coordE(position2)[0]-i,coordE(position2)[1]-i])
            a=True
        else :
            a=True

    if Echec_try==True:
        if turn=="noir":
            turn="blanc"
        elif turn=="blanc":
            turn="noir"
    return deplacement


def cavalier(co):
    global turn
    deplacement=[]
    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    co1[1]=co1[1]+2
    co1[0]=co1[0]+1

    if Echec_try==True:
        if turn=="noir":
            turn="blanc"
        elif turn=="blanc":
            turn="noir"

    if co1[0]>=0 and co1[0]<8 and co1[1]>=0 and co1[1]<8 and piece_on(co1)=="none":
        deplacement.append([coord(position)[0]+1,coord(position)[1]+2])
        if Echec_try==False:
            deplacement.append([coord(position)[0]+1,coord(position)[1]+2])
        else:
            deplacement.append([coordE(position2)[0]+1,coordE(position2)[1]+2])
    elif turn =="blanc":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+1,coord(position)[1]+2])
            else:
                deplacement.append([coordE(position2)[0]+1,coordE(position2)[1]+2])
    elif turn=="noir":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+1,coord(position)[1]+2])
            else:
                deplacement.append([coordE(position2)[0]+1,coordE(position2)[1]+2])

    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    co1[1]=co1[1]+2
    co1[0]=co1[0]-1
    if co1[0]>=0 and co1[0]<8 and co1[1]>=0 and co1[1]<8 and piece_on(co1)=="none":
        deplacement.append([coord(position)[0]-1,coord(position)[1]+2])
        if Echec_try==False:
            deplacement.append([coord(position)[0]-1,coord(position)[1]+2])
        else:
            deplacement.append([coordE(position2)[0]-1,coordE(position2)[1]+2])
    elif turn =="blanc":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-1,coord(position)[1]+2])
            else:
                deplacement.append([coordE(position2)[0]-1,coordE(position2)[1]+2])
    elif turn=="noir":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-1,coord(position)[1]+2])
            else:
                deplacement.append([coordE(position2)[0]-1,coordE(position2)[1]+2])

    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    co1[1]=co1[1]-2
    co1[0]=co1[0]+1
    if co1[0]>=0 and co1[0]<8 and co1[1]>=0 and co1[1]<8 and piece_on(co1)=="none":
        deplacement.append([coord(position)[0]+1,coord(position)[1]-2])
        if Echec_try==False:
            deplacement.append([coord(position)[0]+1,coord(position)[1]-2])
        else:
            deplacement.append([coordE(position2)[0]+1,coordE(position2)[1]-2])
    elif turn =="blanc":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+1,coord(position)[1]-2])
            else:
                deplacement.append([coordE(position2)[0]+1,coordE(position2)[1]-2])
    elif turn=="noir":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+1,coord(position)[1]-2])
            else:
                deplacement.append([coordE(position2)[0]+1,coordE(position2)[1]-2])

    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    co1[1]=co1[1]-2
    co1[0]=co1[0]-1
    if co1[0]>=0 and co1[0]<8 and co1[1]>=0 and co1[1]<8 and piece_on(co1)=="none":
        if Echec_try==False:
            deplacement.append([coord(position)[0]-1,coord(position)[1]-2])
        else:
            deplacement.append([coordE(position2)[0]-1,coordE(position2)[1]-2])
    elif turn =="blanc":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-1,coord(position)[1]-2])
            else:
                deplacement.append([coordE(position2)[0]-1,coordE(position2)[1]-2])
    elif turn=="noir":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-1,coord(position)[1]-2])
            else:
                deplacement.append([coordE(position2)[0]-1,coordE(position2)[1]-2])

    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    co1[1]=co1[1]-1
    co1[0]=co1[0]+2
    if co1[0]>=0 and co1[0]<8 and co1[1]>=0 and co1[1]<8 and piece_on(co1)=="none":
        if Echec_try==False:
            deplacement.append([coord(position)[0]+2,coord(position)[1]-1])
        else:
            deplacement.append([coordE(position2)[0]+2,coordE(position2)[1]-1])
    elif turn =="blanc":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+2,coord(position)[1]-1])
            else:
                deplacement.append([coordE(position2)[0]+2,coordE(position2)[1]-1])
    elif turn=="noir":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+2,coord(position)[1]-1])
            else:
                deplacement.append([coordE(position2)[0]+2,coordE(position2)[1]-1])

    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    co1[1]=co1[1]-1
    co1[0]=co1[0]-2
    if co1[0]>=0 and co1[0]<8 and co1[1]>=0 and co1[1]<8 and piece_on(co1)=="none":
        if Echec_try==False:
            deplacement.append([coord(position)[0]-2,coord(position)[1]-1])
        else:
            deplacement.append([coordE(position2)[0]-2,coordE(position2)[1]-1])
    elif turn =="blanc":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-2,coord(position)[1]-1])
            else:
                deplacement.append([coordE(position2)[0]-2,coordE(position2)[1]-1])
    elif turn=="noir":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-2,coord(position)[1]-1])
            else:
                deplacement.append([coordE(position2)[0]-2,coordE(position2)[1]-1])

    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    co1[1]=co1[1]+1
    co1[0]=co1[0]+2
    if co1[0]>=0 and co1[0]<8 and co1[1]>=0 and co1[1]<8 and piece_on(co1)=="none":
        if Echec_try==False:
            deplacement.append([coord(position)[0]+2,coord(position)[1]+1])
        else:
            deplacement.append([coordE(position2)[0]+2,coordE(position2)[1]+1])
    elif turn =="blanc":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+2,coord(position)[1]+1])
            else:
                deplacement.append([coordE(position2)[0]+2,coordE(position2)[1]+1])
    elif turn=="noir":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+2,coord(position)[1]+1])
            else:
                deplacement.append([coordE(position2)[0]+2,coordE(position2)[1]+1])

    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    co1[1]=co1[1]+1
    co1[0]=co1[0]-2
    if co1[0]>=0 and co1[0]<8 and co1[1]>=0 and co1[1]<8 and piece_on(co1)=="none":
        deplacement.append([coord(position)[0]-2,coord(position)[1]+1])
        if Echec_try==False:
            deplacement.append([coord(position)[0]-2,coord(position)[1]+1])
        else:
            deplacement.append([coordE(position2)[0]-2,coordE(position2)[1]+1])
    elif turn =="blanc":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-2,coord(position)[1]+1])
            else:
                deplacement.append([coordE(position2)[0]-2,coordE(position2)[1]+1])
    elif turn=="noir":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-2,coord(position)[1]+1])
            else:
                deplacement.append([coordE(position2)[0]-2,coordE(position2)[1]+1])

    if Echec_try==True:
        if turn=="noir":
            turn="blanc"
        elif turn=="blanc":
            turn="noir"

    return deplacement


def roi(co):
    global turn
    if Echec_try==True:
        if turn=="noir":
            turn="blanc"
        elif turn=="blanc":
            turn="noir"

    deplacement=[]
    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    co1[1]=co1[1]+1
    co1[0]=co1[0]+1

    if co1[0]>=0 and co1[0]<8 and co1[1]>=0 and co1[1]<8 and piece_on(co1)=="none":
        if Echec_try==False:
            deplacement.append([coord(position)[0]+1,coord(position)[1]+1])
        else:
            deplacement.append([coordE(position2)[0]+1,coordE(position2)[1]+1])
    elif turn =="blanc":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+1,coord(position)[1]+1])
            else:
                deplacement.append([coordE(position2)[0]+1,coordE(position2)[1]+1])
    elif turn=="noir":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+1,coord(position)[1]+1])
            else:
                deplacement.append([coordE(position2)[0]+1,coordE(position2)[1]+1])

    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    co1[1]=co1[1]+1
    co1[0]=co1[0]-1
    if co1[0]>=0 and co1[0]<8 and co1[1]>=0 and co1[1]<8 and piece_on(co1)=="none":
        if Echec_try==False:
            deplacement.append([coord(position)[0]-1,coord(position)[1]+1])
        else:
            deplacement.append([coordE(position2)[0]-1,coordE(position2)[1]+1])
    elif turn =="blanc":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-1,coord(position)[1]+1])
            else:
                deplacement.append([coordE(position2)[0]-1,coordE(position2)[1]+1])
    elif turn=="noir":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-1,coord(position)[1]+1])
            else:
                deplacement.append([coordE(position2)[0]-1,coordE(position2)[1]+1])

    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    co1[1]=co1[1]-1
    co1[0]=co1[0]+1
    if co1[0]>=0 and co1[0]<8 and co1[1]>=0 and co1[1]<8 and piece_on(co1)=="none":
        if Echec_try==False:
            deplacement.append([coord(position)[0]+1,coord(position)[1]-1])
        else:
            deplacement.append([coordE(position2)[0]+1,coordE(position2)[1]-1])
    elif turn =="blanc":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+1,coord(position)[1]-1])
            else:
                deplacement.append([coordE(position2)[0]+1,coordE(position2)[1]-1])
    elif turn=="noir":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+1,coord(position)[1]-1])
            else:
                deplacement.append([coordE(position2)[0]+1,coordE(position2)[1]-1])

    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    co1[1]=co1[1]-1
    co1[0]=co1[0]-1
    if co1[0]>=0 and co1[0]<8 and co1[1]>=0 and co1[1]<8 and piece_on(co1)=="none":
        if Echec_try==False:
            deplacement.append([coord(position)[0]-1,coord(position)[1]-1])
        else:
            deplacement.append([coordE(position2)[0]-1,coordE(position2)[1]-1])
    elif turn =="blanc":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-1,coord(position)[1]-1])
            else:
                deplacement.append([coordE(position2)[0]-1,coordE(position2)[1]-1])
    elif turn=="noir":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-1,coord(position)[1]-1])
            else:
                deplacement.append([coordE(position2)[0]-1,coordE(position2)[1]-1])

    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    co1[1]=co1[1]-1
    if co1[0]>=0 and co1[0]<8 and co1[1]>=0 and co1[1]<8 and piece_on(co1)=="none":
        if Echec_try==False:
            deplacement.append([coord(position)[0],coord(position)[1]-1])
        else:
            deplacement.append([coordE(position2)[0],coordE(position2)[1]-1])
    elif turn =="blanc":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
            if Echec_try==False:
                deplacement.append([coord(position)[0],coord(position)[1]-1])
            else:
                deplacement.append([coordE(position2)[0],coordE(position2)[1]-1])
    elif turn=="noir":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
            if Echec_try==False:
                deplacement.append([coord(position)[0],coord(position)[1]-1])
            else:
                deplacement.append([coordE(position2)[0],coordE(position2)[1]-1])

    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    co1[0]=co1[0]-1
    if co1[0]>=0 and co1[0]<8 and co1[1]>=0 and co1[1]<8 and piece_on(co1)=="none":
        if Echec_try==False:
            deplacement.append([coord(position)[0]-1,coord(position)[1]])
        else:
            deplacement.append([coordE(position2)[0]-1,coordE(position2)[1]])
    elif turn =="blanc":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-1,coord(position)[1]])
            else:
                deplacement.append([coordE(position2)[0]-1,coordE(position2)[1]])
    elif turn=="noir":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
            if Echec_try==False:
                deplacement.append([coord(position)[0]-1,coord(position)[1]])
            else:
                deplacement.append([coordE(position2)[0]-1,coordE(position2)[1]])

    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    co1[1]=co1[1]+1
    if co1[0]>=0 and co1[0]<8 and co1[1]>=0 and co1[1]<8 and piece_on(co1)=="none":
        if Echec_try==False:
            deplacement.append([coord(position)[0],coord(position)[1]+1])
        else:
            deplacement.append([coordE(position2)[0],coordE(position2)[1]+1])
    elif turn =="blanc":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
            if Echec_try==False:
                deplacement.append([coord(position)[0],coord(position)[1]+1])
            else:
                deplacement.append([coordE(position2)[0],coordE(position2)[1]+1])
    elif turn=="noir":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
            if Echec_try==False:
                deplacement.append([coord(position)[0],coord(position)[1]+1])
            else:
                deplacement.append([coordE(position2)[0],coordE(position2)[1]+1])

    co1=coord(position)
    if Echec_try==True:
        co1=coordE(position2)
    co1[0]=co1[0]+1
    if co1[0]>=0 and co1[0]<8 and co1[1]>=0 and co1[1]<8 and piece_on(co1)=="none":
        if Echec_try==False:
            deplacement.append([coord(position)[0]+1,coord(position)[1]])
        else:
            deplacement.append([coordE(position2)[0]+1,coordE(position2)[1]])
    elif turn =="blanc":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="N":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+1,coord(position)[1]])
            else:
                deplacement.append([coordE(position2)[0]+1,coordE(position2)[1]])
    elif turn=="noir":
        if co1[0]<=7 and co1[0]>=0 and co1[1]<=7 and co1[1]>=0 and piece_on(co1)[0]=="B":
            if Echec_try==False:
                deplacement.append([coord(position)[0]+1,coord(position)[1]])
            else:
                deplacement.append([coordE(position2)[0]+1,coordE(position2)[1]])


    if Echec_try==False:

        check_rock()

        if turn=="blanc":
            if echec(co_blanc[14])==False:
                if R_blanc==False:
                    if M_rb==False:
                        if M_grb==False:
                            if co==[3,7] and gr_rockB==True:
                                deplacement.append([7,7])
                        if M_ptb==False:
                            if co==[3,7] and pt_rockB==True:
                                deplacement.append([0,7])
        elif turn=="noir":
            if echec(co_noir[14])==False:
                if R_noir==False:
                    if M_rn==False:
                        if M_grn==False:
                            if co==[3,0] and gr_rockN==True:
                                deplacement.append([7,0])
                        if M_ptn==False:
                            if co==[3,0] and pt_rockN==True:
                                deplacement.append([0,0])

    if Echec_try==True:
        if turn=="noir":
            turn="blanc"
        elif turn=="blanc":
            turn="noir"
    return deplacement


def pion_dep(co,color):
    a=[]
    save=co
    bapt=co
    soph=co

    if color=="noir":
        if co[1]+1<8:
            if bapt[0]-1>=0:
                a.append([bapt[0]-1,bapt[1]+1])

            if soph[0]+1<8:
                a.append([soph[0]+1,soph[1]+1])
    elif color=="blanc":
        if co[1]-1<8:
            if bapt[0]-1>=0:
                a.append([bapt[0]-1,bapt[1]-1])

            if soph[0]+1<8:
                a.append([soph[0]+1,soph[1]-1])
    return a


def echec(co):
    pi=0
    global Echec_try
    global position2
    global piece
    Echec_try=True
    if turn=="blanc":
        if life_all["Npio1"]==True:
            pi=pion_dep(co_noir[0],"noir")
            if co in pi:
                Echec_try=False
                piece="Npio1"
                return True
        if life_all["Npio2"]==True:
            pi=pion_dep(co_noir[1],"noir")
            if co in pi:
                Echec_try=False
                piece="Npio2"
                return True
        if life_all["Npio3"]==True:
            pi=pion_dep(co_noir[2],"noir")
            if co in pi:
                Echec_try=False
                piece="Npio3"
                return True
        if life_all["Npio4"]==True:
            pi=pion_dep(co_noir[3],"noir")
            if co in pi:
                Echec_try=False
                piece="Npio4"
                return True
        if life_all["Npio5"]==True:
            pi=pion_dep(co_noir[4],"noir")
            if co in pi:
                Echec_try=False
                piece="Npio5"
                return True
        if life_all["Npio6"]==True:
            pi=pion_dep(co_noir[5],"noir")
            if co in pi:
                Echec_try=False
                piece="Npio6"
                return True
        if life_all["Npio7"]==True:
            pi=pion_dep(co_noir[6],"noir")
            if co in pi:
                Echec_try=False
                piece="Npio7"
                return True
        if life_all["Npio8"]==True:
            pi=pion_dep(co_noir[7],"noir")
            if co in pi:
                Echec_try=False
                piece="Npio8"
                return True


        if life_all["Ntou1"]==True:
            position2=[co_noir[8][0]*taille_carre+1,co_noir[8][1]*taille_carre+1]
            pi=tour(co_noir[8])
            if co in pi:
                Echec_try=False
                piece="Ntou1"
                return True
        if life_all["Ntou2"]==True:
            position2=[co_noir[9][0]*taille_carre+1,co_noir[9][1]*taille_carre+1]
            pi=tour(co_noir[9])
            if co in pi:
                Echec_try=False
                piece="Ntou2"
                return True
        if life_all["Ncav1"]==True:
            position2=[co_noir[10][0]*taille_carre+1,co_noir[10][1]*taille_carre+1]
            if co in cavalier(co_noir[10]):
                Echec_try=False
                piece="Ncav1"
                return True
        if life_all["Ncav2"]==True:
            position2=[co_noir[11][0]*taille_carre+1,co_noir[11][1]*taille_carre+1]
            if co in cavalier(co_noir[11]):
                Echec_try=False
                piece="Ncav2"
                return True
        if life_all["Nfou1"]==True:
            position2=[co_noir[12][0]*taille_carre+1,co_noir[12][1]*taille_carre+1]
            if co in fou(co_noir[12]):
                Echec_try=False
                piece="Nfou1"
                return True
        if life_all["Nfou2"]==True:
            position2=[co_noir[13][0]*taille_carre+1,co_noir[13][1]*taille_carre+1]
            if co in fou(co_noir[13]):
                Echec_try=False
                piece="Nfou2"
                return True
        if life_all["Nroi"]==True:
            position2=[co_noir[14][0]*taille_carre+1,co_noir[14][1]*taille_carre+1]
            if co in roi(co_noir[14]):
                Echec_try=False
                piece="Nroi"
                return True
        if life_all["Ndam"]==True:
            position2=[co_noir[15][0]*taille_carre+1,co_noir[15][1]*taille_carre+1]
            if co in damme(co_noir[15]):
                Echec_try=False
                piece="Ndam"
                return True



    elif turn=="noir":

        if life_all["Bpio1"]==True:
            pi=pion_dep(co_blanc[0],"blanc")
            if co in pi:
                Echec_try=False
                piece="Bpio1"
                return True
        if life_all["Bpio2"]==True:
            pi=pion_dep(co_blanc[1],"blanc")
            if co in pi:
                Echec_try=False
                piece="Bpio2"
                return True
        if life_all["Bpio3"]==True:
            pi=pion_dep(co_blanc[2],"blanc")
            if co in pi:
                Echec_try=False
                piece="Bpio3"
                return True
        if life_all["Bpio4"]==True:
            pi=pion_dep(co_blanc[3],"blanc")
            if co in pi:
                Echec_try=False
                piece="Bpio4"
                return True
        if life_all["Bpio5"]==True:
            pi=pion_dep(co_blanc[4],"blanc")
            if co in pi:
                Echec_try=False
                piece="Bpio5"
                return True
        if life_all["Bpio6"]==True:
            pi=pion_dep(co_blanc[5],"blanc")
            if co in pi:
                Echec_try=False
                piece="Bpio6"
                return True
        if life_all["Bpio7"]==True:
            pi=pion_dep(co_blanc[6],"blanc")
            if co in pi:
                Echec_try=False
                piece="Bpio7"
                return True
        if life_all["Bpio8"]==True:
            pi=pion_dep(co_blanc[7],"blanc")
            if co in pi:
                Echec_try=False
                piece="Bpio8"
                return True


        if life_all["Btou1"]==True:
            position2=[co_blanc[8][0]*taille_carre+1,co_blanc[8][1]*taille_carre+1]
            pi=tour(co_blanc[8])
            if co in pi:
                Echec_try=False
                piece="Btou1"
                return True
        if life_all["Btou2"]==True:
            position2=[co_noir[9][0]*taille_carre+1,co_blanc[9][1]*taille_carre+1]
            pi=tour(co_blanc[9])
            if co in pi:
                Echec_try=False
                piece="Btou2"
                return True
        if life_all["Bcav1"]==True:
            position2=[co_blanc[10][0]*taille_carre+1,co_blanc[10][1]*taille_carre+1]
            if co in cavalier(co_blanc[10]):
                Echec_try=False
                piece="Bcav1"
                return True
        if life_all["Bcav2"]==True:
            position2=[co_blanc[11][0]*taille_carre+1,co_blanc[11][1]*taille_carre+1]
            if co in cavalier(co_blanc[11]):
                Echec_try=False
                piece="Bcav2"
                return True
        if life_all["Bfou1"]==True:
            position2=[co_blanc[12][0]*taille_carre+1,co_blanc[12][1]*taille_carre+1]
            if co in fou(co_blanc[12]):
                Echec_try=False
                piece="Bfou1"
                return True
        if life_all["Bfou2"]==True:
            position2=[co_blanc[13][0]*taille_carre+1,co_blanc[13][1]*taille_carre+1]
            if co in fou(co_blanc[13]):
                Echec_try=False
                piece="Bfou2"
                return True
        if life_all["Broi"]==True:
            position2=[co_blanc[14][0]*taille_carre+1,co_blanc[14][1]*taille_carre+1]
            if co in roi(co_blanc[14]):
                Echec_try=False
                piece="Broi"
                return True
        if life_all["Bdam"]==True:
            position2=[co_blanc[15][0]*taille_carre+1,co_blanc[15][1]*taille_carre+1]
            if co in damme(co_blanc[15]):
                Echec_try=False
                piece="Bdam"
                return True

    Echec_try=False
    return False

def jeu_bleu(pos,co):
    global deplacement
    global anc_co
    global pos_jouer
    global phase
    global position
    position=pos
    anc_co=co
    typ=piece_on(co)

    if typ[1]=="p":
        deplacement=pion(co)

    elif typ[1]=="d":
        deplacement=damme(co)

    elif typ[1]=="t":
        deplacement=tour(co)


    elif typ[1]=="f":
        deplacement=fou(co)


    elif typ[1]=="c":
        deplacement=cavalier(co)


    elif typ[1]=="r":
        deplacement=roi(co)
        nbr=[]
        for i in range (len(deplacement)):
            if echec(deplacement[i])==True:
                nbr.append(i)
        for i in range(len(nbr)-1,-1,-1):
            del deplacement[nbr[i]]




    if deplacement==[]:
        return False
    phase=1
    for i in range(len(deplacement)):
        pos_jouer=[can.create_oval((deplacement[i][0]+0.3)*taille_carre,(deplacement[i][1]+0.3)*taille_carre,(deplacement[i][0]+0.7)*taille_carre,(deplacement[i][1]+0.7)*taille_carre, fill="blue")]
    return deplacement




#Génération de plateau
def damier():
    y = 0
    while y < 10:
        if y % 2 == 0:
            x = 0
        else:
            x = 1
        carre_noir(x*taille_carre, y*taille_carre,"green")
        y += 1


def carre_noir(x, y,color):
	i = 0
	while i < 5:
		can.create_rectangle(x, y, x+taille_carre, y+taille_carre, fill = color)
		i += 1
		x += taille_carre * 2


def placement():
    can.delete('all')

    damier()

    global Broi
    global Bdam
    global Bfou
    global Bfou2
    global Bcav
    global Bcav2
    global Btou
    global Btou2
    global Bpio
    global Bpio2
    global Bpio3
    global Bpio4
    global Bpio5
    global Bpio6
    global Bpio7
    global Bpio8

    global Nroi
    global Ndam
    global Nfou
    global Nfou2
    global Ncav
    global Ncav2
    global Ntou
    global Ntou2
    global Npio
    global Npio2
    global Npio3
    global Npio4
    global Npio5
    global Npio6
    global Npio7
    global Npio8

    global ech

    #pions Blancs
    if life_all['Broi']==True:
        Broi=[can.create_image(taille_carre*co_liste[14][0],taille_carre*co_liste[14][1],anchor=NW,image=RoiB)]

    if life_all['Bdam']==True:
        Bdam=[can.create_image(taille_carre*co_liste[15][0],taille_carre*co_liste[15][1],anchor=NW,image=DamB)]

    if life_all['Bfou1']==True:
        Bfou1=[can.create_image(taille_carre*co_liste[12][0],taille_carre*co_liste[12][1],anchor=NW,image=FouB)]
    if life_all['Bfou2']==True:
        Bfou2=[can.create_image(taille_carre*co_liste[13][0],taille_carre*co_liste[13][1],anchor=NW,image=FouB)]

    if life_all['Bcav1']==True:
        Bcav1=[can.create_image(taille_carre*co_liste[10][0],taille_carre*co_liste[10][1],anchor=NW,image=CavB)]
    if life_all['Bcav2']==True:
        Bcav2=[can.create_image(taille_carre*co_liste[11][0],taille_carre*co_liste[11][1],anchor=NW,image=CavB)]

    if life_all['Btou1']==True:
        Btou1=[can.create_image(taille_carre*co_liste[8][0],taille_carre*co_liste[8][1],anchor=NW,image=TouB)]
    if life_all['Btou2']==True:
        Btou2=[can.create_image(taille_carre*co_liste[9][0],taille_carre*co_liste[9][1],anchor=NW,image=TouB)]

    if life_all['Bpio1']==True:
        Bpio1=[can.create_image(taille_carre*co_liste[0][0],taille_carre*co_liste[0][1],anchor=NW,image=PioB)]
    elif life_all['Bpio1']=="D":
        Bpio1=[can.create_image(taille_carre*co_liste[0][0],taille_carre*co_liste[0][1],anchor=NW,image=DamB)]
    if life_all['Bpio2']==True:
        Bpio2=[can.create_image(taille_carre*co_liste[1][0],taille_carre*co_liste[1][1],anchor=NW,image=PioB)]
    elif life_all['Bpio2']=="D":
        Bpio2=[can.create_image(taille_carre*co_liste[1][0],taille_carre*co_liste[1][1],anchor=NW,image=DamB)]
    if life_all['Bpio3']==True:
        Bpio3=[can.create_image(taille_carre*co_liste[2][0],taille_carre*co_liste[2][1],anchor=NW,image=PioB)]
    elif life_all['Bpio3']=="D":
        Bpio3=[can.create_image(taille_carre*co_liste[2][0],taille_carre*co_liste[2][1],anchor=NW,image=DamB)]
    if life_all['Bpio4']==True:
        Bpio4=[can.create_image(taille_carre*co_liste[3][0],taille_carre*co_liste[3][1],anchor=NW,image=PioB)]
    elif life_all['Bpio4']=="D":
        Bpio4=[can.create_image(taille_carre*co_liste[3][0],taille_carre*co_liste[3][1],anchor=NW,image=DamB)]
    if life_all['Bpio5']==True:
        Bpio5=[can.create_image(taille_carre*co_liste[4][0],taille_carre*co_liste[4][1],anchor=NW,image=PioB)]
    elif life_all['Bpio5']=="D":
        Bpio5=[can.create_image(taille_carre*co_liste[4][0],taille_carre*co_liste[4][1],anchor=NW,image=DamB)]
    if life_all['Bpio6']==True:
        Bpio6=[can.create_image(taille_carre*co_liste[5][0],taille_carre*co_liste[5][1],anchor=NW,image=PioB)]
    elif life_all['Bpio6']=="D":
        Bpio6=[can.create_image(taille_carre*co_liste[5][0],taille_carre*co_liste[5][1],anchor=NW,image=DamB)]
    if life_all['Bpio7']==True:
        Bpio7=[can.create_image(taille_carre*co_liste[6][0],taille_carre*co_liste[6][1],anchor=NW,image=PioB)]
    elif life_all['Bpio7']=="D":
        Bpio7=[can.create_image(taille_carre*co_liste[6][0],taille_carre*co_liste[6][1],anchor=NW,image=DamB)]
    if life_all['Bpio8']==True:
        Bpio8=[can.create_image(taille_carre*co_liste[7][0],taille_carre*co_liste[7][1],anchor=NW,image=PioB)]
    elif life_all['Bpio8']=="D":
        Bpio8=[can.create_image(taille_carre*co_liste[7][0],taille_carre*co_liste[7][1],anchor=NW,image=DamB)]


    #pions Noirs
    if life_all['Nroi']==True:
        Nroi=[can.create_image(taille_carre*co_liste[30][0],taille_carre*co_liste[30][1],anchor=NW,image=RoiN)]

    if life_all['Ndam']==True:
        Ndam=[can.create_image(taille_carre*co_liste[31][0],taille_carre*co_liste[31][1],anchor=NW,image=DamN)]

    if life_all['Nfou1']==True:
        Nfou1=[can.create_image(taille_carre*co_liste[28][0],taille_carre*co_liste[28][1],anchor=NW,image=FouN)]
    if life_all['Nfou2']==True:
        Nfou2=[can.create_image(taille_carre*co_liste[29][0],taille_carre*co_liste[29][1],anchor=NW,image=FouN)]

    if life_all['Ncav1']==True:
        Ncav1=[can.create_image(taille_carre*co_liste[26][0],taille_carre*co_liste[26][1],anchor=NW,image=CavN)]
    if life_all['Ncav2']==True:
        Ncav2=[can.create_image(taille_carre*co_liste[27][0],taille_carre*co_liste[27][1],anchor=NW,image=CavN)]

    if life_all['Ntou1']==True:
        Ntou1=[can.create_image(taille_carre*co_liste[24][0],taille_carre*co_liste[24][1],anchor=NW,image=TouN)]
    if life_all['Ntou2']==True:
        Ntou2=[can.create_image(taille_carre*co_liste[25][0],taille_carre*co_liste[25][1],anchor=NW,image=TouN)]

    if life_all['Npio1']==True:
        Npio1=[can.create_image(taille_carre*co_liste[16][0],taille_carre*co_liste[16][1],anchor=NW,image=PioN)]
    elif life_all['Npio1']=="D":
        Npio1=[can.create_image(taille_carre*co_liste[16][0],taille_carre*co_liste[16][1],anchor=NW,image=DamN)]
    if life_all['Npio2']==True:
        Npio2=[can.create_image(taille_carre*co_liste[17][0],taille_carre*co_liste[17][1],anchor=NW,image=PioN)]
    elif life_all['Npio2']=="D":
        Npio2=[can.create_image(taille_carre*co_liste[17][0],taille_carre*co_liste[17][1],anchor=NW,image=DamN)]
    if life_all['Npio3']==True:
        Npio3=[can.create_image(taille_carre*co_liste[18][0],taille_carre*co_liste[18][1],anchor=NW,image=PioN)]
    elif life_all['Npio3']=="D":
        Npio3=[can.create_image(taille_carre*co_liste[18][0],taille_carre*co_liste[18][1],anchor=NW,image=DamN)]
    if life_all['Npio4']==True:
        Npio4=[can.create_image(taille_carre*co_liste[19][0],taille_carre*co_liste[19][1],anchor=NW,image=PioN)]
    elif life_all['Npio4']=="D":
        Npio4=[can.create_image(taille_carre*co_liste[19][0],taille_carre*co_liste[19][1],anchor=NW,image=DamN)]
    if life_all['Npio5']==True:
        Npio5=[can.create_image(taille_carre*co_liste[20][0],taille_carre*co_liste[20][1],anchor=NW,image=PioN)]
    elif life_all['Npio5']=="D":
        Npio5=[can.create_image(taille_carre*co_liste[20][0],taille_carre*co_liste[20][1],anchor=NW,image=DamN)]
    if life_all['Npio6']==True:
        Npio6=[can.create_image(taille_carre*co_liste[21][0],taille_carre*co_liste[21][1],anchor=NW,image=PioN)]
    elif life_all['Npio6']=="D":
        Npio6=[can.create_image(taille_carre*co_liste[21][0],taille_carre*co_liste[21][1],anchor=NW,image=DamN)]
    if life_all['Npio7']==True:
        Npio7=[can.create_image(taille_carre*co_liste[22][0],taille_carre*co_liste[22][1],anchor=NW,image=PioN)]
    elif life_all['Npio7']=="D":
        Npio7=[can.create_image(taille_carre*co_liste[22][0],taille_carre*co_liste[22][1],anchor=NW,image=DamN)]
    if life_all['Npio8']==True:
        Npio8=[can.create_image(taille_carre*co_liste[23][0],taille_carre*co_liste[23][1],anchor=NW,image=PioN)]
    elif life_all['Npio8']=="D":
        Npio8=[can.create_image(taille_carre*co_liste[23][0],taille_carre*co_liste[23][1],anchor=NW,image=DamN)]
    if ech==True:
        if turn=="blanc":
                [can.create_oval((co_blanc[14][0]+0.3)*taille_carre,(co_blanc[14][1]+0.3)*taille_carre,(co_blanc[14][0]+0.7)*taille_carre,(co_blanc[14][1]+0.7)*taille_carre, fill="red")]
        elif turn=="noir":
                [can.create_oval((co_noir[14][0]+0.3)*taille_carre,(co_noir[14][1]+0.3)*taille_carre,(co_noir[14][0]+0.7)*taille_carre,(co_noir[14][1]+0.7)*taille_carre, fill="red")]




def echec2():
    global ech
    if turn=="blanc":
        if echec(co_blanc[14])==True and piece_on(co_blanc[14])[1]=="r":
            ech=True
            return True
    elif turn=="noir":
        if echec(co_noir[14])==True and piece_on(co_noir[14])[1]=="r":
            ech=True
            return True
    ech=False
    return False


def check_mat():
    global turn
    dep=0
    if turn=="blanc":
        dep=roi(co_blanc[14])
        for i in range (len(dep)):
            if echec(dep[i])==False:
                return False
        echec(co_blanc[14])

    elif turn=="noir":
        dep=roi(co_noir[14])
        for i in range (len(dep)):
            if echec(dep[i])==False:
                return False
        echec(co_noir[14])
    dep=0
    c=0
    if piece[1]=="p":
        c=piece[-1]
    elif piece[1]=="t":
        c=piece[-1]+7
    elif piece[1]=="c":
        c=piece[-1]+9
    elif piece[1]=="f":
        c=piece[-1]+11
    elif piece[1]=="r":
        c=14
    else:
        c=15
    depla=[]
    if turn=="blanc":
        if echec(co_blanc[c])==True:
            if piece[1]!="r":
                return False
            else:
                turn = "noir"
                if echec(co_blanc[c])==False:
                    turn = "blanc"
                    return False
                else :
                    turn="blanc"
                    if c<8:
                        return True
                    elif c<10:
                        dep = tour(co_noir[c])
                        if co_blanc[14][0]<co_noir[c][0]:
                            for i in range(len(dep)):
                                if dep[i][0]<co_blanc[14][0]:
                                    depla.append(dep[i])
                        elif co_blanc[14][0]>co_noir[c][0]:
                            for i in range(len(dep)):
                                if dep[i][0]>co_blanc[14][0]:
                                    depla.append(dep[i])
                        elif co_blanc[14][1]<co_noir[c][1]:
                            for i in range(len(dep)):
                                if dep[i][1]<co_blanc[14][1]:
                                    depla.append(dep[i])
                        elif co_blanc[14][1]>co_noir[c][1]:
                            for i in range(len(dep)):
                                if dep[i][1]>co_blanc[14][1]:
                                    depla.append(dep[i])
                    elif c<12:
                        return True
                    elif c<15:
                        dep = tour(co_noir[c])
                        if co_blanc[14][0]<co_noir[c][0] and co_blanc[14][1]<co_noir[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]<co_blanc[14][0] and co_blanc[14][1]<co_noir[c][1]:
                                    depla.append(dep[i])
                        elif co_blanc[14][0]<co_noir[c][0] and co_blanc[14][1]>co_noir[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]<co_blanc[14][0] and co_blanc[14][1]>co_noir[c][1]:
                                    depla.append(dep[i])
                        elif co_blanc[14][0]>co_noir[c][0] and co_blanc[14][1]<co_noir[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]>co_blanc[14][0] and co_blanc[14][1]<co_noir[c][1]:
                                    depla.append(dep[i])
                        elif co_blanc[14][0]>co_noir[c][0] and co_blanc[14][1]>co_noir[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]>co_blanc[14][0] and co_blanc[14][1]>co_noir[c][1]:
                                    depla.append(dep[i])
                    else:
                        dep = damme(co_noir[c])
                        if co_blanc[14][0]<co_noir[c][0] and co_blanc[14][1]==co_noir[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]<co_blanc[14][0] and co_blanc[14][1]==co_noir[c][1]:
                                    depla.append(dep[i])
                        elif co_blanc[14][0]>co_noir[c][0] and co_blanc[14][1]==co_noir[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]>co_blanc[14][0] and co_blanc[14][1]==co_noir[c][1]:
                                    depla.append(dep[i])
                        elif co_blanc[14][1]<co_noir[c][1] and co_blanc[14][0]==co_noir[c][0]:
                            for i in range(len(dep)):
                                if dep[i][1]<co_blanc[14][1]and co_blanc[14][0]==co_noir[c][0]:
                                    depla.append(dep[i])
                        elif co_blanc[14][1]>co_noir[c][1]and co_blanc[14][0]==co_noir[c][0]:
                            for i in range(len(dep)):
                                if dep[i][1]>co_blanc[14][1]and co_blanc[14][0]==co_noir[c][0]:
                                    depla.append(dep[i])
                        elif co_blanc[14][0]<co_noir[c][0] and co_blanc[14][1]<co_noir[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]<co_blanc[14][0] and co_blanc[14][1]<co_noir[c][1]:
                                    depla.append(dep[i])
                        elif co_blanc[14][0]<co_noir[c][0] and co_blanc[14][1]>co_noir[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]<co_blanc[14][0] and co_blanc[14][1]>co_noir[c][1]:
                                    depla.append(dep[i])
                        elif co_blanc[14][0]>co_noir[c][0] and co_blanc[14][1]<co_noir[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]>co_blanc[14][0] and co_blanc[14][1]<co_noir[c][1]:
                                    depla.append(dep[i])
                        elif co_blanc[14][0]>co_noir[c][0] and co_blanc[14][1]>co_noir[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]>co_blanc[14][0] and co_blanc[14][1]>co_noir[c][1]:
                                    depla.append(dep[i])


                    for i in range (len(depla)):
                                if echec(depla[i])==True and piece[1]!="r":
                                    return False

    if turn=="noir":
        if echec(co_noir[c])==True:
            if piece[1]!="r":
                turn
                return False
            else:
                turn = "blanc"
                if echec(co_blanc[c])==False:
                    turn = "noir"
                    return False
                else :
                    turn="noir"
                    if c<8:
                            return True
                    elif c<10:
                        dep = tour(co_blanc[c])
                        if co_noir[14][0]<co_blanc[c][0]:
                            for i in range(len(dep)):
                                if dep[i][0]<co_noir[14][0]:
                                    depla.append(dep[i])
                        elif co_noir[14][0]>co_blanc[c][0]:
                            for i in range(len(dep)):
                                if dep[i][0]>co_noir[14][0]:
                                    depla.append(dep[i])
                        elif co_noir[14][1]<co_blanc[c][1]:
                            for i in range(len(dep)):
                                if dep[i][1]<co_noir[14][1]:
                                    depla.append(dep[i])
                        elif co_noir[14][1]>co_blanc[c][1]:
                            for i in range(len(dep)):
                                if dep[i][1]>co_noir[14][1]:
                                    depla.append(dep[i])
                    elif c<12:
                        return True
                    elif c<15:
                        dep = tour(co_blanc[c])
                        if co_noir[14][0]<co_blanc[c][0] and co_noir[14][1]<co_blanc[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]<co_noir[14][0] and co_noir[14][1]<co_blanc[c][1]:
                                    depla.append(dep[i])
                        elif co_noir[14][0]<co_blanc[c][0] and co_noir[14][1]>co_blanc[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]<co_noir[14][0] and co_noir[14][1]>co_blanc[c][1]:
                                    depla.append(dep[i])
                        elif co_noir[14][0]>co_blanc[c][0] and co_noir[14][1]<co_blanc[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]>co_noir[14][0] and co_noir[14][1]<co_blanc[c][1]:
                                    depla.append(dep[i])
                        elif co_noir[14][0]>co_blanc[c][0] and co_noir[14][1]>co_blanc[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]>co_noir[14][0] and co_noir[14][1]>co_blanc[c][1]:
                                    depla.append(dep[i])
                    else:
                        dep = damme(co_noir[c])
                        if co_noir[14][0]<co_blanc[c][0] and co_noir[14][1]==co_blanc[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]<co_noir[14][0] and co_noir[14][1]==co_blanc[c][1]:
                                    depla.append(dep[i])
                        elif co_noir[14][0]>co_blanc[c][0] and co_noir[14][1]==co_blanc[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]>co_noir[14][0] and co_noir[14][1]==co_blanc[c][1]:
                                    depla.append(dep[i])
                        elif co_noir[14][1]<co_blanc[c][1] and co_noir[14][0]==co_blanc[c][0]:
                            for i in range(len(dep)):
                                if dep[i][1]<co_noir[14][1]and co_noir[14][0]==co_blanc[c][0]:
                                    depla.append(dep[i])
                        elif co_noir[14][1]>co_blanc[c][1]and co_noir[14][0]==co_blanc[c][0]:
                            for i in range(len(dep)):
                                if dep[i][1]>co_noir[14][1]and co_noir[14][0]==co_blanc[c][0]:
                                    depla.append(dep[i])
                        elif co_noir[14][0]<co_blanc[c][0] and co_noir[14][1]<co_blanc[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]<co_noir[14][0] and co_noir[14][1]<co_blanc[c][1]:
                                    depla.append(dep[i])
                        elif co_noir[14][0]<co_blanc[c][0] and co_noir[14][1]>co_blanc[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]<co_noir[14][0] and co_noir[14][1]>co_blanc[c][1]:
                                    depla.append(dep[i])
                        elif co_noir[14][0]>co_blanc[c][0] and co_noir[14][1]<co_blanc[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]>co_noir[14][0] and co_noir[14][1]<co_blanc[c][1]:
                                    depla.append(dep[i])
                        elif co_noir[14][0]>co_blanc[c][0] and co_noir[14][1]>co_blanc[c][1]:
                            for i in range(len(dep)):
                                if dep[i][0]>co_noir[14][0] and co_noir[14][1]>co_blanc[c][1]:
                                    depla.append(dep[i])


                    for i in range (len(depla)):
                                if echec(depla[i])==True and piece[1]!="r":
                                    return False
    return True



def jeu(co,anc_co,anc_pos):
    global turn
    global phase
    global co_liste
    global co_noir
    global co_blanc

    check_rock()

    if co==[3,7] and anc_co==[0,7] and piece_on(anc_co)[1]=="t" and piece_on(co)[1]=="r" or anc_co==[3,7] and co==[0,7] and piece_on(co)[1]=="t" and piece_on(anc_co)[1]=="r":
        if pt_rockB==True:
            for i in range (len(co_liste)):
                if [3,7]==co_liste[i]:
                    co_liste[i]=[1,7]
                if [0,7]==co_liste[i]:
                    co_liste[i]=[2,7]
            for i in range (len(co_blanc)):
                if [3,7]==co_blanc[i]:
                    co_blanc[i]=[1,7]
                if [0,7]==co_blanc[i]:
                    co_blanc[i]=[2,7]
            phase = 0
            R_blanc=True
            turn="noir"
            return "rock"

    if co==[3,7] and anc_co==[7,7] and piece_on(anc_co)[1]=="t" and piece_on(co)[1]=="r" or anc_co==[3,7] and co==[7,7] and piece_on(co)[1]=="t" and piece_on(anc_co)[1]=="r":
        if gr_rockB==True:
            for i in range (len(co_liste)):
                if [3,7]==co_liste[i]:
                    co_liste[i]=[5,7]
                if [7,7]==co_liste[i]:
                    co_liste[i]=[4,7]
            for i in range (len(co_blanc)):
                if [3,7]==co_blanc[i]:
                    co_blanc[i]=[5,7]
                if [7,7]==co_blanc[i]:
                    co_blanc[i]=[4,7]
            phase = 0
            R_blanc=True
            turn="noir"
            return "rock"

    if co==[3,0] and anc_co==[0,0] and piece_on(anc_co)[1]=="t" and piece_on(co)[1]=="r" or anc_co==[3,0] and co==[0,0] and piece_on(co)[1]=="t" and piece_on(anc_co)[1]=="r":
        if pt_rockN==True:
            for i in range (len(co_liste)):
                if [3,0]==co_liste[i]:
                    co_liste[i]=[1,0]
                if [0,0]==co_liste[i]:
                    co_liste[i]=[2,0]
            for i in range (len(co_blanc)):
                if [3,0]==co_noir[i]:
                    co_noir[i]=[1,0]
                if [0,0]==co_noir[i]:
                    co_noir[i]=[2,0]
            phase = 0
            R_noir=True
            turn="blanc"
            return "rock"

    if co==[3,0] and anc_co==[7,0] and piece_on(anc_co)[1]=="t" and piece_on(co)[1]=="r" or anc_co==[3,0] and co==[7,0] and piece_on(co)[1]=="t" and piece_on(anc_co)[1]=="r":
        if gr_rockN==True:
            for i in range (len(co_liste)):
                if [3,0]==co_liste[i]:
                    co_liste[i]=[5,0]
                if [7,0]==co_liste[i]:
                    co_liste[i]=[4,0]
            for i in range (len(co_noir)):
                if [3,0]==co_noir[i]:
                    co_noir[i]=[5,0]
                if [7,0]==co_noir[i]:
                    co_noir[i]=[4,0]
            phase = 0
            R_noir=True
            turn="blanc"
            return "rock"



    global deplacement2
    deplacement2="none"

    b=get_png(anc_co)
    new=Image.open(chemin+b)
    resize_image0 = new.resize((taille_carre,taille_carre))
    global new1
    new1 = ImageTk.PhotoImage(resize_image0)

    global life_all

    life_all_back=[]
    co_noir_back=[]
    co_blanc_back=[]
    co_liste_back=[]

    #delete la piece
    for i in range (len(co_liste)):
        if co in co_liste:
            life_all_back.append([piece_on(co),True])
            life_all[piece_on(co)]=False
    for i in range (len(co_liste)):
        if co==co_liste[i]:
            co_liste_back.append([i,co_liste[i]])
            co_liste[i]=[-1,-1]
    if turn=="blanc":
        for i in range (len(co_noir)):
            if co == co_noir[i]:
                co_noir_back.append([i,co_noir[i]])
                co_noir[i]=[-1,-1]
    elif turn=="noir":
        for i in range (len(co_blanc)):
            if co == co_blanc[i]:
                co_blanc_back.append([i, co_blanc[i]])
                co_blanc[i]=[-1,-1]


    for i in range (len(co_liste)):
        if anc_co==co_liste[i]:
            co_liste_back.append([i,co_liste[i]])
            co_liste[i]=co
    if turn=="blanc":
        for i in range (len(co_blanc)):
            if anc_co == co_blanc[i]:
                co_blanc_back.append([i,co_blanc[i]])
                co_blanc[i]=co
    elif turn=="noir":
        for i in range (len(co_noir)):
            if anc_co == co_noir[i]:
                co_noir_back.append([i,co_noir[i]])
                co_noir[i]=co



    if echec2()==True:
        if check_mat()==True:
                todo = messagebox.askyesno("Echec et mat")
                if todo:
                    can.destroy()
                else:
                    can.destroy()

        for i in range(len(life_all_back)):
            life_all[life_all_back[i][0]]=life_all_back[i][1]
        for i in range(len(co_noir_back)):
            co_noir[co_noir_back[i][0]]=co_noir_back[i][1]
        for i in range(len(co_blanc_back)):
            co_blanc[co_blanc_back[i][0]]=co_blanc_back[i][1]
        for i in range(len(co_liste_back)):
            co_liste[co_liste_back[i][0]]=co_liste_back[i][1]
        phase=0
        echec2()
        return

    else:

        #gestion d'un pion qui se transforme de damme
        if piece_on(co)[1]=="p" and co[1]==0 and life_all[piece_on(co)]==True:
            if turn=="blanc":
                if piece_on(co)[4]=="1":
                    co_nom[0]="Bdam"
                    life_all["Bpio1"]="D"
                elif piece_on(co)[4]=="2":
                    co_nom[1]="Bdam"
                    life_all["Bpio2"]="D"
                elif piece_on(co)[4]=="3":
                    co_nom[2]="Bdam"
                    life_all["Bpio3"]="D"
                elif piece_on(co)[4]=="4":
                    co_nom[3]="Bdam"
                    life_all["Bpio4"]="D"
                elif piece_on(co)[4]=="5":
                    co_nom[4]="Bdam"
                    life_all["Bpio5"]="D"
                elif piece_on(co)[4]=="6":
                    co_nom[5]="Bdam"
                    life_all["Bpio6"]="D"
                elif piece_on(co)[4]=="7":
                    co_nom[6]="Bdam"
                    life_all["Bpio7"]="D"
                elif piece_on(co)[4]=="8":
                    co_nom[7]="Bdam"
                    life_all["Bpio8"]="D"

            elif turn=="noir":
                if piece_on(co)[4]=="1":
                    co_nom[16]="Ndam"
                    life_all["Npio1"]="D"
                elif piece_on(co)[4]=="2":
                    co_nom[17]="Ndam"
                    life_all["Npio2"]="D"
                elif piece_on(co)[4]=="3":
                    co_nom[18]="Ndam"
                    life_all["Npio3"]="D"
                elif piece_on(co)[4]=="4":
                    co_nom[19]="Ndam"
                    life_all["Npio4"]="D"
                elif piece_on(co)[4]=="5":
                    co_nom[20]="Ndam"
                    life_all["Npio5"]=="D"
                elif piece_on(co)[4]=="6":
                    co_nom[21]="Ndam"
                    life_all["Npio6"]="D"
                elif piece_on(co)[4]=="7":
                    co_nom[22]="Ndam"
                    life_all["Npio7"]="D"
                elif piece_on(co)[4]=="8":
                    co_nom[23]="Ndam"
                    life_all["Npio8"]="D"


        #check du rock

        global M_grb
        global M_grn
        global M_ptb
        global M_ptn
        global M_rb
        global M_rn

        if anc_co==[0,0]:
            M_ptn=True
        elif anc_co==[7,0]:
            M_grn=True
        elif anc_co==[0,7]:
            M_ptb=True
        elif anc_co==[7,7]:
            M_grb=True
        elif anc_co==[3,7]:
            M_rb=True
        elif anc_co==[3,0]:
            M_rn=True

    if turn=="blanc":
            turn="noir"
    elif turn=="noir":
        turn = "blanc"
    if echec2()==True:
        print("deja là c okkkkkkk")
        if check_mat()==True:
                todo = messagebox.askyesno("Echec et mat")
                if todo:
                    can.destroy()
                else:
                    can.destroy()
    if turn=="blanc":
        turn="noir"
    elif turn=="noir":
        turn = "blanc"


    if turn =="blanc":
        if echec(co_blanc[14])==False:
                turn ="noir"
    elif turn=="noir":
        if echec(co_noir[14])==False:
            turn="blanc"
    phase=0





#Position clique
def click_handler(position):
    global phase
    co=coord(position)
    if phase==0:
        global anc_pos
        anc_pos=position
        piece=piece_on(co)
        if verif(position)==True:
            if jeu_bleu(position,co)!= False:
                jeu_bleu(position,co)
            else:
                phase=0
        elif verif(position)==False:
            phase=0

    elif phase==1:
        if co in deplacement:
            jeu(co,anc_co,anc_pos)
        else:
            print("vous ne pouvez jouer que sur une case indiquée en bleu")
            phase=0
        placement()





fen = Tk()
fen.title("Echec")


can = Canvas(fen, width = (taille_carre * 8)-2, height = (taille_carre * 8)-2, bg = "white")
can.pack()
"""
fen.bind("<Button>", click_handler)
"""

print(chemin+'roi1.png')
roiB=Image.open(chemin+'roi1.png')
resize_image1 = roiB.resize((taille_carre,taille_carre))
RoiB = ImageTk.PhotoImage(resize_image1)

roiN=Image.open(chemin+'roi2.png')
resize_image2 = roiN.resize((taille_carre,taille_carre))
RoiN = ImageTk.PhotoImage(resize_image2)

damB=Image.open(chemin+'damme1.png')
resize_image3 = damB.resize((taille_carre,taille_carre))
DamB = ImageTk.PhotoImage(resize_image3)

damN=Image.open(chemin+'damme2.png')
resize_image4 = damN.resize((taille_carre,taille_carre))
DamN = ImageTk.PhotoImage(resize_image4)

touB=Image.open(chemin+'tour1.png')
resize_image5 = touB.resize((taille_carre,taille_carre))
TouB = ImageTk.PhotoImage(resize_image5)

touN=Image.open(chemin+'tour2.png')
resize_image6 = touN.resize((taille_carre,taille_carre))
TouN = ImageTk.PhotoImage(resize_image6)

fouB=Image.open(chemin+'fou1.png')
resize_image7 = fouB.resize((taille_carre,taille_carre))
FouB = ImageTk.PhotoImage(resize_image7)

fouN=Image.open(chemin+'fou2.png')
resize_image8 = fouN.resize((taille_carre,taille_carre))
FouN = ImageTk.PhotoImage(resize_image8)

cavB=Image.open(chemin+'cavalier1.png')
resize_image9 = cavB.resize((taille_carre,taille_carre))
CavB = ImageTk.PhotoImage(resize_image9)

cavN=Image.open(chemin+'cavalier2.png')
resize_image10 = cavN.resize((taille_carre,taille_carre))
CavN = ImageTk.PhotoImage(resize_image10)

pioB=Image.open(chemin+'pion1.png')
resize_image11 = pioB.resize((taille_carre,taille_carre))
PioB = ImageTk.PhotoImage(resize_image11)

pioN=Image.open(chemin+'pion2.png')
resize_image12 = pioN.resize((taille_carre,taille_carre))
PioN = ImageTk.PhotoImage(resize_image12)





b1 = Button(fen, text = "Lancer partie", command = placement)
b1.pack()

fen.bind("<Button>", click_handler)

fen.mainloop()