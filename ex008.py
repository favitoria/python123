v = float(input('Bodia, digite um valor em metros faz favor: '))
km = v/1000
hm = v/100
dam = v/10
dm = v*10
cm = v*100
mm = v*1000
print('Este valor {} equivale à\n km={}\n hm={}\n dam={}\n dm={:.0f}\n cm={:.0f}\n mm={:.0f}'.format(v, km, hm, dam, dm, cm, mm))
