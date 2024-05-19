#with facede
class TV:
    def on(self):
        print("TV is on")

    def off(self):
        print("TV is off")

class DVDPlayer:
    def play(self):
        print("DVD is playing")

    def stop(self):
        print("DVD stopped")

class SoundSystem:
    def set_volume(self, level):
        print(f"Sound level set to {level}")

class HomeTheaterFacade:
    def __init__(self, tv, dvd, sound):
        self.tv = tv
        self.dvd = dvd
        self.sound = sound

    def watch_movie(self):
        self.tv.on()
        self.dvd.play()
        self.sound.set_volume(10)
        print("Movie is playing")

    def end_movie(self):
        self.dvd.stop()
        self.tv.off()
        print("Movie ended")

if __name__ == "__main__":
    tv = TV()
    dvd = DVDPlayer()
    sound = SoundSystem()
    home_theater = HomeTheaterFacade(tv, dvd, sound)

    home_theater.watch_movie()
    home_theater.end_movie()


