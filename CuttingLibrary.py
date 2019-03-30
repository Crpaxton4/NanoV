"""

CuttingLibrary.py

"""


class CuttingLibrary:
    '''

    CuttingLibrary

    '''

    '''
    Define cutting functionality for cutting tool
    '''
    def Sphere(filename, radius):
        xcent = 0
        ycent = 0
        zcent = 0
        count = 0
        points = []
        typePos = []
        typeResult = []
        result = []
        numAtoms = 0
        with open(filename) as f:
            # Skip second line after getting number of atoms
            numAtoms = int(f.readline().split()[0])
            next(f)
            for line in f.readlines():
                raw_nums = line.split()
                points.append(float(raw_nums[1]))
                points.append(float(raw_nums[2]))
                points.append(float(raw_nums[3]))
                typePos.append(float(raw_nums[0]))
                xcent = xcent + float(raw_nums[1])
                ycent = ycent + float(raw_nums[2])
                zcent = zcent + float(raw_nums[3])
        xcent = xcent / numAtoms
        ycent = ycent / numAtoms
        zcent = zcent / numAtoms
        for i in range(numAtoms):
            distsq = (points[3*i] - xcent) * (points[3*i] - xcent) + (points[3*i+1] - ycent) * (points[3*i+1] - ycent) + (points[3*i+2] - zcent) * (points[3*i+2] - zcent)
            print(distsq)
            if (distsq <= radius * radius):
                count = count + 1
                typeResult.append(typePos[i])
                result.append(points[3*i])
                result.append(points[3*i+1])
                result.append(points[3*i+2])
        file = open("sphereCut.xyz","w")
        numberOfAtoms = count
        file.write("{}\r\n".format(numberOfAtoms))
        file.write('Atoms\n')
        for i in range(count):
            file.write("{}\t {}\t {}\t {}\t\r\n".format(typeResult[i], result[3*i],result[3*i+1], result[3*i+2]))
        file.close()
    #Sphere('bcc.xyz',1)
