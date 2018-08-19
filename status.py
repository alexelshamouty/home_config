# coding=utf-8
from i3pystatus import Status
import psutil
import subprocess
import netifaces

def spawn(*args):
    def wrapper():
        subprocess.Popen(args)
    return wrapper

status = Status(standalone=True,logfile='$HOME/i3pystatus.log')

#clock.Clock.on_leftclick = ""
status.register("clock",
        on_leftclick=[spawn('/usr/bin/xterm', '-class', 'Float', '-geometry', '74x9', '-e', 'cal -3 -w; read')],
        #on_leftclick=[['wpa_gui']],
        format=" %a %-d %b %H:%M")

status.register("pulseaudio",
    format="♪{volume}",
	on_upscroll=[spawn('/usr/bin/pulseaudio-ctl','up')],
	on_downscroll=[spawn('/usr/bin/pulseaudio-ctl','down')],
	)

status.register('now_playing',
                status={'play': '',
                'pause': '',
                'stop': ''})

status.register("temp",
    format="{temp:.0f}°C",)

status.register("xkblayout",
#    format='{symbol}',
    layouts= ["us", "ar"],)

status.register("cpu_usage_bar",
                format='<span color="#FFFFFF"></span> {usage_bar}',
                hints = {"markup": "pango"},
                on_leftclick=[spawn('/usr/sbin/sudo', '/usr/bin/cpupower-gui')],
                bar_type='horizontal'
                )
status.register("mem",
                hints = {"markup": "pango"},
                format='<span color="#FFFFFF"> </span> {used_mem} / {total_mem} GiB',
                on_leftclick=[spawn('/usr/bin/xterm', '-class', 'Float', '-geometry', '120x40', '-e', 'htop')],
                divisor=1024**3)


status.register("disk",
	format='<span color="#FFFFFF">{percentage_used}%</span>',
	hints = {"markup": "pango"},
	path = '/',
	)
status.register("network",
    interface="eno1",
    color_up='#FFFFFF',
    on_leftclick=[spawn('sudo', 'systemctl', 'restart', 'dhcpcd')],
    format_up="{v4}",)
status.register("network",
    interface="virbr1",
    color_up='#FFFFFF',
    on_leftclick=[spawn('sudo', 'systemctl', 'restart', 'dhcpcd')],
    format_up="{v4}",)

wfaces = list(filter(lambda x: x.startswith('w'), netifaces.interfaces()))
if wfaces:
    status.register("network",
        interface=wfaces[0],
        on_leftclick=[spawn('wpa_gui', '-i', 'wlan0')],
        color_up='#FFFFFF',
        format_up="{essid}",)
status.register("weatherme")
#status.register("network",
#    interface="bond0",
#    divisor=1024,
#    start_color='white',
#    format_up=" {bytes_recv}K  {bytes_sent}K",)

#status.register("file",
#        components={'bond': (str, '/sys/class/net/bond0/bonding/active_slave')},
#        format="{bond}")

status.run()


