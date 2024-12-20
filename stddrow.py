import stddraw


def draw_triangle(x0,y0,x1,y1,x2,y2):
    stddraw.line(x0,y0,x1,y1)
    stddraw.line(x1,y1,x2,y2)
    stddraw.line(x2,y2,x0,y0)
    