# Created by: Matthew Walsh
# Created on: september 2017
# Created for: ICS3U
# This program is the Hello, World program, but with 3 buttons

import ui

def english_button(sender):
    # displays the English version
    view['hello_world_label'].text = ('Hello, World!')
    
def french_button(sender):
    # displays the French version
    view['hello_world_label'].text = ('Bonjour le monde!')
    
def spanish_button(sender):
    # displays the Spanish version
    view['hello_world_label'].text = ('Hola Mundo')


view = ui.load_view()
view.present('full_screen')
