from collections import Counter
evaluar = """título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources 
provides the promise of capturing unprecedented details of large-scale complex systems. 
However, the specialized knowledge required for developing such ABMs creates barriers to 
wider adoption and utilization. Here we present our experiences in developing an initial 
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""

x = evaluar.split("resumen")

titulo = x[0].split(" ")

if len(titulo)>10:
    print("El titulo es muy largo")
else:
    print("El titulo esta ok")

cuerpo = x[1].split(".")
facil=0
aceptable=0
dificil=0
muy_dificil=0
for elem in cuerpo:
    oracion = elem.split(" ")
    if (len(oracion)<13):
        facil = facil +1
    elif (len(oracion)>12 & len(oracion)<18):
        aceptable = aceptable+1
    elif (len(oracion)>17 & len(oracion)<26):
        dificil = dificil + 1
    else:
        muy_dificil=muy_dificil+1
    
print("""Hubo {} oraciones faciles de leer. 
    {} oraciones aceptables. 
    {} oraciones dificiles. 
    {} oraciones muy dificiles""".format(facil,aceptable,dificil,muy_dificil))