import math
import argparse
import sys

# Renkler
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def calculate_entropy(data):
    """
    Shannon Entropisi hesaplar.
    Sonuç 0 ile 8 arasındadır.
    0: Tamamen düzenli (Hepsi aynı byte)
    8: Tamamen rastgele (Şifrelenmiş veya Sıkıştırılmış)
    """
    if not data:
        return 0
    
    entropy = 0
    # Her byte değerinin (0-255) frekansını hesapla
    for x in range(256):
        p_x = float(data.count(bytes([x]))) / len(data)
        if p_x > 0:
            entropy += - p_x * math.log(p_x, 2)
            
    return entropy

def scan_file(filepath):
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
            
        entropy = calculate_entropy(data)
        
        print(f"Dosya: {filepath}")
        print(f"Entropi Değeri: {entropy:.4f}")
        
        # Analiz Kararı
        # Genellikle 7.0'ın üzeri şüpheli (paketlenmiş/şifreli) kabul edilir.
        # Normal metin veya kod genellikle 4.0 - 6.0 arasındadır.
        if entropy > 7.2:
            print(f"{RED}[!] KRİTİK: Yüksek Entropi! Dosya paketlenmiş veya şifrelenmiş olabilir.{RESET}")
        elif entropy > 6.5:
             print(f"{YELLOW}[!] UYARI: Orta-Yüksek Entropi. Şüpheli olabilir.{RESET}")
        else:
            print(f"{GREEN}[+] TEMİZ: Düşük Entropi. Standart dosya yapısı.{RESET}")
            
    except Exception as e:
        print(f"Hata: {e}")

def main():
    parser = argparse.ArgumentParser(description="File Entropy Scanner for Malware Analysis")
    parser.add_argument("file", help="Analiz edilecek dosya yolu")
    args = parser.parse_args()
    
    scan_file(args.file)

if __name__ == "__main__":
    main()
