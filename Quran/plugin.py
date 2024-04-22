#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

version = '2.1'

from Plugins.Plugin import PluginDescriptor
import os
from xml.etree.cElementTree import fromstring, ElementTree
from enigma import gFont, eTimer, eConsoleAppContainer, ePicLoad, loadPNG, getDesktop, eServiceReference, iPlayableService, eListboxPythonMultiContent, RT_HALIGN_LEFT, RT_HALIGN_RIGHT, RT_HALIGN_CENTER, RT_VALIGN_CENTER
from Screens.Screen import Screen
from Screens.ChoiceBox import ChoiceBox
from Screens.MessageBox import MessageBox
from Screens.InfoBarGenerics import InfoBarNotifications
from Components.Button import Button
from Components.Label import Label
from Components.ConfigList import ConfigListScreen
from Components.Sources.StaticText import StaticText
from Components.ActionMap import NumberActionMap, ActionMap
from Components.config import config, ConfigSelection, getConfigListEntry, ConfigText, ConfigDirectory, ConfigYesNo, ConfigSelection
from Components.FileList import FileList, FileEntryComponent
from Components.MenuList import MenuList
from Components.Pixmap import Pixmap, MovingPixmap
from Components.AVSwitch import AVSwitch
from Components.ServiceEventTracker import ServiceEventTracker
from Tools.LoadPixmap import LoadPixmap
from Tools.Directories import fileExists, resolveFilename, SCOPE_PLUGINS
PLUGIN_PATH = resolveFilename(SCOPE_PLUGINS, 'Extensions/Quran')
png = loadPNG('{:s}/icons/quran.png'.format(PLUGIN_PATH))
png1 = loadPNG('{:s}/icons/quran1.png'.format(PLUGIN_PATH))
wsize = getDesktop(0).size().width()
hsize = getDesktop(0).size().height()
dwidth = getDesktop(0).size().width()

