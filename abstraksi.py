class Rumah:
    def __init__(self, alamat="", atap=""):
        self.alamat = alamat
        self.atap = atap

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

apartemen_jakarta = Apartemen("Jl. Sudirman No. 10, Jakarta", "Coklat")
print(apartemen_jakarta.deskripsi())
print(apartemen_jakarta.display())
print(apartemen_jakarta.bentuk())
print(apartemen_jakarta.fasilitas())

villa_bali = Villa("Jl. Diponegoro No. 15, Bali", "Hitam")
print(villa_bali.deskripsi())
print(villa_bali.display())
print(villa_bali.bentuk())
print(villa_bali.fasilitas())