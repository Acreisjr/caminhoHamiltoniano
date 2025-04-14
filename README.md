# Caminho Hamiltoniano em Python

## Descrição do Projeto

Este projeto tem como objetivo encontrar um caminho Hamiltoniano em um grafo, utilizando uma abordagem de backtracking. O grafo é representado por uma matriz de adjacência e o caminho Hamiltoniano é uma sequência em que cada vértice aparece exatamente uma vez.

## Explicação do Algoritmo

O algoritmo é composto por três funções principais que colaboram para encontrar o caminho:

### 1. Função `pode_visitar`
Esta função verifica se é possível incluir um vértice candidato na posição atual do caminho. São realizadas duas verificações:
- **Conectividade:** Verifica se existe uma aresta entre o último vértice adicionado no caminho e o vértice candidato.  
  ~~~python
  if matriz_adj[caminho[etapa - 1]][candidato] == 0:
      return False
  ~~~
- **Unicidade:** Confirma que o vértice candidato ainda não foi incluído no caminho.  
  ~~~python
  if candidato in caminho:
      return False
  ~~~  
Se ambas as condições forem satisfeitas, o vértice pode ser visitado:
  ~~~python
  return True
  ~~~

### 2. Função `busca_caminho`
Esta função é responsável por construir o caminho de forma recursiva usando backtracking:
- **Caso Base:** Se a posição atual (`etapa`) igualar o número de vértices, significa que o caminho está completo.
  ~~~python
  if etapa == len(matriz_adj):
      return True
  ~~~
- **Exploração de Candidatos:** Para cada vértice candidato (excetuando o vértice inicial), a função verifica se é seguro adicioná-lo usando `pode_visitar`.  
  ~~~python
  for candidato in range(1, len(matriz_adj)):
      if pode_visitar(candidato, etapa, caminho, matriz_adj):
          caminho[etapa] = candidato
          if busca_caminho(matriz_adj, caminho, etapa + 1):
              return True
          caminho[etapa] = -1
  return False
  ~~~
Caso a inclusão do candidato não conduza a uma solução completa, ele é removido (backtracking) e o algoritmo tenta outras alternativas.

### 3. Função `encontrar_caminho_hamiltoniano`
Esta função inicia o processo de busca:
- **Inicialização:** Cria um vetor `caminho` com tamanho igual ao número de vértices, definindo o vértice inicial como `0`.
  ~~~python
  caminho = [-1] * n
  caminho[0] = 0
  ~~~
- **Chamada Recursiva:** Invoca a função `busca_caminho` a partir da segunda posição.
  ~~~python
  if not busca_caminho(matriz_adj, caminho, 1):
      return None
  return caminho
  ~~~

### 4. Bloco Principal
No bloco `if __name__ == "__main__":`, o algoritmo é executado em um grafo de teste composto por 5 vértices:
  ~~~python
  if __name__ == "__main__":
      grafo = [
          [0, 1, 1, 1, 1],
          [1, 0, 1, 1, 1],
          [1, 1, 0, 1, 1],
          [1, 1, 1, 0, 1],
          [1, 1, 1, 1, 0]
      ]
      solucao = encontrar_caminho_hamiltoniano(grafo)
      if solucao:
          print("Caminho Hamiltoniano encontrado:")
          print(solucao)
      else:
          print("Nenhum Caminho Hamiltoniano encontrado.")
  ~~~
Esta parte do código define o grafo e imprime o caminho Hamiltoniano encontrado, ou uma mensagem informando que não foi possível encontrar um caminho.

## Como Executar o Projeto

1. **Pré-requisito:** Certifique-se de que o Python 3 esteja instalado em seu sistema.
2. **Salvar o Código:** Guarde o código fonte em um arquivo com o nome `main.py`.
3. **Executar:** No terminal, navegue até o diretório contendo o arquivo e execute o comando:
   ~~~bash
   python main.py
   ~~~
4. **Resultado:** O programa exibirá, no terminal, o caminho Hamiltoniano se encontrado, ou indicará que não existe um caminho para o grafo fornecido.

## Relatório Técnico

### Complexidade do Problema
- **NP-Completo:** O problema do Caminho Hamiltoniano é reconhecidamente NP-Completo, o que implica que, embora a verificação de uma solução seja feita em tempo polinomial, encontrar essa solução pode ser computacionalmente custoso.
- **Backtracking:** A abordagem adotada com backtracking tem complexidade O(n!) no pior cenário, devido à quantidade de permutações possíveis dos vértices.

### Análise de Casos
- **Melhor Caso:** Ocorre quando um caminho válido é encontrado logo nas primeiras tentativas, reduzindo significativamente o tempo de execução.
- **Pior Caso:** Se for necessário explorar todas as permutações possíveis para determinar a inexistência de um caminho, o tempo de execução cresce de forma fatorial.
- **Caso Médio:** Geralmente depende da densidade e estrutura do grafo, podendo variar entre os extremos.

### Considerações sobre o Teorema Mestre
O Teorema Mestre não se aplica diretamente ao algoritmo de backtracking utilizado, pois este não subdivide o problema em partes de tamanho fixo, como é requerido pelos casos clássicos de aplicação do teorema.

### Autor : Alberto da Costa Reis Júnior