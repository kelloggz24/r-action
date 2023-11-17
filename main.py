def get_inputs():
  nb_reactifs = int(input("Veuillez entrer le nombre de réactifs : "))
  noms_reactifs = input("Veuillez entrer les noms des reactifs (espace est un séparateur) : ").split()
  stoechiometrics = input("Veuillez entrez les nombres stoechiométriques (espace est un séparateur) : ").split()
  stoechiometrics1 = [eval(i) for i in stoechiometrics]
  mols = input("Veuillez entrer les quantités de matière (espace est un séparateur) : ").split()
  mols1 = [eval(i) for i in mols]
  if len(mols) > len(stoechiometrics):
    print("Erreur : vous avez entré plus de quantités de matière que de nombres stoechiométriques")
    nb_reactifs, stoechiometrics, mols = get_inputs()
  return nb_reactifs, stoechiometrics1, mols1, noms_reactifs



nb_reactifs, stoechiometrics, mols, noms_reactifs = get_inputs()
l = [] 
for i in range(nb_reactifs):
  l.append(mols[i]/stoechiometrics[i])

print(l)
m = min(l)
argm = l.index(m)

print(f"Le reactif limittant est {noms_reactifs[argm]}")
print(f"La valeur de l'avancement final est {m}")


final_mol = []
