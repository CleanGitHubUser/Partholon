# -*- coding: utf-8 -*-

import sys
import os
import copy
import random
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import configparser

config = configparser.ConfigParser()

if not os.path.exists('cfg.ini'):
    config.add_section('hnuml')
    config['hnuml']['hnum1'] = '0'
    config['hnuml']['hnum2'] = '0'
    config['hnuml']['hnum3'] = '0'
    config['hnuml']['hnum4'] = '0'
    config['hnuml']['hnum5'] = '0'
    config['hnuml']['hnum6'] = '0'
    config['hnuml']['hnum7'] = '0'
    config['hnuml']['hnum8'] = '0'
    config['hnuml']['hnum9'] = '0'
    config['hnuml']['hnum10'] = '0'
    config['hnuml']['hnum11'] = '0'
    config['hnuml']['hnum12'] = '0'

    config.add_section('missionl')
    config['missionl']['mission11'] = ''
    config['missionl']['mission12'] = ''
    config['missionl']['mission13'] = ''
    config['missionl']['mission21'] = ''
    config['missionl']['mission22'] = ''
    config['missionl']['mission23'] = ''
    config['missionl']['mission31'] = ''
    config['missionl']['mission32'] = ''
    config['missionl']['mission33'] = ''
    config['missionl']['mission41'] = ''
    config['missionl']['mission42'] = ''
    config['missionl']['mission43'] = ''
    config['missionl']['mission51'] = ''
    config['missionl']['mission52'] = ''
    config['missionl']['mission53'] = ''

    config.add_section('mnuml')
    config['mnuml']['mnum1'] = '0'
    config['mnuml']['mnum2'] = '0'
    config['mnuml']['mnum3'] = '0'
    config['mnuml']['mnum4'] = '0'
    config['mnuml']['mnum5'] = '0'

    with open('cfg.ini', 'w') as configfile:
        config.write(configfile)

def mhhd(hnuml = 0):
    if hnuml == 0:
        hnuml = []
        for i in range(0, 12):
            hnuml.append(0)
    h1char = ['뛰어난 평형 감각', '강인한 내성',
           '예리한 칼날', '복수의 그림자', '검투사의 긍지']
    h1num = hnuml[0]
    h1name = '리시타'
    h1 = [h1char, h1num, h1name]

    h2char = ['강철 위장', '조용한 발걸음',
           '신중한 전술', '복수의 그림자', '방패 전문가']
    h2num = hnuml[1]
    h2name = '피오나'
    h2 = [h2char, h2num, h2name]

    h3char = ['별자리 해석', '깊은 내면',
          '원격 사격', '정화의 일격', '원소의 마법사']
    h3num = hnuml[2]
    h3name = '이비'
    h3 = [h3char, h3num, h3name]

    h4char = ['강철 위장', '깊은 내면',
          '남다른 골격', '정화의 일격', '자이언트']
    h4num = hnuml[3]
    h4name = '카록'
    h4 = [h4char, h4num, h4name]

    h5char = ['어둠에 밝은 눈', '야생동물 지식',
          '원격 사격', '기선 제압', '고독한 저격수']
    h5num = hnuml[4]
    h5name = '카이'
    h5 = [h5char, h5num, h5name]

    h6char = ['항해술', '야생동물 지식',
          '연쇄 타격', '기선 제압', '타고난 모험가']
    h6num = hnuml[5]
    h6name = '벨라'
    h6 = [h6char, h6num, h6name]

    h7char = ['항해술', '강인한 내성',
          '남다른 골격', '거대한 무기', '자유로운 방랑자']
    h7num = hnuml[6]
    h7name = '허크'
    h7 = [h7char, h7num, h7name]

    h8char = ['고결한 태생', '조용한 발걸음',
         '신출귀몰', '정화의 일격', '꽃잎의 맹세']
    h8num = hnuml[7]
    h8name = '린'
    h8 = [h8char, h8num, h8name]

    h9char = ['어둠에 밝은 눈', '야생동물 지식',
           '신출귀몰', '기선 제압', '시공의 지배자']
    h9num = hnuml[8]
    h9name = '아리샤'
    h9 = [h9char, h9num, h9name]

    h10char = ['별자리 해석', '조용한 발걸음',
          '신중한 전술', '복수의 그림자', '환영 마법사']
    h10num = hnuml[9]
    h10name = '헤기'
    h10 = [h10char, h10num, h10name]

    h11char = ['고결한 태생', '강인한 내성',
           '예리한 칼날', '거대한 무기', '신념의 수호자']
    h11num = hnuml[10]
    h11name = '델리아'
    h11 = [h11char, h11num, h11name]

    h12char = ['뛰어난 평형 감각', '깊은 내면',
          '연쇄 타격', '거대한 무기', '드래곤의 후예']
    h12num = hnuml[11]
    h12name = '미리'
    h12 = [h12char, h12num, h12name]

    heroes = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12]
    # print(heroes)

    return heroes

