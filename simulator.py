import sys
from helper import SetUp
import masking_constants as MASKs

class State:
    dataval = []
    PC = 96
    cycle = 1
    R = [3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self, opcode, dataval, address, arg1, arg2, arg3, numInstructs, opcodeStr, arg1Str, arg2Str, arg3Str):
        self.opcode = opcode
        self.dataval = dataval
        self.address = address
        self.numInstructs = numInstructs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.opcodeStr = opcodeStr
        self.arg1Str = arg1Str
        self.arg2Str = arg2Str
        self.arg3Str = arg3Str

    def getIndexOfMemAddress(self, currAddr):
        for i in self.address:
            if i == currAddr:
                return int((i-96)/4)

    def incrementPC(self):
         self.PC += 4

    def printState(self):
        outputFilename = SetUp.get_output_filename()

        with open(outputFilename + "_sim.txt", 'a') as outFile:

            i = self.getIndexOfMemAddress(self.PC)
            outFile.write("====================\n")
            outFile.write("cycle:" + str(self.cycle) + "\t" + str(self.PC) + "\t" + self.opcodeStr[i] + self.arg1Str[i]
                          + self.arg2Str[i] + self.arg3Str[i] + "\n")
            outFile.write("\n")
            outFile.write("register:\n")
            outStr = "r00:"
            for i in range(0, 8):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr + "\n")
            outStr = "r08:"
            for i in range(8, 16):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr + "\n")
            outStr = "r16:"
            for i in range(16, 24):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr + "\n")
            outStr = "r24:"
            for i in range(24, 32):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr + "\n")

            outFile.write("\ndata:\n")
            for i in range(len(self.dataval)):
                if i % 8 == 0 and i != 0 or i == len(self.dataval):
                    outFile.write(outStr + "\n")
                if i % 8 == 0:
                    outStr = str(self.address[i + self.numInstructs]) + ":" + str(self.dataval[i])
                if (i % 8 != 0):
                    outStr = outStr + "\t" + str(self.dataval[i])

            outFile.write(outStr + "\n")
            outFile.close()


class Simulator:

    def __init__(self, opcode, dataval, address, arg1, arg2, arg3, numInstructs, opcodeStr, arg1Str, arg2Str, arg3Str):
        self.opcode = opcode
        self.dataval = dataval
        self.address = address
        self.numInstructs = numInstructs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.opcodeStr = opcodeStr
        self.arg1Str = arg1Str
        self.arg2Str = arg2Str
        self.arg3Str = arg3Str

    def run(self):
        foundBreak = False
        armState = State(self.opcode, self.dataval, self.address, self.arg1, self.arg2, self.arg3, self.numInstructs,
                         self.opcodeStr, self.arg1Str, self.arg2Str, self.arg3Str)
        while not foundBreak:
            jumpAddr = armState.PC
            i = armState.getIndexOfMemAddress(armState.PC)

            if self.opcode[i] == 0: #NOP
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue
            elif 160 <= self.opcode[i] <= 191: #B
                jumpAddr = jumpAddr + ((self.arg1[i] * 4) - 4)
            elif self.opcode[i] == 1112:  # ADD
                armState.R[self.arg3[i]-1] = armState.R[self.arg1[i] - 1] + armState.R[self.arg2[i] - 1]
            elif self.opcode[i] == 1624:  # SUB
                armState.R[self.arg3[i]-1] = armState.R[self.arg1[i] - 1] - armState.R[self.arg2[i] - 1]
            elif (self.opcode[i] == 1104):  # AND
                armState.R[self.arg3[i] - 1] = armState.R[self.arg1[i] -1] & armState.R[self.arg2[i] -1]
            elif (self.opcode[i] == 1360):  # ORR
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] | armState.R[self.arg2[i]]
            elif self.opcode[i] == 1690:  # LSR
                continue
            elif self.opcode[i] == 1691:  # LSL
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] << self.arg2[i]
            elif self.opcode[i] == 1692:  # ASR
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] >> self.arg2[i]
            elif (self.opcode[i] == 1872):  # EOR
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] ^ armState.R[self.arg2[i]]
            elif self.opcode[i] == 1160 or self.opcode[i] == 1161:  # ADDI
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] + self.arg1[i]
            elif self.opcode[i] == 1672 or self.opcode[i] == 1673:  # SUBI
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] - self.arg1[i]
            elif 1440 <= self.opcode[i] <= 1447:  # CBZ
                if armState.R[self.arg2[i]] == 0:
                    jumpAddr = jumpAddr + ((self.arg2[i] * 4) - 4)
            elif 1448 <= self.opcode[i] <= 1455:  # CBNZ
                if armState.R[self.arg2[i]] != 0:
                    jumpAddr = jumpAddr + ((self.arg2[i] * 4) - 4)
            elif 1684 <= self.opcode[i] <= 1687:  # MOVZ
                continue
            elif 1940 <= self.opcode[i] <= 1943:  # MOVK
                continue
            elif self.opcode[i] == 1984:  # STUR
                continue
            elif self.opcode[i] == 1986:  # LDUR
                continue
            elif self.opcode[i] == 2038: #Break
                foundBreak = True
            else:
                print("IN SIM -- UNKNOWN INSTRUCTION ------------------------ !!!!!!!")

            armState.printState()
            armState.PC = jumpAddr
            armState.incrementPC()
            armState.cycle += 1

