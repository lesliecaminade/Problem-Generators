from generator import constants_conversions as c
from generator import random_handler as ran
import sympy as sym
import math
import random

x, y, z = sym.symbols('x y z', real = True)#generic variables

class boylestad_7_1:
    def __init__(self,*args,**kwargs): 
        print('preparing 7_1')
        regen = True
        while regen:
            vdd = c.voltage(ran.main(16))
            rd = c.resistance(ran.main(2000))
            rg = c.resistance(ran.main(1e6))
            vgg = c.voltage(ran.main(2))
            idss = c.current(ran.main(10), 'mA')
            vgsoff = c.voltage(ran.main(-8))
            
            self.question = f"""Determine: VGSQ, IDQ, VDS, VD, VG, VS for a fixed bias JFET circuit with VDD = {vdd.V:5.4} V, RD = {rd.kohms:5.4} kohms, VGG = {vgg.V:5.4} V, RG = {rg.Mohms:5.4} Mohms, and VSS = 0 V. The JFET has characteristics IDSS = {idss.mA:5.4} mA and Vgsoff = {vgsoff.V:5.4} V. The source is grounded."""
            idsat = c.current(vdd.V / rd.ohms)
            vgs = c.voltage( -vgg.V )
            id = c.current(
            idss.A * (1 - (vgs.V / vgsoff.V))**2 
            )
            vds = c.voltage(vdd.V - id.A * rd.ohms)
            vd = c.voltage(vds.V)
            vg = c.voltage(vgs.V)
            vs = c.voltage(0)
            
            if vgs.V < 0 and vgs.V > vgsoff.V and vds.V > 0 and id.A < idsat.A and id.A < idss.A:
                regen = False
        
        self.answer = f"""VGSQ = {vgs.V:5.4} V, IDQ = {id.mA:5.4} mA, VDS = {vds.V:5.4} V, VD = {vd.V:5.4} V, VG = {vg.V:5.4} V, VS = {vs.V:5.4} V"""

class boylestad_7_2:
    def __init__(self,*args,**kwargs): 
        print('preparing 7_2')
        regen = True
        while regen:
            vdd = c.voltage(ran.main(20))
            rd = c.resistance(ran.main(3300))
            rg = c.resistance(ran.main(1e6))
            rs = c.resistance(ran.main(1e3))
            idss = c.current(ran.main(8), 'mA')
            vgsoff = c.voltage(ran.main(-6))
            
            
            
            self.question = f"""Determine VGSQ, IDQ, VDS, VS, VG, and VD for a self-biased JFET with VDD = {vdd.V:5.4} V, RD = {rd.kohms:5.4} kohms, RG = {rg.Mohms:5.4} Mohms, RS = {rs.kohms:5.4} kohms, and VSS = 0V. The JFET characteristics are IDSS = {idss.mA:5.4} mA and VGSoff = {vgsoff.V:5.4} V. The source resistance and the gate resistance are grounded."""
            
            equation = sym.Eq(
            x,
            idss.A * ( 1 - ((- x * rs.ohms)/(vgsoff.V)) )**2
            )
            idsat = c.current(vdd.V / (rd.ohms + rs.ohms))
            idset = sym.solveset(equation, x)
            idlist = list(idset)
            vgslist = []
            vdslist = []
            
            for i in range(len(idlist)):
                vgslist.append(  - idlist[i] * rs.ohms)
                vdslist.append( vdd.V - idlist[i] * (rs.ohms + rd.ohms))
                
            for i in range(len(idlist)):
                if vgslist[i] < 0 and vgslist[i] > vgsoff.V and vdslist[i] > 0 and idlist[i] < idsat.A and idlist[i] < idss.A:
                    #print(vgslist[i])
                    id = c.current(idlist[i])
                    vgs = c.voltage(vgslist[i])
                    vds = c.voltage(vdslist[i])
                    vs = c.voltage(id.A * rs.ohms)
                    vg = c.voltage(0)
                    vd = c.voltage(vds.V + vs.V)
                    regen = False

        self.answer = f"""VGSQ = {vgs.V:5.4} V, IDQ = {id.mA:5.4} mA, VDS = {vds.V:5.4} V, VS = {vs.V:5.4} V, VG = {vg.V:5.4} V, VD = {vd.V:5.4} V"""
        
        
        
