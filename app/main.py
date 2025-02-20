from fasthtml import FastHTML
from pathlib import Path
from fasthtml.common import *
import json

from app.src import Generar_Informe_Mensual, Generar_Informe_Anual
from app.models import get_all, Informe_Mensual, InformeAnual

hdrs = (MarkdownJS(), HighlightJS(langs=['python', 'javascript', 'html', 'css']), )

app, rt = fast_app(hdrs=hdrs, exts='ws')

with open('app/info.md') as f:
    content = f.read()

#@rt('/')
#def get(req):
#    return Titled("Web de infomes de energia", Div(content,cls="marked"))

msgs = []
@rt('/')
def home():
    cts = Div(hx_ext='ws', ws_connect='/ws')(
        Div(id='msg-list'),
        Form(Input(id='msg'), id='form', ws_send=True)
    )
    return Titled('Websocket Test', cts)

async def ws(msg:str):
    if msg == "Informe":
        data = get_all()
        table_div = Main(
            Table(
                Thead(
                    Tr(  
                        Th("Fecha", scope="col"),
                        Th("V1", scope="col"),
                        Th("V2", scope="col"),
                        Th("V3", scope="col"),
                        Th("PA", scope="col"),
                    ),  
                ),  
                Tbody(  
                    Tr(
                        Td(valor.fecha, form="create-form"),
                        Td(valor.v1, form="create-form"),
                        Td(valor.v2, form="create-form"),
                        Td(valor.v3, form="create-form"),
                        Td(valor.pa, form="create-form"),
                        id=f"aarr-{valor.id}"
                )  for valor in data),
            ),
        )
        await send(Container(table_div, id='msg-list'))

send = setup_ws(app, ws)

@rt('/tabla')
def tabla():
    table_div = Table(  
            Thead(  
                Tr(  
                    Th("ID", scope="col"),  
                    Th("Name", scope="col"),  
                    Th("Address", scope="col"),  
                    Th("Email", scope="col"),  
                    Th("Action", scope="col")  
                ),  
            ),  
            Tbody(  
                Tr(  
                    Td(23),  
                    Td(34),  
                    Td(34),  
                    Td(34),  
                    Td(Button("Delete")),   
                ),
                Tr(  
                    Td(23),  
                    Td(34),  
                    Td(34),  
                    Td(34),  
                    Td(Button("Delete")),   
                )
            )  
        )
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