def get_inputs():
  nb_reactifs = int(input("Veuillez entrer le nombre de réactifs : ")
  noms_reacrifs = input("Veuillez entrer les noms des reactifs (espace est un séparateur) : ").split()
  stoechiometrics = input("Veuillez entrez les nombres stoechiométriques (espace est un séparateur) : ").split()
  mols = input("Veuillez entrer les quantités de matière (espace est un séparateur) : ").split()
  if len(mols) > len(stoechiometrics):
    print("Erreur : vous avez entré plus de quantités de matière que de nombres stoechiométriques")
    nb_reactifs, stoechiometrics, mols = get_inputs()
  return nb_reactifs, stoechiometrics, mols



nb_reactifs, stoechiometrics, mols = get_inputs()

l = [] 
for i in range(nb_reactifs):
  
