import subprocess

debianCommands = [
    "sudo apt install polybar",
    "sudo apt install i3-wm",
    "sudo apt install neovim",
    "sudo apt install firefox",
    "sudo apt install nitrogen",
    "sudo apt install rofi",
    "sudo apt install pcmanfm"
    
]

gitCommands = [
    "git clone --recursive https://github.com/thestinger/termite.git",
    "cd termite && make && cd",
    "curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim",
    "git clone https://github.com/Ganther3301/config.git",
    "cd config",
    "cp -r i3 i3blocks nvim polybar qtile termite ~/.config"
]

for i in debianCommands:
    subprocess.run(i, shell=True)

for i in gitCommands:
    subprocess.run(i, shell=True)
