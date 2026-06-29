#id;nome;selecao_id;posicao;idade;gols
from rich.prompt import Prompt
from utils import ler_inteiro, selecionar_id, obter_proximo_id

#id;nome;selecao_id;posicao;idade;gols 
def obter_nome_da_selecao(selecoes, selecao_id):
    for s in selecoes:
        if s['id'] == selecao_id:
            return s['nome']
    
    return "Selecao desconhecida"

def cadastrar_jogadores(jogadores, selecoes):
    print("Cadastrar jogador")

    selecao_id = selecionar_id(selecoes, "Selecione a seleção", 'id', 'nome')
    if not selecao_id:
        return None
    
    nome = input("Nome do jogador: ").strip()
    
    # Validação simples de posição
    posicoes = ["Goleiro", "Zagueiro", "Meio", "Atacante"]
    while True:
        posicao = input(f"Posição ({'/'.join(posicoes)}): ").strip()
        if posicao in posicoes:
            break
        print("Posição inválida.")
    
    idade = ler_inteiro("Idade: ", min_val=14, max_val=50)
    gols = ler_inteiro("Gols: ", min_val=0)
    
    return {
        "id": obter_proximo_id(jogadores, 'id'),
        "nome": nome,
        "selecao_id": selecao_id,
        "posicao": posicao,
        "idade": idade,
        "gols": gols
    }

def listar_jogadores(jogadores, selecoes):
    if not jogadores:
        print("Nenhum jogador cadastrado.")
        return
    
    print(f"{'ID':<4} {'Nome':<25} {'Seleção':<20} {'Pos':<10} {'Idade':<6} {'Gols':<5}")
    print("-" * 75)

    for j in jogadores:
        nome_selecao = obter_nome_da_selecao(selecoes, j.get('selecao_id'))
        print(f"{j['id']:<4};{j['nome']:<25};{nome_selecao:<20};{j['posicao']:<10};{j['idade']:<6};{j['gols']:<5}")


def buscar_jogadores_por_nome(jogadores, termo):
    termo = termo.lower()
    return [j for j in jogadores if termo in j.get('nome','').lower()]

def filtrar_jogadores_por_selecao(jogadores, selecoes):
    if not selecoes:
        print("Nenhuma seleção para filtrar.")
        return []

    try:
        id_sel = int(input("Digite o ID da seleção para filtrar: "))
    except ValueError:
        print("ID inválido.")
        return []
    
    return [j for j in jogadores if j.get('selecao_id') == id_sel]

def filtrar_por_posicao(jogadores, posicao_alvo):

    posicao_alvo = posicao_alvo.lower().strip()
    
    if not jogadores:
        return []

    filtrados = []

    for j in jogadores:
        if j.get('posicao', '').lower() == posicao_alvo:
            filtrados.append(j)
    
    return filtrados

def ordenar_por_idade(jogadores, decrescente=False):
    return sorted(jogadores, key=lambda j: j.get('idade', 0), reverse=decrescente)

def ordenar_por_gols(jogadores,decrescente=True):
    return sorted(jogadores, key=lambda j: j.get('gols', 0), reverse=decrescente)