import random_handler as ran
import sympy as sym
import math
import random
import constants_conversions as c

x, y, z = sym.symbols('x y z', real = True)#generic variables
vbe = c.voltage(0.7)

class boylestad_4_1:
    def __init__(self,*args,**kwargs): 
        print("4_1")
        regen = 1
        while regen:
            vcc = c.voltage(ran.main(12))
            rb = c.resistance(ran.main(240), 'kohms')
            rc = c.resistance(ran.main(2.2), 'kohms')
            beta = ran.main(50)
            self.question = f"""Determine IBQ, ICQ, VCEQ, VB, VC and VBC for the fixed bias configuration. VCC = {vcc.V} V, RB = {rb.kohms} kohms, RC = {rc.kohms} kohms, beta = {beta}.
            https://lesliecaminadecom.files.wordpress.com/2019/07/0p4d1k1aqsv36ctyg63x.png"""
            
            ib = c.current(
            (vcc.V - vbe.V) / rb.ohms
            )
            
            ic = c.current(
            beta * ib.A
            )
            
            vce = c.voltage(
            vcc.V - ic.A * rc.ohms
            )
            
            vb = c.voltage( vbe.V )
            vc = c.voltage( vce.V )
            vbc = c.voltage( vb.V - vc.V )
            
            if ic.A < vcc.V / rc.ohms:
                regen = 0
        
        self.answer = f"""IB = {ib.uA} uA, IC = {ic.mA} mA, VCE = {vce.V} V, VB = {vb.V} V, VC = {vc.V} V, VBC = {vbc.V} V"""

class boylestad_4_2:
    def __init__(self,*args,**kwargs): 
        print("4_2")
        vcc = c.voltage(ran.main(12))
        rb = c.resistance(ran.main(240), 'kohms')
        rc = c.resistance(ran.main(2.2), 'kohms')
        beta = ran.main(50)
        self.question = f"""Determine the saturation level for the fixed bias configuration. VCC = {vcc.V} V, RB = {rb.kohms} kohms, RC = {rc.kohms} kohms, beta = {beta}. 
        https://lesliecaminadecom.files.wordpress.com/2019/07/0p4d1k1aqsv36ctyg63x.png"""
        
        icsat = c.current(
        vcc.V / rc.ohms
        )
        
        self.answer = f"""ICsat = {icsat.mA} mA"""
        
class boylestad_4_3:
    def __init__(self,*args,**kwargs):
        print("4_3")
        regen = 1
        while regen:
            vcc = c.voltage(ran.main(20))
            rb = c.resistance(ran.main(430), 'kohms')
            rc = c.resistance(ran.main(2), 'kohms')
            re = c.resistance(ran.main(1000), 'ohms')
            beta = ran.main(50)
            
            self.question = f"""For the emitter-bias network, determine IB, IC, VCE, VC, VE, VB, VBC for the values VCC = {vcc.V} V, RB = {rb.kohms} kohms, RC = {rc.kohms} kohms, RE = {re.ohms} ohms, beta = {beta}.
            https://lesliecaminadecom.files.wordpress.com/2019/07/fr18ylk5mr6cfhryt59w.png"""
            
            ib = c.current(
            (vcc.V - vbe.V) / (rb.ohms + (beta + 1) * re.ohms)
            )
        
            ic = c.current( beta * ib.A )
            
            if ic.A < (vcc.V / (re.ohms + rc.ohms)):
                regen = 0
        
        vce = c.voltage(
        vcc.V - ic.A * (re.ohms + rc.ohms)
        )
        
        vc = c.voltage(
        vcc.V - ic.A * rc.ohms
        )
        
        ve = c.voltage(
        vc.V - vce.V
        )
        
        vb = c.voltage(
        vbe.V + ve.V
        )
        
        vbc = c.voltage(
        vb.V - vc.V
        )
        
        self.answer = f"""IB = {ib.uA} uA, IC = {ic.mA} mA, VCE = {vce.V} V, VC = {vc.V} V, VE = {ve.V} V, VB = {vb.V} V, VBC = {vbc.V} V"""
        
