


SEPARADOR = ";"
def montar_linha_selecao(s):
    # transforma o registro (dict) em uma string com os atributos separados por ;
    valores = [
        str(s["id"]),
        s["nome"],
        s["confederacao"],
        s["grupo"],
        str(s["ranking_fifa"]),
        str(s["titulos"]),
    ]
    return SEPARADOR.join(valores) # junta tudo com ";"

def salvar_selecoes(caminho, selecoes):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for s in selecoes:
            linha = montar_linha_selecao(s)
            arquivo.write(linha + "\n") # uma linha por registro
    print("Seleções salvas com sucesso!")


def montar_selecao_da_linha(linha):
    partes = linha.split(SEPARADOR) # separa a linha de volta em uma lista
    if partes and partes[-1] == "":
        partes.pop()
    if len(partes) != 6:
        raise ValueError(f"Formato inválido da linha: {linha!r}")
    selecao = {
        "id": int(partes[0]), # converte para int o que é número!
        "nome": partes[1],
        "confederacao": partes[2],
        "grupo": partes[3],
        "ranking_fifa": int(partes[4]),
        "titulos": int(partes[5]),
    }
    return selecao

def carregar_selecoes(caminho):
    selecoes = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip() # remove o "\n" e espaços
                if linha == "": # pula linhas em branco
                    continue
                selecoes.append(montar_selecao_da_linha(linha))
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhuma seleção carregada.")
    return selecoes


#id;nome;selecao_id;posicao;idade;gols
#montar_linha_jogador()
#montar_jogador_da_linha()

#salvar_jogadores()
#carregar_jogadores()

def montar_linha_jogador(j):
    
    index = [
        str(j["id"]),
        j["nome"],
        str(j["selecao_id"]),
        (j["posicao"]),
        str(j["idade"]),
        str(j["gols"]),
    ]
    return SEPARADOR.join(index)

def montar_jogador_da_linha(jogador):

    dados = jogador.split(SEPARADOR)
    if dados and dados[-1] == "":
        dados.pop()
    if len(dados) != 6:
        raise ValueError(f"Formato inválido da linha: {jogador!r}")
    jogadores = {
        "id": int(dados[0]),
        "nome": dados[1],
        "selecao_id": int(dados[2]),
        "posicao": dados[3],
        "idade": int(dados[4]),
        "gols": int(dados[5]),
    }
    return jogadores

def salvar_jogadores(caminho, jogadores):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for j in jogadores:
            jogador = montar_linha_jogador(j)
            arquivo.write(jogador + "\n")
    print("Jogadores salvos com sucesso!!")

def carregar_jogadores(caminho):
    jogadores = []
    try:
        with open(caminho, "r", encoding= "utf-8") as arquivo:
            for jogador in arquivo:
                jogador = jogador.strip()
                if jogador =="":
                    continue
                jogadores.append(montar_jogador_da_linha(jogador))
    except FileNotFoundError:
        print("O arquivo não foi enontrado. Nenhum jogador foi carregado.")
    return jogadores

#montar_linha_partida()
#montar_partida_da_linha()

#salvar_partidas()
#carregar_partidas()
#partidas.txt — ordem: id;selecao_casa_id;selecao_fora_id;gols_casa;gols_fora;fase

def montar_linha_partida(p):
    valores = [
        str(p["id"]),
        str(p["selecao_casa_id"]),
        str(p["selecao_fora_id"]),
        str(p["gols_casa"]),
        str(p["gols_fora"]),
        p["fase"], 
   ]
    return SEPARADOR.join(valores)

def montar_partida_da_linha(jogo):

    dados = jogo.split(SEPARADOR)
    if dados and dados[-1] =="":
        dados.pop()
    if len(dados) != 6:
        raise ValueError(f"Formato inválido encontrado na linha: {jogo!r}")
    partidas = {
        "id": int(dados[0]),
        "selecao_casa_id": int(dados[1]),
        "selecao_fora_id": int(dados[2]),
        "gols_casa": int(dados[3]),
        "gols_fora":int(dados[4]),
        "fase": dados[5]
    }
    return partidas

def salvar_partidas(caminho, partidas):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for p in partidas:
            jogo = montar_linha_partida(p)
            arquivo.write(jogo + "\n")
    print("Partidas salvas com sucesso!")


def carregar_partidas(caminho):
    partidas = []
    try:
        with open(caminho, "r", encoding= "utf=8") as arquivo:
            for jogo in arquivo:
                jogo = jogo.strip()
                if jogo == "":
                    continue
                partidas.append(montar_partida_da_linha(jogo))
    except FileNotFoundError:
            print("O arquivo não foi encontrado. Nenhuma partida foi carregada.")
    return partidas

def main():
    selecoes = carregar_selecoes('selecoes.txt')
    print(f'Total de seleções carregadas: {len(selecoes)}')
    for linha in selecoes:
        print(linha)

    jogadores = carregar_jogadores('jogadores.txt')
    print(f'Total de jogadores carregados: {len(jogadores)}')
    for jogador in jogadores:
        print(jogador)
    
    partidas = carregar_partidas('partidas.txt')
    print(f'Total de partidas carregadas: {len(partidas)}')
    for jogo in partidas:
        print(jogo)

if __name__ == "__main__":
    main()