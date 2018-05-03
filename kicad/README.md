### The gpio board

The gpio board was created using KiCad 5.  (And should be renamed to something else)

### OSH Park

To make a board, use OSH Park.  Upload the `tristate.kicad_pcb` file.

### Parts

The connector is a .1" 2x5 connector.  Similar to this: 
https://ae01.alicdn.com/kf/HTB14E6sJFXXXXaIXVXXq6xXFXXXK/10PCS-2x5-2-54mm-10Pin-Double-Row-Female-Straight-Header-Pitch-Socket-Pin-Strip-Connectors.jpg

While the schematic notes 200 ohm resistors, these should be paired to the LED that you're using.  Eg

    A Diode with a 1.9V forward voltage should use around a 1400 ohm resitor for a 1ma current.  
    
    (3.3v - 1.9v) / .001 mA = 1400ohm.

These are 1206 surface mounts, and can be bought from Digikey, Mouser, Aliexpress, Banggood.




