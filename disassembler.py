from helper import SetUp
import os
import masking_constants as MASKs
import sys


class Disassembler:
    opcodeStr = []
    instrSpaced = []
    arg1 = []
    arg2 = []
    arg3 = []
    arg1Str = []
    arg2Str = []
    arg3Str = []
    dataval = []
    rawdata = []
    address = []
    numInstructs = 0

    def run(self):

        instructions = []
        instructions = SetUp.import_data_file()

        outputFilename = SetUp.get_output_filename()

        print("raw output filename is ", outputFilename)


        for i in range(len(instructions)):
            self.address.append(96 + (i * 4))
        opcode = []

        for z in instructions:
            opcode.append(int(z, base=2) >> 21)

            if opcode[1] == 1112:  for i in range(len(opcode)):
            self.numInstructs = self.numInstructs +
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("ADD")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
            elif opcode[i] == 1624:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("SUB")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
            elif opcode[i] == 1104:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("AND")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
            elif opcode[i] == 1690:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("LSR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
            elif opcode[i] == 1691:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("LSL")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
            elif opcode[i] == 1692:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("ASR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
            elif opcode[i] == 1872:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("EOR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
            elif opcode[i] < 192 & opcode[i] > 159:
                self.instrSpaced.append(SetUp.bin2StringSpacedB(instructions[i]))
                self.opcodeStr.append("B")
                self.arg1.append(int(instructions[i], base=2) & self.bMask)
                self.arg1.append("\t#" + str(self.arg1[i]))
            elif opcode[i] < 1162 & opcode[i] > 1159:
                self.instrSpaced.append((SetUp.bin2StringSpacedI(instructions[i])))
                self.opcodeStr.append("ADDI")
                self.arg1.append((int(instructions[i], base=2) & self.imMask) >> 10)
                self.arg2.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", " + self.arg2[i])
                self.arg3Str.append(", #" + self.arg1[i])
            elif opcode[i] < 1674 & opcode[i] > 1671:
                self.instrSpaced.append((SetUp.bin2StringSpacedI(instructions[i])))
                self.opcodeStr.append("SUBI")
                self.arg1.append((int(instructions[i], base=2) & self.imMask) >> 10)
                self.arg2.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", " + self.arg2[i])
                self.arg3Str.append(", #" + self.arg1[i])
            elif opcode[i] > 1439 & opcode[i] > 1448:
                self.instrSpaced.append(SetUp.bin2StringSpacedCB(instructions[i]))
                self.opcodeStr.append("CBZ")
                self.arg1.append((int(instructions[i], base=2) & self.addr2Mask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + self.arg2[i])
                self.arg2Str.append(", #"+ self.arg1[i])
            elif opcode[i] > 1447 & opcode[i] > 1456:
                self.instrSpaced.append(SetUp.bin2StringSpacedCB(instructions[i]))
                self.opcodeStr.append("CBNZ")
                self.arg1.append((int(instructions[i], base=2) & self.addr2Mask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + self.arg2[i])
                self.arg2Str.append(", #"+ self.arg1[i])
            elif opcode[i] > 1447 & opcode[i] > 1456:
                self.instrSpaced.append(SetUp.bin2StringSpacedIM(instructions[i]))
                self.opcodeStr.append("MOVZ")
                self.arg1.append((int(instructions[i], base=2) & self.imsftMask) >> 21)
                self.arg2.append((int(instructions[i], base=2) & self.imdataMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
            elif opcode[i] == 1984:
                self.instrSpaced.append(SetUp.bin2StringSpacedD(instructions[i]))
                self.opcodeStr.append("STUR")
                self.arg1.append((int(instructions[i], base=2) & self.addrMask) >> 12)
                self.arg2.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", [" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg1[i]) + "]")
            elif opcode[i] == 1986:
                self.instrSpaced.append(SetUp.bin2StringSpacedD(instructions[i]))
                self.opcodeStr.append("LDUR")
                self.arg1.append((int(instructions[i], base=2) & self.addrMask) >> 12)
                self.arg2.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", [" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg1[i]) + "]")








