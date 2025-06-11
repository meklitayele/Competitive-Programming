class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kel = celsius + 273.15
        fah = celsius * 1.80 + 32.00
        return [kel,fah]
    