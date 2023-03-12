# ChronicleTest
 Test for Chronicle

Progress:
[x] Dibuat menggunakan Django versi 3.x.
[x] Database Mysql untuk penyimpanan data
[-] Menggunakan redis untuk caching response.
(configuration is finished, belum diimplementasikan)

Adapun endpoint yang disupport oleh backend adalah sebagai berikut :
[x] Registrasi user baru
[x] Login
[x] Update password
[x] Get list data user (support pagination dan filter by keyword)
[x] Get single data user
[x] Update data user
[x] Hapus data user (soft delete)
[x] Kecuali “Registrasi user baru dan Login”, semua endpoint harus dilindungi menggunakan autentikasi JWT
[x] Field user : email, password, first_name, last_name, sex, date_of_birth, address (untuk last_name dan address bersifat opsional)
[x] Field yang digunakan untuk login adalah email dan password.
[x] Untuk field password disimpan di database setelah dilakukan proses enkripsi (metode enkripsi bebas)
[x] Semua user tidak memiliki role yang berbeda-beda (tidak ada superuser, admin dsb)
[ ] Mendukung swagger untuk dokumentasi api
[x] Menggunakan “rate limit” yang bisa diatur jumlahnya di file environment
[x] Enable CORS

Docker
[x] Compose
[-] Dockerfile

Unit test: 0%
