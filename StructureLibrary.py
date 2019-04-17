import math

"""

StructureLibrary.py

"""
'''
Library of structures that organizes the points of the various structures

Method call:
atomsArray, numOfAtomTypes = CaB6(numx, numy, numz)
where numx, numy, and numz are the dimensions for the structure
'''
class StructureLibrary:
    '''test Ca [type 1] on corners with a 6 atom diamond shape of B [type 2]
    in the middle'''
    def CaB6(numcellx, numcelly, numcellz):
        xpos, ypos, zpos, typepos = ([] for i in range(4))
        Bxpos, Bypos, Bzpos, Btypepos = ([] for i in range(4))
        acell = 1
        # Corner
        xpos.append(0)
        ypos.append(0)
        zpos.append(0)
        typepos.append(1)

        # Face
        xpos.append(acell/2)
        ypos.append(acell/2)
        zpos.append(acell/4)
        typepos.append(2)

        xpos.append(acell/2)
        ypos.append(acell/2)
        zpos.append((3/4)*acell)
        typepos.append(2)
        xpos.append(acell/4)
        ypos.append(acell/2)
        zpos.append((1/2)*acell)
        typepos.append(2)
        xpos.append(acell/2)
        ypos.append(acell/4)
        zpos.append((1/2)*acell)
        typepos.append(2)
        xpos.append((3/4)*acell)
        ypos.append(acell/2)
        zpos.append((1/2)*acell)
        typepos.append(2)
        xpos.append(acell/2)
        ypos.append((3/4)*acell)
        zpos.append((1/2)*acell)
        typepos.append(2)

        # Set iteration numbers and counter
        # now being passed as a parameter
        atnum=0

        #cast typepos to set to get the unique values then do len to get count
        typeset = set(typepos)
        typecount = len(typeset)


        # Loop through and create layers
        for i1 in range(1,numcellx+1):
            for i2 in range(1,numcelly+1):
                for i3 in range(1,numcellz+1):
                    for i in range(7):
                        atnum=atnum+1
                        Bxpos.append(xpos[i]+i1*acell)
                        Bypos.append(ypos[i]+i2*acell)
                        Bzpos.append(zpos[i]+i3*acell)
                        Btypepos.append(typepos[i])
        # rearrange the output
        finalRet = []
        for x in range(atnum):
            points = [Bxpos[x], Bypos[x],Bzpos[x],Btypepos[x]]
            finalRet.append(points)
        return finalRet, typecount
    # data, count = CaB6(2, 2, 2)
    # file = open("CaB6.xyz","w")
    # file.write("{}\r\n".format(len(data)))
    # file.write('Atoms\n')
    # print("num types: " + str(count))
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()
    '''test Al(1) in corner with B(2) atoms on faces parallel to each other'''

    def AlB2(numcellx, numcelly, numcellz):
        xpos, ypos, zpos, typepos = ([] for i in range(4))
        Bxpos, Bypos, Bzpos, Btypepos = ([] for i in range(4))
        acell= math.sqrt(2)
        # Corner
        xpos.append(0)
        ypos.append(0)
        zpos.append(0)
        typepos.append(1)

        # Face
        xpos.append(0)
        ypos.append(acell/2)
        zpos.append(acell/2)
        typepos.append(2)


        atnum=0

        #cast typepos to set to get the unique values then do len to get count
        typeset = set(typepos)
        typecount = len(typeset)

        for i1 in range(1,numcellx + 1):
            for i2 in range(1,numcelly + 1):
                for i3 in range(1,numcellz + 1):
                    for i in range(2):
                        atnum=atnum+1
                        Bxpos.append(xpos[i]+i1*acell)
                        Bypos.append(ypos[i]+i2*acell)
                        Bzpos.append(zpos[i]+i3*acell)
                        Btypepos.append(typepos[i])
        # rearrange the output
        finalRet = []
        print(atnum)
        for x in range(atnum):
            points = [Bxpos[x], Bypos[x],Bzpos[x],Btypepos[x]]
            finalRet.append(points)
        return finalRet, typecount

    # data, count = AlB2(3, 3, 3)
    # print("num atoms: " + str(len(data)))
    # print("num types: " + str(count))
    # file = open("AlB2.xyz","w")
    # file.write("{}\r\n".format(len(data)))
    # file.write('Atoms\n')
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()


    '''test BCC with Bs'''
    def BCC(numcellx, numcelly, numcellz):
        xpos, ypos, zpos = ([] for i in range(3))
        Bxpos, Bypos, Bzpos = ([] for i in range(3))
        acell=(math.sqrt(4)/3)

        xpos.append(0)
        ypos.append(0)
        zpos.append(0)

        xpos.append(acell/2)
        ypos.append(acell/2)
        zpos.append(acell/2)

        xpos.append(0)
        ypos.append(acell)
        zpos.append(acell)

        xpos.append(acell)
        ypos.append(0)
        zpos.append(acell)

        atnum=0

        for i1 in range(1,numcellx + 1):
            for i2 in range(1,numcelly + 1):
                for i3 in range(1,numcellz + 1):
                    for i in range(4):
                        atnum=atnum+1
                        Bxpos.append(xpos[i]+i1*acell)
                        Bypos.append(ypos[i]+i2*acell)
                        Bzpos.append(zpos[i]+i3*acell)
        finalRet = []
        typeatom = 1
        print(atnum)
        for x in range(atnum):
            points = [Bxpos[x], Bypos[x],Bzpos[x],typeatom]
            finalRet.append(points)
        #harded coded since there is only one type of atom in this structure
        return finalRet, 1

    # data, count = BCC(3, 3, 3)
    # print("num atoms: " + str(len(data)))
    # print("num types: " + str(count))
    # file = open("bcc.xyz","w")
    # file.write("{}\r\n".format(len(data)))
    # file.write('Atoms\n')
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()

    '''test Au(type 1) in corner and Cu (type 2) on faces'''
    def Cu3Au(numcellx, numcelly, numcellz):
        xpos, ypos, zpos, typepos = ([] for i in range(4))
        Bxpos, Bypos, Bzpos, Btypepos = ([] for i in range(4))
        acell=math.sqrt(2)

        # Corner
        xpos.append(0)
        ypos.append(0)
        zpos.append(0)
        typepos.append(1)

        # Face
        xpos.append(acell/2)
        ypos.append(acell/2)
        zpos.append(0)
        typepos.append(2)
        # Face
        xpos.append(0)
        ypos.append(acell/2)
        zpos.append(acell/2)
        typepos.append(2)
        # Face
        xpos.append(acell/2)
        ypos.append(0)
        zpos.append(acell/2)
        typepos.append(2)

        #cast typepos to set to get the unique values then do len to get count
        typeset = set(typepos)
        typecount = len(typeset)
        atnum=0

        for i1 in range(1,numcellx+1):
            for i2 in range(1,numcelly+1):
                for i3 in range(1,numcellz+1):
                    for i in range(4):
                           atnum=atnum+1
                           Bxpos.append(xpos[i]+i1*acell)
                           Bypos.append(ypos[i]+i2*acell)
                           Bzpos.append(zpos[i]+i3*acell)
                           Btypepos.append(typepos[i])
        # rearrange the output
        print(atnum)
        finalRet = []
        for x in range(atnum):
            points = [Bxpos[x], Bypos[x],Bzpos[x],Btypepos[x]]
            finalRet.append(points)
        return finalRet, typecount

    # data, count = Cu3Au(3, 3, 3)
    # print("num atoms: " + str(len(data)))
    # print("num types: " + str(count))
    # file = open("Cu3Au.xyz","w")
    # file.write("{}\r\n".format(len(data)))
    # file.write('Atoms\n')
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()

    ''' test Diamond with Bs '''
    def Diamond(numcellx, numcelly, numcellz):
        xpos, ypos, zpos, typepos = ([] for i in range(4))
        Bxpos, Bypos, Bzpos, Btypepos = ([] for i in range(4))
        acell=(math.sqrt(4)/3)

        # Corner
        xpos.append(0)
        ypos.append(0)
        zpos.append(0)
        typepos.append(1)

        # Face
        xpos.append(acell/2)
        ypos.append(acell/2)
        zpos.append(0)
        typepos.append(1)

        # Face
        xpos.append(0)
        ypos.append(acell/2)
        zpos.append(acell/2)
        typepos.append(1)

        # Face
        xpos.append(acell/2)
        ypos.append(0)
        zpos.append(acell/2)
        typepos.append(1)

        # Diamond
        xpos.append((3/4)*acell)
        ypos.append((1/4)*acell)
        zpos.append((1/4)*acell)
        typepos.append(1)

        # Diamond
        xpos.append((1/4)*acell)
        ypos.append((3/4)*acell)
        zpos.append((1/4)*acell)
        typepos.append(1)

        # Diamond
        xpos.append((1/4)*acell)
        ypos.append((1/4)*acell)
        zpos.append((3/4)*acell)
        typepos.append(1)

        # Diamond
        xpos.append((3/4)*acell)
        ypos.append((3/4)*acell)
        zpos.append((3/4)*acell)
        typepos.append(1)


        #cast typepos to set to get the unique values then do len to get count
        typeset = set(typepos)
        typecount = len(typeset)
        atnum=0

        for i1 in range(1,numcellx+1):
            for i2 in range(1,numcelly+1):
                for i3 in range(1,numcellz+1):
                    for i in range(8):
                        atnum=atnum+1
                        Bxpos.append(xpos[i]+i1*acell)
                        Bypos.append(ypos[i]+i2*acell)
                        Bzpos.append(zpos[i]+i3*acell)
                        Btypepos.append(typepos[i])
        # rearrange the output
        print(atnum)
        finalRet = []
        for x in range(atnum):
            points = [Bxpos[x], Bypos[x],Bzpos[x],Btypepos[x]]
            finalRet.append(points)
        return finalRet, typecount

    # data, count = Diamond(3, 3, 3)
    # print("num atoms: " + str(len(data)))
    # print("num types: " + str(count))
    # file = open("diamond.xyz","w")
    # file.write("{}\r\n".format(len(data)))
    # file.write('Atoms\n')
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()

    ''' Laves face structure '''
    def Laves(numcellx, numcelly, numcellz):
        xpos, ypos, zpos = ([] for i in range(3))
        Bxpos, Bypos, Bzpos = ([] for i in range(3))
        a=1.0
        b=a*math.sqrt(3.0)/4.0/1.11
        # altenate
        xpos.append(0)
        ypos.append(0)
        zpos.append(0)

        xpos.append(a/4.0)
        ypos.append(a/4.0)
        zpos.append(a/4.0)

        xpos.append(a/2.0)
        ypos.append(a/2.0)
        zpos.append(0)

        xpos.append(0)
        ypos.append(a/2.0)
        zpos.append(a/2.0)

        xpos.append(a/2.0)
        ypos.append(0)
        zpos.append(a/2.0)

        xpos.append(3.0*a/4.0)
        ypos.append(3.0*a/4.0)
        zpos.append(a/4.0)

        xpos.append(a/4.0)
        ypos.append(3.0*a/4.0)
        zpos.append(3.0*a/4.0)

        xpos.append(3.0*a/4.0)
        ypos.append(a/4.0)
        zpos.append(3.0*a/4.0)

        xpos.append(3.0/4.0*a-b/math.sqrt(8))
        ypos.append(3.0/4.0*a-b/math.sqrt(8))
        zpos.append(3.0/4.0*a-b/math.sqrt(8))

        xpos.append(3.0/4.0*a-b/math.sqrt(8))
        ypos.append(3.0/4.0*a+b/math.sqrt(8))
        zpos.append(3.0/4.0*a+b/math.sqrt(8))

        xpos.append(3.0/4.0*a+b/math.sqrt(8))
        ypos.append(3.0/4.0*a-b/math.sqrt(8))
        zpos.append(3.0/4.0*a+b/math.sqrt(8))

        xpos.append(3.0/4.0*a+b/math.sqrt(8))
        ypos.append(3.0/4.0*a+b/math.sqrt(8))
        zpos.append(3.0/4.0*a-b/math.sqrt(8))

        xpos.append(xpos[7+1]-a/2.0)
        xpos.append(xpos[7+2]-a/2.0)
        xpos.append(xpos[7+3]-a/2.0)
        xpos.append(xpos[7+4]-a/2.0)
        ypos.append(ypos[7+1]-a/2.0)
        ypos.append(ypos[7+2]-a/2.0)
        ypos.append(ypos[7+3]-a/2.0)
        ypos.append(ypos[7+4]-a/2.0)
        zpos.append(zpos[7+1])
        zpos.append(zpos[7+2])
        zpos.append(zpos[7+3])
        zpos.append(zpos[7+4])

        xpos.append(xpos[7+1])
        xpos.append(xpos[7+2])
        xpos.append(xpos[7+3])
        xpos.append(xpos[7+4])
        ypos.append(ypos[7+1]-a/2.0)
        ypos.append(ypos[7+2]-a/2.0)
        ypos.append(ypos[7+3]-a/2.0)
        ypos.append(ypos[7+4]-a/2.0)
        zpos.append(zpos[7+1]-a/2.0)
        zpos.append(zpos[7+2]-a/2.0)
        zpos.append(zpos[7+3]-a/2.0)
        zpos.append(zpos[7+4]-a/2.0)

        xpos.append(xpos[7+1]-a/2.0)
        xpos.append(xpos[7+2]-a/2.0)
        xpos.append(xpos[7+3]-a/2.0)
        xpos.append(xpos[7+4]-a/2.0)
        ypos.append(ypos[7+1])
        ypos.append(ypos[7+2])
        ypos.append(ypos[7+3])
        ypos.append(ypos[7+4])
        zpos.append(zpos[7+1]-a/2.0)
        zpos.append(zpos[7+2]-a/2.0)
        zpos.append(zpos[7+3]-a/2.0)
        zpos.append(zpos[7+4]-a/2.0)

        typepos = []
        Btypepos = []
        for i in range(24):
            if(i<=7):
                typepos.append(1)
            else:
                typepos.append(1)

        nt=0
        #cast typepos to set to get the unique values then do len to get count
        typeset = set(typepos)
        typecount = len(typeset)

        for nx in range(0,numcellx+1):
            for ny in range(0,numcelly+1):
                for nz in range(0,numcellz+1):
                    for i in range(24):
                        nt=nt+1
                        Bxpos.append(xpos[i]+nx*a)
                        Bypos.append(ypos[i]+ny*a)
                        Bzpos.append(zpos[i]+nz*a)
                        Btypepos.append(typepos[i])
        # rearrange the output
        print(nt)
        finalRet = []
        for x in range(nt):
            points = [Bxpos[x], Bypos[x],Bzpos[x],Btypepos[x]]
            finalRet.append(points)
        return finalRet, typecount

    # data, count = Laves(1, 1, 2)
    # print("num atoms: " + str(len(data)))
    # print("num types: " + str(count))
    # file = open("laves.xyz","w")
    # file.write("{}\r\n".format(len(data)))
    # file.write('Atoms\n')
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()

    def SC(numcellx, numcelly, numcellz):
        #test SC with Bs

        xpos, ypos, zpos = ([] for i in range(3))
        Bxpos, Bypos, Bzpos = ([] for i in range(3))
        acell=(1)

        xpos.append(0)
        ypos.append(0)
        zpos.append(0)

        xpos.append(0)
        ypos.append(acell)
        zpos.append(acell)

        xpos.append(acell)
        ypos.append(0)
        zpos.append(acell)

        xpos.append(acell)
        ypos.append(acell)
        zpos.append(acell)

        atnum=0

        for i1 in range(1,numcellx+1):
            for i2 in range(1,numcelly+1):
                for i3 in range(1,numcellz+1):
                    for i in range(4):
                       atnum=atnum+1
                       Bxpos.append(xpos[i]+i1*acell)
                       Bypos.append(ypos[i]+i2*acell)
                       Bzpos.append(zpos[i]+i3*acell)

        finalRet = []
        typeatom = 1
        print(atnum)
        for x in range(atnum):
            points = [Bxpos[x], Bypos[x],Bzpos[x],typeatom]
            finalRet.append(points)
        #hard coded because ther is only one type of atom in the structure
        return finalRet, 1

    # data, count = SC(2, 2, 2)
    # print("num atoms: " + str(len(data)))
    # print("num types: " + str(count))
    # file = open("sc.xyz","w")
    # file.write("{}\r\n".format(24))
    # file.write('Atoms\n')
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()

    #The available code for this one is incorrect
    def MgCu2(numcellx, numcelly, numcellz):
        a=1.0
        b=a*math.sqrt(3.0)/4.0/1.11

        xs, ys, zs, type = ([] for i in range(4))
        Bxpos, Bypos, Bzpos, Btypepos = ([] for i in range(4))

        #altenate
        xs.append(0.0)
        ys.append(0.0)
        zs.append(0.0)

        xs.append(a/4.0)
        ys.append(a/4.0)
        zs.append(a/4.0)

        xs.append(a/2.0)
        ys.append(a/2.0)
        zs.append(0.0)

        xs.append(0)
        ys.append(a/2.0)
        zs.append(a/2.0)

        xs.append(a/2.0)
        ys.append(0)
        zs.append(a/2.0)

        xs.append(3.0*a/4.0)
        ys.append(3*a/4.0)
        zs.append(a/4.0)

        xs.append(a/4.0)
        ys.append(3*a/4.0)
        zs.append(3.0*a/4.0)

        xs.append(3.0*a/4.0)
        ys.append(a/4.0)
        zs.append(3.0*a/4.0)

        xs.append(3.0/4.0*a-b/math.sqrt(8))
        ys.append(3.0/4.0*a-b/math.sqrt(8))
        zs.append(3.0/4.0*a-b/math.sqrt(8))

        xs.append(3.0/4.0*a-b/math.sqrt(8))
        ys.append(3.0/4.0*a+b/math.sqrt(8))
        zs.append(3.0/4.0*a+b/math.sqrt(8))

        xs.append(3.0/4.0*a+b/math.sqrt(8))
        ys.append(3.0/4.0*a-b/math.sqrt(8))
        zs.append(3.0/4.0*a+b/math.sqrt(8))

        xs.append(3.0/4.0*a+b/math.sqrt(8))
        ys.append(3.0/4.0*a+b/math.sqrt(8))
        zs.append(3.0/4.0*a-b/math.sqrt(8))

        xs.append(xs[7+1]-a/2.0)
        xs.append(xs[7+2]-a/2.0)
        xs.append(xs[7+3]-a/2.0)
        xs.append(xs[7+4]-a/2.0)
        ys.append(ys[7+1]-a/2.0)
        ys.append(ys[7+2]-a/2.0)
        ys.append(ys[7+3]-a/2.0)
        ys.append(ys[7+4]-a/2.0)
        zs.append(zs[7+1])
        zs.append(zs[7+2])
        zs.append(zs[7+3])
        zs.append(zs[7+4])

        xs.append(xs[7+1])
        xs.append(xs[7+2])
        xs.append(xs[7+3])
        xs.append(xs[7+4])
        ys.append(ys[7+1]-a/2.0)
        ys.append(ys[7+2]-a/2.0)
        ys.append(ys[7+3]-a/2.0)
        ys.append(ys[7+4]-a/2.0)
        zs.append(zs[7+1]-a/2.0)
        zs.append(zs[7+2]-a/2.0)
        zs.append(zs[7+3]-a/2.0)
        zs.append(zs[7+4]-a/2.0)

        xs.append(xs[7+1]-a/2.0)
        xs.append(xs[7+2]-a/2.0)
        xs.append(xs[7+3]-a/2.0)
        xs.append(xs[7+4]-a/2.0)
        ys.append(ys[7+1])
        ys.append(ys[7+2])
        ys.append(ys[7+3])
        ys.append(ys[7+4])
        zs.append(zs[7+1]-a/2.0)
        zs.append(zs[7+2]-a/2.0)
        zs.append(zs[7+3]-a/2.0)
        zs.append(zs[7+4]-a/2.0)

        for i in range(24):
            if(i<=7):
                type.append(1)
            else:
                type.append(2)

        nt=0
        #cast typepos to set to get the unique values then do len to get count
        typeset = set(type)
        typecount = len(typeset)

        for nx in range(0,numcellx):
            for ny in range (0,numcelly):
                for nz in range(0,numcellz):
                    for i in range(24):
                        nt=nt+1
                        Bxpos.append(xs[i]+nx*a)
                        Bypos.append(ys[i]+ny*a)
                        Bzpos.append(zs[i]+nz*a)
                        Btypepos.append(type[i])

        finalRet = []
        print(nt)
        for x in range(nt):
            points = [Bxpos[x], Bypos[x],Bzpos[x],Btypepos[x]]
            finalRet.append(points)
        return finalRet, typecount

    # data, count = MgCu2(2,2,2)
    # print("num atoms: " + str(len(data)))
    # print("num types: " + str(count))
    # file = open("MgCu2.xyz","w")
    # file.write("{}\r\n".format(len(data)))
    # file.write('Atoms\n')
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()


    def FCC(numcellx, numcelly, numcellz):
        #test FCC with Bs
        xpos, ypos, zpos= ([] for i in range(3))
        Bxpos, Bypos, Bzpos = ([] for i in range(3))

        acell=math.sqrt(2)
        xpos.append(0)
        ypos.append(0)
        zpos.append(0)

        xpos.append(acell/2)
        ypos.append(acell/2)
        zpos.append(0)

        xpos.append(0)
        ypos.append(acell/2)
        zpos.append(acell/2)

        xpos.append(acell/2)
        ypos.append(0)
        zpos.append(acell/2)


        atnum=0

        for i1 in range(1, numcellx+1):
            for i2 in range(1, numcelly+1):
                for i3 in range(1, numcellz+1):
                    for i in range(4):
                        atnum=atnum+1
                        Bxpos.append(xpos[i]+i1*acell)
                        Bypos.append(ypos[i]+i2*acell)
                        Bzpos.append(zpos[i]+i3*acell)

        finalRet = []
        typeatom = 1
        print(atnum)
        for x in range(atnum):
            points = [Bxpos[x], Bypos[x],Bzpos[x],typeatom]
            finalRet.append(points)
        #hard coded as only one atom type in structure
        return finalRet, 1

    # data, count = FCC(2,2,2)
    # print("num atoms: " + str(len(data)))
    # print("num types: " + str(count))
    # file = open("FCC.xyz","w")
    # file.write("{}\r\n".format(len(data)))
    # file.write('Atoms\n')
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()

    def MgSnCu4(numcellx, numcelly, numcellz):
        #test Mg(1)in corners with Sn(2) in the diamond structure.  Cu(3) in a
        #pyrochlore strucutre

        acell=1
        xs, ys, zs, typepos = ([] for i in range(4))
        Bxpos, Bypos, Bzpos, Btypepos = ([] for i in range(4))

        a=1.0
        b=a*math.sqrt(3.0)/4.0/1.11
        #altenate
        xs.append(0.0)
        ys.append(0.0)
        zs.append(0.0)

        xs.append(a/2.0)
        ys.append(0)
        zs.append(a/2.0)

        xs.append(a/2.0)
        ys.append(a/2.0)
        zs.append(0.0)

        xs.append(0)
        ys.append(a/2.0)
        zs.append(a/2.0)

        xs.append(a/4.0)
        ys.append(a/4.0)
        zs.append(a/4.0)

        xs.append(3.0*a/4.0)
        ys.append(3*a/4.0)
        zs.append(a/4.0)

        xs.append(a/4.0)
        ys.append(3*a/4.0)
        zs.append(3.0*a/4.0)

        xs.append(3.0*a/4.0)
        ys.append(a/4.0)
        zs.append(3.0*a/4.0)

        xs.append(3.0/4.0*a-b/math.sqrt(8))
        ys.append(3.0/4.0*a-b/math.sqrt(8))
        zs.append(3.0/4.0*a-b/math.sqrt(8))

        xs.append(3.0/4.0*a-b/math.sqrt(8))
        ys.append(3.0/4.0*a+b/math.sqrt(8))
        zs.append(3.0/4.0*a+b/math.sqrt(8))

        xs.append(3.0/4.0*a+b/math.sqrt(8))
        ys.append(3.0/4.0*a-b/math.sqrt(8))
        zs.append(3.0/4.0*a+b/math.sqrt(8))

        xs.append(3.0/4.0*a+b/math.sqrt(8))
        ys.append(3.0/4.0*a+b/math.sqrt(8))
        zs.append(3.0/4.0*a-b/math.sqrt(8))


        xs.append(xs[7+1]-a/2.0)
        xs.append(xs[7+2]-a/2.0)
        xs.append(xs[7+3]-a/2.0)
        xs.append(xs[7+4]-a/2.0)
        ys.append(ys[7+1]-a/2.0)
        ys.append(ys[7+2]-a/2.0)
        ys.append(ys[7+3]-a/2.0)
        ys.append(ys[7+4]-a/2.0)
        zs.append(zs[7+1])
        zs.append(zs[7+2])
        zs.append(zs[7+3])
        zs.append(zs[7+4])

        xs.append(xs[7+1])
        xs.append(xs[7+2])
        xs.append(xs[7+3])
        xs.append(xs[7+4])
        ys.append(ys[7+1]-a/2.0)
        ys.append(ys[7+2]-a/2.0)
        ys.append(ys[7+3]-a/2.0)
        ys.append(ys[7+4]-a/2.0)
        zs.append(zs[7+1]-a/2.0)
        zs.append(zs[7+2]-a/2.0)
        zs.append(zs[7+3]-a/2.0)
        zs.append(zs[7+4]-a/2.0)

        xs.append(xs[7+1]-a/2.0)
        xs.append(xs[7+2]-a/2.0)
        xs.append(xs[7+3]-a/2.0)
        xs.append(xs[7+4]-a/2.0)
        ys.append(ys[7+1])
        ys.append(ys[7+2])
        ys.append(ys[7+3])
        ys.append(ys[7+4])
        zs.append(zs[7+1]-a/2.0)
        zs.append(zs[7+2]-a/2.0)
        zs.append(zs[7+3]-a/2.0)
        zs.append(zs[7+4]-a/2.0)



        for i in range(24):
            if(i<4):
                typepos.append(1)
            elif(i<9):
                typepos.append(2)
            else:
                typepos.append(3)

        #cast typepos to set to get the unique values then do len to get count
        typeset = set(typepos)
        typecount = len(typeset)

        atnum=0

        for i1 in range(0, numcellx+1):
            for i2 in range(0, numcelly+1):
                for i3 in range(0, numcellz+1):
                    for i in range(24):
                        atnum=atnum+1
                        Bxpos.append(xs[i]+i1*a)
                        Bypos.append(ys[i]+i2*a)
                        Bzpos.append(zs[i]+i3*a)
                        Btypepos.append(typepos[i])

        finalRet = []
        print(atnum)
        for x in range(atnum):
            points = [Bxpos[x], Bypos[x],Bzpos[x],Btypepos[x]]
            finalRet.append(points)
        return finalRet, typecount

    # data, count = MgSnCu4(2,2,2)
    # print("num atoms: " + str(len(data)))
    # print("num types: " + str(count))
    # file = open("MgSnCu4.xyz","w")
    # file.write("{}\r\n".format(len(data)))
    # file.write('Atoms\n')
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()


    def NaCl(numcellx, numcelly, numcellz):
        #test Diamond with Na atoms at corners and faces and Cl in the diamond
        #structure
        acell=1
        xpos, ypos, zpos, typepos = ([] for i in range(4))
        Bxpos, Bypos, Bzpos, Btypepos = ([] for i in range(4))

        xpos.append(0)
        ypos.append(0)
        zpos.append(0)
        typepos.append(1) #corner

        xpos.append(acell/2)
        ypos.append(acell/2)
        zpos.append(0)
        typepos.append(1) #face
        xpos.append(0)
        ypos.append(acell/2)
        zpos.append(acell/2)
        typepos.append(1) #face
        xpos.append(acell/2)
        ypos.append(0)
        zpos.append(acell/2)
        typepos.append(1) #face

        xpos.append(acell/2)
        ypos.append(0)
        zpos.append(0)
        typepos.append(2) #diamond
        xpos.append(0)
        ypos.append((1/2)*acell)
        zpos.append(0)
        typepos.append(2) #diamond
        xpos.append(0)
        ypos.append(0)
        zpos.append((1/2)*acell)
        typepos.append(2) #diamond
        xpos.append((1/2)*acell)
        ypos.append((1/2)*acell)
        zpos.append((1/2)*acell)
        typepos.append(2) #diamond

        #cast typepos to set to get the unique values then do len to get count
        typeset = set(typepos)
        typecount = len(typeset)

        atnum=0

        for i1 in range(1, numcellx+1):
            for i2 in range(1, numcelly+1):
                for i3 in range(1, numcellz+1):
                    for i in range(8):
                        atnum=atnum+1
                        Bxpos.append(xpos[i]+i1*acell)
                        Bypos.append(ypos[i]+i2*acell)
                        Bzpos.append(zpos[i]+i3*acell)
                        Btypepos.append(typepos[i])

        finalRet = []
        print(atnum)
        for x in range(atnum):
            points = [Bxpos[x], Bypos[x],Bzpos[x],Btypepos[x]]
            finalRet.append(points)
        return finalRet, typecount

    # data, count = NaCl(2,2,2)
    # print("num atoms: " + str(len(data)))
    # print("num types: " + str(count))
    # file = open("NaCl.xyz","w")
    # file.write("{}\r\n".format(len(data)))
    # file.write('Atoms\n')
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()




    def ZincBlende(numcellx, numcelly, numcellz):
        '''test Diamond with Bs'''
        acell=1
        xpos, ypos, zpos, typepos = ([] for i in range(4))
        Bxpos, Bypos, Bzpos, Btypepos = ([] for i in range(4))

        xpos.append(0)
        ypos.append(0)
        zpos.append(0)
        typepos.append(1)
        xpos.append(acell/2)
        ypos.append(acell/2)
        zpos.append(0)
        typepos.append(1)
        xpos.append(0)
        ypos.append(acell/2)
        zpos.append(acell/2)
        typepos.append(1)
        xpos.append(acell/2)
        ypos.append(0)
        zpos.append(acell/2)
        typepos.append(1)
        xpos.append((3/4)*acell)
        ypos.append((1/4)*acell)
        zpos.append((3/4)*acell)
        typepos.append(2)
        xpos.append((1/4)*acell)
        ypos.append((3/4)*acell)
        zpos.append((3/4)*acell)
        typepos.append(2)
        xpos.append((1/4)*acell)
        ypos.append((1/4)*acell)
        zpos.append((1/4)*acell)
        typepos.append(2)
        xpos.append((3/4)*acell)
        ypos.append((3/4)*acell)
        zpos.append((1/4)*acell)
        typepos.append(2)

        #cast typepos to set to get the unique values then do len to get count
        typeset = set(typepos)
        typecount = len(typeset)

        atnum=0


        for i1 in range(1, numcellx+1):
            for i2 in range(1, numcelly+1):
                for i3 in range(1, numcellz+1):
                    for i in range(8):
                       atnum=atnum+1
                       Bxpos.append(xpos[i]+i1*acell)
                       Bypos.append(ypos[i]+i2*acell)
                       Bzpos.append(zpos[i]+i3*acell)
                       Btypepos.append(typepos[i])

        finalRet = []
        print(atnum)
        for x in range(atnum):
            points = [Bxpos[x], Bypos[x],Bzpos[x],Btypepos[x]]
            finalRet.append(points)
        return finalRet, typecount

    # data, count = ZincBlende(2,2,2)
    # print("num atoms: " + str(len(data)))
    # print("num types: " + str(count))
    # file = open("ZincBlende.xyz","w")
    # file.write("{}\r\n".format(len(data)))
    # file.write('Atoms\n')
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()

    '''File Reader. This file reader parses an XYZ file
    and returns a list of lists of each set of points in the format of
    X, Y, Z, Particle Type '''
    def FileReader(path):
        points = []
        typeset = []
        with open(path) as f:
            # Skip first 2 lines (XYZ file format)
            next(f)
            next(f)
            for line in f.readlines():
                formatted_pts = []
                raw_nums = line.split()
                formatted_pts.append(float(raw_nums[1]))
                formatted_pts.append(float(raw_nums[2]))
                formatted_pts.append(float(raw_nums[3]))
                formatted_pts.append(float(raw_nums[0]))
                points.append(formatted_pts)
                if (float(raw_nums[0]) not in typeset):
                    typeset.append(float(raw_nums[0]))
        typecount = len(typeset)
        #return points
        return points,typecount

    ''' OutputFiles is a method that takes in a list of points for a structure
    that is either manually loaded or selected from the structure menu and
    writes a file to the directory the user is in with an XYZ format '''
    def OutputFiles(points):
        data = points
        file = open("structure.xyz","w")
        numberOfAtoms = len(data)
        file.write("{}\r\n".format(numberOfAtoms))
        file.write('Atoms\n')
        for y in data:
            file.write("{}\t {}\t {}\t {}\t\r\n".format(y[3], y[0], y[1],y[2]))
        file.close()
