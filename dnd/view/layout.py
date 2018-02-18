import curses


class Layout(object):
    def __init__(self):
        super(Layout, self).__init__()
        self._std_screen = None

    def __enter__(self):
        self._std_screen = curses.initscr()
        return self

    def __exit__(self, etype, evalue, traceback):
        curses.endwin()
