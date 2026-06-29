Um sistema de gerenciamente da copa do mundo de 2026, desenvolvido em python.
Para rodar este sistema você primeiro precisa da biblioteca rich instalada.

Menu: No menu, você pode cadastrar tanto jogadores como seleções e partidas feitas entre as seleções.
rodando o menu siga as instruções que ele pede, como por exemplo: se for cadastrar um jogador, primeiro cadastre uma seleção, depois de ter a seleção cadastrada 
selecione ela e siga botando, nome, posição, idade e gols.

copa_manager/
├── main.py           # Só o menu e o laço principal (while). Quase sem lógica.
├── persistencia.py   # Carregar e gravar os .txt (padrão de string + separador)
├── selecoes.py       # Funções de seleções (cadastrar, listar, buscar, filtrar...)
├── jogadores.py      # Funções para CRUD de jogadores (cadastrar, listar, filtrar, ordenar)
├── partidas.py       # Funções de partidas e classificação
├── utils.py          # Funções utilitárias (leitura de inteiros, seleção de IDs, etc.)
│
├── selecoes.txt # Dados gravados/lidos pelo programa
├── jogadores.txt
└── partidas.txt

