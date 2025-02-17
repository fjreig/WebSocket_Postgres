from fasthtml import FastHTML
from pathlib import Path
from fasthtml.common import *

from app.src import Generar_Informe_Mensual, Generar_Informe_Anual

hdrs = (MarkdownJS(), HighlightJS(langs=['python', 'javascript', 'html', 'css']), )

app, rt = fast_app(hdrs=hdrs)

with open('app/info.md') as f:
    content = f.read()

@rt('/')
def get(req):
    return Titled("Web de infomes de energia", Div(content,cls="marked"))

@app.get("/Infome_Mensual/{year}/{month}")
def informe_mensual(year: int, month: int):
    data = Generar_Informe_Mensual(year, month)
    return(data)

@app.get("/Infome_Anual/{year}")
def informe_anual(year: int):
    data = Generar_Informe_Anual(year)
    return(data)

serve()