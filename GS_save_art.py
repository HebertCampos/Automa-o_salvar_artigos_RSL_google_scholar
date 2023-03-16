import pyautogui as pg

while True:
    for i in range(12):
        for j in range(5):
            if pg.locateCenterOnScreen(r'salvar.png', confidence=0.9):
                x,y = pg.locateCenterOnScreen(r'salvar.png', confidence=0.9)
                pg.click(x=x,y=y)
                pg.click(x=x,y=y)
                break
            

        for j in range(5):
            if pg.locateCenterOnScreen(r'pasta_rsl.png', confidence=0.9):
                x,y = pg.locateCenterOnScreen(r'pasta_rsl.png', confidence=0.9)
                pg.click(x=x,y=y)
                break
            

        for j in range(5):
            if pg.locateCenterOnScreen(r'feito.png', confidence=0.9):
                x,y = pg.locateCenterOnScreen(r'feito.png', confidence=0.9)
                pg.click(x=x,y=y)
                break

    for j in range(5):        
        if pg.locateCenterOnScreen(r'proxima_pagina.png', confidence=0.9):
            x,y = pg.locateCenterOnScreen(r'proxima_pagina.png', confidence=0.9)
            pg.click(x=x,y=y)
            break
        
