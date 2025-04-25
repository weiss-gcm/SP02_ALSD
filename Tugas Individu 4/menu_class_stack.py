from class_stack import Stack

def menu_stack():
    s = Stack()
    while True:
        print("\n=== Menu Stack ===")
        print("1. Push Objek")
        print("2. Pop Objek")
        print("3. Cek Empty")
        print("4. Tampil Objek Terakhir")
        print("5. Panjang Dari Stack")
        print("0. Kembali ke Menu Utama")

        try:
            pilihan = int(input("Pilihan: "))
        except ValueError:
            print("Menu diluar jangkauan, tidak ada di daftar")
            continue

        if pilihan == 1:
            obj = input("Objek yang di push: ")
            s.Push(obj)
            print(f"Objek '{obj}' sudah ditambahkan ke stack.")
        elif pilihan == 2:
            print(f"Objek '{s.Pop()}' sudah dihapus dari stack.")
        elif pilihan == 3:
            print("Stack kosong, di isi terlebih dahulu", s.isEmpty())
        elif pilihan == 4:
            print("Objek terakhir pada stack:", s.Peek())
        elif pilihan == 5:
            print("Panjang stack:", s.Size())
        elif pilihan == 0:
            break
        else:
            print("Menu diluar jangkauan, tidak ada di daftar.")