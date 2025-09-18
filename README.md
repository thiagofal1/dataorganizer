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
### Este projeto está sob a Licença MIT.
