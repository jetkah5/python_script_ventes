
Produits = {"Telephone":120,"Ordinateur":450,"Television":320}

while 1:
    print("-------------------------Debut------------------------------")
    print("Attention: réspectez les majuscules")
    print("---------------")
    print("Entrer votre demande: vendre/V, stock/S, produits/P, Ajouter/Aj, Supprimer/Supr, Modifier/Modif")
    Action = input(">_ ")
    if Action == "V":
        for prod,prix in Produits.items():
            print("+-----------------------------+")
            print('#',prod,' : ',prix, '$')
        print("Entrer le nom du produit à vendre")
        nomprod = input(">_ ");
        if nomprod in Produits:
            print(nomprod ,": ",Produits[nomprod],"$")
            print("Confirmer la vente? oui/O , non/N")
            confirm = input(">_ ");
            if confirm == "O":
                print("Vente terminer avec succès")
            else:
                print("Vente annuler!")        
        else:
            print("Produit non disponible, vérifiez peut-etre bien l'orthographe!")
    elif Action == "S":
          print("Articles en stock:")
          for prod,prix in Produits.items():
            print("+-----------------------------+")
            print('#',prod,' : ',prix, '$')
    elif Action == "Aj":
        print("Approvisionnement du stock")
        print("---------------------")
        print("Entez le nom du produit")
        ajout_nom = input(">_ ")
        print("Entez le prix du produit en $ (le nombre seulement)")
        ajout_prix = input(">_ ")
        print("Ajouter dans le stock? oui/O , non/N")
        confirm_ajout = input(">_ ")
        if confirm_ajout == "O":
            if ajout_nom in Produits:
                print("Ce produit existe déjà dans le stock")
            else:             
                Produits[ajout_nom] = ajout_prix
                print("Stock approvisionné avec succès")
        else:
            print("Approvisionnement annuler")
    elif Action == "P":
        print("Produits disponible:")
        for nom,prix in Produits.items():
            print("+-----------------------------+")
            print("-",nom," : ",prix,"$")
    elif Action == "Supr":
        print("Entrer le nom du produit à supprimer")
        prod_suppr = input(">_ ")
        if prod_suppr in Produits:
            del Produits[prod_suppr]
            print(prod_suppr," supprimé du stock avec succès")
        else:             
            print("'",prod_suppr,"' n'existe pas dans le stock, vérifiez peut-etre bien l'orthographe!")
            
    elif Action == "Modif":
        print("Entrer le nom du produit à modifier le prix")
        prod_modif = input(">_ ")
        if prod_modif in Produits:
            print("Entrez le nouveau prix de '",prod_modif,"' (un nombre seulement)")
            nouveau_prix = input(">_ ")
            print("Confirmez-vous la modification du prix de '",prod_modif,"' ? oui/O , non/N")
            confirm = input(">_ ")
            if confirm == "O":
                Produits[prod_modif] = nouveau_prix
                print("Le nouveau prix de '",prod_modif,"' est : ",nouveau_prix,"$")
            else:
                print("Modification du prix de '",prod_modif,"' annuler!")
        else:
            print("'",prod_modif,"' n'existe pas dans le stock, vérifiez peut-etre bien l'orthographe!")

#Written_By_Jet-kah
