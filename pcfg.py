import os

pcfgPath = os.path.join(os.path.expanduser('~'), 'Documents', '.pcfg')

if os.path.isfile(pcfgPath):
    pcfgFile = open(pcfgPath, mode="r")
    