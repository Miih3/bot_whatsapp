#   ROBÔ WHATSAPP

import time
from googletrans import Translator
import pyautogui as pt   #pip install pyautogui
import pyperclip         #pip install pyperclip
import PIL               #pip install Pillow


def tradutor():

    pt.write('voce tem 30 segundos para enviar a mensagem')
    pt.press('Enter')
    time.sleep(3)
    pt.scroll(200,120,120)
    time.sleep(30) # 30segundos
    pt.scroll(-200,-120,-120)
    pt.scroll(-200,-120,-120)
    time.sleep(2)
    position = pt.locateOnScreen('imagens/mensagem_n_lida.png',confidence=.7)
    
    if position is not None:
        pt.moveTo(position)       
        time.sleep(1)

        #copiar mensagem
        local=pt.locateOnScreen('imagens/digite_aqui.png', confidence=.7)
        pt.moveTo(local)
        pt.moveRel(150,-90)
        time.sleep(2)

        pt.tripleClick()
        time.sleep(1)
        pt.rightClick()
        time.sleep(2)
        pt.moveRel(40,10)
        
        pt.press('Enter')

        # abrir campo de digitar
        escrever_posicao = pt.locateOnScreen('imagens/digite_aqui.png',confidence=.7)
        pt.moveTo(escrever_posicao)
        pt.moveRel(150,0)
        pt.click()
        time.sleep(1)
        
        #traduzindo palavra para o inglês
        translator=Translator()
        lista = pyperclip.paste()
        traduzindo = translator.translate(lista , dest='en')
            
            #escrever e enviar tradução    
        pt.write(traduzindo.text)
        pt.press('Enter')
        print(traduzindo.origin, '->', traduzindo.text)
        time.sleep(3)
        
    else:
        # se nao houver novas mensagens em 30 segundos
        print('nao tem novas msg ')
        pt.write('Tempo esgotado ...*PROGRAMA FINALIZADO*')
        pt.press('Enter')
        time.sleep(3)
        
    
#tradutor()

def copiar_colar_responder():
    #copiar mensagem
    time.sleep(3)
    local=pt.locateOnScreen('imagens/digite_aqui.png', confidence=.7)
    pt.moveTo(local)
    pt.moveRel(130,-85)
    time.sleep(2)

    pt.tripleClick()
    time.sleep(1)
    pt.rightClick()
    time.sleep(2)
    pt.moveRel(40,10)
    
    pt.press('Enter')

        #colar mensagem aqui
    whatsapp_message = pyperclip.paste()

    # respostas
    print("mensagem recebida: " + whatsapp_message)
    
    
    if whatsapp_message.lower() == 'tradutor**':       
        time.sleep(2)
        
        tradutor()

    elif whatsapp_message.lower() =='oi' :
        pt.write('ola td bem com vc??')
        pt.press('Enter')
        
    elif whatsapp_message.lower() =='td bem sim e cntg?':
        pt.write('assim,estou bem!!')
        pt.press('Enter')
    
    elif whatsapp_message.lower() =='bm e vc ' :
        pt.write('assim,estou bem!!')
        pt.press('Enter')

    elif whatsapp_message.lower() =='sim estou e vc':
        pt.write('assim,estou bem!!')
        pt.press('Enter')

    elif whatsapp_message.lower() =='oie':
        pt.write('ooi..Como vai??')
        pt.press('Enter')

    elif whatsapp_message.lower() =='ooi':
        pt.write('ooi..Como vai??')
        pt.press('Enter') 

    elif whatsapp_message.lower() =='bom dia':
        pt.write('bomm diaa' )
        pt.press('Enter')

    elif whatsapp_message.lower() =='boa noite':
        pt.write('boa noitee ' )
        pt.press('Enter')

    elif whatsapp_message.lower() =='boa tarde':
        pt.write('boa tardee' )
        pt.press('Enter')

    elif whatsapp_message.lower() == 'bem e vc':
        pt.write('estou bem tambem')
        pt.press('Enter')
        
    elif whatsapp_message.lower() == 'que faz de bom':
        pt.write('agr nd e vc..?')
        pt.press('Enter')

    elif whatsapp_message.lower() == 'q faz de bom':
        pt.write('agr nd e vc..?')
        pt.press('Enter')

    elif whatsapp_message.lower() == 'oque tá fazendo':
        pt.write('agr nd e vc..?')
        pt.press('Enter')

    elif whatsapp_message.lower() == 'e vc como esta':
        pt.write('estou bem tbm...obgd por perguntar :)')
        pt.press('Enter')

    elif whatsapp_message.lower() == 'como vc esta e como foi seu dia':
        pt.write('estou bem tbm.. meu dia foi bom tbmm ksks')
        pt.press('Enter')
    
    else:
        #  CASO NAO TENHA UMA RESPOSTA
        time.sleep(2)
        
            #COPIAR NOME
        pt.moveTo(600,70)
        pt.click()
        time.sleep(4)
        pt.moveTo(1400,425)
        pt.doubleClick()
        pt.hotkey('Ctrl','c')
        time.sleep(2)
        nome = pyperclip.paste()
        #mover ate pesquisa
        mover_ate_lupa = pt.locateCenterOnScreen('imagens/lupa.png',confidence=.7)
        pt.moveTo(mover_ate_lupa)
        pt.moveRel(+100,0)
        pt.click()

            # COLAR NOME
        pt.hotkey('Ctrl','v')
        time.sleep(3)
        
            #ENTRAR SETINHA
        pt.moveTo(150,300)
        posicao_seta = pt.locateOnScreen("imagens/seta.jpg", confidence = .7)
        pt.moveTo(posicao_seta)
        pt.click()
        time.sleep(2)

            #MARCAR COMO NAO LIDA
        mensagem_nao_lida = pt.locateCenterOnScreen('imagens/nao_lida.png', confidence = .7)
        pt.moveTo(mensagem_nao_lida)
        pt.click()

            #ENTRAR SETINHA
        pt.moveTo(150,300)
        time.sleep(5)
        posicao_seta = pt.locateOnScreen("imagens/seta.jpg", confidence = .7)
        pt.moveTo(posicao_seta)
        pt.click()
        time.sleep(2)

            # ARQUIVAR MENSAGEM
        arquivar_mensagem = pt.locateOnScreen('imagens/aquivar_conversa.png' , confidence = .7)
        pt.moveTo(arquivar_mensagem)
        pt.click()
        time.sleep(1)

            #VOLTAR TELA INICIAL
        voltar_tela = pt.locateOnScreen('imagens/voltar.png' , confidence = .7)
        pt.moveTo(voltar_tela)
        pt.click()

        print('NÃO CONSEGUIU RESPONDER>>  ',nome)


#copiar_colar_responder()
            
   
def cheque_novas_mensagens():

    while True:
        # ENCONTRAR POSIÇÃO CIRCULO 'NOVAS MENSAGENS
        position = pt.locateOnScreen("imagens/circuloo.PNG", confidence = .7)

        if position is not None:
            pt.moveTo(position)
            pt.moveRel(-100,0)
            pt.click()

            time.sleep(3)
            
            copiar_colar_responder()
            time.sleep(10)

        else:
            print(">>> NÃO Á NOVAS MENSAGENS")
            time.sleep(20)


cheque_novas_mensagens()

