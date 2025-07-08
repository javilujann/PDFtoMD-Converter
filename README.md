# PDFtoMD-Converter
[![smithery badge](https://smithery.ai/badge/@javilujann/pdftomd-converter)](https://smithery.ai/server/@javilujann/pdftomd-converter)

Servidor MCP que convierte archivos PDF a formato Markdown (MD).

## Requisitos

Para usar este servidor MCP necesitas instalar las depedencias necesarias. Puedes hacerlo ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

## Uso

### Ejecutar el servidor

El servidor se necesita ejecutar en local para acceder a los archivos, por lo que esta pensado para usarse mediante el comando *uv* o ejecutarlo directamente con *python*.

Su uso mas sencillo es mediante un cliente MCP compatible, como puede ser Visual Studio Code o Cherry Studio.



La configuración que se necesita para usarlo en VSCode es la siguiente: 

```json
{
    "servers": {
        "PDF-Md-Converter-server": {
            "type": "stdio",
            "command": "python",
            "args": ["${workspaceFolder}/main.py"],
            "env": {}
        },
    }
}
```

Mientras que para usarlo con Cherry Studio, la configuración es la siguiente:

```txt
Type: Standard Input/Output(stdio)
Command: uv
Args: 
    --directory
    {path_to_your_workspace}
    run
    main.py
```

### Funcionalidad

El servidor proporciona la herramienta `pdf_to_markdown` con la siguiente firma:

```python
def pdf_to_markdown(input_path: str, output_path: str = None) -> str:
    """
    Convierte un PDF a texto Markdown.

    :param input_path: Ruta al archivo PDF.
    :param output_path: Ruta opcional para guardar el archivo Markdown.
    :return: Cadena con contenido en Markdown.
    """
```

## Integración con clientes MCP

Este servidor es compatible con cualquier cliente que implemente el protocolo MCP (Model Context Protocol), incluyendo:

- Visual Studio Code con extensiones compatibles con MCP
- Cherry Studio
