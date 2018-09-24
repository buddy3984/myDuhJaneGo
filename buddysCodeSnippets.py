### GET VITRTUAL ENVIRMENT RUNNING
install homebrew
install pip3
pip3 install virtualenv
virtualenv buddyPython
source bin/activate
pip install django

### DJNAGO CODE
django-admin startproject website
python manage.py startapp buddy
python manage.py migrate
python manage.py makemigrations buddy
python manage.py migrate

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
### MY TERMINAL CODES

mkdir -p parentdir/childdir/etc
rm -R Archives
#find what directory im in
pwd
#rename folder or directory
mv spooge website
ssh pi@192.168.1.44
source bin/activate
python manage.py runserver 192.168.1.44:8000
#terminal for file exploer finder fuse os x
sshfs pi@192.168.1.44: raspberryPi

### VIM COMMANDS
move to end of the line · A
move to beginning of the next line · o
move to the beginning of current line · 0
move to the beginning of previous line · O
shift bocks of code · shift > then . to repeat
paste on current line · Vp
sort hightlighted text · : then just type sort
in nerdtree open file in split view: hightlight file · s
see hidden files in neard tree · shift i
select text to copy in vim: first hide numbers · :set nonu · command r or fn key
return bring back numbers · :set nu
paste cyle through history · cntrl p or cntrl n
go to top of file · gg
bottome of file · shift g
go to any line· number then gg
search · / then n for next
search backwards · ? then n for next
highlight word and find in file · *
search and replace all · :%s/first/second
search and replace prompt first · :%s/first/second/gc
ignore case in search · \c
switch windows · hold ctrl + ww
switch tabs · gt
close all · :qa
refresh nerdtree · r
select all · ggVG
comment muliple lines · ctrl v then arrow the lines , I, #, esc
uncomment muliple lines · ctrl v then arrow the lines , x

### HTML SNIPPETS
<a href="#">title</a>'
<form action="/action_page.php">


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
buddys github code snippets
### GIT HUB STUFFS
git init
git remote add orgin https://github.com/buddy3984/codeSnips.git
git remote -v
git add .
git commit -m "buddysCode"
git push orgin master
git status
git add buddysCodeSnippets.py
another change

git add.
git commit -m

git commit -am "004"
https://github.com/buddy3984/codeSnips.git
hey it worked!!!
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
++++++++++++++++++
+ MY BUDDY CALL CODE +
++++++++++++++++++
### ADD THIS ###
self.buddy = self.get_app("buddyapp")
###          ###
self.buddy.googlealert("poo buddy")
self.buddy.poweronalertthentriggeralertinhowmanyseconds("hello there", 3)

# # # # # # # # # # # # # # # # # DJANGO CODE # # # # # # # # # # # # # # # # # # # # # #
from django.http import HttpResponse
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    html = ''
    for i in all_albums:
        url = '/buddy/' + i.artist
        html += '<a href="' + url + '">' + i.album_title + '</a><br>'
    return HttpResponse(html)


def detail(request, var_from_main_url):
    return HttpResponse("<h2>details for the album shite!!   " + var_from_main_url + "</h2>")


from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<var_from_main_url>[^$]+)$', views.detail, name='detail'),
]

from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=300)
    album_title = models.CharField(max_length=3000)
    genre = models.CharField(max_length=300)
    album_logo = models.CharField(max_length=3000)

    def __str__(self):
        return self.artist + ' · ' + self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=300)
    song_title = models.CharField(max_length=300)
# # # # # # # # # # # # # # # # # DJANGO CODE # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
++++++++++++++++++
+ MY CODE BLOCKS +
++++++++++++++++++
and datetime.date.today().weekday() in [0, 1, 2, 3, 4]:
self.call_service("remote/send_command", entity_id = remote, device = remotedevice, command = remotecommand, num_repeats = remoterepeats)
self.speakalert = self.run_in(self.buddy.googlealert("poo buddy"), 0)
self.args['shutofftime'] = self.datetime() + timedelta(seconds=+72)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
STRAIGHT UP PYTHON CODE SNPPETS
import turtle
t = turtle.Turtle()



def pussy(n, y):
    x = 0
    while x < 5:
        t.forward(n)
        t.right(n) 
        x += 1
    return print('fuck yea')

for i in range(1):
    pussy(90, 59)

###



sex = 'go-uck-a-duck-bitch'
print(sex.split('-'))
fuck = sex.split('-')
spooge = sex[::-1]
cock = fuck[::-1]
print(spooge)
print(cock)




###

def sum(list):
    count = 0
    for x in list:
        count = count + x 
    return count

assert sum([1, 3, 1]) == 5

###

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import timedelta
from requests import get
import datetime
class buddy(hass.Hass):
    
    def initialize(self):
        
        ### VARIABLES
        self.didgoogleplay = datetime.datetime(2010, 12, 12, 12, 12, 12)
        self.runoncegoogle = datetime.datetime(2010, 12, 12, 12, 12, 12)
        self.alerttimer = datetime.datetime(2010, 12, 12, 12, 12, 12)
        self.mediaplayerturnedon = datetime.datetime(2010, 12, 12, 12, 12, 12)
        self.heytimer = datetime.datetime(2010, 12, 12, 12, 12, 12)
        self.googlealertarray = []
        pass
    
    
    
    def googlealert(self, kwargs):
        if  self.alerttimer < self.datetime():
            self.alerttimer = self.datetime() + timedelta(seconds=+6)
            self.run_in(self.googlesayit, self.googlealertarray[1])
    
    
    
    def checkit(self, kwargs):
        if  len(self.googlealertarray) > 0:
            self.run_in(self.googlesayit, self.googlealertarray[1])
    
    
    
    def googlesayit(self, kwargs):
        self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = self.googlealertarray[0], language= "en-au")
        count = 0
        while self.get_state('media_player.buddyalerts') != "playing":
            count += 1
        if  self.googlealertarray[0] != " ":
            self.log('loading count to play alert was {}'.format(count))
            self.log('goolge just said: "{}"'.format(self.googlealertarray[0]))
        self.googlealertarray.remove(self.googlealertarray[0])
        self.googlealertarray.remove(self.googlealertarray[0])
        self.run_in(self.checkit, 6)
    
    
    
    def poweronalertthentriggeralertinhowmanyseconds(self, alertmessage, time):
        if  self.anyone_home() == True:
            if  self.get_state("media_player.buddyalerts") == "off":
                if  self.heytimer < self.datetime():
                    self.heytimer = self.datetime() + timedelta(seconds=+300)
                    self.googlealertarray.append(" ")
                    self.googlealertarray.append(0)
                self.googlealertarray.append(alertmessage)
                self.googlealertarray.append(time)
                if  self.mediaplayerturnedon < self.datetime():
                    self.mediaplayerturnedon = self.datetime() + timedelta(seconds=+3)
                    self.googlealert(self)
            else:
                self.googlealertarray.append(alertmessage)
                self.googlealertarray.append(time)
                if  self.mediaplayerturnedon < self.datetime():
                    self.mediaplayerturnedon = self.datetime() + timedelta(seconds=+3)
                    self.googlealert(self)
    
    
    
    
    ### SEND URL
    def sendurl(self, sendurllink, sendurllinktimer):
        if  sendurllinktimer == 0:
            url = '{}'.format(sendurllink)
            headers = {'x-ha-access': '7410zz00','content-type': 'application/json'}
            response = get(url, headers=headers)
            sex = str(response.text)
            if  sex.find("profile=") == 13:
                num = sex.find("profile=")
                self.log("blue iris has been changed to {}".format(sex[num:num+9]))
            else:
                dick = sex.find('"result":"')
                self.log("sent to smartthings for message alerts on {} status".format(sex[dick+9:dick+13]))
        else:
            self.runtwo = self.run_in(self.sendurltimerfunc, sendurllinktimer, sendurllink = sendurllink )
    
    
    
    ### SEND URL TIMER FUNC
    def sendurltimerfunc(self, kwargs):
            url = '{}'.format(kwargs['sendurllink'])
            headers = {'x-ha-access': '7410zz00','content-type': 'application/json'}
            response = get(url, headers=headers)
            sex = str(response.text)
            if  sex.find("profile=") == 13:
                num = sex.find("profile=")
                self.log("blue iris has been changed to {}".format(sex[num:num+9]))
            else:
                dick = sex.find('"result":"')
                self.log("sent to smartthings for message alerts on {} status".format(sex[dick+9:dick+13]))
            
            
            
            
            
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import timedelta
import datetime


### CLASS ###
class streamcamerastotvs(hass.Hass):
    def initialize(self):
        
        
    ### VAIRABLES
        self.runhandlearray = []
        return
    
    
    
    def streamblueiristotvs(self, onwhat, where, player, remote, remoteid, hdmi):
        if  self.anyone_home() ==True\
            and self.get_state(onwhat) == "off":
            self.args['turnoffplayer'] = self.datetime() + timedelta(seconds=+69)
            self.args['shutofftime'] = self.datetime() + timedelta(seconds=+72)
            if  len(self.runhandlearray) >= 4:
                self.removeshitfromthearray(self)
            self.putalertvideouponroomtv(where, player)
            one = self.run_at(self.turnoffmediaplayer, self.args['turnoffplayer'], fuk = player, poop = onwhat, remote = remote, remoteid = remoteid, hdmi = hdmi)
            self.runhandlearray.append(one)
            two = self.run_at(self.turnofftvtimer, self.args['shutofftime'], remote = remote, remoteid = remoteid)
            self.runhandlearray.append(two)
            if  remote == "remote.bedroom":
                self.runsix = self.run_in(self.bedroomtvhdmionewhenoff, 3, hdmi = "InputHdmi3")
        else:
            if  self.anyone_home() ==True\
                and self.now_is_between("06:33:33", "09:33:33") == False\
                and self.now_is_between("20:01:00", "21:00:00") == False:
                self.args['turnoffplayer'] = self.datetime() + timedelta(seconds=+33)
                if  len(self.runhandlearray) >= 4:
                    self.removeshitfromthearray(self)
                if  self.get_state(onwhat) != "paused":
                    self.controlchromcast("media_player/media_play_pause", onwhat)
                self.args['numplaying'] += 1
                self.putalertvideouponroomtv(where, player)
                three = self.run_at(self.turnoffmediaplayer, self.args['turnoffplayer'], fuk = player, poop = onwhat, remote = remote, remoteid = remoteid, hdmi = hdmi)
                self.runhandlearray.append(three)
                four = self.run_at(self.setnumplay, self.args['turnoffplayer'])
                self.runhandlearray.append(four)
    
    
    
    def setnumplay(self, kwargs): 
        self.args['numplaying'] = 0
    
    
    
    def removeshitfromthearray(self, kwargs):
        self.cancel_timer(self.runhandlearray[0])
        self.runhandlearray.remove(self.runhandlearray[0])
        if  len(self.runhandlearray) > 2:
            self.removeshitfromthearray(self)
    
    
    
    def turnoffmediaplayer(self, kwargs):
        player = kwargs['fuk']
        self.call_service("media_player/turn_off", entity_id = player)
        self.log("turn N off {}".format(player[13:99].upper()))
        if  self.get_state(kwargs['poop']) == "paused":
            self.controltv(kwargs['remote'], kwargs['remoteid'], kwargs['hdmi'], "1")
            self.log('back to hdmi1 and resuming show on {}'.format(player[25:99]))
            self.runfour = self.run_in(self.tvbacktohdmione, 3, spooge = kwargs['poop'])
    
    
    
    def tvbacktohdmione(self, kwargs):
        self.controlchromcast("media_player/media_play_pause", kwargs['spooge'])
    
    
    
    def turnofftvtimer(self, kwargs):
        self.controltv(kwargs['remote'], kwargs['remoteid'], "PowerToggle", "2")
        self.log('turned off {} tv'.format(kwargs['remote'][7:99]))
    
    
    def controltv(self, remote, remotedevice, remotecommand, remoterepeats):
        self.call_service("remote/send_command", entity_id = remote, device = remotedevice, command = remotecommand, num_repeats = remoterepeats)
    
    
    
    def controlchromcast(self, service, entity,):
        self.call_service(service, entity_id = entity)
    
    
    
    ### PUT UP VIDEO ALERT ON A ROOM TV ###
    def putalertvideouponroomtv(self, where, player):
        self.call_service("media_player/play_media", entity_id = player, media_content_id = "http://192.168.1.230:81/mjpg/{}/video.mjpg".format(where), media_content_type = "image/jpg")
        count = 0
        while self.get_state(player) != "paused":
            count += 1
        self.log('loading count to play was {}. gonna shut it down at {}'.format(count, self.args['shutofftime']))
        self.log("goolge just played {} camera on {}".format(where.upper(), player[13:99].upper()))
    
    
    
    def bedroomtvhdmionewhenoff(self, kwargs):
            self.controltv("remote.bedroom", "48480156", kwargs['hdmi'], "1")
            self.log("switch bedroom tv to hdmi3")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import timedelta
from requests import get
import datetime
import time

