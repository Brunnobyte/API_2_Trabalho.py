from utils import ler_inteiro, selecionar_id, obter_proximo_id
#id;selecao_casa_id;selecao_fora_id;gols_casa;gols_fora;fase
def obter_nome_da_selecao(selecoes, selecao_id):
     for s in selecoes:
        if s['id'] == selecao_id:
            return s['nome']
        
     return 'Desconhecida'

def formatar_partida(partida, selecoes):
    nome_casa = obter_nome_da_selecao(selecoes, partida ['selecao_casa_id'])
    nome_fora = obter_nome_da_selecao(selecoes, partida['selecao_fora_id'])
    return f"{nome_casa} {partida['gols_casa']} X {partida['gols_fora']} {nome_fora} ({partida['fase']})"

def cadastrar_partida(partidas, selecoes):
    print("--- CADASTRAR PARTIDA ---")
    
    casa_id = selecionar_id(selecoes, "Selecione o time da casa")
    if not casa_id: return None
    
    fora_id = selecionar_id(selecoes, "Selecione o time visitante")
    if not fora_id or fora_id == casa_id:
        print("Times devem ser diferentes.")
        return None # Ou repete a seleção
    
    gols_casa = ler_inteiro("Gols da casa: ", min_val=0)
    gols_fora = ler_inteiro("Gols do visitante: ", min_val=0)
    fase = input("Fase (Grupos/Oitavas/Quartas...): ").strip()
    
    return {
        "id": obter_proximo_id(partidas, 'id'),
        "selecao_casa_id": casa_id,
        "selecao_fora_id": fora_id,
        "gols_casa": gols_casa,
        "gols_fora": gols_fora,
        "fase": fase
    }

 
def listar_partidas(partidas, selecoes):
    if not partidas:
        print("Nenhuma partida cadastrada.")
        return
    print(f"{'ID':<4} {'partida':<45} {'fase':<15}")
    print("-" * 65)
    for p in partidas:
        print(f"{p['id']:<4} {formatar_partida(p, selecoes):<45} {p['fase']:<15}")

def buscar_partidas_casa_id(partidas, id_busca):
    try:
        id_busca = int(id_busca)
        for p in partidas:
            if p['id'] == id_busca:
                return [p]
        return[]
    except ValueError:
        return[]

def filtrar_partidas_por_fase(partidas):
    fase_alvo = input("Digite a fase para filtrar ").strip()
    return [p for p in partidas if p['fase'].upper() == fase_alvo.upper()]

def filtrar_partidas_por_time(partidas, selecoes):
    if not selecoes:
        return []
    
    nome_time = input("Nome do time para filtrar partidas: ").strip()
    time_alvo = None
    for s in selecoes:
        if nome_time.upper() in s['nome'].upper():
            time_alvo = s['id']
            break

    if not time_alvo:
        print("Time não encontrado.")
        return []
    
    return [p for p in partidas if p['selecao_casa_id'] == time_alvo or p['selecao_fora_id'] == time_alvo]

def filtrar_partidas_por_gols(partidas):
    try:
        min_gols = int(input("Minimo de gols totais na partida: "))
    except ValueError:
        return []
    return [p for p in partidas if (p["gols_casa"] + p["gols_fora"]) >= min_gols]

def ordenar_partidas_por_gols(partidas, decrescente=True):

    return sorted(partidas, key=lambda p: (p['gols_casa'] + p['gols_fora']), reverse=decrescente)


def ordenar_partidas_por_fase(partidas):

    return sorted(partidas, key=lambda p: p['fase'])

def calcular_estatisticas_da_partida(partida, selecoes):
    """
    Calcula o resultado de UMA partida para uma seleção específica.
    Retorna um dict com: pontos, saldo, gols_pro, gols_contra, vitorias, empates, derrotas.
    """
    # Identifica os IDs
    id_casa = partida['selecao_casa_id']
    id_fora = partida['selecao_fora_id']
    gols_casa = partida['gols_casa']
    gols_fora = partida['gols_fora']

    # Inicializa estatísticas para ambos (serão atualizadas depois)
    # Calcular o impacto de uma partida e retornar um dict de mudanças.
    
    stats = {
        "casa": {"pontos": 0, "saldo": 0, "gols_pro": 0, "gols_contra": 0, "v": 0, "e": 0, "d": 0},
        "fora": {"pontos": 0, "saldo": 0, "gols_pro": 0, "gols_contra": 0, "v": 0, "e": 0, "d": 0}
    }

    # Atualiza Gols
    stats["casa"] ["gols_pro"] = gols_casa
    stats["casa"] ["gols_contra"] = gols_fora
    stats["casa"] ["saldo"] = gols_casa - gols_fora

    stats["fora"] ["gols_pro"] = gols_fora
    stats["fora"] ["gols_contra"] = gols_casa
    stats["fora"] ["saldo"] = gols_fora - gols_casa

    # Determina Vitória/Empate
    if gols_casa > gols_fora:
        # Casa venceu
        stats["casa"] ["pontos"] = 3
        stats["casa"] ["v"] = 1
        stats["fora"] ["pontos"] = 0
        stats["fora"] ["d"] = 1
    elif gols_fora > gols_casa:
        # Fora venceu
        stats["fora"] ["pontos"] = 3
        stats["fora"] ["v"] = 1
        stats["casa"] ["pontos"] = 0
        stats["casa"] ["d"] = 1
    else:
        # Empate
        stats["casa"] ["pontos"] = 1
        stats["casa"] ["e"] = 1
        stats["fora"] ["pontos"] = 1
        stats["fora"] ["e"] = 1

    return stats

