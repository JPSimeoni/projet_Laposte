  
from datetime import datetime       


file_input = open('connexion.txt','r')
suspects = []


lines_input = file_input.readlines()
for line in lines_input:

    utilisateur = line.split(";")

    #Creation date time (dd/mm/yy HH:MM)
    datetime_obj = datetime.strptime(utilisateur[2][:-1],"%d/%m/%y %H:%M")

    #Heures et minutes
    heure = datetime_obj.hour
    minutes = datetime_obj.minute

    #Conditions entre 8 et 19h
    if (heure>=19 or heure<8) and minutes!=0:
        suspect = utilisateur[1]+" - "+utilisateur[0]
        if suspect not in suspects:
            suspects.append(suspect) 


for i in suspects:
    print(i)


file_input .close()