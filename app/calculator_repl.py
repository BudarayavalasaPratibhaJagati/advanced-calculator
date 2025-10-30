# pragma: no cover
import sys
from colorama import init as color_init, Fore, Style
from .calculator import Calculator, LoggingObserver, AutoSaveObserver
from .input_validators import two_numbers
from .calculator_config import load_config
from .exceptions import OperationError, ValidationError

def rounder_factory(precision:int):
    def _r(x: float) -> float: return round(x, precision)
    return _r

def main():
    color_init(autoreset=True)
    cfg = load_config()
    calc = Calculator()
    calc.register(LoggingObserver())
    calc.register(AutoSaveObserver(calc.history))
    rnd = rounder_factory(cfg.precision)

    HELP = f'''
{Fore.CYAN}commands:{Style.RESET_ALL}
  add|subtract|multiply|divide|power|root|modulus|int_divide|percent|abs_diff a b
  history | clear | undo | redo | save | load | help | exit
'''
    print(HELP)
    while True:
        try:
            raw = input(Fore.GREEN + 'calc> ' + Style.RESET_ALL).strip()
        except (EOFError, KeyboardInterrupt):
            print('\nbye!'); break
        if not raw: continue
        parts = raw.split(); cmd = parts[0].lower()
        try:
            if cmd in {'add','subtract','multiply','divide','power','root','modulus','int_divide','percent','abs_diff'}:
                if len(parts) != 3:
                    print(Fore.YELLOW + 'need two numbers like: add 2 3'); continue
                a,b = two_numbers(parts[1], parts[2])
                c = calc.calculate(cmd, a, b, rnd)
                print(Fore.MAGENTA + f'{c.operation}({c.a}, {c.b}) = {c.result}')
            elif cmd == 'history':
                if not calc.history.items: print(Fore.YELLOW + 'no history yet')
                else:
                    for i,h in enumerate(calc.history.items, start=1):
                        print(f'{i}. {h.timestamp} | {h.operation}({h.a}, {h.b}) = {h.result}')
            elif cmd == 'clear': calc.history.clear(); print('history cleared')
            elif cmd == 'undo': calc.undo(); print('undone')
            elif cmd == 'redo': calc.redo(); print('redone')
            elif cmd == 'save': calc.history.save_csv(); print('saved')
            elif cmd == 'load': calc.history.load_csv(); print('loaded')
            elif cmd == 'help': print(HELP)
            elif cmd == 'exit': print('bye!'); break
            else: print(Fore.RED + f'unknown command: {cmd}')
        except (OperationError, ValidationError) as e:
            print(Fore.RED + f'error: {e}')
        except Exception as e:
            print(Fore.RED + f'unexpected error: {e}')

if __name__ == '__main__':  # pragma: no cover
    main()