class boylestad_7_4:
    def __init__(self,*args,**kwargs): 
        print('preparing 7_4')
        regen = True
        while regen:
            vdd = c.voltage(ran.main(16))
            rd = c.resistance(ran.main(2.4e3))
            r1 = c.resistance(ran.main(2.1e6))
            r2 = c.resistance(ran.main(270e3))
            rs = c.resistance(ran.main(1.5e3))
            idss = c.current(ran.main(8), 'mA')
            vgsoff = c.voltage(ran.main(-4))
            
            
            self.question = f"""Determine IDQ, VGSQ, VD, VS, VDS, and VDG for a voltage divider biased JFET with VDD = {vdd.V:5.4} V, RD = {rd.kohms:5.4} kohms, RS = {rs.kohms:5.4} kohms, R1(limiter) = {r1.Mohms:5.4} Mohms, R2(bleeder) = {r2.kohms:5.4} kohms and both the bleeder and source resistances are grounded. The JFET characteristics are IDSS = {idss.mA:5.4} mA and VGSoff = {vgsoff.V:5.4} V."""
            
            vg = c.voltage(
            (r2.ohms * vdd.V) / (r1.ohms + r2.ohms)
            )
            
            equation = sym.Eq(
            x,
            idss.A * (1 - ((vg.V - x * rs.ohms) / (vgsoff.V)) )**2
            )
            
            idsat = c.current(vdd.V / (rd.ohms  + rs.ohms ))
            idset = sym.solveset(equation, x)
            idlist = list(idset)
            vgslist = []
            vdslist = []
            
            for i in range(len(idlist)):
                vgslist.append( vg.V - idlist[i] * rs.ohms)
                vdslist.append( vdd.V - idlist[i] * (rd.ohms + rs.ohms))
                
            for i in range(len(idlist)):
                if vgslist[i] < 0 and vgslist[i] > vgsoff.V and vdslist[i] > 0 and idlist[i] < idss.A and idlist[i] < idsat.A:
                    id = c.current(idlist[i])
                    vgs = c.voltage(vgslist[i])
                    vd = c.voltage(vdd.V - id.A * rd.ohms) 
                    vs = c.voltage(id.A * rs.ohms)
                    vds = c.voltage(vdslist[i])
                    vdg = c.voltage(vd.V - vg.V)
                    regen = False
                
        
        self.answer = f"""VGSQ = {vgs.V:5.4} V, IDQ = {id.mA:5.4} mA, VDS = {vds.V:5.4} V, VS = {vs.V:5.4} V, VD = {vd.V:5.4} V, VDG = {vdg.V:5.4} V"""

        
        
        
class boylestad_7_5:
    def __init__(self,*args,**kwargs): 
        print('preparing 7_5')
        regen = True
        while regen:
            vdd = c.voltage(ran.main(12))
            rd = c.resistance(ran.main(1.5e3))
            rs = c.resistance(ran.main(680))
            idss = c.current(ran.main(12), 'mA')
            vgsoff = c.voltage(ran.main(-6))
            
            
            self.question = f"""Determine: VGSQ, IDQ, VD, VG, VS, VDS for a common-gate JFET configuration with VDD = {vdd.V:5.4} V, RD = {rd.kohms:5.4} kohms, RS = {rs.ohms:5.4} ohms, with the gate and the source resistance grounded. The JFET characteristics are IDSS = {idss.mA:5.4} mA and VGSoff = {vgsoff.V:5.4} V.""" 

            
            equation = sym.Eq(
            x,
            idss.A * ( 1 - ((- x * rs.ohms)/(vgsoff.V)) )**2
            )
            
            idsat = c.current(vdd.V / (rd.ohms + rs.ohms))
            idset = sym.solveset(equation, x)
            idlist = list(idset)
            vgslist = []
            vdslist = []
            
            for i in range(len(idlist)):
                vgslist.append( - idlist[i] * rs.ohms)
                vdslist.append(   (vdd.V - idlist[i] * rd.ohms) - (idlist[i] * rs.ohms) )     
                
            for i in range(len(idlist)):
                if vgslist[i] < 0 and vgslist[i] > vgsoff.V and vdslist[i] > 0 and idlist[i] < idsat.A and idlist[i] < idss.A:
                    #print('VDStest' + str(vdslist[i]))
                    id = c.current(idlist[i])
                    vgs = c.voltage(vgslist[i])
                    vds = c.voltage(vdslist[i])
                    vd = c.voltage(vdd.V - id.A * rd.ohms)
                    vg = c.voltage(0)
                    vs = c.voltage(id.A * rs.ohms)
                    regen = False

        self.answer = f"""VGSQ = {vgs.V:5.4} V, IDQ = {id.mA:5.4} mA, VDS = {vds.V:5.4} V, VS = {vs.V:5.4} V, VG = {vg.V:5.4} V, VD = {vd.V:5.4} V"""

