import time
from datetime import datetime
from PySimpleGUI import PySimpleGUI as sg

def inicio(): ### Tela inicial do programa
    layoutInicio = [ #Layout da tela inicial
        [sg.Image(r'Tela_inicial.png')],
        [sg.Button('Fazer registro',button_color=('White','Red')),sg.Button('Sair',button_color=('White','Red'))]
                    ]

    windowInicio = sg.Window('LabEHGames - Registro AC: Brotherhood (Beta 2.0) by João Gabriel', layoutInicio) #Inicia a janela do windows com o layout específico

    while True:
        event, values = windowInicio.read() ## Lê os eventos da janela 
        if event == sg.WIN_CLOSED or event == 'Sair':
            windowInicio.close()
            quit()
        if event == 'Fazer registro':
            windowInicio.close()
            break
    
def erro(txt): ### Faz aparecer uma tela de erro
    layoutError = [
        [sg.Text(txt)],
        [sg.Button('Ok')],
        ]
             
    windowErro = sg.Window('Erro!', layoutError)
    
    while True:
        event, values = windowErro.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            windowErro.close()
            break
        
#Base de dados
seq_1 = {'Nome':'1 - Peace At Last', 'seq1-1':'1- Mass Exodus', 'seq1-2':'2- R & R', 'seq1-3':'3- Horsing Around',
         'seq1-4':'4- Target Practice','seq1-5':'5- Reunion', 'seq1-6':'6- Vilified', 'seq1-7':'7- Emergency Exit'}
keys_seq_1 = []
for i in seq_1:
    keys_seq_1.append(i)

seq_2 = {'Nome':'2 - The Wildernes of Tigers', 'seq2-1':'1- Desmond Miles, Present Day', 'seq2-2':'2- As Good as New', 'seq2-3':'3- Well Executed',
         'seq2-4':'4- New Man in Town', 'seq2-5':'5- Easy Come, Easy Go', 'seq2-6':"6- Who's Got Mail ", 'seq2-7':'7- Crepi Il Lupo',
         'seq2-8':'8- The Halls of Nero', 'seq2-9':'9- Roman Underground'}
keys_seq_2 = []
for i in seq_2:
    keys_seq_2.append(i)

seq_3 = {'Nome':'3 - The Fighter, The Lover And The Thief', 'seq3-1':'1- Double Agent', 'seq3-2':'2- Between a Rock and a Hard Place',
         'seq3-3':'3- High-Stakes Negotiation', 'seq3-4':'4- Collective Intelligence'}
keys_seq_3 = []
for i in seq_3:
    keys_seq_3.append(i)

seq_4 = {'Nome':'4 - Den Of Thieves', 'seq4-1':'1- Castello Crasher', 'seq4-2':'2- Femme Fatale', 'seq4-3':'3- The Burdens We Carry',
         'seq4-4':'4- Guardian of Forli', 'seq4-5':'5- Man of the People', 'seq4-6':'6- Serial Offender', 'seq4-7':'7- Human Cargo',
         'seq4-8':'8- An Unexpected Visitor', 'seq4-9':'9- War Plans', 'seq4-10':'10- Outgunned', 'seq4-11':'11- The Plan'}
keys_seq_4 = []
for i in seq_4:
    keys_seq_4.append(i)

seq_5 = {'Nome':'5 - The Banker', 'seq5-1':'1- Escape from Debt', 'seq5-2':'2- Follow the Money', 'seq5-3':'3- When in Rome',
         'seq5-4':'4- In and Out', 'seq5-5':'5- Paper Trail'}
keys_seq_5 = []
for i in seq_5:
    keys_seq_5.append(i)

seq_6 = {'Nome':'6 - The Baron De Valois', 'seq6-1':'1- Gatekeeper', 'seq6-2':'2- French Kiss', 'seq6-3':'3- Trojan Horse', 'seq6-4':'4- Au Revoir'}
keys_seq_6 = []
for i in seq_6:
    keys_seq_6.append(i)

seq_7 = {'Nome':'7 - The Key To The Castle', 'seq7-1':'1- Patching the Leak', 'seq7-2':'2- Calling All Stand-ins', 'seq7-3':'3- Exit Stage Right',
         'seq7-4':'4- Intervention', 'seq7-5':'5- Ascension'}
