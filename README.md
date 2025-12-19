cat <<EOF > README.md
# CSTemp - CPU Temperature Monitor for Linux Mint

[TR] Linux Mint (Cinnamon) için geliştirilmiş, sistem çekmecesinden (tray) anlık CPU sıcaklığını renkli rakamlarla takip etmenizi sağlayan hafif bir araçtır.

## Özellikler
* **Akıllı Renkler:** 50°C altı Yeşil, 50-68°C arası Sarı, 68°C üstü Kırmızı.
* **Uyarı Bildirimi:** Sıcaklık 68°C'yi geçtiğinde masaüstü uyarısı gönderir.
* **Menü Desteği:** Sistem menüsünden başlatılabilir.

## Kurulum
Şu anlık sadece kaynak koddan veya .deb paketinden kurulabilir.

\`\`\`bash
python3 cstemp.py
\`\`\`
EOF

git add README.md
git commit -m "README eklendi"
git push origin main