class boylestad_7_6:
    def __init__(self,*args,**kwargs): 
        print('preparing 7_6')
        regen = True
        while regen:
            vdd = c.voltage(ran.main(18))
            rd = c.resistance(ran.main(1.8e3))
            r1 = c.resistance(ran.main(110e6))
            r2 = c.resistance(ran.main(10e6))
            rs = c.resistance(ran.main(750))
            idss = c.current(ran.main(6), 'mA')
            vgsoff = c.voltage(ran.main(-3))
            
            
            self.question  = f"""For an n - channel depletion type MOSFET biased by a voltage divider method, determine IDQ, VGSQ, and VDS, if VDD = {vdd.V:5.4} V, RD = {rd.kohms:5.4} kohms, R1(limiter) = {r1.Mohms:5.4} Mohms, R2(bleeder) = {r2.Mohms:5.4} Mohms, RS = {rs.ohms:5.4} ohms. The bleeder resistor and the source resistor are grounded. The JFET characteristics are IDSS = {idss.mA:5.4} mA and VGSoff = {vgsoff.V:5.4} V."""
            
            vg = c.voltage(
            (vdd.V * r2.ohms) / (r1.ohms + r2.ohms)
            )
            
            equation = sym.Eq(
            x,
            idss.A * (1 - ((vg.V - x * rs.ohms) / (vgsoff.V)) )**2
            )
            idsat = c.current(vdd.V / (rd.ohms + rs.ohms))
            idset = sym.solveset(equation, x)
            idlist = list(idset)
            vgslist = []
            vdslist = []
            
            for i in range(len(idlist)):
                vgslist.append(vg.V - idlist[i] * rs.ohms)
                vdslist.append(vdd.V - idlist[i] * (rs.ohms + rd.ohms))
            
            for i in range(len(idlist)):
                if vdslist[i] > 0 and vgslist[i] > vgsoff.V and idlist[i] < idsat.A:
                    id = c.current(idlist[i])
                    vgs = c.voltage(vgslist[i])
                    vds = c.voltage(vdslist[i])
                    regen = False
                    
        self.answer = f"""IDQ = {id.mA:5.4} mA, VGSQ = {vgs.V:5.4} V, VDS = {vds.V:5.4} V"""


class boylestad_7_8:
    def __init__(self,*args,**kwargs): 
        print('preparing 7_8')
        regen = True
        while regen:
            vdd = c.voltage(ran.main(18))
            rd = c.resistance(ran.main(1.8e3))
            r1 = c.resistance(ran.main(110e6))
            r2 = c.resistance(ran.main(10e6))
            rs = c.resistance(ran.main(750))
            idss = c.current(ran.main(6), 'mA')
            vgsoff = c.voltage(ran.main(-3))
            
            
            self.question  = f"""For an n - channel depletion type MOSFET biased by a voltage divider method, determine IDQ, VGSQ, and VDS, if VDD = {vdd.V:5.4} V, RD = {rd.kohms:5.4} kohms, R1(limiter) = {r1.Mohms:5.4} Mohms, R2(bleeder) = {r2.Mohms:5.4} Mohms, RS = {rs.ohms:5.4} ohms. The bleeder resistor and the source resistor are grounded. The JFET characteristics are IDSS = {idss.mA:5.4} mA and VGSoff = {vgsoff.V:5.4} V."""
            
            vg = c.voltage(
            (vdd.V * r2.ohms) / (r1.ohms + r2.ohms)
            )
            
            equation = sym.Eq(
            x,
            idss.A * (1 - ((vg.V - x * rs.ohms) / (vgsoff.V)) )**2
            )
            idsat = c.current(vdd.V / (rs.ohms + rd.ohms))
            idset = sym.solveset(equation, x)
            idlist = list(idset)
            vgslist = []
            vdslist = []
            
            for i in range(len(idlist)):
                vgslist.append(vg.V - idlist[i] * rs.ohms)
                vdslist.append(vdd.V - idlist[i] * (rs.ohms + rd.ohms))
            
            for i in range(len(idlist)):
                if vdslist[i] > 0 and vgslist[i] > vgsoff.V and idlist[i] < idsat.A:
                    id = c.current(idlist[i])
                    vgs = c.voltage(vgslist[i])
                    vds = c.voltage(vdslist[i])
                    regen = False
                    
        self.answer = f"""IDQ = {id.mA:5.4} mA, VGSQ = {vgs.V:5.4} V, VDS = {vds.V:5.4} V"""


