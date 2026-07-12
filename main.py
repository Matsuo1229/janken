import json
import pygame
import asyncio
import sys
import random
from platform import window

idx = 0
effect = []
rireki_1 = []
result = 0
BLACK = (256, 256, 256)
WHITEe = (0, 0, 0)

HAND = ("無限", "創造の儀式", "混逆の魂")
hand = ["グー", "チョキ", "パー"]

async def check():#出された手の変化
    global hand_1, rireki_1

    if HAND[0] in rireki:#無限の処理
        if hand_1 == HAND[0]:
            rireki.remove(HAND[1])
        else:
            hand_1 = HAND[1]


    if HAND[2] in effect:#混逆の魂
        if hand_1 == hand[0]:
            hand_1 = hand[1]

        elif hand_1 == hand[1]:
            hand_1 = hand[2]

        elif hand_1 == hand[2]:
            hand_1 = dokuji_1

        elif hand_1 == dokuji:
            hand_1 = hand[0]
    if hand_1 == HAND[2]:
        if HAND[2] in effect:
            effect.remove(HAND[2])
        else:
            effect.append(HAND[2])
    if hand_2 == HAND[2]:
        if HAND[2] in effect:
            effect.remove(HAND[2])
        else:
            effect.append(HAND[2])
        

    rireki_1.append(hand_1)
    await asyncio.sleep(0)
    

async def battle():
    global result
        if hand_1 == hand[0]:
            if hand_2 == hand[0]
                result = 0

            elif hand_2 == hand[1]:
                result = 1

            elif hand_2 == hand[2]:
                result = -1

        if hand_1 == hand[1]:
            if hand_2 == hand[0]
                result = -1

            elif hand_2 == hand[1]:
                result = 0

            elif hand_2 == hand[2]:
                result = 1

        if hand_1 == hand[2]:
            if hand_2 == hand[0]
                result = 1

            elif hand_2 == hand[1]:
                result = -1

            elif hand_2 == hand[2]:
                result = 0

        if hand_1 == HAND[0]:
            result = -1

        if hand_1 == HAND[1]:
            rireki.count(hand[2]) >=2 and rireki.count(hand[1]) >=2 and rireki.count(hand[2]) >=2:
                result = 1

        client.send(result)
        await asyncio.sleep(0)
                

class Client:

    def __init__(self, url):
        self.connected = False
        self.messages = []

        self.ws = window.WebSocket.new(url)

        self.ws.onopen = self.on_open
        self.ws.onmessage = self.on_message
        self.ws.onclose = self.on_close
        self.ws.onerror = self.on_error
        await asyncio.sleep(0)

    def on_open(self, event):
#        print("接続成功")
        self.connected = True
        await asyncio.sleep(0)

    def on_message(self, event):
        global hand_2,recieve
#        print("受信:", event.data)
        recieve = 0
        self.messages.append(data)
        hand_2 = data
        recieve = 1
        await asyncio.sleep(0)

    def on_close(self, event):
#        print("切断")
        self.connected = False
        await asyncio.sleep(0)

    def on_error(self, event):
#        print("エラー")
        await asyncio.sleep(0)

    def send(self, obj):
        if self.connected:
            self.ws.send(text)
        await asyncio.sleep(0)

async def main():
    global hand_1, hand_2, idx,hand_1, dokuji_1,sent,kati,make

    kati, make = 0, 0

    pygame.mouse.set_set.pos((400, 300))
    
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 30)

    client = WSClient("wss://jankenserver.my-647.workers.dev/")

    dokuji_1 = random.choice(HAND)

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if idx == 0:
                cele = 1
                sent = 0
                
                screen.fill(BLACK)
                txt_1 = font.render("グー", True, WHITE)
                txt_2 = font.render("チョキ", True, WHITE)
                txt_3 = font.render("パー", True, WHITE)
                txt_4 = font.render(dokuji_1, True, WHITE)

                screen.blit(txt_1, [150, 350])
                screen.blit(txt_2, [300, 400])
                screen.blit(txt_3, [450, 400])
                screen.blit(txt_4, [600, 400])

                pygame.display.update()

                if event.type == KEYDOWN:#選択の切り替え
                    if event.key == K_SPACE:
                        if cele == 1:
                            cele += 1
                            screen.blit(txt_1, [150, 400])
                            screen.blit(txt_2, [300, 350])

                        elif cele == 2:
                            cele += 1
                            screen.blit(txt_2, [150, 400])
                            screen.blit(txt_3, [300, 350])

                        elif cele == 3:
                            cele += 1
                            screen.blit(txt_3, [150, 400])
                            screen.blit(txt_4, [300, 350])

                        elif cele == 4:
                            cele = 1
                            screen.blit(txt_4, [300, 400])
                            screen.blit(txt_1, [150, 350])

                    pygame.display.update()

                    check()
                        

                    if event.key == K_ENTER:
                        if cele == 1:
                            hand_1 = hand[0]

                        elif cele == 2:
                            hand_1 = hand[1]

                        elif cele == 3:
                            hand_1 = hand[2]

                        elif cele ==4:
                            hand_1 = dokuji_1


                        client.send(hand_1)
                        sent = 1
                        idx = 1


        if idx == 1:
            if sent ==1 and recieve == 1:
                txt_5 = font.render(hand_2, True, WHITE)
                screen.blit(txt_5, [250, 200])

                pygame.display.update()

                idx = 2

        if idx == 2:
            await check()
            await asyncio.sleep(0)
            await battle()
            await asyncio.sleep(0)
            
            if hand_2 == result:
                txt_6 = font.render("あいこ", True, WHITE)
                screen.blit(txt_6, [350, 200])

            if result >> 1:
                txt_6 = font.render("勝ち", True, WHITE)
                screen.blit(txt_6, [350, 200])
                kati += 1

            if result << 1:
                txt_6 = font.render("負け", True, WHITE)
                screen.blit(txt_6, [350, 200])
                make += 1

            idx = 0

        if kati == 3 or make ==3:
            idx = 3
                
            
        clock.tick(60)
        await asyncio.sleep(0)


asyncio.run(main()) 

                    
                            

            
        
        
    