class boylestad_4_6:
    def __init__(self,*args,**kwargs): 
        print("4_6")
        vcc = c.voltage(ran.main(20))
        rb = c.resistance(ran.main(430), 'kohms')
        rc = c.resistance(ran.main(2), 'kohms')
        re = c.resistance(ran.main(1000), 'ohms')
        beta = ran.main(50)
        
        self.question = f"""For the emitter-bias network, determine the saturation current for the values VCC = {vcc.V} V, RB = {rb.kohms} kohms, RC = {rc.kohms} kohms, RE = {re.ohms} ohms, beta = {beta}.
        https://lesliecaminadecom.files.wordpress.com/2019/07/fr18ylk5mr6cfhryt59w.png"""
   
        icsat = c.current(
        vcc.V / (re.ohms + rc.ohms)
        )
            
        self.answer = f"""ICsat = {icsat.A} A"""
            
class boylestad_4_8:
    def __init__(self,*args,**kwargs):
        print("4_8")
        regen = 1
        while regen:
            vcc = c.voltage(ran.main(22))
            r1 = c.resistance(ran.main(39), 'kohms')
            r2 = c.resistance(ran.main(3.9), 'kohms')
            rc = c.resistance(ran.main(10), 'kohms')
            re = c.resistance(ran.main(1.5), 'kohms')
            beta = ran.main(100)
            
            self.question = f"""Determine the DC bias voltage VCE and the current IC for the voltage divider configuration. VCC = {vcc.V} V, R1(top) = {r1.kohms} kohms, R2(bottom) = {r2.kohms} kohms, RC = {rc.kohms} kohms, RE = {re.kohms} kohms, beta = {beta}.
            https://lesliecaminadecom.files.wordpress.com/2019/07/s2zbg7wry8s4nov813u4.png"""
            
            rth = r1.parallel(r2)
            
            eth = c.voltage(
            ( r2.ohms * vcc.V ) / ( r1.ohms + r2.ohms ) 
            )
            
            ib = c.current(
            (eth.V - vbe.V) / (rth.ohms + (beta + 1) * re.ohms)
            )
            
            ic = c.current(
            beta * ib.A
            )
            
            vce = c.voltage(
            vcc.V - ic.A * (rc.ohms + re.ohms)
            )
            
            if ic.A < (vcc.V / (re.ohms + rc.ohms)):
                regen = 0
            
        self.answer = f"""IC = {ic.mA} mA, VCE = {vce.V} V"""
        
class boylestad_4_12:
    def __init__(self,*args,**kwargs): 
        print("4_12")
        regen = 1
        while regen:
            vcc = c.voltage(ran.main(10))
            rc = c.resistance(ran.main(4.7), 'kohms')
            rf = c.resistance(ran.main(250), 'kohms')
            re = c.resistance(ran.main(1.2), 'kohms')
            beta = ran.main(90)
            
            self.question = f"""Determine the quiescent levels of IC and VCE for the network where VCC = {vcc.V} V, RC = {rc.kohms} kohms, RF = {rf.kohms} kohms, RE = {re.kohms} kohms, and beta = {beta} 
            https://lesliecaminadecom.files.wordpress.com/2019/07/vu3z85fuaeeq72rhgbrn.png"""
            
            ib = c.current(
            (vcc.V - vbe.V) / (rf.ohms + beta * ( rc.ohms + re.ohms ) )
            )
            
            ic = c.current(
            beta * ib.A
            )
        
            if ic.A < (vcc.V / ( rc.ohms + re.ohms )):
                regen = 0
                
        vce = c.voltage(
        vcc.V - ic.A * ( rc.ohms + re.ohms )
        )
        
        self.answer = f"""IC = {ic.mA} mA
VCE = {vce.V} V"""

