def ask_for_confirmation(prompt, prompt_sufix=' (y/n)[n]: '):
    answer = raw_input(prompt + prompt_sufix).strip()
    if answer == '':
        return False
    elif answer not in ('y', 'n', 'yes', 'no'):
        print 'Please answer yes or no'
    elif answer == 'y' or answer == 'yes':
        return True
    else:
        return False
