from functions import *
import time
import yaml
import json
if __name__ == "__main__":
    path = "./files"
    listeVlan=[]
    dictVlanFiltered=dict()
    fichiers = fileFinder(path)
    for fichier in fichiers:
        listeVlan.append(listFinder(path,fichier))
    for x,vlan in enumerate(listeVlan):
        dictVlanFiltered[fichiers[x]] = wordFinder(vlan)
    result = compareLists(dictVlanFiltered)
    print(json.dumps(result)) # or yaml.dump
    time.sleep(100)