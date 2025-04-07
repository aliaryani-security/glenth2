def ert(time) -> dict :
    try:
        time = float(time)
    except:
        return
    hr = int(float(time / 60 / 60))
    mn = int(( time /60) % 60)
    return {'hr' : hr , 'mn' : mn}