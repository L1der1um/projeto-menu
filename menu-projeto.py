import pygame
import pygame_menu

#INICIALIZADOR PYGAME
pygame.init()

#CONFIGURAÇÕES DE TELA
largura, altura = 1080, 720
tela = pygame.display.set_mode((largura, altura))

#FUNÇÃO PARA MOSTRAR O MENU INICIAL
def menu_inicial():
    
    #CRIA MENU PRINCIPAL
    menu = pygame_menu.Menu("Menu Principal", largura, altura, theme=pygame_menu.themes.THEME_DARK)

    #ADICIONANDO NOME DA MATÉRIA
    menu.add.label("PROJETO INTEGRADOR - COMPILADORES E GRAFOS \n")
    #ADICIONANDO NOME DA MATÉRIA
    menu.add.label("Engenharia da Computação - Modulo 4 \n")
    
    #FUNÇÃO INICIAR JOGO
    def iniciar_jogo():
        pass

    #FUNÇÃO PARA MOSTRAR OS INTEGRANTES
    def mostrar_integrantes():
        
        #MENU INTEGRANTES DO PROJETO
        menu_integrantes = pygame_menu.Menu("Integrantes", largura, altura, theme=pygame_menu.themes.THEME_DARK)

        #ADICIONA OS NOMES DOS INTEGRANTES
        menu_integrantes.add.label("Gabriel Resende")
        menu_integrantes.add.label("(Lider) Luis Antonio de Albuquerque Adamski")
        menu_integrantes.add.label("Luis Filipe Giglio Frasão")
        menu_integrantes.add.label("Matheus Henrique de Oliveira")
        menu_integrantes.add.label("Matheus Setsuo Mihara de Siqueira")
        menu_integrantes.add.label("Pedro Ludovico Rodrigues \n")

        #BOTÃO VOLTAR MENU
        menu_integrantes.add.button("Voltar", menu_inicial)

        #EXECUTA O MENU INTEGRANTES
        menu_integrantes.mainloop(tela)

    #ITENS CLICAVEIS DO MENU
    menu.add.button("Iniciar Jogo", iniciar_jogo)
    menu.add.button("Integrantes", mostrar_integrantes)
    menu.add.button("Sair", pygame_menu.events.EXIT)


    #ADICIONANDO NOME DA MATÉRIA
    menu.add.label("\n2023")

    #EXECUTA O MENU PRINCIPAL
    menu.mainloop(tela)

#CHAMADA DA FUNÇÃO MENU INICIAL
menu_inicial()

#ENCERRANDO PYGAME
#pygame.quit()
