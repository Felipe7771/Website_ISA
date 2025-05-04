# AI de coleta da HORA
# transformar tudo isso em uma função que possa ser chamada

# !!!
# Se a estrutura da pesquisa se mantiver a mesma, a coleta
# dos dados vei ocorrer conforme o esperado
from datetime import datetime, date
import checkNik as check

def Ai_hour(command):

        # PODE RETORNAR:
        # Horário
        # Dia
        # Dia da semana

        #Coleta do ANO/MES/DIA
        data = date.today()
        year = data.year
        month = data.month
        day = data.day

        #Coleta da HORA/MINUTOS
        clock = datetime.now()
        hour = clock.hour
        minutes = clock.minute


        weekdays = ["Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"]
        meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
        month = meses[month]
        #Dia da Semana
        week = clock.weekday()

        day_week = weekdays[week]

        response = ""

        # busca pelas horas
        if check.check_name(command,['horas','hora']):
                response = response + f'O horário atual é {hour} horas e {minutes} minutos.'
        
        # busca pelo dia da semana
        if check.check_name(command,['dia da semana']):
                response = response + f'Hoje é {day_week}.'
        
        # busca pelo dia/mes/ano tal que não foi introduzido as palavras mes e ano
        if 'dia' in command and ('mes' not in command or 'ano' not in command):
                response = response + f'Hoje é dia {day} de {month} de {year}.'
        
        # caso tenha a palavra dia junto com mes ou ano, ele só retorna o dia
        if 'dia' in command and ('mes' in command or 'ano' in command):
                response = response + f'Hoje é dia {day}.'

        # busca pelo mes    
        if 'mes' in command:
               response = response + f'O mês de hoje é {month}.'
        
        # busca pelo ano
        if 'ano' in command:
                response = response + f'O ano atual é {year}.'
        
        # retorna o conjunto de infromações pedidas
        return response
                


