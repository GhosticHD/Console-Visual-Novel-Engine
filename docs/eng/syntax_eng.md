# Whale Engine Docs ENG
Whale Engine user documentation in English

### [Contents](./index.md)

## Introduction
Whale Engine uses a simple text-based syntax based on prefixes to create interactive visual novels.

## List of commands
| **Prefix** | **Назначение** | **Example** | **Description** |
|---------|------------|--------|-----------|
| `!` | **Character name** | `!John` | Sets the name of the speaking character |
| `@` | **Text of the message** | `@Hello!` | Adds text to the current message |
| `;` | **End of message** | `@End of message;` | Completes and displays the current message |
| `>` | **Go to file** | `>chapter2.txt` | Moves on to executing another script file |
| `:` | **Print speed** | `:0.02` | Sets the delay between characters (in seconds) |
| `?` | **Image** | `?images/scene1.png` | Sets the background image (converted to ASCII) |
| `&` | **Image size** | `&60` | Sets the width of the ASCII image in characters |
| `%` | **The end of the novella** | `%` | Concludes the novella and shows the final part |
| `+` | **The question of choice** | `+Where will you go?` | Sets the question for the selection menu |
| `$` | **Text of the variant** | `$1. To the left` | Adds the text of the selection option |
| `^` | **Purpose of the option** | `^left.txt` | Specifies the file to navigate to when selecting an option |
| `=` | **Show selection** | `=` | Activates the selection menu display |

# [🎭] Working with dialogues

## Basic dialogue

```
!Maria
@Hello! How are you?;
```

## Multi-line dialogue

```
!John
@This is a long message
@that continues
@over several lines;
```

## Dialogue with image

```
?images/forest.png
&50
!Forest Guide
@We have arrived in a mysterious forest...;
```

# [🎮] Selection system

## Simple choice

```
+What shall we do?
$1. Look around the room
^search_room.txt
$2. Go outside
^go_outside.txt
=
```

## Multiple choice

```
+Select an action:
$1. Attack
^attack.txt
$2. Defend
^defend.txt
$3. Escape
^escape.txt
$4. Try to negotiate
^negotiate.txt
=
```

# [📁] Scenario management

## Switching between files

```
!Narrator
@Chapter 1 complete...;
>chapter2.txt
```

## The end of the novella

```
!Narrator
@And so our story has come to an end.;
%
```

# [⚙️] Display settings

## Text speed

```
:0.05
!Fast character
@This text is displayed quickly;
:0.1
!Slow character
@And this one is slower;
```

## Images

```
?images/castle.jpg
&70
!Knight
@We approached the majestic castle.;
?images/dungeon.png
&40
!Knight
@Now we are in a gloomy dungeon...;
```

# [💡] Example of a complete scenario

```
:0.03
?images/start.jpg
&60
!Author
@Welcome to our visual novel!;

!Main character
@Waking up in the morning, I realised that an important decision awaited me today.;

+What should I do today?
$1. Go to work
^work_path.txt
$2. Stay at home
^home_path.txt
$3. Go on a trip
^travel_path.txt
=
```

# [🎨] Special features

## Real-time speed control

```
:0.1
!Character
@Slow text...;
:0.01
@And now very fast!;
```

## Feature with images
If an image does not change over several lines, it is not necessary to write it out multiple times:

```
?images/day.jpg
&50
!Hero
@Morning has come...;

!Hero
@It's time to set off!;
```

# [📝] Usage notes

- **Command order**: Commands are executed sequentially from top to bottom

- **Case sensitivity**: Prefixes are case sensitive (use only the specified characters)

- **Spaces**: It is recommended to put a space after the prefix for readability

- **Encoding**: All files must be in UTF-8 encoding

- **Images**: PNG, JPEG, BMP and other formats compatible with PIL are supported

### This markup language allows you to create complex interactive stories with minimal effort! 🐋