import re

paramId = 0
htmlElement = input("Wklej element: ")
print("\nWybrany element: ", htmlElement)

##DEFINIOWANIE I WYSZUKIWANIE ATRYBUTÓW
htmlParams = re.findall('(\\S+)=', htmlElement)
print("Elementy do wyboru(należy unikać korzystania z elementów typu style):\n")
for params in htmlParams:
    print("ID " + str(paramId) + " " + params)
    paramId = paramId + 1

htmlParamsWithValues = re.findall('''(\\S+)=["']?((?:.(?!["']?\s+(?:\S+)=|[>"']))+.)["']?''', htmlElement)

##WYBÓR ID ATRYBUTÓW
def Convert(string):
    li = list(string.split(","))
    return li
selectedElements = input("\nPodaj id parametrów na których chcesz bazować(oddzielone przecinkiem): ")
print(Convert(selectedElements))
selectedElements = Convert(selectedElements)

##GENEROWANIE SELECTORA

result = "$(" + "'" + input("\nPodaj typ elementu(div/input/textarea etc.): ")
if(len(selectedElements)>0):
        for id in selectedElements:
            if htmlParamsWithValues[int(id)][0] == "class":
                result = result + "." + htmlParamsWithValues[int(id)][1].replace('"', "").split()[0]
            if(htmlParamsWithValues[int(id)][0]) == "id":
                result = result + "#" + htmlParamsWithValues[int(id)][1].replace('"', "").split()[0]
            if(htmlParamsWithValues[int(id)][0]) != "id" and htmlParamsWithValues[int(id)][0] != "class":
                result = result + "["+htmlParamsWithValues[int(id)][0]+"="+'"'+htmlParamsWithValues[int(id)][1].replace('"', "")+'"'+"]"
result = result + "'" + ")"
print("\n" + "Twój selector to: " + result)
