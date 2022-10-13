## Perbedaan antara asynchronous programming dengan synchronous programming.

Seperti namanya, 'asynchronous programming' berarti ketika dijalankan, kode program dapat berjalan secara asinkronus atau paralel dengan kode lain yang sedang dijalankan. Asynchronous programming pada pemrograman web memungkinkan program melakukan request dan memunculkan hasilnya tanpa harus melakukan refresh pada seluruh halaman web. Berbeda dengan synchronous programming, di mana halaman web perlu direfresh terlebih dahulu agar response baru dapat dimunculkan.

## Event-Driven Programming

Yaitu semacam trigger perubahan pada halaman web yang mana biasanya berupa interaksi dari user. Trigger tersebut dapat berupa document 'ready', button 'onclick', cursor 'hover', keyboard 'keyup', dan lain sebagainya. Misalnya ketika ingin menambahkan data pada todolist di tugas kali ini, digunakan `document.getElementById("submit_button").onclick` sebagai trigger ketika user ingin menyimpan isi form.

## Jelaskan penerapan asynchronous programming pada AJAX.

AJAX diterapkan sama seperti penerapan view html biasa, namun request dan responsenya dilakukan secara paralel dengan halaman web. Salah satu caranya adalah menggunakan javascript. Javascript memberi kemudahan bagi programmer untuk melakukan fetch() terhadap data yang ingin di-load, lalu, baik secara mandiri maupun event-triggered, menampilkan data tersebut dalam format html dengan `document.getElementBy<selector>('<selector-name>').innerHTML` yang mengarah ke dokumen (web page yang sedang dibuka).

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Membuat modal, yang mana dapat ditemukan pada website [Bootstrap](https://getbootstrap.com/docs/5.2/components/modal/)

2. Menyalin form yang digunakan pada [new_task.html](templates/new_task.html) ke dalam modal-body dalam [todolist.html](templates/todolist.html), juga mematikan link menuju new_task.html untuk tugas kali ini. Dilakukan karena yang perlu diimplementasikan adalah asynchronous programming atau AJAX.

3. Membuat views baru yang dapat menerima request POST dari modal. Fungsi ini akan menyimpan data dari POST yang diterima serta mengembalikan HTTP Response daripada melakukan redirect.

4. Dalam file [todolist.html](templates/todolist.html), menuliskan javascript menggunakan tag `<script>` di mana fungsi-fungsi asinkronus akan diimplementasikan. Terdapat fungsi, yang dengan trigger berupa button 'onclick', akan menerima request POST dari form dalam modal yang telah dibuat yang kemudian mengaktifkan fungsi yang akan merefresh deretan 'cards' berisi task-task yang telah dibuat. Perlu diketahui bahwa data yang diambil untuk cards adalah data berformat JSON, yang mana dalam file [views.py](views.py) telah diproses oleh fungsi bernama `todolist_json`.

5. Fungsi-fungsi dalam views.py dicantumkan dalam urlpatterns dalam file [urls.py](urls.py) sehingga dapat dipanggil melalui link dalam file html.