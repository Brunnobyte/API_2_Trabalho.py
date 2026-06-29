def ler_inteiro(mensagem, min_val=None, max_val=None):
    """Lê um inteiro com validação de faixa."""
    while True:
        try:
            valor = int(input(mensagem))
            if min_val is not None and valor < min_val:
                print(f"Valor deve ser maior ou igual a {min_val}.")
                continue
            if max_val is not None and valor > max_val:
                print(f"Valor deve ser menor ou igual a {max_val}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def selecionar_id(lista_itens, titulo, chave_id='id', chave_nome='nome'):
    """Mostra lista e pede para escolher um ID válido."""
    if not lista_itens:
        print("Nenhum item cadastrado.")
        return None
    
    print(f"--- {titulo} ---")
    for item in lista_itens:
        print(f"{item[chave_id]} - {item[chave_nome]}")
    
    while True:
        try:
            id_escolhido = int(input("Digite o ID da opção: "))
            # Verifica se existe
            if any(item[chave_id] == id_escolhido for item in lista_itens):
                return id_escolhido
            print("ID não encontrado. Tente novamente.")
        except ValueError:
            print("Digite um número válido.")

def obter_proximo_id(lista_itens, chave_id='id'):
    """Retorna maior ID + 1."""
    if not lista_itens:
        return 1
    return max(item[chave_id] for item in lista_itens) + 1