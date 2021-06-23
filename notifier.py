import ctypes


def windows_pop_up(change):
    opened_slots = change.get("opened")
    closed_slots = change.get("closed")
    if len(opened_slots):
        ctypes.windll.user32.MessageBoxW(0, str(opened_slots), "NEW SLOTS AVAILABLE", 1)
    if len(closed_slots):
        ctypes.windll.user32.MessageBoxW(0, str(closed_slots), "ALL SLOTS GONE", 1)