class StreamtvCoran(Screen, InfoBarNotifications):
    PLAYER_IDLE = 0
    PLAYER_PLAYING = 1
    PLAYER_PAUSED = 2
    PLAYER_STOPS = 3

    def __init__(self, session, service, cbServiceCommand, chName, chURL, chIcon):
            Screen.__init__(self, session)
            InfoBarNotifications.__init__(self)
            if dwidth == 1280:
                PATH_IMAGE = '{:s}/icons/{:s}'.format(PLUGIN_PATH, chIcon)
                self.skin = '<screen name="StreamtvCoran" flags="wfNoBorder" position="0,0" size="1280,720" title="StreamtvCoran" backgroundColor="#41000000">  <widget source="session.CurrentService" render="Label" position="580,530" size="100,40" font="Regular;30" halign="right" valign="center" foregroundColor="#f4df8d" backgroundColor="#41000000" transparent="1">    <convert type="ServicePosition">Position</convert>  </widget>  <widget name="channel_icon" position="20,377" zPosition="-1" size="300,300" backgroundColor="#41000000" />  <widget name="channel_name" position="416,41" size="442,95" font="Regular;50" halign="center" valign="center" foregroundColor="#ffffff" backgroundColor="#41000000" transparent="1" />  <ePixmap position="559,600" size="180,32" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Quran/icons/M_Player.png" zPosition="1" transparent="1" alphatest="blend" />  <ePixmap position="-10,0" size="1280,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Quran/icons/player.png" zPosition="-1" transparent="1" alphatest="blend" />  <ePixmap position="20,377" size="300,300" pixmap="{:s}" zPosition="-1" transparent="1" alphatest="blend" />  <widget source="session.CurrentService" render="Progress" position="550,580" size="200,6" borderWidth="1" backgroundColor="blue">    <convert type="ServicePosition">Position</convert>  </widget></screen>'.format(PATH_IMAGE)
            elif dwidth == 1920:
                PATH_IMAGE = '{:s}/icons/{:s}'.format(PLUGIN_PATH, chIcon)
                self.skin = '<screen name="StreamtvCoran" flags="wfNoBorder" position="0,0" size="1920,1080" title="InfoBar" backgroundColor="#41000000">  <widget source="session.CurrentService" render="Label" position="919,815" size="100,40" font="Regular;30" halign="right" valign="center" foregroundColor="#f4df8d" backgroundColor="#41000000" transparent="1">    <convert type="ServicePosition">Position</convert>  </widget>  <widget name="channel_icon" position="28,686" zPosition="-1" size="300,300" backgroundColor="#41000000" />  <widget name="channel_name" position="643,66" size="656,136" font="Regular;50" halign="center" valign="center" foregroundColor="#ffffff" backgroundColor="#41000000" transparent="1" />  <ePixmap position="892,894" size="180,32" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Quran/icons/M_Player.png" zPosition="1" transparent="1" alphatest="blend" />  <ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Quran/icons/player44.png" zPosition="-1" transparent="1" alphatest="blend" />  <ePixmap position="28,686" size="300,300" pixmap="{:s}" zPosition="-1" transparent="1" alphatest="blend" />  <widget source="session.CurrentService" render="Progress" position="880,867" size="200,6" borderWidth="1" backgroundColor="blue">    <convert type="ServicePosition">Position</convert>  </widget></screen>'.format(PATH_IMAGE)
            else:
                PATH_IMAGE = '{:s}/icons/{:s}'.format(PLUGIN_PATH, chIcon)
                self.skin = '<screen name="StreamtvCoran" flags="wfNoBorder" position="0,0" size="2560,1440" title="القرأن الكريمé" backgroundColor="#41000000"><widget source="session.CurrentService" render="Label" position="center,1100" size="100,50" font="Regular;46" halign="right" valign="center" foregroundColor="#f4df8d" backgroundColor="#41000000" transparent="1"><convert type="ServicePosition">Position</convert></widget><widget name="channel_icon" position="28,686" zPosition="-1" size="300,300" backgroundColor="#41000000" /><widget name="channel_name" position="center,100" size="2560,136" font="Regular;50" halign="center" valign="center" foregroundColor="#ffffff" backgroundColor="#41000000" transparent="1" /><ePixmap size="380,132" position="center,1175" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Quran/icons/M_Player.png" zPosition="1" transparent="1" alphatest="blend" /><ePixmap position="0,0" size="2560,1440" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Quran/icons/player44.png" zPosition="-1" transparent="1" alphatest="blend" /><ePixmap position="28,686" size="500,500" pixmap="{:s}" zPosition="-1" transparent="1" alphatest="blend" /><widget source="session.CurrentService" render="Progress" position="center,1165" size="560,10" borderWidth="1" backgroundColor="blue"><convert type="ServicePosition">Position</convert></widget></screen>'.format(PATH_IMAGE)

            isEmpty = lambda x: x is None or len(x) == 0 or x == 'None'
            if isEmpty(chName):
                chName = 'Unknown'
            if isEmpty(chURL):
                chURL = 'Unknown'
            if isEmpty(chIcon):
                chIcon = 'default.png'
            chIcon = PATH_IMAGE
            self.session = session
            self.service = service
            self.cbServiceCommand = cbServiceCommand
            self['actions'] = ActionMap(['OkCancelActions',
                'InfobarSeekActions',
                'MediaPlayerActions',
                'MovieSelectionActions',
                'ColorActions'], {'yellow': self.dopauseService,
                'cancel': self.doExit,
                'stop': self.doExit,
                'blue': self.dostop,
                'green': self.playerservice,
                'red': self.dorepeter}, -2)
            self.__event_tracker = ServiceEventTracker(screen=self, eventmap={iPlayableService.evSeekableStatusChanged: self.__seekableStatusChanged,
                iPlayableService.evStart: self.__serviceStarted,
                iPlayableService.evEOF: self.__evEOF})
            self.hidetimer = eTimer()
            try: # Edit By OSTENDE For DreamOS
                self.hidetimer.timeout.get().append(self.doInfoAction)
            except:
                self.hidetimer_conn = self.hidetimer.timeout.connect(self.doInfoAction)
            self.state = self.PLAYER_PLAYING
            self.lastseekstate = self.PLAYER_PLAYING
            self.__seekableStatusChanged()
            self.onClose.append(self.__onClose)
            self.doPlay()
            self['channel_icon'] = Pixmap()
            self['channel_name'] = Label(chName)
            self['channel_uri'] = Label(chURL)
            self.picload = ePicLoad()
            self.scale = AVSwitch().getFramebufferScale()
            try: # Edit By OSTENDE For DreamOS
                self.picload.PictureData.get().append(self.cbDrawChannelIcon)
            except:
                self.picload_conn = self.picload.PictureData.connect(self.cbDrawChannelIcon)
            print(self.scale[0])
            print(self.scale[1])
            self.picload.setPara((300,
                300,
                self.scale[0],
                self.scale[1],
                False,
                0,
                '#00000000'))
            self.picload.startDecode(chIcon)
            self.bypassExit = False
            self.repeter = False
            self.stops = False
            self.cbServiceCommand(('docommand', self.doCommand))

    def doCommand(self, cmd):
        if cmd == 'bypass_exit':
            self.bypassExit = True

    def cbDrawChannelIcon(self, picInfo = None):
        ptr = self.picload.getData()
        if ptr != None:
            self['channel_icon'].instance.setPixmap(ptr.__deref__())
            self['channel_icon'].show()
        return

    def __onClose(self):
        self.session.nav.stopService()

    def __seekableStatusChanged(self):
        service = self.session.nav.getCurrentService()
        if service is not None:
            seek = service.seek()
            if seek is None or not seek.isCurrentlySeekable():
                self.setSeekState(self.PLAYER_PLAYING)
        return

    def __serviceStarted(self):
        self.state = self.PLAYER_PLAYING
        self.__seekableStatusChanged()

    def __evEOF(self):
        if self.bypassExit:
            return
        if self.repeter:
            self.state = self.PLAYER_PLAYING
            self.session.nav.stopService()
            self.session.nav.playService(self.service)
        else:
            self.state = self.PLAYER_STOPS

    def __setHideTimer(self):
        pass

    def doExit(self):
        self.cbServiceCommand()
        self.close()

    def cbDoExit(self, answer):
        answer = answer and answer[1]
        if answer == 'y':
            self.cbServiceCommand()
            self.close()

    def setSeekState(self, wantstate):
        service = self.session.nav.getCurrentService()
        if service is None:
            print ('No Service found')
            return
        else:
            pauseable = service.pause()
            if pauseable is not None:
                if wantstate == self.PLAYER_PAUSED:
                    pauseable.pause()
                    self.state = self.PLAYER_PAUSED
                    if not self.shown:
                        self.show()
                elif wantstate == self.PLAYER_PLAYING:
                    pauseable.unpause()
                    self.state = self.PLAYER_PLAYING
                    if self.shown:
                        self.__setHideTimer()
            else:
                self.state = self.PLAYER_PLAYING
            return

    def doInfoAction(self):
        if self.shown:
            self.show()
        else:
            self.show()
            if self.state == self.PLAYER_PLAYING:
                self.__setHideTimer()

    def doPlay(self):
        if self.state == self.PLAYER_PAUSED:
            if self.shown:
                self.__setHideTimer()
        self.state = self.PLAYER_PLAYING
        self.session.nav.playService(self.service)
        if self.shown:
            self.__setHideTimer()

    def dorepeter(self):
        self.repeter = True

    def dostop(self):
        self.stops = True
        self.repeter = False
        self.state = self.PLAYER_STOPS
        self.session.nav.stopService()

    def playerservice(self):
        if self.state == self.PLAYER_PAUSED:
            self.stops = False
            self.setSeekState(self.PLAYER_PLAYING)
        elif self.state == self.PLAYER_STOPS:
            self.state = self.PLAYER_PLAYING
            self.session.nav.stopService()
            self.doPlay()

    def dopauseService(self):
        if self.state == self.PLAYER_PLAYING:
            self.setSeekState(self.PLAYER_PAUSED)


