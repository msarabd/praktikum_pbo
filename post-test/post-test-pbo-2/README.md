
# CLI Penalty Simulator

Program simulasi adu penalti berbasis python yang mencakup konsep **Relasi UML (Asosiasi, Agregasi, Komposisi)**, **Pewarisan (Inheritance & Method Overriding)**, serta **Enkapsulasi**.

---

## 📋 Daftar Isi

1. [Deskripsi Program](#deskripsi-program)
2. [Implementasi Konsep OOP](#implementasi-konsep-oop)
   - [1. Relasi UML](#1-relasi-uml)
   - [2. Inheritance (Pewarisan)](#2-inheritance-pewarisan)
   - [3. Enkapsulasi &amp; Aksesibilitas](#3-enkapsulasi--aksesibilitas)
3. [Struktur Kelas](#struktur-kelas)
4. [Alur Logika Simulasi](#alur-logika-simulasi)
5. [Cara Menjalankan](#cara-menjalankan)

---

## ⚽ Deskripsi Program

Program ini mensimulasikan adu tendangan penalti antara dua tim (`Barcelona` dan `Madrid`). Setiap putaran mempertemukan seorang penendang (`Kicker`) dan seorang penjaga gawang (`Keeper`). Hasil penalti ditentukan oleh arah tendangan vs arah lompatan kiper, atribut statistik masing-masing pemain (`shotStat` vs `reachStat`), serta faktor ketidakpastian acak (*random factor*).

---

## 🧩 Implementasi Konsep OOP

### 1. Relasi UML

Program ini memenuhi 3 jenis relasi:

| Jenis Relasi                      | Implementasi dalam Kode                                                 | Penjelasan                                                                                                                                                                             |
| :-------------------------------- | :---------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Asosiasi (Association)**  | `MatchRound` $\leftrightarrow$ `Player` (`Kicker` & `Keeper`) | `MatchRound` mereferensikan objek `Kicker` dan `Keeper` untuk mengeksekusi duel putaran penalti tanpa memiliki siklus hidup pemain tersebut. Objek pemain dapat berdiri sendiri. |
| **Agregasi (Aggregation)**  | `Team` $\diamondsuit\longrightarrow$ `Player`                     | Tim menampung kumpulan pemain melalui method`add_player()`. Jika objek `Team` dihapus, objek `Player` masih tetap eksis secara independen.                                       |
| **Komposisi (Composition)** | `Match` $\blacklozenge\longrightarrow$ `MatchRound`               | Objek`MatchRound` diinstansiasi secara internal di dalam method `add_round()` milik `Match`. Putaran babak tidak dapat eksis tanpa adanya pertandingan induk.                    |

---

### 2. Inheritance (Pewarisan)

Sistem pewarisan dibangun dengan tingkatan:

- **Superclass (Parent Class):** `Player`
- **Subclass (Child Class):** `Kicker` dan `Keeper`

Karakteristik implementasi inheritance pada kode:

1. **Penggunaan `super().__init__()`:**
   Kedua subclass (`Kicker` dan `Keeper`) memanggil konstruktor parent class untuk inisialisasi nama (`_name`) dan tim (`_team`).
   ```python
   class Kicker(Player):
       def __init__(self, name, team=None, shotStat=0):
           super().__init__(name, team)
           self.__shotStat = max(0, shotStat)
   ```
2. **Atribut Spesifik (Child-Specific Attributes):**
   - `Kicker`: Memiliki atribut unik `__shotStat` (kekuatan/akurasi tendangan).
   - `Keeper`: Memiliki atribut unik `__reachStat` (jangkauan/kemampuan tepisan).
3. **Method Overriding:**
   Method `respawn()` dari `Player` didefinisikan ulang (*override*) pada masing-masing subclass:
   - `Player.respawn()` $\rightarrow$ *"Berhasil menambah pemain atas nama {name}"*
   - `Kicker.respawn()` $\rightarrow$ *"Berhasil menambah penendang atas nama {name}"*
   - `Keeper.respawn()` $\rightarrow$ *"Berhasil menambah kiper atas nama {name}"*

---

### 3. Enkapsulasi & Aksesibilitas

Program membedakan hak akses atribut dan method secara ketat:

- **Protected (`_attribute`):**
  - Digunakan untuk atribut yang diwariskan atau diakses subclass, seperti `self._name` dan `self._team`.
- **Private (`__attribute`):**
  - Digunakan untuk data internal eksklusif:
    - Counter statik: `Player.__playerCount`, `Team.__teamCount`, `Kicker.__kickerCount`, `Keeper.__keeperCount`.
    - Statistik performa: `Kicker.__shotStat` dan `Keeper.__reachStat`.
    - Helper method: `MatchRound.__execute_duel()`.
- **Property & Setter Validation:**
  - `shotStat` dan `reachStat` diverifikasi menggunakan decorator `@property` dan `@setter` untuk memastikan nilai bertipe `int` dan bernilai non-negatif ($\ge 0$).

---

## 🏛️ Struktur Kelas

```
        ┌─────────────────────────┐
        │         Player          │
        ├─────────────────────────┤
        │ - __playerCount: int    │
        │ # _name: str            │
        │ # _team: Team           │
        ├─────────────────────────┤
        │ + respawn(): void       │
        └────────────▲────────────┘
                     │ (Inheritance)
         ┌───────────┴───────────┐
         │                       │
┌────────────────────┐  ┌────────────────────┐
│      Kicker        │  │       Keeper       │
├────────────────────┤  ├────────────────────┤
│ - __kickerCount    │  │ - __keeperCount    │
│ - __shotStat: int  │  │ - __reachStat: int │
├────────────────────┤  ├────────────────────┤
│ + respawn(): void  │  │ + respawn(): void  │
└────────────────────┘  └────────────────────┘

Relasi Struktural Tambahan:
- Team o--> Player (Agregasi)
- Match *--> MatchRound (Komposisi)
- MatchRound --> Kicker & Keeper (Asosiasi)
```

---

## ⚙️ Alur Logika Simulasi

Pada setiap eksekusi putaran:

1. **Peluang Melebar (5%):**
   Tendangan memiliki kemungkinan 5% meleset keluar tanpa gangguan kiper.
2. **Perbedaan Arah:**
   Jika arah tembakan penendang (`kiri`, `tengah`, `kanan`) berbeda dengan arah lompatan kiper, maka langsung menghasilkan **GOL**.
3. **Arah Sama (Adu Statistik):**
   Jika kiper menebak arah dengan tepat:

   $$
   \text{Power Shot} = \text{shotStat} + \text{random}(1, 15)
   $$

   $$
   \text{Reach Save} = \text{reachStat} + \text{random}(1, 15)
   $$

   - Jika $\text{Power Shot} > \text{Reach Save}$, tembakan terlalu keras dan menghasilkan **GOL**.
   - Jika sebaliknya, bola berhasil ditepis (**DITEPIS**).

---

## 🚀 Cara Menjalankan

1. Pastikan Python 3.x telah terinstal di komputer Anda.
2. Simpan skrip kode utama ke dalam file, misalnya `main.py`.
3. Jalankan melalui terminal:
   ```bash
   python main.py
   ```
