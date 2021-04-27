import subprocess

apps = [
    " polybar",
    " i3-wm",
    " neovim",
    " firefox",
    " nitrogen",
    " rofi",
    " pcmanfm",
    "nnn",
    "zsh",
    "powerline",
    
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
    "cp -r i3 i3blocks nvim polybar qtile termite ~/.config",
    # Setting up zsh
    "curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh",
    'mkdir -p "$HOME/.zsh"',
    'git clone https://github.com/sindresorhus/pure.git "$HOME/.zsh/pure"',
    'git clone https://github.com/denysdovhan/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt" --depth=1',
    'ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"',
    'sudo git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions',
    'sudo git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting',
    'cp ~/config/.zshrc ~',
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
