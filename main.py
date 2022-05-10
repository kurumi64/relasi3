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
minyak1.set_nama("Minyak Eceran")
minyak1.set_harga(56500)
minyak1.show_produk()

print("=" * 30)

minyak2 = Minyak()
minyak2.set_nama("Minyak Bimoli")
minyak2.set_harga(1000000)
minyak2.show_produk()
