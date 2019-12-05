import random_handler as ran
import math
import random
import constants_conversions as c
import interpolation
import sympy as sym
import frequency_and_phase_modulation as fm

x, y, z, t = sym.symbols('x y z t', real = True)

class tomasi_1_5:
    def __init__(self, *args, **kwargs):
        internal_resistance = c.resistance(ran.main(100))
        load_resistance = c.resistance(ran.main(100))
        temperature = c.temperature(ran.main(17), 'C')
        bandwidth = c.frequency(ran.main(10), 'kHz')
        
        
        self.question = f"""For a device operating at a temperature of {temperature.C} degC with a bandwidth of {bandwidth.kHz} kHz, determine: a) the noise power density No, b) the total noise power N, c) the rms noise voltage Vn for a {internal_resistance.ohms}-ohm internal resistance and a {load_resistance.ohms}-ohm load resistance."""
        
        noise_density = c.BOLTZMANNS_CONSTANT * temperature.K
        
        noise_power = c.power(c.BOLTZMANNS_CONSTANT * temperature.K * bandwidth.Hz )
        
        noise_voltage = c.voltage(
        math.sqrt(
        4 * load_resistance.ohms * c.BOLTZMANNS_CONSTANT * temperature.K * bandwidth.Hz
        )
        )
        
        self.answer = f"""Noise Density: {noise_density} W/Hz
Total noise power: {noise_power.W} W
RMS noise voltage: {noise_voltage.uV} uV"""

class tomasi_1_6:
    def __init__(self, *args, **kwargs):
        input_signal_voltage = c.voltage(ran.main(0.1e-3))
        input_noise_voltage = c.voltage(ran.main(0.01e-6))
        input_signal_power = c.power(ran.main(2e-10))
        
        input_noise_power = c.power(
        (math.sqrt(input_noise_voltage.W) * input_signal_power.W) / 
        (math.sqrt(input_signal_voltage.V))
        )
        
        voltage_gain = ran.main(1000)
        power_gain = voltage_gain**2
        
        amplifier_noise_voltage = c.voltage(ran.main(1e-6))
        amplifier_noise_power = c.power(ran.main(6e-12))
        
        
        self.question = f"""For the amplifier in the figure, with the following parameters, determine: a) Input signal to noise ratio, b) output signal to noise ratio, c) noise figure.

Input signal voltage (Si): {input_signal_voltage.V} V
Input signal power (Pi): {input_signal_power.W} W
Input noise voltage (Ni): {input_noise_voltage.V} V
Input noise power (Pn): {input_noise_power.W} W
Voltage gain (Av): {voltage_gain}
Power gain (Ap): {power_gain}
Amplifier Noise Voltage (Nd): {amplifier_noise_voltage.V} V
Amplifier Noise Power (Np): {amplifier_noise_power.W} W"""

        input_snr_voltage = c.dbvalue(
        input_signal_voltage.V / input_noise_voltage.V
        )
        
        input_snr_power = c.dbvalue(
        input_signal_power.W / input_noise_power.W
        )
        
        output_snr_voltage = c.dbvavlue(
        ( voltage_gain * input_signal_voltage.V ) / 
        ( voltage_gain * input_noise_voltage.V  + amplifier_noise_voltage.V)
        )
        
        output_snr_power = c.dbvalue(
        ( power_gain * input_signal_power.W ) / 
        ( power_gain * input_noise_power.W + amplifier_noise_power.W)
        )
        
        noise_figure_voltage = c.dbvalue(
        input_snr_voltage.unitless / output_snr_voltage.unitless
        )
        
        noise_figure_power = c.dbvalue(
        input_snr_power.unitless / output_snr_power.unitless
        )
        
        self.answer = f"""Input SNR: {input_snr_power.dB} dB, {input_snr_voltage.dB20} dB
Output SNR: {output_snr_power.dB} dB, {output_snr_voltage.dB20} dB
Voltage noise figure: {noise_figure_voltage.dB20} dB
Power noise figure: {noise_figure_power.dB} dB"""

class tomasi_1_7:
    def __init__(self, *args, **kwargs):
    
        noise_figures = c.dbvalue(ran.main(3), 'dB')
        gains = c.dbvalue(ran.main(10), 'dB')
        
        
        self.question = f"""For three cascaded amplifiers each with noise figures of {noise_figures.dB} dB, and gains of {gains.dB} dB, determine the total noise figure."""
        
        
        total_noise_figure = c.dbvalue(
        noise_figures.unitless + ((noise_figures.unitless - 1)/gains.unitless) + ((noise_figures.unitless - 1)/(gains.unitless**2))
        
        )
        
        self.answer = f"""Total noise figure: {total_noise_figure.dB} dB"""
        
class tomasi_2_1:
    def __init__(self, *args, **kwargs):
    
        frequency = c.frequency(ran.main(10), 'MHz')
        coefficient = ran.main(10)
        increase_temp = c.temperature(ran.main(10), 'C')
        decrease_temp = c.temperature(ran.main(5), 'C')
        
        self.question = f"""For a {frequency.MHz}-MHz crystal with a positive temperature coefficient of {coefficient} Hz/MHz/degC, determine the frequency of operation of the temperature: a) increases by {increase_temp.C} degC and b) decreases by {decrease_temp.C} degC"""
        
        delta_freq1 = c.frequency(
        coefficient * frequency.MHz * increase_temp.C
        )
        
        operating_frequency_1 = c.frequency(
        frequency.Hz + delta_freq1.Hz
        )
        
        delta_freq2 = c.frequency(
        coefficient * frequency.MHz * decrease_temp.C
        )
        
        operating_frequency_2 = c.frequency(
        frequency.Hz + delta_freq2.Hz
        )
        
        self.answer = f"""Operating frequency at +{increase_temp.C}degC: {operating_frequency_1.MHz} MHz
Operating frequency at -{decrease_temp.C} degC: {operating_frequency_2.MHz} MHz"""

