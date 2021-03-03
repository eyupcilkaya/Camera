# RemotlyControlDevices

Bu proje 3D Printer'ı raspberry pi aracılığı ile uzaktan kontrol etmek için yapılmıştır.
Proje firebase platformu ile bağlı olup alınan veriler bir mobil uygulama tarafından işlenmiştir. 

Proje 3 kısımdan oluşmaktadır:
  1. Raspberry pi kamera modulü ile yazıcının canlı olarak görüntüleri alınmıştır.
  2. Yazıcıyı açmak ve kapatmak için raspberry pi ile bir röle bağlantısı yapılmıştır.
  3. Yazıcının sıcaklık bilgilerini almak ve süreci takip etmek için seri bağlantı yapılmıştır.

Kameradan alınan görüntüler anlık olarak firebase storage a kayıt edilmektedir. 
Yazıcı açmak ve kapatmak için firebase realtime database de bir bölüm oluşturulmuş ve raspberry pi oradan gelecek değere göre cihazı role yardımı ile açıp kapatmaktadır. Burada atanacak değer mobil cihazdan gönderilmektedir. Yazıcının sıcaklık değerlerini ve süreç bilgilerini almak için ise usb bağlantısı ile raspberry pi ve yazıcı arasında seri haberleşme gerçekleştirilmiştir. 

Projeyi çalıştırmak için öncelikle bir firebase projesi oluşturmanız gerekmektedir. Sonrasında size verilen json dosyayı indirip projenin bulunduğu konuma yerleştirmeniz gerekmektedir. 
Proje de printer_values.py kısmında bağlayacağınız port numarasını güncelleyin.
En son olarak main.py I çalıştırmanız yeterli olacaktır.
  
