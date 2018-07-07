import sys
import os
import copy
import random
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import configparser
import functools

hnumlr = range(0, 12)

missionlr = range(0, 5)
mcharr = range(0, 3)

mnumlr = range(0, 5)

config = configparser.ConfigParser()

if not os.path.exists('cfg.ini'):
    config.add_section('hnuml')

    for i in hnumlr:
        config['hnuml']['hnum' + str(i)] = '0'
#
    config.add_section('missionl')

    for i in missionlr:
        for j in mcharr:
            config['missionl']['mission' + str(i) + str(j)] = ''

    config.add_section('mnuml')

    for i in mnumlr:
        config['mnuml']['mnum' + str(i)] = '0'

    with open('cfg.ini', 'w') as configfile:
        config.write(configfile)

def mhhd(hnuml = 0):
    if hnuml == 0:
        hnuml = []
        for i in hnumlr:
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

herol = mhhd()

charl = []
for hero in herol:
    for char in hero[0]:
        charl.append(char)
# print(charl)

chars = set(charl)
ucharl = list(chars)
ucharl.sort()
# print(self.ucharl)

class mhmain(QMainWindow):

    def __init__(self):

        config = configparser.ConfigParser()
        config.read('cfg.ini')

        self.hnuml = []
        for i in hnumlr:
            self.hnuml.append(int(config['hnuml']['hnum' + str(i)]))
        # print(hnuml)

        self.missionl = []
        for i in missionlr:
            self.missionl.append([])
            for j in mcharr:
                self.missionl[i].append(config['missionl']['mission' + str(i) + str(j)])
        # print(self.missionl)

        self.mnuml = []
        for i in mnumlr:
            self.mnuml.append(int(config['mnuml']['mnum' + str(i)]))
        # print(mnuml)

        super().__init__()
        self.title = '파르홀른 배치'
        self.left = 100
        self.top = 100
        self.width = 390
        self.height = 355
        self.setWindowIcon(QIcon(sys.argv[0]))
        self.cwinl = []
        for i in missionlr:
            self.cwinl.append(CWindow(QMainWindow))
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel("캐릭터 수", self)
        label.move(20, 10)

        ydist = 35

        for i in hnumlr:
            label = QLabel(herol[i][2], self)
            label.move(20, ydist)
            ydist += 25

        self.hnumql = []
        for i in hnumlr:
            self.hnumql.append(QLineEdit(self))

        ydist = 40
        for i in hnumlr:
            self.hnumql[i].move(70, ydist)
            self.hnumql[i].setText(str(self.hnuml[i]))
            self.hnumql[i].resize(20, 20)
            # self.hnumql[i].textChanged.connect(lambda: self.onChangedhn(i))
            ydist += 25

        missionbl = []
        for i in missionlr:
            missionbl.append(QPushButton('미션' + str(i + 1), self))
        # print(missionbl)

        xdist = 110
        ydist = 10
        for i in missionlr:
            if i == 3:
                xdist = 250
                ydist = 10
            missionbl[i].move(xdist, ydist)
            missionbl[i].clicked.connect(lambda: self.missionsetting(i))
            ydist += 110

        self.show()

    # def onChangedhn(self, i):
    #     if self.hnumql[i].text.isdigit():
    #         self.hnuml[i] = int(self.hnumql[i].text)
    #     else:
    #         self.hnuml[i] = 0

    def missionsetting(self, i):
        print(i)
        # midx = []
        # for mchar in self.missionl[i]:
        #     print(ucharl.index(mchar))
        #     midx.append(ucharl.index(mchar))
        #
        # for j in midx:
        #     self.cwinl[i].mcharql[j].toggle()

        self.cwinl[i].show()

class CWindow(QMainWindow):

    def __init__(self, parent):
        super(CWindow, self).__init__()
        self.setFixedSize(450, 430)
        self.setWindowIcon(QIcon(sys.argv[0]))
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # self.initUI()

        self.title = '특성 선택'
        self.setWindowTitle(self.title)
        self.resize(300, 300)
        self.initUI()

    def initUI(self):

        self.mcharql = []
        for uchar in ucharl:
            self.mcharql.append(QCheckBox(uchar, self))
        # print(self.mcharq)

        xdist = 20
        ydist = 15
        k = 1
        for i in range(len(self.mcharql)):
            if (i % 16 == 0) & (i != 0):
                xdist += 120
                ydist = 15

            self.mcharql[i].move(xdist, ydist)
            self.mcharql[i].resize(120, 20)
            # mcharq.toggle()
            # mcharq[i].stateChanged.connect(self.changeTitle)
            ydist += 25

        button = QPushButton('완료', self)
        button.move(250, 280)
        button.resize(120, 20)
        button.clicked.connect(self.csetting)

    def csetting(self):
        for mcharq in self.mcharql:
            print(mcharq.checkState())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mhmain()
    sys.exit(app.exec_())