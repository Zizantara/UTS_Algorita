class ProgramKasir:
    def __init__(self):
        # Inisialisasi keranjang kosong
        self.keranjang = []
        
    def tambah_barang(self):
        """Fungsi untuk menambah barang ke keranjang"""
        print("\n=== TAMBAH BARANG ===")
        try:
            nama = input("Masukkan nama barang: ")
            harga = int(input("Masukkan harga barang: Rp "))
            jumlah = int(input("Masukkan jumlah barang: "))
            
            # Menambahkan barang ke keranjang
            barang = {
                'nama': nama,
                'harga': harga,
                'jumlah': jumlah,
                'total': harga * jumlah
            }
            self.keranjang.append(barang)
            print("\nBarang berhasil ditambahkan!")
            
        except ValueError:
            print("\nError: Masukkan angka yang valid untuk harga dan jumlah!")
    
    def tampilkan_daftar(self):
        """Fungsi untuk menampilkan daftar barang"""
        if not self.keranjang:
            print("\nKeranjang masih kosong!")
            return
        
        print("\n=== DAFTAR BARANG ===")
        print("No. | Nama Barang | Harga | Jumlah | Total")
        print("-" * 50)
        
        for i, barang in enumerate(self.keranjang, 1):
            print(f"{i:<4}| {barang['nama']:<11} | {barang['harga']:,} | {barang['jumlah']:^6} | Rp {barang['total']:,}")
    
    def hitung_total(self):
        """Fungsi untuk menghitung total harga"""
        total = sum(barang['total'] for barang in self.keranjang)
        print(f"\nTotal Belanja: Rp {total:,}")
        return total
    
    def cetak_struk(self):
        """Fungsi untuk mencetak struk"""
        if not self.keranjang:
            print("\nKeranjang masih kosong!")
            return
            
        print("\n" + "="*40)
        print(f"{'STRUK PEMBELIAN':^40}")
        print("="*40)
        print(f"{'No.':<4}{'Barang':<15}{'Qty':<8}{'Total':>13}")
        print("-"*40)
        
        for i, barang in enumerate(self.keranjang, 1):
            print(f"{i:<4}{barang['nama']:<15}{barang['jumlah']:<8}Rp {barang['total']:>10,}")
        
        print("-"*40)
        total = self.hitung_total()
        print(f"Total Pembayaran: {'Rp ' + str(total):>26,}")
        print("="*40)
        print(f"{'Terima Kasih Atas Kunjungan Anda':^40}")
        print("="*40)

def main():
    kasir = ProgramKasir()
    
    while True:
        print("\n=== PROGRAM KASIR ===")
        print("1. Tambah Barang")
        print("2. Tampilkan Daftar Barang")
        print("3. Hitung Total")
        print("4. Cetak Struk")
        print("5. Keluar")
        
        pilihan = input("\nPilih menu (1-5): ")
        
        if pilihan == '1':
            kasir.tambah_barang()
        elif pilihan == '2':
            kasir.tampilkan_daftar()
        elif pilihan == '3':
            kasir.hitung_total()
        elif pilihan == '4':
            kasir.cetak_struk()
        elif pilihan == '5':
            print("\nTerima kasih telah menggunakan program ini!")
            break
        else:
            print("\nPilihan tidak valid! Silakan pilih menu 1-5.")
            
if __name__ == "__main__":
    main()