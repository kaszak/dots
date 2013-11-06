#!/bin/sh
#
# ~/.xinitrc
#
# Executed by startx (run your window manager from here)

if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

# exec gnome-session
# exec startkde
# exec startxfce4
# ...or the Window Manager of your choice

xset +fp /usr/share/fonts/local
xset fp rehash
[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"
export TERMINAL=urxvtc
export VDPAU_DRIVER=r600
mpd ~/.mpdconf
urxvtd -q -f -o
# NUKE CAPS, FFS
xmodmap -e 'keycode  66 = NoSymbol Caps_Lock Caps_Lock'
unclutter -grab -idle 10 &
exec i3
#exec startkde