class backyardlights(hass.Hass):
    def initialize(self):
        
        #VARIABLES
        self.run_at_sunrise(self.tuningoffbackyardlightsmorning, offset = -9999)
        self.x = 0
        self.buddytimer = datetime.datetime(2010, 12, 12, 12, 12, 12)
        self.offlogphrase = ""
        self.lightentities = ['light.ge_zw7101_smart_led_light_bulb_ze26i_level', 'light.ge_zw7101_smart_led_light_bulb_ze26i_level_5',
                              'light.ge_zw7101_smart_led_light_bulb_ze26i_level_2', 'light.ge_zw7101_smart_led_light_bulb_ze26i_level_3',
                              'light.ge_zw7101_smart_led_light_bulb_ze26i_level_4', 'switch.aeotec_zw140_dual_nano_switch_switch_3',
                              'switch.zooz_zen15_power_switch_switch_2']
        
        ###  TRIGGERS
        self.listen_state(self.turnonbackyyardlights, "binary_sensor.ecolink_doorwindow_sensor_sensor", new= "on")
        self.listen_state(self.turnonbackyyardlights, "binary_sensor.ecolink_doorwindow_sensor_sensor_5", new= "on")
        self.listen_state(self.turnonbackyyardlights, "binary_sensor.ecolink_doorwindow_sensor_sensor_6", new= "on")
        self.listen_state(self.turnonbackyyardlights, "binary_sensor.ecolink_doorwindow_sensor_sensor_2", new= "on")
        self.listen_state(self.turnoffbackyyardlights, "binary_sensor.ecolink_doorwindow_sensor_sensor", new= "off")
        self.listen_state(self.turnoffbackyyardlights, "binary_sensor.ecolink_doorwindow_sensor_sensor_2", new= "off")
        self.listen_state(self.turnoffbackyyardlights, "binary_sensor.ecolink_doorwindow_sensor_sensor_5", new= "off")
        self.listen_state(self.turnoffbackyyardlights, "binary_sensor.ecolink_doorwindow_sensor_sensor_6", new= "off")
    
    
    
    def turnonbackyyardlights(self, entity, attribute, old, new, kwargs):
        if  self.buddytimer < self.datetime():
            self.offlogphrase = "gonna try to turn these light off"
        else:
            try:
                self.cancel_timer(self.newbuddycounddown)
                self.offlogphrase = "tried to turn em off but interupted! trying again"
            except:
                self.log("no timer running", level = "DEBUG")
        
        if  self.now_is_between("sunset - 00:33:33", "sunrise - 00:33:33") == True\
            and self.buddytimer < self.datetime()\
            and self.get_state("light.ge_zw7101_smart_led_light_bulb_ze26i_level") == "off":
            self.buddytimer = self.datetime() + timedelta(hours=+3)
            #turn on my backyard lights!
            self.x = 0
            self.turnonlightarray(self)
            self.log("yo bitch the backyard lights are on now!")
    
    
    
    def turnonlightarray(self, kwargs):
        self.turn_on(self.lightentities[self.x])
        if  self.x < 6:
            self.x += 1
            self.run_in(self.turnonlightarray, 0)
    
    
    
    def turnofflightarray(self, kwargs):
        self.turn_off(self.lightentities[self.x])
        if  self.x < 6:
            self.x += 1
            self.run_in(self.turnofflightarray, 0)
    
    
    
    def turnoffbackyyardlights(self, entity, attribute, old, new, kwargs):
        if  self.get_state("light.ge_zw7101_smart_led_light_bulb_ze26i_level") == "on"\
            and self.get_state("binary_sensor.ecolink_doorwindow_sensor_sensor") == "off"\
            and self.get_state("binary_sensor.ecolink_doorwindow_sensor_sensor_5") == "off"\
            and self.get_state("binary_sensor.ecolink_doorwindow_sensor_sensor_6") == "on"\
            and self.get_state("binary_sensor.ecolink_doorwindow_sensor_sensor_2") == "on":
            self.buddytimer = self.datetime() + timedelta(seconds=+33)
            self.newbuddycounddown = self.run_at(self.turnemoffin33seconds, self.buddytimer)
            self.log("{} in 33 seconds".format(self.offlogphrase))
    
    
    
    
    def turnemoffin33seconds(self, kwargs):
        #turn off my backyard lights!
        self.x = 0
        self.turnofflightarray(self)
        self.log("okay fuck face the backyard lights are 0FF now!")
    
    
    
    def tuningoffbackyardlightsmorning(self, kwargs):
        if  self.get_state("light.ge_zw7101_smart_led_light_bulb_ze26i_level") == "on":
            #turn off my backyard lights!
            self.x = 0
            self.turnofflightarray(self)
            self.log("okok it's now morning so shutting off backyard lights")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import timedelta
import datetime


### CLASS ###
class streamcamerastotvs(hass.Hass):
    def initialize(self):
        
        
    ### VAIRABLES
        self.runhandlearray = []
        return
    
    
    
    def streamblueiristotvs(self, onwhat, where, player, remote, remoteid, hdmi):
        if  self.anyone_home() ==True\
            and self.get_state(onwhat) == "off":
            self.args['turnoffplayer'] = self.datetime() + timedelta(seconds=+69)
            self.args['shutofftime'] = self.datetime() + timedelta(seconds=+72)
            if  len(self.runhandlearray) >= 4:
                self.removeshitfromthearray(self)
            self.putalertvideouponroomtv(where, player)
            one = self.run_at(self.turnoffmediaplayer, self.args['turnoffplayer'], fuk = player, poop = onwhat, remote = remote, remoteid = remoteid, hdmi = hdmi)
            self.runhandlearray.append(one)
            two = self.run_at(self.turnofftvtimer, self.args['shutofftime'], remote = remote, remoteid = remoteid)
            self.runhandlearray.append(two)
            if  remote == "remote.bedroom":
                self.runsix = self.run_in(self.bedroomtvhdmionewhenoff, 6)
        else:
            if  self.anyone_home() ==True:
                self.args['turnoffplayer'] = self.datetime() + timedelta(seconds=+33)
                self.controlchromcast("media_player/media_play_pause", onwhat)
                self.putalertvideouponroomtv(where, player)
                three = self.run_at(self.turnoffmediaplayer, self.args['turnoffplayer'], fuk = player, poop = onwhat, remote = remote, remoteid = remoteid, hdmi = hdmi)
                self.runhandlearray.append(three)
    
    
    
    def removeshitfromthearray(self, kwargs):
        self.cancel_timer(self.runhandlearray[0])
        self.runhandlearray.remove(self.runhandlearray[0])
        if  len(self.runhandlearray) > 2:
            self.removeshitfromthearray(self)
    
    
    
    def turnoffmediaplayer(self, kwargs):
        player = kwargs['fuk']
        self.call_service("media_player/turn_off", entity_id = player)
        self.log("turn N off {}".format(player[13:99].upper()))
        if  self.get_state(kwargs['poop']) == "paused":
            self.controltv(kwargs['remote'], kwargs['remoteid'], kwargs['hdmi'], "1")
            self.log('back to hdmi1 and resuming show on {}'.format(player[25:99]))
            self.runfour = self.run_in(self.tvbacktohdmione, 3, spooge = kwargs['poop'])
    
    
    
    def tvbacktohdmione(self, kwargs):
        self.controlchromcast("media_player/media_play_pause", kwargs['spooge'])
    
    
    
    def turnofftvtimer(self, kwargs):
        self.controltv(kwargs['remote'], kwargs['remoteid'], "PowerToggle", "1")
        self.log('turned off {} tv'.format(kwargs['remote'][7:99]))
    
    
    def controltv(self, remote, remotedevice, remotecommand, remoterepeats):
        self.call_service("remote/send_command", entity_id = remote, device = remotedevice, command = remotecommand, num_repeats = remoterepeats)
    
    
    
    def controlchromcast(self, service, entity,):
        self.call_service(service, entity_id = entity)
    
    
    
    ### PUT UP VIDEO ALERT ON A ROOM TV ###
    def putalertvideouponroomtv(self, where, player):
        self.call_service("media_player/play_media", entity_id = player, media_content_id = "http://192.168.1.230:81/mjpg/{}/video.mjpg".format(where), media_content_type = "image/jpg")
        count = 0
        while self.get_state(player) != "paused":
            count += 1
        self.log('loading count to play was {}. gonna shut it down at {}'.format(count, self.args['shutofftime']))
        self.log("goolge just played {} camera on {}".format(where.upper(), player[13:99].upper()))


    
    
    
    def bedroomtvhdmionewhenoff(self, kwargs):
            self.controltv("remote.bedroom", "48480156", "InputHdmi3", "1")
            self.log("switch bedroom tv to hdmi3")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import timedelta
import datetime

### CLASS ###
class streamcamerastotvs(hass.Hass):
    def initialize(self):
        self.didgoogleplay = datetime.datetime(2010, 12, 12, 12, 12, 12)
        return
    
    
    
    def streamblueiristotvs(self, onwhat, where, player, remote, remoteid, hdmi):
        if  self.anyone_home() ==True\
            and self.get_state(onwhat) == "off":
            self.putalertvideouponroomtv(where, player)
            self.runone = self.run_in(self.turnoffmediaplayer, 69, fuk = player, poop = onwhat, remote = remote, remoteid = remoteid, hdmi = hdmi)
            self.runtwo = self.run_in(self.turnofftvtimer, 72, remote = remote, remoteid = remoteid)
        else:
            if  self.anyone_home() ==True:
                self.controlchromcast("media_player/media_play_pause", onwhat)
                self.putalertvideouponroomtv(where, player)
                self.runthree = self.run_in(self.turnoffmediaplayer, 33, fuk = player, poop = onwhat, remote = remote, remoteid = remoteid, hdmi = hdmi)
    
    
    
    def turnoffmediaplayer(self, kwargs):
        player = kwargs['fuk']
        self.call_service("media_player/turn_off", entity_id = player)
        self.log("turn N off {}".format(player[13:99].upper()))
        if  self.get_state(kwargs['poop']) == "paused":
            self.controltv(kwargs['remote'], kwargs['remoteid'], kwargs['hdmi'], "1")
            self.log('back to hdmi1 and resuming show on {}'.format(player[25:99]))
            self.runfour = self.run_in(self.tvbacktohdmione, 3, spooge = kwargs['poop'])
    
    
    
    def tvbacktohdmione(self, kwargs):
        self.controlchromcast("media_player/media_play_pause", kwargs['spooge'])
    
    
    
    def turnofftvtimer(self, kwargs):
        self.controltv(kwargs['remote'], kwargs['remoteid'], "PowerToggle", "1")
        self.log('turned off {} tv'.format(kwargs['remote'][7:99]))
    
    
    def controltv(self, remote, remotedevice, remotecommand, remoterepeats):
        self.call_service("remote/send_command", entity_id = remote, device = remotedevice, command = remotecommand, num_repeats = remoterepeats)
    
    
    
    def controlchromcast(self, service, entity,):
        self.call_service(service, entity_id = entity)
    
    
    
    ### PUT UP VIDEO ALERT ON A ROOM TV ###
    def putalertvideouponroomtv(self, where, player):
        self.cancellistenervideo = self.listen_state(self.listeningforplayingvideo, player, new= "paused", where = where, player = player)
        self.call_service("media_player/play_media", entity_id = player, media_content_id = "http://192.168.1.230:81/mjpg/{}/video.mjpg".format(where), media_content_type = "image/jpg")
    
    
    
    ### PUT UP VIDEO ALERT ON A ROOM TV ###
    def listeningforplayingvideo(self, entity, attribute, old, new, kwargs):
        self.log('goolge just played {} camera on {}'.format(kwargs['where'].upper(), kwargs['player'][13:99].upper()))
        if  self.didgoogleplay < self.datetime():
            self.didgoogleplay = self.datetime() + timedelta(seconds=+99)
            self.runfive = self.run_at(self.runcanceltimer, self.didgoogleplay)
    
    
    
    def runcanceltimer(self, kwargs):
        self.cancel_listen_state(self.cancellistenervideo)
        self.log('"did google play video alert" listener just canceled')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        self.fruits = ['banana', 'apple',  'mango', 'shit', 'fuck', 'ballz']
        self.fruits.append('cunt')
        self.log('starts with {}'.format(self.fruits))
        self.sex(self)
    
    
    
    def sex(self, kwargs):
        self.fruits.remove(self.fruits[len(self.fruits)-1])
        self.log('this is now {}'.format(self.fruits))
        if  len(self.fruits) > 2:
            self.sex(self)
            
            
            
        self.fruits = ['banana', 'apple',  'mango', 'shit', 'fuck', 'ballz']
        self.fruits.append('cunt')
        self.log('starts with {}'.format(self.fruits))
        self.sex(self)
    
    
    
    def sex(self, kwargs):
        self.fruits.remove(self.fruits[0])
        self.log('this is now {}'.format(self.fruits))
        if  len(self.fruits) > 2:
            self.sex(self)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    ### PUT UP VIDEO ALERT ON A ROOM TV ###
    def putalertvideouponroomtv(self, where, player):
        x = self.listen_state(self.listeningforplayingvideo, player, new= "paused", where = where, player = player)
        self.playvideolisterhandle.append(x)
        self.call_service("media_player/play_media", entity_id = player, media_content_id = "http://192.168.1.230:81/mjpg/{}/video.mjpg".format(where), media_content_type = "image/jpg")
    
    
    
    ### PUT UP VIDEO ALERT ON A ROOM TV ###
    def listeningforplayingvideo(self, entity, attribute, old, new, kwargs):
        self.log("the lister handle now has a value of {}".format(self.playvideolisterhandle[0]), level = "DEBUG")
        self.log("goolge just played {} camera on {}".format(kwargs['where'].upper(), kwargs['player'][13:99].upper()))
        self.cancel_listen_state(self.playvideolisterhandle[0])
        self.playvideolisterhandle.remove(self.playvideolisterhandle[0])
        self.log("canceled listen timer")
        #self.log("this is whats in your array {}".format(self.playvideolisterhandle))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    ### PUT UP VIDEO ALERT ON A ROOM TV ###
    def putalertvideouponroomtv(self, where, player):
        x = ""
        x = self.listen_state(self.listeningforplayingvideo, player, new= "paused", where = where, player = player)
        #self.playvideolisterhandle.append(x)
        self.call_service("media_player/play_media", entity_id = player, media_content_id = "http://192.168.1.230:81/mjpg/{}/video.mjpg".format(where), media_content_type = "image/jpg")
        self.log("the lister handle now has a value of {}".format(x))
        self.canceldatlistener(x, player)
    
    
    
    ### PUT UP VIDEO ALERT ON A ROOM TV ###
    def listeningforplayingvideo(self, entity, attribute, old, new, kwargs):
        self.log("goolge just played {} camera on {}".format(kwargs['where'].upper(), kwargs['player'][13:99].upper()))
    
    
    
    def canceldatlistener(self, handler, player):
        self.cancel_listen_state(handler)
        #self.playvideolisterhandle.remove(handler)
        self.log("this is whats in your array {}".format(handler))
        self.log("canceled listen timer for {}".format(player[13:99].upper()))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        if  self.playvideolisterhandle in [1]:
            self.log('this shit fired')
            ### VAIABLE
            count = 0
            ### LOOP
            while (count < 33):
                count += 1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #self.log(self.shit)
        self.xx = self.listen_state(self.listeningforplayingvideo, "input_boolean.amother_test", new= "on")
        #self.shit.append(x)
        self.set_state("input_boolean.amother_test", state = "on")
    
    ### PUT UP VIDEO ALERT ON A ROOM TV ###
    def listeningforplayingvideo(self, entity, attribute, old, new, kwargs):
        self.log(self.xx)
        
        self.cancel_listen_state(self.xx)
        self.set_state("input_boolean.amother_test", state = "on")
        self.log("canceling listen timer")
        self.log(self.xx)
        self.run_in(self.goaheadandtalkbitch, 9)
    
    
    
    def goaheadandtalkbitch(self, kwargs):
        self.log(self.xx)
        self.set_state("input_boolean.amother_test", state = "off")
        self.log('this shit is done')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        x = 2
        y = 1
        self.dict = {}
        self.dict[y] = "This is one"
        self.dict[x]     = "This is two"
        self.log(self.dict[2])
        self.log(self.dict[1])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import timedelta
