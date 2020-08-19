import turtle as t

def box(x,y,color):
    t.speed('normal')
    t.color(color)
    t.begin_fill() # 색깔채우기, 시작부분 코드
    t.fd(x) #forword와 같음
    t.left(90)
    t.fd(y)
    t.left(90)
    t.fd(x)
    t.left(90)
    t.fd(y)
    t.end_fill()
box(100,50,'red')
input("")