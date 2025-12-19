# 🌡️ CSTemp - CPU Temperature Monitor for Linux Mint

[TR] Linux Mint (Cinnamon) için geliştirilmiş, sistem çekmecesinden (tray) anlık CPU sıcaklığını renkli bir sayı olarak gösteren hafif ve kullanışlı bir araçtır.

[EN] A lightweight tool for Linux Mint (Cinnamon) that displays real-time CPU temperature as a colored number in the system tray.

---

## ✨ Özellikler / Features

* **📊 Anlık Takip:** İşlemci sıcaklığını her 2 saniyede bir günceller.
* **🎨 Akıllı Renkler:** * **50°C altı:** Yeşil (Normal)
    * **50-70°C arası:** Sarı (Uyarı)
    * **70°C üstü:** Kırmızı (Yüksek Sıcaklık)
* **🚀 Düşük Kaynak Tüketimi:** Sistemi yormadan arka planda çalışır.
* **📦 Kolay Kurulum:** `.deb` paketi desteği ile saniyeler içinde kurulur.

---

## 🛠️ Kurulum / Installation

### 1. Gereksinimleri Yükleyin (Requirements)
Uygulamanın çalışması için gerekli kütüphaneleri terminale şu komutu yazarak yükleyin:
```bash
sudo apt update && sudo apt install python3-tk python3-pil python3-psutil gir1.2-appindicator3-0.1
