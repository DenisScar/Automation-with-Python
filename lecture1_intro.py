import ezdxf

doc = ezdxf.new("R2010")
msp = doc.modelspace()

msp.add_line((0,0), (100,0))

doc.saveas("lecture1.dxf")
