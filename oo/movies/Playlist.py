class Playlist:

    def __init__(self, name, programs):
        self._name = name
        self._programs = programs

    @property
    def programs(self):
        return self._programs

    def __len__(self):
        return len(self._programs)

    def add_program(self, program):
        self._programs.append(program)

    def __getitem__(self, item):
        return self._programs[item]


# __ methods represent data models methods
