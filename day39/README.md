# Day 39 - Hangman

## Objetivo 🎯
- Transformar uma sentença inserida pelo usuário em um "arco-iris".

## O que fiz 💻

- Defini uma variável-lista para cada cor
- Criei um loop `for` com condicionais para trocar a cor da letra contida na frase do usuário
- `print('\033[0m', end='')` para retornar à cor original
- Imprimi a frase original e a mesma "arcoirizada"

## Como executar ⏯️
No terminal, execute:
```bash
python main.py