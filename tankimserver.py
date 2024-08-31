#   Heights sockets Ex. 2.7 template - server side
#   Author: Barak Gonen, 2017
import socket
import time
import base64
IP = '127.0.0.1'
PORT = 5000


def TouchCube(xtank,ytank,cubesData,cubewidth,tank_width,tank_height,request):

    cubesData=list(cubesData)
    i=0

    while(len(cubesData)-3>=i):
        if(request=='right'):
            if((xtank+tank_width>=cubesData[i+1])and(ytank<cubesData[i+2])and(ytank+tank_height>cubesData[i+2])and(xtank<=cubesData[i+1]))or((xtank+tank_width>=cubesData[i+1])and(ytank<cubesData[i+2]+cubewidth)and(ytank+tank_height>cubesData[i+2]+cubewidth)and(xtank<=cubesData[i+1])):
                return True


        if(request=='left'):
            if((xtank+tank_width>=cubesData[i+1]+cubewidth)and(ytank<cubesData[i+2])and(ytank+tank_height>cubesData[i+2])and(xtank<=cubesData[i+1]+cubewidth))or((xtank+tank_width>=cubesData[i+1]+cubewidth)and(ytank<cubesData[i+2]+cubewidth)and(ytank+tank_height>cubesData[i+2]+cubewidth)and(xtank<=cubesData[i+1]+cubewidth)):
                return True


        if(request=='down'):
            if((ytank+tank_height>=cubesData[i+2])and(xtank<cubesData[i+1])and(xtank+tank_width>cubesData[i+1])and(ytank<=cubesData[i+2]))or((ytank+tank_height>=cubesData[i+2])and(xtank<cubesData[i+1]+cubewidth)and(xtank+tank_width>cubesData[i+1]+cubewidth)and(ytank<=cubesData[i+2])):
                return True


        if(request=='up'):
            if((ytank+tank_height>=cubesData[i+2]+cubewidth)and(xtank<cubesData[i+1])and(xtank+tank_width>cubesData[i+1])and(ytank<=cubesData[i+2]+cubewidth))or((ytank+tank_height>=cubesData[i+2]+cubewidth)and(xtank<cubesData[i+1]+cubewidth)and(xtank+tank_width>cubesData[i+1]+cubewidth)and(ytank<=cubesData[i+2]+cubewidth)):
                return True
        i=i+3
    return False






def ShotTouchCube(x,y,cubesData,cubewidth,shot_width,shot_height,way):

    cubesData=list(cubesData)
    i=0

    while(len(cubesData)-3>=i):

        if(x>=cubesData[i+1])and(x<=cubesData[i+1]+cubewidth)and(y>=cubesData[i+2])and(y<=cubesData[i+2]+cubewidth)or(TouchCube(x,y,cubesData,cubewidth,shot_width,shot_height,way)==True):
            return True
        i=i+3
    return False



def listener(Soc):
    Soc.setblocking(False)
    try:
        return Soc.recv(2000)
    except socket.error:
        return None


