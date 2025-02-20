from fasthtml import FastHTML
from pathlib import Path
from fasthtml.common import *

from app.models import Informe_Mensual, InformeAnual
from app.table import Generar_tabla_Informe, tabla_prueba

hdrs = (MarkdownJS(), HighlightJS(langs=['python', 'javascript', 'html', 'css']), )

app, rt = fast_app(hdrs=hdrs, exts='ws')

with open('app/info.md') as f:
    content = f.read()

#@rt('/')
#def get(req):
#    return Titled("Web de infomes de energia", Div(content,cls="marked"))

@rt('/')
def home():
    cts = Div(hx_ext='ws', ws_connect='/ws')(
        Div(id='msg-list'),
        Form(Input(id='msg'), id='form', ws_send=True)
    )
    return Titled('Websocket Test', cts)

async def ws(msg:str):
    if msg == "Informe":
        table_div = Generar_tabla_Informe()
        await send(Container(table_div, id='msg-list'))

send = setup_ws(app, ws)

@rt('/tabla')
def tabla():
    table_div = tabla_prueba()
    return Titled('Table Test', table_div)

@app.get("/Infome_Mensual/{year}/{month}")
def informe_mensual(year: int, month: int):
    data = Informe_Mensual(year, month)
    return(data)

@app.get("/Infome_Anual/{year}")
def informe_anual(year: int):
    data = InformeAnual(year)
    return(data)

serve()