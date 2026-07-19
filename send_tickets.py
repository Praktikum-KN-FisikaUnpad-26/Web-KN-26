import smtplib
import os
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Konfigurasi Sender
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Data Pemenang dan File PDF-nya
winners = [
    {
        "name": "Fahri Fadilah",
        "email": "fahri25002@mail.unpad.ac.id",
        "file": "GT/GT_AKN26-FF.pdf"
    },
    {
        "name": "Dede Siti Masriah",
        "email": "dede25002@mail.unpad.ac.id",
        "file": "GT/GT_AKN26-DSM.pdf"
    },
    {
        "name": "Zahy Bahasuan",
        "email": "zahy25001@mail.unpad.ac.id",
        "file": "GT/GT_AKN26-ZB.pdf"
    }
]

def send_golden_tickets():
    print("=== PENGIRIMAN GOLDEN TICKET OTOMATIS ===")
    print("Gunakan akun Gmail kepanitiaan (pastikan sudah membuat App Password)")
    sender_email = input("Email Pengirim: ")
    sender_password = getpass.getpass("App Password: ")
    
    try:
        # Koneksi ke Server SMTP
        print("\nMenghubungkan ke server email...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(sender_email, sender_password)
        print("Login berhasil!\n")
        
        for winner in winners:
            print(f"Mengirim tiket untuk {winner['name']} ({winner['email']})...")
            
            # Cek apakah file PDF ada
            if not os.path.exists(winner['file']):
                print(f"  [ERROR] File {winner['file']} tidak ditemukan! Lewati pengiriman ini.")
                continue
            
            # Setup struktur email
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = winner['email']
            msg['Subject'] = "🏆 PENGUMUMAN GOLDEN TICKET PRAKTIKUM KOMPUTASI NUMERIK 2026"
            
            # Isi teks email
            body = f"""Halo {winner['name']},

Selamat! Kamu terpilih sebagai peraih nilai terbaik dalam Projek Praktikum Komputasi Numerik 2026.

Terlampir Golden Ticket khusus untukmu sebagai bentuk apresiasi kami atas dedikasi dan kerja kerasmu.

Salam hangat,
Asisten Lab Praktikum Komputasi Numerik 2026
"""
            msg.attach(MIMEText(body, 'plain'))
            
            # Attach file PDF
            with open(winner['file'], "rb") as f:
                pdf_attachment = MIMEApplication(f.read(), _subtype="pdf")
                pdf_attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(winner['file']))
                msg.attach(pdf_attachment)
            
            # Kirim email
            server.send_message(msg)
            print("  [SUCCESS] Email terkirim!")
            
        server.quit()
        print("\nSemua tiket berhasil dikirim!")
        
    except Exception as e:
        print(f"\n[GAGAL] Terjadi kesalahan: {e}")
        print("Pastikan email/password benar, dan akun Gmail mengizinkan App Passwords.")

if __name__ == "__main__":
    send_golden_tickets()
