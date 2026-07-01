import os
import time
import threading
import platform


class Alarm:

    def __init__(self):

        self.cooldown = 5          # seconds

        self.last_alarm = 0

        self.running = False

        self.sound_file = "assets/alarm.wav"

    def _play(self):

        system = platform.system()

        try:

            # -------------------------
            # Windows
            # -------------------------

            if system == "Windows":

                import winsound

                if os.path.exists(self.sound_file):

                    winsound.PlaySound(
                        self.sound_file,
                        winsound.SND_FILENAME
                    )

                else:

                    winsound.Beep(1500, 700)

            # -------------------------
            # Linux
            # -------------------------

            else:

                if os.path.exists(self.sound_file):

                    os.system(
                        f'aplay "{self.sound_file}" >/dev/null 2>&1'
                    )

                else:

                    print("\a", end="", flush=True)

        except Exception as e:

            print("Alarm Error:", e)

        self.running = False

    def trigger(self, reason):

        current = time.time()

        if current - self.last_alarm < self.cooldown:
            return

        if self.running:
            return

        self.last_alarm = current

        self.running = True

        print("\n" + "=" * 60)
        print("🚨 SAFE DRIVE AI ALERT")
        print("=" * 60)
        print("Reason :", reason)
        print("=" * 60)

        threading.Thread(
            target=self._play,
            daemon=True
        ).start()