class boylestad_7_10:
    def __init__(self,*args,**kwargs): 
        print('preparing 7_10')
        regen = True
        while regen:
            vdd = c.voltage(ran.main(12))
            rd = c.resistance(ran.main(2000))
            rf = c.resistance(ran.main(10e6))
            idon = c.current(ran.main(6), 'mA')
            vgsth = c.voltage(ran.main(3))
            vgson = c.voltage(vgsth.V + ran.main(5))
            
            self.question = f"""Determine IDQ and VDSQ for an enhancement type MOSFET that uses a feedback biasing arrangement with VDD = {vdd.V:5.4} V, RD = {rd.kohms:5.4} kohms, RF = {rf.Mohms:5.4} Mohms, and the source grounded. The MOSFET has characteristics IDon = {idon.mA:5.4} mA, VGSon = {vgson.V:5.4} V, and VGSth = {vgsth.V:5.4} V."""
            
            k  = (idon.A) / ((vgson.V - vgsth.V)**2)
            
            equation = sym.Eq(
            x,
            k * (( ((vdd.V) - (x * rd.ohms)) - vgsth.V )**2)
            )
            idsat = c.current(vdd.V / (rd.ohms))
            idset = sym.solveset(equation, x, domain = sym.Reals)
            idlist = list(idset)
            vgslist = []
            vdslist = []
            
            for i in range(len(idlist)):
                vgslist.append(vdd.V - idlist[i] * rd.ohms)
                vdslist.append(vdd.V - idlist[i] * rd.ohms)
            
            for i in range(len(idlist)):
                if vgslist[i] > vgsth.V and vdslist[i] > 0:
                    id = c.current(idlist[i])
                    vgs = c.voltage(vgslist[i])
                    vds = c.voltage(vgs.V)
                    regen = False
                
        self.answer = f"""IDQ = {id.mA:5.4} mA, VDSQ = {vds.V:5.4} V"""

class boylestad_7_11:
    def __init__(self,*args,**kwargs): 
        print('preparing 7_11')
        regen = True
        while regen:
            vdd = c.voltage(ran.main(40))
            rd = c.resistance(ran.main(3000))
            r1 = c.resistance(ran.main(22e6))
            r2 = c.resistance(ran.main(18e6))
            rs = c.resistance(ran.main(0.82e3))
            vgsth = c.voltage(ran.main(5))
            idon = c.current(ran.main(3), 'mA')
            vgson = c.voltage(vgsth.V + ran.main(5))
            
            self.question = f"""Determine IDQ, VGSQ, and VDS for an enhancement MOSFET in a voltage divider configuration where VDD = {vdd.V:5.4} V, RD = {rd.kohms:5.4} kohms, R1(limiter) = {r1.Mohms:5.4} Mohms, RS = {rs.kohms:5.4} kohms, R2(bleeder) = {r2.Mohms:5.4} Mohms where the bleeder and the source resistors are grounded. The MOSFET has characteristics VGSth = {vgsth.V:5.4} V, IDon = {idon.mA:5.4} mA at VGSon = {vgson.V:5.4} V."""
            
            vg = c.voltage(
            (vdd.V * r2.ohms) / (r2.ohms + r1.ohms)
            )
            
            k = (idon.A) / ((vgson.V - vgsth.V)**2)

            
            equation = sym.Eq(
            x,
            k * (((vg.V - x * rs.ohms) - vgsth.V )**2)
            )
            idsat = c.current(vdd.V / (rd.ohms + rs.ohms))
            idset = sym.solveset(equation, x, domain = sym.Reals)
            idlist = list(idset)
            vgslist = []
            vdslist = []
            
            for i in range(len(idlist)):
                vgslist.append(vg.V - idlist[i] * rs.ohms)
                vdslist.append(vdd.V - idlist[i] * (rs.ohms + rd.ohms))
                
            for i in range(len(idlist)):
                if vgslist[i] > vgsth.V and vdslist[i] > 0:
                    id = c.current(idlist[i])
                    vgs = c.voltage(vgslist[i])
                    vds = c.voltage(vdslist[i])
                    regen = False
                    
        self.answer = f"""IDQ = {id.mA:5.4} mA, VGSQ = {vgs.V:5.4} V, VDS = {vds.V:5.4} V"""



