from auto_battle import auto_battle
import win32gui

auto_b = auto_battle()

# ウィンドウの大きさ設定↓
# target_window = win32gui.FindWindow(None,'SOV41')
# target_window_rect = win32gui.GetWindowRect(target_window)
# print('left={}, top={} right={} , bottom={}'.format(target_window_rect[0],target_window_rect[1],target_window_rect[2],target_window_rect[3]))
# print(target_window)
# win32gui.MoveWindow(target_window,0, 0,2520,1080,True)

# 位置設定
# auto_b.regist_click_posission()

# 保存した設定を読み込む
auto_b.read_option()

# 設定した内容を保存する
# auto_b.save_file()

# 現在の設定でバトルをスタートする
# auto_b.run_battle()

# バトル終了後にフレンドを選択する
auto_b.run_select_friend()
