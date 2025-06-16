# PDFtoMD-Converter
Servidor MCP que convierte archivos PDF a formato Markdown (MD).

## Requisitos

Para usar este servidor MCP necesitas tener instalado:

```bash
pip install pdfplumber markdownify mcp-server
```

## Uso

### Ejecutar el servidor

Para iniciar el servidor MCP, ejecuta:

```bash
python main.py
```

Esto lanzará el servidor usando transporte stdio, que es compatible con múltiples clientes MCP.


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

- GitHub Copilot
- Azure OpenAI Service
- Visual Studio Code con extensiones compatibles con MCP
