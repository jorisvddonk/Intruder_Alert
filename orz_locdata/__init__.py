# adapted from uqm/comm/orz/orzc.c

ONE_SECOND = 1
CIRCULAR_ANIM = "CIRCULAR_ANIM"
RANDOM_ANIM = "RANDOM_ANIM"
YOYO_ANIM = "YOYO_ANIM"

AMBIENT_ANIM = [
    {
        "StartIndex": 4,  # StartIndex
        "NumFrames": 6,  # NumFrames
        "AnimFlags": CIRCULAR_ANIM,  # AnimFlags
        "FrameRate": [ONE_SECOND / 10, 0],  # FrameRate
        "RestartRate": [ONE_SECOND, ONE_SECOND * 3],  # RestartRate
        "BlockMask": 0,  # BlockMask
    },
    {
        "StartIndex": 10,  # StartIndex
        "NumFrames": 5,  # NumFrames
        "AnimFlags": CIRCULAR_ANIM,  # AnimFlags
        "FrameRate": [ONE_SECOND / 10, 0],  # FrameRate
        "RestartRate": [ONE_SECOND, ONE_SECOND * 3],  # RestartRate
        "BlockMask": 0,  # BlockMask
    },
    {
        "StartIndex": 15,  # StartIndex
        "NumFrames": 2,  # NumFrames
        "AnimFlags": RANDOM_ANIM,  # AnimFlags
        "FrameRate": [ONE_SECOND / 10, ONE_SECOND / 10],  # FrameRate
        "RestartRate": [ONE_SECOND, ONE_SECOND * 3],  # RestartRate
        "BlockMask": 0,  # BlockMask
    },
    {
        "StartIndex": 17,  # StartIndex
        "NumFrames": 3,  # NumFrames
        "AnimFlags": YOYO_ANIM,  # AnimFlags
        "FrameRate": [ONE_SECOND / 10, ONE_SECOND / 10],  # FrameRate
        "RestartRate": [ONE_SECOND, ONE_SECOND * 3],  # RestartRate
        "BlockMask": 0,  # BlockMask
    },
    {
        "StartIndex": 20,  # StartIndex
        "NumFrames": 2,  # NumFrames
        "AnimFlags": YOYO_ANIM,  # AnimFlags
        "FrameRate": [ONE_SECOND / 10, 0],  # FrameRate
        "RestartRate": [ONE_SECOND / 10, ONE_SECOND * 3],  # RestartRate
        "BlockMask": (1 << 7),  # BlockMask
    },
    {
        "StartIndex": 22,  # StartIndex
        "NumFrames": 8,  # NumFrames
        "AnimFlags": CIRCULAR_ANIM,  # AnimFlags
        "FrameRate": [ONE_SECOND / 10, 0],  # FrameRate
        "RestartRate": [ONE_SECOND / 10, ONE_SECOND * 3],  # RestartRate
        "BlockMask": (1 << 6),  # BlockMask
    },
    {
        "StartIndex": 30,  # StartIndex
        "NumFrames": 3,  # NumFrames
        "AnimFlags": CIRCULAR_ANIM,  # AnimFlags
        "FrameRate": [ONE_SECOND / 10, 0],  # FrameRate
        "RestartRate": [ONE_SECOND / 10, ONE_SECOND * 3],  # RestartRate
        "BlockMask": (1 << 5),  # BlockMask
    },
    {
        "StartIndex": 33,  # StartIndex
        "NumFrames": 3,  # NumFrames
        "AnimFlags": YOYO_ANIM,  # AnimFlags
        "FrameRate": [ONE_SECOND / 10, 0],  # FrameRate
        "RestartRate": [ONE_SECOND / 10, ONE_SECOND * 3],  # RestartRate
        "BlockMask": (1 << 4),  # BlockMask
    },
    {
        "StartIndex": 36,  # StartIndex
        "NumFrames": 25,  # NumFrames
        "AnimFlags": CIRCULAR_ANIM,  # AnimFlags
        "FrameRate": [ONE_SECOND / 60, ONE_SECOND / 15],  # FrameRate
        "RestartRate": [ONE_SECOND, ONE_SECOND * 3],  # RestartRate
        "BlockMask": 0,  # BlockMask
    },
    {
        "StartIndex": 61,  # StartIndex
        "NumFrames": 15,  # NumFrames
        "AnimFlags": CIRCULAR_ANIM,  # AnimFlags
        "FrameRate": [ONE_SECOND / 60, ONE_SECOND / 15],  # FrameRate
        "RestartRate": [ONE_SECOND, ONE_SECOND * 3],  # RestartRate
        "BlockMask": 0,  # BlockMask
    },
    {
        "StartIndex": 76,  # StartIndex
        "NumFrames": 17,  # NumFrames
        "AnimFlags": CIRCULAR_ANIM,  # AnimFlags
        "FrameRate": [ONE_SECOND / 60, ONE_SECOND / 15],  # FrameRate
        "RestartRate": [ONE_SECOND, ONE_SECOND * 3],  # RestartRate
        "BlockMask": (1 << 12),  # BlockMask
    },
    {
        "StartIndex": 93,  # StartIndex
        "NumFrames": 25,  # NumFrames
        "AnimFlags": CIRCULAR_ANIM,  # AnimFlags
        "FrameRate": [ONE_SECOND / 60, ONE_SECOND / 15],  # FrameRate
        "RestartRate": [ONE_SECOND, ONE_SECOND * 3],  # RestartRate
        "BlockMask": 0,  # BlockMask
    },
    {
        "StartIndex": 118,  # StartIndex
        "NumFrames": 11,  # NumFrames
        "AnimFlags": CIRCULAR_ANIM,  # AnimFlags
        "FrameRate": [ONE_SECOND / 60, ONE_SECOND / 15],  # FrameRate
        "RestartRate": [ONE_SECOND, ONE_SECOND * 3],  # RestartRate
        "BlockMask": (1 << 10),  # BlockMask
    },
]
TRANSITION_DESC = {  # AlienTransitionDesc
    0,  # StartIndex
    0,  # NumFrames
    0,  # AnimFlags
    0, 0,  # FrameRate
    0, 0,  # RestartRate
    0,  # BlockMask
}


TALK_DESC = {  # AlienTalkDesc
    1,  # StartIndex
    3,  # NumFrames
    0,  # AnimFlags
    ONE_SECOND / 15, ONE_SECOND / 15,  # FrameRate
    ONE_SECOND / 12, ONE_SECOND * 3 / 8,  # RestartRate
    0,  # BlockMask
}