class tomasi_2_2:
    def __init__(self, *args, **kwargs):
        regen = 1
        while regen:
            frequency_1 = c.frequency(ran.main(5), 'kHz')
            frequency_2 = c.frequency(ran.main(7), 'kHz')
            if frequency_1.Hz < frequency_2.Hz:
                regen = 0
                
        
        self.question = f"""For a nonlinear amplifier with two input frequencies {frequency_1.kHz} kHz and {frequency_2.kHz} kHz: a) determine the first three harmonics present in the output for each input frequency. b) determine the cross products produced in the output for values of m and n of 1 and 2."""
        
        second_harmonic_1 = c.frequency( frequency_1.Hz * 2)
        third_harmonic_1 = c.frequency( frequency_1.Hz * 3)
        
        second_harmonic_2 = c.frequency( frequency_2.Hz * 2 )
        third_harmonic_2 = c.frequency( frequency_2.Hz * 3)

        cross_product_low = c.frequency( frequency_2.Hz - frequency_1.Hz )
        
        cross_product_high = c.frequency( frequency_1.Hz + frequency_2.Hz )
        
        self.answer = f"""First harmonics: {frequency_1.kHz} kHz, {frequency_2.kHz} kHz
Second harmonics: {second_harmonic_1.kHz} kHz, {second_harmonic_2.kHz} kHz
Third harmonics: {third_harmonic_1.kHz} kHz, {second_harmonic_2.kHz} kHz
Cross products: {cross_product_low.kHz} kHz and {cross_product_high.kHz} kHz"""

class tomasi_3_1:
    def __init__(self, *args, **kwargs):
        
        carrier_frequency = c.frequency(ran.main(100), 'kHz')
        modulating_frequency = c.frequency(ran.main(5), 'kHz')
        modulating_frequency_2 = c.frequency(ran.main(3), 'kHz')
        
        self.question = f"""For an AM modulator with a carrier frequency of {carrier_frequency.kHz} kHz and a maximum modulating signal frequency of {modulating_frequency.kHz} kHz: a) Determine the frequency limits for the upper and lower sidebands, b) Determine the upper and the lower side frequencies produced when the modulating signal is a single-frequency {modulating_frequency_2.kHz} kHz tone, c) determine the bandwidth."""
        
        upper_sideband = c.frequency( 
        carrier_frequency.Hz + modulating_frequency.Hz
        )
        
        lower_sideband = c.frequency(
        carrier_frequency.Hz - modulating_frequency.Hz
        )
        
        upper_sidefrequency = c.frequency(
        carrier_frequency.Hz + modulating_frequency_2.Hz
        )
        
        lower_sidefrequency = c.frequency(
        carrier_frequency.Hz - modulating_frequency_2.Hz
        )
        
        bandwidth = c.frequency( 2 * modulating_frequency.Hz )
        
        self.answer = f"""Lower and upper sidebands: {lower_sideband.kHz} kHz to {upper_sideband.kHz} kHz
Lower and upper side frequencies: {lower_sidefrequency.kHz} kHz and {upper_sidefrequency.kHz} kHz
Bandwidth: {bandwidth.kHz} kHz"""

class tomasi_3_2:
    def __init__(self, *args, **kwargs):
    
        vmax = c.voltage(ran.main(18))
        vmin = c.voltage(ran.main(2))
        
        
        self.question = f"""For the AM envelope in the figure with Vmax = {vmax.V} V and Vmin = {vmin.V} V, determine: a) the peak amplitude of the upper and lower side frequencies, b) the peak amplitude of the unmodulated carrier, c) the peak change in the amplitude of the envelope, d) the modulation coefficient, e) the percent modulation.
        https://lesliecaminadecom.files.wordpress.com/2019/09/djg5rjdpvvo7h58aqyft.png"""

        E_upper = c.voltage( 0.25 * (vmax.V - vmin.V) )
        E_lower = c.voltage( E_upper.V )
        E_carrier = c.voltage( 0.5 * (vmax.V + vmin.V))
        E_modulating = c.voltage( 0.5 * (vmax.V - vmin.V))
        modulation_index = c.percentage( E_modulating.V / E_carrier.V )
        
        self.answer = f"""Peak amplitude of upper and lower sidebands: {E_upper.V} V and {E_lower.V} V
Peak amplitude of the unmodulated carrier: {E_carrier.V} V
Peak change in the amplitude of the envelope: {E_modulating.V} V
Modulation coefficient: {modulation_index.decimal} 
Percent modulation: {modulation_index.percent} %"""

class tomasi_3_3:
    def __init__(self, *args, **kwargs):
        
        carrier_frequency = c.frequency(ran.main(500), 'kHz')
        carrier_voltage = c.voltage(ran.main(20))
        modulating_frequency = c.frequency(ran.main(10), 'kHz')
        peak_change = c.voltage(ran.main(7.5))
        
        
        self.question = f"""One input to an AM modulator is a {carrier_frequency.kHz}-kHz carrier with a peak amplitude of {carrier_voltage.V} V. The second input is a {modulating_frequency.kHz}-kHz modulating signal that is of sufficient amplitude to cause a peak change in the output wave of +/- {peak_change.V} V. a) determine the USF and LSF, b) determine the modulation coefficient and the percent modulation. c) determine the peak amplitude of the modulated carrier, the USF and the LSF. d) determine the maximumm and minimum amplitudes of the AM envelope. e) determine the expression for the modulated AM wave."""
        
        upper_sidefrequency = c.frequency(
        carrier_frequency.Hz + modulating_frequency.Hz
        )
        
        lower_sidefrequency = c.frequency(
        carrier_frequency.Hz - modulating_frequency
        )
        
        modulating_voltage = c.voltage(
        peak_change.V
        )
        
        modulation_index = c.percentage(
        modulating_voltage.V / carrier_voltage.V, 'decimal'
        )
        
        peak_usf_voltage = c.voltage(
        modulation_index.decimal * carrier_voltage.V / 2
        )
        
        peak_lsf_voltage = c.voltage( 
        peak_usf_voltage.V
        )
        
        vmax = c.voltage(
        carrier_voltage.V + modulating_voltage.V
        )
        
        vmin = c.voltage(
        carrier_voltage.V - modulating_voltage.V
        )
        
        self.answer = f"""LSF and USF: {lower_sidefrequency.kHz} kHz and {upper_sidefrequency.kHz} kHz
Modulation index and percent modulation: {modulation_index.decimal}, {modulation_index.percent} %
Carrier peak amplitude: {carrier_voltage.V} V
LSF and USF peak amplitude: {peak_usf_voltage.V} V
Vmax and Vmin: {vmax.V} V and {vmin.V} V
Expression:
{carrier_voltage.V} sin (2 pi {round(carrier_frequency.kHz,2)}k t) - {peak_usf_voltage.V} cos (2 pi {round(upper_sidefrequency.KHz,2)}k t) - {peak_lsf_voltage.V} cos (2 pi {round(lower_sidefrequency.kHz,2)}k t)"""

