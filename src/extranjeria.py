import csv
from typing import NamedTuple

RegistroExtranjeria = NamedTuple("RegistroExtranjeria", [("distrito",str),("seccion",str),("barrio",str),("pais",str),("hombres",int),("mujeres",int)])

def lee_datos_extranjeria(ruta_fichero): 
    """
    Recibe la ruta del fichero CSV, devolviendo una lista de tuplas de tipo RegistroExtranjeria con 
    toda la información contenida en el fichero.
    """
    res = []
    with open (ruta_fichero,encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for d,s,b,p,h,m in lector:
            hombres = int(h)
            mujeres = int(m)
            res.append(RegistroExtranjeria(d,s,b,p,hombres,mujeres))
    return res


def numero_nacionalidades_distintas(registros: list[RegistroExtranjeria])-> int: 
    ''' 
    Recibe una lista de tuplas de tipo RegistroExtranjeria y 
    devuelve el número de nacionalidades distintas presentes en 
    los registros de la lista recibida como parámetro.
    '''
    nacional= set()
    for registro in registros:
        nacional.add(registro.pais)
    return len(nacional)


def secciones_distritos_con_extranjeros_nacionalidades(
        registros:list[RegistroExtranjeria], paises:set[str]) -> tuple[str,str]:
    '''
    Recibe una lista de tuplas de tipo RegistroExtranjeria y un conjunto
    de cadenas con nombres de países, y devuelve una lista de tuplas 
    (distrito, seccion) con los distritos y secciones en los que hay 
    extranjeros del conjunto de paises dado como parámetro. La lista 
    de tuplas devuelta estará ordenada por distrito.
    '''
    res=set()
    for registro in registros:
        if registro.pais in paises:
            res.add((registro.distrito,registro.seccion))
    return sorted(res)


def total_extranjeros_por_pais(registros:list[RegistroExtranjeria])->dict[str,int]: 
    '''
    Recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve 
    un diccionario de tipo {str:int} en el que las claves son los países
    y los valores son el número total de extranjeros (tanto hombres 
    como mujeres) de cada país.
    '''
    res = {}
    for registro in registros:
        if registro.pais not in res:
            res[registro.pais]=registro.hombres + registro.mujeres
        else:
            res[registro.pais]+=registro.hombres + registro.mujeres
    return res


def top_n_extranjeria(registros:list[RegistroExtranjeria], n:int=3)->list[tuple[str,int]]: 
    """
    Recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve una lista de tuplas (pais, numero_extranjeros) 
    con los n países de los que hay más población extranjera en los registros pasados como parámetros.
    """
    num_extranjeros_por_pais = total_extranjeros_por_pais(registros)
    #num_extranjeros_por_pais.items()
    return sorted(num_extranjeros_por_pais.items(),key=lambda registro:registro[1],reverse=True)[:n]
    lista=[]
    for registro in registros:
        lista.append((registro.pais,(registro.hombres+registro.mujeres)))
    return sorted(lista,key=lambda registro:registro[1])


def barrio_mas_multicultural(registros:list[RegistroExtranjeria])->str: 
    """
    Recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve el nombre del barrio en el que hay un mayor número 
    de países de procedencia distintos.
    """
    res={}
    for registro in registros:
        if registro.barrio not in res:
            res[registro.barrio]=1
        else:
            res[registro.barrio]+=1
    return max(res.items(),key=lambda registro:registro[1])[0]

def barrio_mas_multicultural_bien_(registros:list[RegistroExtranjeria])->str: 
    """
    Recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve el nombre del barrio en el que hay un mayor número 
    de países de procedencia distintos.
    """
    res={}
    for registro in registros:
        if registro.distrito not in res:
            res[registro.distrito]={registro.pais}
        else:
            res[registro.distrito].add(registro.pais)
    return max(res.items(),key= lambda registro:len(registro[1]))[0]

def barrio_con_mas_extranjeros(registros:list[RegistroExtranjeria], tipo:str=None)->str: 
    """
    Recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve el nombre del barrio en el que hay 
    un mayor número de extranjeros, bien sea en total (tanto hombres como mujeres) si tipo tiene el valor None, 
    bien sea de hombres si tipo es 'Hombres', o de mujeres si tipo es 'Mujeres'.
    """
    res={}
    for registro in registros:
        if registro.barrio not in res:
            if tipo == "Hombres":
                res[registro.barrio]=registro.hombres
            elif tipo == "Mujeres":
                res[registro.barrio]=registro.mujeres
            else:
                res[registro.barrio]=registro.hombres+registro.mujeres
        else:
            if tipo == "Hombres":
                res[registro.barrio]+=registro.hombres
            elif tipo == "Mujeres":
                res[registro.barrio]+=registro.mujeres
            else:
                res[registro.barrio]+=registro.hombres+registro.mujeres
    return max(res.items(),key=lambda registro:registro[1])[0]


def pais_mas_representado_por_distrito(registros:list[RegistroExtranjeria])->dict[str,str]: 
    """
    Recibe una lista de tuplas de tipo RegistroExtranjeria y devuelve un diccionario de tipo {str:str} 
    en el que las claves son los distritos y los valores los países de los que hay más extranjeros residentes 
    en cada distrito.
    """
    res={}
    for registro in registros:
        if registro.distrito not in res:
            res[registro.distrito]={registro.pais}
        else:
            res[registro.distrito].add(registro.pais)
    return res