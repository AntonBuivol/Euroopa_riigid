from module1 import *
while True:
    v=int(input("1-Näita riigid ja pealinnad\n2-Otsige pealinn riigi järgi\n3-Otsige riigi pealinna järgi\n4-Lisa riik ja pealinn\n5-Parandamine\n6-Test\n"))
    if v==1:
        asd=Loe_fail("riigid_pealinnd.txt")
        print(asd)
    if v==2:
        asd=Loe_fail("riigid_pealinnd.txt")
        x=Leia_pealinn(asd)
    elif v==3:
        asd=Loe_vastupidi("riigid_pealinnd.txt")
        x=Leia_riik(asd)
    elif v==4:
        asd=Loe_fail("riigid_pealinnd.txt")
        x=Lisa(asd)
        print(asd)
    elif v==5:
        asd=Loe_fail("riigid_pealinnd.txt")
        x=parandamine(asd)
        print(x)
    elif v==6:
        asd=Loe_fail("riigid_pealinnd.txt")
        x=test(asd)
        print(x)
    else:
        v=int(input("1-Näita riigid ja pealinnad\n2-Otsige pealinna\n3-Leidke riik\n4-Lisa riik ja pealinn\n5-Parandamine\n6-Test\n"))

