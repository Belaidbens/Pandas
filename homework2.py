import pandas as pd
import os
from statistics import mode
import matplotlib.pyplot as plt

#merging 12 months of sales into single file
Ap = pd.read_csv("./Sales_Data/Sales_April_2019.csv")
print(Ap.head())
print(Ap.shape)


#concattener 
all_months_data = pd.DataFrame()#creer un tableau a deux dimensions qui est vide comme table SQL
files = [file for file in os.listdir('./Sales_Data')]
for file in files :
 #lire un ensemble de fichier d'un dosier
 print(file)
 #concatener un ensemble de fichier
 Ap = pd.read_csv("./Sales_Data/"+file)
 all_months_data=pd.concat([all_months_data,Ap])


all_months_data.to_csv("all_data.csv" , index=False) #index=false pour ne pas sauvegarder la colonne des numeros de lignes
print(all_months_data.head())

#ajout d'une colonne   moi a partir de la date
all_months_data['Month'] = all_months_data['Order Date'].str[0:2]
print(all_months_data.tail())

#supprimer les lignes qui contiennent NAn //all pou preciser que la ligne est supprimée si toutes les valeurs sont pas valides
all_months_data=all_months_data.dropna(how="all")
print(all_months_data.head())


#convertir les données
all_months_data["Quantity Ordered"]=pd.to_numeric(all_months_data["Quantity Ordered"], errors='coerce')  # pour eviter valeur non significative
all_months_data = all_months_data.dropna(subset=['Quantity Ordered'])
all_months_data["Quantity Ordered"]=all_months_data["Quantity Ordered"].astype("int")

all_months_data["Price Each"]=pd.to_numeric(all_months_data["Price Each"], errors='coerce')  # pour eviter valeur non significative
all_months_data = all_months_data.dropna(subset=['Price Each'])




#ajouter une colonnes des prix globlal
all_months_data["Sales"]=all_months_data["Quantity Ordered"] * all_months_data["Price Each"]
print(all_months_data.head())

#the best month for sales
print("the best month for sales")
results=all_months_data.groupby("Month").sum()
print(results)


#affichange en graphe
month =range(1,13)
plt.bar(month,results['Sales'])
plt.xticks(month)
plt.xlabel("months")
plt.ylabel("Sales in USD ($)")
plt.show() 

#the city that had the highest number of sales

#ajouter une ville 

def getcity(address):
  return address.split(",")[1] 
def get_state(address):
  return address.split(",")[2].split(" ")[1]
all_months_data["city"]=all_months_data['Purchase Address'].apply(lambda x : getcity(x) + " " +get_state(x))
print(all_months_data["city"].head())

city_results=all_months_data.groupby("city").sum()
print(city_results)

city =all_months_data['city'].unique()
plt.bar(city,city_results['Sales'])
plt.xlabel("City name")
plt.ylabel("Slaes on USD $")
plt.xticks(city , rotation='vertical',size='8')
plt.show()



#what I learned
# conact files  #ajouter une colonne #suppression de ligne  #conversion données   #affichage en graphe   #manipulation de quelques fonction like "apply , split, groupby, ...."





