#!/usr/bin/env python3
import gi
import psutil
import signal
import os
import time
from PIL import Image, ImageDraw, ImageFont

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7') # Bildirim sistemi için
from gi.repository import Gtk, AppIndicator3, GLib, Notify

class CSTempApp:
    def __init__(self):
        self.app_id = "cstemp_indicator"
        Notify.init(self.app_id) # Bildirim sistemini başlat
        
        self.indicator = AppIndicator3.Indicator.new(
            self.app_id,
            "utilities-system-monitor",
            AppIndicator3.IndicatorCategory.HARDWARE
        )
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        
        menu = Gtk.Menu()
        item_quit = Gtk.MenuItem(label="CSTemp'ten Çık")
        item_quit.connect('activate', Gtk.main_quit)
        menu.append(item_quit)
        menu.show_all()
        self.indicator.set_menu(menu)

        self.last_notify_time = 0 # Sürekli bildirim gitmemesi için zaman kontrolü
        self.update()
        GLib.timeout_add_seconds(1, self.update)

    def create_icon(self, temp):
        img = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 44)
        except:
            font = ImageFont.load_default()
        
        # İstediğin Renk Kademeleri
        if temp >= 68:
            color = (255, 0, 0) # Kırmızı
            self.send_alert(temp) # Kritik sıcaklıkta bildirim gönder
        elif temp >= 50:
            color = (255, 255, 0) # Sarı
        else:
            color = (0, 255, 0) # Yeşil
        
        # Rakam ve Derece simgesi (°)
        text = f"{temp}°"
        draw.text((0, 8), text, font=font, fill=color)
        
        toggle = int(time.time()) % 2
        icon_path = f"/tmp/cstemp_{toggle}.png"
        img.save(icon_path)
        return icon_path

    def send_alert(self, temp):
        # 5 dakikada bir sadece 1 kez bildirim gönder (Rahatsız etmemesi için)
        current_time = time.time()
        if current_time - self.last_notify_time > 300: 
            n = Notify.Notification.new(
                "CSTemp: Yüksek Sıcaklık Uyarısı!",
                f"İşlemci sıcaklığı {temp}°C seviyesine ulaştı. Lütfen fanları kontrol edin.",
                "dialog-warning"
            )
            n.show()
            self.last_notify_time = current_time

    def update(self):
        try:
            temps = psutil.sensors_temperatures()
            if temps:
                sensor_name = list(temps.keys())[0]
                current_temp = int(temps[sensor_name][0].current)
                
                icon_path = self.create_icon(current_temp)
                self.indicator.set_icon_full(icon_path, f"CSTemp: {current_temp}°C")
        except Exception as e:
            print(f"Hata: {e}")
        return True

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = CSTempApp()
    Gtk.main()

