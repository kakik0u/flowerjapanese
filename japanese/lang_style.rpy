# GUI - DEFAULT

translate japanese style default: #sans-serif
    font "tl/japanese/fonts/LightNovelPOPv2.otf"
    language "japanese-normal"

translate japanese style default_bold is default: #sans-serif bold
    font "tl/japanese/fonts/LightNovelPOPv2.otf"


# GUI - LICENSE

translate japanese style license_font: #Noto Sans Mono
    font "tl/japanese/fonts/MPLUS1-Medium.ttf"

translate japanese style license_description_1 is default: #sans-serif
    size 27.49
    line_spacing 15.2
    color "#ffffff99"

translate japanese style license_description_2 is default: #sans-serif
    size 16.35
    line_spacing 5.2
    color "#ffffff99"


# GUI - HISTORY

translate japanese style history_text: #rounded sans-serif
    font "tl/japanese/fonts/LightNovelPOPv2.otf"
    language "japanese-loose"

translate japanese style history_name_text: #serif
    font "tl/japanese/fonts/MPLUS1-Medium.ttf"

translate japanese style choice_pick_text is default #sans-serif


# GUI - OTHERS

translate japanese style navi_music_name_text is default_bold: #bold sans-serif
    kerning -0.5


# DIALOGUE - SCRIPT

translate japanese style dialogue_text_base:
    font "tl/japanese/fonts/LightNovelPOPv2.otf"
    size 24
    color "#ffffff"
    language "japanese-loose"
    line_spacing 8
    line_overlap_split -2

translate japanese style dialogue_text is dialogue_text_base:
    pos (202, 556)
    xsize 760

translate japanese style dialogue_text_letterbox is dialogue_text_base:
    pos (154, 631)
    xsize 900

translate japanese style say_dialogue is dialogue_text:
    line_spacing 8


# DIALOGUE - NAME

translate japanese style dialogue_name_text:
    font "tl/japanese/fonts/MPLUS1-Medium.ttf"
    size 33
    color "#ffffff"
    anchor (0.5, 0.5)
    pos (119, 603)

translate japanese style dialogue_name_text_letterbox is dialogue_name_text:
    size 31
    anchor (1.0, 0.5)
    pos (115, 648)


# DIALOGUE - NVL

translate japanese style dialogue_nvl_text:
    font "tl/japanese/fonts/MPLUS1-Medium.ttf"
    size 37
    language "japanese-normal"
    color "#ffffff"
    align (0.5, 0.5)
    line_spacing 8
    xsize 1000
    textalign 0.5


# SYSTEM

translate japanese python:
    gui.system_font = u'tl/japanese/fonts/MPLUS1-Medium.ttf'
    gui.font = u"tl/japanese/fonts/MPLUS1-Medium.ttf"