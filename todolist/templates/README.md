# Tugas 5

## Perbedaan Inline, Internal, dan External CSS serta kelebihan masing-masing (Reference: https://www.hostinger.com/tutorials/difference-between-inline-external-and-internal-css)

### Inline
Style yang diinginkan didefinisikan dalam tag elemen yang diinginkan. Style hanya berlaku dalam tag tersebut.

Keunggulan: Pembuatan cepat dan mudah

### Internal
Menggunakan tag <style> langsung di dalam file .html yang akan ditampilkan. Style yang didefinisikan hanya dapat digunakan dalam file tersebut.

Keunggulan: Tidak perlu membuat file .css baru untuk mendefinisikan sebuah style.

### External
Menggunakan elemen link pada file 'base.html'. Tag <link> diletakkan di dalam tag <head>. Style yang dituju didefinisikan dalam sebuah file .css terpisah.

Keunggulan: Style yang sudah didefinisikan dapat digunakan di banyak file berbeda tanpa perlu menuliskan <link> lagi selama masih di dalam {% block content %}.



## HTML5 Tags (Reference: https://www.w3schools.com/tags/default.asp)

```
'!--...--'      | Bagian '...' untuk menulis comment
'!DOCTYPE ...'  | Bagian '...' untuk tipe dokumen
'a'             | Hyperlink
'body'          | Isi
'br'            | Line-break
'button'        | Tombol, dapat ditekan dan melakukan sesuatu
'col'           | Spesifikasi untuk kolom
'div'           | Section dalam dokumen, paling sering digunakan untuk men-define inline css, terutama ketika menggunakan bootstrap
'footer'        | Elemen yang terkandung dalam tag ini akan muncul di bagian bawah halaman
'form'          | Dapat menerima input user
'h1' to 'h6'    | Heading berbeda ukuran, dengan h1 ukuran terbesar dan h6 ukuran terkecil
'head'          | Yang mengandung metadata; misal digunakan untuk memberi judul halaman, atau setup bootstrap
'header'        | Elemen yang terkandung dalam tag ini akan muncul di bagian atas halaman
'hr'            | Muncul sebagai garis horizontal
'html'          | Definisikan root dokumen
'img'           | Memunculkan gambar (perlu men-define style)
'input'         | Kontrol sebuah input
'label'         | Label untuk 'input'
'li'            | Definisikan list item
'link'          | Menghubungkan dokumen dengan sumber eksternal, misal bootstrap atau style sheet (css terpisah)
'main'          | Konten utama dokumen; optional
'meta'          | Definisikan metadata
'ol'            | List berurutan (1, 2, 3, ...)
'p'             | Paragraf
'script'        | Client-side script; misal untuk aktivasi fungsi tambahan bootstrap yang sengaja dipisah untuk menghemat byte
'section'       | Section dalam dokumen
'span'          | Section dalam dokumen; digunakan untuk styling sebuah text, tidak memiliki align, dan tidak membuat line baru setelahnya
'style'         | Untuk internal styling
'table'         | Membuat area tabel
'tbody'         | Body untuk tabel
'td'            | Isi cell pada tabel
'th'            | Header tabel
'title'         | Judul dokumen (yang akan tertulis sebagai nama tab pada browser)
'ul'            | List tidak berurutan (Bulletin)
```



## CSS Selectors  (Reference: https://www.w3schools.com/css/css_selectors.asp)

### Tag
Didefinisikan langsung dengan nama tag milik HTML5 untuk mengubah elemen-elemen dengan tag tersebut.

misal:
```
h1 {
    background-color: black;
}
```
> akan mengubah apapun dengan tag 'h1' menjadi memiliki background berwarna hitam

### ID
Didefinisikan dengan menggunakan '#' diikuti dengan nama ID.

misal:
```
#bg {
    background-color: blue;
    height: 100vh;
}
```
> akan membuat tag apapun dengan 'id="bg"' memiliki style tersebut.

### Class
Didefinisikan dengan menggunakan '.' diikuti dengan nama class yang diinginkan.

misal:
```
.bg {
    background-color: red;
    height: 100vh;
}
```
> akan membuat tag apapun dengan 'class="bg"' memiliki style tersebut.

## Implementasi Tugas 5

1. Setiap custom styling pada halaman (login, register, dan create-task) ada yang dibuat secara internal dan ada yang secara inline. Untuk memudahkan lebih lanjut, digunakan external css dari bootstrap yang diambil menggunakan <link> pada file [base.html](templates\base.html).
2. Format untuk cards telah disediakan oleh bootstrap. Untuk animasi hover perlu dibuat dalam internal styling menggunakan .card untuk style sebelum dan .card:hover untuk style saat kursor diarahkan ke card.
3. Tiap halaman dibuat responsive terhadap perubahan ukuran window browser dengan menambahkan "-fluid" pada class atau dengan menambahkan "height=100vh".