import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    #こうかとん
    chara_img = pg.image.load("fig/3.png")
    chara_img = pg.transform.flip(chara_img, True, False)
    chara_img = pg.transform.rotozoom(chara_img, 10, 1.0)

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%800
        screen.blit(bg_img, [-x, 0])

        chara_rct = chara_img.get_rect() #こうかとんレクトの取得
        chara_rct.center = 300, 200
        screen.blit(chara_img, chara_rct)

        pg.display.update()
        tmr += 1   


        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()