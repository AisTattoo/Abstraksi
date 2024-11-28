from abc import ABC, abstractmethod

class Rumah(ABC):

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def bentuk(self):
        pass

    @abstractmethod
    def fasilitas(self):
        pass

    def deskripsi(self):
        return "Ini adalah sebuah rumah."

class Apartemen(Rumah):
    def display(self):
        return f"Alamat apartemen ini adalah: {self.alamat}"

    def bentuk(self):
        return f"Atap apartemen ini adalah: {self.atap}"

    def fasilitas(self):
        return "Apartemen ini memiliki kolam renang dan gym."

class Villa(Rumah):
    def display(self):
        return f"Alamat villa ini adalah: {self.alamat}"

    def bentuk(self):
        return f"Atap villa ini adalah: {self.atap}"

    def fasilitas(self):
        return "Villa ini memiliki taman pribadi dan area BBQ."

# Membuat objek Apartemen
apartemen_jakarta = Apartemen()
apartemen_jakarta.alamat = "Jl. Sudirman No. 10, Jakarta"
apartemen_jakarta.atap = "Coklat"
print(apartemen_jakarta.deskripsi())
print(apartemen_jakarta.display())
print(apartemen_jakarta.bentuk())
print(apartemen_jakarta.fasilitas())

# Membuat objek Villa
villa_bali = Villa()
villa_bali.alamat = "Jl. Diponegoro No. 15, Bali"
villa_bali.atap = "Hitam"
print(villa_bali.deskripsi())
print(villa_bali.display())
print(villa_bali.bentuk())
print(villa_bali.fasilitas())