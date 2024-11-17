import os
import json

def listar_tarefas(tarefas):
    print()
    if not tarefas:
        print("Nenhuma tarefa para listar.")
        print()
        return
    
    print("TAREFAS: ")
    for tarefa in tarefas:
        print(f"\t {tarefa}")
    print()


def desfazer_tarefas(tarefas, refazer_tarefas):
    print()
    if not tarefas:
        print("Nenhma tarefa para desfazer.")
        print()
        return
    
    tarefa = tarefas.pop()
    refazer_tarefas.append(tarefa)
    print()
    listar_tarefas(tarefas)


def refazer_tarefas(tarefas, refazer_tarefas):
    print()
    if not refazer_tarefas:
        print("Nenhuma tarefa para refazer.")
        print()
        return
    
    tarefa = refazer_tarefas.pop()
    tarefas.append(tarefa)
    print()
    listar_tarefas(tarefas)


def adicionar_tarefa(tarefa, lista_tarefa):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print("Você não digitou nada.")
        print()
        return
    lista_tarefa.append(tarefa)
    print()
    listar_tarefas(tarefas)


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo não existe!")
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = 'aula120.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_resfazer = []

while True:
    print("COMANDOS: listar, desfazer, refazer")
    tarefa = input("Digite uma tarefa ou comando: ")

    comandos = {
        'listar': lambda: listar_tarefas(tarefas),
        'desfazer': lambda: desfazer_tarefas(tarefas, tarefas_resfazer),
        'refazer': lambda: refazer_tarefas(tarefas, tarefas_resfazer),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicionar_tarefa(tarefa, tarefas)
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)