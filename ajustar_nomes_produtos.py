class Produto:
  def deixar_minúsculo(self):
    self._nome = self._nome.lower()

  def remover_espacos_extra(self):
    self._nome = self._nome.strip()

  @property
  def nome(self):
    return self._nome

  @nome.setter
  def nome(self, nome: str):
    if len(nome) <= 1:
      rase ValueError('Perdão, mas não é possível guardar um nome de produto tão pequeno')
    else:
      self._nome = nome
      
      self.deixar_minusculo()
      self.remover_espacos_extra()
      # Notas: 
      # 1. Como as duas funções criadas antes do init interagem diretamente com o self,
      # não há necessidade de fazer algo como "self._nome = self._nome.função()",
      # pois a ação de modificar o parâmetro "_nome" no self já ocorre nas funções.
      # 2. O encadeamento de funções [parâmetro.função().função()] não funcionaria neste caso
      # pois as funções em si não têm retorno (não há "return") e, portanto, a primeira funcionaria perfeitamente,
      # mas a segunda daria um erro pois estaria recebendo um None vindo da primeira função.
      
      # Opção mais eficiente (não utilizada para manter o senso dos comentários acima):
      # nome_tratado = nome.lower().strip()
      # self.nome = nome_tratado
    
  def __init__(self, nome: str):
    self.nome = nome
    # Notas: 
    # 1. A lógica para não colocar "_" antes do nome é que não se está aplicando o nome a _nome diretamente,
    # mas segue-se o caminho: nome.setter -> verifica se a string é grande o bastante -> se sim, salva em self._nome
    
  def __str__(self):
    return self._nome

while True:
  try:
    nome_produto = input('Digite o nome do produto, por favor: ')
    produto = Produto(nome_produto)
    break
  except ValueError as e:
    print(f'Erro: {e}')

print(f'Confira: o nome do produto é {produto}')
