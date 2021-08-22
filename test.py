from auto_battle import auto_battle
import pyautogui

auto_b = auto_battle()
# auto_b.regist_click_posission()
auto_b.read_option()
# auto_b.save_file()
auto_b.run_battle()

# print(pyautogui.locateOnScreen('./read_image/battle_exp.png',confidence=0.9))
# print(pyautogui.locateOnScreen('./read_image/battle_kizuna.png',confidence=0.9))
# print(pyautogui.locateOnScreen('./read_image/master.png',confidence=0.9))
# print(pyautogui.locateOnScreen('./read_image/next_battle.png',confidence=0.9))
# print(pyautogui.locateOnScreen('./read_image/next_button.png',confidence=0.9))

# pyautogui.click()