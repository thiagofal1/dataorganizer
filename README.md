# DataOrganizer

Um organizador de arquivos em Python que separa os arquivos de uma pasta em
subpastas de acordo com a extensão.

## Recursos

- Classifica imagens, vídeos, documentos e músicas.
- Envia extensões não reconhecidas para a pasta `Others`.
- Evita sobrescrever arquivos: em caso de conflito, adiciona um sufixo numérico
  ao nome, como `relatorio_1.pdf`.
- Exibe o progresso no terminal e oferece logs detalhados com `--verbose`.

## Requisitos

- Python 3.9 ou superior.

O projeto usa somente a biblioteca padrão do Python, portanto não requer a
instalação de pacotes adicionais.

## Como usar

No terminal, entre na pasta do projeto e informe a pasta que deseja organizar:

```bash
python dataorganizer.py "C:\\caminho\\para\\sua\\pasta"
```

Para acompanhar informações mais detalhadas durante a execução:

```bash
python dataorganizer.py "C:\\caminho\\para\\sua\\pasta" --verbose
```

## Categorias

| Pasta criada | Extensões |
| --- | --- |
| `Images` | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff` |
| `Videos` | `.mp4`, `.avi`, `.mov`, `.mkv`, `.wmv` |
| `Documents` | `.pdf`, `.doc`, `.docx`, `.txt`, `.xlsx`, `.ppt`, `.pptx` |
| `Music` | `.mp3`, `.wav`, `.flac`, `.aac` |
| `Others` | Todas as demais extensões |

## Atenção

O script move arquivos de verdade. Antes de executá-lo em uma pasta importante,
faça um backup ou teste primeiro com uma cópia dos arquivos.

As subpastas de categoria são criadas dentro da pasta informada. Arquivos que
já estiverem na categoria correta não são movidos novamente.