import datetime

### CLASS ###
class streamcamerastotvs(hass.Hass):
    def initialize(self):
        
        
        ### VAIRABLES
        self.cancellistenertimer = datetime.datetime(2010, 12, 12, 12, 12, 12)
        self.listenrunoncetimer = datetime.datetime(2010, 12, 12, 12, 12, 12)
        return
    
    
    
    def streamblueiristotvsarray(self, onwhat, where, player, remote, remoteid, hdmi):
        self.args['goodies'] = []
        self.args['goodies'].append(onwhat)
        self.args['goodies'].append(where)
        self.args['goodies'].append(player)
        self.args['goodies'].append(remote)
        self.args['goodies'].append(remoteid)
        self.args['goodies'].append(hdmi)
        self.runseven = self.run_in(self.fireothertvinthreeseconds, 3)
    
    
    
    def fireothertvinthreeseconds(self, kwargs):
        self.streamblueiristotvs(self.args['goodies'][0], self.args['goodies'][1], self.args['goodies'][2], self.args['goodies'][3], self.args['goodies'][4], self.args['goodies'][5])
        i = 0
        while i < 6:
            self.args['goodies'].remove(self.args['goodies'][0])
            i += 1
    
    
    
    def streamblueiristotvs(self, onwhat, where, player, remote, remoteid, hdmi):
        if  self.anyone_home() ==True\
            and self.get_state(onwhat) == "off":
            self.putalertvideouponroomtv(where, player)
            self.runone = self.run_in(self.turnoffmediaplayer, 69, fuk = player, poop = onwhat, remote = remote, remoteid = remoteid, hdmi = hdmi)
            self.runtwo = self.run_in(self.turnofftvtimer, 72, remote = remote, remoteid = remoteid)
            if  remote == "remote.bedroom":
                self.runsix = self.run_in(self.bedroomtvhdmionewhenoff, 6)
        else:
            if  self.anyone_home() ==True:
                self.controlchromcast("media_player/media_play_pause", onwhat)
                self.putalertvideouponroomtv(where, player)
                self.runthree = self.run_in(self.turnoffmediaplayer, 33, fuk = player, poop = onwhat, remote = remote, remoteid = remoteid, hdmi = hdmi)
    
    
    
    def turnoffmediaplayer(self, kwargs):
        player = kwargs['fuk']
        self.call_service("media_player/turn_off", entity_id = player)
        self.log("turn N off {}".format(player[13:99].upper()))
        if  self.get_state(kwargs['poop']) == "paused":
            self.controltv(kwargs['remote'], kwargs['remoteid'], kwargs['hdmi'], "1")
            self.log('back to hdmi1 and resuming show on {}'.format(player[25:99]))
            self.runfour = self.run_in(self.tvbacktohdmione, 3, spooge = kwargs['poop'])
    
    
    
    def bedroomtvhdmionewhenoff(self, kwargs):
            self.controltv("remote.bedroom", "48480156", "InputHdmi3", "1")
            self.log("switch bedroom tv to hdmi3")
    
    
    
    def tvbacktohdmione(self, kwargs):
        self.controlchromcast("media_player/media_play_pause", kwargs['spooge'])
    
    
    
    def turnofftvtimer(self, kwargs):
        self.controltv(kwargs['remote'], kwargs['remoteid'], "PowerToggle", "1")
        self.log('turned off {} tv'.format(kwargs['remote'][7:99]))
    
    
    def controltv(self, remote, remotedevice, remotecommand, remoterepeats):
        self.call_service("remote/send_command", entity_id = remote, device = remotedevice, command = remotecommand, num_repeats = remoterepeats)
    
    
    
    def controlchromcast(self, service, entity,):
        self.call_service(service, entity_id = entity)
    
    
    
    ### PUT UP VIDEO ALERT ON A ROOM TV ###
    def putalertvideouponroomtv(self, where, player):
        self.args['cancellistenervideo_handle'] = self.listen_state(self.listeningforplayingvideo, player, new= "paused", where = where, player = player)
        self.call_service("media_player/play_media", entity_id = player, media_content_id = "http://192.168.1.230:81/mjpg/{}/video.mjpg".format(where), media_content_type = "image/jpg")
    
    
    
    ### PUT UP VIDEO ALERT ON A ROOM TV ###
    def listeningforplayingvideo(self, entity, attribute, old, new, kwargs):
        try:
            self.cancel_timer(self.cream)
        except:
            self.log("no timer running", level = "DEBUG")
        self.listenrunoncetimer = self.datetime() + timedelta(seconds=+3)
        self.cream = self.run_at(self.listenrunonce, self.listenrunoncetimer, where = kwargs['where'], player = kwargs['player'])
    
    
    
    def listenrunonce(self, kwargs):
        self.log('goolge just played {} camera on {}'.format(kwargs['where'].upper(), kwargs['player'][13:99].upper()))
        self.cancel_listen_state(self.args['cancellistenervideo_handle'])
#        self.cancellistenertimer = self.datetime() + timedelta(seconds=+99)
#        self.dude = self.run_at(self.runcanceltimer, self.cancellistenertimer)



#    def runcanceltimer(self, kwargs):
#        self.cancel_listen_state(self.args['cancellistenervideo_handle'])
#        self.log("canceling listen timer caues try didn't work")



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import timedelta
import datetime

class security(hass.Hass):
    def initialize(self):
#        return
        
        ### VARIABLES
        self.buddysirenes = ['switch.aeotec_zw080_siren_gen5_switch', 'switch.aeotec_zw080_siren_gen5_switch_2', 'switch.aeotec_zw080_siren_gen5_switch_3']
        
        ### PLUGINS
        self.buddy = self.get_app("buddyapp")
        
        ### TRIGGERS
        self.listen_state(self.anyonehomedude, "device_tracker.life360_aileen_")
        self.listen_state(self.anyonehomedude, "device_tracker.life360_buddy_thomas")
        self.listen_state(self.weleft, "binary_sensor.house_disarmed")
        
        ### TURN OFF SIREN
        self.listen_state(self.deactivatesiren, "binary_sensor.motion_bedroom", new= "off")
        self.listen_state(self.deactivatesiren, "binary_sensor.motion_corner_room", new= "off")
        self.listen_state(self.deactivatesiren, "binary_sensor.motion_kitchen", new= "off")
        self.listen_state(self.deactivatesiren, "binary_sensor.motion_living_room", new= "off")
        self.listen_state(self.deactivatesiren, "binary_sensor.motion_painting_cam", new= "off")
        self.listen_state(self.deactivatesiren, "binary_sensor.ecolink_doorwindow_sensor_sensor", new= "off")
        self.listen_state(self.deactivatesiren, "binary_sensor.ecolink_doorwindow_sensor_sensor_4", new= "off")
        self.listen_state(self.deactivatesiren, "binary_sensor.ecolink_doorwindow_sensor_sensor_5", new= "off")
    
    
    
    ### FUNCTIONS
    def anyonehomedude(self, entity, attribute, old, new, kwargs):
        if  self.noone_home() == True\
            and self.get_state("device_tracker.life360_aileen_") != "home"\
            and self.get_state("device_tracker.life360_buddy_thomas") != "home":
            self.call_service("mqtt/publish", topic = "house/armed", payload = "active" )
            self.log("no one home")
        else:
            self.call_service("mqtt/publish", topic = "house/armed", payload = "inactive" )
    
    
    
    def weleft(self, entity, attribute, old, new, kwargs):
        self.log("weleft")
        if  self.get_state("binary_sensor.house_disarmed") == "on"\
            and self.noone_home() == True\
            and self.get_state("device_tracker.life360_aileen_") != "home"\
            and self.get_state("device_tracker.life360_buddy_thomas") != "home":
            self.buddy.sendurl("http://192.168.1.230:81/admin?user=buddy3984&pw=1212&profile=3", 0)
            self.buddy.sendurl("https://graph-na04-useast2.api.smartthings.com/api/token/a2caf648-6876-4c54-a25f-8b49331cfb42/smartapps/installations/24a3aae1-475e-45e3-8d4a-3926e15230ea/execute/:33152be1ec700906f04f5fe206d2d71a:", 3)
            self.turn_off("switch.chromcastamplifier")
            self.log("ok dude house is now armed, nobody home")
            self.listen(self)
        else:
            self.log("test")
            if  self.get_state("binary_sensor.house_disarmed") == "off":
                self.buddy.sendurl("https://graph-na04-useast2.api.smartthings.com/api/token/a2caf648-6876-4c54-a25f-8b49331cfb42/smartapps/installations/24a3aae1-475e-45e3-8d4a-3926e15230ea/execute/:979e099e4e707ba1fbc1023284962084:", 0)
                self.turn_on("switch.chromcastamplifier")
                if  self.now_is_between("18:33:33", "11:57:00") == True:
                     self.buddy.sendurl("http://192.168.1.230:81/admin?user=buddy3984&pw=1212&profile=5", 3)
                else:
                     self.buddy.sendurl("http://192.168.1.230:81/admin?user=buddy3984&pw=1212&profile=1", 3)
                self.log("sweet!! da house is now disarmed, someones's home")
                self.cancellisten(self)
    
    
    
    
    def listen(self, kwargs):
        self.one = self.listen_state(self.activatesiren, "binary_sensor.motion_bedroom", new= "on")
        self.two = self.listen_state(self.activatesiren, "binary_sensor.motion_corner_room", new= "on")
        self.three = self.listen_state(self.activatesiren, "binary_sensor.motion_kitchen", new= "on")
        self.four = self.listen_state(self.activatesiren, "binary_sensor.motion_living_room", new= "on")
        self.five = self.listen_state(self.activatesiren, "binary_sensor.motion_painting_cam", new= "on")
        self.six = self.listen_state(self.activatesiren, "binary_sensor.ecolink_doorwindow_sensor_sensor", new= "on")
        self.seven = self.listen_state(self.activatesiren, "binary_sensor.ecolink_doorwindow_sensor_sensor_4", new= "on")
        self.eight = self.listen_state(self.activatesiren, "binary_sensor.ecolink_doorwindow_sensor_sensor_5", new= "on")
    
    
    
    def cancellisten(self, kwargs):
        self.cancel_listen_state(self.one)
        self.cancel_listen_state(self.two)
        self.cancel_listen_state(self.three)
        self.cancel_listen_state(self.four)
        self.cancel_listen_state(self.five)
        self.cancel_listen_state(self.six)
        self.cancel_listen_state(self.seven)
        self.cancel_listen_state(self.eight)
    
    
    
    def activatesiren(self, entity, attribute, old, new, kwargs):
        if  self.get_state("device_tracker.life360_aileen_") != "home"\
            and self.get_state("device_tracker.life360_buddy_thomas") != "home"\
            and self.get_state("binary_sensor.house_disarmed") == "on":
            self.saythatshit(self)
            self.buddy.sendurl("https://graph-na04-useast2.api.smartthings.com/api/token/a2caf648-6876-4c54-a25f-8b49331cfb42/smartapps/installations/24a3aae1-475e-45e3-8d4a-3926e15230ea/execute/:74a8f76a049ee3ef8dd12677f135d8f2:", 0)
            for turniton in self.buddysirenes:
                self.turn_on(turniton)
            self.log("siren is ACTIVE")
            self.args['sirenson'] = "on"
    
    
    
    def saythatshit(self, kwargs):
        self.buddy.poweronalertthentriggeralertinhowmanyseconds("break in detected. contacting the poe lease!", 0)
        self.saythatpoo = self.run_in(self.saythatshit, 6)
    
    
    
    def deactivatesiren(self, entity, attribute, old, new, kwargs):
        if  self.args['sirenson'] == "on"\
            and self.get_state("binary_sensor.motion_kitchen") == "off"\
            and self.get_state("binary_sensor.motion_bedroom") == "off"\
            and self.get_state("binary_sensor.motion_corner_room") == "off"\
            and self.get_state("binary_sensor.motion_living_room") == "off"\
            and self.get_state("binary_sensor.motion_painting_cam") == "off"\
            and self.get_state("binary_sensor.ecolink_doorwindow_sensor_sensor") == "off"\
            and self.get_state("binary_sensor.ecolink_doorwindow_sensor_sensor_4") == "off"\
            and self.get_state("binary_sensor.ecolink_doorwindow_sensor_sensor_5") == "off":
            for turniton in self.buddysirenes:
                self.turn_off(turniton)
            self.buddy.sendurl("https://graph-na04-useast2.api.smartthings.com/api/token/a2caf648-6876-4c54-a25f-8b49331cfb42/smartapps/installations/24a3aae1-475e-45e3-8d4a-3926e15230ea/execute/:8bad3d92a9b3919f83928f683bf695b2:", 0)
            self.cancel_timer(self.saythatpoo)
            self.log("okok siren deactivated now")
            self.args['sirenson'] = "off"
        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