keys_seq_7 = []
for i in seq_7:
    keys_seq_7.append(i)

seq_8 = {'Nome':'8 - ', 'seq8-1':'1- Requiem', 'seq8-2':'2- An Apple a Day', 'seq8-3':'3- The Apple of Eden', 'seq8-4':'4- Demilitarization',
         'seq8-5':'5- Seeing Red', 'seq8-6':'6- All Roads Lead To'}
keys_seq_8 = []
for i in seq_8:
    keys_seq_8.append(i)

seq_9 = {'Nome':'9 - The Fall', 'seq9-1':'1- Pax Romana'}
keys_seq_9 = []
for i in seq_9:
    keys_seq_9.append(i)

seq_list = seq_1['Nome'], seq_2['Nome'], seq_3['Nome'], seq_4['Nome'], seq_5['Nome'], seq_6['Nome'], seq_7['Nome'], seq_8['Nome'], seq_9['Nome']


# TEMA DA JANELA
sg.theme('DarkAmber')

# Janela de inicio
inicio()

#Layouts
layout_seq1 = [
    [sg.Checkbox('1- Mass Exodus',key='seq1-1',size=(25,1)),sg.Checkbox('2- R & R',key='seq1-2',size=(25,1)),sg.Checkbox('3- Horsing Around',key='seq1-3',size=(25,1))],
    [sg.Checkbox('4- Target Practice',key='seq1-4',size=(25,1)),sg.Checkbox('5- Reunion',key='seq1-5',size=(25,1)),sg.Checkbox('6- Vilified',key='seq1-6',size=(25,1))],
    [sg.Checkbox('7- Emergency Exit',key='seq1-7',size=(25,1))],
    ]

layout_seq2 = [
    [sg.Checkbox('1- Desmond Miles, Present Day',key='seq2-1',size=(25,1)),sg.Checkbox('2- As Good as New',key='seq2-2',size=(25,1)),sg.Checkbox('3- Well Executed',key='seq2-3',size=(25,1))],
    [sg.Checkbox('4- New Man in Town',key='seq2-4',size=(25,1)),sg.Checkbox('5- Easy Come, Easy Go',key='seq2-5',size=(25,1)),sg.Checkbox("6- Who's Got Mail",key='seq2-6',size=(25,1))],
    [sg.Checkbox('7- Crepi Il Lupo',key='seq2-7',size=(25,1)),sg.Checkbox('8- The Halls of Nero',key='seq2-8',size=(25,1)),sg.Checkbox('9- Roman Underground',key='seq2-9',size=(25,1))]
    ]

layout_seq3 = [
    [sg.Checkbox('1- Double Agent',key='seq3-1',size=(25,1)),sg.Checkbox('2- Between a Rock and a Hard Place',key='seq3-2',size=(25,1))],
    [sg.Checkbox('3- High-Stakes Negotiation',key='seq3-3',size=(25,1)),sg.Checkbox('4- Collective Intelligence',key='seq3-4',size=(25,1))]
    ]

layout_seq4 = [
    [sg.Checkbox('1- Castello Crasher',key='seq4-1',size=(25,1)),sg.Checkbox('2- Femme Fatale',key='seq4-2',size=(25,1)),sg.Checkbox('3- The Burdens We Carry',key='seq4-3',size=(25,1))],
    [sg.Checkbox('4- Guardian of Forli',key='seq4-4',size=(25,1)),sg.Checkbox('5- Man of the People',key='seq4-5',size=(25,1)),sg.Checkbox('6- Serial Offender',key='seq4-6',size=(25,1))],
    [sg.Checkbox('7- Human Cargo',key='seq4-7',size=(25,1)),sg.Checkbox('8- An Unexpected Visitor',key='seq4-8',size=(25,1)),sg.Checkbox('9- War Plans',key='seq4-9',size=(25,1))],
    [sg.Checkbox('10- Outgunned',key='seq4-10',size=(25,1)),sg.Checkbox('11- The Plan',key='seq4-11',size=(25,1))]
    ]

