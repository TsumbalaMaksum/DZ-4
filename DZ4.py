class SSD:
    def __init__(self, *rgs, **kwargs):
        super().__init__(*rgs, **kwargs)
        self.ssdname = "Kingston A2000"
        self.ssdmemory = "1TB"
        self.ssdspeed = "2800mb"
        self.ssdcolor = "black"

class RAM:
    def __init__(self, *rgs, **kwargs):
        super().__init__(*rgs, **kwargs)
        self.memoryname = "Hyperx Kingston Fury"
        self.memorymemory = "16gb"
        self.memoryddr = "DDR4"
        self.memorything = "2"
        self.memorycolor = "black"

class GPU:
    def __init__(self, *rgs, **kwargs):
        super().__init__(*rgs, **kwargs)
        self.gpuname = "RX 570"
        self.gpumemory = "8gb"
        self.gpucooler = "2 cooler without backlight"
        self.gpubacklight = "RGB only logo"
        self.gpucolor = "black"

class CPU:
    def __init__(self, *rgs, **kwargs):
        super().__init__(*rgs, **kwargs)
        self.cpuname = "Intel Core i3-9100F"
        self.cpucore = "8"
        self.cpuddr = "DDR4"
        self.cpusteam = "16"

class Motherboard:
    def __init__(self, *rgs, **kwargs):
        super().__init__(*rgs, **kwargs)
        self.motherboardname = "Gigabyte b365m HD3"
        self.motherboardhubs = "4 USB 3.0 2 USB 2.0 1 WGA 1 DVI 1 HDMI 3 Mini-Jeck"
        self.motherboardcolor = "black"

class Case:
    def __init__(self, *rgs, **kwargs):
        super().__init__(*rgs, **kwargs)
        self.casename = "Gamemax"
        self.casecooler = "3 cooler with/without RGB backlight"
        self.casehubs = "2 USB 3.0 2 Mini-Jeck"

class PC(SSD, RAM, GPU, CPU, Motherboard, Case):
        def __init__(self, prise, *rgs, **kwargs):
              super().__init__(*rgs, **kwargs)
              self.prise = prise

        def print_info(self):
            print("SSD")
            print("")
            print(self.ssdname)
            print(self.ssdmemory)
            print(self.ssdspeed)
            print(self.ssdcolor)
            print("===============")
            print("RAM")
            print("")
            print(self.memoryname)
            print(self.memorymemory)
            print(self.memoryddr)
            print(self.memorything)
            print(self.memorycolor)
            print("===============")
            print("GPU")
            print("")
            print(self.gpuname)
            print(self.gpumemory)
            print(self.gpucooler)
            print(self.gpubacklight)
            print(self.gpucolor)
            print("===============")
            print("CPU")
            print("")
            print(self.cpuname)
            print(self.cpucore)
            print(self.cpuddr)
            print(self.cpusteam)
            print("===============")
            print("Motherboard")
            print("")
            print(self.motherboardname)
            print(self.motherboardhubs)
            print(self.motherboardcolor)
            print("===============")
            print("Case")
            print("")
            print(self.casename)
            print(self.casecooler)
            print(self.casehubs)
            print("===============")
            print("Price")
            print("")
            print(self.prise)


PC = PC(prise=35000)
PC.print_info()



