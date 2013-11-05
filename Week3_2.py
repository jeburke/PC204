import sys

def average_coord(pdb):
    fin = open(pdb, 'r')
    fin.seek(0)
    x = 0
    y = 0
    z = 0
    atom = 0
    for line in fin:
        if line[0:4] == 'ATOM':
            x = x + float(line[31:39])
            y = y + float(line[39:47])
            z = z + float(line[47:54])
            atom += 1
    x_avg = x / atom
    y_avg = y / atom
    z_avg = z / atom

    fin.close()

    print '%f \t %f \t %f' %(x_avg, y_avg, z_avg)

average_coord(sys.argv[1])
