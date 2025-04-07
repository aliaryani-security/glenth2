def ert(time) -> dict :
    time = float(time)
    hr = int(float(time / 60 / 60))
    mn = int(( time /60) % 60)
    return {'hr' : hr , 'mn' : mn}