layout_seq5 = [
    [sg.Checkbox('1- Escape from Debt',key='seq5-1',size=(25,1)),sg.Checkbox('2- Follow the Money',key='seq5-2',size=(25,1)),sg.Checkbox('3- When in Rome',key='seq5-3',size=(25,1))],
    [sg.Checkbox('4- In and Out ',key='seq5-4',size=(25,1)),sg.Checkbox('5- Paper Trai',key='seq5-5',size=(25,1))]
    ]

layout_seq6 = [
    [sg.Checkbox('1- Gatekeeper',key='seq6-1',size=(25,1)),sg.Checkbox('2- French Kiss',key='seq6-2',size=(25,1)),sg.Checkbox('3- Trojan Horse',key='seq6-3',size=(25,1))],
    [sg.Checkbox('4- Au Revoir ',key='seq6-4',size=(25,1))]
    ]

layout_seq7 = [
    [sg.Checkbox('1- Patching the Leak',key='seq7-1',size=(25,1)),sg.Checkbox('2- Calling All Stand-ins',key='seq7-2',size=(25,1)),sg.Checkbox('3- Exit Stage Right',key='seq7-3',size=(25,1))],
    [sg.Checkbox('4- Intervention',key='seq7-4',size=(25,1)),sg.Checkbox('5- Ascension',key='seq7-5',size=(25,1))]
    ]

layout_seq8 = [
    [sg.Checkbox('1- Requiem',key='seq8-1',size=(25,1)),sg.Checkbox('2- An Apple a Day',key='seq8-2',size=(25,1)),sg.Checkbox('3- The Apple of Eden',key='seq8-3',size=(25,1))],
    [sg.Checkbox('4- Demilitarization',key='seq8-4',size=(25,1)),sg.Checkbox('5- Seeing Red',key='seq8-5',size=(25,1)),sg.Checkbox('6- All Roads Lead To',key='seq8-6',size=(25,1))]
    ]

layout_seq9 = [
    [sg.Checkbox('1- Pax Romana',key='seq9-1',size=(25,1))]
    ]

layout1 = [ [sg.Text(45*' '),sg.Text("Registro de atividade Assasin's Creed: Brotherhood\n")],
            [sg.Text(35*' '),sg.Text('Preencha os campos abaixo e confirme para gerar o registro em .TXT\n')],
            [sg.Text('Início da jogatina (HH:MM)'), sg.InputText(size=(5,1),key='hora1'), sg.Text('Fim da jogatina (HH:MM)'), sg.InputText(size=(5,1),key='hora2')],
            [sg.Text('')],
            [sg.Text('Qual sequência foi feita?')],
            [sg.InputCombo(('1 - Peace At Last','2 - The Wildernes of Tigers','3 - The Fighter, The Lover And The Thief','4 - Den Of Thieves','5 - The Banker',
                            '6 - The Baron De Valois','7 - The Key To The Castle','8 - ', '1- Requiem','9 - The Fall'), size=(35, 1),key='Sequencia')],
            [sg.Text('Quais memórias foram feitas?')],
            [sg.TabGroup([[sg.Tab('1',layout_seq1),sg.Tab('2',layout_seq2),sg.Tab('3',layout_seq3),sg.Tab('4',layout_seq4),sg.Tab('5',layout_seq5),
                           sg.Tab('6',layout_seq6),sg.Tab('7',layout_seq7),sg.Tab('8',layout_seq8),sg.Tab('9',layout_seq9)]])],
            [sg.Text('Quais foram os avanços?\n(Progressos in game, Mecanicas, Database, Itens...)')],
            [sg.InputText(size=(100,40),key='avancos')],
            [sg.Text('Qual foi a progressão da narrativa?\n(Progressões na Narrativa historica do jogo)')],
            [sg.InputText(size=(100,40),key='narra')],
            [sg.Text('Apontamentos:\n(Referencias históricas e outras Observações)')],
            [sg.InputText(size=(100,40),key='points')],
            [sg.Text('')],
            [sg.Button('Confirmar dados')]
             ]

layout2 = [ [sg.Text('Dados confirmados!')],
            [sg.Text('Arquivo Txt gerado')],
            [sg.Button('Fechar')]
            ]



