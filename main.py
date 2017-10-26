'''
Created on Oct 25, 2017

@author: kevin
'''
from scraper.driver import Driver
from scraper.lowes import Lowes

def main():
    
    pLowes = Lowes()
    
    pLowes.scrap_it("https://www.lowes.com/pd/GE-Z-Wave-Plus-15-Amp-Single-Pole-3-Way-Wireless-White-Toggle-Indoor-Light-Switch/1000241625","1000241625")
    pLowes.scrap_it("https://www.lowes.com/pd/GE-Z-Wave-Plus-15-Amp-Single-Pole-3-Way-Wireless-White-Almond-Rocker-Indoor-Light-Switch/1000241629","1000241629")
    pLowes.dispose()
    del pLowes

if __name__ == '__main__':
    main()
    #pass