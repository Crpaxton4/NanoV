"""

StructureLibrary.py

"""

class StructureLibrary:
        """

        StructureLibrary

        """
'''test Ca [type 1] on corners with a 6 atom diamond shape of B [type 2]
in the middle'''
def CaB6:
    acell = 1
    # Corner
    xpos[1]=0
    ypos[1]=0
    zpos[1]=0
    typepos[1]=1

    # Face
    xpos[2]=acell/2
    ypos[2]=acell/2
    zpos[2]=acell/4
    typepos[2]=2

    xpos[3]=acell/2
    ypos[3]=acell/2
    zpos[3]=(3/4)*acell
    typepos[3]=2
    xpos[4]=acell/4
    ypos[4]=acell/2
    zpos[4]=(1/2)*acell
    typepos[4]=2
    xpos[5]=acell/2
    ypos[5]=acell/4
    zpos[5]=(1/2)*acell
    typepos[5]=2
    xpos[6]=(3/4)*acell
    ypos[6]=acell/2
    zpos[6]=(1/2)*acell
    typepos[6]=2
    xpos[7]=acell/2
    ypos[7]=(3/4)*acell
    zpos[7]=(1/2)*acell
    typepos[7]=2;
