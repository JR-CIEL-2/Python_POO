from Vehicle import Vehicle
from Car import Car

def main():
    vehicule1 = Vehicle("Renault", "Clio IV", 2019)
    print(f"Le vehicule est de marque : {vehicule1.get_brand()}, de modèle {vehicule1.get_model()} et d'année {vehicule1.get_year()}")
    vehicule1.set_model("CLIO V")
    print(f"Le vehicule est de marque : {vehicule1.get_brand()}, de modèle {vehicule1.get_model()} et d'année {vehicule1.get_year()}")
    car1 = Car("peugeot", "3008", 2023 , 5 )
    print(f"Le vehicule est de marque {car1.get_brand()}, de modele {car1.get_model()}, d'année {car1.get_year()} et possede {car1.get_number_of_doors()} portes")


if __name__ == "__main__":
    main()