class tomasi_3_4:
    def __init__(self, *args, **kwargs):
        regen = 1
        while regen:
            carrier_voltage = c.voltage(ran.main(10))
            load_resistance = c.resistance(ran.main(10))
            modulation_index = c.percentage(ran.main(0.5), 'decimal')
            if modulation_index.decimal > 0 and modulation_index.decimal < 1:
                regen = 0
        
        self.question = f"""For an AM DSBFC wave with a peak unmodulated carrier voltage of {carrier_voltage.V} V and a load resistance of {load_resistance.ohms} ohms: a) determine the peak and rms powers of the carrier, the USF, and the LSF. b) determine the total power of the modulated wave for a modulation coefficient of {modulation_index.decimal}."""
        
        peak_carrier_power = c.power(
        carrier_voltage.V**2 /  load_resistance.ohms
        )
        
        rms_carrier_power = c.power(
        carrier_voltage.V**2 / ( 2 * load_resistance.ohms )
        )
        
        peak_usf_power = c.power(
        modulation_index.decimal**2 * peak_carrier_power.W / 4
        )
        
        rms_usf_power = c.power(
        modulation_index.decimal**2  * rms_carrier_power.W / 4
        )
        
        peak_total_sideband_power = c.power(
        2 * peak_usf_power.W
        )
        
        rms_total_sideband_power = c.power(
        2 * rms_usf_power.W
        )
        
        peak_total_power = c.power(
        peak_carrier_power.W + peak_total_sideband_power.W
        )
        
        rms_total_power = c.power(
        rms_carrier_power.W + rms_total_sideband_power.W
        )
        
        self.answer = f"""Peak and RMS carrier power: {peak_carrier_power.W} W, {rms_carrier_power.W} W
LSF and USF peak and RMS powers: {peak_usf_power.W} W, {rms_usf_power.W} W
Total peak and RMS powers: {peak_total_power.W} W, {rms_total_power.W} W"""


class tomasi_3_6:
    def __init__(self, *args, **kwargs):
        
        regen = 1
        while regen:
            modulation_index = c.percentage(
            ran.main(0.8)
            )
            
            gain = ran.main(100)
            carrier_input_voltage = c.votlage(ran.main(5), 'mV')
            
            if modulation_index.decimal < 1 and modulation_index.decimal > 0:
                regen = 0
        
        self.question = f"""For a low-power transistor AM modulator with a modulation coefficient of {modulation_index.decimal}, a quiescent gain of {gain}, and an input carrier amplitude of {carrier_input_voltage.V} V: a) determine the maximum and minimum gains for the transistor, b) determine the maximum and minimum amplitude of Vout"""

        gain_max = gain * ( 1 + modulation_index.decimal )
        gain_min = gain * ( 1 - modulation_index.decimal )
        
        output_voltage_max = gain_max * carrier_input_voltage.V
        output_voltage_min = gain_min * carrier_input_voltage.V
        
        self.answer = f"""Maximum and minimum gains: {gain_max} , {gain_min}
Maximum and minimum output voltages: {output_voltage_max.V} V, {output_voltage_min.V} V"""

class tomasi_4_1:
    def __init__(self, *args, **kwargs):
        
        negative_three_bandwidth = c.frequency(ran.main(10), 'kHz')
        negative_sixty_bandwidth = c.frequency(ran.main(100), 'kHz')
        
        self.question = f"""Determine the shape factor and the percent selectivity for the gain versus frequency characteristics of:
-3 dB bandwidth of {negative_three_bandwidth.kHz} kHz
-60 dB bandwidth of {negative_sixty_bandwidth.kHz} kHz"""

        shape_factor = c.percentage(
        negative_sixty_bandwidth.Hz / negative_three_bandwidth.Hz
        , 'decimal')
        
        self.answer = f"""Shape factor: {shape_factor.decimal} 
Percent selectivity: {shape_factor.percentage} %"""

class tomasi_4_2:
    def __init__(self, *args, **kwargs):
    
        rf_bandwidth = c.frequency(ran.main(200), 'kHz')
        if_bandwidth = c.frequency(ran.main(10), 'kHz')
        
        self.question = f"""Determine the improvement in the noise figure for a receiver with an RF bandwidth equal to {rf_bandwdth.kHz} kHz and an IF bandwidth equal to {if_bandwidth.kHz} kHz."""
        
        bandwidth_improvement = c.dbvalue(
        rf_bandwidth.Hz / if_bandwidth.Hz
        )
        
        self.answer = f"""Noise figure improvement: {bandwidth_improvement.dB} dB"""
        
class tomasi_4_3:
    def __init__(self, *args, **kwargs):
        Q_factor = ran.main(54)
        self.question = f"""For an AM commercial broadcast-band receiver ( 535 to 1605 kHz ) with an input filter Q-factor of {Q_factor}, determine the bandwidth at the low and high ends of the RF spectrum."""
        
        bandwidth_low_end = c.frequency(
        540e3 / Q_factor
        )
        
        bandwidth_high_end = c.frequency(
        1600e3 / Q_factor
        )
        
        self.answer = f"""Bandwidth at low end: {bandwidth_low_end.kHz} kHz
Bandwidth at high end: {bandwidth_high_end.kHz} kHz"""

