import asyncio
from asyncio import AbstractEventLoop
from threading import Thread
from tkinter_gui import LoadGui

class ThreadedEventLoop(Thread):
    def __init__(self, loop: AbstractEventLoop):
        super().__init__()
        self._loop = loop
        self.daemon = True

    def run(self):
        self._loop.run_forever()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    async_thread = ThreadedEventLoop(loop)
    async_thread.start()

    app = LoadGui(loop)
    app.mainloop()
