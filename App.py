import customtkinter as ctk
from tkinter import messagebox
import os   

# Configurações globais de aparência
ctk.set_appearance_mode("Dark")  # Modos: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas: "blue" (standard), "green", "dark-blue"

class ToDoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.title("To-Do List Moderna")
        self.geometry("550x475")
        
        # Arquivo de salvamento
        self.arquivo_tarefas = "tarefas.txt"

        # --- Estrutura da UI ---
        
        # Título
        self.label_titulo = ctk.CTkLabel(self, text="Minhas Tarefas", font=("Segoe UI", 20, "bold"))
        self.label_titulo.pack(pady=(20, 10))

        # Frame superior para entrada e botões principais
        self.frame_topo = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_topo.pack(pady=10, padx=20, fill="x")

        self.entry_tarefa = ctk.CTkEntry(self.frame_topo, placeholder_text="Nova tarefa...", width=250)
        self.entry_tarefa.pack(side="left", padx=(0, 10))

        self.btn_adicionar = ctk.CTkButton(self.frame_topo, text="Adicionar", width=100, 
                                           command=self.adicionar_tarefa, fg_color="#4CAF50", hover_color="#45a049")
        self.btn_adicionar.pack(side="left", padx=5)

        self.btn_remover_tudo = ctk.CTkButton(self.frame_topo, text="Remover Tudo", width=100,
                                              command=self.remover_todas_tarefas, fg_color="#e74c3c", hover_color="#c0392b")
        self.btn_remover_tudo.pack(side="left", padx=5)

        # Container Principal para as tarefas (Scrollable)
        # Substitui o Listbox + Scrollbar antigo
        self.frame_tarefas = ctk.CTkScrollableFrame(self, width=500, height=250, label_text="Lista de Tarefas")
        self.frame_tarefas.pack(pady=20, padx=20, fill="both", expand=True)

        # Label de status (salvo/erro)
        self.status_label = ctk.CTkLabel(self, text="", text_color="#4CAF50", font=("Arial", 12))
        self.status_label.pack(pady=(0, 10))

        # Lista para armazenar as referências dos widgets de tarefas
        self.widgets_tarefas = []

        # Carregar tarefas existentes ao iniciar
        self.carregar_tarefas()

    # --- Funções de Lógica ---

    def mostrar_status(self, mensagem, cor="#4CAF50"):
        self.status_label.configure(text=mensagem, text_color=cor)
        self.after(2000, lambda: self.status_label.configure(text=""))

    def adicionar_tarefa(self):
        texto = self.entry_tarefa.get()
        if texto:
            self.criar_widget_tarefa(texto)
            self.entry_tarefa.delete(0, "end")
            self.salvar_tarefas()
        else:
            messagebox.showwarning("Aviso", "Digite uma tarefa para adicionar.")

    def criar_widget_tarefa(self, texto, concluida=False):
        # Frame individual para cada tarefa
        frame_item = ctk.CTkFrame(self.frame_tarefas, fg_color=("#f0f0f0", "#2b2b2b"), corner_radius=5)
        frame_item.pack(fill="x", pady=2, padx=5)

        # Label com o texto da tarefa
        label_tarefa = ctk.CTkLabel(frame_item, text=texto, font=("Segoe UI", 13), anchor="w")
        label_tarefa.pack(side="left", padx=10, pady=5, fill="x", expand=True)

        if concluida or texto.startswith("✓ "):
            label_tarefa.configure(text_color="green")

        # Botão Marcar/Desmarcar Concluída (Checkmark)
        btn_check = ctk.CTkButton(frame_item, text="✔️", width=30, height=30, fg_color="transparent", 
                                  text_color=("#333333", "white"), hover_color=("#e0e0e0", "#3a3a3a"),
                                  command=lambda: self.alternar_conclusao(label_tarefa))
        btn_check.pack(side="right", padx=2)

        # Botão Remover (Lixeira)
        btn_del = ctk.CTkButton(frame_item, text="🗑️", width=30, height=30, fg_color="transparent",
                                text_color="#e74c3c", hover_color=("#feebea", "#4a2522"),
                                command=lambda: self.remover_tarefa_especifica(frame_item))
        btn_del.pack(side="right", padx=(2, 5))

        # Guarda a referência para salvar depois
        self.widgets_tarefas.append({"frame": frame_item, "label": label_tarefa})

    def alternar_conclusao(self, label_widget):
        texto_atual = label_widget.cget("text")
        
        if texto_atual.startswith("✓ "):
            # Desmarcar
            label_widget.configure(text=texto_atual[2:], text_color=("#333333", "white"))
        else:
            # Marcar como concluída
            label_widget.configure(text="✓ " + texto_atual, text_color="green")
        
        self.salvar_tarefas()

    def remover_tarefa_especifica(self, frame_widget):
        # Encontra e remove da lista de referências
        for i, item in enumerate(self.widgets_tarefas):
            if item["frame"] == frame_widget:
                self.widgets_tarefas.pop(i)
                break
        
        # Remove o widget da tela
        frame_widget.destroy()
        self.salvar_tarefas()

    def remover_todas_tarefas(self):
        if self.widgets_tarefas and messagebox.askyesno("Confirmar", "Deseja apagar TODAS as tarefas?"):
            for item in self.widgets_tarefas:
                item["frame"].destroy()
            self.widgets_tarefas = []
            self.salvar_tarefas()

    def salvar_tarefas(self):
        tarefas_para_salvar = []
        for item in self.widgets_tarefas:
            tarefas_para_salvar.append(item["label"].cget("text"))
        
        try:
            with open(self.arquivo_tarefas, "w", encoding="utf-8") as file:
                for tarefa in tarefas_para_salvar:
                    file.write(tarefa + "\n")
            self.mostrar_status("Tarefas salvas ✔")
        except Exception as e:
            self.mostrar_status(f"Erro ao salvar: {e}", cor="red")

    def carregar_tarefas(self):
        if not os.path.exists(self.arquivo_tarefas):
            return

        try:
            with open(self.arquivo_tarefas, "r", encoding="utf-8") as file:
                tarefas = file.readlines()
                for tarefa in tarefas:
                    texto = tarefa.strip()
                    if texto:
                        # Criar o widget e definir a cor se já estiver concluída
                        concluida = texto.startswith("✓ ")
                        self.criar_widget_tarefa(texto, concluida=concluida)
        except Exception as e:
            self.mostrar_status(f"Erro ao carregar: {e}", cor="red")

if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()