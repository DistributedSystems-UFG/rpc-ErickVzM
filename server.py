import rpyc
from constRPYC import * 
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    """Adiciona um elemento ao final da lista."""
    self.value.append(data)
    print(f"Adicionado: {data}. Lista atual: {self.value}")
    return self.value

  def exposed_value(self):
    """Retorna o valor atual da lista."""
    return self.value

  def exposed_insert(self, index, data):
    """Insere um elemento em um índice específico."""
    if 0 <= index <= len(self.value):
      self.value.insert(index, data)
      print(f"Inserido: {data} na posição {index}. Lista atual: {self.value}")
      return True
    print(f"Erro: Índice {index} fora do alcance.")
    return False

  def exposed_remove(self, data):
    """Remove a primeira ocorrência de um elemento da lista."""
    try:
      self.value.remove(data)
      print(f"Removido: {data}. Lista atual: {self.value}")
      return True
    except ValueError:
      print(f"Erro: Item {data} não encontrado para remoção.")
      return False

  def exposed_find(self, data):
    """Encontra o índice da primeira ocorrência de um elemento."""
    try:
      index = self.value.index(data)
      print(f"Item {data} encontrado na posição {index}.")
      return index
    except ValueError:
      print(f"Item {data} não encontrado na lista.")
      return -1 

  def exposed_sort(self, reverse_order=False):
    """Ordena a lista."""
    self.value.sort(reverse=reverse_order)
    print(f"Lista ordenada. Ordem reversa={reverse_order}. Lista atual: {self.value}")
    return self.value


if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  print(f"Servidor iniciado na porta {PORT}...")
  server.start()
