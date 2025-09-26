import re
import os
import time
from rich.console import Console
from PIL import Image
import numpy as np
import json

""""CONSTS AND GLOBAL"""
COMMAND_PREFIX = '!'
GREATER_THAN_PREFIX = '>'
AT_PREFIX = '@'
LINE_ENDING = ';'
DOUBLE_DOT_PREFIX = ':'
QUESTION_MARK_PREFIX = '?'
AMPERSAND_PREFIX = '&'
PERCENT_PREFIX = '%'
"""CHOICE UPDATE"""
PLUS_PREFIX = '+'
CHOICE_PREFIX = '$'
CIRCUMFLEX_PREFIX = '^'
EQUAL_PREFIX = '='


NAME = ''
MESSAGE = ''
TIMER_SECS = 0.1
IMAGE = ''
WIDTH = 40

LIST_OF_CHOICES = {}
LIST_OF_TEXT_CHOICES = {}
QUESTION_OF_CHOICE = ''

LOCALIZATION = ''

console = Console()

""""GENERAL FUNCTIONS"""

def intro():
    json = loadSettings()
    colorOfRule = json['style_of_title']
    console.rule(json['title'], style=f"{colorOfRule}")

    if LOCALIZATION == "ru":
        console.print(f"{json['description']}")
        time.sleep(3)
        console.print(f"\nАвтор: {json['author']}", justify="center")
        time.sleep(1)
        console.print(f"Версия: {json['version']}", justify="center")
        time.sleep(2)
        console.print("\n\n[italic]Нажмите [bold]Enter[/bold] для продолжения...[/italic]", justify="center")
        input("")
        readFile(json['start_file'])

    else:
        console.print(f"Description: {json['description']}")
        time.sleep(3)
        console.print(f"Author: {json['author']}", justify="center")
        time.sleep(1)
        console.print(f"Version: {json['version']}", justify="center")
        time.sleep(2)
        console.print("\n\n[italic]Press [bold]Enter[/bold] to continue...[/italic]", justify="center")
        input("")
        readFile(json['start_file'])

def autro():
    clear()
    json = loadSettings()
    colorOfRule = json['style_of_autro_title']
    console.rule(json['autro_title'], style=f"{colorOfRule}")
    if LOCALIZATION == "ru":
        console.print(f"Послесловие: {json['autro_description']}")
        time.sleep(3)
        console.print(f"Автор: {json['author']}", justify="center")
        time.sleep(1)
        console.print(f"Версия: {json['version']}", justify="center")
        time.sleep(2)
        console.print("\n\n[italic]Нажмите [bold]Enter[/bold] для выхода[/italic]", justify="center")
        input("")
        exit()
        

    else:
        console.print(f"Epilogue: {json['autro_description']}")
        time.sleep(3)
        console.print(f"Автор: {json['author']}", justify="center")
        time.sleep(1)
        console.print(f"Версия: {json['version']}", justify="center")
        time.sleep(2)
        console.print("\n\n[italic]Press [bold]Enter[/bold] to exit[/italic]", justify="center")
        input("")
        exit()
        
def jsonParse(PATH):
    global LOCALIZATION
    with open(PATH, 'r') as file:
        DATA = json.load(file)
    LOCALIZATION = DATA['localization']

def loadSettings():
    with open('settings.json', encoding='utf-8') as file:
        DATA = json.load(file)  # Теперь это работает
    return DATA

def message(name, text) -> None:
    printedMessage = ''
    formattedMessage = removeBracketsContent(MESSAGE)
    clear()
    if IMAGE and WIDTH and WIDTH > 0:
        ascii_image = image_to_ascii(IMAGE, WIDTH)
        for i in range(len(formattedMessage)):
            print(ascii_image)
            printedMessage += formattedMessage[i]
            console.print(f"{NAME}: {printedMessage}")
            time.sleep(TIMER_SECS)
            clear()
        print(ascii_image)
        console.print(f"{NAME}: {MESSAGE}")
        if LOCALIZATION == "ru":
            console.print("\n[italic]Нажмите [bold]Enter[/bold] для продолжения...[/italic]", justify="center")
        else:
            console.print("\n[italic]Press [bold]Enter[/bold] to continue...[/italic]", justify="center")
        input()
    else:
        for i in range(len(formattedMessage)):
            printedMessage += formattedMessage[i]
            console.print(f"{NAME}: {printedMessage}")
            time.sleep(TIMER_SECS)
            clear()
        console.print(f"{NAME}: {MESSAGE}")
        if LOCALIZATION == "ru":
            console.print("\n[italic]Нажмите [bold]Enter[/bold] для продолжения...[/italic]", justify="center")
        else:
            console.print("\n[italic]Press [bold]Enter[/bold] to continue...[/italic]", justify="center")
        input()


