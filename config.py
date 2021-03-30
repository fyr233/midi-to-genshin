# coding:utf-8
# 参数配置部分

#以下为main-active的参数
config_active = {
    'hotkey': {
        'begin': 'f9',
        'pause': 'f10',
        'end': 'f11',
        'restart': 'f12'
    },
    'midifile': [
        'midi/Animenz- 原神組曲 (B站直播).mid',
        'midi/苏维埃进行曲钢琴.mid',
        'midi/ilem,洛天依,言和-达拉崩吧.mid',
        'midi/病名为爱.mid',
        'midi/九九八十一.mid',
        'midi/夜的第七章.mid',
        'midi/一剪梅.mid',
        'midi/東方紅魔郷U.N.オーエンは彼女なのか？.mid',
        'midi/东方萃梦想.mid',
        'midi/极乐净土.mid'
    ],
    'velocity_threshold': {
        '1': [],
        '2': [90],
        '3': [80, 100],
        '4': [70, 90, 110],
    },
    'passive_server': [
        {
            'ip': '192.168.1.107',
            'port': '4000',
            'delay': 10# 延迟，ms
        }
    ],
    'delay': 10,# 延迟，ms
    'key_note': {
        "G": 55,
        "Ab": 56,
        "A": 57,
        "Bb": 58,
        "B": 59,
        "C": 60,
        "C#": 61,
        "D": 62,
        "D#": 63,
        "Eb": 63,
        "E": 64,
        "F": 65,
        "F#": 66,
        "Gb": 66,
    }
}

#以下为main-passive的参数
config_passive = {
    'key':{
        'do1': 'q',
        're1': 'w',
        'mi1': 'e',
        'fa1': 'r',
        'so1': 't',
        'la1': 'y',
        'ti1': 'u',
        'do2': 'a',
        're2': 's',
        'mi2': 'd',
        'fa2': 'f',
        'so2': 'g',
        'la2': 'h',
        'ti2': 'j',
        'do3': 'z',
        're3': 'x',
        'mi3': 'c',
        'fa3': 'v',
        'so3': 'b',
        'la3': 'n',
        'ti3': 'm',
        'none': 'p'
    },
    'note':{
        0: 'do1',
        2: 're1',
        4: 'mi1',
        5: 'fa1',
        7: 'so1',
        9: 'la1',
        11: 'ti1',
        12: 'do2',
        14: 're2',
        16: 'mi2',
        17: 'fa2',
        19: 'so2',
        21: 'la2',
        23: 'ti2',
        24: 'do3',
        26: 're3',
        28: 'mi3',
        29: 'fa3',
        31: 'so3',
        33: 'la3',
        35: 'ti3',
    }
    
}