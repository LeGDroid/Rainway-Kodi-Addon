import platform
import os
if platform.system() == 'Windows': child=os.system('start chrome "https://play.rainway.com/" --start-fullscreen')
elif platform.system() == 'Linux': child=os.system('google-chrome "https://play.rainway.com/" --start-fullscreen')
elif platform.system() == 'Darwin': child=os.system('open -a "Google Chrome" https://play.rainway.com/ --start-fullscreen')