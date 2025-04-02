# DICIONÁRIO

aluno = {
    "Nome" : "João",
    "Idade" : 20,
    "Curso" : "Ciência de Dados"
}

print(aluno)

# Acelerando valores pelo nome das "CHAVES"
print(aluno["Nome"]) #João
print(aluno["Idade"]) #20

# Adiciona um novo par de chave-valor ("email" : "joao8@email.com")
aluno["email"] = "joao8@email.com"
print(aluno)  

# Modifica um valor
aluno["Idade"] = 21
print(aluno)

# Remover um item pelo nome da chave
del aluno["Curso"]
print(aluno)

# Verificação de Chaves

print("Idade" in aluno) #TRUE
print("Curso" in aluno) #FALSE

# Iterando sobre o dicionário
for chave, valor in aluno.items():
    print(f"{chave} : {valor}")

# Lista de dicionário

alunos = [
    {
    "Nome" : "João",
    "Idade" : 20,
    "Curso" : "Ciência de Dados"
    },
    {
    "Nome" : "Matheus",
    "Idade" : 27,
    "Curso" : "Ciência de Dados"
    },
    {
    "Nome" : "Jessica",
    "Idade" : 25,
    "Curso" : "Redes"
    }
]

for aluno in alunos:
    print("Dados do aluno: ")
    for chave, valor in aluno.items():
        print(f"{chave} : {valor}")
    print("-" * 20)