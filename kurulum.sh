pip install fastapi
pip install hypercorn

calismaOrtami\Scripts\activate
Çalıştırmak İçin hypercorn main:app --reload

farklı bir ip bind etme
hypercorn main:app --bind 192.168.3.4:5000  --reload
