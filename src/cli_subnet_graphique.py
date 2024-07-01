from model.network import Network, network_from_str
from service.network_table_service import NetworkTableService


def main():
    print("Bienvenu dans Calculateur Subnet Graphique.")
    print("Ce programme a pour but de facilité la création et la gestion de sous réseaux.\n")

    user_input = ""
    print("# Commençons")
    ip_origine = input("Entrez l'ip du réseau :")       # TODO : Also enable to use command params
    mask_origine = input("Entrez le mask du réseau :")  # TODO : Also enable to use command params
    network_table = NetworkTableService(network_from_str(ip_origine, mask_origine))
    while user_input != "q":
        print(network_table)
        user_input = input("Entrez le # du réseau à séparer en deux :")
        if not user_input.isnumeric():
            print("\nLa valeur entrée est invalide.\n")
            if user_input != "q":
                print("Entrez q si vous voulez quitter le programme.\n")
            continue
        try:
            network_table.split(int(user_input))
        except Exception as ex:
            print("\nUne erreur est survenu :", ex, end="\n"*2)


if __name__ == '__main__':
    main()
