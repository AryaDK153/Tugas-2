## Link Aplikasi Tugas 2:
Tugas 2: [Katalog](https://gingerharbinger.herokuapp.com/katalog/)


## Bagan Django
![bagan-django](https://user-images.githubusercontent.com/112199564/190310797-d0bc2e0c-89e2-4a9d-805c-94cf53793766.png)

> Melalui bagan di atas dapat diketahui bahwa setiap request dari client akan pertama kali diproses
> oleh 'urls.py' yang berisi alamat dan fungsi yang akan dieksekusi setiap alamat. Selanjutnya, fungsi
> pada 'views.py' akan melakukan pemrosesan yaitu pengambilan data dari model, menyajikan data kepada
> file html template, hingga mengirimkan HTTP Response ke client.


## Kenapa menggunakan virtual environmment?
```
Tentu, suatu project Django **dapat tetap dijalankan tanpa menggunakan virtual environment**.
Namun, hal ini memungkinkan tumpang tindih ketika ada lebih dari satu project Django yang
dibuat. Dengan kata lain, virtual environment berfungsi sebagai **sekat atau pemisah** antara
dua project yang berbeda.
```

## Implementasi Langkah Pembuatan "Katalog" App
1. Dalam file **views.py**, cukup import fungsi **render** yang telah disediakan oleh django
   serta **kelas model** dari file models.py yang ingin kita ambil datanya. Kemudian, buat fungsi
   dengan parameter request yang berisikan **context dictionary**. Gunakan fungsi **objects.all()**
   untuk mengubah kelas model ke dalam bentuk query dan memasukkannya ke dalam context.
   Terakhir, gunakan fungsi **render** saat melakukan **return** dengan parameter **request**,
   **nama file html** yang dituju, serta **context dictionary** yang telah dibuat.
2. Setelah selesai mengimplementasikan views.py, kita dapat melakukan routing menggunakan
   file **urls.py**. Import **path** milik django serta **fungsi** yang telah dibuat dalam file views.py.
   Kemudian, buat suatu variable bernama **app_name** berisikan **nama aplikasi** yang ingin dibuat,
   serta sebuah list bernama **urlpatterns** berisikan fungsi **path** dengan tiga parameter, yaitu
   **string rute** yang dapat dikosongkan saja, **fungsi milik views.py** yang telah diimpor, serta
   **nama fungsi** view yang telah diimpor (boleh sama dengan parameter ke dua dengan syntax
   ***"name='[nama fungsi]'"*** tanpa kurung siku dan petik dua).
3. Pemetaan pada file html dilakukan dengan meletakkan syntax ***"{{[nama variabel]}}"*** (tanpa
   kurung siku dan petik dua) di tempat yang diinginkan. Nama variabel yang dimaksud di sini
   **sesuai** dengan apa yang ada pada file **models.py**. Sisanya akan dikerjakan oleh fungsi
   render yang terdapat pada fungsi berparameter request pada file views.py.
4. Sebelum mendeploy ke heroku, pastikan sudah membuat akun heroku serta menambahkan aplikasi
   baru di laman [heroku](https://dashboard.heroku.com/). Pergi ke account settings > API Key, dan copy API Key tersebut.
   Kemudian, add, commit, push repositori project django yang ingin di-deploy ke github. Pergi ke github
   dan buka repositori, buka tab settings > secrets > actions dan buat 2 secret baru dengan nama dan variable
   berikut:

   > nama: HEROKU_API_KEY; variabel: [api key yang telah dicopy] (tanpa kurung siku)
   > nama: HEROKU_APP_NAME; variabel: [nama aplikasi yang terdaftar di heroku] (tanpa kurung siku)

   Kemudian, pergi ke tab action, tekan tombol deployment dan tunggu hingga proses selesai.
   Aplikasi yang telah dibuat dapat dilihat di link [nama aplikasi].herokuapp.com/ (tanpa kurung siku).