def choice():
    while True:

        global LIST_OF_CHOICES, LIST_OF_TEXT_CHOICES, QUESTION_OF_CHOICE

        clear()

        console.print(QUESTION_OF_CHOICE + '\n')

        for i in LIST_OF_CHOICES:
            console.print(LIST_OF_TEXT_CHOICES.get(i))

        if LOCALIZATION == "ru":
            console.print("[italic]Напишите [bold]предложенный вариант[/bold] для продолжения...[/italic]", justify="center")
        else:
            console.print("[italic]Write the [bold]suggested option[/bold] to continue...[/italic]", justify="center")

        try:
            userInput = int(input())

            if LIST_OF_CHOICES.get(userInput) != None:
                readFile(LIST_OF_CHOICES.get(userInput))
                break
        except:
            pass


    
def choiceLineFormat(choice_char, choice_text):
    return f'{choice_char} {choice_text}'
    
def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def readFile(PATH: str) -> None:
    global IMAGE
    clearStr()
    IMAGE = ''
    try:
        with open(PATH, 'r', encoding='utf-8') as file:
            for line in file:
                analyzeLine(line.strip()) 
    except (FileNotFoundError, PermissionError) as e:
        if LOCALIZATION == "ru":
            print(f"Ошибка при чтении файла: {e}")
    else:
        print(f"Error reading file: {e}")

def analyzeLine(line: str):
    global NAME, MESSAGE, TIMER_SECS, IMAGE, WIDTH, LIST_OF_CHOICES, LIST_OF_TEXT_CHOICES, QUESTION_OF_CHOICE

    if not line:
        return

    if line.startswith(COMMAND_PREFIX):
        NAME = line[1:].strip()  

    if line.startswith(AT_PREFIX):
        MESSAGE += line[1:].strip() + " "  

    if line.endswith(LINE_ENDING):
        MESSAGE += line[:-1].strip()  
        message(NAME, MESSAGE)
        clearStr()

    if line.startswith(GREATER_THAN_PREFIX):
        readFile(line[1:])

    if line.startswith(DOUBLE_DOT_PREFIX):
        TIMER_SECS = float(line[1:])

    if line.startswith(QUESTION_MARK_PREFIX):
        IMAGE = line[1:]

    if line.startswith(AMPERSAND_PREFIX):
        WIDTH = int(line[1:])

    if line.startswith(PERCENT_PREFIX):
        autro()

    if line.startswith(PLUS_PREFIX):
        QUESTION_OF_CHOICE = line[1:].strip()

    if line.startswith(CHOICE_PREFIX):
        LIST_OF_TEXT_CHOICES[len(LIST_OF_TEXT_CHOICES)+1] = line[1:]

    if line.startswith(CIRCUMFLEX_PREFIX):
        LIST_OF_CHOICES[len(LIST_OF_CHOICES)+1] = line[1:]

    if line.startswith(EQUAL_PREFIX):
        choice()

def removeBracketsContent(text):
    return re.sub(r'\[.*?\]', '', text)

        
def clearStr():
    global NAME, MESSAGE
    NAME = ''
    MESSAGE = ''   

def image_to_ascii(image_path, width):
    img = Image.open(image_path)
    aspect_ratio = img.height / img.width
    new_height = int(aspect_ratio * width * 0.55) 
    img = img.resize((width, new_height))
    img = img.convert('L') 

    pixels = np.array(img)
    chars = " .:!/r1W$@"
    ascii_str = ""
    
    for row in pixels:
        for pixel in row:
            ascii_str += chars[min(pixel // 25, len(chars) - 1)]
        ascii_str += "\n"
    
    return ascii_str
