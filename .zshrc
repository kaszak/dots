# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
setopt appendhistory autocd
unsetopt beep
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/kaszak/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

# SUCK IT, POLKIT
#alias poweroff="sudo poweroff"
#alias reboot="sudo reboot"
BROWSER=chromium
EDITOR=nano
export PATH="/home/kaszak/bin:$PATH"
