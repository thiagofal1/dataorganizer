📂 dataorganizer
Um script Python simples e inteligente para organizar arquivos de forma automática, movendo-os para pastas categorizadas.

A simple yet smart Python script to automatically organize files by moving them into categorized folders.

✨ Sobre o Projeto / About the Project
O dataorganizer é a ferramenta perfeita para quem precisa colocar a casa em ordem. Ele escaneia uma pasta e categoriza todos os arquivos (imagens, vídeos, documentos, músicas e outros) em subpastas correspondentes.

Recursos Principais:

Organização Automática: Movimenta arquivos de forma inteligente com base na extensão.

Segurança: Evita a sobrescrita de arquivos com o mesmo nome, adicionando um sufixo numérico (arquivo_1.txt, arquivo_2.txt).

Simples de Usar: Funciona a partir da linha de comando, sem necessidade de configuração complexa.

dataorganizer is the perfect tool for anyone who needs to tidy up their folders. It scans a directory and categorizes all files (images, videos, documents, music, and others) into corresponding subfolders.

Key Features:

Automatic Organization: Moves files intelligently based on their extensions.

Safety: Prevents file overwrites by adding a numerical suffix (file_1.txt, file_2.txt) to duplicate filenames.

Simple to Use: Works directly from the command line, no complex configuration needed.

🚀 Como Usar / How to Use
Pré-requisitos / Prerequisites
Para rodar este script, você precisa ter o Python 3 instalado na sua máquina.

To run this script, you need to have Python 3 installed on your machine.

Execução / Execution
Basta executar o script a partir do terminal, passando o caminho da pasta que você deseja organizar.

Just run the script from the terminal, providing the path to the folder you want to organize.

Bash

python dataorganizer.py "/caminho/da/sua/pasta"
Exemplo / Example:
Se o seu código estiver na pasta ~/scripts/ e você quiser organizar a pasta ~/downloads/, o comando seria:
If your code is in the ~/scripts/ folder and you want to organize the ~/downloads/ folder, the command would be:

Bash

python ~/scripts/dataorganizer.py ~/downloads/
Modo Verbose / Verbose Mode
Para ver detalhes do processo, como quais arquivos estão sendo movidos e se já estão na pasta correta, use a flag -v ou --verbose:

To see detailed process logs, such as which files are being moved and if they are already in the correct folder, use the -v or --verbose flag:

Bash

python dataorganizer.py "/caminho/da/sua/pasta" -v
📝 Exemplo de Uso / Usage Example
Imagine que a sua pasta de downloads esteja assim:

Imagine your downloads folder looks like this:

Antes da organização / Before organization:

/downloads/
├── relatório_mensal.pdf
├── video_ferias.mp4
├── foto_aniversario.jpg
├── apresentação_projeto.pptx
└── música_favorita.mp3
Depois de rodar o script / After running the script:

/downloads/
├── Documents/
│   ├── relatório_mensal.pdf
│   └── apresentação_projeto.pptx
├── Images/
│   └── foto_aniversario.jpg
├── Videos/
│   └── video_ferias.mp4
└── Music/
    └── música_favorita.mp3
🤝 Contribuições / Contributions
Sinta-se à vontade para sugerir melhorias, adicionar novas categorias de arquivos ou relatar bugs. Você pode abrir uma issue ou enviar um pull request no repositório.

Feel free to suggest improvements, add new file categories, or report bugs. You can open an issue or submit a pull request to the repository.

⚖️ Licença / License
Este projeto está licenciado sob a Licença MIT.

This project is licensed under the MIT License.
