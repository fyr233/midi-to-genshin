# coding:utf-8
# main-passive是被动端，负责通过http接收按键事件、模拟键盘输入

import json
import keyboard
from flask import Flask, request

from config import config_passive as config

app = Flask(__name__)

# key_note:"G"=55,"Ab"=56,"A"=57,"Bb"=58,"B"=59,"C"=60,"C#"=61,"D"=62,"D#"=63,"E"=64,"F"=65,"F#"=66
def pitchToKey(v,key):
    print((v - key + 12)%36)
    note_tem = ''
    
    try:
        note_tem = config['note'][(v - key + 12)%36]
    except:
        note_tem = config['note'][(v - key + 12 + 1)%36]
    
    return config['key'][note_tem]

@app.route('/playnote', methods=['POST'])
def playnote():
    #print(request.form)
    pitch = request.form['pitch']

    key = pitchToKey(int(pitch), int(request.form['key']))
    keyboard.press_and_release(key)

    return 'Success'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)