def mhmd(missionl, mnuml):

    resultml = []
    for mission, mnum in zip(missionl, mnuml):
        resultml.append([mission, mnum])
    # print(resultml)

    return resultml

def placeOne(herol, missionl, placel):
    # print(placel)
    # for mission in missionl:
    #     print('msp', mission[1])
    for hero in herol:
        mmatchl = []
        for mission in missionl:
            cnt = 0
            if mission[1] != 0:
                for char in hero[0]:
                    if char in mission[0]:
                        cnt += 1
            mmatchl.append(cnt)
        hero.append(mmatchl)
    # for hero in herol:
    #     print('mmatch', hero[1:4])

    maxmm = 0
    for hero in herol:
        if max(hero[3]) > maxmm:
            maxmm = max(hero[3])
    # print('maxmm', maxmm)

    if maxmm == 0: resultl = False
    else:
        maxmmhl = []
        for hero in herol:
            if max(hero[3]) == maxmm:
                maxmmhl.append(hero)
        # for maxmmh in maxmmhl:
        #     print('maxmmh', maxmmh[1:4])

        import numpy as np
        for hero in maxmmhl:
            hero[3] = np.array(hero[3])
            idx = np.where(hero[3] == maxmm)[0]
            hero[3] = list(hero[3])
            idx = list(idx)
            hero.append(idx)
        # for hero in maxmmhl:
            # print('idx', hero[1:5])

        mindiff = 100
        mindiffhl = []
        for hero in maxmmhl:
            for idx in hero[4]:

                tmpml = copy.deepcopy(missionl)
                for char in hero[0]:
                    if char in tmpml[idx][0]:
                        tmpml[idx][0].remove(char)
                tmphl = []
                for tmph in herol:
                    tmphl.append(copy.deepcopy(tmph[0:3]))
                for tmph in tmphl:
                    if tmph[2] == hero[2]:
                        tmph[1] -= 1
                    mmatchl = []
                    for tmpm in tmpml:
                        cnt = 0
                        for char in tmph[0]:
                            if char in tmpm[0]:
                                cnt += 1
                        mmatchl.append(cnt)
                    tmph.append(mmatchl)
                diff = 0
                for i in range(0, len(herol)):
                    diff += sum(herol[i][3]) - sum(tmphl[i][3])
                if diff < mindiff:
                    mindiff = diff
                    tmph = hero[0:4]
                    tmph.append(idx)
                    mindiffhl = [tmph]
                elif diff == mindiff:
                    tmph = hero[0:4]
                    tmph.append(idx)
                    mindiffhl.append(tmph)
        # for hero in mindiffhl:
            # print('mindiffh', hero[2:5])

        minmm = 100
        minmmhl = []
        for mindh in mindiffhl:
            if sum(mindh[3]) < minmm:
                minmm = sum(mindh[3])
                minmmhl = [mindh]
            elif sum(mindh[3]) == minmm:
                minmmhl.append(mindh)
        # for hero in minmmhl:
            # print('minmmh', hero[1:5])

        resultl = []
        for minmmh in minmmhl:
            hnamel = []
            for hero in herol:
                hnamel.append(hero[2])
            idx = hnamel.index(minmmh[2])

            resulthl = []
            for hero in herol:
                resulthl.append(copy.deepcopy(hero[0:3]))
            resulthl[idx][1] -= 1

            tmphl = copy.deepcopy(resulthl)
            for hero in tmphl:
                if hero[1] == 0:
                    resulthl.remove(hero)

            idx = minmmh[4]
            resultml = copy.deepcopy(missionl)
            resultml[idx][1] -= 1

            for char in minmmh[0]:
                if char in missionl[idx][0]:
                    resultml[idx][0].remove(char)

            resultpl = copy.deepcopy(placel)
            resultpl.append([minmmh[2], minmmh[4]])

            resultl.append([resulthl, resultml, resultpl])
        # for result in resultl:
            # print(result[2])

    return resultl

