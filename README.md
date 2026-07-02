# Conversor de Áudio para MP3

Um script simples em Python para converter diversos formatos de áudio (como `.opus`, `.aac`, `.m4a`, `.wav`, etc.) para o formato `.mp3` utilizando a biblioteca `moviepy`.

## Tecnologias Utilizadas
- Python 3
- [MoviePy](https://zulko.github.io/moviepy/) (para manipulação e conversão de áudio)

## Como Usar

1. **Clone o repositório ou baixe os arquivos.**
2. **Instale o `uv`** (caso ainda não tenha instalado):
   Siga as instruções oficiais em [docs.astral.sh/uv](https://docs.astral.sh/uv/).
3. **Sincronize as dependências e o ambiente virtual:**
   Na raiz do projeto, execute o comando abaixo para que o `uv` crie automaticamente o ambiente `.venv` e instale as dependências listadas no `pyproject.toml`:
   ```bash
   uv sync
   ```
   *(Nota: no Windows, caso ocorram erros de permissão "arquivo não encontrado", adicione a flag `--link-mode copy` ao comando)*

4. **Execute o script:**
   Abra o arquivo `main.py`, altere o nome do arquivo na linha `converter_para_mp3("seu_arquivo.extensao")` no final do script para o áudio que você deseja converter. Depois, execute o script usando o `uv`:
   ```bash
   uv run main.py
   ```

## Funcionalidades
- Converte vários formatos suportados pelo `ffmpeg` em `.mp3`.
- Usa codificação com qualidade variável (VBR) para um ótimo equilíbrio entre tamanho e qualidade do arquivo de saída.


