import time
import json
import pyautogui
from pyscreeze import locateOnScreen
import win32gui

class auto_battle:

    # コンストラクタ
    def __init__(self):
        # 設定内容
        self.option = []

        # バトル中の画像
        self.check_master_path = './read_image/battle/master.png'

        # リザルト中の画像
        # 連続出撃の画像
        self.check_next_battle_path = './read_image/result/next_battle.png'
        # 次への画像
        self.check_next_button_path = './read_image/result/next_button.png'

        # フレンド検索の画像
        self.check_battle_start = './read_image/friend_search/battle_start.png'
        self.check_select_friend = './read_image/friend_search/select_friend.png'
        self.check_yes_button = './read_image/friend_search/yes_button.png'
        self.check_list_update_button = './read_image/friend_search/friend_list_update.png'

        # 獲得EXPの画像
        self.check_exp_path = './read_image/battle_exp.png'
        # 獲得絆の画像
        self.check_kizuna_path = './read_image/battle_kizuna.png'
    
    # 位置情報を設定する
    def regist_config(self):
        with open('./posision/save_template.json','r') as f:
            save_string = f.read()
        save_json = json.loads(save_string)
        # 対象のウィンドウの位置取得
        print("対象のウィンドウの位置を座標します")
        window_name = input('対象のウィンドウ名を入力してください:')
        target_window = win32gui.FindWindow(None, window_name)
        if(target_window != 0):
            locate_obj = win32gui.GetWindowRect(target_window)
            save_json['window_name'] = window_name
            save_json['window_pos']['left'] = locate_obj[0]
            save_json['window_pos']['top'] = locate_obj[1]
            save_json['window_pos']['right'] = locate_obj[2]
            save_json['window_pos']['bottom'] = locate_obj[3]
            print("ウィンドウの座標を取得できました")
        else:
            print("ウィンドウの座標を取得できませんでした")
            return
        
        # バトル画面の設定
        # アタックカードの設定
        print('Attackの設定')
        input('Attackの位置設定(aを入力してEnterで登録):')
        locate_obj = pyautogui.position()
        save_json['battle']['attack'] = {'x':locate_obj.x,'y':locate_obj.y}
        for i in range(5):
            input('カード{}枚目の位置'.format(i+1))
            locate_obj = pyautogui.position()
            save_json['battle']['attack_card'].append({'x':locate_obj.x,'y':locate_obj.y})

        for i in range(3):
            input('サーバント{}体目の宝具カードの位置'.format(i+1))
            locate_obj = pyautogui.position()
            save_json['battle']['NP'].append({'x':locate_obj.x,'y':locate_obj.y})

        # サーヴァント1機目のスキル位置の設定
        print('サーヴァント1機目のスキル位置設定')
        for i in range(3):
            skill_pos = input('スキル{}の場所設定(aを入力してEnterで登録):'.format(i+1))
            locate_obj = pyautogui.position()
            save_json['servant1']['skill'].append({'x':locate_obj.x,'y':locate_obj.y})
        
        # サーヴァント2機目のスキル位置の設定
        print('サーヴァント2機目のスキル位置設定')
        for i in range(3):
            skill_pos = input('スキル{}の場所設定(aを入力してEnterで登録):'.format(i+1))
            locate_obj = pyautogui.position()
            save_json['servant2']['skill'].append({'x':locate_obj.x,'y':locate_obj.y})

        # サーヴァント3機目のスキル位置の設定
        print('サーヴァント3機目のスキル位置設定')
        for i in range(3):
            skill_pos = input('スキル{}の場所設定(aを入力してEnterで登録):'.format(i+1))
            locate_obj = pyautogui.position()
            save_json['servant3']['skill'].append({'x':locate_obj.x,'y':locate_obj.y})
        
        # スキル対象サーヴァントにするの位置設定
        print("スキルの対象にする位置の設定")
        for i in range(3):
            skill_pos = input('サーヴァント{}の位置(aを入力してEnterで登録):'.format(i+1))
            locate_obj = pyautogui.position()
            save_json['servant{}'.format(i+1)]['target'] = {'x':locate_obj.x,'y':locate_obj.y}

        # マスタースキルの位置設定
        print("マスタースキルの位置設定")
        skill_pos = input('マスタースキルの位置(aを入力してEnterで登録):'.format(i+1))
        locate_obj = pyautogui.position()
        save_json['master_skill'].append({'x':locate_obj.x,'y':locate_obj.y})
        for i in range(3):
            skill_pos = input('スキル{}の位置(aを入力してEnterで登録):'.format(i+1))
            locate_obj = pyautogui.position()
            save_json['master_skill'].append({'x':locate_obj.x,'y':locate_obj.y})

        # 設定保存
        with open('./posision/option.json', 'w') as f:
            f.write(json.dumps(save_json,indent=4))
        
        print("設定完了")

    # 設定をロードする
    def read_option(self):
        read_str = ''
        with open('./posision/option.json','r') as f:
            read_str = f.read()
        self.option = json.loads(read_str)

    # 指定の位置に移動してクリックする処理
    def move_click(self,x_pos,y_pos,wait):
        pyautogui.moveTo(x_pos, y_pos)
        pyautogui.click()
        time.sleep(float(wait))

    # 待ち処理
    def wait_battle(self,image_path):
        # 表示待ち
        while(1):
            if(pyautogui.locateOnScreen(image_path, confidence=0.9) != None):
                break

    # カードを開いて選択する処理
    def select_card(self):
        pass
        # カードを開く

        # カードを選択する


    # 登録したマクロを開始する
    def run_battle(self):
        # 表示待ち
        self.wait_battle(self.check_master_path)
        
        # バトル1をすすめる
        for (x_posision, y_posision, wait) in zip(self.battle1_Xposision_list, self.battle1_Yposision_list, self.battle1_wait):
            self.move_click(x_posision, y_posision, wait)

        # カードを選択する
        self.wait_battle(self.check_master_path)
        self.select_card()

        # 表示待ち
        self.wait_battle(self.check_master_path)

        # バトル2をすすめる
        for (x_posision, y_posision, wait) in zip(self.battle2_Xposision_list, self.battle2_Yposision_list, self.battle2_wait):
            self.move_click(x_posision, y_posision, wait)
        
        self.wait_battle(self.check_master_path)
        self.select_card()

        # 表示待ち
        self.wait_battle(self.check_master_path)

        # バトル3をすすめる
        for (x_posision, y_posision, wait) in zip(self.battle3_Xposision_list, self.battle3_Yposision_list, self.battle3_wait):
            self.move_click(x_posision, y_posision, wait)
        
        self.wait_battle(self.check_master_path)
        self.select_card()

        # TODO: 終了したあとの処理(作成途中)

        # リザルト画面を進める処理
        # 次へボタンをクリックする
        while(1):
            pyautogui.click()
            locate_obj = pyautogui.locateOnScreen(self.check_next_button_path, confidence=0.9)
            if(locate_obj != None):
                pyautogui.moveTo(locate_obj.left,locate_obj.top)
                pyautogui.click()
                break
        
        # 連続出撃をクリック
        while(1):
            locate_obj = pyautogui.locateOnScreen(self.check_next_battle_path, confidence=0.9)
            if(locate_obj != None):
                pyautogui.moveTo(locate_obj.left,locate_obj.top)
                pyautogui.click()
                break

    # フレンドを選択して連続出撃する
    def run_select_friend(self):
        time.sleep(1)
        is_find = False

        # フレンドを選ぶ処理
        while(is_find == False):
            for i in range(5):
                time.sleep(0.5)
                # 対象のフレンドを探す
                f = pyautogui.locateOnScreen(self.check_select_friend, confidence=0.9)
                print(f)
                # 見つかった場合
                if(f != None):
                    pyautogui.moveTo(f.left,f.top)
                    pyautogui.click()
                    is_find = True
                    break
                # 見つからなかった場合
                else:
                    # リストをドラッグする
                    pyautogui.moveTo(self.battle_start_posX+50,self.battle_start_posY)
                    time.sleep(1)
                    pyautogui.drag(0,-300,1)
            # フレンドリストを更新
            if(is_find == False):
                list_update = pyautogui.locateOnScreen(self.check_list_update_button,confidence=0.9)
                pyautogui.moveTo(list_update.left,list_update.top)
                pyautogui.click()
                time.sleep(1)
                yes_b = pyautogui.locateOnScreen(self.check_yes_button,confidence=0.8)
                print(yes_b)
                pyautogui.moveTo(yes_b.left,yes_b.top)
                pyautogui.click()
        time.sleep(2)
