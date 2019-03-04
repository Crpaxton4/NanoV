import math
from tkinter import filedialog
from tkinter import *

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
        numcellx=2
        numcelly=2
        numcellz=2
        atnum=0

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
        return finalRet
    # data = CaB6()
    # file = open("CaB6.xyz","w")
    # file.write("{}\r\n".format(56))
    # file.write('Atoms\n')
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()
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
        return finalRet
    # data = AlB2()
    # file = open("AlB2.xyz","w")
    # file.write("{}\r\n".format(16))
    # file.write('Atoms\n')
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()


    '''test BCC with Bs'''
    def BCC():
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

        numcellx=2
        numcelly=2
        numcellz=2
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
        return finalRet
    # data = BCC()
    # file = open("bcc.xyz","w")
    # file.write("{}\r\n".format(32))
    # file.write('Atoms\n')
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()

    '''test Au(type 1) in corner and Cu (type 2) on faces'''
    def Cu3Au():
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

        numcellx=2
        numcelly=2
        numcellz=2
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
        return finalRet
    # data = Cu3Au()
    # file = open("Cu3Au.xyz","w")
    # file.write("{}\r\n".format(32))
    # file.write('Atoms\n')
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()

    ''' test Diamond with Bs '''
    def Diamond():
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


        numcellx=2
        numcelly=2
        numcellz=2
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
        return finalRet
    # data = Diamond()
    # file = open("diamond.xyz","w")
    # file.write("{}\r\n".format(64))
    # file.write('Atoms\n')
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()

    ''' Laves face structure '''
    def Laves():
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
        maxx=1
        maxy=1
        maxz=1
        for nx in range(0,maxx+1):
            for ny in range(0,maxy+1):
                for nz in range(0,maxz+1):
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
        return finalRet
    # data = Laves()
    # file = open("laves.xyz","w")
    # file.write("{}\r\n".format(192))
    # file.write('Atoms\n')
    # for x in data:
    #     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
    # file.close()

    ''' File Reader. This file reader parses an XYZ file
    and returns a list of lists of each set of points in the format of
    X, Y, Z, Particle Type '''
    def FileReader(path):
        points = []
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
        #return points
        return points
    #
    #
# root = Tk()
# root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("xyz files","*.xyz"),("all files","*.*")))
# print(StructureLibrary.FileReader(root.filename))

''' Writing files to test the coords '''
# data = StructureLibrary.Diamond(StructureLibrary)
# file = open("diamond.xyz","w")
# file.write("{}\r\n".format(64))
# file.write('Atoms\n')
# for x in data:
#     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
# file.close()

# data = StructureLibrary.BCC(StructureLibrary)
# file = open("bcc.xyz","w")
# file.write("{}\r\n".format(32))
# file.write('Atoms\n')
# for x in data:
#     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
# file.close()

# data = StructureLibrary.Laves(StructureLibrary)
# file = open("laves.xyz","w")
# file.write("{}\r\n".format(192))
# file.write('Atoms\n')
# for x in data:
#     file.write("{}\t {}\t {}\t {}\t\r\n".format(x[3], x[0], x[1],x[2]))
# file.close()
