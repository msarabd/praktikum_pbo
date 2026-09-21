
# ⚽ CLI Penalty Simulator

Halo bang-abang! Selamat datang di repo kodingan **CLI Penalty Simulator**. Intinya, ini program simulasi adu penalti sederhana yang dibikin pakai Python. Program ini dibuat pakai pendekatan *Object-Oriented Programming* (OOP), jadi udah *include* materi Class & Object, Attribute & Method, sampai Encapsulation & Property.

---

## 🏗️ Struktur Class

Ada **3 Class Utama** yang saling berinteraksi. Semuanya udah disetting pakai *private attribute* dan diakses pakai *decorator* `@property` (getter) dan `@<nama>.setter` (setter).

### 1. `Kicker` (Penendang)

Class ini fungsinya buat nyetak objek pemain yang akan  menendang bola.

* **Atribut Class:** `__jumlahKicker` (buat tracking udah ada berapa penendang yang didaftarin).
* **Atribut Instance:** `name` (public), `__team` (private), dan `__shotStat` (private).
* **Validasi:** Tim cuma bisa diisi "barca" atau "madrid" (selain itu akan kena `ValueError`). Nilai tembakan (`shotStat`) juga tidak boleh bertipe data string ataupun bernilai negatif.

### 2. `Keeper` (Kiper)

Class ini fungsinya buat nyetak objek kiper yang akan menepis bola.

* **Atribut Class:** `__jumlahKeeper` (tracking total kiper).
* **Atribut Instance:** `name` (public), `__team` (private), dan `__reachStat` (private).
* **Validasi:** Sama kayak `Kicker`, timnya dilock cuma buat Barca dan Madrid. Nilai jangkauan (`reachStat`) wajib angka dan tidak boleh negatif.

### 3. `Match` (Pertandingan)

Class ini yang mengatur *flow* pertandingannya.

* **Atribut Class:** `__jumlahMatch` (ngitung total match yang udah jalan).
* **Atribut Instance:** `__skorA`, `__skorB`, dan `__jumlahPutaran`.
* **Method:**
  * `add_goal(team)` (*Instance method*): Buat nambahin skor tim sekaligus nambahin jumlah putaran.
  * `get_skor()` (*Instance method*): Buat nge-print skor saat ini.
  * `cekPutaranUp5()` (*Instance method*): Validasi kalau putaran udah lebih dari 5, dia bakal di-modulo 5.
  * `show_jumlahMatch()` (*Class method*): Buat nampilin total match yang udah terjadi.

---

## 🚀 Pengujian (Setter)

Di akhir kode, terdapat pengisian setter dengan nilai yang valid ataupun tidak. Untuk pengujian dengan nilai tidak valid, aku mencoba untuk memberikan nilai yang berbeda untuk setter team, nilai negatif untuk setter shotStat, input kosong untuk setter team, nilai bertipe data string untuk setter reachStat, dan input kosong untuk setter jumlah putaran. Semua setter berhasil dijalankan dan mengembalikan error yang ditangkap pada blok try-except.