class boylestad_8_7:
    def __init__(self,*args,**kwargs): 
        print('preparing 8_7')
        regen = True
        while regen:
            vdd = c.voltage(ran.main(16))
            rd = c.resistance(ran.main(2000))
            rg = c.resistance(ran.main(1e6))
            vgg = c.voltage(ran.main(2))
            idss = c.current(ran.main(10), 'mA')
            vgsoff = c.voltage(ran.main(-8))
            yos = c.conductance(ran.main(40), 'uS')
            
            self.question = f"""Determine: gm, rd, Zi, Zo, Av considering rd, and Av without considering rd, for a fixed bias JFET circuit with VDD = {vdd.V:5.4} V, RD = {rd.kohms:5.4} kohms, VGG = {vgg.V:5.4} V, RG = {rg.Mohms:5.4} Mohms, and VSS = 0 V. The JFET has characteristics IDSS = {idss.mA:5.4} mA and Vgsoff = {vgsoff.V:5.4} V. The source is grounded."""
            
            
            idsat = c.current(vdd.V / rd.ohms)
            vgs = c.voltage( -vgg.V )
            id = c.current(
            idss.A * (1 - (vgs.V / vgsoff.V))**2 
            )
            vds = c.voltage(vdd.V - id.A * rd.ohms)
            vd = c.voltage(vds.V)
            vg = c.voltage(vgs.V)
            vs = c.voltage(0)
            
            if vgs.V < 0 and vgs.V > vgsoff.V and vds.V > 0 and id.A < idsat.A and id.A < idss.A:
                regen = False
                
        gm = c.conductance( 
        (2 * idss.A / abs(vgsoff.V)) * ( 1 -  (vgs.V / vgsoff.V))
        )
        
        rdsmall = c.resistance( 1/ yos.S )
        
        zi = c.resistance( rg.ohms )
        
        zo = rd.parallel(rdsmall)
        
        av = - gm.S * zo.ohms
        
        av_nord = - gm.S * rd.ohms
            
        self.answer = f"""gm = {gm.mS:5.4} mS, rd = {rdsmall.kohms:5.4} kohms, zi = {zi.Mohms:5.4} Mohms, zo = {zo.kohms:5.4} kohms, Av considering rd = {av:5.4}, Av without considering rd = {av_nord:5.4}"""


class boylestad_8_8:
    def __init__(self,*args,**kwargs): 
        print('preparing 8_8')
        regen = True
        while regen:
            vdd = c.voltage(ran.main(20))
            rd = c.resistance(ran.main(3300))
            rg = c.resistance(ran.main(1e6))
            rs = c.resistance(ran.main(1e3))
            idss = c.current(ran.main(8), 'mA')
            vgsoff = c.voltage(ran.main(-6))
            gos = c.conductance(ran.main(20), 'uS')
            
            
            
            self.question = f"""Determine gm, rd, Zi, Zo with and without the effects of rd, and Av with and without the effects of rd, for a self-biased unbypased source resistance JFET with VDD = {vdd.V:5.4} V, RD = {rd.kohms:5.4} kohms, RG = {rg.Mohms:5.4} Mohms, RS = {rs.kohms:5.4} kohms, and VSS = 0V. The JFET characteristics are IDSS = {idss.mA:5.4} mA and VGSoff = {vgsoff.V:5.4} V. The source resistance and the gate resistance are grounded. The value of gos = {gos.uS:5.4} uS"""
            
            equation = sym.Eq(
            x,
            idss.A * ( 1 - ((- x * rs.ohms)/(vgsoff.V)) )**2
            )
            idsat = c.current(vdd.V / (rd.ohms + rs.ohms))
            idset = sym.solveset(equation, x)
            idlist = list(idset)
            vgslist = []
            vdslist = []
            
            for i in range(len(idlist)):
                vgslist.append(  - idlist[i] * rs.ohms)
                vdslist.append( vdd.V - idlist[i] * (rs.ohms + rd.ohms))
                
            for i in range(len(idlist)):
                if vgslist[i] < 0 and vgslist[i] > vgsoff.V and vdslist[i] > 0 and idlist[i] < idsat.A and idlist[i] < idss.A:
                    #print(vgslist[i])
                    id = c.current(idlist[i])
                    vgs = c.voltage(vgslist[i])
                    vds = c.voltage(vdslist[i])
                    vs = c.voltage(id.A * rs.ohms)
                    vg = c.voltage(0)
                    vd = c.voltage(vds.V + vs.V)
                    regen = False
                    
        gm = c.conductance( 
        (2 * idss.A / abs(vgsoff.V)) * (1 - (vgs.V) / (vgsoff.V))
        )
        
        rdsmall = c.resistance( 1 / gos.S)
        
        zi = c.resistance( rg.ohms )
        
        zo = c.resistance( 
        ((1 + gm.S * rs.ohms + (rs.ohms/rdsmall.ohms)) * rd.ohms ) / 
        (1 + gm.S * rs.ohms + (rs.ohms/rdsmall.ohms) + (rd.ohms / rdsmall.ohms))
        )
        
        zo_nord = c.resistance( rd.ohms )
        
        av = (
        ( - gm.S * rd.ohms ) / 
        (1 + gm.S * rs.ohms + (rs.ohms/rdsmall.ohms) + (rd.ohms / rdsmall.ohms))
        )
        
        av_nord = (
        ( - gm.S * rd.ohms )/
        ( 1 + gm.S * rs.ohms )
        )
            
        self.answer = f"""gm = {gm.mS:5.4} mS, rd = {rdsmall.kohms:5.4} kohms, zi = {zi.Mohms:5.4} Mohms, zo considering rd = {zo.kohms:5.4} kohms, zo without considering rd = {zo_nord.kohms:5.4} kohms, Av considering rd = {av:5.4}, Av without considering rd = {av_nord:5.4}"""   