def main():

    # open socket with client
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(2)
    client_socket, address = server_socket.accept()
    client_socket2, address2 = server_socket.accept()
    # handle requests until user asks to exit
    shot_speed=25
    tankspeed=20
    done = False
    width = 1000
    height = 600
    tankAdown = "tankAdown.png"
    tankAright = "tankAright.png"
    tankAup = "tankAup.png"
    tankAleft = "tankAleft.png"
    tankBdown = "tankBdown.png"
    tankBright = "tankBright.png"
    tankBup = "tankBup.png"
    tankBleft = "tankBleft.png"
    boom="boom.jpg"
    win="win.jpg"
    lose="lose.png"
    cover ="black.png"
    shot="tankBshot.png"
    wallcube = "wallcube.png"
    ironcube="ironcube.jpg"
    isShotA=False
    with open(tankBright, "rb") as imageFile:
        tBr= base64.b64encode(imageFile.read())
    with open(tankBleft, "rb") as imageFile:
        tBl= base64.b64encode(imageFile.read())
    with open(tankBup, "rb") as imageFile:
        tBu= base64.b64encode(imageFile.read())
    with open(tankBdown, "rb") as imageFile:
        tBd= base64.b64encode(imageFile.read())
    with open(tankAright, "rb") as imageFile:
        tAr= base64.b64encode(imageFile.read())
    with open(tankAleft, "rb") as imageFile:
        tAl= base64.b64encode(imageFile.read())
    with open(tankAup, "rb") as imageFile:
        tAu= base64.b64encode(imageFile.read())
    with open(tankAdown, "rb") as imageFile:
        tAd= base64.b64encode(imageFile.read())
    with open(boom, "rb") as imageFile:
        bm= base64.b64encode(imageFile.read())
    with open(win, "rb") as imageFile:
        vic= base64.b64encode(imageFile.read())
    with open(lose, "rb") as imageFile:
        los= base64.b64encode(imageFile.read())
    with open(cover, "rb") as imageFile:
        cov= base64.b64encode(imageFile.read())
    with open(shot, "rb") as imageFile:
        sht= base64.b64encode(imageFile.read())
    with open(wallcube, "rb") as imageFile:
        wcub= base64.b64encode(imageFile.read())
    with open(ironcube, "rb") as imageFile:
        icub= base64.b64encode(imageFile.read())
    cubwidth=40
    picA=tankAleft
    obw=80
    obh=80
    width_shot = 4
    height_shot = 4
    xA=width-obw
    yA=height-obh
    xShotA=260
    yShotA=260
    shotWayA='left'
    wayA='left'
    liveA=True
    isShotB=False
    picB=tankBright
    xB=0
    yB=0
    xShotB=0
    yShotB=0
    width_tank=80
    hight_tank=80
    shotWayB='right'
    wayB='right'
    liveB=True

    cubesData=(wallcube,240,160,wallcube,280,160,wallcube,320,160,wallcube,360,160,wallcube,400,160,wallcube,440,160,wallcube,480,160,wallcube,520,160,wallcube,560,160,wallcube,600,160,wallcube,640,160,wallcube,680,160,wallcube,720,160,wallcube,240,400,wallcube,280,400,wallcube,320,400,wallcube,360,400,wallcube,400,400,wallcube,440,400,wallcube,480,400,wallcube,520,400,wallcube,560,400,wallcube,600,400,wallcube,640,400,wallcube,680,400,wallcube,720,400,wallcube,360,200,wallcube,360,240,wallcube,600,360,wallcube,600,320,wallcube,460,0,wallcube,460,40,wallcube,540,560,wallcube,540,520)
    pictures=(((tBr,tBl,tBu,tBd,tAr,tAl,tAu,tAd,bm,vic,los,cov,sht,width,height,wcub,icub,cubwidth)),(cubesData))
    alldata=((picB,xB,yB,isShotB,xShotB,yShotB,obw,obh,),(picA,xA,yA,isShotA,xShotA,yShotA,obw,obh,))

    Running = True
    client_socket.send(str(pictures))
    client_socket2.send(str(pictures))
    client_socket.send(str(alldata))
    client_socket2.send(str(alldata))
    done=False

    while Running:
        request = listener(client_socket)
        requestfromTank2 = listener(client_socket2)


        #THE BLUE TANK request HANDLE
        if(liveA==False)or(liveB==False):
            Running=False
        if(str(request)!='None')and(liveB==True)and(liveA==True):
            print request
            alldata = list(alldata)
            alldata[0]=list(alldata[0])
            alldata[1]=list(alldata[1])

            #BLUE TANK SHOOT REQUEST
            if (request=='shoot' and alldata[0][3]!=True):

                alldata[0][3]=True
                if(alldata[0][0]==tankBdown):
                    alldata[0][4]=alldata[0][1]+(obw/2)
                    alldata[0][5]=alldata[0][2]+obh-shot_speed
                    shotWayB='down'
                if(alldata[0][0]==tankBright):
                    alldata[0][4]=alldata[0][1]+obw-shot_speed
                    alldata[0][5]=alldata[0][2]+(obh/2)
                    shotWayB='right'
                if(alldata[0][0]==tankBup):
                    alldata[0][4]=alldata[0][1]+(obw/2)
                    alldata[0][5]=alldata[0][2]+0-height_shot+shot_speed
                    shotWayB='up'
                if(alldata[0][0]==tankBleft):
                    alldata[0][4]=alldata[0][1]+0-width_shot+shot_speed
                    alldata[0][5]=alldata[0][2]+(obh/2)
                    shotWayB='left'

            if(alldata[0][3]==True):
                alldata = list(alldata)
                alldata[0]=list(alldata[0])
                if(shotWayB=='down'):
                    if(alldata[0][5]<height):
                         alldata[0][5]=alldata[0][5]+shot_speed
                    else:
                        alldata[0][3]=False
                if(shotWayB=='right'):
                    if(alldata[0][4]<width):
                         alldata[0][4]=alldata[0][4]+shot_speed
                    else:
                        alldata[0][3]=False
                if(shotWayB=='up'):
                    if(alldata[0][5]>=0):
                         alldata[0][5]=alldata[0][5]-shot_speed
                    else:
                        alldata[0][3]=False
                if(shotWayB=='left'):
                    if(alldata[0][4]>=0):
                        alldata[0][4]=alldata[0][4]-shot_speed
                    else:
                        alldata[0][3]=False


                if(ShotTouchCube(alldata[0][4],alldata[0][5],cubesData,cubwidth,width_shot ,height_shot , shotWayB)==True):
                    alldata[0][3]=False

                if(alldata[0][4]>=alldata[1][1])and(alldata[0][4]<=alldata[1][1]+40)and(alldata[0][5]>=alldata[1][2])and(alldata[0][5]<=alldata[1][2]+40):
                    alldata[1][0]=boom
                    liveA=False





            #BLUE TANK MOVMENT REQUEST HANDLE
            if(request=='up'):
                alldata=list(alldata)
                alldata[0] = list(alldata[0])
                alldata[1] = list(alldata[1])

                xtankA=alldata[1][1]
                ytankA=alldata[1][2]


                x = alldata[0][1]
                y = alldata[0][2]
                if ((((y>0)and(y<ytankA))or((y>0)and(y-obh>ytankA))or(((x<=xtankA and x+obw<=xtankA) or (x>=xtankA+obw and x>=xtankA))and(y>0)))and(TouchCube(x,y,cubesData,cubwidth, obw, obh, request)==False))and(alldata[0][0]==tankBup):
                    y = y-tankspeed
                    alldata[0][2] = y
                alldata[0][0]=tankBup

            if(request=='down'):
                alldata=list(alldata)
                alldata[0] = list(alldata[0])
                alldata[1] = list(alldata[1])

                xtankA=alldata[1][1]
                ytankA=alldata[1][2]


                x = alldata[0][1]
                y = alldata[0][2]
                if (((( y < height-obh) and(y>=ytankA+obh))or((y<height-obh)and(y+obh<ytankA))or(((x<=xtankA and x+obw<=xtankA) or (x>=xtankA+obw and x>=xtankA))and(y<height-obh)))and(TouchCube(x,y,cubesData,cubwidth, obw, obh, request)==False))and(alldata[0][0]==tankBdown):
                    y = y+tankspeed
                    alldata[0][2] = y
                alldata[0][0]=tankBdown

            if(request=='right'):
                alldata=list(alldata)
                alldata[0] = list(alldata[0])
                alldata[1] = list(alldata[1])

                xtankA=alldata[1][1]
                ytankA=alldata[1][2]


                x = alldata[0][1]
                y = alldata[0][2]
                if ((((x<width-obw)and(x>=xtankA+obw))or((x<width-obw)and(x+obw<xtankA))or(((y<=ytankA and y+obh<=ytankA) or (y>=ytankA+obh and y>=ytankA))and(x<width-obh)))and(TouchCube(x,y,cubesData,cubwidth, obw, obh, request)==False))and(alldata[0][0]==tankBright):
                    x = x+tankspeed
                    alldata[0][1] = x
                alldata[0][0]=tankBright

            if(request=='left'):
                alldata=list(alldata)
                alldata[0] = list(alldata[0])
                alldata[1] = list(alldata[1])

                xtankA=alldata[1][1]
                ytankA=alldata[1][2]


                x = alldata[0][1]
                y = alldata[0][2]
                if ((((x>0)and(x<xtankA))or((x>0)and(x-obw>xtankA))or(((y<=ytankA and y+obh<=ytankA) or (y>=ytankA+obh and y>=ytankA))and(x>0)))and(TouchCube(x,y,cubesData,cubwidth, obw, obh, request)==False))and(alldata[0][0]==tankBleft):
                    x = x-tankspeed
                    alldata[0][1] = x
                alldata[0][0]=tankBleft


            alldata[1]=tuple(alldata[1])
            alldata[0]=tuple(alldata[0])
            alldata=tuple(alldata)
            send=str(alldata)
            print send
            client_socket.send(send)
            client_socket2.send(send)








        #THE YELLOW TANK request HANDLE
        if(str(requestfromTank2)!='None')and(liveA==True)and(liveB==True):
            alldata=list(alldata)
            alldata[0]=list(alldata[0])
            alldata[1]=list(alldata[1])


            #YELLOW TANK SHOOT REQUEST
            if (requestfromTank2=='shoot' and alldata[1][3]!=True):

                alldata[1][3]=True
                if(alldata[1][0]==tankAdown):
                    alldata[1][4]=alldata[1][1]+(obw/2)
                    alldata[1][5]=alldata[1][2]+obh-shot_speed
                    shotWayA='down'
                if(alldata[1][0]==tankAright):
                    alldata[1][4]=alldata[1][1]+obw-shot_speed
                    alldata[1][5]=alldata[1][2]+(obh/2)
                    shotWayA='right'
                if(alldata[1][0]==tankAup):
                    alldata[1][4]=alldata[1][1]+(obw/2)
                    alldata[1][5]=alldata[1][2]+0-height_shot+shot_speed
                    shotWayA='up'
                if(alldata[1][0]==tankAleft):
                    alldata[1][4]=alldata[1][1]+0-width_shot+shot_speed
                    alldata[1][5]=alldata[1][2]+(obh/2)
                    shotWayA='left'

            if(alldata[1][3]==True):
                alldata = list(alldata)
                alldata[1]=list(alldata[1])
                if(shotWayA=='down'):
                    if(alldata[1][5]<height):
                         alldata[1][5]=alldata[1][5]+shot_speed
                    else:
                        alldata[1][3]=False
                if(shotWayA=='right'):
                    if(alldata[1][4]<width):
                         alldata[1][4]=alldata[1][4]+shot_speed
                    else:
                        alldata[1][3]=False
                if(shotWayA=='up'):
                    if(alldata[1][5]>=0):
                         alldata[1][5]=alldata[1][5]-shot_speed
                    else:
                        alldata[1][3]=False
                if(shotWayA=='left'):
                    if(alldata[1][4]>=0):
                        alldata[1][4]=alldata[1][4]-shot_speed
                    else:
                        alldata[1][3]=False


                if(ShotTouchCube(alldata[1][4],alldata[1][5],cubesData,cubwidth,width_shot ,height_shot , shotWayB)==True):
                    alldata[1][3]=False

                if(alldata[1][4]>=alldata[0][1])and(alldata[1][4]<=alldata[0][1]+obw)and(alldata[1][5]>=alldata[0][2])and(alldata[1][5]<=alldata[0][2]+obh):
                    alldata[0][0]=boom
                    liveB=False


            #YELLOW TANK MOVMENT REQUEST HANDLE
            if(requestfromTank2=='up'):
                alldata=list(alldata)
                alldata[0] = list(alldata[0])
                alldata[1] = list(alldata[1])

                xtankB=alldata[0][1]
                ytankB=alldata[0][2]


                x = alldata[1][1]
                y = alldata[1][2]
                if ((((y>0)and(y<ytankB))or((y>0)and(y-obh>ytankB))or(((x<=xtankB and x+obw<=xtankB) or (x>=xtankB+obw and x>=xtankB))and(y>0)))and(TouchCube(x,y,cubesData,cubwidth, obw, obh, requestfromTank2)==False))and(alldata[1][0]==tankAup):
                    y = y-tankspeed
                    alldata[1][2] = y
                alldata[1][0]=tankAup

            if(requestfromTank2=='down'):
                alldata=list(alldata)
                alldata[0] = list(alldata[0])
                alldata[1] = list(alldata[1])

                xtankB=alldata[0][1]
                ytankB=alldata[0][2]


                x = alldata[1][1]
                y = alldata[1][2]
                if ((((y<height-obh)and(y>=ytankB+obh))or((y<height-obh)and(y+obh<ytankB))or(((x<=xtankB and x+obw<=xtankB) or (x>=xtankB+obw and x>=xtankB))and(y<height-obh)))and(TouchCube(x,y,cubesData,cubwidth, obw, obh, requestfromTank2)==False))and(alldata[1][0]==tankAdown):
                    y = y+tankspeed
                    alldata[1][2] = y
                alldata[1][0]=tankAdown

            if(requestfromTank2=='right'):
                alldata=list(alldata)
                alldata[0] = list(alldata[0])
                alldata[1] = list(alldata[1])

                xtankB=alldata[0][1]
                ytankB=alldata[0][2]


                x = alldata[1][1]
                y = alldata[1][2]
                if ((((x<width-obw)and(x>=xtankB+obw))or((x<width-obw)and(x+obw<xtankB))or(((y<=ytankB and y+obh<=ytankB) or (y>=ytankB+obh and y>=ytankB))and(x<width-obw)))and(TouchCube(x,y,cubesData,cubwidth, obw, obh, requestfromTank2)==False))and(alldata[1][0]==tankAright):
                    x = x+tankspeed
                    alldata[1][1] = x
                alldata[1][0]=tankAright

            if(requestfromTank2=='left'):
                alldata=list(alldata)
                alldata[0] = list(alldata[0])
                alldata[1] = list(alldata[1])

                xtankB=alldata[0][1]
                ytankB=alldata[0][2]


                x = alldata[1][1]
                y = alldata[1][2]
                if ((((x>0)and(x<xtankB))or((x>0)and(x-obw>xtankB))or(((y<=ytankB and y+obh<=ytankB) or (y>=ytankB+obh and y>=ytankB))and(x>0)))and(TouchCube(x,y,cubesData,cubwidth, obw, obh, requestfromTank2)==False))and(alldata[1][0]==tankAleft):
                    x = x-tankspeed
                    alldata[1][1] = x
                alldata[1][0]=tankAleft


            alldata[1]=tuple(alldata[1])
            alldata[0]=tuple(alldata[0])
            alldata=tuple(alldata)
            send=str(alldata)
            print send
            client_socket.send(send)
            client_socket2.send(send)


        #TANK 1(THE BLUE SHOOT WITHOUT MOVEMENTS)
        if(str(request)=="None")and(liveB==True)and(liveA==True):
            alldata = list(alldata)
            alldata[0]=list(alldata[0])
            alldata[1]=list(alldata[1])
            if(alldata[0][3]==True):
                alldata=list(alldata)
                alldata[0] = list(alldata[0])
                if(shotWayB=='down'):
                    if(alldata[0][5]<height):
                         alldata[0][5]=alldata[0][5]+shot_speed
                    else:
                        alldata[0][3]=False
                if(shotWayB=='right'):
                    if(alldata[0][4]<width):
                         alldata[0][4]=alldata[0][4]+shot_speed
                    else:
                        alldata[0][3]=False
                if(shotWayB=='up'):
                    if(alldata[0][5]>=0):
                         alldata[0][5]=alldata[0][5]-shot_speed
                    else:
                        alldata[0][3]=False
                if(shotWayB=='left'):
                    if(alldata[0][4]>=0):
                         alldata[0][4]=alldata[0][4]-shot_speed
                    else:
                        alldata[0][3]=False
                if(ShotTouchCube(alldata[0][4],alldata[0][5],cubesData,cubwidth,width_shot ,height_shot , shotWayB)==True):
                    alldata[0][3]=False

                if(alldata[0][4]>=alldata[1][1])and(alldata[0][4]<=alldata[1][1]+obw)and(alldata[0][5]>=alldata[1][2])and(alldata[0][5]<=alldata[1][2]+obh):
                    alldata[1][0]=boom
                    liveA=False


                alldata[0]=tuple(alldata[0])
                alldata[1]=tuple(alldata[1])
                alldata=tuple(alldata)
                send=str(alldata)
                client_socket.send(send)
                client_socket2.send(send)


        #TANK 2(THE YELLOW SHOOT WITHOUT MOVEMENTS)
        if(str(requestfromTank2)=="None")and(liveA==True)and(liveB==True):
            alldata = list(alldata)
            alldata[0]=list(alldata[0])
            alldata[1]=list(alldata[1])
            if(alldata[1][3]==True):
                alldata=list(alldata)
                alldata[1] = list(alldata[1])
                if(shotWayA=='down'):
                    if(alldata[1][5]<height):
                         alldata[1][5]=alldata[1][5]+shot_speed
                    else:
                        alldata[1][3]=False
                if(shotWayA=='right'):
                    if(alldata[1][4]<width):
                         alldata[1][4]=alldata[1][4]+shot_speed
                    else:
                        alldata[1][3]=False
                if(shotWayA=='up'):
                    if(alldata[1][5]>=0):
                         alldata[1][5]=alldata[1][5]-shot_speed
                    else:
                        alldata[1][3]=False
                if(shotWayA=='left'):
                    if(alldata[1][4]>=0):
                         alldata[1][4]=alldata[1][4]-shot_speed
                    else:
                        alldata[1][3]=False


                if(ShotTouchCube(alldata[1][4],alldata[1][5],cubesData,cubwidth,width_shot ,height_shot , shotWayB)==True):
                    alldata[1][3]=False

                if(alldata[1][4]>=alldata[0][1])and(alldata[1][4]<=alldata[0][1]+obw)and(alldata[1][5]>=alldata[0][2])and(alldata[1][5]<=alldata[0][2]+obh):
                    alldata[0][0]=boom
                    liveB=False



                alldata[0]=tuple(alldata[0])
                alldata[1]=tuple(alldata[1])
                alldata=tuple(alldata)
                send=str(alldata)
                #print send
                client_socket.send(send)
                client_socket2.send(send)


        #if THE YELLOW TANK DIES
        if(liveA==False):
            alldata = list(alldata)
            alldata[0]=list(alldata[0])
            alldata[1]=list(alldata[1])

            alldata[0][0]=win
            alldata[0][1]=250
            alldata[0][2]=100
            alldata[0][6]=500
            alldata[0][7]=300
            alldata[1][0]=lose
            alldata[1][1]=250
            alldata[1][2]=100
            alldata[1][6]=500
            alldata[1][7]=300
            alldata[0][3]=False
            alldata[1][3]=False

            alldata[0]=tuple(alldata[0])
            alldata[1]=tuple(alldata[1])
            alldata=tuple(alldata)
            send=str(alldata)
            #print send
            time.sleep(1)
            client_socket.send(send)
            client_socket2.send(send)


        #IF THE BLUE TANK DIES
        if(liveB==False):
            alldata = list(alldata)
            alldata[0]=list(alldata[0])
            alldata[1]=list(alldata[1])

            alldata[1][0]=win
            alldata[1][1]=250
            alldata[1][2]=100
            alldata[1][6]=500
            alldata[1][7]=300
            alldata[0][0]=lose
            alldata[0][1]=250
            alldata[0][2]=100
            alldata[0][6]=500
            alldata[0][7]=300
            alldata[0][3]=False
            alldata[1][3]=False

            alldata[0]=tuple(alldata[0])
            alldata[1]=tuple(alldata[1])
            alldata=tuple(alldata)
            send=str(alldata)
            #print send
            time.sleep(1)
            client_socket.send(send)
            client_socket2.send(send)

        time.sleep(0.035)
    end=raw_input()
    client_socket.close()
    server_socket.close()
if __name__ == '__main__':
    main()


