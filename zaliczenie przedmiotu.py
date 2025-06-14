import os
import json
from datetime import datetime


class ZdalneRepozytorium:
    def __init__(self, nazwa="MojeRepo"):
        self.nazwa = nazwa
        self.pliki = []
        self.sciezka = f"{nazwa}_repo.json"
        self.wczytaj_repo()

    def dodaj_plik(self, nazwa_pliku):
        """Dodaje plik do repozytorium"""
        if nazwa_pliku not in self.pliki:
            self.pliki.append(nazwa_pliku)
            print(f"✅ Dodano plik: {nazwa_pliku}")
            self.zapisz_repo()
        else:
            print(f"❌ Plik {nazwa_pliku} już istnieje!")

    def usun_plik(self, nazwa_pliku):
        """Usuwa plik z repozytorium"""
        if nazwa_pliku in self.pliki:
            self.pliki.remove(nazwa_pliku)
            print(f"🗑️ Usunięto plik: {nazwa_pliku}")
            self.zapisz_repo()
        else:
            print(f"❌ Plik {nazwa_pliku} nie istnieje!")

    def pokaz_pliki(self):
        """Wyświetla wszystkie pliki w repozytorium"""
        print(f"\n📁 Repozytorium: {self.nazwa}")
        print("-" * 30)
        if self.pliki:
            for i, plik in enumerate(self.pliki, 1):
                print(f"{i}. 📄 {plik}")
        else:
            print("Brak plików w repozytorium")
        print("-" * 30)

    def synchronizuj(self):
        """Synchronizuje repozytorium"""
        print("🔄 Synchronizowanie...")
        print("✅ Repozytorium zsynchronizowane!")
        self.zapisz_repo()

    def udostepnij(self):
        """Generuje link do udostępnienia"""
        link = f"https://github.com/user/{self.nazwa.lower()}"
        print(f"🔗 Link do repozytorium: {link}")
        return link

    def zapisz_repo(self):
        """Zapisuje stan repozytorium do pliku"""
        dane = {
            "nazwa": self.nazwa,
            "pliki": self.pliki,
            "ostatnia_aktualizacja": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        with open(self.sciezka, 'w', encoding='utf-8') as f:
            json.dump(dane, f, ensure_ascii=False, indent=2)

    def wczytaj_repo(self):
        """Wczytuje stan repozytorium z pliku"""
        if os.path.exists(self.sciezka):
            try:
                with open(self.sciezka, 'r', encoding='utf-8') as f:
                    dane = json.load(f)
                    self.pliki = dane.get("pliki", [])
                    print(f"📂 Wczytano repozytorium: {self.nazwa}")
            except:
                print("⚠️ Błąd wczytywania, tworzę nowe repozytorium")


def main():
    print("🚀 Witaj w Zdalnym Repozytorium!")

    # Tworzenie repozytorium
    repo = ZdalneRepozytorium("MojProjekt")

    while True:
        print("\n📋 Menu:")
        print("1. Dodaj plik")
        print("2. Usuń plik")
        print("3. Pokaż pliki")
        print("4. Synchronizuj")
        print("5. Udostępnij")
        print("6. Wyjście")

        wybor = input("\nWybierz opcję (1-6): ").strip()

        if wybor == "1":
            nazwa = input("Nazwa pliku: ").strip()
            if nazwa:
                repo.dodaj_plik(nazwa)

        elif wybor == "2":
            repo.pokaz_pliki()
            nazwa = input("Nazwa pliku do usunięcia: ").strip()
            if nazwa:
                repo.usun_plik(nazwa)

        elif wybor == "3":
            repo.pokaz_pliki()

        elif wybor == "4":
            repo.synchronizuj()

        elif wybor == "5":
            repo.udostepnij()

        elif wybor == "6":
            print("👋 Do widzenia!")
            break

        else:
            print("❌ Nieprawidłowy wybór!")


if __name__ == "__main__":
    main()