class StreamURIParser:

    def __init__(self, xml):
        self.xml = xml

    def parseStreamList(self):
        tvlist = []
        im = 0
        tree = ElementTree()
        tree.parse(self.xml)
        for iptv in tree.findall('mp3'):
            n = str(iptv.findtext('name'))
            i = str(iptv.findtext('icon'))
            u = str(iptv.findtext('uri'))
            t = str(iptv.findtext('type'))
            im = im + 1
            tvlist.append({'name': n,
                'icon': i,
                'type': t,
                'uri': self.parseStreamURI(u),
                'img': str(im) + '.png'})

        return tvlist

    def parseStreamURI(self, uri):
        uriInfo = {}
        splitedURI = uri.split()
        uriInfo['URL'] = splitedURI[0]
        for x in splitedURI[1:]:
            i = x.find('=')
            uriInfo[x[:i].upper()] = str(x[i + 1:])

        return uriInfo


def streamListEntry(entry):
    uriInfo = entry[1].get('uri')
    png = loadPNG('{:s}/icons/{:s}'.format(PLUGIN_PATH, str(entry[1].get('icon'))))
    return [entry, (eListboxPythonMultiContent.TYPE_PIXMAP_ALPHATEST,
        580,
        2,
        85,
        85,
        png), (eListboxPythonMultiContent.TYPE_TEXT,
        200,
        15,
        300,
        50,
        0,
        RT_HALIGN_CENTER,
        entry[0])]


