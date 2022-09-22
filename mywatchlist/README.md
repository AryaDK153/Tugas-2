## Link Herokuapp

[HTML view](https://fistofadventure.herokuapp.com/mywatchlist/html/)

[XML view](https://fistofadventure.herokuapp.com/mywatchlist/xml/)

[JSON view](https://fistofadventure.herokuapp.com/mywatchlist/json/)


## Perbedaan JSON, XML, dan HTML

HTML berisi format untuk tampilan, sedangkan XML dan JSON berisi data yang ingin ditampilkan.

Format XML dan JSON membutuhkan CSS atau Javascript agar dapat muncul di tampilan browser, sedangkan format html bisa langsung muncul di tampilan browser.

File XML lebih besar dari JSON karena format penulisannya. 


## Mengapa data delivery dibutuhkan dalam pengimplementasian sebuah platform?

Data delivery dilakukan agar browser dapat menerima respon dari server sesuai request yang diminta. Misalnya, ketika browser meminta laman HTML, server akan mengembalikan file HTML yang sudah diformat selama pembuatan web. Selain itu, browser juga dapat meminta data dalam bentuk yang diinginkan, misalnya, browser meminta data dalam bentuk JSON, maka server akan mengembalikan data dalam bentuk JSON. 


## Pengimplementasian Tugas-3 : Poin 1-3

1. Buka command prompt, masukkan "python manage.py startapp mywatchlist", tambahkan INSTALLED_APPS di settings.py.

2. Masuk ke folder app yang telah dibuat, buat file baru bernama urls.py, import "path" yang disediakan django untuk membuat path, serta fungsi-fungsi dalam views.py yang akan dibuat, buat list urlpatterns yang akan diakses. Jangan lupa untuk menambahkan urlpattern menuju app yang telah dibuat di project_django/urls.py

3. Buka models.py kemudian buat fungsi dengan parameter models yang dapat diimport dari django, buat variabel-variabel untuk model yang diinginkan, pastikan masing-masing memiliki data-type yang benar, model yang telah dibuat akan dapat dibaca oleh views.py setelah melakukan migration dengan 'python manage.py makemigration', jika belum memiliki folder migration, dan 'python manage.py migrate'. Ini perlu dilakukan agar django dapat mendeteksi perubahan pada models.py.


## Postman URL test
# HTML
![html](https://user-images.githubusercontent.com/112199564/191658476-5b35a49e-06fe-4cd5-807d-aafb30965d3c.png)

# XML
![xml](https://user-images.githubusercontent.com/112199564/191658557-2503c04b-dc5a-4c06-a5dd-33094e863148.png)

# JSON
![json](https://user-images.githubusercontent.com/112199564/191658561-40a074cf-b518-44b5-8cc2-ca60b21a1d7c.png)