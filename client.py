import rpyc
from constRPYC import * 

conn = rpyc.connect(SERVER, PORT)
print("Conectado ao servidor RPyC.")

db_list = conn.root

print("--- Demonstração das Operações na Lista Remota ---")

print("\n1. Adicionando elementos [20, 10, 30]...")
db_list.exposed_append(20)
db_list.exposed_append(10)
db_list.exposed_append(30)
print(f"   Lista atual no servidor: {db_list.exposed_value()}")

print("\n2. Inserindo o número 15 na posição 1...")
db_list.exposed_insert(1, 15)
print(f"   Lista atual no servidor: {db_list.exposed_value()}")

print("\n3. Ordenando a lista...")
db_list.exposed_sort()
print(f"   Lista ordenada no servidor: {db_list.exposed_value()}")

print("\n4. Pesquisando pelo elemento 20...")
index = db_list.exposed_find(20)
print(f"   O elemento 20 está na posição: {index}")

print("\n5. Pesquisando pelo elemento 99 (inexistente)...")
index = db_list.exposed_find(99)
print(f"   Resultado da busca por 99: {index}")

print("\n6. Removendo o elemento 15...")
removido = db_list.exposed_remove(15)
print(f"   Remoção bem-sucedida: {removido}")
print(f"   Lista final no servidor: {db_list.exposed_value()}")

print("\n7. Tentando remover o elemento 99 (inexistente)...")
removido = db_list.exposed_remove(99)
print(f"   Remoção bem-sucedida: {removido}")
print(f"   Lista final no servidor: {db_list.exposed_value()}")

conn.close()
print("\nConexão com o servidor fechada.")
