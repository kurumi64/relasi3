from produk import Produk

class Telur(Produk):
  def show_produk(self):
    print(f"Nama Produk: {self.get_nama()}\nHarga: {self.get_harga()}")