self.alerttimer = datetime.datetime(2010, 12, 12, 12, 12, 12)
self.alerttimer = self.datetime() + timedelta(seconds=+6)
while self.alerttimer > self.datetime():
    pass
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import timedelta
from requests import get
import datetime
class buddy(hass.Hass):
    
    def initialize(self):
        
        ### VARIABLES
        self.didgoogleplay = datetime.datetime(2010, 12, 12, 12, 12, 12)
        self.runoncegoogle = datetime.datetime(2010, 12, 12, 12, 12, 12)
        self.alerttimer = datetime.datetime(2010, 12, 12, 12, 12, 12)
        self.cancellistener = ""
        pass
    
    
    
    def googlealert(self, kwargs):
        goodies = []
        goodies.append(kwargs['message'])
        for doit in goodies:
            if  self.cancellistener == "":
                self.googlesayit(doit)
                goodies.remove(doit)
            else:
                while self.cancellistener != "":
                    pass
                self.googlesayit(doit)
                goodies.remove(doit)
    
    
    
    def googlesayit(self, damessage):
        self.cancellistener = self.listen_state(self.listeningforplaying, "media_player.buddyalerts", old= "playing", damessage = damessage)
        self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = damessage, language= "en-au")
    
    
    
    def listeningforplaying(self, entity, attribute, old, new, kwargs):
        self.cancel_listen_state(self.cancellistener)
        self.log('goolge just said: "{}"'.format(kwargs['damessage']))
        self.alerttimer = self.datetime() + timedelta(seconds=+6)
        while self.alerttimer > self.datetime():
            pass
        self.cancellistener = ""
    
    
    
    def poweronalertthentriggeralertinhowmanyseconds(self, alertmessage, time):
        if  self.anyone_home() == True:
            if  self.get_state("media_player.buddyalerts") == "off":
                self.call_service("media_player/turn_on", entity_id = "media_player.buddyalerts")
                if time != 0:
                    self.alertone = self.run_in(self.googlealert, time, message = alertmessage )
                else:
                    self.alertone = self.run_in(self.googlealert, 0, message = alertmessage )
            else:
                if time != 0:
                    self.alertone = self.run_in(self.googlealert, time, message = alertmessage )
                else:
                    self.alertone = self.run_in(self.googlealert, 0, message = alertmessage )
    
    
    
    ### SEND URL
    def sendurl(self, kwargs):
        if  self.args['sendurllinktimer'] == 0:
            url = '{}'.format(self.args['sendurllink'])
            headers = {'x-ha-access': '7410zz00','content-type': 'application/json'}
            response = get(url, headers=headers)
            sex = str(response.text)
            if  sex.find("profile=") == 13:
                num = sex.find("profile=")
                self.log("blue iris has been changed to {}".format(sex[num:num+9]))
            else:
                dick = sex.find('"result":"')
                self.log("sent to smartthings for message alerts on {} status".format(sex[dick+9:dick+13]))
        else:
            self.runtwo = self.run_in(self.sendurltimerfunc, self.args['sendurllinktimer'])
    
    
    
    ### SEND URL TIMER FUNC
    def sendurltimerfunc(self, kwargs):
            self.args['sendurllinktimer'] = 0
            url = '{}'.format(self.args['sendurllink'])
            headers = {'x-ha-access': '7410zz00','content-type': 'application/json'}
            response = get(url, headers=headers)
            sex = str(response.text)
            if  sex.find("profile=") == 13:
                num = sex.find("profile=")
                self.log("blue iris has been changed to {}".format(sex[num:num+9]))
            else:
                dick = sex.find('"result":"')
                self.log("sent to smartthings for message alerts on {} status".format(sex[dick+9:dick+13]))
            
            
            
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass

### CLASS ###
class officelighttest(hass.Hass):
    def initialize(self):
#        return
        ### VARIBALE
        self.x = 0
        self.lightentities = ['light.ge_zw7101_smart_led_light_bulb_ze26i_level', 'light.ge_zw7101_smart_led_light_bulb_ze26i_level_5',
                              'light.ge_zw7101_smart_led_light_bulb_ze26i_level_2', 'light.ge_zw7101_smart_led_light_bulb_ze26i_level_3',
                              'light.ge_zw7101_smart_led_light_bulb_ze26i_level_4', 'switch.aeotec_zw140_dual_nano_switch_switch_3',
                              'switch.zooz_zen15_power_switch_switch_2']
        
        ### GET APPS
        self.buddy = self.get_app("buddyapp")
        
        ### TRIGGER
        self.turniton(self)
        
    def turniton(self, kwargs):
    #turn on my backyard lights!
#        self.log(self.lightentities[self.x])
        self.run_in(self.turnemon, 0, light = self.lightentities[self.x])
        if  self.x <= len(self.lightentities):
            self.x += 1
            self.run_in(self.turniton, 0)
    
    
    
    def turnemon(self, kwargs):
        self.turn_off('{}'.format(kwargs['light']))
        self.log('{}'.format(kwargs['light']))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        self.buddy = self.get_app("buddyapp")
        
        self.buddy.args['test'] = "so0oge om my ass!"
        self.log(self.buddy.args['test'])
        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass

### CLASS ###
class officelighttest(hass.Hass):
    def initialize(self):
#        return
        ### VARIBALE
        self.x = 0
        
        ### GET APPS
        self.buddy = self.get_app("buddyapp")
        
        self.buddy.args['alertmessage'] = "hello there"
        self.buddy.args['alerttime'] = 1
        self.saythatshit(self)
        
    def saythatshit(self, kwargs):
        self.buddy.poweronalertthentriggeralertinhowmanyseconds(self)
        if  self.x < 3:
            self.x += 1
            self.log(self.x)
            self.saythatpoo = self.run_in(self.saythatshit, 6)
        else:
            self.cancel_timer(self.saythatpoo)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            if  self.get_state("device_tracker.life360_aileen_") == "home"\
                and datetime.date.today().weekday() in [0, 1, 2, 3, 4]\
                and self.now_is_between("18:57:00", "21:00:00") == True:
                self.log("aileen is about to enter", level = "DEBUG")
                self.log("the front yard alert didn't fire for aileen welcome alert")
            else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
self.googlealert(fuk=10)
       
    def googlealert(self, **kwargs):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    dependencies: 
        - buddyapp   #the module
        - streamcamerastotvsapp
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
self.runone = self.run_in(self.turnoffmediaplayer, 9, fuk = player)
    def turnoffmediaplayer(self, kwargs):
        self.log(kwargs['fuk'])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #            self.runone = self.run_in(self.turnoffmediaplayer, 33)
#            self.runtwo = self.run_in(self.turnoffkitchentv, 36)
    
    
    self.putalertvideouponroomtv(where, player)
    
    def turnoffmediaplayer(self, kwargs):    
        self.call_service("media_player/turn_off", entity_id = "media_player.securitycamskitchentv")
    
    def turnoffmediaplayer(self, player):    
        self.call_service("media_player/turn_off", entity_id = player)
    
    ### PUT UP VIDEO ALERT ON A ROOM TV ###
    def putalertvideouponroomtv(self, where, player):
        self.cancellistenervideo = self.listen_state(self.listeningforplayingvideo, player, new= "paused")
        self.call_service("media_player/play_media", entity_id = player, media_content_id = "http://192.168.1.230:81/mjpg/{}/video.mjpg".format(where), media_content_type = "image/jpg")
        self.log("tits", level = "DEBUG")
        self.titsplayer = player
        self.titswhere = where
    
    
    ### PUT UP VIDEO ALERT ON A ROOM TV ###
    def listeningforplayingvideo(self, entity, attribute, old, new, kwargs):
        self.cancel_listen_state(self.cancellistenervideo)
        self.log('goolge just played {} on {}'.format(self.titswhere.upper(), self.titsplayer[13:99].upper()))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
### 101 electroics hub
### 7 bedroom
### 5 pojector
### 18 kitchen
{
  "entity_id": "remote.kitchen", "device":"54056702", "command":"PowerToggle"
}
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import timedelta
from requests import get
import datetime
### CLASS ###
class kitchentvalert(hass.Hass):
    def initialize(self):
        ###1 VARIABLE ###
        self.buddy = self.get_app("buddyapp")
        self.t = self.args["datime"]
        self.x = self.args["didgooglespeak"]
        ### TRIGGERS ###
        self.poo()
    ### FUNCTIONS ###
    def poo(self):
        self.log(self.buddy.args["test"])
        self.t = self.datetime()
        self.log(self.t)
        self.log(self.x)
        if  self.buddy.args["test"] == "shit fucker":
            self.buddy.googlealert("test")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
TEST TO SEE IF  GOOGLE ALERT REALLY SPOKE ALERT
import appdaemon.plugins.hass.hassapi as hass
from datetime import timedelta
from requests import get
import datetime
### CLASS ###
class officelighttest(hass.Hass):
    def initialize(self):
        ###1 VARIABLE ###
        self.didgooglespeak = datetime.datetime(2010, 12, 12, 12, 12, 12)
        ### TRIGGERS ###
        self.poo()
    ### FUNCTIONS ###
    def poo(self):
        self.googlemessage = "yo buddy! this is a test"
        self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = self.googlemessage, language= "en-au")
        self.listen_state(self.aileenminwarning, "media_player.buddyalerts")
        self.slimball = self.run_in(self.pooshit, 9)
    
    def pooshit(self, kwargs):
        self.googlemessage = "okok this is another test"
        self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = self.googlemessage, language= "en-au")
    
    def aileenminwarning(self, entity, attribute, old, new, kwargs):
        if  old == "playing"\
            and self.didgooglespeak < self.datetime():
            self.didgooglespeak = self.datetime() + timedelta(seconds=+3)
            self.log('google said "{}"'.format(self.googlemessage))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
GET STATE
import appdaemon.plugins.hass.hassapi as hass
from datetime import timedelta
from requests import get
import datetime
### CLASS ###
class officelighttest(hass.Hass):
    def initialize(self):
        ###1 VARIABLE ###
        self.buddytimer = datetime.datetime(2010, 12, 12, 12, 12, 12)
        ### TRIGGERS ###
        self.poo()
    ### FUNCTIONS ###
    def poo(self):
        self.buddytimer = self.datetime() + timedelta(seconds=+33)
        self.log(self.get_state("sensor.aileen_to_home"))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import timedelta
from requests import get
import datetime
### CLASS ###
class officelighttest(hass.Hass):
    def initialize(self):
        ###1 VARIABLE ###
        self.buddytimer = datetime.datetime(2010, 12, 12, 12, 12, 12)
        ### TRIGGERS ###
        self.poo()
    ### FUNCTIONS ###
    def poo(self):
        self.buddytimer = self.datetime() + timedelta(seconds=+33)
        timestring = str(self.buddytimer)
        self.homeat = timestring[10:16]
        self.log("test {} pm".format(self.homeat), level = "DEBUG")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import timedelta