class tomasi_4_4:
    def __init__(self, *args, **kwargs):
        
        if_frequency  = c.frequency(455, 'kHz')
        rf_modulating_frequency = c.frequency(ran.main(5), 'kHz')
        rf_carrier_frequency = c.frequency(ran.main(900), 'kHz')
        
        rf_upper_side_frequency = c.frequency(
        rf_carrier_frequency.Hz + rf_modulating_frequency.Hz
        )
        
        rf_lower_side_frequency = c.frequency(
        rf_carrier_frequency.Hz - rf_modulating_frequency.Hz
        )
        
        local_oscillator_frequency = c.frequency(
        if_frequency.Hz + rf_carrier_frequency.Hz
        )
        
        self.question = f"""For an AM superheterodyne receiver that uses high-side injection and has a local oscillator frequency of {local_oscillator_frequency.kHz} kHz, determine the IF carrier, upper side frequency, and lower side frequency for an RF envelope which is made up of a carrier and upper and lower side frequencies of {rf_carrier_frequency.kHz} , {rf_upper_side_frequency.kHz} and {rf_lower_side_frequency.kHz} kHz respectively."""
        
        if_upper_side_frequency = c.frequency(
        local_oscillator_frequency.Hz - rf_lower_side_frequency.Hz
        )
        
        if_lower_side_frequency = c.frequency(
        local_oscillator_frequency.Hz - rf_upper_side_frequency.Hz
        )
        
        self.answer = f"""IF upper side frequency: {if_upper_side_frequency.kHz} kHz
IF lower side frequency: {if_lower_side_frequency.kHz} kHz"""

class tomasi_4_6:
    def __init__(self, *args, **kwargs):
        
        if_frequency = c.frequency(455, 'kHz')
        rf_frequency = c.frequency(ran.main(600), 'kHz')
        local_oscillator_frequency = c.frequency(
        if_frequency.Hz + rf_frequency.Hz
        )
        
        Q_factor = ran.main(200)
        
        self.question = f"""For an AM broadcast-band superheterodyne receiver with an IF, RF, and local oscillator frequency of {if_frequency.kHz} kHz, {rf_frequency.kHz} kHz, and {local_oscillator_frequency.kHz} kHz respectively: a) determine the image frequency and b) calculate the IFRR for a preselector Q of {Q_factor}."""
        
        image_frequency = c.frequency(
        local_oscillator_frequency.Hz + if_frequency.Hz
        )
        
        rho =  (image_frequency.Hz / rf_frequency.Hz ) - (rf_frequency.Hz/ image_frequency.Hz)
        
        ifrr = c.dbvalue(
        math.sqrt(
        1 + rho**2 * Q_factor**2
        )
        )
        
        self.answer = f"""Image frequency: {image_frequency.kHz} kHz
IFRR: {ifrr.unitless} or {ifrr.dB20} dB"""
        
class tomasi_4_7:
    def __init__(self, *args, **kwargs):
        rf_frequency = c.frequency(ran.main(27), 'MHz')
        if_frequency = c.frequency(455, 'kHz')
        Q_factor = ran.main(100)
        rf_frequency_2 = c.frequency(ran.main(600), 'kHz')
        
        self.question = f"""For a citizen's band receiver using high-side injection with an RF of {rf_frequency.MHz} MHz and an IF of {if_frequency.kHz} kHz determine: a) the local oscillator frequency. b) the image frequency. c) the IFRR for a preselector Q of {Q_factor}. d) the preselector Q required to achieve the same IFRR as that achieved for an RF of {rf_frequency_2.kHz} kHz"""
        
        local_oscillator_frequency = c.frequency(
        rf_frequency.Hz + if_frequency.Hz
        )
        
        image_frequency = c.frequency(
        local_oscillator_frequency.Hz + if_frequency.Hz
        )
        
        rho =  (image_frequency.Hz / rf_frequency.Hz ) - (rf_frequency.Hz/ image_frequency.Hz) 
        
        ifrr = c.dbvalue(
        math.sqrt(
        1 + rho**2 * Q_factor**2
        )
        )
        
        rho_2 =  (image_frequency.Hz / rf_frequency_2.Hz ) - (rf_frequency_2.Hz/ image_frequency.Hz) 
        
        ifrr_2 = c.dbvalue(
        math.sqrt(
        1 + rho_2**2 * Q_factor**2
        )
        )
        
        Q_factor_2 = math.sqrt(
        (ifrr_2.unitless**2 - 1) / (rho_2**2)
        )
        
        self.answer = f"""Local oscillator: {local_oscillator_frequency.MHz} MHz
Image frequency: {image_frequency.MHz} MHz
IFRR: {ifrr.dB20} dB
Q factor for {rf_frequency_2.kHz} kHz: {Q_factor_2}"""

