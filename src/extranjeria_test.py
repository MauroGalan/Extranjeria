from extranjeria import *

if __name__ == "__main__":
    #print(f"Se leyeron {len(lee_datos_extranjeria("data/extranjeriaSevilla.csv"))} registros")
    #print(f"Hay {numero_nacionalidades_distintas(lee_datos_extranjeria("data/extranjeriaSevilla.csv"))} nacionalidades distintas")
    #print(f"Hay {len(secciones_distritos_con_extranjeros_nacionalidades((lee_datos_extranjeria("data/extranjeriaSevilla.csv")),{"ALEMANIA","ITALIA"}))} secciones de distritos con residentes cuya procedencia es ALEMANIA o ITALIA. Mostrando 3 secciones:{secciones_distritos_con_extranjeros_nacionalidades(lee_datos_extranjeria("data/extranjeriaSevilla.csv"),{"ALEMANIA","ITALIA"})[:3]}")
    #print(f"Mostrando el número de residentes para algunos países de procedencia: {total_extranjeros_por_pais(lee_datos_extranjeria("data/extranjeriaSevilla.csv"))["ALEMANIA"]} de Alemania")
    #print(f"Mostrando los top 5{top_n_extranjeria(lee_datos_extranjeria("data/extranjeriaSevilla.csv"),5)}")
    #print(f"El barrio con más nacionalidades distintas es {barrio_mas_multicultural(lee_datos_extranjeria("data/extranjeriaSevilla.csv"))}")
    print(f"EL barrio con más extranjeros hombres es {barrio_con_mas_extranjeros(lee_datos_extranjeria("data/extranjeriaSevilla.csv"),"Hombres")}")
    print(f"El país más representado por cada distrito es: {pais_mas_representado_por_distrito(lee_datos_extranjeria("data/extranjeriaSevilla.csv"))}")