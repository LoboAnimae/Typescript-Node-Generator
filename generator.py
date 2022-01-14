import os
import bash_checker


def main():
    real_path = os.path.realpath(__file__)
    dir_path = os.path.dirname(real_path)
    os.chdir(dir_path)
    os.chdir('..')
    os.system('cls' if os.name == 'nt' else 'clear')
    name = input('What is the name of the project?\n>>> ')
    os.system('mkdir ' + name)
    os.chdir(name)
    bash_checker.check_bash_command_exists(['node', 'npm', 'git'])
    installerCommand = 'npm install'
    installerDevCommand = 'npm install --save-dev'
    try:
        bash_checker.check_bash_command_exists_single('yarn')
        installerCommand = 'yarn add'
        installerDevCommand = 'yarn add -D'
    except:
        pass
    os.system(
        'git clone https://github.com/LoboAnimae/Typescript-NodeJS-Template.git .')
    os.system('rm ./package.json')
    os.system('rm ./package-lock.json')
    os.system('npm init --y')
    os.system(installerCommand + ' config moment winston')
    os.system(installerDevCommand + ' typescript @types/config @types/webpack-node-externals nodemon ts-loader ts-node typescript webpack webpack-cli webpack-node-externals')


main()
