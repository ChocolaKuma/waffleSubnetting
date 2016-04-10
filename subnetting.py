##The MIT License (MIT)
##
##Copyright (c) 2016 Johnathan Hinebrook (github.com/Juggalojohn)
##
##Permission is hereby granted, free of charge, to any person obtaining a copy
##of this software and associated documentation files (the "Software"), to deal
##in the Software without restriction, including without limitation the rights
##to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##copies of the Software, and to permit persons to whom the Software is
##furnished to do so, subject to the following conditions:
##
##The above copyright notice and this permission notice shall be included in all
##copies or substantial portions of the Software.
##
##THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
##SOFTWARE.

##subnetpractice.py 
##Python 3.X
##Last Updated: 02.25.2016..23.36
##
##This Program generates a IPv4 Address and amount of required subnets
##I have not tested if the custom submask for
##class A and B is returning proper result use it at your own risk
##

import random

ipClass = ""

def question():
    global a,b,c,d,e
    print("===========================================")
    print(a,".",b,".",c,".",d)
    print("")
    print("With:",e,"subnets")
    print("")
    print("")
    print("")


def Fclass(a):
    #finds class and default subnet
    global ipClass
    
    if a <= 127:
        print("Class A")
        print("Default Subnet: 255.0.0.0")
        ipClass = "A"
    if a in range (128, 191):
        print("Class B")
        print("Default Subnet: 255.255.0.0")
        ipClass = "B"
    if a in range (192, 223):
        print("Class C")
        print("Default Subnet: 255.255.255.0")
        ipClass = "C"
    if a in range (224, 239):
        print("Class D")
        print("No Default Subnet")
        ipClass = "D"
    if a in range (240, 255):
        print("Class E")
        print("No Default Subnet")
        ipClass = "E"

def findsubnetamt(amtsubnet):
    #finds total number of requred subnets
    if amtsubnet == 1:
        global AMTOFSUBNETex
        #Binary 1
        AMTOFSUBNETex = 0
    if amtsubnet == 2:
        #Binary 2
        global AMTOFSUBNETex
        AMTOFSUBNETex = 1
    if amtsubnet  == 3 or 4:
        #Binary 4
        global AMTOFSUBNETex
        AMTOFSUBNETex = 2
    if amtsubnet in range (5, 8):
        #Binary 4
        global AMTOFSUBNETex
        AMTOFSUBNETex = 3
    if amtsubnet in range (9, 16):
        #Binary 4
        global AMTOFSUBNETex
        AMTOFSUBNETex = 4
    if amtsubnet in range (17, 32):
        #Binary 4
        global AMTOFSUBNETex
        AMTOFSUBNETex = 5
    if amtsubnet in range (33, 64):
        #Binary 4
        global AMTOFSUBNETex
        AMTOFSUBNETex = 6
    if amtsubnet in range (65, 128):
        #Binary 4
        global AMTOFSUBNETex
        AMTOFSUBNETex = 7

def findCustomMask(amtNetBits,ipClass):
    global cmask
    cmask = ""
  

    if amtNetBits == 1:
        cmask = "128"
    if amtNetBits == 2:
        cmask = "192"
    if amtNetBits == 3:
        cmask = "224"
    if amtNetBits == 4:
        cmask = "240"
    if amtNetBits == 5:
        cmask = "248"
    if amtNetBits == 6:
        cmask = "252"
    if amtNetBits == 7:
        cmask = "254"
    if amtNetBits == 8:
        cmask = "255"

    if amtNetBits == 9:
        cmask = "255.128"
    if amtNetBits == 10:
        cmask = "255.192"
    if amtNetBits == 11:
        cmask = "255.224"
    if amtNetBits == 12:
        cmask = "255.240"
    if amtNetBits == 13:
        cmask = "255.248"
    if amtNetBits == 14:
        cmask = "255.252"
    if amtNetBits == 15:
        cmask = "255.254"
    if amtNetBits == 16:
        cmask = "255.255"

    if amtNetBits == 17:
        cmask = "255.255.128"
    if amtNetBits == 18:
        cmask = "255.255.192"
    if amtNetBits == 19:
        cmask = "255.255.224"
    if amtNetBits == 20:
        cmask = "255.255.240"
    if amtNetBits == 21:
        cmask = "255.255.248"
    if amtNetBits == 22:
        cmask = "255.255.252"
    if amtNetBits == 23:
        cmask = "255.255.254"
    if amtNetBits == 24:
        cmask = "255.255.255"

def answer():
    print("Press Enter For Answers")
    BLANKINPUT = input()        
    print("Answers:")
    print("")
    findsubnetamt(e)
    Fclass(a)
    # ** to notate exponits
    NUMSUBNETTOTAL = 2 ** AMTOFSUBNETex
    print("Total Amount of Required Subnets:",NUMSUBNETTOTAL)
    print("Total Amount of bits borrowed:",AMTOFSUBNETex)
    amtOfnettBits = 8 - AMTOFSUBNETex
    possableHosts = 2 ** amtOfnettBits
    print("Total of possable IPs:",possableHosts)
    usableHosts = possableHosts - 2
    print("Number of usable Hosts",usableHosts)   
    print("")
    print("")
    print("")
    print("Custom Subnet mask")
    findCustomMask(amtOfnettBits,ipClass)
    if ipClass == "A":
        print(cmask)
    if ipClass == "B":
        print(cmask)        
    if ipClass == "C":  
        print(cmask)       
    if ipClass == "D":
        print("This Feature Has not been written *only works with class a-C")        
    if ipClass == "E":
        print("This Feature Has not been written *only works with class a-C")
    print("===========================================")


def main():
    question()
    answer()
play = 0

while play !=1:
    
    a = random.randint(1,255) #IPv4 octet 1
    b =  random.randint(1,255) #IPv4 octet 2
    c =  random.randint(1,255) #IPv4 octet 3
    d =   0 #0 is dedault value in IPv4
    e =   random.randint(1,128)  #Num hof suubnets
    main()
    print("Would you like to keep practicing?")
    print("Enter to going")
    input()

    

