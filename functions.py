import os
import re
def compareLists(dictList):
       commonList=[]
       sizeOfDict=len(dictList)
       resultDict = dict()
       for x, fileName in enumerate(dictList):
              counter = 0
              while counter < sizeOfDict:
                     if counter == x: 
                        if counter <= (sizeOfDict - 1):
                              break                      
                        else:      
                              counter = counter + 1
                     a = list(set(list(dictList.values())[x]).intersection(list(dictList.values())[counter])) 
                     resultDict[f" {list(dictList)[x]} & {list(dictList)[counter]}"] = a
                     counter = counter + 1
       return resultDict
def wordFinder(liste):
        liste2 = []
        for line in liste:
            for word in line.split():
                r = re.findall('^[\d ]*$',word) #\d+ pb match des chiffres dans les noms
                try:
                        liste2.append(r[0])
                except:
                       pass
        return liste2
def listFinder(chemin,file):
        content = open(file=f"{chemin}/{file}")
        return content.readlines()
def fileFinder(chemin):
        return os.listdir(path=chemin)