class tomasi_4_8:
    def __init__(self, *args, **kwargs):
        
        bandwidth_one_single_tuned = c.frequency(
        ran.main(10) , 'kHz'
        )
        
        critical_coupling_coefficient = ran.main(0.02)
        resonant_frequency = c.frequency(ran.main(1), 'MHz')
        
        self.question = f"""Determine the overall bandwidth for a) two single-tuned amplifiers each with a bandwidth of {bandwidth_one_single_tuned.kHz} kHz. b) three single-tuned amplifiers each with a bandwidth of {bandwidth_one_single_tuned.kHz} kHz and c) four single-tuned amplifiers each with a bandwidth of {bandwidth_one_single_tuned.kHz} kHz. d) Determine the bandwidth for a double-tuned amplifier with optimum coupling, a kc of {critical_coupling_coefficient}, and a resonant frequency of {resonant_frequency.MHz} MHz. e) Repeat parts (a) (b) and (c) for the double-tuned amplifier of part (d)."""
        
        single_tuned_2 = c.frequency(
        bandwidth_one_single_tuned.Hz * math.sqrt(
        2**(1/2) - 1
        )
        )
        
        single_tuned_3 = c.frequency(
        bandwidth_one_single_tuned.Hz * math.sqrt(
        2**(1/3) - 1
        )
        )
        
        single_tuned_4 = c.frequency(
        bandwidth_one_single_tuned.Hz * math.sqrt(
        2**(1/4) - 1
        )
        )
        
        optimum_coupling_coefficient = 1.5 * critical_coupling_coefficient
        
        bandwidth_one_double_tuned = c.frequency(
        optimum_coupling_coefficient * resonant_frequency.Hz
        )
        
        double_tuned_2 = c.frequency(
        bandwidth_one_single_tuned.Hz * (2**(1/2) - 1)**(1/4)
        )
        
        double_tuned_3 = c.frequency(
        bandwidth_one_single_tuned.Hz * (2**(1/3) - 1)**(1/4)
        )
        
        double_tuned_4 = c.frequency(
        bandwidth_one_single_tuned.Hz * (2**(1/4) - 1)**(1/4)
        )
        
        self.answer = f"""Bandwidth of single tuned for 2, 3 and 4 stages: {single_tuned_2.Hz} Hz, {single_tuned_3.Hz} Hz, and {single_tuned_4.Hz} Hz
Bandwidth of a single double-tuned stage: {bandwidth_one_double_tuned.kHz} kHz
Bandwidth of double tuned for 2, 3, and 4 stages: {double_tuned_2.Hz} Hz, {double_tuned_3.Hz} Hz, and {double_tuned_4.Hz} Hz"""

class tomasi_5_1:
    def __init__(self, *args, **kwargs):
        regen = 1
        while regen:
            natural_frequency = c.frequency(
            ran.main(200), 'kHz'
            )
            
            input_frequency = c.frequency(
            ran.main(210), 'kHz'
            )
        
            if natural_frequency.Hz < input_frequency.Hz:
                regen = 0
                
        phase_comparator_gain = ran.main(0.2)
        filter_gain = ran.main(1)
        opamp_gain = ran.main(5)
        vco_gain = ran.main(20) #khz / V
        
        self.question = f"""For the PLL shown, a VCO natural frequency Fn = {natural_frequency.kHz} kHz, an input frequency Fi = {input_frequency.kHz} kHz and the following circuit gains: Kd = {phase_comparator_gain} V/rad, Kf = {filter_gain}, Ka = {opamp_gain}, and Ko = {vco_gain} kHz/V, determine:
a) the open loop gain Kv
b) the change in frequency required to achieve lock, deltaF
c) Vout
d) Vd
e) the static phase error, theta_e
f) The hold-in range, delta_fmax

https://lesliecaminadecom.files.wordpress.com/2019/09/er6zsjkbx01g6qm91uvq.png"""

        open_loop_gain_pers = c.dbvalue(phase_comparator_gain * filter_gain * opamp_gain * vco_gain * 1000 * 2 * math.pi ) # per second
       
        open_loop_gain_freqperrad = c.frequency(
       phase_comparator_gain * filter_gain * opamp_gain * vco_gain 
       )
       
        delta_f = c.frequency(
       input_frequency.Hz - natural_frequency.Hz
       )
       
        vout = c.voltage(
       delta_f.kHz / ( vco_gain )
       )
       
        vd = c.voltage(
       vout.V / ( filter_gain * opamp_gain )
       )
       
        phase_error = c.angle(
       vd.V / phase_comparator_gain, 'radians'
       )
       
        delta_fmax = c.frequency(
       (math.pi/2) * open_loop_gain_freqperrad.Hz
       )
       
        self.answer = f"""Open loop gain: {open_loop_gain_pers} s^(-1) or {open_loop_gain_kHzperrad} kHz/rad
Capture range: {delta_f.kHz} kHz
Vout: {vout.V} V
Vd: {vd.V} V
Phase Error: {phase_error.degrees} degrees or {phase_error.radians} radians
Lock range: {delta_fmax.kHz} kHz"""

class tomasi_6_1:
    def __init__(self, *args, **kwargs):
        regen = 1
        while regen:
            bandwidth = c.frequency(
            ran.main(5), 'kHz'
            )
            
            rf_received_low = c.frequency(ran.main(30), 'MHz')
            fr_received_high = c.frequency(rf_received_low.Hz + bandwidth.Hz)
            
            local_oscillator_frequency = c.frequency(ran.main(20), 'MHz')
            
            if_received_low = c.frequency( rf_received_low.Hz - local_oscillator_frequency.Hz )
            
            if_received_high = c.frequency( if_received_low.Hz + bandwidth.Hz )
            
            bfo_frequency = c.frequency(
            ran.main(10), 'MHz'
            )
            
            drift = c.percentage( ran.main(0.001), 'percent')
            
            demodulated_output_low = c.frequency(
            if_received_low.Hz - bfo_frequency.Hz
            )
            
            demodulated_output_high = c.frequency(
            if_received_high.Hz - bfo_frequency.Hz
            )
            
            local_oscillator_frequency_drifted = c.frequency(
            local_oscillator_frequency.Hz * (1 - drift.decimal)
            )
            
            if_received_high_drifted = c.frequency(
            rf_received_high.Hz - local_oscillator_frequency_drifted.Hz
            )
            
            if_received_low_drifted = c.frequency(
            rf_received_low.Hz - local_oscillator_frequency_drifted.Hz
            )
            
            demodulated_output_high_drifted = c.frequency(
            if_received_high_drifted.Hz - bfo_frequency.Hz
            )
            
            demodulated_output_low_drifted = c.frequency(
            if_received_low_drifted.Hz - bfo_frequency.Hz
            )
            
            if demodulated_output_low_drifted.Hz > 0:
                regen = 0
        
        self.question = f"""For the BFO receiver (https://lesliecaminadecom.files.wordpress.com/2019/09/k229zn222n37bcw4ebxe.png) an RF received signal of {rf_received_low.MHz} to {rf_received_high.MHz} MHz, an RF local oscillator frequency of {local_oscillator_frequency.MHz}, an IF frequency band of {if_frequency_low.MHz} to {if_frequency_high.MHz} MHz, and a BFO frequency of {bfo_frequency.MHz} MHz, determine:
a) the demodulated first IF frequency band and demodulated information spectrum
b) the demodulated information spectrum when the RF local oscillator drifts down {drift.percent} %"""

        self.answer = f"""Mixer output: {if_received_low.MHz} MHz to {if_received_high.MHz} MHz
Demodulated output: {demodulated_output_low.kHz} kHz to {demodulated_output_high.kHz} kHz
Mixer output after drift: {if_received_low_drifted.MHz} MHz to {if_received_high_drifted.MHz} MHz
Demodulated output after drift: {demodulated_output_low_drift.kHz} kHz to {demodulated_output_high_drift.kHz} kHz"""

