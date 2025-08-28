import sys
from rich import print
from time import sleep

def printLyrics():
    lines = [
        ("I wanna da-", 0.06), 
        ("I wanna dance in the lights", 0.05),
        ("I wanna ro- ", 0.07),
        ("I wanna rock your body", 0.08),
        ("I wanna go", 0.07),    
        ("I wanna go for a ride", 0.08),
        ("Hop in the music and", 0.068),
        ("Rock your body", 0.07),
        ("Rock that body", 0.08),
        ("Come on, come on", 0.069),
        ("Rock that body", 0.035),
        ("(Rock your body)", 0.05),
        ("Rock that body", 0.03),
        ("come on, come on", 0.049),
        ("Rock that body", 0.035),
        
    ]

    # 16 delays, um para cada linha
    delays = [
        0.2, 1, 0.2, 1, 0.2, 0.8, 0.2, 0.5,
        0.18, 0.1, 0.15, 0.3, 0.3, 0.1, 5
    ]

    for i, (line, char_delay) in enumerate(lines):
        if line == '(Rock your body)':
            for char in line:
                print(f"[bold magenta]{char}[/]", end='', flush=True)
                sys.stdout.flush()
                sleep(char_delay)
        else:
            for char in line:
                print(f"[bold gold3]{char}[/]", end='', flush=True)
                sys.stdout.flush()
                sleep(char_delay)
        print()  # Nova linha após cada linha de letra
        sleep(delays[i])

# Executar a função
printLyrics()