def gerar_tabela_classificacao(grupo_letra, selecoes, partidas):
    """
    Gera a tabela de classificação para um grupo específico.
    Retorna uma lista de dicionários ordenada.
    """
    # Filtra seleções do grupo
    selecoes_grupo = [s for s in selecoes if s['grupo'].upper() == grupo_letra.upper()]
    
    if not selecoes_grupo:
        print(f"Nenhuma seleção encontrada no grupo {grupo_letra}.")
        return []

    # Inicializa a estrutura de dados para cada seleção
    # Chave: ID da seleção, Valor: dict de estatísticas acumuladas
    tabela = {}
    for s in selecoes_grupo:
        tabela[s['id']] = {
            "id": s['id'],
            "nome": s['nome'],
            "jogos": 0,
            "v": 0,
            "e": 0,
            "d": 0,
            "gp": 0, # Gols Pró
            "gc": 0, # Gols Contra
            "sg": 0, # Saldo de gols
            "pontos": 0
        }

    # Percorre TODAS as partidas e acumula estatísticas
    for p in partidas:
        # Só processa se a partida for do grupo (opcional, mas recomendado se houver outras fases)
        # Se a partida for "Grupos", verificamos se os times pertencem ao grupo alvo
        casa_data = calcular_estatisticas_da_partida(p, selecoes)
        
        # Verifica se os times da partida pertencem ao grupo pedido
        # (Assumindo que a partida de grupo envolve times do grupo)
        # Se o ID da casa estiver na nossa tabela de estatísticas
        if p['selecao_casa_id'] in tabela:
            stats = casa_data["casa"]
            tabela[p['selecao_casa_id']] ['jogos'] += 1
            tabela[p['selecao_casa_id']] ['v'] += stats['v']
            tabela[p['selecao_casa_id']] ['e'] += stats['e']
            tabela[p['selecao_casa_id']] ['d'] += stats['d']
            tabela[p['selecao_casa_id']] ['gp'] += stats['gols_pro']
            tabela[p['selecao_casa_id']] ['gc'] += stats['gols_contra']
            tabela[p['selecao_casa_id']] ['sg'] += stats['saldo']
            tabela[p['selecao_casa_id']] ['pontos'] += stats['pontos']

        if p['selecao_fora_id'] in tabela:
            stats = casa_data["fora"]
            tabela[p['selecao_fora_id']] ['jogos'] += 1
            tabela[p['selecao_fora_id']] ['v'] += stats['v']
            tabela[p['selecao_fora_id']] ['e'] += stats['e']
            tabela[p['selecao_fora_id']] ['d'] += stats['d']
            tabela[p['selecao_fora_id']] ['gp'] += stats['gols_pro']
            tabela[p['selecao_fora_id']] ['gc'] += stats['gols_contra']
            tabela[p['selecao_fora_id']] ['sg'] += stats['saldo']
            tabela[p['selecao_fora_id']] ['pontos'] += stats['pontos']

    # Converte o dict para lista para ordenação
    lista_tabela = list(tabela.values())

    # Ordenação com múltiplos critérios 
    # Ordena por: Pontos (DESC), depois Saldo de Gols (DESC), depois Gols Pró (DESC)
    # Usamos uma chave com tupla: (-pontos, -saldo, -gp) para facilitar a ordenação decrescente
    lista_ordenada = sorted(lista_tabela, key=lambda x: (-x['pontos'], -x['sg'], -x['gp']))

    return lista_ordenada

def mostrar_tabela_grupo(grupo_letra, selecoes, partidas):
    
    tabela = gerar_tabela_classificacao(grupo_letra, selecoes, partidas)
    
    if not tabela:
        return

    print(f"\n{'='*60}")
    print(f"CLASSIFICAÇÃO - GRUPO {grupo_letra.upper()}")
    print(f"{'='*60}")
    print(f"{'Pos':<4} {'Seleção':<20} {'P':<3} {'V':<3} {'E':<3} {'D':<3} {'GP':<3} {'GC':<3} {'SG':<4}")
    print("-" * 60)

    for i, time in enumerate(tabela):
        pos = f"{i+1}º"
        print(f"{pos:<4} {time['nome']:<20} {time['pontos']:<3} {time['v']:<3} {time['e']:<3} {time['d']:<3} {time['gp']:<3} {time['gc']:<3} {time['sg']:<4}")
    
    print(f"{'='*60}\n")