class tomasi_6_2:
    def __init__(self, *args, **kwargs):
        
        frequency_1 = c.frequency(
        ran.main(1.5) , 'kHz'
        )
        
        frequency_2 = c.frequency(
        ran.main(3), 'kHz'
        )
        
        carrier_frequency = c.frequency(
        ran.main(100), 'kHz'
        )
        
        voltage = c.voltage(ran.main(10))
        
        load_resistance = c.resistance(ran.main(50))
        
        self.question = f"""For a two-tone test signal of {frequeuncy_1.kHz} kHz and {frequency_2.kHz} kHz and a carrier frequency of {carrier_frequency.kHz} kHz: 
a) Determine the output frequency spectrum
b) For e1 = e2 = {voltage.V} Vp and a load resistance of {load_resistance.ohms} ohms, determine the PEP and average output power."""
        
        upper_side_frequency_1 = c.frequency(
        carrier_frequency.Hz + frequency_1.Hz
        )
        
        upper_side_frequency_2 = c.frequency(
        carrier_frequency.Hz + frequency_2.Hz
        )
        
        rms_voltage = c.voltage(
        (voltage.V / 2) * (math.sqrt(2) / 2)
        )
        
        peak_envelope_power = c.power(
        (4 * rms_voltage.V**2) / (load_resistance.ohms)
        )
        
        ave_power = c.power(
        (2 * rms_voltage.V**2)/(load_resistance.ohms)
        )
        
        self.answer = f"""Upper side frequency 1 : {upper_side_frequency_1.kHz} kHz
Upper side frequency 2: {upper_side_frequency_2.kHz} kHz
Peak envelope power: {peak_envelope_power.W} W
Average Power: {average_power.W} W"""

class tomasi_7_1:
    def __init__(self, *args, **kwargs):
        
        frequency_deviation_sensitivity = c.frequency(
        ran.main(5), 'kHz'
        )
        
        peak_modulating_voltage = c.voltage(ran.main(2))
        
        modulating_frequency = c.frequency(ran.main(2000))
        
        phase_deviation_sensitivity = c.angle(
        ran.main(2.5) , 'radians'
        )
        
        self.question = f"""Determine the peak frequency deviation (delta F) and modulation index (m) for an FM modulator wuth a deviation sensitivity K1 = {frequency_deviation_sensitivity.kHz} kHz/V and a modulating signal v(t) = {peak_modulating_voltage.V} cos (2 pi {modulating_frequency.Hz} t). Determine the peak phase deviation (m) for a PM modulator with a deviation sensitivity K = {phase_deviation_sensitivity.rad} rad/V and a modulating signal v(t) = {peak_modulating_voltage.V} cos (2  pi {modulating_frequency.Hz} t)"""

        delta_f = c.frequency(
        frequency_deviation_sensitivity.Hz * peak_modulating_voltage.V
        )
        
        modulation_index_fm = delta_f.Hz / modulating_frequency.Hz
        
        modulation_index_pm = phase_deviation_sensitivity.radians * peak_modulating_voltage.V
        
        self.answer = f"""Peak frequency deviation: {delta_f.kHz} kHz
FM modulation index: {modulation_index_fm}
PM modulation index: {modulation_index_pm}"""

class tomasi_7_2:
    def __init__(self, *args, **kwargs):
    
        modulation_index = ran.main(1)
        
        modulating_frequency = c.frequency(ran.main(1000))
        
        peak_unmodulated_carrier_voltage = c.voltage(ran.main(10))
        
        carrier_frequency = c.frequency(ran.main(500), 'kHz')
    
        self.question = f"""For an FM modulator with a modulation index m = {modulation_index}, a modulating signal v(t) = Vm sin (2pi {modulating_frequency.Hz} t) and an unmodulated carrier vc = {peak_unmodulated_carrier_voltage.V} sin (2pi {carrier_frequency.kHz} k t )
a) determine the number of sets of significant side frequencies
b) determine their amplitudes"""
        
        number_of_significant_sidebands = fm.significant_sidebands(modulation_index)
        
        bessel_list = []
        
        for i in range(number_of_significant_sidebands + 1):
            bessel_list.append(
            mpmath.besselj(i, modulation_index)
            )
        
        
        


        
       
       
       
       
       
       
        
        

class tomasi_14_1:
    def __init__(self, *args, **kwargs):
        power = c.power(ran.main(100), 'W')
        distance = c.length(ran.main(1500), 'm')
        
        self.question = f"""For an isotropic antenna radiating {power.W} W of power, determine the power density {distance.m} m from the source."""
        
        power_density = c.powerDensity( power.W / ( 4 * math.pi * distance.m**2))
        
        self.answer = f"""Power density: {power_density.uWperm2} uW/m2"""
        

