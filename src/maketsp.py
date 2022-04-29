from sys import argv


def main():
    print("Make TSP Grid File")
    if len(argv) != 2:
        print("Correct use: python3 src/maketsp.py 100")
        return -1
    gridSz = int(argv[1])
    f = open("assets/grid-{:d}.tsp".format(gridSz), "w")
    f.write("NAME : grid-{:d} \r\n".format(gridSz))
    totalPts = gridSz * gridSz
    f.write("COMMENT : {:d} x {:d} locations auto generated\r\n".format(gridSz, gridSz))
    f.write("TYPE : TSP\r\n")
    f.write("DIMENSION : {:d}\r\n".format(totalPts))
    f.write("EDGE_WEIGHT_TYPE : EUC_2D\r\n")
    f.write("NODE_COORD_SECTION\r\n")
    count = 1
    for x in range(gridSz):
        for y in range(gridSz):
            f.write("{:d} {:04} {:04}\r\n".format(count, x, y))
            count = count + 1
    f.close()
    print('Done!')


main()
