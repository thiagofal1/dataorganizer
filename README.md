# 📂 Data Organizer | Organizador de Dados

A simple Python script to organize files into categories (Images, Videos, Documents, Music, Others).  
Um script Python simples para organizar arquivos em categorias (Imagens, Vídeos, Documentos, Música, Outros).

---

## 🚀 Features | Funcionalidades
- Automatically organizes files by extension.  
- Avoids overwriting by renaming duplicates.  
- Recursive search in subfolders.  
- Customizable categories.  

---
- Organiza arquivos automaticamente por extensão.  
- Evita sobrescrita renomeando duplicados.  
- Busca recursiva em subpastas.  
- Categorias personalizáveis.  

---

## ⚙️ Requirements | Requisitos
- Python 3.7+

---

## ▶️ Usage | Como usar

### Run in the terminal | Execute no terminal:
```bash
python dataorganizer.py "/path/to/your/folder"
```
---

## 🛠️ Configuration | Configuração

### Edit the dictionary CATEGORIES inside organizer.py to add or remove extensions.

---

### Edite o dicionário CATEGORIES dentro do organizer.py para adicionar ou remover extensões.

```bash
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".avi"],
    "Documents": [".pdf", ".docx"],
    "Music": [".mp3"],
    "Others": []
}
```
## 📄 License | Licença

### This project is under the MIT License.

## Escopo do projeto

O Data Organizer deve ser uma ferramenta simples para Windows que recebe uma pasta de origem e organiza seus arquivos por tipo, sem apagar dados e sem exigir configurações complexas.

### Incluído no escopo atual

- Classificação por extensão em `Images`, `Videos`, `Documents`, `Music` e `Others`.
- Busca recursiva em subpastas.
- Renomeação segura de duplicatas com sufixo numérico.
- Execução por linha de comando.
- Categorias e extensões configuráveis no código.

### Fora do escopo por enquanto

- Sincronização com nuvem.
- Exclusão automática de arquivos.
- Organização baseada no conteúdo semântico.
- Monitoramento contínuo de pastas em segundo plano.

## Melhorias planejadas

Antes de criar o instalável, a prioridade é tornar o script confiável para uso diário:

1. Separar a lógica de organização da interface de linha de comando.
2. Adicionar modo `--dry-run` para simular mudanças sem mover arquivos.
3. Criar logs e um relatório final com arquivos movidos, ignorados e conflitantes.
4. Permitir configurar categorias e extensões por arquivo externo.
5. Validar caminhos, permissões e nomes inválidos no Windows.
6. Adicionar testes automatizados para classificação, duplicatas, subpastas e erros.
7. Definir o comportamento para links simbólicos, arquivos ocultos e extensões desconhecidas.
8. Melhorar a documentação com exemplos reais de uso.

## Próxima etapa: software instalável `.exe`

Depois das melhorias, o projeto deverá gerar um instalável para Windows com:

- executável independente de uma instalação manual do Python;
- interface para selecionar pasta de origem e destino;
- pré-visualização ou modo simulação antes de mover arquivos;
- logs acessíveis para diagnosticar falhas;
- pacote versionado publicado como release no GitHub.

A primeira versão gráfica pode usar uma interface desktop leve e ser empacotada com PyInstaller. A tecnologia definitiva do instalador deve ser decidida depois de validar a experiência da interface.

## Status

**Em definição de escopo e planejamento da próxima versão.** O objetivo é estabilizar a lógica e a experiência de uso antes de distribuir o instalável `.exe`.
### Este projeto está sob a Licença MIT.