def streamListEntry1(entry):
    uriInfo = entry[1].get('uri')
    return [entry,
        (eListboxPythonMultiContent.TYPE_PIXMAP_ALPHATEST,
        442,
        2,
        223,
        85,
        png),
        (eListboxPythonMultiContent.TYPE_TEXT,
        200,
        15,
        300,
        50,
        0,
        RT_HALIGN_CENTER,
        entry[0]),
        (eListboxPythonMultiContent.TYPE_PIXMAP_ALPHATEST,
        5,
        2,
        223,
        85,
        png1)]


class StreamTVListCoran(Screen):
    skin = '\n\t\t<screen name="StreamTVListCoran" position="center,center" size="700,500" title="Quran karim V {:s}">\n\t\t      \xD8\xA7\xD9\x84\xD9\x82\xD8\xB1\xD8\xA2\xD9\x86 \xD8\xA7\xD9\x84\xD9\x85\xD8\xB1\xD8\xAA\xD9\x84">\n\t\t    <ePixmap position="0,0" size="700,130" pixmap="{:s}/icons/header.png" zPosition="-1" transparent="1" alphatest="blend" />\n\t\t\t<ePixmap position="300,1" size="128,128" pixmap="{:s}/icons/iquran.png" zPosition="-1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="streamlist" position="0,130" size="700,370" backgroundColor="#000000" zPosition="10" scrollbarMode="showOnDemand" />\n\t        </screen>\n\t\t'.format(version, PLUGIN_PATH, PLUGIN_PATH)

    def __init__(self, session):
        self.session = session
        Screen.__init__(self, session)
        self['actions'] = ActionMap(['OkCancelActions',
            'ShortcutActions',
            'WizardActions',
            'ColorActions',
            'SetupActions',
            'NumberActions',
            'MenuActions'], {'ok': self.keyOK,
            'cancel': self.keyCancel,
            'up': self.keyUp,
            'down': self.keyDown,
            'left': self.keyLeft,
            'right': self.keyRight}, -1)
        self.streamBin = resolveFilename(SCOPE_PLUGINS, 'Extensions/Quran/tilawat/rtmpdump')
        self.streamFile = resolveFilename(SCOPE_PLUGINS, 'Extensions/Quran/tilawat/kuraas.xml')
        self.streamList = []
        self.makeStreamList()
        self.streamMenuList = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)
        self.streamMenuList.l.setFont(0, gFont('Regular', 43))
        self.streamMenuList.l.setFont(1, gFont('Regular', 18))
        self.streamMenuList.l.setItemHeight(92)
        self['streamlist'] = self.streamMenuList
        self.streamMenuList.setList(list(map(streamListEntry, self.streamList)))
        self.onLayoutFinish.append(self.layoutFinished)
        self.rtmpConsole = None
        self.beforeService = None
        self.currentService = None
        self.playerStoped = False
        self.serviceDoCommand = None
        self.keyLocked = False
        return

    def layoutFinished(self):
        rc = os.popen('ps -ef | grep rtmpdump | grep -v grep').read()
        print ('a process already running :', rc)
        if rc is not None:
            if rc.strip() != '':
                os.system('killall -INT rtmpdump')
        return

    def keyLeft(self):
        if self.keyLocked:
            return
        self['streamlist'].pageUp()

    def keyRight(self):
        if self.keyLocked:
            return
        self['streamlist'].pageDown()

    def keyUp(self):
        if self.keyLocked:
            return
        self['streamlist'].up()

    def keyDown(self):
        if self.keyLocked:
            return
        self['streamlist'].down()

    def keyCancel(self):
        self.cbAppClosed(True)
        self.keyLocked = False
        self.close()

    def keyOK(self):
        if self.keyLocked:
            return
        streamInfo = self['streamlist'].getCurrent()[0][1]
        uriInfo = streamInfo.get('uri')
        imag = streamInfo.get('img')
        urls = uriInfo.get('URL')
        self.session.open(StreamTVList1, urls, imag)

    def doStreamAction(self, url = None, serviceType = '4097', bufferSize = None):
        if url is None:
            url = '/tmp/stream.avi'
            self.streamPlayerTimer.stop()
        try:
            serviceType = int(serviceType)
        except:
            serviceType = 4097

        try:
            bufferSize = int(bufferSize)
        except:
            bufferSize = None

        service = eServiceReference(serviceType, 0, url)
        streamInfo = self['streamlist'].getCurrent()[0][1]
        uriInfo = streamInfo.get('uri')
        self.beforeService = self.session.nav.getCurrentlyPlayingServiceReference()
        self.currentService = self.session.openWithCallback(self.cbFinishedStream, StreamtvCoran, service, cbServiceCommand=self.cbServiceCommand, chName=str(streamInfo.get('name')), chURL=str(uriInfo.get('URL')), chIcon=str(streamInfo.get('icon')))
        return

    def cbServiceCommand(self, params = None):
        if params is None:
            self.playerStoped = True
            return
        else:
            if params[0] == 'docommand':
                self.serviceDoCommand = params[1]
            return

    def cbAppClosed(self, ret):
        print(ret)
        self.doConsoleStop()
        if self.currentService is not None and not self.playerStoped:
            self.serviceDoCommand('bypass_exit')
            message = 'The connection was terminated from the stream server.'
            self.session.open(MessageBox, message, type=MessageBox.TYPE_INFO)
            self.currentService.close()
            self.currentService = None
            self.serviceDoCommand = None
        return

    def cbDataAvail(self, data):
        print (data)
        if str(data) == 'Connected...':
            self.streamPlayerTimer = eTimer()
            try: # Edit By OSTENDE For DreamOS
                self.streamPlayerTimer.timeout.get().append(self.doStreamAction)
            except:
                self.streamPlayerTime_conn = self.streamPlayerTimer.timeout.connect(self.doStreamAction)
            self.streamPlayerTimer.start(1000)

    def cbFinishedStream(self):
        self.doConsoleStop()
        self.session.nav.playService(self.beforeService)
        print ('player done!!')

    def doConsoleStop(self):
        self.keyLocked = False
        if self.rtmpConsole is not None:
            self.rtmpConsole.sendCtrlC()
            self.rtmpConsole = None
        return

    def makeCommand(self, uriInfo):

        def appendCommand(key, option):
            try:
                d = uriInfo.get(key)
                if d is not None:
                    return '-{:s} {:s} '.format(option, d)
            except:
                pass

            return ''

        command = '{:s} -v '.format(self.streamBin)
        command += appendCommand('URL', 'r')
        command += appendCommand('PLAYPATH', 'y')
        command += appendCommand('SWFURL', 'W')
        return command

    def makeStreamList(self):
        streamDB = StreamURIParser(self.streamFile).parseStreamList()
        self.streamList = []
        for x in streamDB:
            self.streamList.append((x.get('name'), x))