def mhprocess(herol, missionl):
    # herol = mhhd([1, 2, 1, 1, 1, 1,
    #                   1, 1, 1, 1, 1, 1])
    tmphl = copy.deepcopy(herol)
    for hero in tmphl:
        if hero[1] == 0:
            herol.remove(hero)
    # print(tmphl)

    # missionl = mhmd()
    beforenum = 0
    for mission in missionl:
        beforenum += len(mission[0])

    tmpml = copy.deepcopy(missionl)
    for mission in tmpml:
        if mission[1] == 0:
            missionl.remove(mission)
    # print(tmpml)

    totalhnum = 0
    for hero in herol:
        totalhnum += hero[1]
    totalsnum = 0
    for mission in missionl:
        totalsnum += mission[1]

    placel = []
    runningrl = [[herol, missionl, placel]]
    totalresultl = []
    while True:
        ttmprl = []
        for resultl in runningrl:
            tmprl = placeOne(resultl[0], resultl[1], resultl[2])
            if tmprl == False:
                totalresultl.append(resultl[2])
            else:
                for tmpr in tmprl:
                    ttmprl.append(tmpr)
        runningrl = ttmprl
        if len(runningrl) == 0: break

    herol = mhhd()
    hnamel = []
    for hero in herol:
        hnamel.append(hero[2])

    maxdiff = 0
    maxdiffrl = []
    for placel in totalresultl:
        tmpml = copy.deepcopy(missionl)
        for place in placel:
            idx = hnamel.index(place[0])
            for char in herol[idx][0]:
                if char in tmpml[place[1]][0]:
                    tmpml[place[1]][0].remove(char)
        afternum = 0
        for mission in tmpml:
            afternum += len(mission[0])
        if beforenum - afternum > maxdiff:
            maxdiff = beforenum - afternum
            maxdiffrl = [placel]
        elif beforenum - afternum == maxdiff:
            maxdiffrl.append(placel)
    # print(maxdiffrl)
    return maxdiffrl


