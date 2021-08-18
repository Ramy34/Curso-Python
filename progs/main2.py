from sys import path
#agregar el path de la carpeta extra
path.append('..\\packages')

from extra.iota import FunI
print(FunI())

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.good.best.tau import FunT

print(sig.FunS())
print(alp.FunA())
print(FunT())