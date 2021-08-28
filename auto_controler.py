from auto_battle import auto_battle
import json
import win32gui
import pyautogui

class auto_controler:

    # コンストラクタ
    def __init__(self):
        self.auto_b = auto_battle()

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

    # 周回の設定
    def regist_battle(self):
        pass

    # 画像認識の確認
    def check_image(self):
        battle_path = './read_image/battle/'
        friend_search_path = './read_image/friend_search/'
        result_path = './read_image/result/'

        # 確認する画像の画面を選択(バトル画面、リザルト画面、フレンド選択画面)
        print('確認する画面を選択してください')
        select_since = input('[1.バトル画面 2.リザルト画面 3.フレンド選択画面]:')
        
        print('画像が検出できるか確認します')
        if(select_since == '1'):
            input('バトル画面を表示したらENTERを押してください:')
            # バトル画面の画像確認
            check_image_obj = self.auto_b.check_image(battle_path + 'master.png')
            if(check_image_obj != None):
                print('検出できました')
            else:
                print('検出できませんでした')

        elif(select_since == '2'):
            input('リザルトの報酬獲得画面を表示したらENTERを押してください:')
            # 次へボタンを確認
            check_image_obj = self.auto_b.check_image(result_path + 'next_button.png')
            if(check_image_obj != None):
                print('検出できました')
            else:
                print('検出できませんでした')
            
            input('連続出撃画面を表示したらENTERを押してください:')
            # 連続出撃ボタンを確認
            check_image_obj = self.auto_b.check_image(result_path + 'next_battle.png')
            if(check_image_obj != None):
                print('検出できました')
            else:
                print('検出できませんでした')
            
        elif(select_since == '3'):
            input('フレンド選択画面を表示したらENTERを押してください:')
            # リスト更新ボタンを確認
            check_image_obj = self.auto_b.check_image(friend_search_path + 'friend_list_update.png')
            if(check_image_obj != None):
                print('検出できました')
            else:
                print('検出できませんでした')
            
            # 「はい」ボタンを確認
            input('リスト更新ボタンをクリックしたらENTERを押してください:')
            check_image_obj = self.auto_b.check_image(friend_search_path + 'yes_button.png')
            if(check_image_obj != None):
                print('検出できました')
            else:
                print('検出できませんでした')

            # 選ぶフレンドを確認
            check_image_obj = self.auto_b.check_image(friend_search_path + 'select_friend.png')
            if(check_image_obj != None):
                print('検出できました')
            else:
                print('検出できませんでした')
        else:
            print('終了')
            return
        
        return

    # コンソール上で選ぶメニューを表示する
    def menu(self):
        while(1):
            print()
            menu_number = input('番号を入力してください[1:位置設定 2:周回設定 3:画像認識確認 4:終了]:')

            if(menu_number == '1'):
                self.regist_config()
            elif(menu_number == '2'):
                self.regist_battle()
            elif(menu_number == '3'):
                self.check_image()
            elif(menu_number == '4'):
                print('終了します')
                return 0