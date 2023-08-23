import math

def suma(c1,c2):
    suma_r=c1[0]+c2[0]
    suma_c=c1[1]+c2[1]
    return (suma_r,suma_c)

def mult(c1,c2):
    mult_r= c1[0]*c2[0]-c1[1]*c2[1]
    mult_c = (c1[0]*c2[1])+(c1[1]*c2[0])
    return (mult_r,mult_c)

def resta(c1,c2):
    resta_r= c1[0]-c2[0]
    resta_c= c1[1]-c2[1]
    return (resta_r,resta_c)

def divi(c1,c2):
    divi_r = ((c1[0]*c2[0])+(c1[1]*c2[1]))/(c2[0]**2+c2[1]**2)
    divi_c = ((c1[1]*c2[0])-(c1[0]*c2[1]))/(c2[0]**2+c2[1]**2)
    return (divi_r,divi_c)

def modulo(c1):
    modulo_rc=(c1[0]**2+c1[1]**2)**0.5
    return modulo_rc

def conjugado(c1):
    conjugado_rc=c1[0],c1[1]

    if c1[1]<0 or c1[1]>0:
        return c1[0],-c1[1]


def polar(c1):
    z=(c1[0]**2+c1[1]**2)**0.5
    a= math.atan(c1[1]/c1[0])
    polar_r=z*math.cos(a)
    polar_c=z*math.sin(a)
    return (polar_r,polar_c)



print(suma((3,2),(-5,5.2)))
print(suma((7, 3), (5.5, 1.2)))

print(mult((3,2),(-5,5.2)))
print(mult((7, 3), (5.5, 1.2)))

print(resta((3,2),(-5,5.2)))
print(resta((7, 3), (5.5, 1.2)))

print(divi((3,2),(-5,5.2)))
print(divi((7, 3), (5.5, 1.2)))

print(modulo((3,2)))
print(modulo((7, 3)))

print(conjugado((3,2)))
print(conjugado((7, 3)))

print(polar((3, 2)))
print(polar((7, 3)))
print(polar((5, -5)))