from requests import get
import datetime
        ### CLASS ###
class chromcastamplifier(hass.Hass):
    def initialize(self):
        #### VARIABLES ###
        self.buddytimer = datetime.datetime(2010, 12, 12, 12, 12, 12)
        ### TRIGGERS ###
        self.listen_state(self.runin33, "switch.chromcastamplifier", new= "off")
    #FUNCTIONS
    def runin33(self, entity, attribute, old, new, kwargs):
        if  self.buddytimer < self.datetime()\
            and self.anyone_home() == True:
            self.buddytimer = self.datetime() + timedelta(seconds=+33)
            self.dude = self.run_at(self.turnchromeapliferbackon, self.buddytimer)
            self.log("turning chromecast amplifier back on at {}".format(self.buddytimer))
    #
    def turnchromeapliferbackon(self, kwargs):
        self.turn_on("switch.chromcastamplifier")
        self.log("turned chromecast amplifierback on")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import timedelta
from requests import get
import datetime
import random


class baloosprinkler(hass.Hass):
    def initialize(self):
        # VARIABLES
        self.buddytimer = datetime.datetime(2010, 12, 12, 12, 12, 12)
        #TRIGGERS
        self.listen_state(self.tripwirecrossed, "binary_sensor.ecolink_doorwindow_sensor_sensor_2", new= "off")
    #FUNCTIONS
    def tripwirecrossed(self, entity, attribute, old, new, kwargs):
        if  datetime.date.today().weekday() == 3\
            and self.now_is_between("06:33:00", "09:33:00") == True:
            self.log("no alerts right now, the mowing guys are out", level = "DEBUG")
        else:    
            if  self.buddytimer < self.datetime():
                self.buddytimer = self.datetime() + timedelta(seconds=+66)
                self.turn_on("switch.sprinklerbaloo")
                self.dude = self.run_at(self.timerexpired, self.buddytimer)
                self.triggercornercam()
                self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = "", language= "en-au")
                self.slimball = self.run_in(self.goaheadandtalkbitch, 3)
    #
    def goaheadandtalkbitch(self, kwargs):
        self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = "stupid baloo jumped the fence", language= "en-au")
        self.log("google said the shit")    
    #
    #TIGGER FRONT YARD ALERT MESSAGE
    def triggercornercam(self):
        url = 'http://192.168.1.230:81/admin?camera=sideBackDoor&trigger&user=buddy3984&pw=1212'
        headers = {'x-ha-access': '7410zz00','content-type': 'application/json'}
        response = get(url, headers=headers)
        sex = str(response.text)
        num = sex.find("camera=")
        self.log("blue iris alert sent to {} at {}!".format(sex[num+7:num+20], self.time()))
    #
    def timerexpired(self, kwargs):
        self.turn_off("switch.sprinklerbaloo")
        self.log("baloo alert ready to fire again")
    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
import datetime
from datetime import timedelta
import random
from requests import get

class officelighttest(hass.Hass):
    def initialize(self):
        #1 VARIABLE
        self.buddytimer = datetime.datetime(2010, 12, 12, 12, 12, 12)
        self.lightentities = ['switch.aeotec_zw140_dual_nano_switch_switch_3', 'switch.zooz_zen15_power_switch_switch_2', 
                              'light.ge_zw7101_smart_led_light_bulb_ze26i_level_2', 'light.ge_zw7101_smart_led_light_bulb_ze26i_level_3',
                              'light.ge_zw7101_smart_led_light_bulb_ze26i_level_4', 'light.ge_zw7101_smart_led_light_bulb_ze26i_level_5',
                              'light.ge_zw7101_smart_led_light_bulb_ze26i_level']
        #
#        self.poo(self, "", "", "", "")
        self.poo()
        #
    def poo(self):
        self.log("tryingit")
        if  self.get_state("device_tracker.life360_aileen_") in ["not_home", "home"]\
            and self.now_is_between("23:03:00", "23:03:03") == False\
            and datetime.date.today().weekday() in [0, 1, 2, 3, 4, 5, 6]:
            self.buddytimer = self.datetime() + timedelta(seconds=+1)
            self.speakalert = self.run_at(self.reboot, self.buddytimer)
    
    def reboot(self, kwargs):
        self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = "this shit rebooted", language= "en-au")
#        for turniton in self.lightentities:
#            self.turn_on(turniton)
        self.log("rebooted at {}".format(self.buddytimer))
#        self.thenturnitoff = self.run_in(self.thenitsoff, 12)
    #
#    def thenitsoff(self, kwargs):
#        for turniton in self.lightentities:
#            self.turn_off(turniton)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
import datetime
from datetime import timedelta
from requests import get

class frontyardalert(hass.Hass):
    def initialize(self):
        self.buddytimer = datetime.datetime(2010, 12, 12, 12, 12, 12)
        self.speakalert = ""
        self.wheredamotionat = ""
        #
        self.listen_state(self.tripwirefrontactive, "binary_sensor.ecolink_doorwindow_sensor_sensor_3", new= "off")
        self.listen_state(self.camsandporchmotion, "binary_sensor.motion_driveway_camera", new= "on")
        self.listen_state(self.camsandporchmotion, "binary_sensor.motion_front_door", new= "on")
        self.listen_state(self.camsandporchmotion, "binary_sensor.motion_front_yard", new= "on")
        self.listen_state(self.frontyardfrontdooranddrivewaycam, "binary_sensor.motion_front_door", new= "on")
        self.listen_state(self.frontyardfrontdooranddrivewaycam, "binary_sensor.motion_front_yard", new= "on")
    #
    #
    #FRONT YARD AND FRONT DOOR CAM MOTION
    def frontyardfrontdooranddrivewaycam(self, entity, attribute, old, new, kwargs):
        if  self.get_state("binary_sensor.motion_front_door") == "on"\
            and self.get_state("binary_sensor.motion_front_yard") == "on"\
            and self.now_is_between("08:01:00", "12:33:00") == True\
            and self.buddytimer < self.datetime():
            self.buddytimer = self.datetime() + timedelta(seconds=+33)
            self.wheredamotionat = "front yard and front door motion"
            self.buddyalert()
    #
    #FRONT YARD OR FRONT DOOR CAM AND DRIVEWAY CAM MOTION
    def frontyardfrontdooranddrivewaycam(self, entity, attribute, old, new, kwargs):
        if  self.get_state("binary_sensor.motion_driveway_camera") == "on"\
            and self.now_is_between("08:01:00", "13:33:00") == True\
            and self.buddytimer < self.datetime():
            self.buddytimer = self.datetime() + timedelta(seconds=+33)
            self.wheredamotionat = "front yard or front door plus driveway motion"
            self.buddyalert()
    #
    #FRONT YARD OR FRONT DOOR OR DRIVE WAY CAM AND PORCH MOTION
    def camsandporchmotion(self, entity, attribute, old, new, kwargs):
        if  self.get_state("binary_sensor.motion_porch_motion") == "on"\
            and self.buddytimer < self.datetime():
            self.buddytimer = self.datetime() + timedelta(seconds=+33)
            self.wheredamotionat = "all cams plus porch motion"
            self.buddyalert()
    #
    #TRIP WIRE CONDITION
    def tripwirefrontactive(self, entity, attribute, old, new, kwargs):
        if  self.buddytimer < self.datetime():
            self.buddytimer = self.datetime() + timedelta(seconds=+33)
            self.wheredamotionat = "tripwire motion in front"
            self.buddyalert()
    #
    #GO AHEAD AND SPEAK THAT SHIT
    def buddyalert(self):
        if  datetime.date.today().weekday() == 3\
            and self.now_is_between("06:33:00", "09:33:00") == True:
            self.log("no alerts right now, the mowing guys are out", level = "DEBUG")
        else:
            if  self.now_is_between("23:57:00", "06:57:00") == True:
                self.speakalert = "alert!! trip wire is active right now. someone could be outside"
            else:
                self.speakalert = "hey bitch!!  you got someone creeping up on you in your driveway"
            self.triggercornercam()
            self.dude = self.run_at(self.alertinthepasttimer, self.buddytimer)
            if  self.get_state("device_tracker.life360_aileen_") == "home"\
                and datetime.date.today().weekday() == 0 or 1 or 2 or 3 or 4\
                and self.now_is_between("18:57:00", "21:00:00") == True:
                self.log("aileen is about to enter", level = "DEBUG")
            else:
                self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = "", language= "en-au")
                self.slimball = self.run_in(self.goaheadandtalkbitch, 3)
    #TIMERS NEED KWARGS
    def goaheadandtalkbitch(self, kwargs):
        self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = "{}".format(self.speakalert), language= "en-au")
        self.log("google said the shit")
    #TIMERS NEED KWARGS
    def alertinthepasttimer(self, kwargs):
        self.log("ready to fire again")
    #
    #TIGGER FRONT YARD ALERT MESSAGE
    def triggercornercam(self):    
        url = 'http://192.168.1.230:81/admin?camera=cornerRoomCam&trigger&user=buddy3984&pw=1212'
        headers = {'x-ha-access': '7410zz00','content-type': 'application/json'}
        response = get(url, headers=headers)
        sex = str(response.text)
        num = sex.find("camera=")
        self.log("blue iris alert sent to {} at {} for {}".format(sex[num+7:num+20], self.time(), self.wheredamotionat))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
import datetime
from datetime import timedelta
import random
from requests import get

class officelighttest(hass.Hass):
    def initialize(self):
        #1 VARIABLE
        self.buddytimer = datetime.datetime(2010, 12, 12, 12, 12, 12)
        self.lightentities = ['switch.aeotec_zw140_dual_nano_switch_switch_3', 'switch.zooz_zen15_power_switch_switch_2', 
                              'light.ge_zw7101_smart_led_light_bulb_ze26i_level_2', 'light.ge_zw7101_smart_led_light_bulb_ze26i_level_3',
                              'light.ge_zw7101_smart_led_light_bulb_ze26i_level_4', 'light.ge_zw7101_smart_led_light_bulb_ze26i_level_5',
                              'light.ge_zw7101_smart_led_light_bulb_ze26i_level']
        #
#        self.poo(self, "", "", "", "")
        self.poo()
        #
    def poo(self):
        if  datetime.date.today().weekday() == 1 or 2 or 3 or 4 or 5\
            and self.buddytime < self.datetime()\
            and self.now_is_between("18:57:00", "23:00:00") == True:
            self.buddytimer = self.datetime() + timedelta(seconds=+12)
            self.speakalert = self.run_at(self.reboot, self.buddytimer)
    
    def reboot(self, kwargs):
        self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = "this shit rebooted", language= "en-au")
        for turniton in self.lightentities:
            self.turn_on(turniton)
        self.log("rebooted at {}".format(self.buddytimer))
        self.thenturnitoff = self.run_in(self.thenitsoff, 12)
    #
    def thenitsoff(self, kwargs):
        for turniton in self.lightentities:
            self.turn_off(turniton)
###    def tomorrow(self):
        """
        Return datetime.date object +1 day from current internal AppDaemon 
        clock
        """
        return self.date() + timedelta(days=1)
        
    def cunt(self, entity, attribute, old, new, kwargs):
        self.log("thi shit works like big titties")
        self.log("Tomorrow is fucking titts{}".format(self.tomorrow()))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def initialize(self):
        self.fuckshit = self.get_app("utilites")
        self.listen_state(self.cunt, "input_boolean.amother_test", new= "on")

#    def tomorrow(self):
#        """
#        Return datetime.date object +1 day from current internal AppDaemon 
#        clock
#        """
#        return self.date() + timedelta(days=1)
        
    def cunt(self, entity, attribute, old, new, kwargs):
        self.log("big titties")
        self.log(self.fuckshit.buddyfuck())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import datetime, timedelta
    
class HelloWorld(hass.Hass):
    
    def initialize(self):
        self.fuckshit = self.get_app("utilites")
        self.listen_state(self.cunt, "input_boolean.amother_test", new= "on")

#    def tomorrow(self):
#        """
#        Return datetime.date object +1 day from current internal AppDaemon 
#        clock
#        """
#        return self.date() + timedelta(days=1)
        
    def cunt(self, entity, attribute, old, new, kwargs):
        self.log("big titties")
        self.log("Tomorrow is fucking titts {}".format(self.fuckshit.tomorrow()))
#        self.log(self.fuckshit.buddyfuck()) 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def buddyfuck(self):
        return self.datetime()
self.log("Tomorrow is fucking titts {}".format(self.buddyfuck()))
or
self.log("Tomorrow is fucking titts {}".format(self.datetime()))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def initialize(self):
   self.timer_handle = self.run_in(self.send_alarm, 5*60)

def send_alarm(self):
   #send notification

Then when you update the status do

self.cancel_timer(self.timer_handle)
  self.timer_handle = self.run_in(self.send_alarm, 5*60)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
Run_daily(callback,time,constrain_days=mon,tue,wed,thu,fri)
Or
Run_daily(callback,time,constrain_days=sat,sun)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import datetime, timedelta
    
