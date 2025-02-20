from fasthtml.common import *

from app.models import get_all

def Generar_tabla_Informe():
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
    return(table_div)

def tabla_prueba():
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
    return(table_div)