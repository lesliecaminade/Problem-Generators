import random_handler as ran
import math
import random
import constants_conversions as c
import interpolation
import sympy as sym

x, y, z, t = sym.symbols('x y z t', real = True)

class jma_5_121:
    def __init__(self, *args, **kwargs):
        
        area = c.area(ran.main(2000), 'km2')
        radius = c.length(ran.main(2), 'km')
        
        self.question = f"""A province in the Philippines has an area of {area.km2} sq. kms. It has to be covered by cellular mobile telephone service using cells with radius of {radius.km} kms. Assuming hexagonal cells, find the number of cellsites needed."""
        
        cells = area.km2 / ( 3.464 * radius.km**2 )
        cells = math.ceil(cells)
        
        self.answer = f"""Number of cells = {cells} cells"""
        
class jma_5_122:
    def __init__(self, *args, **kwargs):
        
        clusters = ran.main(20, 'int')
        cells = ran.main(10, 'int')
        channelspercell = ran.main(16, 'int')
        
        self.question = f"""Calculate the theoretical number of full duplex channels available in a cluster and the total capacity for a cellular system where there are {clusters} clusters, each consisting of {cells} cells with {channelspercell} channels per cell."""
        
        channels = cells * channelspercell
        capacity = clusters * channels
        
        self.answer = f"""Full duplex channels per clusters = {channels}
Total capacity = {capacity} channels"""

class jma_5_123_a:
    def __init__(self, *args, **kwargs):
        
        
        cellspercluster = ran.main(25, 'int')
        
        self.question = f"""Determine the co-channel reuse ratio for a cluster with {cellspercluster} cells"""
        
        cochannelreuseratio = math.sqrt( 3 * cellspercluster )
        
        self.answer = f"""Co-channel reuse ratio = {cochannelreuseratio}"""
        
class jma_5_123_b:
    def __init__(self, *args, **kwargs):
        
        
        velocity = c.velocity(ran.main(100), 'kmperh')
        distance = c.length(ran.main(10), 'km')
        
        self.question = f"""How often will handoffs occur when the vehicle travels through a CMTS at {velocity.kmperh} km/h speed if the distance between cellsites is {distance.km} km?"""
        
        time = c.time(
        distance.m / velocity.mpers
        )
        
        self.answer = f"""Handoff interval = {time.s} s"""
        
class jma_5_132_a:
    def __init__(self, *args, **kwargs):
        
        channelpercell = ran.main(5, 'int')
        erlangs = ran.main(1.66)
        
        self.question = f"""Calculate the blocking probability for {channelpercell}-channel cell with an offered traffic of {erlangs} erlangs."""
        
        blocking = c.percentage(
        (erlangs**channelpercell/math.factorial(channelpercell)) / 
        sym.Sum(erlangs**x/sym.factorial(x), (x, 1, channelpercell)).doit(), 'decimal'
        )
        
        self.answer = f""" Blocking probability = {blocking.percent} %"""

class jma_5_132_b:
    def __init__(self, *args, **kwargs):
        
        maxcallsperhourpercell = ran.main(3000, 'int')
        averagecallingtime = c.time(ran.main(1.76), 'min')
        blocking = c.percentage(ran.main(2), 'percent')
        
        self.question = f"""From the following data, determine the offered traffic of a cell.
Maximum calls per hour in one cell = {maxcallsperhourpercell}
Average calling time = {averagecallingtime.min}
Blocking probability = {blocking.percent} %"""

        erlangs = maxcallsperhourpercell * averagecallingtime.min / 60
        
        self.answer = f"""Traffic = {erlangs} erlangs"""

class jma_5_133_a:
    def __init__(self, *args, **kwargs):
        
        cells = ran.main(120, 'int')
        subscribers = ran.main(20_000, 'int')
        cellspercluster = ran.main(12, 'int')
        peakhourminutes = c.time(ran.main(20, 'int'), 'min')
        usageminutesperday = c.time(peakhourminutes.min + ran.main(25, 'int'), 'min')
        
        self.question = f"""A particular cellular telephone system consisting of {cells} cells and catering {subscribers} is using a {cellspercluster}-cell repeating pattern. If each subscriber on this network uses his/her phone on average {usageminutesperday.min} minutes per day, and also on average  {peakhourminutes.min} of those minutes are used during the peak hour, calculate the peak and average traffic for one cell, assuming callers are evenly distributed over the system."""
        
        peaktraffic = subscribers * peakhourminutes.min/60
        avetraffic = subscribers * usageminutesperday.day
        
        peaktraffic_cell = peaktraffic/cells
        avetraffic_cell = avetraffic/cells
        
        self.answer = f"""Peak traffic = {peaktraffic_cell} Erlangs
Average traffic = {avetraffic_cell} Erlangs"""

class jma_5_133_b:
    def __init__(self, *args, **kwargs):
        
        callduration = c.time(ran.main(1.76), 'min')
        blocking = c.percentage(ran.main(2), 'percent')
        channels = random.randint(661, 699)
        
        self.question = f"""Assuming the average duration of each call be {callduration.min} minutes and from Erlang B tables for {blocking.percent} % blocking.
Channels            Traffic
660                 587.2
{channels}          ?
700                 688.2

How many channels can be served with {channels} voice channels if all the channels are used in a single cell?"""

        traffic = interpolation.translate(channels, 660, 700, 587.2, 688.2)
        calls = (traffic/callduration.min) * (60)
        
        self.answer = f"""Calls = {calls}"""
        


        
        
        

        
        
        
        
        
        
        
        
        
