from command_runner import CommandRunner
import os

if __name__ == '__main__':
    DATA_DIR = r'C:\Users\hp\Desktop\Pythonprogramming\week5\process\task\files'
    OUTPUT_DIR = r'C:\Users\hp\Desktop\Pythonprogramming\week5\process\task\outputs'

    if not os.path.exists(DATA_DIR):
        print('Directory does not exist')
    else:
        for folder, subfolders, files in os.walk(DATA_DIR):
            for file in files:
                if file.endswith('.txt'):
                    programs_file_path = os.path.join(folder, file)
                    programs_file_name = os.path.splitext(file)[0]
                    runner = CommandRunner(programs_file_path, os.path.join(OUTPUT_DIR, programs_file_name))
                    runner.run_commands()