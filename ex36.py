
def execute_command(command):
    if command == 'ls':
        print('$ listing files')
    elif command == 'cd':
        print('$ chanding directory')
    else:
        print('$ command not implemented')
        
    print('... rest of the code')
    
#execute_command('ls')

       
def execute_command(command: str):
    match command:
        case 'ls':
            print('$ listing files')
        case 'cd':
            print('$ chanding directory')
        case _:  # NAO PASSOU NADA DENTRO DAS CONDIÇÕES
            print('$ command not implemented')
        
    print('... rest of the code')
    
execute_command('pwd')


#       | = OU

def execute_command(command: str):
    match command.split():
        case ['ls' | 'list', *directories, '--force']:
            for dic in directories:
                print('$ listing files from', dic)
        case ['cd' | 'change', path]:
            print('$ change directory to', path)
        case _:  # NAO PASSOU NADA DENTRO DAS CONDIÇÕES
            print('$ command not implemented')
        
    print('... rest of the code')
    
    

execute_command('list /home /user /google --force')
execute_command('change /home')
