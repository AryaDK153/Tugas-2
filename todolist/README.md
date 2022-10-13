## Link Herokuapp

[README Tugas 5](templates/README.md)

[README Tugas 6](README-TWO.md)

[Todolist Lobby](https://gingerharbinger.herokuapp.com/todolist)

akun dummy:
1. espotong (limaribuan)
2. dk (yorunikakeru)

## Kegunaan {% csrf_token %}

Agar data yang disimpan di app tidak mudah terkena serangan "cross site request forgery" dari user

## Membuat form secara manual, serta alur data dari submisi

Membuat form secara manual tanpa bantuan form.as_table dapat dilakukan dengan menuliskan input input yang diinginkan di views, mengirimkan request tipe POST melalui file html, dan melakukan <model-name>.objects.create(<model>, ...) pada views.py. lakukan render ketika return, agar data yang telah didapatkan dapat diperlihatkan melalui file html.

## Pengimplementasian Tugas-4

1. Preparasi pembuatan aplikasi hingga setting url mirip dengan tugas-tugas sebelumnya.

2. Registrasi menggunakan UserCreationForm yang telah disediakan django. Login dibuat wajib dengan menambahkan @login_required sebelum halaman utama, login akan membuat cookie yang berfungsi agar user memiliki session yang akan memberinya akses ke halaman utama. Logout menghapus cookie yang dibuat ketika login agar mengakhiri session.

3. Membuat task baru dengan mengarahkan user ke url 'new_task', dimana form disediakan secara semi-manual. Dilakukan agar task baru secara otomatis dibuat untuk pengguna yang logged-in.