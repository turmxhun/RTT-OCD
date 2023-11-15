"""Másodokú egyenlet megoldása pythonban"""

import math

class egyenletMegoldo():
    """másodfokú egyenlet megoldó metódus"""
    def masodfokuEgyenletMegoldo(self,a,b,c):
        if type(a) not in[int, float] or type(b) not in[int, float] or type(c) not in[int, float]:
            raise TypeError('Csak int vagy float tipus lehet')

        d = math.pow(b,2)-(4*a*c)
        if d < 0:
            return None, None
        return (-b + math.sqrt(d))/(2*a), (-b - math.sqrt(d))/(2*a)

    def feladatMegoldo(self,a,b,c):
        """feladatmegodó metódus"""
        e = egyenletMegoldo()
        x1,x2 = e.masodfokuEgyenletMegoldo(a,b,c)

        print(f"{a}x^2 + {b}x + {c} = 0")

        if(x1 is None) and (x2 is None):
            print("Nincs megoldás")
        elif x1 == x2:
            print(f"Egy megoldás van: {x1}")
        else:
            print(f"Két megoldás van: x1={x1}, x2={x2}")

    #feladatMegoldo(1,2,8)
    #feladatMegoldo(1, -14, 49)
    #feladatMegoldo("alma", 1, "körte")