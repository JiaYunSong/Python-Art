from turtle import *
import math

speed("fastest")

width(3)            #圆
kkk=30
while kkk>0:
    width(kkk)
    setheading(90)
    penup()
    if kkk==30:
        color('#F7F8E0')
    elif kkk==5:
        color('#F2F5A9')
    elif kkk==1:
        color('#FF8000')
    k=700
    dd=0
    while k>=15:
        if k<80 and dd==0:
            if kkk==30:
                color('#F7F8E0')
                kkk=5
            elif kkk==5:
                color('#F3F781')
                kkk=1
            elif kkk==1:
                color('#DF7401')
                kkk=0
            dd=1
        forward(k)
        left(90)
        pendown()
        circle(k,360,int(k*3/15))
        penup()
        right(90)
        back(k)
        k=k-k/4

kkk=11              #星芒
while kkk>0:
    width(kkk)
    setheading(0)
    penup()
    if kkk==11:
        color('#F8EFFB')
        kkk=4
    elif kkk==4:
        color('#F6CEF5')
        kkk=1
    elif kkk==1:
        color('#D358F7')
        kkk=0
    xi1=1100         #外边长
    xip=3           #内边长比例
    step=6          #步数
    j=2**step
    
    i1=100
    istep=(xi1-i1)/step

    if kkk==4:
        i1+=istep
        j=j/2
        step-=1
    
    while step>0:
        i2=i1/((xip-1)/step+1)
        k=360       #记录旋转次数
        j*=2
        xcos=math.cos(math.radians(360/j))
        xsin=math.sin(math.radians(360/j))
        long=(i1**2+i2**2-2*i1*i2*xcos)**0.5
        xita=math.degrees(math.asin(xsin*i2/long))
        close=180-2*(360/j+xita)
        forward(i1)
        pendown()
        left(xita)
        while k > 0:
            left(180-2*xita)
            forward(long)
            left(-close)
            forward(long)
            k-=360/j*2
        penup()
        left(180-xita)
        forward(i1)
        left(180)
        i1+=istep
        j=j/4
        step-=1

kkk=7                   #蓝色三角
while kkk>0:
    setheading(-15)
    width(kkk)
    if kkk==7:
        kkk=2
        color('#CEF6F5')
    elif kkk==2:
        kkk=0
        color('#00BFFF')
    k=300
    while k>=5:
        penup()
        left(-150)
        forward(k*2*2/(3**(1/2)))
        pendown()
        left(150)
        forward(k)
        left(120)
        forward(k)
        left(120)
        forward(k)
        left(150)
        penup()
        forward(k*2*2/(3**(1/2)))
        left(50)
        k=k-k/4

kkk=7                   #红色三角
while kkk>0:
    setheading(165)
    width(kkk)
    if kkk==7:
        kkk=2
        color('#F8E0E0')
    elif kkk==2:
        kkk=0
        color('#FA8258')
    k=300
    while k>=5:
        penup()
        left(-150)
        forward(k*2*2/(3**(1/2)))
        pendown()
        left(150)
        forward(k)
        left(120)
        forward(k)
        left(120)
        forward(k)
        left(150)
        penup()
        forward(k*2*2/(3**(1/2)))
        left(50)
        k=k-k/4

penup()
forward(700)

x=input('按任意键结束……\nCopyleft.Rsmx.2019-06-17')