class boylestad_4_14:
    def __init__(self,*args,**kwargs): 
        print("4_14")
        regen = 1
        while regen:
            vcc = c.voltage(ran.main(18))
            rc = c.resistance(ran.main(3.3), 'kohms')
            rf2 = c.resistance(ran.main(110), 'kohms')
            rf1 = c.resistance(ran.main(91), 'kohms')
            re = c.resistance(ran.main(510), 'ohms')
            beta = ran.main(75)
            
            self.question = f"""Determine the DC level of IB and VC for the network. VCC = {vcc.V} V, RC = {rc.kohms} kohms, RF1 = {rf1.kohms} kohms, RF2 = {rf2.kohms} kohms, RE = {re.kohms} kohms, and beta = {beta}. 
            https://lesliecaminadecom.files.wordpress.com/2019/07/f21o27k3wek108bofwtq.png"""
            
            ib = c.current(
            (vcc.V - vbe.V) / (rf1.ohms + rf2.ohms + beta * ( rc.ohms + re.ohms ))
            )
            
            ic = c.current(
            beta * ib.A
            )
            
            ie = c.current(
            ib.A + ic.A
            )
            
            if ie.A < (vcc.V / (rc.ohms + re.ohms)):
                regen = 0
        
        vc = c.voltage(
        vcc.V - ie.A * rc.ohms
        )
        
        self.answer = f"""IB = {ib.uA} uA
VC = {vc.V} V"""

class boylestad_4_16:
    def __init__(self,*args,**kwargs): 
        print("4_16")
        regen = 1
        while regen:
            vee = c.voltage(ran.main(-20))
            re = c.resistance(ran.main(2), 'kohms')
            rb = c.resistance(ran.main(240), 'kohms')
            beta = ran.main(90)
            
            self.question = f"""Determine VCE and IE for the network where VEE = {vee.V} V, RE = {re.kohms} kohms, RB = {rb.kohms} kohms, and beta = {beta}. 
            https://lesliecaminadecom.files.wordpress.com/2019/07/sjrsnbmupqf31688aept.png"""
            
            ib = c.current(
            (-vee.V - vbe.V) / (rb.ohms + (beta + 1) * re.ohms)
            )
            
            vce = c.voltage(
            - vee.V - (beta + 1) * ib.A * re.ohms
            )
            
            ie = c.current(
            (beta + 1) * ib.A
            )
            
            if ie.A < (-vee.V / re.ohms):
                regen = 0
        
        
        self.answer = f"""VCE = {vce.V} V
IE = {ie.mA} mA"""


class boylestad_4_17:
    def __init__(self,*args,**kwargs):
        print("4_17")
        regen = 1
        while regen:
            vcc = c.voltage(ran.main(10))
            vee = c.voltage(ran.main(4))
            re = c.resistance(ran.main(1.2), 'kohms')
            rc = c.resistance(ran.main(2.4), 'kohms')
            beta = ran.main(60)
            
            self.question = f"""Determine the current IE and IB and the voltages VCE and VCB for the common-base configuration where VEE = {vee.V} V, VCC = {vcc.V} V, RE = {re.kohms} kohms, RC ={rc.kohms} kohms and beta = {beta}.
            https://lesliecaminadecom.files.wordpress.com/2019/07/iea7tq05l6f34euza4q7.png"""
            
            ie = c.current(
            (vee.V - vbe.V) / re.ohms
            )
            
            ib = c.current(
            ie.A / (beta + 1)
            )
            
            vce = c.voltage(
            vee.V + vcc.V - ie.A * (rc.ohms + re.ohms)
            )
            
            if vce.V > 0:
                regen = 0
                
        vcb = c.voltage(
        vcc.V - beta * ib.A * rc.ohms
        )
        
        self.answer = f"""IE = {ie.mA} mA
IB = {ib.uA} uA
VCE = {vce.V} V
VCB = {vcb.V} V"""

class boylestad_4_18:
    def __init__(self,*args,**kwargs): 
        print("4_18")
        regen = 1
        while regen:
        
            vcc = c.voltage(ran.main(20))
            rc = c.resistance(ran.main(4.7), 'kohms')
            rb = c.resistance(ran.main(680), 'kohms')
            beta = ran.main(120)
            
            self.question = f"""Determine IC, VCE, VB, VC, VE and VBC from the network where VCC = {vcc.V} V, RC = {rc.kohms} kohms, RB = {rb.kohms} kohms, and beta = {beta}.
            https://lesliecaminadecom.files.wordpress.com/2019/07/84sgobka0ptm9b1aj9qb.png"""
            
            ib = c.current(
            (vcc.V - vbe.V) / (rb.ohms + beta * rc.ohms)
            )
            
            ic = c.current(
            beta * ib.A
            )
            
            vce = c.voltage(
            vcc.V - ic.A * rc.ohms
            )
            
            if vce.V > 0:
                regen = 0
        
        vb = c.voltage(
        vbe.V
        )
        
        vc = c.voltage(
        vce.V
        )
        
        ve = c.voltage(0)
        
        vbc = c.voltage(
        vb.V - vc.V
        )
        
        self.answer = f"""IC = {ic.mA} mA
VCE = {vce.V} V
VB = {vb.V} V
VC = {vc.V} V
VE = {ve.V} V
VBC = {vbc.V} V"""

