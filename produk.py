from abc import ABC, abstractclassmethod

class Produk:
  def __init__(self):
    self.__nama = ""
    self.__harga = 0
  
  def set_nama(self, nama: str):
    self.__nama = nama
  
  def get_nama(self):
    return self.__nama
  
  def set_harga(self, harga: float):
    self.__harga = harga
  
  def get_harga(self):
    return self.__harga
  
  @abstractclassmethod
  def show_produk(self):
    pass