class boylestad_8_9:
    def __init__(self,*args,**kwargs): 
        print('preparing 8_9')
        regen = True
        while regen:
            vdd = c.voltage(ran.main(12))
            rd = c.resistance(ran.main(3.6e3))
            rs = c.resistance(ran.main(1.1e3))
            idss = c.current(ran.main(10), 'mA')
            vgsoff = c.voltage(ran.main(-4))
            gos = c.conductance(ran.main(50), 'uS')
            vi = c.voltage(ran.main(40), 'mV')
            
            self.question = f"""Determine: gm, rd, Zi with and without considering rd, Zo with and without considering rd, and Vo with and without considering rd for a common-gate JFET configuration with VDD = {vdd.V:5.4} V, RD = {rd.kohms:5.4} kohms, RS = {rs.ohms:5.4} ohms, with the gate and the source resistance grounded. The JFET characteristics are IDSS = {idss.mA:5.4} mA, VGSoff = {vgsoff.V:5.4} V, gos = {gos.uS:5.4} uS and the input is a {vi.mV:5.4} mV signal.""" 

            
            equation = sym.Eq(
            x,
            idss.A * ( 1 - ((- x * rs.ohms)/(vgsoff.V)) )**2
            )
            
            idsat = c.current(vdd.V / (rd.ohms + rs.ohms))
            idset = sym.solveset(equation, x)
            idlist = list(idset)
            vgslist = []
            vdslist = []
            
            for i in range(len(idlist)):
                vgslist.append( - idlist[i] * rs.ohms)
                vdslist.append(   (vdd.V - idlist[i] * rd.ohms) - (idlist[i] * rs.ohms) )     
                
            for i in range(len(idlist)):
                if vgslist[i] < 0 and vgslist[i] > vgsoff.V and vdslist[i] > 0 and idlist[i] < idsat.A and idlist[i] < idss.A:
                    #print('VDStest' + str(vdslist[i]))
                    id = c.current(idlist[i])
                    vgs = c.voltage(vgslist[i])
                    vds = c.voltage(vdslist[i])
                    vd = c.voltage(vdd.V - id.A * rd.ohms)
                    vg = c.voltage(0)
                    vs = c.voltage(id.A * rs.ohms)
                    regen = False
                         
        gm = c.conductance( 
        (2 * idss.A / abs(vgsoff.V)) * (1 - (vgs.V) / (vgsoff.V))
        )
        
        rdsmall = c.resistance( 1 / gos.S)
        
        zi = rs.parallel(c.resistance(
        (rdsmall.ohms + rd.ohms) / 
        (1 + gm.S * rdsmall.ohms))
        )
        
        zi_nord = rs.parallel(c.resistance(1 / gm.S))
        
        zo = rd.parallel(rdsmall)
        
        zo_nord = c.resistance(rd.ohms)
        
        av = (
        (gm.S * rd.ohms + (rd.ohms / rdsmall.ohms)) / 
        (1 + (rd.ohms/ rdsmall.ohms))
        )
        
        av_nord = gm.S * rd.ohms
        
        vo = c.voltage( vi.V * av)
        
        vo_nord = c.voltage( vi.V * av_nord)
        
        self.answer = f"""gm = {gm.mS:5.4} mS, rd = {rdsmall.kohms:5.4} kohms, zi considering rd= {zi.kohms:5.4} kohms, zi without considering rd = {zi_nord.kohms:5.4} kohms, zo considering rd = {zo.kohms:5.4} kohms, zo without considering rd = {zo_nord.kohms:5.4} kohms, vo considering rd = {vo.V:5.4} V, vo without considering rd = {vo_nord.V:5.4} V"""  
        