class boylestad_4_19:
    def __init__(self,*args,**kwargs):
        print("4_19")
        regen = 1
        while regen:
            vee = c.voltage(ran.main(-9))
            rb = c.resistance(ran.main(100), 'kohms')
            rc = c.resistance(ran.main(1.2), 'kohms')
            beta = ran.main(45)
            
            self.question = f"""Determine VC and VB for the network where VEE = {vee.V} V, RB = {rb.kohms} kohms, RC = {rc.kohms} kohms, and beta = {beta} 
            https://lesliecaminadecom.files.wordpress.com/2019/07/415hm8o25ig5se9e8219.png"""
            
            vee = c.voltage( - vee.V)
            
            ib = c.current(
            (vee.V - vbe.V) / rb.ohms
            )
            
            ic = c.current(
            beta * ib.A
            )
            
            if ic.A < vee.V / rc.ohms:
                regen = 0
                
        vc = c.voltage(
        - ic.A * rc.ohms
        )
        
        vb = c.voltage(
        - ib.A * rb.ohms
        )
        
        self.answer = f"""VC = {vc.V} V
VB = {vb.V} V"""


class boylestad_4_20:
    def __init__(self,*args,**kwargs): 
        print("4_20")
        regen = 1
        while regen:
        
            vcc = c.voltage(ran.main(20))
            vee = c.voltage(vcc.V)
            rc = c.resistance(ran.main(2.7), 'kohms')
            re = c.resistance(ran.main(1.8), 'kohms')
            r1 = c.resistance(ran.main(8.2), 'kohms')
            r2 = c.resistance(ran.main(2.2), 'kohms')
            beta = ran.main(120)
            
            self.question = f"""Determine VC and VB for the network where VCC = - VEE = {vcc.V} V, R1(top) = {r1.kohms} kohms, R2(bottom) = {r2.kohms} kohms, RC = {rc.kohms} kohms, RE = {re.kohms} kohms, and beta = {beta}
            https://lesliecaminadecom.files.wordpress.com/2019/07/0o2i7c2ti2j3vsyovy9w.png"""
            
            rth = r1.parallel(r2)
            
            i_main = c.current(
            (vcc.V + vee.V) / (r1.ohms + r2.ohms)
            )
            
            eth = c.voltage(
            i_main.A * r2.ohms - vee.V
            )
            
            ib = c.current(
            (vee.V - eth.V - vbe.V) / (rth.ohms + (beta + 1) * re.ohms)
            )
            
            ic = c.current(
            beta * ib.A
            )
            
            if ic.A < ((vcc.V + vee.V) / (rc.ohms + re.ohms)):
                regen = 0
        
        vc = c.voltage(
        vcc.V - ic.A * rc.ohms
        )
        
        vb = c.voltage(
        - eth.V - ib.A * rth.ohms
        )
        
        self.answer = f"""VC = {vc.V} V
VB = {vb.V} V"""

class boylestad_4_27:
    def __init__(self,*args,**kwargs): 
        print("4_27")
        vcc = c.voltage(ran.main(12))
        r1 = c.resistance(ran.main(1.1), 'kohms')
        
        self.question = f"""Calculate the mirrored current I in the circuit if the resistor value is {r1.kohms} kohms and the supply voltage is {vcc.V} V
        https://lesliecaminadecom.files.wordpress.com/2019/07/u9q74dnf127mai659ec7.png"""
        
        icontrol = c.current(
        (vcc.V - vbe.V) / r1.ohms
        )
        
        self.answer = f"""Mirrored current = {icontrol.mA} mA"""
        
