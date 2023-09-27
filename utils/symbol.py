class Symbol:
  
  def messager(self):
        if self.type == 1:
          message = f"SAT\nKod: {self.code} Tavan Bozdu\nAnlık Fiyat: {self.currentPrice}₺\nGünlük Değişim: %{self.dailyChangePercentage:.2f}"
        elif self.type == 2:
            message = f"ALIM/SATIM FIRSATI\nKod: {self.code} \nAnlık Fiyat: {self.currentPrice}₺\nGünlük Değişim: %{self.dailyChangePercentage:.2f}"
        else:
            message = f"Envanter\nKod: {self.code}\nFiyat: {self.currentPrice:.4f}₺\nDeğişim: %{self.dailyChangePercentage:.2f}"
        return message

  def __init__(self, symbol, currentPrice, previousClose, type):
    self.symbol = symbol
    self.type = type
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