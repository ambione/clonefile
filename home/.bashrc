# • CONFIG BASH •

 # If not running interactively, don't do anything
[[ $- != *i* ]] && return
 
# :: ALIASES 
alias ls='ls --color=auto'
alias la='ls -la'
alias grep='grep --color=auto'
alias AI1='ollama run gemma'
alias AI='ollama run phi3'
alias neo='neofetch'
alias wlan0='iwctl device wlan0 show'
alias up='sudo pacman -Syu'
alias tp='btop'
alias grim='grim screenshot.png'
alias ambione='Hyprland'
alias mp='mpg123 -C -z ~/Músicas/*'
 
# :: PROMPT  [ל]
#PS1="\e[0;32m• ל • "
PS1="\e[0;33m╭─ \e[1;34m\d \e[0;33m• \e[1;37m\t \e[0;33m• \e[1;36m\u \e[0;33m• \e[1;34mcd \w \e[0;33m\n╰•  "
#PS1="\e[0;32m╭─ \e[1;34m\d \e[0;32m• \e[1;37m\t \e[0;32m• \e[1;31m\u \e[0;32m• \e[1;34mcd \w \e[0;32m\n╰•  "
 
# :: DISPLAY SESSION START
#neofetch
#df -h
