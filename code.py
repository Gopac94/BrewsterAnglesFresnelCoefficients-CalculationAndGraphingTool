import math
import matplotlib.pyplot as plt

while True:
        print("----------------------------------------------------")
        print("Application:")
        print("1)Select the refractive indices and rp, rs, tp, ts, brewster and calculate the critical angle.")
        print("2)Create a fresnel coefficient plot by entering refractive indices.")
        print("----------------------------------------------------")
        pick = int(input("choice:"))
        
        if pick == 1:
            while True:
                print("----------------------------------------------------") 
                print("Write 'menu' to return to the menu again.")
                n1 = float(input("(n1) --> Refractive index of the first field:"))
                if n1 == 999.0:
                    break
                n2 = float(input("(n2) --> Refractive index of the second field:"))
                if n2 == 999.0:
                    break
                cla = float(input("Angle of incidence of light:"))
                if cla == 999.0:
                    break
                print("----------------------------------------------------")
                if n1<n2:
                    op = math.asin((((n1*math.sin(math.pi/(180/cla))/n2))))
                    gla=(op*180)/math.pi
                    rs = ((n1*math.cos(math.pi/(180/cla)))-
                          (n2*math.cos(math.pi/(180/gla))))/((n1*math.cos(math.pi/(180/cla)))+
                          (n2*math.cos(math.pi/(180/gla))))
                    ts = ((2*n1*math.cos(math.pi/(180/cla))))/((n1*math.cos(math.pi/(180/cla)))+
                          (n2*math.cos(math.pi/(180/gla))))
                    rp = ((n2*math.cos(math.pi/(180/cla)))-
                          (n1*math.cos(math.pi/(180/gla))))/((n2*math.cos(math.pi/(180/cla)))+
                          (n1*math.cos(math.pi/(180/gla))))
                    tp = ((2*n1*math.cos(math.pi/(180/cla))))/((n2*math.cos(math.pi/(180/cla)))+
                          (n1*math.cos(math.pi/(180/gla))))
                    v = math.atan(n2/n1)
                    w = (v*180)/math.pi
                    print("****************************************************") 
                    print("Brewster angle:",w)
                    q = math.asin(n1/n2)
                    z = (q*180)/math.pi
                    print("Critical angle:", z)
                    print("Angle of refraction within the field:",gla,
                    "\nrs fresnel coefficient:",rs,
                    "\nts fresnel coefficient",ts,
                    "\nrp fresnel coefficient",rp,
                    "\ntp fresnel coefficient",tp)
                    print("****************************************************")
                if n1>n2:
                    v = math.atan(n2/n1)
                    w = (v*180)/math.pi
                    print("****************************************************")
                    print("n1> n2, there is no internal reflection.\nTherefore there is no critical angle.\nFresnel coefficients cannot be calculated.")
                    print("Brewster angle:",w)
                    print("****************************************************")
        if pick == 2:
            while True:
                op1 = 1
                count = 1
                rslist = []
                tslist = []
                rplist = []
                tplist = []
                op1list = []
                print("----------------------------------------------------")
                print("Create a graph of fresnel coefficients spread from 1 to 90 degrees.")
                x = float(input("(n1) --> Refractive index of the first field:"))
                if x == 999:
                    break
                y = float(input("(n2) --> Refractive index of the second field:"))
                if y == 999:
                    break
                print("----------------------------------------------------")
                if x > y :
                    print("****************************************************")
                    print("n1> n2, there is no internal reflection.\nFresnel coefficients cannot be calculated.")
                    print("Give new value.")
                    print("****************************************************")
                if x < y :
                    while True:
                        n1 = x
                        n2 = y
                        a = op1
                        op1list.append(op1)
                        op = math.asin((((n1*math.sin(math.pi/(180/a))/n2))))
                        b=(op*180)/math.pi
                        rs = ((n1*math.cos(math.pi/(180/a)))-
                              (n2*math.cos(math.pi/(180/b))))/((n1*math.cos(math.pi/(180/a)))+
                              (n2*math.cos(math.pi/(180/b))))
                        ts = ((2*n1*math.cos(math.pi/(180/a))))/((n1*math.cos(math.pi/(180/a)))+
                              (n2*math.cos(math.pi/(180/b))))
                        rp = ((n2*math.cos(math.pi/(180/a)))-
                              (n1*math.cos(math.pi/(180/b))))/((n2*math.cos(math.pi/(180/a)))+
                              (n1*math.cos(math.pi/(180/b))))
                        tp = ((2*n1*math.cos(math.pi/(180/a))))/((n2*math.cos(math.pi/(180/a)))+
                              (n1*math.cos(math.pi/(180/b))))
                        rslist.append(rs)
                        tslist.append(ts)
                        rplist.append(rp)
                        tplist.append(tp)
                        op1 = op1+1
                        count = count+1
                        if count == 90:
                            v = math.atan(n2/n1)
                            w = (v*180)/math.pi
                            fig_size = [16,9]
                            plt.figure(figsize=fig_size)
                            plt.plot(op1list,rslist,"--b")
                            plt.plot(op1list,rplist,"--c")
                            plt.plot(op1list,tslist,"-oy")
                            plt.plot(op1list,tplist,"--r")
                            plt.ylim(-1, +1)
                            plt.xlim(0, 90)
                            plt.axvline(w)
                            plt.ylabel("coefficient")
                            plt.xlabel("degree")
                            plt.title("Fresnel coefficients graphic")
                            plt.grid()
                            plt.legend(["rs","rp","ts","tp","brewster","n2/n1 K.A."])
                            print("rs list:",rslist,"\nts list:",tslist,"\nrp list:",rplist,"\ntp list:",tplist)
                            print("Brewster angle:",w)
                            plt.show()
                            rslist.clear()
                            tslist.clear()
                            rplist.clear()
                            tplist.clear()
                            op1list.clear()
                            break