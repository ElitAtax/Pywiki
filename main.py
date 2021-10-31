#Wikipedia in only 10 lines realised


import ctypes
import wikipedia as wiki 
word = input()
info = wiki.summary(word)
ctypes.windll.user32.MessageBoxW(
    0, info[:400], word,
)
