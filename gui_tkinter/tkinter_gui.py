from queue import Queue
from tkinter import Tk, Label, Entry, ttk
from typing import Optional
from load_scenario import StressTest

class LoadGui(Tk):
    def __init__(self, loop, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self._loop = loop
        self._queue = Queue()
        self._refresh_ms :int = 25
        self._load_test : Optional[StressTest] = None

        self.title("URL Requester")

        self._url_label = Label(self, text="URL:")
        self._url_label.grid(row=0, column=0)

        self._url_field = Entry(self, width=10)
        self._url_field.grid(row=0, column=1)

        self._request_label = Label(self, text="Number of requests:")
        self._request_label.grid(row=1, column=0)

        self._request_field = Entry(self, width=10)
        self._request_field.grid(row=1, column=1)

        self._submit = ttk.Button(self, text="Submit", command=self._start)
        self._submit.grid(row=1, column=2)

        self.pb_label = Label(self, text="Progress:")
        self.pb_label.grid(row=3, column=0)

        self.pb = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")
        self.pb.grid(row=3, column=1, columnspan=2)

    def _update_bar(self, percent: int):
        if percent == 100:
            self._load_test = None
            self._submit['text'] = 'Submit'
        else:
            self.pb['value'] = percent
            self.after(self._refresh_ms, self._poll_queue)


    def _queue_update(self, completed_requests: int, total_requests: int):
        self._queue.put(int(completed_requests) / total_requests * 100)

    def _poll_queue(self):
        if not self._queue.empty():
            percent_complete = self._queue.get()
            self._update_bar(percent_complete)
        else:
            if self._load_test:
                self.after(self._refresh_ms, self._poll_queue)

    def _start(self):
        if self._load_test is None:
            self._submit['text'] = 'Cancel'
            self._load_test = StressTest(self._loop,
                                         self._url_field.get(),
                                         int(self._request_field.get()),
                                         self._queue_update)
            self.after(self._refresh_ms, self._poll_queue)
            self._load_test.start()
        else:
            self._load_test.cancel()
            self._load_test = None
            self._submit['text'] = 'Submit'