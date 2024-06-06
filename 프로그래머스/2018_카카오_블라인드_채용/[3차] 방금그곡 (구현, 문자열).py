def solution(m, musicinfos):
    def get_play_time(s, e):
        eh, em = e.split(":")
        sh, sm = s.split(":")
        return (int(eh)*60+int(em)) - (int(sh)*60+int(sm))

    def replace(mus):
        mus = mus.replace("C#", 'c')
        mus = mus.replace("D#", 'd')
        mus = mus.replace("F#", 'f')
        mus = mus.replace("G#", 'g')
        mus = mus.replace("A#", 'a')
        mus = mus.replace("B#", 'b')
        return mus

    def get_played_music(pt, mus):
        res = ""
        for i in range(pt):
            res += mus[i%len(mus)]
        return res


    rep_m = replace(m)
    max_length = -1
    result = ""
    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(",")
        play_time = get_play_time(start, end)
        music = replace(music)
        played_music = get_played_music(play_time, music)

        if rep_m in played_music:
            if max_length < play_time:
                max_length = play_time
                result = title

    if result == "":
        return "(None)"

    return result