# Janela principal
window = sg.Window('LabEHGames - Registro AC: Brotherhood (Beta 2.0) by João Gabriel', layout1)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        window.close()
        quit()
        
    if event == 'Confirmar dados':
        
        hora1 = values['hora1']
        if hora1 == '':
            erro('Campo do início da jogatina vazio!')
            continue
        if len(hora1) != 5 or hora1[2] != ':':
            erro('Entrada inválida!')
            continue
        check_hora = hora1.split(':')
        if check_hora[0].isnumeric() == False or check_hora[1].isnumeric() == False:
            erro('Entrada inválida!')
            continue
        elif int(check_hora[0]) > 23 or int(check_hora[0]) < 0:
            erro('Hora inválida!')
            continue
        elif int(check_hora[1]) > 59 or int(check_hora[1]) < 0:
            erro('Minutos inválidos!')
            continue
        
        hora2 = values['hora2']
        if hora2 == '':
            erro('Campo do fim da jogatina vazio!')
            continue
        if len(hora2) != 5 or hora1[2] != ':':
            erro('Entrada inválida!')
            continue
        check_hora = hora2.split(':')
        if check_hora[0].isnumeric() == False or check_hora[1].isnumeric() == False:
            erro('Entrada inválida!')
            continue
        elif int(check_hora[0]) > 23 or int(check_hora[0]) < 0:
            erro('Hora inválida!')
            continue
        elif int(check_hora[1]) > 59 or int(check_hora[1]) < 0:
            erro('Minutos inválidos!')
            continue
        
        horas_jogadas = hora1 + ' - ' + hora2

        data_hora = datetime.now()
        data_hora = data_hora.strftime('%d/%m/%Y %H:%M')

        if values['Sequencia'] == '':
            erro('Sequência não selecionada!')
            continue
        sequencia = values['Sequencia']

        memorias = ''
        for n in keys_seq_1:    #1 ---------------
            if n == keys_seq_1[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_1[n] + '\n'
        for n in keys_seq_2:    #2 ---------------
            if n == keys_seq_2[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_2[n] + '\n'
        for n in keys_seq_3:    #3 ---------------
            if n == keys_seq_3[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_3[n] + '\n'
        for n in keys_seq_4:    #4 ---------------
            if n == keys_seq_4[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_4[n] + '\n'
        for n in keys_seq_5:    #5 ---------------
            if n == keys_seq_5[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_5[n] + '\n'
        for n in keys_seq_6:    #6 ---------------
            if n == keys_seq_6[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_6[n] + '\n'
        for n in keys_seq_7:    #7 ---------------
            if n == keys_seq_7[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_7[n] + '\n'
        for n in keys_seq_8:    #8 ---------------
            if n == keys_seq_8[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_8[n] + '\n'
        for n in keys_seq_9:    #9 ---------------
            if n == keys_seq_9[0]:
                continue
            elif values[n] == True:
                memorias = memorias + seq_9[n] + '\n'
        
        avancos = values['avancos']
        if avancos == '':
            erro('Campo de avanços em branco!')
            continue
        
        narra = values['narra']
        if narra == '':
            erro('Campo de narrativa em branco!')
            continue
        
        points = values['points']
        if points == '':
            erro('Campo de apontamentos em branco!')
            continue
        
        break

window.close()

# Janela secundária
window2 = sg.Window('LabEHGames - Confirmado!', layout2)

final = 'Assassins Creed: Brotherhood\n\n' + 'Data: ' + data_hora + '\n' + 'Horas jogadas: ' + horas_jogadas + '\n\n' + 'Sequencia ' + sequencia + '\n\n' + 'Memorias feitas:\n' + memorias + '\n' + 'Avanços:\n' + avancos + '\n\n' + 'Narrativa:\n' + narra + '\n\n' + 'Apontamentos:\n' + points + '\n\n '
with open('Realatório.txt','w') as regdados:
    regdados.write(str(final))

while True:
    event, values = window2.read()
    if event == sg.WIN_CLOSED or event == 'Fechar': # if user closes window or clicks cancel
        window2.close()
        quit()
