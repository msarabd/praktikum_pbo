class AkunBank:
    def __init__(self,nama, saldo):
        self.nama = nama
        self.saldo = saldo
        
    def hitung_bunga(self):
        return 0
    
    
class Tabungan(AkunBank):
    def hitung_bunga(self):
        return self.saldo * 0.02
    
class Deposito(AkunBank):
    def hitung_bunga(self):
        return self.saldo * 0.06

daftar_akun = [Tabungan("Budi", 1000000), Deposito("Siti", 2000000)]

for akun in daftar_akun:
    print(f"Bunga {akun.nama}: Rp {akun.hitung_bunga():,.2f}")

class RekeningTabungan:
    def __init__(self, saldo):
        self.saldo = saldo

    def tarik_uang(self, jumlah):
        if jumlah <= self.saldo:
            self.saldo -= jumlah
        else:
            print(f"Saldo tidak cukup")

class RekeningGiro:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def tarik_uang(self, jumlah):
        if jumlah <= self.saldo:
            self.saldo -= jumlah
            print(f"Penarikan Rp{jumlah:,} dari rekening giro berhasil.")
            print(f"Saldo tersisa: Rp{self.saldo:,}")
        else:
            print("Saldo tidak cukup.")

# duck typing
def proses_penarikan(rekening, jumlah):
    rekening.tarik_uang(jumlah)

tabungan = RekeningTabungan(5_000_000)
giro = RekeningGiro(10_000_000)
proses_penarikan(tabungan, 1_000_000)
proses_penarikan(giro, 2_000_000)

from abc import ABC, abstractmethod
class Transaksi(ABC):
    @abstractmethod
    def validasi(self):
        pass
    
    @abstractmethod
    def eksekusi(self):
        pass

class TarikTunai(Transaksi):
    def __init__(self, saldo_akun, nominal):
        self.saldo = saldo_akun
        self.nominal = nominal
    
    def validasi(self):
        if self.nominal > self.saldo:
            return False
        return True
    
    def eksekusi(self):
        if self.validasi():
            self.saldo -= self.nominal
            print(f"Tarik tunai berhasil. Sisa saldo: {self.saldo}")
        else:
            print("Saldo tidak cukup!")

class TransferGagal(Transaksi):
    def validasi(self):
        return True


transaksi_sukses = TarikTunai(100000, 50000)
transaksi_sukses.eksekusi()
print (transaksi_sukses)