class tomasi_14_2:
    def __init__(self, *args, **kwargs):
        frequency = c.frequency(ran.main(6), 'GHz')
        distance = c.length(ran.main(50), 'km')
        
        self.question = f"""For a carrier frequency of {frequency.GHz} GHz and a distance of {distance.km} km, determine the free-space path loss."""
        
        path_loss = c.dbvalue(
        ((4 * math.pi * distance.m) / 
        (3e8 / frequency.Hz))**2
        )
        
        self.answer = f"""Free-space path loss: {path_loss.dB} dB"""
        


class tomasi_14_3:
    def __init__(self, *args, **kwargs):
        
        distance = c.length(ran.main(40), 'km')
        frequency = c.frequency(ran.main(1.8), 'GHz')
        i = random.randint(0,3)
        j = random.randint(0,2)
        roughness_text = ['water', 'very smooth terrain', 'average terrain', 'very rough mountainous terrain']
        roughness_value = [4,4,1,0.25]
        climate_text = ['hot humid area', 'average inland area', 'very dry']
        climate_value = [0.5, 0.25, 0.125]
        reliability = c.percentage(random.sample([99.9, 99.99, 99.999], 1)[0], 'percent')
        
        self.question = f"""Determine the fade margin for the following conditions: distance between sites = {distance.km} km, frequency = {frequency.GHz} GHz, {roughness_text[i]}, {climate_text[j]}, and a reliability objective of {reliability.percent}%."""

        fade_margin = c.dbvalue(
        30 * math.log(distance.km, 10) + 10 * math.log( 6 * roughness_value[i] * climate_value[j] * frequency.GHz, 10) - 10 * math.log(1 - reliability.decimal, 10) - 70, 'dB'
        )
        
        self.answer = f"""Fade margin: {fade_margin.dB} dB"""
        
class tomasi_14_3_b:
    def __init__(self, *args, **kwargs):
        
        distance = c.length(ran.main(40), 'km')
        frequency = c.frequency(ran.main(1.8), 'GHz')
        i = random.randint(0,3)
        j = random.randint(0,2)
        roughness_text = ['water', 'very smooth terrain', 'average terrain', 'very rough mountainous terrain']
        roughness_value = [4,4,1,0.25]
        climate_text = ['hot humid area', 'average inland area', 'very dry']
        climate_value = [0.5, 0.25, 0.125]
        reliability = c.percentage(random.sample([99.9, 99.99, 99.999], 1)[0], 'percent')
        
        self.question = f"""Determine the multipath effect for the following conditions: distance between sites = {distance.km} km, frequency = {frequency.GHz} GHz, {roughness_text[i]}, {climate_text[j]}, and a reliability objective of {reliability.percent}%."""

        multipath_effect = c.dbvalue(
        30 * math.log(distance.km, 10), 'dB'
        )
        
        self.answer = f"""Multipath effect: {multipath_effect.dB} dB"""
        
class tomasi_14_3_c:
    def __init__(self, *args, **kwargs):
        
        distance = c.length(ran.main(40), 'km')
        frequency = c.frequency(ran.main(1.8), 'GHz')
        i = random.randint(0,3)
        j = random.randint(0,2)
        roughness_text = ['water', 'very smooth terrain', 'average terrain', 'very rough mountainous terrain']
        roughness_value = [4,4,1,0.25]
        climate_text = ['hot humid area', 'average inland area', 'very dry']
        climate_value = [0.5, 0.25, 0.125]
        reliability = c.percentage(random.sample([99.9, 99.99, 99.999], 1)[0], 'percent')
        
        self.question = f"""Determine the terrain sensitivity for the following conditions: distance between sites = {distance.km} km, frequency = {frequency.GHz} GHz, {roughness_text[i]}, {climate_text[j]}, and a reliability objective of {reliability.percent}%."""

        terrain_sensitivity = c.dbvalue(
        10 * math.log( 6 * roughness_value[i] * climate_value[j] * frequency.GHz, 10), 'dB'
        )
        
        self.answer = f"""Multipath effect: {terrain_sensitivity.dB} dB"""

class tomasi_14_3_d:
    def __init__(self, *args, **kwargs):
        
        distance = c.length(ran.main(40), 'km')
        frequency = c.frequency(ran.main(1.8), 'GHz')
        i = random.randint(0,3)
        j = random.randint(0,2)
        roughness_text = ['water', 'very smooth terrain', 'average terrain', 'very rough mountainous terrain']
        roughness_value = [4,4,1,0.25]
        climate_text = ['hot humid area', 'average inland area', 'very dry']
        climate_value = [0.5, 0.25, 0.125]
        reliability = c.percentage(random.sample([99.9, 99.99, 99.999], 1)[0], 'percent')
        
        self.question = f"""Determine the reliability objectives for the following conditions: distance between sites = {distance.km} km, frequency = {frequency.GHz} GHz, {roughness_text[i]}, {climate_text[j]}, and a reliability objective of {reliability.percent}%."""

        reliability_objectives = c.dbvalue(
        - 10 * math.log(1 - reliability.decimal, 10), 'dB'
        )
        
        self.answer = f"""Reliability objectives: {reliability_objectives.dB} dB"""
        
class tomasi_15_1:
    def __init__(self, *args, **kwargs):
        gain = c.dbvalue(ran.main(10), 'unitless')
        power = c.power(ran.main(100), 'W')
        distance = c.length(ran.main(10), 'km')
        
        self.question = f"""For a transmit antenna with a power gain A = {gain.unitless} and input power Pin = {power.W} W, determine EIRP, power density {distance.km} km from the antenna and the power density had an isotropic antenna been used with the same input power and efficiency."""
        
        eirp = c.power(power.W * gain.unitless)
        power_density = c.powerDensity((power.W * gain.unitless) / (4 * math.pi * distance.m**2))
        
        power_density_iso = c.powerDensity(power.W / (4 * math.pi * distance.m**2))
        
        self.answer = f"""EIRP: {eirp.W} W, {eirp.dBm} dBm, {eirp.dBW} dBW
Power density: {power_density.uWperm2} uW/m2
Power density if isotropic: {power_density_iso.uWperm2} uW/m2"""