class HelloWorld(hass.Hass):
    
    def initialize(self):
        self.fuckshit = self.get_app("utilites")
        self.listen_state(self.cunt, "input_boolean.amother_test", new= "on")
    
    def buddyfuck(self):
        return self.time()

#    def tomorrow(self):
#        """
#        Return datetime.date object +1 day from current internal AppDaemon 
#        clock
#        """
#        return self.date() + timedelta(days=1)
        
    def cunt(self, entity, attribute, old, new, kwargs):
         self.log("big titties")
#         self.log("Tomorrow is fucking titts {}".format(self.fuckshit.tomorrow()))
         self.log("Tomorrow is fucking titts {}".format(self.fuckshit.soon(second=333)))
#         self.log("Tomorrow is fucking titts {}".format(self.buddyfuck()))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
CALL BACK TO A FUNCTION

import appdaemon.plugins.hass.hassapi as hass
from datetime import datetime, timedelta
    
class HelloWorld(hass.Hass):
    
    def initialize(self):
        self.listen_state(self.cunt, "input_boolean.amother_test", new= "on")
    
    def buddyfuck(self, sex=5):
        poo = sex
        return poo

    def cunt(self, entity, attribute, old, new, kwargs):
#        timestamp = self.datetime() - timedelta(seconds=333)
#        self.buddyfuck(sex=15)
        
        self.log("Tomorrow is fucking titts {}".format(self.buddyfuck(33)))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import datetime, timedelta

buddyfuck = ""
    
class HelloWorld(hass.Hass):
    
    def initialize(self):
        self.listen_state(self.cunt, "input_boolean.amother_test", new= "on")
    
    def cunt(self, entity, attribute, old, new, kwargs):
#        timestamp = self.datetime() - timedelta(seconds=333)
#        self.buddyfuck(sex=15)
        buddyfuck = 2018
        
        self.log("Tomorrow is fucking titts {}".format(buddyfuck))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import datetime, timedelta

buddyfuck = ""
    
class officelighttest(hass.Hass):
    
    def initialize(self):
        self.listen_state(self.cunt, "input_boolean.turn_on_shit_test", new= "on")
    
    def cunt(self, entity, attribute, old, new, kwargs):
        is_buddy_home = self.get_state("device_tracker.buddy_9splus")
		if	is_buddy_home == "home":
		    self.turn_off("fan.office_fan")    
		    fan.office_fan
            timestamp = self.datetime() + timedelta(seconds=60)
            buddyfuck = timestamp
            self.log("python turned on office fan")
            self.log("this is the time in the future ={}".format(buddyfuck))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
TURNS ON FAN WITH LOGS
import appdaemon.plugins.hass.hassapi as hass
from datetime import datetime, timedelta

class officelighttest(hass.Hass):
    def initialize(self):
        self.buddyfuck = datetime(2013, 9, 13)
        self.listen_state(self.cunt, "input_boolean.amother_test", new= "on")
        self.listen_state(self.didofficefanturnon, "fan.office_fan", new= "on")
    
    def cunt(self, entity, attribute, old, new, kwargs):
        self.buddyfuck = self.datetime() + timedelta(seconds=60)
        buddyhome = self.get_state("device_tracker.buddy_9splus")
        if	buddyhome == "home":
            self.log(buddyhome)
            self.turn_on("fan.office_fan")
            
    def didofficefanturnon(self, entity, attribute, old, new, kwargs):
            self.log("office fan tured on bitch")
            self.log(self.buddyfuck)
              
            
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def Jack(self):
        responses = [
            "Jack is asleep on his chair",
            "Jack just went out bowling with his kitty friends",
            "Jack is in the hall cupboard",
            "Jack is on the back of the den sofa",
            "Jack is on the bed",
            "Jack just stole a spot on daddy's chair",
            "Jack is in the kitchen looking out of the window",
            "Jack is looking out of the front door",
            "Jack is on the windowsill behind the bed",
            "Jack is out checking on his clown suit",
            "Jack is eating his treats",
            "Jack just went out for a walk in the neigbourhood",
            "Jack is by his bowl waiting for treats"
        ]

        return random.choice(responses)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import datetime, timedelta

class officelighttest(hass.Hass):
    def initialize(self):
        self.buddyfuck = datetime(2013, 9, 13)
        self.listen_state(self.cunt, "input_boolean.amother_test", new= "on")
        self.listen_state(self.didofficefanturnon, "fan.office_fan", new= "on")
    
    def cunt(self, entity, attribute, old, new, kwargs):
        self.buddyfuck = self.datetime() + timedelta(seconds=60)
        buddyhome = self.get_state("device_tracker.buddy_9splus")
        if	buddyhome == "home":
            self.log(buddyhome)
            self.turn_on("fan.office_fan")
            
    def didofficefanturnon(self, entity, attribute, old, new, kwargs):
        if  self.buddyfuck > self.datetime():
            self.log("office fan tured on bitch")   
            self.log(self.buddyfuck)
            self.run_in(self.turnofofficefan, 9)
            
    def turnofofficefan(self, kwargs):
    	self.turn_off("fan.office_fan")
    	self.log("sent request to turn OFF office light")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
WEB REQUEST GET METHOD
import appdaemon.plugins.hass.hassapi as hass
from datetime import datetime, timedelta
from requests import get

class officelighttest(hass.Hass):
    def initialize(self):
        self.listen_state(self.cunt, "input_boolean.amother_test", new= "on")
        self.listen_state(self.cunt, "input_boolean.turn_on_shit_test", new= "on")

    def cunt(self, entity, attribute, old, new, kwargs):
        if  self.now_is_between("18:30:00", "06:00:00") and self.get_state("switch.testderp") == "off" and self.get_state("binary_sensor.doorbacksensor") == "off":
            self.log("the switch is off bro")
            url = 'https://graph-na04-useast2.api.smartthings.com/api/token/a2caf648-6876-4c54-a25f-8b49331cfb42/smartapps/installations/24a3aae1-475e-45e3-8d4a-3926e15230ea/execute/:07de045ff969e68596957fb621943313:'
            headers = {'x-ha-access': 'YOUR_PASSWORD','content-type': 'application/json'}
            response = get(url, headers=headers)
            self.log(response.text)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
COMPLETE BACKYARD LIGHTS APP

import appdaemon.plugins.hass.hassapi as hass
from datetime import datetime, timedelta
from requests import get

class backyardlights(hass.Hass):
    def initialize(self):
        self.buddyfuck = datetime(2010, 12, 12)
        self.nighttime = self.now_is_between("sunset - 00:33:33", "sunrise - 00:33:33")
        self.offtimer = ""
        self.offlogphrase = ""
        
        self.listen_state(self.turnonbackyyardlights, "binary_sensor.doorgaragesensor", new= "on")
        self.listen_state(self.turnonbackyyardlights, "binary_sensor.tripwirebackdoor", new= "on")
        self.listen_state(self.turnonbackyyardlights, "binary_sensor.doorbacksensor", new= "on")
        self.listen_state(self.turnoffbackyyardlights, "binary_sensor.doorgaragesensor", new= "off")
        self.listen_state(self.turnoffbackyyardlights, "binary_sensor.doorbacksensor", new= "off")

    def turnonbackyyardlights(self, entity, attribute, old, new, kwargs):
        
        if  self.offtimer == "":
            self.offlogphrase = "gonna try to turn these light off"
        else:
            self.offlogphrase = "tried to turn em off but interupted! trying again"
        
        try:
            self.cancel_timer(self.offtimer)
        except:
            self.log("no timer running", level = "DEBUG")
        
        if  self.buddyfuck < self.datetime()\
            and self.nighttime == False\
            and self.offtimer == "":
            
            self.buddyfuck = self.datetime() + timedelta(seconds=33)
            
            #turn on my backyard lights!
            self.turn_on("light.baloolight")
            self.turn_on("light.laundry_room_light")
            self.turn_on("light.backdoor_light_one")
            self.turn_on("light.backdoor_light_two")
            self.turn_on("light.backdoor_light_three")
            self.turn_on("light.backdoor_light_four")
            self.log("💡 yo bitch the backyard lights are on now! 💡")
    
    def turnoffbackyyardlights(self, entity, attribute, old, new, kwargs):
        
        if      self.get_state("light.laundry_room_light") == "on"\
            and self.get_state("binary_sensor.doorbacksensor") == "off"\
            and self.get_state("binary_sensor.doorgaragesensor") == "off"\
            and self.get_state("binary_sensor.tripwirebackdoor") == "off"\
            and self.get_state("binary_sensor.tripwirebaloo") == "off":
            
            self.offtimer = self.run_in(self.turnemoffin33seconds, 33)
            self.log("{} in 33 seconds".format(self.offlogphrase))
    
    def turnemoffin33seconds(self, kwargs):        
        #turn on my backyard lights!
        self.turn_off("light.baloolight")
        self.turn_off("light.laundry_room_light")
        self.turn_off("light.backdoor_light_one")
        self.turn_off("light.backdoor_light_two")
        self.turn_off("light.backdoor_light_three")
        self.turn_off("light.backdoor_light_four")
        self.offtimer = ""
        self.log("☠️ okay fuck face the backyard lights are 0FF now! ☠️")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


172.249.233.104:8123/api/services/switch/turn_on?api_password=7410zz00

{ "topic": "baloo/motion", "payload": "active"}

switch.turn_on
"entity_id": "group.buddysirens"

http://192.168.1.230:81/admin?user=buddy3984&pw=1212&profile=6

###GOOGLE TEXT TO SPEECH
{"entity_id":"media_player.buddyalerts", "message":"you are so hot right now", "language":"en-au"}

self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = "this is a test", language= "en-au")

self.call_service("media_player/volume_set", entity_id = "media_player.buddyalerts", volume_level = 0.5)

service: media_player.volume_set
      data_template:
        entity_id: media_player.master_bedroom_home
        volume_level: 0.5
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
CHANGE BLUE IRIS PROFILE
url = 'http://192.168.1.230:81/admin?user=buddy3984&pw=1212&profile=2'
            headers = {'x-ha-access': '7410zz00','content-type': 'application/json'}
            response = get(url, headers=headers)
            self.log(response.text)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
from datetime import datetime, timedelta
from requests import get

class alarm(hass.Hass):
    def initialize(self):
        self.wehome = self.anyone_home()
        
        ###   TURN ON SIREN        
        self.listen_state(self.activatesiren, "binary_sensor.motion_bedroom", new= "on")
        self.listen_state(self.activatesiren, "binary_sensor.motion_corner_room", new= "on")
        self.listen_state(self.activatesiren, "binary_sensor.motion_kitchen", new= "on")
        self.listen_state(self.activatesiren, "binary_sensor.motion_living_room", new= "on")
        self.listen_state(self.activatesiren, "binary_sensor.motion_painting_cam", new= "on")
        self.listen_state(self.activatesiren, "binary_sensor.ecolink_doorwindow_sensor_sensor", new= "on")
        self.listen_state(self.activatesiren, "binary_sensor.ecolink_doorwindow_sensor_sensor_4", new= "on")
        self.listen_state(self.activatesiren, "binary_sensor.ecolink_doorwindow_sensor_sensor_5", new= "on")
        ###   TURN OFF SIREN        
        self.listen_state(

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
ALARM COMPLETE WORKING
import appdaemon.plugins.hass.hassapi as hass
from datetime import datetime, timedelta
from requests import get

class alarm(hass.Hass):
    def initialize(self):
        self.wehome = self.anyone_home()
        
        ###   TURN ON SIREN        
        self.listen_state(self.activatesiren, "binary_sensor.motion_bedroom", new= "on")
        self.listen_state(self.activatesiren, "binary_sensor.motion_corner_room", new= "on")
        self.listen_state(self.activatesiren, "binary_sensor.motion_kitchen", new= "on")
        self.listen_state(self.activatesiren, "binary_sensor.motion_living_room", new= "on")
        self.listen_state(self.activatesiren, "binary_sensor.motion_painting_cam", new= "on")
        self.listen_state(self.activatesiren, "binary_sensor.ecolink_doorwindow_sensor_sensor", new= "on")
        self.listen_state(self.activatesiren, "binary_sensor.ecolink_doorwindow_sensor_sensor_4", new= "on")
        self.listen_state(self.activatesiren, "binary_sensor.ecolink_doorwindow_sensor_sensor_5", new= "on")
        ###   TURN OFF SIREN        
        self.listen_state(self.deactivatesiren, "binary_sensor.motion_bedroom", new= "off")
        self.listen_state(self.deactivatesiren, "binary_sensor.motion_corner_room", new= "off")
        self.listen_state(self.deactivatesiren, "binary_sensor.motion_kitchen", new= "off")
        self.listen_state(self.deactivatesiren, "binary_sensor.motion_living_room", new= "off")
        self.listen_state(self.deactivatesiren, "binary_sensor.motion_painting_cam", new= "off")
        self.listen_state(self.deactivatesiren, "binary_sensor.ecolink_doorwindow_sensor_sensor", new= "off")
        self.listen_state(self.deactivatesiren, "binary_sensor.ecolink_doorwindow_sensor_sensor_4", new= "off")
        self.listen_state(self.deactivatesiren, "binary_sensor.ecolink_doorwindow_sensor_sensor_5", new= "off")
        
    def activatesiren(self, entity, attribute, old, new, kwargs):
        if  self.wehome == True:
            self.log("siren is ACTIVE")
            self.repeatpolice = True
            self.call_service("media_player/volume_set", entity_id = "media_player.buddyalerts", volume_level = 0.6)
            self.saythatshit(kwargs)
            self.sendalerts("8bad3d92a9b3919f83928f683bf695b2")
#            self.turn_on("")
#            self.turn_on("")
#            self.turn_on("")

    def saythatshit(self, kwargs):
        if  self.repeatpolice == True:
            self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = "break in detected. contacting the poe lease!", language= "en-au")
            self.run_in(self.saythatshit, 6)
        
    def sendalerts(self, buddyurl):
        url = 'https://graph-na04-useast2.api.smartthings.com/api/token/a2caf648-6876-4c54-a25f-8b49331cfb42/smartapps/installations/24a3aae1-475e-45e3-8d4a-3926e15230ea/execute/:{}:'.format(buddyurl)
        headers = {'x-ha-access': '7410zz00','content-type': 'application/json'}
        response = get(url, headers=headers)
        self.log(response.text)
    
    def deactivatesiren(self, entity, attribute, old, new, kwargs):
        if  self.get_state("binary_sensor.motion_kitchen") == "off"\
            and self.get_state("binary_sensor.motion_bedroom") == "off"\
            and self.get_state("binary_sensor.motion_corner_room") == "off"\
            and self.get_state("binary_sensor.motion_living_room") == "off"\
            and self.get_state("binary_sensor.motion_painting_cam") == "off"\
            and self.get_state("binary_sensor.ecolink_doorwindow_sensor_sensor") == "off"\
            and self.get_state("binary_sensor.ecolink_doorwindow_sensor_sensor_4") == "off"\
            and self.get_state("binary_sensor.ecolink_doorwindow_sensor_sensor_5") == "off":
