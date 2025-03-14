class Node:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.last = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node("root")
        self.inserted_words = []  # lista com todas as palavras inseridas para facilitar algumas funções

    def find(self, word):
        """criei essa outra busca para usar na hora de inserir, com a outra ficava atualizava o contandor, então pensei nessa solução."""
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                return False
            pointer = pointer.children[letter]
        return pointer.last

    def search(self, word):
        """Busca normal mesmo."""
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                return print(f"palavra inexistente: {word}")
            pointer = pointer.children[letter]
        if not pointer.last:
            return print(f"palavra inexistente: {word}")
        else:
            pointer.count += 1
            return print(f"palavra existente: {word} {pointer.count}")

    def insert(self, word):
        if self.find(word):
            print(f"palavra ja existente: {word}")
            return
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                pointer.children[letter] = Node(letter)
            pointer = pointer.children[letter]
        pointer.last = True  # Marca o final da palavra
        self.inserted_words.append(word)  # Adiciona a palavra à lista
        print(f"palavra inserida: {word}")

    def search_counter(self):
        if not self.inserted_words:
            print("trie vazia")
            return

        max_count = 0
        max_words = []
        for word in self.inserted_words:
            pointer = self.root
            for letter in word:
                pointer = pointer.children[letter]
            if pointer.count > max_count:
                max_count = pointer.count
                max_words = [word]  # Atualiza a lista
            elif pointer.count == max_count:
                max_words.append(word)  # Adiciona a palavra com contagem igual ao máximo

        if not max_words:
            print("trie vazia")
            return

        max_words.sort()  
        print("palavras mais consultadas:")
        for word in max_words:
            print(word)
        print(f"numero de acessos: {max_count}")

    def print_trie(self):
        if not self.root.children:
            print("trie vazia")
            return

        def traverse(node, pointer):
            if pointer == "root":
                children_letters = sorted(node.children.keys())
                print(f"letra: raiz - {' '.join(children_letters)}")
            else:
                children_letters = sorted(node.children.keys())
                if node.last:
                    children_letters.append("*")
                print(f"letra: {pointer} - {' '.join(children_letters)}")

            if node.last:
                print("letra: *")

            for key in sorted(node.children.keys()):
                traverse(node.children[key], key)

        traverse(self.root, "root")

#Teste
'''ex = Trie()
ex.insert('casa')
ex.insert('carro')
ex.insert('caro')
ex.insert('bala')
ex.insert('balao')
ex.search('bala')
ex.search('carro')
ex.search_counter()
ex.print_trie()'''
