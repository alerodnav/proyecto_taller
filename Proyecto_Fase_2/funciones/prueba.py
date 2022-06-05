import datetime
semanas = [
    {
        'numero': 1,
        'inicio': '07-02',
        'fin': '13-02'
    },
    {
        'numero': 2,
        'inicio': '14-02',
        'fin': '20-02'
    },
    {
        'numero': 3,
        'inicio': '21-02',
        'fin': '27-02'
    },
    {
        'numero': 4,
        'inicio': '28-02',
        'fin': '06-03'
    },
    {
        'numero': 5,
        'inicio': '07-03',
        'fin': '13-03'
    },
    {
        'numero': 6,
        'inicio': '14-03',
        'fin': '20-03'
    },
    {
        'numero': 7,
        'inicio': '21-03',
        'fin': '27-03'
    },
    {
        'numero': 8,
        'inicio': '28-03',
        'fin': '03-04'
    },
    {
        'numero': 9,
        'inicio': '04-04',
        'fin': '10-04'
    },
    {
        'numero': 10,
        'inicio': '18-04',
        'fin': '24-04'
    },
    {
        'numero': 11,
        'inicio': '25-04',
        'fin': '01-05'
    },
    {
        'numero': 12,
        'inicio': '02-05',
        'fin': '08-05'
    },
    {
        'numero': 13,
        'inicio': '09-05',
        'fin': '15-05'
    },
    {
        'numero': 14,
        'inicio': '16-05',
        'fin': '22-05'
    },
    {
        'numero': 15,
        'inicio': '23-05',
        'fin': '29-05'
    },
    {
        'numero': 16,
        'inicio': '30-05',
        'fin': '05-06'
    },
    {
        'numero': 17,
        'inicio': '06-06',
        'fin': '12-06'
    }
]

agendarEvento = []

def ver_hora(h):
    hora = ""
    for i in h:
        if i == ":":
            return int(hora)
        hora=hora+i

def validar(l,ns,d,hi,hf):
    valido1 = False
    valido2 = False
    for i in l:
        if (ns == i['numero_semana']) & (d == i['dia']):
            if ver_hora(hi)==ver_hora(i['hora_inicio']):
                print("Inicia a la misma hora que {0}.".format(i['nombre']))
            if (ver_hora(hi)<ver_hora(i['hora_inicio'])) & (ver_hora(hf)>ver_hora(i['hora_inicio'])):
                print("Debes terminar antes, porque chocaría con el horario de {0}".format(i['nombre']))
            if (ver_hora(hi)>ver_hora(i['hora_inicio'])) & (ver_hora(hf)<ver_hora(i['hora_final'])):
                print("Esta hora no te sirve, te choca con {0}".format(i['nombre']))
            #Creo que ya la validación de hora 
        
def encontrar_semana(fi,ff,s):
    for i in s:
        if ((i['inicio'][-1] == fi[-1]) & (i['inicio'][-2] == fi[-2])) & ((i['fin'][-1] >= ff[-1]) & (i['fin'][-2] == ff[-2])):
            #Validar fecha inicio < fecha fin
            if (fi[0]+fi[1]) < (ff[0]+ff[1]):
                if ((int(i['inicio'][0] + i['inicio'][1])<=(int(fi[0] + fi[1]))) & (i['fin'][-1] > ff[-1])):
                    return i['numero']
                elif(int(i['fin'][0] + i['fin'][1])>=(int(ff[0] + ff[1]))):
                    return i['numero']
    return "Este rango de fechas no existe dentro de una única semana"
    # Me devuelve el numero de la semana (Solo permite una) de la fecha PERO TENGO QUE PROBAR MÁS CASOS
                
# print(encontrar_semana('20-04','29-04',semanas))

opcion = input("Para salir seleccione 2")
while opcion != "2":
    evento = input("Evento ")
    fecha_inicio = input("Fecha Inicio")
    fecha_final = input("Fecha Final")
    dia = input("Dia ")
    h_inicio = input("Hora inicio ")
    h_final = input ("Hora final ")
    num_semana = encontrar_semana(fecha_inicio,fecha_final,semanas)
    validar(agendarEvento,num_semana,dia,h_inicio,h_final)
    agendarEvento.append(
    {
    'nombre': evento,
    'numero_semana': num_semana,
    'dia': dia,
    'hora_inicio': h_inicio,
    'hora_final': h_final 
    }
    )
    print(agendarEvento)

    opcion = input("Para salir seleccione 2")
