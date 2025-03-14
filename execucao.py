from operacao import Node, Trie


def main():
    trie = Trie()  # Inicializa a trie

    while True:
        try:
            command = input().strip()  # Lê o comando
        except EOFError:
            break  # Encerra no final da entrada

        if command == "e":
            break  # Encerra o programa
        elif command == "i":
            word = input().strip()  # Lê a palavra para inserção
            result = trie.insert(word)  # Insere na trie
            if result:
                print(result)
        elif command == "c":
            word = input().strip()  # Lê a palavra para consulta
            result = trie.search(word)  # Consulta a palavra
            if result:
                print(result)
        elif command == "f":
            result = trie.search_counter()  # Palavras mais consultadas
            if result:
                print(result)
        elif command == "p":
            result = trie.print_trie()  # Imprime a estrutura da trie
            if result:
                print(result)

main()

