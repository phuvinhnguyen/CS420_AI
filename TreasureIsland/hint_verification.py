def hintVerify(input):
    match input[0]:
        case 1:
            return "Tile(s) " + str(input[2])+ " do(es) not contain treasure."
        case 2:
            return "One region in the list "+ str(input[2])+ " contains treasure."
        case 3:
            return "Region(s) "+str(input[2])+ " do(es) not contain treasure."
        case 4:
            return "A rectangle area from "+str(input[2][0:1])+" to "+str(input[2][2:4])+" contains the treasure."
        case 5:
            return "A rectangle area from "+str(input[2][0:1])+" to "+str(input[2][2:4])+" does not the treasure."
        case 6:
            return "You are the nearest person from the treasure."
        case 7:
            if (input[2][0]==-1):
                return "Column "+str(input[2][1])+" contains the treasure."
            elif (input[2][1]==-1):
                return "Row "+str(input[2][0])+" contains the treasure."
            else: 
                return "The treasure is contained somewhere in row "+str(input[2][0])+" and column "+str(input[2][1])+"."
        case 8:
            if (input[2][0]==-1):
                return "Column "+str(input[2][1])+" does not contain the treasure."
            elif (input[2][1]==-1):
                return "Row "+str(input[2][0])+" does not contain the treasure."
            else: 
                return "The treasure is not contained anywhere in row "+str(input[2][0])+" or column "+str(input[2][1])+"."
        case 9:
            return "The treasure is somewhere in the boundary of 2 regions "+str(input[2][0])+" and "+str(input[2][1])+"."
        case 10:
            return "The treasure is somewhere in the boundary of 2 regions."
        case 11:
            return "The treasure is somewhere in an area bounded by 2-3 tiles from sea."
        case 12:
            t = ""
            if input[2]=="U":
                t="upper"
            elif input[2]=="D":
                t="lower"
            elif input[2]=="L":
                t="left"
            else:
                t="right"
            return "The treasure is not contained in the "+t+" half of the map."
        case 13:
            t = ""
            if input[2]=="N":
                t="north"
            elif input[2]=="S":
                t="south"
            elif input[2]=="W":
                t="west"
            elif input[1]=="E":
                t="east"
            elif input[2]=="SE":
                t="southeast"
            elif input[2]=="NE":
                t="northeast"
            elif input[1]=="WS":
                t="southwest"
            else:
                t="northwest"
            return "The treasure is contained in the "+t+" part of the map."
        case 14:
            return "The treasure is somewhere between the gap of the rectangle from "+str(input[2][0][0:1])+" to "+str(input[2][0][2:4])+" and the rectangle from "+str(input[2][1][0:1])+" to "+str(input[2][1][2:4])+"."
        case 15:
            return "The treasure is in a region that has mountain."
