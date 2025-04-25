from class_queue import Queue

def menu_queue():
    q = Queue()
    while True:
        print("\n=== Menu Queue ===")
        print("1. Enqueue Object")
        print("2. Dequeue Object")
        print("3. Cek Empty")
        print("4. Tampil Objek Pertama")
        print("5. Panjang Dari Queue")
        print("0. Kembali ke Menu Utama")

        try:
            pilihan = int(input("Pilihan: "))
        except ValueError:
            print("Menu diluar jangkauan, tidak ada di daftar")
            continue

        if pilihan == 1:
            obj = input("Objek yang di enqueue: ")
            q.Enqueue(obj)
            print(f"Objek '{obj}' sudah ditambahkan ke queue.")
        elif pilihan == 2:
            print(f"Objek '{q.Dequeue()}' sudah dihapus dari queue.")
        elif pilihan == 3:
            print("Queue kosong, di isi terlebih dahulu", q.isEmpty())
        elif pilihan == 4:
            print("Objek pertama queue:", q.Peek())
        elif pilihan == 5:
            print("Panjang queue:", q.Size())
        elif pilihan == 0:
            break
        else:
            print("Menu diluar jangkauan, tidak ada di daftar")