class boylestad_8_10:
    def __init__(self,*args,**kwargs): 
        print('preparing 8_10')
        regen = True
        while regen:
            vdd = c.voltage(ran.main(9))
            rs = c.resistance(ran.main(2.2e3))
            rg = c.resistance(ran.main(1e6))
            idss = c.current(ran.main(16), 'mA')
            vgsoff = c.voltage(ran.main(-4))
            gos = c.conductance(ran.main(25), 'uS')
            
            self.question = f"""A source follower network has VDD = {vdd.V:5.4} V, RS = {rs.kohms:5.4} kohms, RG = {rg.Mohms:5.4} Mohms. The gate resistance and the source resistance are both grounded. The network uses a JFET with characteristics IDSS = {idss.mA:5.4} mA, VGSoff = {vgsoff.V:5.4} V, and gos = {gos.uS:5.4} uS. Determine gm, rd, Zi, Zo with and without considering rd, and Av with and without considering rd."""
            
            equation = sym.Eq(
            x,
            idss.A * ( 1 - (( - x * rs.ohms) / (vgsoff.V)))**2
            )
            
            idsat = c.current(vdd.V / rs.ohms)
            idset = sym.solveset(equation, x)
            idlist = list(idset)
            vgslist = []
            vdslist = []
            
            for i in range(len(idlist)):
                vgslist.append( - idlist[i] * rs.ohms)
                vdslist.append( vdd.V - idlist[i] * rs.ohms )     
                
            for i in range(len(idlist)):
                if vgslist[i] < 0 and vgslist[i] > vgsoff.V and vdslist[i] > 0 and idlist[i] < idsat.A and idlist[i] < idss.A:
                    #print('VDStest' + str(vdslist[i]))
                    id = c.current(idlist[i])
                    vgs = c.voltage(vgslist[i])
                    vds = c.voltage(vdslist[i])
                    vd = c.voltage( vdd.V )
                    vg = c.voltage( vgs.V )
                    vs = c.voltage( id.A * rs.ohms )
                    regen = False
                
        gm = c.conductance( 
        (2 * idss.A / abs(vgsoff.V)) * (1 - (vgs.V) / (vgsoff.V))
        )
        
        rdsmall = c.resistance( 1 / gos.S)
        
        zi = c.resistance(rg.ohms)
        
        zo = rdsmall.parallel(rs).parallel(c.resistance(1/gm.S))
        
        zo_nord = rs.parallel(c.resistance(1/gm.S))
        
        av = (
        ( gm.S * (rdsmall.parallel(rs).ohms)) / 
        ( 1 + gm.S * (rdsmall.parallel(rs).ohms))
        )
        
        av_nord = (
        (gm.S * rs.ohms) /
        (1 + gm.S * rs.ohms)
        )
        
        self.answer = f"""gm = {gm.mS:5.4} mS, rd = {rdsmall.kohms:5.4} kohms, zi = {zi.kohms:5.4} kohms, zo considering rd = {zo.kohms:5.4} kohms, zo without considering rd = {zo_nord.kohms:5.4} kohms, av considering rd = {av:5.4}, av without considering rd = {av_nord:5.4}"""


class boylestad_8_11:
    def __init__(self,*args,**kwargs): 
        print('preparing 8_11')
        regen = True
        while regen:
            vdd = c.voltage(ran.main(18))
            r1 = c.resistance(ran.main(110e6))
            r2 = c.resistance(ran.main(10e6))
            rd = c.resistance(ran.main(1.8e3))
            rs = c.resistance(ran.main(150))
            idss = c.current(ran.main(6), 'mA')
            vgsoff = c.voltage(ran.main(-3))
            gos = c.conductance(ran.main(10), 'uS')
            
            self.question = f"""An n - channel DMOSFET is biased in a common source,  voltage divider network with VDD = {vdd.V:5.4} V, RD = {rd.kohms:5.4} kohms, RS = {rs.ohms:5.4} ohms, R1 (limiter) = {r1.Mohms:5.4} Mohms and R2 (bleeder) = {r2.Mohms:5.4} Mohms. The source resistance and the bleeder resistance are grounded with an installed bypass capacitor across the source resistance. The DMOSFET characteristics are IDSS = {idss.mA:5.4} mA, VGSoff = {vgsoff.V:5.4} V and gos = {gos.uS:5.4} uS. Determine gm, rd, Zi, Zo and Av."""
            
            
            vg = c.voltage(
            (vdd.V * r2.ohms) / (r1.ohms + r2.ohms)
            )
            
            equation = sym.Eq(
            x, 
            idss.A * ( 1 - ( ( vg.V - x * rs.ohms ) / ( vgsoff.V)  ))**2
            )
            
            
            idsat = c.current(vdd.V / (rs.ohms + rd.ohms))
            idset = sym.solveset(equation, x)
            idlist = list(idset)
            vgslist = []
            vdslist = []
            
            for i in range(len(idlist)):
                vgslist.append( vg.V - idlist[i] * rs.ohms)
                vdslist.append( vdd.V - idlist[i] * (rs.ohms + rd.ohms) )     
                
            for i in range(len(idlist)):
                if vgslist[i] > vgsoff.V and vdslist[i] > 0 and idlist[i] < idsat.A:  #and idlist[i] < idss.A: vgslist[i] < 0 and
                    id = c.current(idlist[i])
                    vgs = c.voltage(vgslist[i])
                    vds = c.voltage(vdslist[i])
                    regen = False
                    
        gm = c.conductance( 
        (2 * idss.A / abs(vgsoff.V)) * (1 - ((vgs.V) / (vgsoff.V)))
        )
        
        rdsmall = c.resistance( 1 / gos.S)
        
        zi = r1.parallel(r2)
        
        zo = rdsmall.parallel(rd)

        av = - gm.S * zo.ohms

        self.answer = f"""gm = {gm.mS:5.4} mS, rd = {rdsmall.kohms:5.4} kohms, Zi = {zi.Mohms:5.4} Mohms, Zo = {zo.kohms:5.4} kohms, Av = {av:5.4}"""


