# RemotlyControlDevices

This project was made to control the 3D Printer remotely via raspberry pi. 
The project is connected with the firebase platform and the data received has been processed by a mobile application.

The project consists of 3 parts:
  1. Live images of the printer were taken with the Raspberry pi camera module.
  2. A relay connection is made with raspberry pi to turn the printer on and off.
  3. Serial connection has been made to get the temperature information of the printer and to follow the process.
  
The images taken from the camera are instantly recorded in firebase storage.
A section has been created in the firebase realtime database to turn the printer on and off, and raspberry pi turns the device on and off with the help of a relay, according to the value that will come from there. The value to be assigned here is sent from the mobile device. In order to obtain the temperature values ​​and process information of the printer, serial communication was realized between raspberry pi and the printer via usb connection.

To run the project, you must first create a firebase project. Then you need to download the given json file and place it in the location of the project.
Update the port number that you will connect in the printer_values.py section of the project.
Finally, it will be enough to run main.py.

### TR

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