class mhmain(QMainWindow):

    def __init__(self):

        config = configparser.ConfigParser()
        config.read('cfg.ini')
        self.hnum1 = int(config['hnuml']['hnum1'])
        self.hnum2 = int(config['hnuml']['hnum2'])
        self.hnum3 = int(config['hnuml']['hnum3'])
        self.hnum4 = int(config['hnuml']['hnum4'])
        self.hnum5 = int(config['hnuml']['hnum5'])
        self.hnum6 = int(config['hnuml']['hnum6'])
        self.hnum7 = int(config['hnuml']['hnum7'])
        self.hnum8 = int(config['hnuml']['hnum8'])
        self.hnum9 = int(config['hnuml']['hnum9'])
        self.hnum10 = int(config['hnuml']['hnum10'])
        self.hnum11 = int(config['hnuml']['hnum11'])
        self.hnum12 = int(config['hnuml']['hnum12'])

        self.mission11 = config['missionl']['mission11']
        self.mission12 = config['missionl']['mission12']
        self.mission13 = config['missionl']['mission13']
        self.mission21 = config['missionl']['mission21']
        self.mission22 = config['missionl']['mission22']
        self.mission23 = config['missionl']['mission23']
        self.mission31 = config['missionl']['mission31']
        self.mission32 = config['missionl']['mission32']
        self.mission33 = config['missionl']['mission33']
        self.mission41 = config['missionl']['mission41']
        self.mission42 = config['missionl']['mission42']
        self.mission43 = config['missionl']['mission43']
        self.mission51 = config['missionl']['mission51']
        self.mission52 = config['missionl']['mission52']
        self.mission53 = config['missionl']['mission53']

        self.mnum1 = int(config['mnuml']['mnum1'])
        self.mnum2 = int(config['mnuml']['mnum2'])
        self.mnum3 = int(config['mnuml']['mnum3'])
        self.mnum4 = int(config['mnuml']['mnum4'])
        self.mnum5 = int(config['mnuml']['mnum5'])

        super().__init__()
        self.title = '파르홀른 배치'
        self.left = 100
        self.top = 100
        self.width = 390
        self.height = 355
        self.setWindowIcon(QIcon(sys.argv[0]))
        self.win2 = Window2(QMainWindow)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel("캐릭터 수", self)
        label.move(20, 10)

        # 리시타 수
        label = QLabel('리시타', self)
        label.move(20, 35)

        self.hnumq1 = QLineEdit(self)
        self.hnumq1.move(70, 40)
        self.hnumq1.setText(str(self.hnum1))
        self.hnumq1.resize(20, 20)
        self.hnumq1.textChanged[str].connect(self.onChangedhn1)
        

        # 피오나 수
        label = QLabel('피오나', self)
        label.move(20, 60)

        self.hnumq2 = QLineEdit(self)
        self.hnumq2.move(70, 65)
        self.hnumq2.setText(str(self.hnum2))
        self.hnumq2.resize(20, 20)
        self.hnumq2.textChanged[str].connect(self.onChangedhn2)

        # 이비 수
        label = QLabel('이비', self)
        label.move(20, 85)

        self.hnumq3 = QLineEdit(self)
        self.hnumq3.move(70, 90)
        self.hnumq3.setText(str(self.hnum3))
        self.hnumq3.resize(20, 20)
        self.hnumq3.textChanged[str].connect(self.onChangedhn3)

        # 카록 수
        label = QLabel('카록', self)
        label.move(20, 110)

        self.hnumq4 = QLineEdit(self)
        self.hnumq4.move(70, 115)
        self.hnumq4.setText(str(self.hnum4))
        self.hnumq4.resize(20, 20)
        self.hnumq4.textChanged[str].connect(self.onChangedhn4)

        # 카이 수
        label = QLabel('카이', self)
        label.move(20, 135)

        self.hnumq5 = QLineEdit(self)
        self.hnumq5.move(70, 140)
        self.hnumq5.setText(str(self.hnum5))
        self.hnumq5.resize(20, 20)
        self.hnumq5.textChanged[str].connect(self.onChangedhn5)

        # 벨라 수
        label = QLabel('벨라', self)
        label.move(20, 160)

        self.hnumq6 = QLineEdit(self)
        self.hnumq6.move(70, 165)
        self.hnumq6.setText(str(self.hnum6))
        self.hnumq6.resize(20, 20)
        self.hnumq6.textChanged[str].connect(self.onChangedhn6)

        # 허크 수
        label = QLabel('허크', self)
        label.move(20, 185)

        self.hnumq7 = QLineEdit(self)
        self.hnumq7.move(70, 190)
        self.hnumq7.setText(str(self.hnum7))
        self.hnumq7.resize(20, 20)
        self.hnumq7.textChanged[str].connect(self.onChangedhn7)

        # 린 수
        label = QLabel('린', self)
        label.move(20, 210)

        self.hnumq8 = QLineEdit(self)
        self.hnumq8.move(70, 215)
        self.hnumq8.setText(str(self.hnum8))
        self.hnumq8.resize(20, 20)
        self.hnumq8.textChanged[str].connect(self.onChangedhn8)

        # 아리샤 수
        label = QLabel('아리샤', self)
        label.move(20, 235)

        self.hnumq9 = QLineEdit(self)
        self.hnumq9.move(70, 240)
        self.hnumq9.setText(str(self.hnum9))
        self.hnumq9.resize(20, 20)
        self.hnumq9.textChanged[str].connect(self.onChangedhn9)

        # 헤기 수
        label = QLabel('헤기', self)
        label.move(20, 260)

        self.hnumq10 = QLineEdit(self)
        self.hnumq10.move(70, 265)
        self.hnumq10.setText(str(self.hnum10))
        self.hnumq10.resize(20, 20)
        self.hnumq10.textChanged[str].connect(self.onChangedhn10)

        # 델리아 수
        label = QLabel('델리아', self)
        label.move(20, 285)

        self.hnumq11 = QLineEdit(self)
        self.hnumq11.move(70, 290)
        self.hnumq11.setText(str(self.hnum11))
        self.hnumq11.resize(20, 20)
        self.hnumq11.textChanged[str].connect(self.onChangedhn11)

        # 미리 수
        label = QLabel('미리', self)
        label.move(20, 310)

        self.hnumq12 = QLineEdit(self)
        self.hnumq12.move(70, 315)
        self.hnumq12.setText(str(self.hnum12))
        self.hnumq12.resize(20, 20)
        self.hnumq12.textChanged[str].connect(self.onChangedhn12)

        # 특성 목록
        herol = mhhd()

        charl = []
        for hero in herol:
            for char in hero[0]:
                charl.append(char)

        chars = set(charl)
        ucharl = list(chars)
        ucharl.sort()

        # 미션1
        label = QLabel('미션1', self)
        label.move(110, 10)

        self.contq11 = QComboBox(self)
        for char in ucharl:
            self.contq11.addItem(char)
        self.contq11.move(110, 40)
        self.contq11.setCurrentText(self.mission11)
        self.contq11.resize(120, 20)
        self.contq11.currentTextChanged.connect(self.combobox_changedct11)

        self.contq12 = QComboBox(self)
        for char in ucharl:
            self.contq12.addItem(char)
        self.contq12.move(110, 60)
        self.contq12.setCurrentText(self.mission12)
        self.contq12.resize(120, 20)
        self.contq12.currentTextChanged.connect(self.combobox_changedct12)

        self.contq13 = QComboBox(self)
        for char in ucharl:
            self.contq13.addItem(char)
        self.contq13.move(110, 80)
        self.contq13.setCurrentText(self.mission13)
        self.contq13.resize(120, 20)
        self.contq13.currentTextChanged.connect(self.combobox_changedct13)

        label = QLabel('슬롯 수', self)
        label.move(110, 95)

        self.mnumq1 = QLineEdit(self)
        self.mnumq1.move(160, 100)
        self.mnumq1.setText(str(self.mnum1))
        self.mnumq1.resize(20, 20)
        self.mnumq1.textChanged[str].connect(self.onChangedmn1)

        # 미션2
        label = QLabel('미션2', self)
        label.move(110, 120)

        self.contq21 = QComboBox(self)
        for char in ucharl:
            self.contq21.addItem(char)
        self.contq21.move(110, 150)
        self.contq21.setCurrentText(self.mission21)
        self.contq21.resize(120, 20)
        self.contq21.currentTextChanged.connect(self.combobox_changedct21)

        self.contq22 = QComboBox(self)
        for char in ucharl:
            self.contq22.addItem(char)
        self.contq22.move(110, 170)
        self.contq22.setCurrentText(self.mission22)
        self.contq22.resize(120, 20)
        self.contq22.currentTextChanged.connect(self.combobox_changedct22)

        self.contq23 = QComboBox(self)
        for char in ucharl:
            self.contq23.addItem(char)
        self.contq23.move(110, 190)
        self.contq23.setCurrentText(self.mission23)
        self.contq23.resize(120, 20)
        self.contq23.currentTextChanged.connect(self.combobox_changedct23)

        label = QLabel('슬롯 수', self)
        label.move(110, 205)

        self.mnumq2 = QLineEdit(self)
        self.mnumq2.move(160, 210)
        self.mnumq2.setText(str(self.mnum2))
        self.mnumq2.resize(20, 20)
        self.mnumq2.textChanged[str].connect(self.onChangedmn2)

        # 미션3
        label = QLabel('미션3', self)
        label.move(110, 230)

        self.contq31 = QComboBox(self)
        for char in ucharl:
            self.contq31.addItem(char)
        self.contq31.move(110, 260)
        self.contq31.setCurrentText(self.mission31)
        self.contq31.resize(120, 20)
        self.contq31.currentTextChanged.connect(self.combobox_changedct31)

        self.contq32 = QComboBox(self)
        for char in ucharl:
            self.contq32.addItem(char)
        self.contq32.move(110, 280)
        self.contq32.setCurrentText(self.mission32)
        self.contq32.resize(120, 20)
        self.contq32.currentTextChanged.connect(self.combobox_changedct32)

        self.contq33 = QComboBox(self)
        for char in ucharl:
            self.contq33.addItem(char)
        self.contq33.move(110, 300)
        self.contq33.setCurrentText(self.mission33)
        self.contq33.resize(120, 20)
        self.contq33.currentTextChanged.connect(self.combobox_changedct33)

        label = QLabel('슬롯 수', self)
        label.move(110, 315)

        self.mnumq3 = QLineEdit(self)
        self.mnumq3.move(160, 320)
        self.mnumq3.setText(str(self.mnum3))
        self.mnumq3.resize(20, 20)
        self.mnumq3.textChanged[str].connect(self.onChangedmn3)

        # 미션4
        label = QLabel('미션4', self)
        label.move(250, 10)

        self.contq41 = QComboBox(self)
        for char in ucharl:
            self.contq41.addItem(char)
        self.contq41.move(250, 40)
        self.contq41.setCurrentText(self.mission41)
        self.contq41.resize(120, 20)
        self.contq41.currentTextChanged.connect(self.combobox_changedct41)

        self.contq42 = QComboBox(self)
        for char in ucharl:
            self.contq42.addItem(char)
        self.contq42.move(250, 60)
        self.contq42.setCurrentText(self.mission42)
        self.contq42.resize(120, 20)
        self.contq42.currentTextChanged.connect(self.combobox_changedct42)

        self.contq43 = QComboBox(self)
        for char in ucharl:
            self.contq43.addItem(char)
        self.contq43.move(250, 80)
        self.contq43.setCurrentText(self.mission43)
        self.contq43.resize(120, 20)
        self.contq43.currentTextChanged.connect(self.combobox_changedct43)

        label = QLabel('슬롯 수', self)
        label.move(250, 95)

        self.mnumq4 = QLineEdit(self)
        self.mnumq4.move(300, 100)
        self.mnumq4.setText(str(self.mnum4))
        self.mnumq4.resize(20, 20)
        self.mnumq4.textChanged[str].connect(self.onChangedmn4)

        # 미션5
        label = QLabel('미션5', self)
        label.move(250, 120)

        self.contq51 = QComboBox(self)
        for char in ucharl:
            self.contq51.addItem(char)
        self.contq51.move(250, 150)
        self.contq51.setCurrentText(self.mission51)
        self.contq51.resize(120, 20)
        self.contq51.currentTextChanged.connect(self.combobox_changedct51)

        self.contq52 = QComboBox(self)
        for char in ucharl:
            self.contq52.addItem(char)
        self.contq52.move(250, 170)
        self.contq52.setCurrentText(self.mission52)
        self.contq52.resize(120, 20)
        self.contq52.currentTextChanged.connect(self.combobox_changedct52)

        self.contq53 = QComboBox(self)
        for char in ucharl:
            self.contq53.addItem(char)
        self.contq53.move(250, 190)
        self.contq53.setCurrentText(self.mission53)
        self.contq53.resize(120, 20)
        self.contq53.currentTextChanged.connect(self.combobox_changedct53)

        label = QLabel('슬롯 수', self)
        label.move(250, 205)

        self.mnumq5 = QLineEdit(self)
        self.mnumq5.move(300, 210)
        self.mnumq5.setText(str(self.mnum5))
        self.mnumq5.resize(20, 20)
        self.mnumq5.textChanged[str].connect(self.onChangedmn5)

        button = QPushButton('시작', self)
        button.move(250, 280)
        button.resize(120, 20)
        button.clicked.connect(self.on_click)
        self.show()

    def onChangedhn1(self, text):
        if text != '':
            self.hnum1 = int(text)
        else:
            self.hnum1 = 0

    def onChangedhn2(self, text):
        if text != '':
            self.hnum2 = int(text)
        else:
            self.hnum2 = 0

    def onChangedhn3(self, text):
        if text != '':
            self.hnum3 = int(text)
        else:
            self.hnum3 = 0

    def onChangedhn4(self, text):
        if text != '':
            self.hnum4 = int(text)
        else:
            self.hnum4 = 0

    def onChangedhn5(self, text):
        if text != '':
            self.hnum5 = int(text)
        else:
            self.hnum5 = 0

    def onChangedhn6(self, text):
        if text != '':
            self.hnum6 = int(text)
        else:
            self.hnum6 = 0

    def onChangedhn7(self, text):
        if text != '':
            self.hnum7 = int(text)
        else:
            self.hnum7 = 0

    def onChangedhn8(self, text):
        if text != '':
            self.hnum8 = int(text)
        else:
            self.hnum8 = 0

    def onChangedhn9(self, text):
        if text != '':
            self.hnum9 = int(text)
        else:
            self.hnum9 = 0

    def onChangedhn10(self, text):
        if text != '':
            self.hnum10 = int(text)
        else:
            self.hnum10 = 0

    def onChangedhn11(self, text):
        if text != '':
            self.hnum11 = int(text)
        else:
            self.hnum11 = 0

    def onChangedhn12(self, text):
        if text != '':
            self.hnum12 = int(text)
        else:
            self.hnum12 = 0

    def combobox_changedct11(self, text):
        self.mission11 = text

    def combobox_changedct12(self, text):
        self.mission12 = text

    def combobox_changedct13(self, text):
        self.mission13 = text

    def combobox_changedct21(self, text):
        self.mission21 = text

    def combobox_changedct22(self, text):
        self.mission22 = text

    def combobox_changedct23(self, text):
        self.mission23 = text

    def combobox_changedct31(self, text):
        self.mission31 = text

    def combobox_changedct32(self, text):
        self.mission32 = text

    def combobox_changedct33(self, text):
        self.mission33 = text

    def combobox_changedct41(self, text):
        self.mission41 = text

    def combobox_changedct42(self, text):
        self.mission42 = text

    def combobox_changedct43(self, text):
        self.mission43 = text

    def combobox_changedct51(self, text):
        self.mission51 = text

    def combobox_changedct52(self, text):
        self.mission52 = text

    def combobox_changedct53(self, text):
        self.mission53 = text

    def onChangedmn1(self, text):
        if text != '':
            self.mnum1 = int(text)
        else:
            self.mnum1 = 0

    def onChangedmn2(self, text):
        if text != '':
            self.mnum2 = int(text)
        else:
            self.mnum2 = 0

    def onChangedmn3(self, text):
        if text != '':
            self.mnum3 = int(text)
        else:
            self.mnum3 = 0

    def onChangedmn4(self, text):
        if text != '':
            self.mnum4 = int(text)
        else:
            self.mnum4 = 0

    def onChangedmn5(self, text):
        if text != '':
            self.mnum5 = int(text)
        else:
            self.mnum5 = 0

    def on_click(self, parent):
        self.hnuml = [self.hnum1, self.hnum2, self.hnum3, self.hnum4, self.hnum5, self.hnum6,
                      self.hnum7, self.hnum8, self.hnum9, self.hnum10, self.hnum11, self.hnum12]

        self.missionl = [[self.mission11, self.mission12, self.mission13],
                         [self.mission21, self.mission22, self.mission23],
                         [self.mission31, self.mission32, self.mission33],
                         [self.mission41, self.mission42, self.mission43],
                         [self.mission51, self.mission52, self.mission53]]

        self.mnuml = [self.mnum1, self.mnum2, self.mnum3, self.mnum4, self.mnum5]
        config = configparser.ConfigParser()
        config.read('cfg.ini')
        config.set('hnuml', 'hnum1', str(self.hnum1))
        config.set('hnuml', 'hnum2', str(self.hnum2))
        config.set('hnuml', 'hnum3', str(self.hnum3))
        config.set('hnuml', 'hnum4', str(self.hnum4))
        config.set('hnuml', 'hnum5', str(self.hnum5))
        config.set('hnuml', 'hnum6', str(self.hnum6))
        config.set('hnuml', 'hnum7', str(self.hnum7))
        config.set('hnuml', 'hnum8', str(self.hnum8))
        config.set('hnuml', 'hnum9', str(self.hnum9))
        config.set('hnuml', 'hnum10', str(self.hnum10))
        config.set('hnuml', 'hnum11', str(self.hnum11))
        config.set('hnuml', 'hnum12', str(self.hnum12))
        config.set('missionl', 'mission11', self.mission11)
        config.set('missionl', 'mission12', self.mission12)
        config.set('missionl', 'mission13', self.mission13)
        config.set('missionl', 'mission21', self.mission21)
        config.set('missionl', 'mission22', self.mission22)
        config.set('missionl', 'mission23', self.mission23)
        config.set('missionl', 'mission31', self.mission31)
        config.set('missionl', 'mission32', self.mission32)
        config.set('missionl', 'mission33', self.mission33)
        config.set('missionl', 'mission41', self.mission41)
        config.set('missionl', 'mission42', self.mission42)
        config.set('missionl', 'mission43', self.mission43)
        config.set('missionl', 'mission51', self.mission51)
        config.set('missionl', 'mission52', self.mission52)
        config.set('missionl', 'mission53', self.mission53)
        config.set('mnuml', 'mnum1', str(self.mnum1))
        config.set('mnuml', 'mnum2', str(self.mnum2))
        config.set('mnuml', 'mnum3', str(self.mnum3))
        config.set('mnuml', 'mnum4', str(self.mnum4))
        config.set('mnuml', 'mnum5', str(self.mnum5))
        with open('cfg.ini', 'w') as configfile:
            config.write(configfile)

        herol = mhhd(self.hnuml)
        missionl = mhmd(self.missionl, self.mnuml)
        placel = mhprocess(herol, missionl)
        # print(placel)

        # print(2)
        maxdiffrl = placel
        # print(maxdiffrl)
        resultpll = []
        for placel in maxdiffrl:
            # print(placel)
            resultpl = [['1'], ['2'], ['3'], ['4'], ['5']]
            for place in placel:
                # print(place)
                resultpl[place[1]].append(place[0])
            resultpll.append(resultpl)
        # print(resultpll)
        placel = random.choice(resultpll)
        # print(placel)
        # print(' '.join(placel[0]))
        # self.label1.setText(txt)

        self.win2.update_label1(' '.join(placel[0]))
        self.win2.update_label2(' '.join(placel[1]))
        self.win2.update_label3(' '.join(placel[2]))
        self.win2.update_label4(' '.join(placel[3]))
        self.win2.update_label5(' '.join(placel[4]))

        self.win2.show()
        # self.window2.showresult()

class Window2(QMainWindow):

    def __init__(self, parent):
        super(Window2, self).__init__()
        self.setFixedSize(150, 150)
        self.setWindowIcon(QIcon(sys.argv[0]))
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # self.initUI()

        self.title = '결과'
        self.setWindowTitle(self.title)
        self.resize(300, 300)

        label1 = QLabel(self)
        label1.move(20, 20)
        label1.resize(200, 20)

        label2 = QLabel(self)
        label2.move(20, 40)
        label2.resize(200, 20)

        label3 = QLabel(self)
        label3.move(20, 60)
        label3.resize(200, 20)

        label4 = QLabel(self)
        label4.move(20, 80)
        label4.resize(200, 20)

        label5 = QLabel(self)
        label5.move(20, 100)
        label5.resize(200, 20)

        self.labell = [label1, label2, label3, label4, label5]

    def update_label1(self, txt):
        self.labell[0].setText(txt)

    def update_label2(self, txt):
        self.labell[1].setText(txt)

    def update_label3(self, txt):
        self.labell[2].setText(txt)

    def update_label4(self, txt):
        self.labell[3].setText(txt)

    def update_label5(self, txt):
        self.labell[4].setText(txt)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mhmain()
    sys.exit(app.exec_())