class Stok:
  def __init__(self, Produk, qty):
    self.__Produk = Produk
    self.__qty = qty
  
  def get_produk(self):
    return self.__Produk
  
  def get_qty(self):
    return self.__qty
  