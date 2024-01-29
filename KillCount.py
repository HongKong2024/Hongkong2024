# make a class to hold the kill count


class KillCount:
    def __init__(self):
        self.kill_count = 0

    def increment(self):
        self.kill_count += 1

    def get_kill_count(self):
        return self.kill_count


kill_count = KillCount()
