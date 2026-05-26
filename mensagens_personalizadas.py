class Cliente:
  __init__(self, nome, cidade):
    self.nome = nome
    self.cidade = cidade

  @property
  def nome(self, nome):
    return self._nome

  @nome.setter
  def nome(self, nome):
    self._nome = nome

  @property
  def cidade(self, cidade):
    return self._cidade

  @cidade.setter
  def cidade(self, cidade):
    self._cidade = cidade

  def __str__(self):
    return(f'Olá, {self._nome}! Bem-vindo(a) ao sistema da cidade de {self._cidade}.')

nome = input('Digite o nome do cliente: ')
cidade = input('Digite a cidade do cliente: ')
