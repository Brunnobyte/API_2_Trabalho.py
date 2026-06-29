from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.text import Text

from persistencia import carregar_selecoes, salvar_selecoes, carregar_jogadores, salvar_jogadores, carregar_partidas, salvar_partidas
from selecoes import cadastrar_selecoes, listar_selecoes, buscar_selecoes_por_nome, filtrar_por_grupo
from jogadores import cadastrar_jogadores, listar_jogadores, filtrar_por_posicao, ordenar_por_gols
from partidas import cadastrar_partida, listar_partidas, mostrar_tabela_grupo

console = Console()

def mostrar_status(selecoes, jogadores, partidas):
    texto = Text()
    texto.append(f"Seleções: {len(selecoes)} | ", style="bold cyan")
    texto.append(f"Jogadores: {len(jogadores)} | ", style="bold magenta")
    texto.append(f"Partidas: {len(partidas)}", style="bold green")
    return Panel(texto, title="⚽ COPA MANAGER 2026 - STATUS", border_style="blue")

def exibir_menu():
    console.clear()
    console.print(mostrar_status(selecoes, jogadores, partidas))
    
    menu_text = Text()
    menu_text.append("\n--- SELEÇÕES ---\n", style="bold yellow")
    menu_text.append("1. Cadastrar Seleção\n")
    menu_text.append("2. Listar Seleções\n")
    menu_text.append("3. Buscar Seleção por Nome\n")
    menu_text.append("4. Filtrar por Grupo\n")
    
    menu_text.append("\n--- JOGADORES ---\n", style="bold yellow")
    menu_text.append("5. Cadastrar Jogador\n")
    menu_text.append("6. Listar Todos os Jogadores\n")
    menu_text.append("7. Filtrar Jogadores por Posição\n")
    menu_text.append("8. Ordenar Jogadores por Gols (Artilheiros)\n")
    
    menu_text.append("\n--- PARTIDAS ---\n", style="bold yellow")
    menu_text.append("9. Cadastrar Partida\n")
    menu_text.append("10. Listar Partidas\n")
    menu_text.append("11. Ver Tabela de Classificação\n")
    
    menu_text.append("\n--- SISTEMA ---\n", style="bold red")
    menu_text.append("0. Salvar e Sair\n")
    
    console.print(Panel(menu_text, title="MENU PRINCIPAL", border_style="green"))

def main():
    global selecoes, jogadores, partidas
     
    console.print("[bold blue]⚡ Carregando dados...[/bold blue]")
    selecoes = carregar_selecoes('selecoes.txt')
    jogadores = carregar_jogadores('jogadores.txt')
    partidas = carregar_partidas('partidas.txt')
    
    console.print(f"✅ Carregados: {len(selecoes)} seleções, {len(jogadores)} jogadores, {len(partidas)} partidas.\n")
    
    while True:
        exibir_menu()
        
        try:
            
            opcao = IntPrompt.ask("Escolha uma opção", choices=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"], default=0)
        except KeyboardInterrupt:
            console.print("\n[yellow]⚠️ Interrupção do usuário. Salvando e saindo...[/yellow]")
            salvar_selecoes('selecoes.txt', selecoes)
            salvar_jogadores('jogadores.txt', jogadores)
            salvar_partidas('partidas.txt', partidas)
            break

        if opcao == 1:
            novo = cadastrar_selecoes(selecoes)
            if novo:
                selecoes.append(novo)
                console.print("[green]✅ Seleção cadastrada com sucesso![/green]")
            console.input("\n[press ENTER to continue]")

        elif opcao == 2:
            listar_selecoes(selecoes)
            console.input("\n[press ENTER to continue]")

        elif opcao == 3:
            termo = Prompt.ask("Nome da seleção para buscar")
            resultados = buscar_selecoes_por_nome(selecoes, termo)
            if resultados:
                console.print(f"[bold green]Encontradas {len(resultados)} seleções:[/bold green]")
                for s in resultados:
                    console.print(f"  • {s['nome']} ({s['grupo']})")
            else:
                console.print("[red]Nenhuma seleção encontrada.[/red]")
            console.input("\n[press ENTER to continue]")

        elif opcao == 4:
            grupo = Prompt.ask("Grupo (A-F)").strip().upper()
            filtrados = filtrar_por_grupo(selecoes, grupo)
            listar_selecoes(filtrados)
            console.input("\n[press ENTER to continue]")

        elif opcao == 5:
            novo_jogador = cadastrar_jogadores(jogadores, selecoes)
            if novo_jogador:
                jogadores.append(novo_jogador)
                console.print("[green]✅ Jogador cadastrado com sucesso![/green]")
            console.input("\n[press ENTER to continue]")

        elif opcao == 6:
            
            listar_jogadores(jogadores, selecoes)
            console.input("\n[press ENTER to continue]")

        
        elif opcao == 7:
            console.print("\n[bold blue]--- FILTRAR POR POSIÇÃO ---[/bold blue]")
           
            posicao_alvo = Prompt.ask("Digite a posição (ex: Atacante, Goleiro, Zagueiro)").strip().title()
            
            
            resultados_filtrados = filtrar_por_posicao(jogadores, posicao_alvo)
            
            if not resultados_filtrados:
                console.print(f"[yellow]Nenhum jogador encontrado com a posição '{posicao_alvo}'.[/yellow]")
            else:
                console.print(f"[green]Encontrados {len(resultados_filtrados)} jogadores na posição '{posicao_alvo}'![/green]")
                
                listar_jogadores(resultados_filtrados, selecoes)
            
            console.input("\n[press ENTER to continue]")

        
        elif opcao == 8:
            console.print("\n[bold blue]--- ORDENAR POR GOLS (ARTEIHEIROS) ---[/bold blue]")
            
            
            lista_ordenada = ordenar_por_gols(jogadores)
            
            if not lista_ordenada:
                console.print("[yellow]Nenhum jogador cadastrado para ordenar.[/yellow]")
            else:
                console.print("[green]Lista ordenada dos maiores artilheiros:[/green]")
                listar_jogadores(lista_ordenada, selecoes)
            
            console.input("\n[press ENTER to continue]")

        elif opcao == 9:
            
            nova_partida = cadastrar_partida(partidas, selecoes)
            if nova_partida:
                partidas.append(nova_partida)
                console.print("[green]✅ Partida cadastrada com sucesso![/green]")
            console.input("\n[press ENTER to continue]")

        elif opcao == 10:
            
            listar_partidas(partidas, selecoes)
            console.input("\n[press ENTER to continue]")

        elif opcao == 11:
            
            grupo_letra = Prompt.ask("Digite a letra do grupo (A-F)").strip().upper()
            mostrar_tabela_grupo(grupo_letra, selecoes, partidas)
            console.input("\n[press ENTER to continue]")

        elif opcao == 0:
            console.print("\n[bold yellow]Salvando dados...[/bold yellow]")
            salvar_selecoes('selecoes.txt', selecoes)
            salvar_jogadores('jogadores.txt', jogadores)
            salvar_partidas('partidas.txt', partidas)
            console.print("[green]✅ Dados salvos com sucesso! Até a próxima! 👋[/green]")
            break
        else:
            console.print("[red]Opção inválida.[/red]")
            console.input("\n[press ENTER to continue]")

if __name__ == "__main__":
    main()