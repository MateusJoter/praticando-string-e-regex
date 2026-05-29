class Cliente:
  def __init__(self, nome, cidade):
    self.nome = nome
    self.cidade = cidade

  @property
  def nome(self):
    return self._nome

  @nome.setter
  def nome(self, nome):
    self._nome = nome

  @property
  def cidade(self):
    return self._cidade

  @cidade.setter
  def cidade(self, cidade):
    self._cidade = cidade

  @property
  def boas_vindas(self):
    return(f'Olá, {self._nome}! Bem-vindo(a) ao sistema da cidade de {self._cidade}.')

nome = input('Digite o nome do cliente: ')
cidade = input('Digite a cidade do cliente: ')

cliente = Cliente(nome, cidade)
print(cliente.boas_vindas)
