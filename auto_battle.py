import time
import pyautogui

class auto_battle:

    # コンストラクタ
    def __init__(self):
        # スキルクリック位置の横座標
        self.battle1_Xposision_list = []
        self.battle2_Xposision_list = []
        self.battle3_Xposision_list = []

        # スキルクリック位置の縦座標
        self.battle1_Yposision_list = []
        self.battle2_Yposision_list = []
        self.battle3_Yposision_list = []

        # クリック後の待ち時間
        self.battle1_wait = []
        self.battle2_wait = []
        self.battle3_wait = []

        # クリック数の記録
        self.battle1_skill_num = 1
        self.battle2_skill_num = 1
        self.battle3_skill_num = 1

        # バトルスタートボタンの位置
        self.battle_start_posX = 0
        self.battle_start_posY = 0

        # 選択するカードの位置
        self.select_card1_posX = 0
        self.select_card1_posY = 0
        self.select_card2_posX = 0
        self.select_card2_posY = 0
        self.select_card3_posX = 0
        self.select_card3_posY = 0

        # menu
        self.check_master_path = './read_image/master.png'
        # 獲得EXPの画像
        self.check_exp_path = './read_image/battle_exp.png'
        # 獲得絆の画像
        self.check_kizuna_path = './read_image/battle_kizuna.png'
        # 連続出撃の画像
        self.check_next_battle_path = './read_image/next_battle.png'
        # 次への画像
        self.check_next_button_path = './read_image/next_button.png'
    
    # マクロ(クリック位置)を登録する処理
    def regist_click_posission(self):
        print('バトルスタートボタンの位置設定(aを入力してEnterで登録)')
        input()
        locate_obj = pyautogui.position()
        self.battle_start_posX = locate_obj.x
        self.battle_start_posY = locate_obj.y

        print('選択するカードの位置設定(aを入力してEnterで登録)')
        print('1つ目')
        input()
        locate_obj = pyautogui.position()
        self.select_card1_posX = locate_obj.x
        self.select_card1_posY = locate_obj.y

        print('2つ目')
        input()
        locate_obj = pyautogui.position()
        self.select_card2_posX = locate_obj.x
        self.select_card2_posY = locate_obj.y

        print('3つ目')
        input()
        locate_obj = pyautogui.position()
        self.select_card3_posX = locate_obj.x
        self.select_card3_posY = locate_obj.y

        print('バトル1で撃つスキルの設定')
        is_posision_save=input()
        print('クリック{}回目(aを入力してEnterで登録、nを入力で登録終了)'.format(self.battle1_skill_num))
        while(is_posision_save == 'a'):

            locate_obj = pyautogui.position()
            self.battle1_Xposision_list.append(locate_obj.x)
            self.battle1_Yposision_list.append(locate_obj.y)

            print('クリック登録：x={}, y={}'.format(locate_obj.x, locate_obj.y))
            print('待ち時間入力')
            wait_time = input() 
            
            while(wait_time.isascii() == False):
                print('数値を入力してください')
                wait_time = input()
            
            self.battle1_wait.append(wait_time)
            self.battle1_skill_num +=1

            print('クリック{}回目(aを入力してEnterで登録、nを入力で登録終了)'.format(self.battle1_skill_num))
            is_posision_save=input()

        print('バトル2登録完了')

        print('バトル2で撃つスキルの設定')
        is_posision_save=input()
        print('クリック{}回目(aを入力してEnterで登録、nを入力で登録終了)'.format(self.battle2_skill_num))
        while(is_posision_save == 'a'):

            locate_obj = pyautogui.position()
            self.battle2_Xposision_list.append(locate_obj.x)
            self.battle2_Yposision_list.append(locate_obj.y)

            print('クリック登録：x={}, y={}'.format(locate_obj.x, locate_obj.y))
            print('待ち時間入力')
            wait_time = input() 
            
            while(wait_time.isascii() == False):
                print('数値を入力してください')
                wait_time = input()
            
            self.battle2_wait.append(wait_time)
            self.battle2_skill_num +=1

            print('クリック{}回目(aを入力してEnterで登録、nを入力で登録終了)'.format(self.battle1_skill_num))
            is_posision_save=input()

        print('バトル2登録完了')

        print('バトル3で撃つスキルの設定')
        print('クリック{}回目(aを入力してEnterで登録、nを入力で登録終了)'.format(self.battle3_skill_num))
        is_posision_save=input()
        while(is_posision_save == 'a'):

            locate_obj = pyautogui.position()
            self.battle3_Xposision_list.append(locate_obj.x)
            self.battle3_Yposision_list.append(locate_obj.y)

            print('クリック登録：x={}, y={}'.format(locate_obj.x, locate_obj.y))
            print('待ち時間入力')
            wait_time = input() 
            
            while(wait_time.isascii() == False):
                print('数値を入力してください')
                wait_time = input()
            
            self.battle3_wait.append(wait_time)
            self.battle3_skill_num +=1

            print('クリック{}回目(aを入力してEnterで登録、nを入力で登録終了)'.format(self.battle1_skill_num))
            is_posision_save=input()

        print('バトル3登録完了')

    # 登録している設定を保存する
    def save_file(self):
        self.save_skill_file()
        self.save_card_select_file()

    # カードセレクトの場所を記録
    def save_card_select_file(self):
        save_string = ''
        save_string = '{},{}\n'.format(self.battle_start_posX,self.battle_start_posY)
        save_string = save_string + '{},{}\n'.format(self.select_card1_posX,self.select_card1_posY)
        save_string = save_string + '{},{}\n'.format(self.select_card2_posX,self.select_card2_posY)
        save_string = save_string + '{},{}\n'.format(self.select_card3_posX,self.select_card3_posY)
        with open('./posision/save_select.txt','w') as f:
            f.write(save_string)

    # スキル選択の場所を記録
    def save_skill_file(self):
        save_string = ''
        save_string = str(self.battle1_skill_num - 1) + '\n'
        for (x_posision, y_posision, wait) in zip(self.battle1_Xposision_list, self.battle1_Yposision_list, self.battle1_wait):
            save_string = save_string + '{},{},{}\n'.format(x_posision, y_posision,wait)

        save_string = save_string + str(self.battle2_skill_num) + '\n'
        for (x_posision, y_posision, wait) in zip(self.battle2_Xposision_list, self.battle2_Yposision_list, self.battle2_wait):
            save_string = save_string + '{},{},{}\n'.format(x_posision, y_posision,wait)

        save_string = save_string + str(self.battle3_skill_num) + '\n'
        for (x_posision, y_posision, wait) in zip(self.battle3_Xposision_list, self.battle3_Yposision_list, self.battle3_wait):
            save_string = save_string + '{},{},{}\n'.format(x_posision, y_posision,wait)

        with open('./posision/save_skill.txt','w') as f:
            f.write(save_string)

    # 設定をロードする
    def read_option(self):
        self.read_skill_file()
        self.read_select_file()

    # スキル選択の場所をロード
    def read_skill_file(self):
        with open('./posision/save_skill.txt','r') as f:
            read_string = f.readline().removeprefix('\n')
            for i in range(int(read_string)):
                read_string_pos = f.readline().removeprefix('\n')
                pos_x,pos_y,waitnum = str(read_string_pos).split(',')
                self.battle1_Xposision_list.append(int(pos_x))
                self.battle1_Yposision_list.append(int(pos_y))
                self.battle1_wait.append(float(waitnum))

            read_string = f.readline().removeprefix('\n')
            for i in range(int(read_string)):
                read_string_pos = f.readline().removeprefix('\n')
                pos_x,pos_y,waitnum = str(read_string_pos).split(',')
                self.battle2_Xposision_list.append(int(pos_x))
                self.battle2_Yposision_list.append(int(pos_y))
                self.battle2_wait.append(float(waitnum))

            read_string = f.readline().removeprefix('\n')
            for i in range(int(read_string)):
                read_string_pos = f.readline().removeprefix('\n')
                pos_x,pos_y,waitnum = str(read_string_pos).split(',')
                self.battle3_Xposision_list.append(int(pos_x))
                self.battle3_Yposision_list.append(int(pos_y))
                self.battle3_wait.append(float(waitnum))

    # カードセレクトの場所をロード
    def read_select_file(self):
        with open('./posision/save_select.txt','r') as f:
            read_string = f.readline().removeprefix('\n')
            pos_x,pos_y = read_string.split(',')
            self.battle_start_posX = int(pos_x)
            self.battle_start_posY = int(pos_y)

            read_string = f.readline().removeprefix('\n')
            pos_x,pos_y = read_string.split(',')
            self.select_card1_posX = int(pos_x)
            self.select_card1_posY = int(pos_y)

            read_string = f.readline().removeprefix('\n')
            pos_x,pos_y = read_string.split(',')
            self.select_card2_posX = int(pos_x)
            self.select_card2_posY = int(pos_y)

            read_string = f.readline().removeprefix('\n')
            pos_x,pos_y = read_string.split(',')
            self.select_card3_posX = int(pos_x)
            self.select_card3_posY = int(pos_y)


    def test(self):
        # バトル1をすすめる
        for (x_posision, y_posision, wait) in zip(self.battle1_Xposision_list, self.battle1_Yposision_list, self.battle1_wait):
            self.move_click(x_posision, y_posision, wait)

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
        # カードを開く
        self.move_click(self.battle_start_posX, self.battle_start_posY, 2)

        # カードを選択する
        self.move_click(self.select_card1_posX,self.select_card1_posY, 0.5)
        self.move_click(self.select_card2_posX,self.select_card2_posY, 0.5)
        self.move_click(self.select_card3_posX,self.select_card3_posY, 0.5)

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

        # フレンドを選ぶ処理

        # ↓リザルトを進める処理の作りかけ
        self.wait_battle(self.check_kizuna_path)
        self.wait_battle(self.check_master_path)
        self.wait_battle(self.check_next_button_path)
        self.wait_battle(self.check_next_battle_path)
        
        # 獲得絆画面を進める
        while(1):
            locate_obj = pyautogui.locateOnScreen(self.check_kizuna_path, confidence=0.9)
            if(locate_obj != None):
                pyautogui.click(locate_obj.width,locate_obj.height)
                break
        
        # マスターEXP画面を進める
        while(1):
            locate_obj = pyautogui.locateOnScreen(self.check_master_path, confidence=0.9)
            if(locate_obj != None):
                pyautogui.click(locate_obj.width,locate_obj.height)
                break
        # 次へボタンをクリックする
        while(1):
            locate_obj = pyautogui.locateOnScreen(self.check_next_button_path, confidence=0.9)
            if(locate_obj != None):
                pyautogui.click(locate_obj.width,locate_obj.height)
                break
            
        # 連続出撃をクリック
        while(1):
            locate_obj = pyautogui.locateOnScreen(self.check_next_battle_path, confidence=0.9)
            if(locate_obj != None):
                pyautogui.click(locate_obj.width,locate_obj.height)
                break

        
