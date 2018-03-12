import execjs

f = open('jszhihu.js', 'r').read()
ec = execjs.compile(f)
print ec.call('run', 'password', '1515735035596')