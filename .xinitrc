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

#wicd-client --tray
#urxvtd
xset +fp /usr/share/fonts/local
xset fp rehash
[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"
mpd ~/.mpdconf
# NUKE CAPS, FFS
xmodmap -e 'keycode  66 = NoSymbol Caps_Lock Caps_Lock'
exec i3

#DEFAULT_SESSION=awesome
#case $1 in
#  awesome|wmii|xmonad) exec $1 ;;
#  *) exec $DEFAULT_SESSION ;;
#esac