class tomasi_15_2:
    def __init__(self, *args, **kwargs):
        radiation_resistance = c.resistance(ran.main(72))
        effective_resistance = c.resistance(ran.main(8))
        directive_gain = c.dbvalue(ran.main(20))
        power = c.power(ran.main(100))
        
        self.question = f"""For a transmit antenna with a radiation resistance Rr = {radiation_resistance.ohms} ohms, an effective antenna resistance Re = {effective_resistance.ohms} ohms, a directive gain D = {directive_gain.unitless}, and an input power of Pin = {power.W} W, determine the antenna efficiency, antenna gain (absolute and in dB) , radiated power (in watts, dBm, and dBW), and EIRP (in watts, dBm, and dBW)."""
        
        efficiency = c.percentage(
        radiation_resistance.ohms / (radiation_resistance.ohms + effective_resistance.ohms), 'decimal'
        )
        
        antenna_gain = c.dbvalue(
        efficiency.decimal * directive_gain.unitless
        )
        
        radiated_power = c.power(
        power.W * efficiency.decimal
        )
        
        eirp = c.power(
        power.W * antenna_gain.unitless
        )
        
        
        self.answer = f"""Efficiency: {efficiency.percent} %
Antenna Gain: {antenna_gain.unitless}, {antenna_gain.dB} dB
Radiated Power: {radiated_power.W} W, {radiated_power.dBW} dBW, {radiated_power.dBm} dBm
EIRP: {eirp.W} W, {eirp.dBW} dBW, {eirp.dBm} dBm"""

class tomasi_15_3:
    def __init__(self, *args, **kwargs):
        power_output = c.power(ran.main(40), 'dBm')
        transmission_line_loss = c.dbvalue(ran.main(3), 'dB')
        free_space_path_loss = c.dbvalue(ran.main(50), 'dB')
        directive_gain = c.dbvalue(ran.main(10))
        efficiency = c.percentage(ran.main(50), 'percent')
        
        self.question = f"""Given the free-space radio transmission system with the following transmission characteristics:
Transmitter power output: {power_output.dBm} dBm
Transmission line loss: {transmission_line_loss.dB} dB
Free-space path loss: {free_space_path_loss.dB} dB
Determine the antenna input power, radiated power, EIRP, and received power density for an antenna with directivity D = {directive_gain.unitless} and an efficiency of {efficiency.percent} %."""

        antenna_input_power = c.power(
        power_output.dBm - transmission_line_loss.dB, 'dBm'
        )
        
        radiated_power = c.power(
        antenna_input_power.dBm + 10 * math.log(efficiency.decimal, 10), 'dBm'
        )
        
        eirp = c.power(
        radiated_power.dBm + directive_gain.dB, 'dBm'
        )
        
        receive_power_density = c.power(
        eirp.dBm - free_space_path_loss.dB, 'dBm'
        )
        
        self.answer = f"""Antenna input power: {antenna_input_power.dBm} dBm
Radiated power: {radiated_power.dBm} dBm
EIRP: {eirp.dBm} dBm
Received power density: {receive_power_density.dBm} dBm"""

class tomasi_15_4:
    def __init__(self, *args, **kwargs):
        receive_power_density = c.powerDensity(ran.main(10), 'uWperm2')
        capture_area = c.area(ran.main(0.2), 'm2')
    
        self.question = f"""For a receive power density of {receive_power_density.uWperm2} uW/m2 and a receive antenna with a capture area of {capture_area.m2} m2, determine the captured power in watts and dBm."""
        
        captured_power = c.power(
        receive_power_density.Wperm2 * capture_area.m2
        )
        
        self.answer = f"""Captured power: {captured_power.W} W, {captured_power.dBm} dBm"""
        
class tomasi_15_5:
    def __init__(self, *args, **kwargs):
        frequency = c.frequency(ran.main(400), 'MHz')
        offset = c.frequency(ran.main(20), 'MHz')
        upper = c.frequency(frequency.Hz + offset.Hz)
        lower = c.frequency(frequency.Hz - offset.Hz)
        
        self.question = f"""Determine the percent bandwidth for an antenna with an optimum frequency of operation of {frequency.MHz} MHz and - 3dB frequencies of {lower.MHz} MHz and {upper.MHz} MHz."""
        
        percent_bandwidth = c.percentage(
        (upper.Hz - lower.Hz) / (frequency.Hz), 'decimal'
        )
        
        self.answer = f"""Percent Bandwidth = {percent_bandwidth.percent} %"""
        
class tomasi_15_6:
    def __init__(self, *args, **kwargs):
        diameter = c.length(ran.main(2))
        power = c.power(10)
        frequency = c.frequency(ran.main(6), 'GHz')
        antenna_efficiency = c.percentage(ran.main(55), 'percent')
        aperture_efficiency = c.percentage(antenna_efficiency.percent, 'percent')
        
        self.question = f"""For a {diameter.m}-m diameter parabolic reflector with {power.W} W of power radiated by the feed mechanism operating at {frequency.GHz} GHz with a transmit antenna efficiency of {antenna_efficiency.percent} % and an aperture efficiency of {aperture_efficiency.percent} %, determine the beamwidth, the transmit power gain, receive power gain, and the EIRP."""
        
        beamwidth = c.angle(
        (70 * 3e8) / (frequency.Hz * diameter.m) , 'degrees'
        )
        
        antenna_gain = c.dbvalue(
        antenna_efficiency.decimal * ((math.pi * diameter.m)/(3e8/frequency.Hz))**2, 'unitless'
        )
        
        eirp = c.power( 
        antenna_gain.dB + power.dBm, 'dBm'
        )
        
        self.answer = f"""Beamwidth: {beamwidth.degrees} degrees
Transmit/Receive power gain: {antenna_gain.dB} dB
EIRP: {eirp.dBm} dBm"""


