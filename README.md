# 📝 To-Do List Moderna

Uma aplicação de lista de tarefas desenvolvida em **Python** utilizando a biblioteca **CustomTkinter**, com interface moderna, suporte a modo escuro e salvamento automático das tarefas.

## 📌 Funcionalidades

* ✅ Adicionar novas tarefas
* ✔️ Marcar tarefas como concluídas
* 🗑️ Remover tarefas individualmente
* 🔥 Remover todas as tarefas de uma vez
* 💾 Salvamento automático em arquivo local
* 📂 Carregamento automático das tarefas ao iniciar o programa
* 🌙 Interface moderna com tema escuro
* 📜 Lista de tarefas com rolagem

---

## 📷 Interface

A aplicação possui:

* Campo para adicionar tarefas
* Botão de adicionar tarefa
* Botão para apagar todas as tarefas
* Lista de tarefas rolável
* Indicador de status para operações de salvamento

---

## 🛠️ Tecnologias Utilizadas

* Python 3.x
* CustomTkinter
* Tkinter
* Sistema de arquivos local (TXT)

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/todo-list-moderna.git
```

### 2. Acesse a pasta do projeto

```bash
cd todo-list-moderna
```

### 3. Instale as dependências

```bash
pip install customtkinter
```

### 4. Execute o projeto

```bash
python main.py
```

---

## 📁 Estrutura do Projeto

```text
📦 ToDo-List-Moderna
│
├── main.py
├── tarefas.txt
└── README.md
```

### Arquivos

| Arquivo     | Descrição                     |
| ----------- | ----------------------------- |
| main.py     | Código principal da aplicação |
| tarefas.txt | Armazena as tarefas salvas    |
| README.md   | Documentação do projeto       |

---

## 💾 Sistema de Salvamento

Todas as tarefas são armazenadas automaticamente no arquivo:

```text
tarefas.txt
```

Quando o programa é iniciado, as tarefas são carregadas automaticamente.

Tarefas concluídas são identificadas pelo símbolo:

```text
✓ Minha tarefa concluída
```

---

## 🚀 Possíveis Melhorias Futuras

* Editar tarefas existentes
* Categorias de tarefas
* Datas de vencimento
* Prioridades (Alta, Média e Baixa)
* Notificações e lembretes
* Banco de dados SQLite
* Exportação para PDF ou Excel
* Sincronização em nuvem

---

## 👨‍💻 Autor

Desenvolvido por **Ricardo Davi Oliveira da Silva**.

Projeto criado para praticar:

* Programação Orientada a Objetos (POO)
* Desenvolvimento de Interfaces Gráficas
* Manipulação de Arquivos
* Organização de Projetos Python

---

## 📄 Licença

Este projeto é de uso livre para estudos e aprimoramento de conhecimentos em Python.