class boylestad_8_12:
    def __init__(self,*args,**kwargs): 
        print('preparing 8_12')
        regen = True
        while regen:
            vdd = c.voltage(ran.main(12))
            rd = c.resistance(ran.main(2000))
            rf = c.resistance(ran.main(10e6))
            idon = c.current(ran.main(6), 'mA')
            vgsth = c.voltage(ran.main(3))
            vgson = c.voltage(vgsth.V + ran.main(5))
            gos = c.conductance(ran.main(20), 'uS')
            
            self.question = f"""Determine gm, rd, Zi with and without rd, Zo with and without rd, and Av with and without rd, for an enhancement type MOSFET that uses a feedback biasing arrangement with VDD = {vdd.V:5.4} V, RD = {rd.kohms:5.4} kohms, RF = {rf.Mohms:5.4} Mohms, and the source grounded. The MOSFET has characteristics IDon = {idon.mA:5.4} mA, VGSon = {vgson.V:5.4} V, and VGSth = {vgsth.V:5.4} V. Note also that gos = {gos.uS:5.4} uS"""
            
            k  = (idon.A) / ((vgson.V - vgsth.V)**2)
            
            equation = sym.Eq(
            x,
            k * (( ((vdd.V) - (x * rd.ohms)) - vgsth.V )**2)
            )
            idsat = c.current(vdd.V / (rd.ohms))
            idset = sym.solveset(equation, x, domain = sym.Reals)
            idlist = list(idset)
            vgslist = [0]
            vdslist = [0]
            
            for i in range(len(idlist)):
                vgslist.append(vdd.V - idlist[i] * rd.ohms)
                vdslist.append(vdd.V - idlist[i] * rd.ohms)
            
            for i in range(len(idlist)):
                if vgslist[i] > vgsth.V and vdslist[i] > 0:
                    id = c.current(idlist[i])
                    vgs = c.voltage(vgslist[i])
                    vds = c.voltage(vgs.V)
                    regen = False
        
        gm = c.conductance( 2 * k * (vgs.V - vgsth.V ))
        rdsmall = c.resistance(1 / gos.S)
        zi = c.resistance(
        (rf.ohms + rdsmall.parallel(rd).ohms ) / 
        (1 + gm.S * (rdsmall.parallel(rd).ohms))
        )
        zi_nord = c.resistance(
        (rf.ohms) / 
        (1 + gm.S * rd.ohms)
        )
        zo = rf.parallel(rdsmall).parallel(rd)
        zo_nord = c.resistance(rd.ohms)
        av = - gm.S * zo.ohms
        av_nord = - gm.S * zo_nord.ohms
        
        self.answer = f"""gm = {gm.mS:5.4} mS, rd = {rdsmall.kohms:5.4} kohms, Zi considering rd = {zi.Mohms:5.4} Mohms, Zi without considering rd = {zi_nord.Mohms:5.4} Mohms, Zo considering rd = {zo.kohms:5.4} kohms, Zo without considering rd = {zo_nord.kohms:5.4} kohms, Av considering rd = {av:5.4}, Av without considering rd = {av_nord:5.4}"""



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        