class boylestad_4_28:
    def __init__(self,*args,**kwargs): 
        print("4_28")
        vcc = c.voltage(ran.main(6))
        r1 = c.resistance(ran.main(1.3), 'kohms')
        
        self.question = f"""Calculate the current I through each of the transistors Q2 and Q3 in the circuit given that the resistor value is {r1.kohms} kohms and the supply voltage is {vcc.V} V.
        https://lesliecaminadecom.files.wordpress.com/2019/07/y5y4126r7lh1lf5ri0sg.png"""
        
        icontrol = c.current(
        (vcc.V - vbe.V) / r1.ohms
        )
        
        self.answer = f"""I = {icontrol.mA} mA"""
        
class boylestad_4_29:
    def __init__(self,*args,**kwargs): 
        print("4_29")
        r1 = c.resistance(ran.main(5.1), 'kohms')
        r2 = c.resistance(ran.main(5.1), 'kohms')
        r3 = c.resistance(ran.main(2), 'kohms')
        vee = c.voltage(ran.main(-20))
        
        self.question = f"""Calculate the constant current I in the circuit given that R1 = {r1.kohms} kohms, R2 = {r2.kohms} kohms, R3 = {r3.kohms} kohms and the supply voltage is {vee.V} V.
        https://lesliecaminadecom.files.wordpress.com/2019/07/9nq30cl87ky30ygt0dfn.png"""
        
        vb = c.voltage(
        (r1.ohms / (r1.ohms + r2.ohms)) * vee.V
        )
        
        ve = c.voltage(
        vb.V - vbe.V
        )
        
        ie = c.current(
        (ve.V - (vee.V))
        )
        
        self.answer = f"""I = {ie.mA} mA"""
        
class boylestad_4_30:
    def __init__(self,*args,**kwargs): 
        print("4_30")
        vee = c.voltage(ran.main(-18))
        r1 = c.resistance(ran.main(2.2), 'kohms')
        r2 = c.resistance(ran.main(1.8), 'kohms')
        vz = c.voltage(ran.main(6.2))
        
        self.question = f"""Calculate the constant current I in the circuit given that R1 = {r1.kohms} kohms, R2 = {r2.kohms} kohms, VZ = {vz.V} V, and the supply voltage is {vee.V} V.
        https://lesliecaminadecom.files.wordpress.com/2019/07/j1slfpbupu27nffjrlyv.png"""
        
        icontrol = c.current(
        (vz.V - vbe.V) / r2.ohms
        )
        
        self.answer =f"""I = {icontrol.mA} mA"""
        
class boylestad_4_31:
    def __init__(self,*args,**kwargs): 
        print("4_31")
        regen = 1
        while regen:
            vcc = c.voltage(ran.main(-18))
            r1 = c.resistance(ran.main(47), 'kohms')
            r2 = c.resistance(ran.main(10), 'kohms')
            rc = c.resistance(ran.main(2.4), 'kohms')
            re = c.resistance(ran.main(1.1), 'kohms')
            beta = ran.main(120)
            
            self.question = f"""Determine VCE for the voltage divider bias configuration when VCC = {vcc.V} V, R1(top) = {r1.kohms} kohms, R2(bottom) = {r2.kohms} kohms, RC = {rc.kohms} kohms, RE = {re.kohms} kohms, and beta = {beta}. Use approximate analysis.
            https://lesliecaminadecom.files.wordpress.com/2019/07/jcacmam8963k80575b1r.png"""
            
            vb = c.voltage(
            (r2.ohms * vcc.V ) / (r1.ohms + r2.ohms)
            )
            
            ve = c.voltage(
            vb.V - vbe.V
            )
            
            ie = c.current(
            ve.V / re.ohms
            )
            
            vce = c.voltage(
            vcc.V + ie.A * (rc.ohms + re.ohms)
            )
            
            if vce.V < 0:
                regen = 0
            
        self.answer = f"""VCE = {vce.V} V"""
        
