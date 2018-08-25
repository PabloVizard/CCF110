from typing import NamedTuple
n = 50
class reg (NamedTuple):
    nome = [0 for i in range(n)]
    class end (NamedTuple):
        rua = [0 for i in range(n)]
        bairro = [0 for i in range(n)]
        cidade = [0 for i in range(n)]
        estado = [0 for i in range(n)]
        cep = [0 for i in range(n)]

    salario = [0 for i in range(n)]
    identidade = [0 for i in range(n)]
    cpf = [0 for i in range(n)]
    estadocivil = [0 for i in range(n)]
    telefone = [0 for i in range(n)]
    idade = [0 for i in range(n)]
    sexo = [0 for i in range(n)]

for i in range(n):
    reg.nome[i] = input("Nome: ")
    reg.end.rua[i] = input("Rua: ")
    reg.end.bairro[i] = input("Beirro: ")
    reg.end.cidade[i] = input("Cidade: ")
    reg.end.estado[i] = input("Estado: ")
    reg.end.cep[i] = input("CEP: ")
    reg.salario[i] = float(input("Salario: "))
    reg.identidade[i] = input("Identidade: ")
    reg.cpf[i] = input("CPF: ")
    reg.estadocivil[i] = input("Estado Civil: ")
    reg.telefone[i] = int(input("Telefone: "))
    reg.idade[i] = int(input("Idade: "))
    reg.sexo[i] = input("Sexo: ")

for i in range(n):
    if reg.salario[i] >= 500:
        if reg.estadocivil[i] == 'Casado':
            if reg.end.estado[i] == 'SP':
                print(reg.nome[i])