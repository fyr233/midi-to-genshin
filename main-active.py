# coding:utf-8
# main-active是主动端，负责解析midi、通过http发送按键事件给被动端（多个）
# 主动端将监听热键，在游戏后台开始播放

import mido
import keyboard
import requests
import json
from threading import Timer

from config import config_active as config

class Note:
    def __init__(self, time, pitch, velocity, key_signature):
        self.time = time
        self.pitch = pitch
        self.velocity = velocity
        self.key_signature = key_signature

Track = []

def loadMidiFile():

    key_signature = config['key_note']['G']
    tempo = 500000
    globaltime = 0.0
    Track_tmp = []

    for filename in config['midifile']:
        
        mid = mido.MidiFile(filename, clip=True)
        print(mid.filename, mid.length, mid.ticks_per_beat)

        for i, track in enumerate(mid.tracks):
            print('Track', i, track.name)

            starttime = globaltime
            for msg in track:

                globaltime += msg.time / mid.ticks_per_beat * tempo / 1000000
                if msg.type == 'key_signature':
                    key_signature = config['key_note'][msg.key]
                elif msg.type == 'set_tempo':
                    tempo = msg.tempo
                elif msg.type == 'note_on':
                    Track_tmp.append(Note(globaltime, msg.note, msg.velocity, key_signature))
            
            globaltime = starttime
        
        globaltime += mid.length
    
    Track_tmp.sort(key= lambda item: item.time)
    print([(i.time,i.pitch, i.key_signature) for i in Track_tmp[:100]])
    Track.append(Track_tmp[0])
    Track[0].pitch = [Track_tmp[0].pitch]

    for i in range(1, len(Track_tmp)):
        if Track_tmp[i].time - Track[-1].time < 8e-2:
            Track[-1].pitch.append(Track_tmp[i].pitch)
        else:
            Track.append(Track_tmp[i])
            Track[-1].pitch = [Track_tmp[i].pitch]

    print([(i.time,i.pitch, i.key_signature) for i in Track[:100]])

def play(index):
    if index+1 >= len(Track):
        index = 0
    print(index, end='\r')
    url = 'http://' + config['passive_server'][0]['ip'] + ':' + config['passive_server'][0]['port'] + '/playnote'
    data={
            'pitch': Track[index].pitch,
            'key': Track[index].key_signature
        }
    print(data)
    r = requests.post(
        url,
        json=json.dumps(data)
    )
    t = Timer(
        Track[index+1].time - Track[index].time,
        play,
        (index+1,)
    )
    t.start()

def beginPlay():
    play(0)

if __name__ == '__main__':
    loadMidiFile()

    beginPlay()