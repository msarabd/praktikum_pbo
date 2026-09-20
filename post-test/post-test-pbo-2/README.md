
# Dokumentasi Posttest: Simulasi Pertandingan Sepak Bola (OOP Python)

Dokumentasi ini berisi penjelasan mengenai program simulasi pertandingan sepak bola berbasis *Object-Oriented Programming* (OOP) dalam bahasa pemrograman Python. Program ini mengimplementasikan konsep dasar OOP, pembatasan hak akses (*encapsulation*), serta penggunaan berbagai jenis method dan property.

---

## 1. Deskripsi Program

Program ini mensimulasikan komponen-komponen dalam sebuah pertandingan penalti/sepak bola antara dua tim (Barca dan Madrid). Program terdiri dari tiga class utama:

1. **`Kicker`**: Memodelkan pemain penendang beserta statistik tendangannya.
2. **`Keeper`**: Memodelkan penjaga gawang beserta statistik jangkauannya.
3. **`Match`**: Memodelkan jalannya pertandingan, pencatatan skor, dan perhitungan jumlah putaran.

---

## 2. Struktur Class dan Atribut

### A. Class `Kicker`

* **Atribut Kelas**:
  * `__jumlahKicker` (*private*): Menyimpan total objek Kicker yang telah dibuat.
* **Atribut Instance**:
  * `name` (*public*): Nama penendang.
  * `__team` (*private*): Nama tim penendang (`"barca"` atau `"madrid"`).
  * `__shotStat` (*private*): Statistik kekuatan/akurasi tendangan (integer $\ge 0$).
* **Method**:
  * `__init__(name, team, shotStat)`: Constructor untuk inisialisasi objek.
  * `@property team`: Getter untuk mengambil data tim.
  * `@team.setter`: Setter untuk merubah tim dengan validasi (hanya menerima `"barca"` atau `"madrid"`).
  * `@property shotStat`: Getter untuk mengambil statistik tendangan.
  * `@shotStat.setter`: Setter untuk merubah statistik tendangan dengan validasi (tipe data integer dan $\ge 0$).
  * `@staticmethod get_JumlahKicker()`: Static method untuk mengembalikan jumlah objek Kicker.

---

### B. Class `Keeper`

* **Atribut Kelas**:
  * `__jumlahKeeper` (*private*): Menyimpan total objek Keeper yang telah dibuat.
* **Atribut Instance**:
  * `name` (*public*): Nama penjaga gawang.
  * `__team` (*private*): Nama tim penjaga gawang (`"barca"` atau `"madrid"`).
  * `__reachStat` (*private*): Statistik jangkauan kiper (integer $\ge 0$).
* **Method**:
  * `__init__(name, team, reachStat)`: Constructor untuk inisialisasi objek.
  * `@property team`: Getter untuk mengambil data tim.
  * `@team.setter`: Setter untuk merubah tim dengan validasi.
  * `@property reachStat`: Getter untuk mengambil statistik jangkauan.
  * `@reachStat.setter`: Setter untuk merubah statistik jangkauan dengan validasi (tipe data integer dan $\ge 0$).
  * `@staticmethod get_JumlahKeeper()`: Static method untuk mengembalikan jumlah objek Keeper.

---

### C. Class `Match`

* **Atribut Kelas**:
  * `__jumlahMatch` (*private*): Menyimpan total pertandingan yang telah dilaksanakan.
* **Atribut Instance**:
  * `__skorA` (*private*): Skor untuk Barca.
  * `__skorB` (*private*): Skor untuk Madrid.
  * `__jumlahPutaran` (*private*): Jumlah putaran/tendangan yang berjalan.
* **Method**:
  * `__init__(skorA, skorB)`: Constructor untuk inisialisasi skor dan perhitungan putaran awal.
  * `@property jumlahPutaran`: Getter untuk melihat jumlah putaran.
  * `@jumlahPutaran.setter`: Setter untuk memperbarui jumlah putaran dengan logika *modulo* jika nilai $> 5$.
  * `add_goal(team)` (*Instance Method*): Menambahkan skor tim dan menambah jumlah putaran.
  * `get_skor()` (*Instance Method*): Mengembalikan string format skor akhir/saat ini.
  * `@classmethod show_jumlahMatch(cls)`: Class method untuk menampilkan total pertandingan yang telah berjalan.

---

## 3. Panduan Pengujian (Testing Guide)

Pengujian program dilakukan di bagian bawah file (*Main Code*) untuk membuktikan bahwa seluruh logika dan validasi berjalan dengan baik.

### Skenario Pengujian:

1. **Instansiasi Objek (Minimal 2 Objek per Class)**:
   * Membuat `kicker1`, `kicker2`, `keeper1`, `keeper2`, `match1`, dan `match2`.
2. **Pengujian Jenis Method**:
   * **Static Method**: `Kicker.get_JumlahKicker()` & `Keeper.get_JumlahKeeper()`
   * **Instance Method**: `match1.add_goal("barca")` & `match2.get_skor()`
   * **Class Method**: `Match.show_jumlahMatch()`
3. **Pengujian Setter Data Valid**:
   * Mengubah properti dengan input yang sesuai aturan (misal: mengubah tim menjadi `"madrid"` atau `shotStat` menjadi `23`).
4. **Pengujian Setter Data Invalid (Validasi)**:
   * Menguji percobaan pengisian data yang melanggar syarat (misal: tim di luar barca/madrid, angka negatif, atau tipe data string pada statistik).
   * Pengujian dibungkus menggunakan blok `try ... except` untuk membuktikan bahwa exception (`ValueError` / `TypeError`) berhasil ditangkap tanpa menghentikan program secara paksa.

---

## 4. Cara Jalankan Program

Pastikan Python 3.x telah terinstal di perangkat Anda, kemudian jalankan perintah berikut pada terminal/command prompt:

```bash
python nama_file_anda.py
```