#            self.turn_off("")
#            self.turn_off("")
#            self.turn_off("")
            self.repeatpolice = False
            self.sendalerts("74a8f76a049ee3ef8dd12677f135d8f2")
            self.log("☠️ this is a deactivate test☠️")
            
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    SEND ALERT THROUGH CALL BACK
    
    def whateverdude(self, entity, attribute, old, new, kwargs):
            self.buddyalert("http://192.168.1.230:81/admin?user=buddy3984&pw=1212&profile=3")
        
        #TRIGGER CAMERA
        #http://http://192.168.1.230:81/admin?camera=cornerRoomCam&trigger&user=buddy3984&pw=1212   
            
    def triggercornercam(self, kwargs):    
        url = 'http://http://192.168.1.230:81/admin?camera=cornerRoomCam&trigger&user=buddy3984&pw=1212'
        headers = {'x-ha-access': '7410zz00','content-type': 'application/json'}
        response = get(url, headers=headers)
        self.log(response.text)
        self.log("ok dude house is now armed")
    
    
    def buddyalert(self, buddyurl):    
        url = '{}'.format(buddyurl)
        headers = {'x-ha-access': '7410zz00','content-type': 'application/json'}
        response = get(url, headers=headers)
        self.log(response.text)
        self.log("ok dude house is now armed")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
       RUN MINUETLEY
        poop = datetime.time(0, 0, 0)
        self.run_minutely(self.shitfuck, poop)
            
    def shitfuck(self, kwargs): 
        self.log("poo nuts the tmeier workes bro")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
GET WEEKDAY NUMBER
        poo = datetime.date.today().weekday()
        self.log(poo)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
import datetime
from datetime import timedelta
from requests import get

class frontyardalert(hass.Hass):
    def initialize(self):
        self.buddytimer = datetime.datetime(2010, 12, 12, 12, 12, 12)
        self.speakalert = ""
        self.wheredamotionat = ""
        #
        self.listen_state(self.tripwirefrontactive, "binary_sensor.ecolink_doorwindow_sensor_sensor_3", new= "off")
        self.listen_state(self.camsandporchmotion, "binary_sensor.motion_driveway_camera", new= "on")
        self.listen_state(self.camsandporchmotion, "binary_sensor.motion_front_door", new= "on")
        self.listen_state(self.camsandporchmotion, "binary_sensor.motion_front_yard", new= "on")
        self.listen_state(self.frontyardfrontdooranddrivewaycam, "binary_sensor.motion_front_door", new= "on")
        self.listen_state(self.frontyardfrontdooranddrivewaycam, "binary_sensor.motion_front_yard", new= "on")
    #
    #
    #FRONT YARD AND FRONT DOOR CAM MOTION
    def frontyardfrontdooranddrivewaycam(self, entity, attribute, old, new, kwargs):
        if  self.get_state("binary_sensor.motion_front_door") == "on"\
            and self.get_state("binary_sensor.motion_front_yard") == "on"\
            and self.now_is_between("08:01:00", "12:33:00") == True\
            and self.buddytimer < self.datetime():
            self.buddytimer = self.datetime() + timedelta(seconds=+33)
            self.wheredamotionat = "front yard and front door motion"
            self.buddyalert()
    #
    #FRONT YARD OR FRONT DOOR CAM AND DRIVEWAY CAM MOTION
    def frontyardfrontdooranddrivewaycam(self, entity, attribute, old, new, kwargs):
        if  self.get_state("binary_sensor.motion_driveway_camera") == "on"\
            and self.now_is_between("08:01:00", "15:33:00") == True\
            and self.buddytimer < self.datetime():
            self.buddytimer = self.datetime() + timedelta(seconds=+33)
            self.wheredamotionat = "front yard or front door plus driveway motion"
            self.buddyalert()
    #
    #FRONT YARD OR FRONT DOOR OR DRIVE WAY CAM AND PORCH MOTION
    def camsandporchmotion(self, entity, attribute, old, new, kwargs):
        if  self.get_state("binary_sensor.motion_porch_motion") == "on"\
            and self.buddytimer < self.datetime():
            self.buddytimer = self.datetime() + timedelta(seconds=+33)
            self.wheredamotionat = "all cams plus porch motion"
            self.buddyalert()
    #
    #TRIP WIRE CONDITION
    def tripwirefrontactive(self, entity, attribute, old, new, kwargs):
        if  self.buddytimer < self.datetime():
            self.buddytimer = self.datetime() + timedelta(seconds=+33)
            self.wheredamotionat = "tripwire motion in front"
            self.buddyalert()
    #
    #GO AHEAD AND SPEAK THAT SHIT
    def buddyalert(self):
        if  datetime.date.today().weekday() == 3\
            and self.now_is_between("06:33:00", "09:33:00") == True:
            self.log("no alerts right now, the mowing guys are out", level = "DEBUG")
        else:
            if  self.now_is_between("23:57:00", "06:57:00") == True:
                self.speakalert = "alert!! trip wire is active right now. someone could be outside"
            else:
                self.speakalert = "hey bitch!!  you got someone creeping up on you in your driveway"
            self.triggercornercam()
            self.dude = self.run_at(self.alertinthepasttimer, self.buddytimer)
            if  self.get_state("device_tracker.life360_aileen_") == "home"\
                and datetime.date.today().weekday() in [0, 1, 2, 3, 4]\
                and self.now_is_between("18:57:00", "21:00:00") == True:
                self.log("aileen is about to enter", level = "DEBUG")
                self.log("the front yard alert shit didn't work")
            else:
                self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = "", language= "en-au")
                self.slimball = self.run_in(self.goaheadandtalkbitch, 3)
    #TIMERS NEED KWARGS
    def goaheadandtalkbitch(self, kwargs):
        self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = "{}".format(self.speakalert), language= "en-au")
        self.log("google said the shit")
    #TIMERS NEED KWARGS
    def alertinthepasttimer(self, kwargs):
        self.log("ready to fire again")
    #
    #TIGGER FRONT YARD ALERT MESSAGE
    def triggercornercam(self):    
        url = 'http://192.168.1.230:81/admin?camera=cornerRoomCam&trigger&user=buddy3984&pw=1212'
        headers = {'x-ha-access': '7410zz00','content-type': 'application/json'}
        response = get(url, headers=headers)
        sex = str(response.text)
        num = sex.find("camera=")
        self.log("blue iris alert sent to {} at {} for {}".format(sex[num+7:num+20], self.time(), self.wheredamotionat))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
CALL A FUCNTION AND RANDOM

self.poop()
    
    def poop(self):
          self.log(random.choice(self.foo))

sensor_state = self.entities.binary_sensor.downstairs_sensor.state

OR

        self.poo(self, "", "", "", "")
    #
    #
    def poo(self, entity, attribute, old, new, kwargs):
        self.log("shit balls test")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
OFFICE TEST FOR FRONT TRIPWIRE
import appdaemon.plugins.hass.hassapi as hass
import datetime
import random
from requests import get

class officelighttest(hass.Hass):
    def initialize(self):
        self.alertinthepastthirtythreeseconds = False
        self.speakalert = ""
        #
#        self.frontyardfrontdooranddrivewaycam()
    #
    #
    #FRONT YARD AND FRONT DOOR CAM MOTION
    def frontyardfrontdooranddrivewaycam(self):
        if  self.get_state("binary_sensor.motion_front_door") == "off"\
            and self.get_state("binary_sensor.motion_front_yard") == "off":
            self.buddyalert()
            self.log("front yard and front door motion")
    
    def buddyalert(self):
        if  datetime.date.today().weekday() == 3\
            and self.now_is_between("06:33:00", "09:33:00") == True:
            self.log("no alerts right now, the mowing guys are out", level = "DEBUG")
        else:
            if  self.now_is_between("23:57:00", "06:57:00") == True:
                self.speakalert = "alert!! trip wire is active right now. someone could be outside"
                volumelevel = 0.3
            else:
                self.speakalert = "hey bitch!!  you got someone creeping up on you in your driveway"
                volumelevel = 0.9
        self.triggercornercam()
        self.dude = self.run_in(self.alertinthepasttimer, 33)
        self.log("ran at {}".format(self.time()))
        if  self.anyone_home() == True:
            self.call_service("media_player/volume_set", entity_id = "media_player.buddyalerts", volume_level = volumelevel)
            self.slimball = self.run_in(self.goaheadandtalkbitch, 3)
    #TIMERS NEED KWARGS
    def goaheadandtalkbitch(self, kwargs):
        self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = "{}".format(self.speakalert), language= "en-au")
        self.log("google said the shit")
    #TIMERS NEED KWARGS
    def alertinthepasttimer(self, kwargs):
        self.alertinthepastthirtythreeseconds = False
        self.log("ready to fire again")
    #
    #TIGGER FRONT YARD ALERT MESSAGE
    def triggercornercam(self):    
        url = 'http://192.168.1.230:81/admin?camera=cornerRoomCam&trigger&user=buddy3984&pw=1212'
        headers = {'x-ha-access': '7410zz00','content-type': 'application/json'}
        response = get(url, headers=headers)
        self.log(response.text)
        self.log("alert send to blue iris")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
TRIGGER AND ACTION IF STATMENT TRIGGER SOMETHING

self.listen_state(self.pottyboxalert, "sensor.zooz_zen15_power_switch_power")
        
    def pottyboxalert(self, entity, attribute, old, new, kwargs):
        poo = float(new)
        threshold = 3
        if  poo < threshold:
            self.log("my shit worked")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass

class laundryalert(hass.Hass):
    def initialize(self):
        #VARIABLES
        self.runonce = False
        self.machineison = False
        #TRIGGERS
        self.listen_state(self.laundryalert, "sensor.zooz_zen15_power_switch_power")
    #
    def laundryalert(self, entity, attribute, old, new, kwargs):
        if  float(new) > 3\
            and self.runonce == False:
            self.runonce = True
            self.run_in(self.islaundrymachinerunning, 33)
        else:
            if  self.machineison == True\
                and float(new) < 3:
                self.machineison = False
                self.run_in(self.islaundrymachineoff, 33)
    #
    def islaundrymachinerunning(self, kwargs):     
        digits = self.get_state("sensor.zooz_zen15_power_switch_power")
        if  float(digits) > 3:
            self.runonce = False
            self.machineison = True
            self.log("laundry machine active and operating at {}w".format(float(digits)))
    #
    def islaundrymachineoff(self, kwargs):     
        digits = self.get_state("sensor.zooz_zen15_power_switch_power")
        if  float(digits) < 3:
            self.log("laundry machine is OFF and now at {}w".format(float(digits)))
            if  self.anyone_home() == True:
                self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = " ", language= "en-au")
                self.speakalert = self.run_in(self.goaheadandtalkbitch, 3)
    #
    #NOTIFY MACHINE IS OFF
    def goaheadandtalkbitch(self, kwargs):
        self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = "excuse me eileen. sorry to bother you but you should check the laundry machine because i think the cycle is done.", language= "en-au")
        self.log("laundry speech given.. its now off")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import appdaemon.plugins.hass.hassapi as hass
import datetime
from requests import get

