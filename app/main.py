from fasthtml import FastHTML
from pathlib import Path
from fasthtml.common import *

from fh_altair import altair_headers
from monsterui.all import *

from app.models import Informe_Mensual, InformeAnual
from app.table import Generar_tabla_Informe, tabla_prueba
from app.graficos import generate_chart1, generate_chart2

from app.lista import page_heading, tasks_ui, CreateTaskModal

hdrs = (MarkdownJS(), HighlightJS(langs=['python', 'javascript', 'html', 'css']), altair_headers, Theme.blue.headers())

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

def StatCard(title, value, color='primary'):
    "A card with a statistics.  Since there is no row/col span class it will take up 1 slot"
    return Card(P(title, cls=TextPresets.muted_sm), H3(value, cls=f'text-{color}'),)

stats = [StatCard(*data) for data in [
                ("Total Users", "1,234",   "blue-600"),
                ("Active Now",  "342",     "green-600"),
                ("Revenue",     "$45,678", "purple-600"),
                ("Conversion",  "2.4%",    "amber-600")]]

def ChartCard(title): 
    "A card for a chart.  col-span-2 means it will take up 2 columns"
    return Div(cls="col-span-2")( 
        Card(H3(title),Div("Chart Goes Here", cls="h-64 uk-background-muted")))
chart_cards = [ChartCard(title) for title in ("Monthly Revenue", "User Growth")]


sidebar = Form(
    H3("SideBar"),
    LabelRange("Range For Filters", min=0, max=100),
    LabelInput("A search Bar"),
    LabelSelect(map(Option, ["Product Line A", "Product Line B", "Product Line C", "Product Line D"]),
                     label="Choose Product Line"),
    LabelCheckboxX("Include Inactive Users"),
    LabelCheckboxX("Include Users without order"),
    LabelCheckboxX("Include Users without email"),
    # This sidebar will take up 2 rows b/c of row-span-2
    cls='row-span-2 space-y-5'
)

@rt('/chart')
def index():
    grafico1 = generate_chart1()
    grafico2 = generate_chart2()
    return Titled('Table Test', #grafico1
            Div(
                Div(grafico1), 
                Div(grafico2), 
                cls="grid",
            ),
            Container(Grid(sidebar, *stats, *chart_cards, cols=5))
    )

@rt('/lista')
def index():
    return Container(page_heading, tasks_ui, CreateTaskModal())

@app.get("/Infome_Mensual/{year}/{month}")
def informe_mensual(year: int, month: int):
    data = Informe_Mensual(year, month)
    return(data)

@app.get("/Infome_Anual/{year}")
def informe_anual(year: int):
    data = InformeAnual(year)
    return(data)

serve()