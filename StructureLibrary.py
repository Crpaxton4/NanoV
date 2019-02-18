import math
"""

StructureLibrary.py

"""
'''
Library of structures that organizes the points of the various structures
'''
class StructureLibrary:
    '''test Ca [type 1] on corners with a 6 atom diamond shape of B [type 2]
    in the middle'''
    def CaB6():
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
        numcellx=2;
        numcelly=2;
        numcellz=2;
        atnum=0;

        # Loop through and create layers
        for i1 in range(numcellx):
            for i2 in range(numcelly):
                for i3 in range(numcellz):
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
        return finalRet

    '''test Al(1) in corner with B(2) atoms on faces parallel to each other'''
    def AlB2():
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

        numcellx=2
        numcelly=2
        numcellz=2
        atnum=0

        for i1 in range(numcellx):
            for i2 in range(numcelly):
                for i3 in range(numcellz):
                    for i in range(2):
                        atnum=atnum+1;
                        Bxpos.append(xpos[i]+i1*acell)
                        Bypos.append(ypos[i]+i2*acell)
                        Bzpos.append(zpos[i]+i3*acell)
                        Btypepos.append(typepos[i])
        # rearrange the output
        finalRet = []
        for x in range(atnum):
            points = [Bxpos[x], Bypos[x],Bzpos[x],Btypepos[x]]
            finalRet.append(points)
        return finalRet
