from telur import Telur
from minyak import Minyak
from stok import Stok

telur_asin = Telur()
telur_asin.set_nama("Telur Asin")
telur_asin.set_harga(12500)
stok_telur_asin = Stok(telur_asin, 3)

telur_asin.show_produk()
print("Stok:", stok_telur_asin.get_qty())

print("=" * 30)

minyak1 = Minyak()
minyak1.set_nama("minyak eceran")
minyak1.set_harga(30000)
stok_minyak1 = Stok(minyak1, 2)

minyak1.show_produk()
print("Stok:", stok_minyak1.get_qty())

print("=" * 30)

minyak2 = Minyak()
minyak2.set_nama("minyak bimoli")
minyak2.set_harga(1000000)
stok_minyak2 = Stok(minyak2, 12)

minyak2.show_produk()
print("Stok:", stok_minyak2.get_qty())

minyak1 = Minyak()
minyak1.set_nama("minyak eceran")
minyak1.set_harga(30000)
minyak1.show_produk()

print("=" * 30)

minyak2 = Minyak()
minyak2.set_nama("minyak bimoli")
minyak2.set_harga(1000000)
minyak2.show_produk()

