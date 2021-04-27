import subprocess

apps = [
    " polybar",
    " i3-wm",
    " neovim",
    " firefox",
    " nitrogen",
    " rofi",
    " pcmanfm"
    
]

gitCommands = [
    # For termite
    "git clone --recursive https://github.com/thestinger/termite.git ~",
    "cd ~/termite && make && cd",
    # For vim-plug
    "curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim",
    # For downloading and placing my config files
    "git clone https://github.com/Ganther3301/config.git ~",
    "cd ~/config",
    "cp -r i3 i3blocks nvim polybar qtile termite ~/.config"
]
invalid = True
while invalid:
    pkg = input("Which operating system, Debian or Arch?[d/a]")
    if pkg == "d" or pkg == "D":
        invalid = False
        for i in apps:
            subprocess.run("sudo apt-get install "+i, shell=True)
    elif pkg == "a" or pkg == "A":
        invalid = False
        for i in apps:
            subprocess.run("sudo pacman -S "+i, shell=True)
    else:
        print("Enter valid option")

for i in gitCommands:
    subprocess.run(i, shell=True)
