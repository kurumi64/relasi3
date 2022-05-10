from telur import Telur
from minyak import Minyak

telur = Telur()
telur.set_nama("Telur Asin")
telur.set_harga(12500)
telur.show_produk()

print("=" * 30)

telur.set_nama("Telur Asin (Banget)")
telur.set_harga(13000)
telur.show_produk()

minyak1 = Minyak()
minyak1.set_nama("minyak eceran")
minyak1.set_harga(30000)
minyak1.show_produk()

print("=" * 30)

minyak2 = Minyak()
minyak2.set_nama("minyak bimoli")
minyak2.set_harga(1000000)
minyak2.show_produk()