class StreamTVList1(Screen):
    skin = '\n\t\t<screen name="StreamTVList" position="center,center" size="700,500" title="Quran karim V {:s}">\n\t\t    <ePixmap position="0,0" size="700,130" pixmap="{:s}/icons/header.png" zPosition="-1" transparent="1" alphatest="blend" />\n\t\t\t<ePixmap position="300,1" size="128,128" pixmap="{:s}/icons/iquran.png" zPosition="-1" transparent="1" alphatest="blend" />\n\t\t\t<widget name="streamlist" position="0,130" size="700,370" backgroundColor="#000000" zPosition="10" scrollbarMode="showOnDemand" />\n\t        </screen>\n\t\t'.format(version, PLUGIN_PATH, PLUGIN_PATH)

    def __init__(self, session, urls, imag):
        self.session = session
        self.urls = urls
        self.imag = imag
        Screen.__init__(self, session)
        self['actions'] = ActionMap(['OkCancelActions',
            'ShortcutActions',
            'WizardActions',
            'ColorActions',
            'SetupActions',
            'NumberActions',
            'MenuActions'], {'ok': self.keyOK,
            'cancel': self.keyCancel,
            'up': self.keyUp,
            'down': self.keyDown,
            'left': self.keyLeft,
            'right': self.keyRight}, -1)
        self.streamFile = resolveFilename(SCOPE_PLUGINS, 'Extensions/Quran/tilawat/soura.xml')
        self.streamList = []
        self.makeStreamList()
        self.streamMenuList = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)
        self.streamMenuList.l.setFont(0, gFont('Regular', 43))
        self.streamMenuList.l.setFont(1, gFont('Regular', 18))
        self.streamMenuList.l.setItemHeight(92)
        self['streamlist'] = self.streamMenuList
        self.streamMenuList.setList(list(map(streamListEntry1, self.streamList)))
        self.onLayoutFinish.append(self.layoutFinished)
        self.rtmpConsole = None
        self.beforeService = None
        self.currentService = None
        self.playerStoped = False
        self.serviceDoCommand = None
        self.keyLocked = False
        return

    def layoutFinished(self):
        rc = os.popen('ps -ef | grep rtmpdump | grep -v grep').read()
        print ('a process already running :', rc)
        if rc is not None:
            if rc.strip() != '':
                os.system('killall -INT rtmpdump')
        return

    def keyLeft(self):
        if self.keyLocked:
            return
        self['streamlist'].pageUp()

    def keyRight(self):
        if self.keyLocked:
            return
        self['streamlist'].pageDown()

    def keyUp(self):
        if self.keyLocked:
            return
        self['streamlist'].up()

    def keyDown(self):
        if self.keyLocked:
            return
        self['streamlist'].down()

    def keyCancel(self):
        self.close()

    def keyOK(self):
        if self.keyLocked:
            return
        else:
            self.keyLocked = True
            self.rtmpConsole = None
            self.beforeService = None
            self.currentService = None
            self.playerStoped = False
            self.serviceDoCommand = None
            streamInfo = self['streamlist'].getCurrent()[0][1]
            uriInfo = streamInfo.get('uri')
            typeInfo = streamInfo.get('type').split(':')
            protocol = typeInfo[0]
            url = self.urls + uriInfo.get('URL')
            if protocol == 'rtmp':
                self.layoutFinished()
                self.rtmpConsole = eConsoleAppContainer()
                self.rtmpConsole.dataAvail.append(self.cbDataAvail)
                self.rtmpConsole.appClosed.append(self.cbAppClosed)
                self.rtmpConsole.execute(self.makeCommand(uriInfo))
            elif protocol in ('rtsp', 'http', 'hls'):
                serviceType = typeInfo[1]
                bufferSize = typeInfo[2]
                self.doStreamAction(url, serviceType, bufferSize)
            return

    def doStreamAction(self, url = None, serviceType = '4097', bufferSize = None):
        if url is None:
            url = '/tmp/stream.avi'
            self.streamPlayerTimer.stop()
        try:
            serviceType = int(serviceType)
        except:
            serviceType = 4097

        try:
            bufferSize = int(bufferSize)
        except:
            bufferSize = None

        service = eServiceReference(serviceType, 0, url)
        streamInfo = self['streamlist'].getCurrent()[0][1]
        uriInfo = streamInfo.get('uri')
        self.beforeService = self.session.nav.getCurrentlyPlayingServiceReference()
        self.currentService = self.session.openWithCallback(self.cbFinishedStream, StreamtvCoran, service, cbServiceCommand=self.cbServiceCommand, chName=str(streamInfo.get('name')), chURL=str(uriInfo.get('URL')), chIcon=str(self.imag))
        return

    def cbServiceCommand(self, params = None):
        if params is None:
            self.playerStoped = True
            return
        else:
            if params[0] == 'docommand':
                self.serviceDoCommand = params[1]
            return

    def cbAppClosed(self, ret):
        print (ret)
        self.doConsoleStop()
        if self.currentService is not None and not self.playerStoped:
            self.serviceDoCommand('bypass_exit')
            message = 'The connection was terminated from the stream server.'
            self.session.open(MessageBox, message, type=MessageBox.TYPE_INFO)
            self.currentService.close()
            self.currentService = None
            self.serviceDoCommand = None
        return

    def cbDataAvail(self, data):
        print (data)
        if str(data) == 'Connected...':
            self.streamPlayerTimer = eTimer()
            try: # Edit By OSTENDE For DreamOS
                self.streamPlayerTimer.timeout.get().append(self.doStreamAction)
            except:
                self.streamPlayerTime_conn = self.streamPlayerTimer.timeout.connect(self.doStreamAction)
            self.streamPlayerTimer.start(1000)

    def cbFinishedStream(self):
        self.doConsoleStop()
        self.session.nav.playService(self.beforeService)
        print ('player done!!')

    def doConsoleStop(self):
        self.keyLocked = False
        if self.rtmpConsole is not None:
            self.rtmpConsole.sendCtrlC()
            self.rtmpConsole = None
        return

    def makeCommand(self, uriInfo):

        def appendCommand(key, option):
            try:
                d = uriInfo.get(key)
                if d is not None:
                    return '-{:s} {:s} '.format(option, d)
            except:
                pass

            return ''

        command = '{:s} -v '.format(self.streamBin)
        command += appendCommand('URL', 'r')
        command += appendCommand('PLAYPATH', 'y')
        command += appendCommand('SWFURL', 'W')
        return command

    def makeStreamList(self):
        streamDB = StreamURIParser(self.streamFile).parseStreamList()
        self.streamList = []
        for x in streamDB:
            self.streamList.append((x.get('name'), x))


def main(session, **kwargs):
    session.open(StreamTVListCoran)


def Plugins(**kwargs):
    return PluginDescriptor(name=_('Quran Karim'), description='Quran Karim v {:s}'.format(version), where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main, icon='Quran.png')
