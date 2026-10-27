# Aplicação com Streamlit

1) Aplicação separada nas camadas Modelo, Servico e Visao
2) Código dentro da pasta *src*
3) Operações de inserir e listar

## Arquitetura

O diagrama PlantUML da aplicação está em [arquitetura.puml](./arquitetura.puml).
O arquivo pode ser aberto ou colado no PlantText para visualizar a arquitetura.

## Como executar

No diretório deste projeto, execute:

```bash
uv run streamlit run src/Inicio.py
```

O `uv` instala e gerencia as dependências definidas em `pyproject.toml`. Depois que o servidor iniciar, acesse o endereço exibido no terminal - normalmente `http://localhost:8501`.
