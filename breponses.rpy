screen breponses:
    #style_prefix "stats"
    frame:
        #background Solid("#FFFFFF")
        background "transparent.png"
        xalign 0.0
        yalign 0.0
        xsize 300
        ysize 45
        if breponses <= 1:
            text "{color=#32a836}{size=30}[breponses] bonne réponse"
        else:
            text "{color=#32a836}{size=30}[breponses] bonnes réponses"