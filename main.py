import pygame
import asyncio
import sys
import random
from platform import window


idx = 0
effect = []
rireki_1 = []

result = 0
receive = 0
cele = 1

hand_1 = ""
hand_2 = ""

WHITE = (255,255,255)
BLACK = (0,0,0)

HAND = (
    "無限",
    "創造の儀式",
    "混逆の魂"
)

hand = [
    "グー",
    "チョキ",
    "パー"
]


# =========================
# WebSocket Client
# =========================

class Client:

    def __init__(self,url):

        self.connected = False
        self.messages = []

        self.ws = window.WebSocket.new(url)

        self.ws.onopen = self.on_open
        self.ws.onmessage = self.on_message
        self.ws.onclose = self.on_close
        self.ws.onerror = self.on_error


    def on_open(self,event):

        print("WebSocket接続成功")
        self.connected = True


    def on_message(self,event):

        global hand_2, receive

        print("受信:",event.data)

        hand_2 = event.data
        receive = 1


    def on_close(self,event):

        print("切断")
        self.connected = False


    def on_error(self,event):

        print("WebSocketエラー")


    def send(self,data):

        if self.connected:

            self.ws.send(data)

            print("送信:",data)



# =========================
# 手の特殊処理
# =========================

async def check():

    global hand_1


    if HAND[0] in rireki_1:

        if hand_1 == HAND[0]:

            if HAND[1] in rireki_1:
                rireki_1.remove(HAND[1])

        else:

            hand_1 = HAND[1]



    if HAND[2] in effect:

        if hand_1 == hand[0]:
            hand_1 = hand[1]

        elif hand_1 == hand[1]:
            hand_1 = hand[2]

        elif hand_1 == hand[2]:
            hand_1 = dokuji_1


        elif hand_1 == dokuji_1:
            hand_1 = hand[0]



    if hand_1 == HAND[2]:

        if HAND[2] in effect:
            effect.remove(HAND[2])

        else:
            effect.append(HAND[2])



    rireki_1.append(hand_1)

    await asyncio.sleep(0)



# =========================
# 勝敗判定
# =========================

async def battle():

    global result


    if hand_1 == hand[0]:

        if hand_2 == hand[0]:
            result=0

        elif hand_2==hand[1]:
            result=1

        elif hand_2==hand[2]:
            result=-1



    elif hand_1 == hand[1]:

        if hand_2==hand[0]:
            result=-1

        elif hand_2==hand[1]:
            result=0

        elif hand_2==hand[2]:
            result=1



    elif hand_1 == hand[2]:

        if hand_2==hand[0]:
            result=1

        elif hand_2==hand[1]:
            result=-1

        elif hand_2==hand[2]:
            result=0



    await asyncio.sleep(0)



# =========================
# Main
# =========================

async def main():

    global idx
    global cele
    global hand_1
    global dokuji_1
    global receive


    pygame.init()


    screen = pygame.display.set_mode(
        (800,600)
    )

    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None,30)


    # ★ Cloudflare Workers URL
    client = Client(
        "wss://あなたのworker名.workers.dev/"
    )


    dokuji_1=random.choice(HAND)



    while True:


        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()



            if idx==0:


                if event.type==pygame.KEYDOWN:


                    if event.key==pygame.K_SPACE:


                        cele+=1

                        if cele>4:
                            cele=1



                    if event.key==pygame.K_RETURN:


                        if cele==1:
                            hand_1=hand[0]

                        elif cele==2:
                            hand_1=hand[1]

                        elif cele==3:
                            hand_1=hand[2]

                        elif cele==4:
                            hand_1=dokuji_1



                        client.send(hand_1)


                        receive=0

                        idx=1



        screen.fill(BLACK)



        if idx==0:


            texts=[
                "グー",
                "チョキ",
                "パー",
                dokuji_1
            ]


            for i,t in enumerate(texts):

                img=font.render(
                    t,
                    True,
                    WHITE
                )

                screen.blit(
                    img,
                    (
                    150+i*150,
                    400
                    )
                )



        elif idx==1:


            wait=font.render(
                "相手待ち...",
                True,
                WHITE
            )

            screen.blit(wait,(300,200))


            if receive:

                idx=2



        elif idx==2:


            await check()

            await battle()



            if result==1:

                msg="勝ち"

            elif result==-1:

                msg="負け"

            else:

                msg="あいこ"



            img=font.render(
                msg,
                True,
                WHITE
            )

            screen.blit(
                img,
                (350,200)
            )


            await asyncio.sleep(2)

            idx=0



        pygame.display.flip()

        clock.tick(60)

        await asyncio.sleep(0)



asyncio.run(main())
