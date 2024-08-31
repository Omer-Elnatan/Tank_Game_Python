import pygame,sys
from pygame.locals import *
import socket
import base64
import time
IP = '127.0.0.1'
PORT = 5000
width = 1000
height = 600




lastx=0
lasty=0
x=0
y=0
obw=40
obh=40
width_shot = 4
height_shot = 4

Running = True
def listener(Soc):
    Soc.setblocking(False)
    try:
        return Soc.recv(4000)
    except socket.error:
        return None

def main():
    lastx=0
    lasty=0
    isshot=False
    xshot=0
    yshot=0
    xshototherTank=1500
    yshototherTank=1500
    lastxotherTank=1500
    lastyotherTank=1500
    lastotherTankPic=''

    # open socket with the server
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, PORT))

    firstdata=my_socket.recv(1000000)
    firstdata = eval(str(firstdata))
    pictures = list(firstdata[0])
    areadata = list(firstdata[1])
    #print(type(tup))
    pictures=list(pictures)
    tB1 = open("tankBright.png", "wb")
    tB1.write(pictures[0].decode('base64'))
    tB1.close()
    tB2 = open("tankBleft.png", "wb")
    tB2.write(pictures[1].decode('base64'))
    tB2.close()
    tB3 = open("tankBup.png", "wb")
    tB3.write(pictures[2].decode('base64'))
    tB3.close()
    tB4 = open("tankBdown.png", "wb")
    tB4.write(pictures[3].decode('base64'))
    tB4.close()
    tB5 = open("tankAright.png", "wb")
    tB5.write(pictures[4].decode('base64'))
    tB5.close()
    tB6 = open("tankAleft.png", "wb")
    tB6.write(pictures[5].decode('base64'))
    tB6.close()
    tB7 = open("tankAup.png", "wb")
    tB7.write(pictures[6].decode('base64'))
    tB7.close()
    tB8 = open("tankAdown.png", "wb")
    tB8.write(pictures[7].decode('base64'))
    tB8.close()
    tB9 = open("boom.jpg", "wb")
    tB9.write(pictures[8].decode('base64'))
    tB9.close()
    tB10 = open("win.jpg", "wb")
    tB10.write(pictures[9].decode('base64'))
    tB10.close()
    tB11 = open("lose.png", "wb")
    tB11.write(pictures[10].decode('base64'))
    tB11.close()
    tB12 = open("black.png", "wb")
    tB12.write(pictures[11].decode('base64'))
    tB12.close()
    tB13 = open("tankBshot.png", "wb")
    tB13.write(pictures[12].decode('base64'))
    tB13.close()
    tB14 = open("wallcube.png", "wb")
    tB14.write(pictures[15].decode('base64'))
    tB14.close()
    tB15 = open("ironcube.jpg", "wb")
    tB15.write(pictures[16].decode('base64'))
    tB15.close()
    width=pictures[13]
    height=pictures[14]
    pygame.init()
    window = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()
    cube_width=pictures[17]
    shot="tankBshot.png"
    cover = pygame.image.load("black.png")
    window.blit(pygame.transform.scale(cover,(pictures[13],pictures[14])),(0,0))

    i=0
    while len(areadata)-3>=i:
        print areadata[i]
        window.blit(pygame.transform.scale(pygame.image.load(str(areadata[i])),(cube_width,cube_width)),(areadata[i+1],areadata[i+2]))
        i=i+3

    # loop until user requested to exit
    while Running:
        response = listener(my_socket)
        #print str(response)
        if(str(response)!='None'):
            i=0
            z= str(response).find('([')
            j= str(response).find('((')
            i= str(response).find('))')
            response=response[0:i+2]
            if j!=0:
                if z!=0:
                    response='None'
        print response

        if(str(response)!='None'):

            tup = eval(str(response))
            #print(type(tup))
            alldata=list(tup)

            #print(type(alldata))
            data=list(alldata[1])
            otherTankData=list(alldata[0])
            #print(type(data))
            #print data[0]

            isshot=data[3]
            isshototherTank=otherTankData[3]

            #print isshot+xshot+yshot
            window.blit(pygame.transform.scale(cover,(data[6],data[7])),(lastx,lasty))

            if(isshot==True):
                window.blit(pygame.transform.scale(cover,(width_shot,height_shot)),(xshot,yshot))
                xshot=data[4]
                yshot=data[5]
                window.blit(pygame.transform.scale(pygame.image.load(shot),(width_shot,height_shot)),(xshot,yshot))
            if(isshot==False):
                window.blit(pygame.transform.scale(cover,(width_shot,height_shot)),(xshot,yshot))



            if(isshototherTank==True):
                window.blit(pygame.transform.scale(cover,(width_shot,height_shot)),(xshototherTank,yshototherTank))
                xshototherTank=otherTankData[4]
                yshototherTank=otherTankData[5]
                window.blit(pygame.transform.scale(pygame.image.load(shot),(width_shot,height_shot)),(xshototherTank,yshototherTank))
            if(isshototherTank==False):
                window.blit(pygame.transform.scale(cover,(width_shot,height_shot)),(xshototherTank,yshototherTank))




            if(lastxotherTank!=otherTankData[1])or(lastyotherTank!=otherTankData[2])or(otherTankData[0]!=lastotherTankPic):

                window.blit(pygame.transform.scale(cover,(otherTankData[6],otherTankData[7])),(lastxotherTank,lastyotherTank))
                window.blit(pygame.transform.scale(pygame.image.load(otherTankData[0]),(otherTankData[6],otherTankData[7])),(otherTankData[1],otherTankData[2]))
                lastxotherTank=otherTankData[1]
                lastyotherTank=otherTankData[2]


            window.blit(pygame.transform.scale(pygame.image.load(data[0]),(data[6],data[7])),(data[1],data[2]))
            pygame.display.update()
            pygame.display.flip()
            lastx=data[1]
            lasty=data[2]




        for event in pygame.event.get():
            #BLUE TANK MOVEMENTS

            if event.type == pygame.KEYUP:
                if event.key == 273:


                    my_socket.send('up')
            if event.type == pygame.KEYDOWN:

                if event.key == 274:


                    my_socket.send('down')

                elif event.key == K_RIGHT:


                    my_socket.send('right')

                elif event.key == K_LEFT:


                    my_socket.send('left')


            if(pygame.key.get_pressed()[ord('e')]==1) and (isshot==False):

                my_socket.send('shoot')


        clock.tick(60)


    pygame.quit()





if __name__ == '__main__':
    main()