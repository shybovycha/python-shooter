# Side Scrolling Shooter

## Zadanie

Side scrolling shooter - klasyczna strzelanka gdzie lecimy statkiem/innym obiektem caly czas w prawo i walczymy z nadlatującymi wrogami. Gra powinna zawierac kilka plansz, rozne rodzaje wrogow, broni/bonusow, conajmniej jedna walke z bossem i tryb dla 2 graczy.

## Technologię

Python + Cocos2d (PyGlet pod spodem)

## Instalacja

### Wymagania

1. [pip](https://pip.pypa.io/en/latest/installing.html)
2. [cocos2d](https://github.com/los-cocos/cocos)

Dla systemów Linux można użyć komand:

    [sudo] apt-get install libsdl2-dev libsdl2-image-dev libsdl2-ttf-dev libsdl2-mixer-dev

### Wymagane moduły Pythona

Dla instalacji modułów, użyć `pip`:

    pip install cocos2d
    
## Uruchamienie

Wystarczy uruchomić `python main.py`

## Wykonane

1. Jedna plansza
2. Dwa wrogi, które umią latać i strzelać
3. Wrogów można zniszczać
4. Kontroler gracza (mysz)

## Class diagram

![class diagram](https://github.com/shybovycha/python-shooter/raw/master/doc/class_diagram.png)

## TODO

1. Kilka plansz
2. Transition między planszami
3. Boss
4. Kilka bonusów
5. Menu
6. Warunki wygrania
7. Kontroler drugiego gracza (klawiatura)
