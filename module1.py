from random import *

sonastik={}
                       
def Loe_fail(fail:str):
    file=open(fail,'r',encoding="utf-8-sig")
    for line in file:
        k, v=line.strip().split('-')
        sonastik[k.strip()] = v.strip()
    return (sonastik)

def Loe_vastupidi(f):
    sonastik = {}
    file=open(f, "r", encoding="utf-8-sig")
    for line in file:
        k, v=line.split("-")
        sonastik[v.strip()] = k.strip()
    file.close()
    return sonastik

def Leia_pealinn(fail:dict):
    riik=input("Sisesta riik: ")
    pealinn=fail.get(riik)
    print(f"See on pealinn: {pealinn}\n")
    return pealinn

def Leia_riik(fail:dict):
    pealinn=input("Sisestage pealinn: ")
    riik=fail.get(pealinn)
    print(f"See on riik: {riik}\n")
    return riik

def Lisa(fail:dict):
    riik=input("Sisesta riik: ")
    pealinn=input("Sisestage pealinn: ")
    fail.update({riik:pealinn})
    return fail

def parandamine(fail:dict):
    p=input("Sisestage riik, mida soovite parandada: ")
    fail.pop(p)
    riik=input("Sisesta riik: ")
    pealinn=input("Sisestage pealinn: ")
    fail.update({riik:pealinn})
    return fail

def test(fail:dict):
    riik=list(fail.keys())
    pealinn=list(fail.values())
    kord=int(input("Mitu korda sa tahad mängida? "))
    kokku=0
    for i in range(kord):
        ans=int(input("Kas arvame pealinnad(1) või riigid(2)?"))
        if ans==1:
            rand=choice(riik)
            ind=riik.index(rand)
            print(pealinn[ind])
            sona=input("Sisesta: ")
            if sona in riik[ind]:
                print("Õige")
                kokku+=1
            else:
                print("Vale")
        elif ans==2:
            rand=choice(pealinn)
            ind=pealinn.index(rand)
            print(riik[ind])
            sona=input("Sisesta: ")
            if sona in pealinn[ind]:
                print("Õige")
                kokku+=1
            else:
                print("Vale")
    print(f"{round(kokku/kord*100,1)}% vastused on õige ja {round(100-kokku/kord*100,1)}% on vale")