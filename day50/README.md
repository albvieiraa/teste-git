# Day 50 - Idea Storage

## Objetivo 🎯
-  Implementar o sistema de armazenamento de ideias.
  
## O que fiz 💻

- Menu principal: adicionar ideia, carregar ideia aleatória ou sair.
- Adicionar uma ideia: recebe uma entrada do usuário, verifica se não está vazia e adiciona ao arquivo 'my.ideas' no modo append `"a"`
- Carregar ideia: Abre o arquivo my.ideas no modo leitura `"r"`, carrega todas as ideias, escolhe uma aleatória com `random.choice()` e a exibe. Caso o arquivo não exista ou esteja vazio, exibe mensagens apropriadas.
- Saida do programa: selecionando a opção 3.

## Como executar ⏏️▶️
No terminal, execute:
```bash
python main.py
```
