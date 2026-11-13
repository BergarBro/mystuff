G21 (Metric)
G90 (Absolute Positioning)
G54 G00 X0 Y-3 Z0 (Set machine to start position)

G00 Z-0
o100 call
G00 Z-0.5
o100 call
G00 Z-1
o100 call
G00 Z-1.5
o100 call
G00 Z-2
o100 call
G00 Z-2.5
o100 call
G00 Z-3
o100 call
G00 Z-3.5
o100 call
G00 Z-4
o100 call
G00 Z-4.5
o100 call
G00 Z-5
o100 call
G00 Z-5.5
o100 call
G00 Z-6
o100 call
G00 Z-6.5
o100 call
G00 Z-7
o100 call
G00 Z-7.5
o100 call
G00 Z-8
o100 call
G00 Z-8.5
o100 call
G00 Z-9
o100 call
G00 Z-9.5
o100 call
G00 Z-10
o100 call
G00 Z-10.5
o100 call
G00 Z-11
o100 call
G00 Z-11.5
o100 call
G00 Z-12
o100 call
G00 Z-12.5
o100 call
G00 Z-13
o100 call
G00 Z-13.5
o100 call
G00 Z-14
o100 call
M30


o100 sub
    G01 X0 Y-3 F110
    G01 X17.321 Y-3 
    G01 X34.671 Y27
    G01 X17.321 Y57
    G01 X-17.321 Y57
    G01 X-34.671 Y27
    G01 X-17.321 Y-3
    G01 X0 Y-3
o100 endsub