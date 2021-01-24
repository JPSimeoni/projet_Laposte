fileName=open("connexion.txt","r")
lines = [i for i in fileName.readlines()]

for line in lines :
    print (line.split(";")[1])
    user = open ("suspects.txt", "a")
    user.write (line.split(";")[1] + "\n")

    user.close()
    
fileName.close()