class boylestad_4_32:
    def __init__(self,*args,**kwargs): 
        print("4_32")
        icsat = c.current(ran.main(10), 'mA')
        hfe = ran.main(250)
        vcc = c.voltage(10)
        vi = c.voltage(10)
        
        self.question = f"""Determine maximum RB, and RC for the transistor inverter in the figure if ICsat ={icsat.mA} mA and hfe = {hfe}.
        https://lesliecaminadecom.files.wordpress.com/2019/07/l3yu2b6k51ubj18av592.png"""
        
        rc = c.resistance(
        vcc.V / icsat.A
        )
        
        ib = c.current(
        icsat.A / hfe
        )
        
        rb = c.resistance(
        (vi.V - vbe.V) / ib.A
        )
        
        self.answer = f"""RB >= {rb.kohms} kohms
RC = {rc.kohms} kohms"""

class boylestad_4_35:
    def __init__(self,*args,**kwargs): 
        print("4_35")
        rbperre_list = [250, 10, 0.01]
        rbperre = ran.main(random.choice(rbperre_list)*100)/100
        beta = ran.main(50)
        deltaICO = c.current(ran.main(19.9), 'nA')
        
        self.question = f"""Calculate the stability factor (SICO) and the change in IC from 25 degC to 100 degC for the transistor with beta = {beta} and deltaICO = {deltaICO.nA} nA for an emitter-bias arrangement with RB/RE = {rbperre}"""
        
        sico = (
        (beta * ( 1 + rbperre )) / (beta + rbperre)
        )
        
        deltaic = c.current(
        sico * deltaICO.A
        )
        
        self.answer  = f"""SICO = {sico}
deltaIC = {deltaic.nA} nA"""

class boylestad_4_36:
    def __init__(self,*args,**kwargs): 
        print("4_36")
        regen = 1
        while regen:
        
            beta = ran.main(100)
            deltaVBE = c.voltage(0.65-0.48)
            
            rba = c.resistance(ran.main(240), 'kohms')
            rbb = c.resistance(ran.main(240), 'kohms')
            reb = c.resistance(ran.main(1000))
            rbc = c.resistance(ran.main(47), 'kohms')
            rec = c.resistance(ran.main(4.7), 'kohms')
            
            self.question = f"""Determine the stability factor (SVBE) and the change in IC from 25 degC to 100 degC for the transistor with beta = {beta} and deltaVBE = {deltaVBE.V} for the following bias arrangements:
    a) Fixed bias with RB = {rba.kohms} kohms.
    b) Emitter - bias with RB = {rbb.kohms} kohms, RE = {reb.kohms} kohms.
    c) Emitter - bias with RB = {rbc.kohms} kohms, RE = {rec.kohms} kohms.""" 
            
            #A
            svbea = (
            -beta * rba.ohms
            )
            
            deltaica = c.current(
            svbea * deltaVBE.V
            )
            
            #B
            svbeb = (
            ( -beta * reb.ohms) / (beta + rbb.ohms/reb.ohms)
            )
            
            deltaicb = c.current(
            svbeb * deltaVBE.V 
            )
            
            #C
            svbec = (
            -1 / rec.ohms
            )
            
            deltaicc = c.current(
            svbec * deltaVBE.V
            )
        
            if (rbb.ohms / reb.ohms) > beta and beta > (rbc.ohms/rec.ohms):
                regen = 0
            
        self.answer  = f"""Situtation A: SVBE = {svbea}, deltaIC = {deltaica.uA} uA
Situation B: SVBE = {svbeb}, deltaIC = {deltaicb.uA} uA
Situation C: SVBE = {svbec}, deltaIC = {deltaicc.uA} uA"""

class boylestad_4_37:
    def __init__(self,*args,**kwargs): 
        print("4_37")
        ic1 = c.current(ran.main(2), 'mA')
        beta1 = ran.main(50)
        beta2 = beta1 + ran.main(30)
        rbperre = ran.main(20)
        
        self.question = f"""Determine ICQ at a temperature of 100degC if ICQ = {ic1.mA} mA at 25degC for the emitter-bias configuration. The transistor used has beta1 = {beta1} and beta2 = {beta2}, and a resistance ratio RB/RE of {rbperre}."""
        
        sbeta = (
        (ic1.A * ( 1 + rbperre)) / 
        (beta1 * ( 1 + beta2 + rbperre))
        )
        
        deltaic = c.current(
        sbeta * (beta2 - beta1)
        )
        
        self.answer = f"""Sbeta = {sbeta}
deltaIC = {deltaic.mA} mA"""


#chapter 5 - BJT ac analysis
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        