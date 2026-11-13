# ai-tugas5-F1D02410111
Nama: Dita Ayu Julita
NIM: F1D02410111
Topik: Sistem Pakar Identifikasi Penyebab Masalah Pengisian Daya Baterai Laptop

Cara menjalankan program:
Bahasa Pemrograman: Python dengan Python 3.14.4
Memastikan python telah terpasang dan file main.py (file program) dengan kb_laptop (pengetahuan) ada di folder yang sama. Lalu run file main.py, dan user dapat memasukkan jawaban

Daftar Sumber:
S1. Dell Support
Judul: How to Troubleshoot AC Adapter Issues on a Dell Laptop
URL: https://www.dell.com/support/kbdoc/en-us/000125125/how-to-troubleshoot-ac-adapter-issues

S2. Microsoft Support
Judul: Use Smart charging in Windows
URL: https://support.microsoft.com/en-us/windows/experience/power-battery/use-smart-charging-in-windows

Aturan (Kondisi IF, Kesimpulan THEN, sumber)
R1 (Kabel atau adaptor mengalami kerusakan fisik, Indikasi masalah adaptor, S1)
R2 (BIOS menunjukkan adaptor Unknown atau daya adaptor tidak sesuai, Indikasi masalah adaptor, S1)
R3 (Indikasi masalah adaptor DAN laptop tidak mengisi daya, C1: Kemungkinan masalah adaptor atau kabel, S1)
R4 (Port atau sambungan pengisian daya terindikasi bermasalah, C2: Kemungkinan masalah port atau sambungan, S1)
R5 (Windows tidak mengenali adaptor meskipun sudah terhubung, C3: Kemungkinan masalah suplai daya, sambungan, atau rangkaian pengisian, S1)
R6 (Pengisian dibatasi oleh pengaturan BIOS atau Smart Charging, C4: Pengisian daya dibatasi oleh pengaturan, (S1, S2))
R7 (Kesehatan baterai menunjukkan Fair/Poor atau diagnostik berulang kali menunjukkan kesalahan, C5: Kemungkinan kesehatan baterai menurun, S1)

Metode yang dipilih: 
Metode yang digunakan adalah Forward Chaining, memulai proses penalaran dari fakta awal yang diberikan oleh user, lalu mencocokkan dengan aturan IF-THEN untuk menghasilkan fakta baru atau kesimpulan.

Tiga kasus uji dan screenshot:
![kasus1](screenshot/kasus1.png)
Pada kasus 1, user memberikan fakta bahwa kabel atau adaptor terlihat mengalami kerusakan fisik dan laptop sama sekali mengisi daya, sementara kondisi lain dijawab tidak. Berdasarkan fakta tersebut, aturan R1 terpenuhi dan menghasilkan indikasi masalah adaptor, kemudian R3 terpenuhi karna indikasi masalah adaptor dan tidak mengisi. Sistem memberikan kesimpulan C1, kemungkinan masalah pada adaptor atau kabel pengisi daya.

![kasus2](screenshot/kasus2.png)
Pada kasus 2, user memberikan fakta bahwa sambungan adaptor ke port laptop tidak stabil atau port pengisian daya terindikasi bermasalah, sementara kondisi lain dijawab tidak. Berdasarkan fakta tersebut, aturan R4 terpenuhi sehingga sistem memberikan kesimpulan C2, kemungkinan masalah pada port atau sambungan pengisian daya

![kasus3](screenshot/kasus3.png)
Pada kasus 3, user menjawab semua pertanyaan dengan tidak. Berdasarkan fakta tersebut tidak ada aturan yang terpenuhi sehingga sistem tidak menghasilkan kesimpulan.

Batas keberlakuan:
Batas pengetahuan sistem ini berdasarkan informasi dari Dell Support dan Microsoft Support. Identifikasi ditujukan sebagai panduan awal untuk kemungkinan masalah pengisian daya laptop seperti masalah adaptor, kabel, port pengaturan pengisian daya dan kondisi baterai. Hasil sistem merupakan saran berdasarkan fakta yang dimasukkan user, bukan diagnosis akhir.

Penggunaan alat bantu:
Menggunakan alat bantu AI untuk melakukan brainstorming dan untuk memahami konsep dari Forward Chaining untuk merancang aturan IF-THEN