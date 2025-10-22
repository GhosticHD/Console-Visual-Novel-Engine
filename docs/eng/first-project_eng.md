# Whale Engine Docs ENG
Whale Engine user documentation in English

### [Contents](./index.md)

# First project
The code demonstrations will use demonstration materials from the repository.

## Engine structure:

```
project/
├── docs                # Documentation, can be deleted
├── engine              # Folder with engine scripts
    ├── general.py      # Main code
    ├── run.py          # Code for launching the novel
├── LICENSE             # This file can be deleted
├── README.md           # This file can be deleted
├── requirements.txt    # Project dependencies, can be deletedлить
├── run.bat             # File to launch the novel
├── settings.json       # Main settings for the novel
```

## Settings file (settings.json)

The file defines the basic settings for your novel.

```
{
  "title": "[bold red]Engine demonstration[/bold red]",                                     # Title of your novel
  "style_of_title": "white",                                                                # Colour of the strip next to the title of the novel
  "description": "[bold purple]Description of this excellent novella[/bold purple]",        # Description of your novel
  "version": "1.0",                                                                         # Version of your novel
  "author": "Your name",                                                                    # Author's name
  "autro_title": "Thank you for watching!",                                                 # Main text of the novel's outro
  "autro_description": "This demonstration shows what can be implemented in the engine.",   # Text in the outro
  "style_of_autro_title": "white",                                                          # Colour of the strip in the outro
  "localization": "ru",                                                                     # Localisation of the engine text (ru/en)
  "start_file": "src/Звуки.txt"                                                             # File from which your novel begins
}
```

## Run file and scripts (run.bat, general.py, run.py)
Leave them unchanged, they are configured correctly. You can add scripts if you are not satisfied with the main engine code.

## Folder organisation
The engine supports a feature that allows you to specify the full path to the file containing the novel text or images.

Example:

```
?day.jpg
&50
!Hero
@Morning has come...;
```

or 

```
?images/chapter2/battle/day.jpg
&50
!Hero
@Morning has come...;
```

The folder path starts with the main engine folder

## Image stylisation
If you look at the images in the engine usage examples, you will see that they are black and white. The script for converting images to ASCII art works on the principle of brightness. White is the lightest, which means it will take the brightest symbol, and black is the darkest. 

## To use the engine, you need to know its syntax
If you haven't read the syntax documentation yet, it can be found at [this link](./syntax_ru.md)