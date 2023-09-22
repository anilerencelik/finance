class Symbol:

  def messager1(self):
      message = f"SAT\nKod: {self.code} Tavan Bozdu\nAnlık Fiyat: {self.currentPrice}₺\nGünlük Değişim: %{self.dailyChangePercentage:.2f}"
      return message

  def messager2(self):
      message = f"SATIN ALIM FIRSATI\nKod: {self.code} \nAnlık Fiyat: {self.currentPrice}₺\nGünlük Değişim: %{self.dailyChangePercentage:.2f}"
      return message

  def __init__(self, symbol, currentPrice, previousClose):
    self.symbol = symbol
    self.currentPrice = currentPrice
    self.previousClose = previousClose
    self.dailyChange = currentPrice - previousClose
    self.dailyChangePercentage = (abs(currentPrice-previousClose)/previousClose) * 100
    self.code = self.symbol.split(".")[0]
    if self.dailyChange > 0:
        self.isHigher = True
    else:
        self.isHigher = False
        self.dailyChangePercentage *= -1