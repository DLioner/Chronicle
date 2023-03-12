# Progress:

1. [x] Dibuat menggunakan Django versi 3.x.
1. [x] Database Mysql untuk penyimpanan data
1. [ ] Menggunakan redis untuk caching response.
(configuration is finished, belum diimplementasikan)

### Adapun endpoint yang disupport oleh backend adalah sebagai berikut :
1. [x] Registrasi user baru
1. [x] Login
1. [x] Update password
1. [x] Get list data user (support pagination dan filter by keyword)
1. [x] Get single data user
1. [x] Update data user
1. [x] Hapus data user (soft delete)

1. [x] Kecuali “Registrasi user baru dan Login”, semua endpoint harus dilindungi menggunakan autentikasi JWT
1. [x] Field user : email, password, first_name, last_name, sex, date_of_birth, address (untuk last_name dan address bersifat opsional)
1. [x] Field yang digunakan untuk login adalah email dan password.
1. [x] Untuk field password disimpan di database setelah dilakukan proses enkripsi (metode enkripsi bebas)
1. [x] Semua user tidak memiliki role yang berbeda-beda (tidak ada superuser, admin dsb)
1. [ ] Mendukung swagger untuk dokumentasi api
1. [x] Menggunakan “rate limit” yang bisa diatur jumlahnya di file environment
1. [x] Enable CORS

### Docker
1. [x] Compose
1. [ ] Dockerfile

### Unit test: 0%
