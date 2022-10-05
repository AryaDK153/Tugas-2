## Perbedaan Inline, Internal, dan External CSS serta kelebihan masing-masing

### Inline
Style yang diinginkan didefinisikan dalam tag elemen yang diinginkan. Style hanya berlaku dalam tag tersebut.

Keunggulan: Pembuatan cepat dan mudah

### Internal
Menggunakan tag <style> langsung di dalam file .html yang akan ditampilkan. Style yang didefinisikan hanya dapat digunakan dalam file tersebut.

Keunggulan: Tidak perlu membuat file .css baru untuk mendefinisikan sebuah style.

### External
Menggunakan elemen link pada file 'base.html'. Tag <link> diletakkan di dalam tag <head>. Style yang dituju didefinisikan dalam sebuah file .css terpisah.

Keunggulan: Style yang sudah didefinisikan dapat digunakan di banyak file berbeda tanpa perlu menuliskan <link> lagi selama masih di dalam {% block content %}.

## HTML5 Tags

## CSS Selectors

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