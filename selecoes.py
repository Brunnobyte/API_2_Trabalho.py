from utils import ler_inteiro, obter_proximo_id

def cadastrar_selecoes(selecoes):
    print("Cadastrar Seleções")

    novo_id = obter_proximo_id(selecoes, 'id')
    nome = input("Nome seleção: ").strip()
    confederacao = input("Nome da confederação: ").strip()
    grupo = input("Grupo (A-F): ").strip().upper()
    ranking_fifa = ler_inteiro("Ranking fifa: ", min_val=1)
    titulos = ler_inteiro("Títulos: ", min_val=0)

    return {
        "id": novo_id,
        "nome": nome,
        "confederacao": confederacao,
        "grupo": grupo,
        "ranking_fifa": ranking_fifa,
        "titulos": titulos
    }

def listar_selecoes(selecoes):
    print(f"{len(selecoes)} selecoes cadastradas.")
    for selecao in selecoes:
        print('>', selecao['nome'], selecao['confederacao'], selecao['grupo'])
    
    print(20*'-')
    sucesso()

def buscar_selecoes_por_nome(selecoes, nome):
    resultados = []

    for selecao in selecoes:
        if nome.upper() in selecao['nome'].upper():
            resultados.append(selecao)

    return resultados

def filtrar_por_confederacao(selecoes, confederacao):
    resultados = []

    for selecao in selecoes:
        if confederacao.upper() in selecao['confederacao'].upper():
            resultados.append(selecao)

    return resultados

def filtrar_por_grupo(selecoes, grupo):
    resultados = []

    for selecao in selecoes:
        if grupo.upper() in selecao['grupo'].upper():
            resultados.append(selecao)

    return resultados

def ordenar_por_ranking_fifa(selecoes):

    return sorted(selecoes, key=lambda selecao: selecao['ranking_fifa'])

def ordenar_por_titulos(selecoes): 

    return sorted(selecoes, key=lambda selecao: selecao['titulos'], reverse=True)

def sucesso():
    print('Operacao realizada com sucesso!')


