import sys
import os

def create_files(input):

    # convert file in a list of strings
    with open(input) as file:
        lines = file.readlines()

    i = 1
    o = open(input[0:-4]+"{}.txt".format(i), "w")
    for line in lines:
        if len(line.strip()) == 0:
            o.close()
            i = i+1
            o = open(input[0:-4]+"{}.txt".format(i), "w")
        else:
            o.write(line)
    return i


def get_file(input,num):        
    return input[0:-4]+str(num)+".txt"


def main():

    # two arguments are expected
    # 1) input file
    # 2) output file
    input  = sys.argv[1]
    output = sys.argv[2]

    # loudly complain if input file does not exist
    if not os.path.isfile(input):
        print("File path {} does not exist. Exiting...".format(input))
        sys.exit()

    num = create_files(input)

    print(num)

    for i in range(1,num):

        print('file #'+str(i))
        
        # convert file in a list of strings
        with open(get_file(input,i)) as file:
            lines = file.readlines()

            try:
                stop_1 = lines.index('AU Aad, G\n')
            except:
                stop_1 = lines.index('AU Aaboud, M\n')
            stop_2 = lines.index('CA ATLAS Collaboration\n')

            print(' author list #'+str(stop_1)+' '+str(stop_2))
            
            # remove the full author list except the first name
            lines = lines[:stop_1+1]+lines[stop_2:]

            # substitute the first name with mine
            lines[stop_1] = 'AU COCCARO A; others\n'
            
            # remove very long strings
            #lines = ([s for s in lines if not s.startswith('RI ')])
            #lines = ([s for s in lines if not s.startswith('OI ')])
            
            # find the indexes of another unneeded long list
            #stop_1 = lines.index('PY 2020\n')
            #stop_2 = lines.index('ZS 0\n')
            
            # remove this long list
            #lines = lines[:stop_1+1]+lines[stop_2:]
    
            with open(get_file(input,i), 'w') as file:
                file.write(''.join(lines))

    with open(output, 'w') as file:
        for i in range(1,num+1):
            with open(get_file(input,i)) as infile:
                for line in infile:
                    file.write(line)
                os.remove(infile.name)
                file.write('\n')
                
if __name__ == '__main__':
    main()
