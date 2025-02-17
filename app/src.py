import psycopg2
import psycopg2.extras

from app.config import postgres_config

def Generar_Informe_Mensual(year, month):
    conn = None
    try:
        params = postgres_config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        sql_stmt = f"""SELECT cast(EXTRACT(Day FROM fecha) as varchar) as Day,
            max(ea_import)-min(ea_import) as ea_import
            FROM aarr
            where EXTRACT(MONTH FROM fecha) = {month} and EXTRACT(YEAR FROM fecha) = {year}
            group by Day
            order by Day;"""
        cur.execute(sql_stmt)
        results = cur.fetchall()
        cur.close()
        conn.close()
        return {"data": results}
    except (Exception, psycopg2.DatabaseError) as error:
        if conn is not None:
            conn.close()
        return {"error": str(error)}
    finally:
        if conn is not None:
            conn.close()

def Generar_Informe_Anual(year):
    conn = None
    try:
        params = postgres_config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        sql_stmt = f"""SELECT cast(EXTRACT(MONTH FROM fecha) as varchar) as Month,
            max(ea_import)-min(ea_import) as ea_import
            FROM aarr
            where EXTRACT(YEAR FROM fecha) = {year}
            group by Month
            order by Month;"""
        cur.execute(sql_stmt)
        results = cur.fetchall()
        cur.close()
        conn.close()
        return {"data": results}
    except (Exception, psycopg2.DatabaseError) as error:
        if conn is not None:
            conn.close()
        return {"error": str(error)}
    finally:
        if conn is not None:
            conn.close()