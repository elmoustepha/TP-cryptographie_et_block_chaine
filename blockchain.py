import hashlib  # Bibliothèque pour le hachage
import datetime  # Bibliothèque pour obtenir la date et l'heure actuelles


# 1. Définition du bloc (Block)
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index  # Numéro du bloc
        self.timestamp = timestamp  # Date et heure de création
        self.data = data  # Données stockées dans le bloc
        self.previous_hash = previous_hash  # Hachage du bloc précédent
        self.hash = self.calculate_hash()  # Hachage du bloc actuel

    # Calcul du hachage en utilisant la bibliothèque hashlib
    def calculate_hash(self):
        data_to_hash = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(data_to_hash.encode()).hexdigest()

# 2. Définition de la chaîne de blocs (Blockchain)
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # La chaîne commence avec le bloc de genèse

    # Création du bloc de genèse (Genesis Block)
    def create_genesis_block(self):
        return Block(0, str(datetime.datetime.now()), "Genesis Block", "0")

    # Obtention du dernier bloc dans la chaîne
    def get_latest_block(self):
        return self.chain[-1]

    # Ajout d'un nouveau bloc à la chaîne
    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    # Vérification de l'intégrité de la chaîne
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Vérification de la validité du hachage
            if current_block.hash != current_block.calculate_hash():
                return False

            # Vérification du lien entre le bloc actuel et le précédent
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# 3. Test de la chaîne
if __name__ == "__main__":
    # Création de la chaîne de blocs
    my_blockchain = Blockchain()

    # Ajout de nouveaux blocs
    my_blockchain.add_block(Block(1, str(datetime.datetime.now()), "Transaction du Bloc 1", ""))
    my_blockchain.add_block(Block(2, str(datetime.datetime.now()), "Transaction du Bloc 2", ""))

    # Affichage des blocs dans la chaîne
    for block in my_blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Date et heure: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Hachage du bloc précédent: {block.previous_hash}")
        print(f"Hachage du bloc actuel: {block.hash}")
        print("-" * 92)

    # Vérification de l'intégrité de la chaîne
    print("La chaîne de blocs est-elle valide ?", my_blockchain.is_chain_valid())