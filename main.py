from mcp.server.fastmcp import FastMCP
import pdfplumber
import markdownify

app = FastMCP("Pdf-To-Md-server", dependencies=["pdfplumber", "markdownify"])

@app.tool()
def pdf_to_markdown(input_path: str) -> str:
    """
    Convierte un PDF a texto Markdown.

    :param input_path: Ruta al archivo PDF.
    :return: Cadena con contenido en Markdown.
    """
    md_blocks = []
    with pdfplumber.open(input_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            md = markdownify.markdownify(text, heading_style="ATX")
            md_blocks.append(md)
    return "\n\n".join(md_blocks)


if __name__ == "__main__":
    app.run(transport="stdio")