class frontyardalert(hass.Hass):
    def initialize(self):
        self.alertinthepastthirtythreeseconds = False
        self.speakalert = ""
        #
        self.listen_state(self.tripwirefrontactive, "binary_sensor.ecolink_doorwindow_sensor_sensor_3", new= "off")
        self.listen_state(self.camsandporchmotion, "binary_sensor.motion_driveway_camera", new= "on")
        self.listen_state(self.camsandporchmotion, "binary_sensor.motion_front_door", new= "on")
        self.listen_state(self.camsandporchmotion, "binary_sensor.motion_front_yard", new= "on")
        self.listen_state(self.frontyardfrontdooranddrivewaycam, "binary_sensor.motion_front_door", new= "on")
        self.listen_state(self.frontyardfrontdooranddrivewaycam, "binary_sensor.motion_front_yard", new= "on")
    #
    #
    #FRONT YARD AND FRONT DOOR CAM MOTION
    def frontyardfrontdooranddrivewaycam(self, entity, attribute, old, new, kwargs):
        if  self.get_state("binary_sensor.motion_front_door") == "on"\
            and self.get_state("binary_sensor.motion_front_yard") == "on"\
            and self.now_is_between("08:01:00", "12:33:00") == True:
            self.buddyalert()
            self.log("front yard and front door motion")
    #
    #FRONT YARD OR FRONT DOOR CAM AND DRIVEWAY CAM MOTION
    def frontyardfrontdooranddrivewaycam(self, entity, attribute, old, new, kwargs):
        if  self.get_state("binary_sensor.motion_driveway_camera") == "on"\
            and self.now_is_between("08:01:00", "15:33:00") == True: 
            self.buddyalert()
            self.log("front yard or front door plus driveway motion")
    #
    #FRONT YARD OR FRONT DOOR OR DRIVE WAY CAM AND PORCH MOTION
    def camsandporchmotion(self, entity, attribute, old, new, kwargs):
        if  self.get_state("binary_sensor.motion_porch_motion") == "on":
            self.buddyalert()
            self.log("all cams plus porch motion")
    #
    #TRIP WIRE CONDITION
    def tripwirefrontactive(self, entity, attribute, old, new, kwargs):
        if  self.alertinthepastthirtythreeseconds == False:
            self.alertinthepastthirtythreeseconds = True
            self.buddyalert()
            self.log("we got tripwire motion in front")
    #
    #GO AHEAD AND SPEAK THAT SHIT
    def buddyalert(self):
        if  datetime.date.today().weekday() == 3\
            and self.now_is_between("06:33:00", "09:33:00") == True:
            self.log("no alerts right now, the mowing guys are out", level = "DEBUG")
        else:
            if  self.now_is_between("23:57:00", "06:57:00") == True:
                self.speakalert = "alert!! trip wire is active right now. someone could be outside"
                volumelevel = 0.3
            else:
                self.speakalert = "hey bitch!!  you got someone creeping up on you in your driveway"
                volumelevel = 0.9
        self.triggercornercam()
        self.dude = self.run_in(self.alertinthepasttimer, 33)
        self.log("ran at {}".format(self.time()))
        if  self.anyone_home() == True:
            self.call_service("media_player/turn_on", entity_id = "media_player.buddyalerts")
            self.slimball = self.run_in(self.goaheadandtalkbitch, 3)
    #TIMERS NEED KWARGS
    def goaheadandtalkbitch(self, kwargs):
        self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = "{}".format(self.speakalert), language= "en-au")
        self.log("google said the shit")
    #TIMERS NEED KWARGS
    def alertinthepasttimer(self, kwargs):
        self.alertinthepastthirtythreeseconds = False
        self.log("ready to fire again")
    #
    #TIGGER FRONT YARD ALERT MESSAGE
    def triggercornercam(self):    
        url = 'http://192.168.1.230:81/admin?camera=cornerRoomCam&trigger&user=buddy3984&pw=1212'
        headers = {'x-ha-access': '7410zz00','content-type': 'application/json'}
        self.log("alert send to blue iris")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
EXTRACT TEXT FROM STRING URL FORMAT GET FIND TEXT IN STRING

    def poo(self, kwargs):
        url = 'http://192.168.1.230:81/admin?camera=cornerRoomCam&trigger&user=buddy3984&pw=1212'
        headers = {'x-ha-access': '7410zz00','content-type': 'application/json'}
        response = get(url, headers=headers)
        sex = str(response.text)
        num = sex.find("profile=")
        self.log("blue iris is now set to {}".format(sex[num:num+9]))
        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
RUN ONCE timer_handle

import appdaemon.plugins.hass.hassapi as hass
import datetime
from datetime import timedelta
import random
from requests import get

class officelighttest(hass.Hass):
    def initialize(self):
        ##########from datetime import timedelta##########################################
        #1 VARIABLE
        self.buddytimer = datetime.datetime(2010, 12, 12, 12, 12, 12)
        #
#        self.poo(self, "", "", "", "")
        self.run_in(self.poo, 0)
        #
    def poo(self, kwargs):
        #2 IF STATEMENT
        if  self.buddytimer < self.datetime():
            self.log("do some shite")
        #3 ADD TIME TO THE TIMER
            self.buddytimer = self.datetime() + timedelta(hours=+12)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
LAUNDRY COPY
import appdaemon.plugins.hass.hassapi as hass

class laundryalert(hass.Hass):
    def initialize(self):
        #VARIABLES
        self.runonce = False
        self.machineison = False
        #TRIGGERS
        self.listen_state(self.laundryalert, "sensor.zooz_zen15_power_switch_power")
    #
    def laundryalert(self, entity, attribute, old, new, kwargs):
        if  float(new) > 3\
            and self.runonce == False:
            self.runonce = True
            self.laundryrun = self.run_in(self.islaundrymachinerunning, 33)
        else:
            if  self.machineison == True\
                and float(new) < 3:
                self.machineison = False
                self.laundryoff = self.run_in(self.islaundrymachineoff, 33)
    #
    def islaundrymachinerunning(self, kwargs):     
        digits = self.get_state("sensor.zooz_zen15_power_switch_power")
        if  float(digits) > 3:
            self.runonce = False
            self.machineison = True
#            self.log("laundry machine active and operating at {}w".format(float(digits)))
    #
    def islaundrymachineoff(self, kwargs):     
        digits = self.get_state("sensor.zooz_zen15_power_switch_power")
        if  float(digits) < 3:
            self.log("laundry machine is OFF and now at {}w".format(float(digits)))
            if  self.anyone_home() == True:
                self.runonce = False
                self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = " ", language= "en-au")
                self.speakalert = self.run_in(self.goaheadandtalkbitch, 3)
    #
    #NOTIFY MACHINE IS OFF
    def goaheadandtalkbitch(self, kwargs):
        self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = "excuse me eileen. sorry to bother you but you should check the laundry machine because i think the cycle is done.", language= "en-au")
        self.log("laundry speech given.. its now off")


### GET TIME TERMINAL
date '+%A %W %Y %X'

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
FRONTYARD ALERT BACKUP
import appdaemon.plugins.hass.hassapi as hass
import datetime
from requests import get

class frontyardalert(hass.Hass):
    def initialize(self):
        self.alertinthepastthirtythreeseconds = False
        self.speakalert = ""
        self.alertfired = False
        #
        self.listen_state(self.tripwirefrontactive, "binary_sensor.ecolink_doorwindow_sensor_sensor_3", new= "off")
        self.listen_state(self.camsandporchmotion, "binary_sensor.motion_driveway_camera", new= "on")
        self.listen_state(self.camsandporchmotion, "binary_sensor.motion_front_door", new= "on")
        self.listen_state(self.camsandporchmotion, "binary_sensor.motion_front_yard", new= "on")
        self.listen_state(self.frontyardfrontdooranddrivewaycam, "binary_sensor.motion_front_door", new= "on")
        self.listen_state(self.frontyardfrontdooranddrivewaycam, "binary_sensor.motion_front_yard", new= "on")
    #
    #
    #FRONT YARD AND FRONT DOOR CAM MOTION
    def frontyardfrontdooranddrivewaycam(self, entity, attribute, old, new, kwargs):
        if  self.get_state("binary_sensor.motion_front_door") == "on"\
            and self.get_state("binary_sensor.motion_front_yard") == "on"\
            and self.now_is_between("08:01:00", "12:33:00") == True\
            and self.alertinthepastthirtythreeseconds == False:
            self.alertinthepastthirtythreeseconds = True
            self.buddyalert()
            self.log("front yard and front door motion")
    #
    #FRONT YARD OR FRONT DOOR CAM AND DRIVEWAY CAM MOTION
    def frontyardfrontdooranddrivewaycam(self, entity, attribute, old, new, kwargs):
        if  self.get_state("binary_sensor.motion_driveway_camera") == "on"\
            and self.now_is_between("08:01:00", "15:33:00") == True\
            and self.alertinthepastthirtythreeseconds == False:
            self.alertinthepastthirtythreeseconds = True
            self.buddyalert()
            self.log("front yard or front door plus driveway motion")
    #
    #FRONT YARD OR FRONT DOOR OR DRIVE WAY CAM AND PORCH MOTION
    def camsandporchmotion(self, entity, attribute, old, new, kwargs):
        if  self.get_state("binary_sensor.motion_porch_motion") == "on"\
            and self.alertinthepastthirtythreeseconds == False:
            self.alertinthepastthirtythreeseconds = True
            self.buddyalert()
            self.log("all cams plus porch motion")
    #
    #TRIP WIRE CONDITION
    def tripwirefrontactive(self, entity, attribute, old, new, kwargs):
        if  self.alertinthepastthirtythreeseconds == False:
            self.alertinthepastthirtythreeseconds = True
            self.buddyalert()
            self.log("we got tripwire motion in front")
    #
    #GO AHEAD AND SPEAK THAT SHIT
    def buddyalert(self):
        if  self.alertfired == False\
            and datetime.date.today().weekday() == 3\
            and self.now_is_between("06:33:00", "09:33:00") == True:
            self.log("no alerts right now, the mowing guys are out", level = "DEBUG")
        else:
            if  self.now_is_between("23:57:00", "06:57:00") == True:
                self.speakalert = "alert!! trip wire is active right now. someone could be outside"
                self.alertfired = True
            else:
                self.speakalert = "hey bitch!!  you got someone creeping up on you in your driveway"
                self.alertfired = True
            self.triggercornercam()
            self.dude = self.run_in(self.alertinthepasttimer, 33)
            self.log("ran at {}".format(self.time()))
            if  self.anyone_home() == True:
                self.call_service("media_player/turn_on", entity_id = "media_player.buddyalerts")
                self.slimball = self.run_in(self.goaheadandtalkbitch, 3)
    #TIMERS NEED KWARGS
    def goaheadandtalkbitch(self, kwargs):
        self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = "{}".format(self.speakalert), language= "en-au")
        self.log("google said the shit")
    #TIMERS NEED KWARGS
    def alertinthepasttimer(self, kwargs):
        self.alertinthepastthirtythreeseconds = False
        self.alertfired = False
        self.log("ready to fire again")
    #
    #TIGGER FRONT YARD ALERT MESSAGE
    def triggercornercam(self):    
        url = 'http://192.168.1.230:81/admin?camera=cornerRoomCam&trigger&user=buddy3984&pw=1212'
        headers = {'x-ha-access': '7410zz00','content-type': 'application/json'}
        response = get(url, headers=headers)
        sex = str(response.text)
        num = sex.find("camera=")
        self.log("blue iris alert sent to {} for front yard alert".format(sex[num+7:num+20]))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import appdaemon.plugins.hass.hassapi as hass
import datetime

class pottybox(hass.Hass):
    def initialize(self):
        self.pottyalert = ''
        self.listen_state(self.pottyboxalert, "binary_sensor.motion_pottybox", new= "on")
        self.listen_state(self.fireplacelert, "binary_sensor.motion_fireplace", new= "on")
    
    
    def pottyboxalert(self, entity, attribute, old, new, kwargs):
        if  self.anyone_home() == True:
            self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = "", language= "en-au")
            self.pottyalert = "hey yo! check the potty box dumbo"
            self.speakalert = self.run_in(self.goaheadandtalkbitch, 3)
    
    
    def fireplacelert(self, entity, attribute, old, new, kwargs):
        if  self.anyone_home() == True:
            self.pottyalert = "bugsy!! no potty there!"
            self.speakalert = self.run_in(self.goaheadandtalkbitch, 0)
    
    
    #TIMERS NEED KWARGS
    def goaheadandtalkbitch(self, kwargs):
        self.call_service("tts/google_say", entity_id = "media_player.buddyalerts", message = self.pottyalert, language= "en-au")
        if  self.potyalert == "bugsy!! no potty there!":
            self.log("bugsy is on the fireplace!!")
        else:
            self.log("pottybox alert fired bro")
            
            
            
            - id: '1533086819877'
  alias: testTurnOffKitchenTvAfterTurnsOn
  trigger:
  - entity_id: media_player.kitchen_tv
    from: idle
    platform: state
    to: idle
  condition: []
  action:
  - delay: 00:00:33
  - data:
      entity_id: media_player.kitchen_tv
    service: media_player.turn_off
- id: '1533111186466'
  alias: cunt
  trigger:
  - entity_id: script.1533109474843
    from: 'off'
    platform: state
    to: 'on'
  condition: []
  action:
  - data:
      entity_id: media_player.kitchen_tv
      media_content_id: http://192.168.1.230:81/mjpg/pottybox/video.mjpg
      media_content_type: image/jpg
    service: media_player.media_play
