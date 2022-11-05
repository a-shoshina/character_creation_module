from random import randint

# Стандартное значение атаки.
DEFAULT_ATTACK: int = 5
# Стандартное значение защиты.
DEFAULT_DEFENCE: int = 10
# Стандартное значение выносливости.
DEFAULT_STAMINA: int = 80

class Character:
    # Стандартное описание.
    BRIEF_DESC_CHAR_CLASS: str = 'отважный любитель приключений.'
    # Константа для диапазона очков урона.
    RANGE_VALUE_ATTACK: tuple = (1, 3)
    # Констаната для диапазона очков защиты.
    RANGE_VALUE_DEFENCE: tuple = (1, 5)
    # Очки и название специального умения.
    SPECIAL_BUFF: int = 15
    SPECIAL_SKILL: str = 'Удача'

    # Объявляем конструктор класса.
    def __init__(self, name):
        self.name = name
    
   # Объявляем метод атаки.
    def attack(self) -> str:
        # Вычисляем значение атаки в переменной value_attack.
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}.')
    
    # Объявляем метод защиты.
    def defence(self) ->str:
        # Вычисляем значение защиты в переменной value_defence.
        value_defence =  DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')
    
    # Объявляем метод специального умения.
    def special(self) -> str:
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}"')

    # Описание класса.
    def __str__(self) -> str:
        return (f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}')



class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' дерзкий воин ближнего боя. '
                                  'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK: tuple = (3, 5)
    RANGE_VALUE_DEFENCE: tuple = (5, 10)
    SPECIAL_BUFF: int = DEFAULT_STAMINA + 25
    SPECIAL_SKILL: str = 'Выносливость'



class Mage(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' находчивый воин дальнего боя. '
                                  'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK: tuple = (5, 10)
    RANGE_VALUE_DEFENCE: tuple = (-2, 2)
    SPECIAL_BUFF: int = DEFAULT_ATTACK + 40
    SPECIAL_SKILL: str = 'Атака'



class Healer(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' могущественный заклинатель. '
                                  'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK: tuple = (-3, -1)
    RANGE_VALUE_DEFENCE: tuple = (2, 5)
    SPECIAL_BUFF: int = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL: str = 'Защита' 

# Новая функция.
# Добавили новый параметр — char_name.
def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным классом персонажа.
    """
    # Добавили словарь, в котором соотносится ввод пользователя и класс персонажа.
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    
    approve_choice: str  = None
    
    while approve_choice != 'y':
        selected_class: str = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        # Вывели в терминал описание персонажа.
        print(char_class)
        approve_choice: str = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class 


def start_training(character: Character) -> str:
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах тренировки персонажа.
    """
    print('Потренируся управлять своими навыками.')
    print('Введи одну из команд: attack - чтобы атаковать противника, '
    'defence - чтобы блокировать атаку противника или '
    'special - чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    commands: dict = {
        'attack': character.attack(),
        'defence': character.defence(),
        'special': character.special()
    }
    command: str = None
    while command != 'skip':
        cmd = input('Введи команду: ')
        if command in commands:
           print(f'{commands[command]}')
    return 'Тренировка окончена.'
               

if __name__ == '__main__':
 #   run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          f'Сейчас твоя выносливость — {DEFAULT_STAMINA}, '
          f'атака — {DEFAULT_ATTACK} '
          f'и защита — {DEFAULT_DEFENCE}.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class(char_name)
    print(start_training(char_class))
