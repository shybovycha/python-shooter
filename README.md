# Side Scrolling Shooter

![Screenshot](/../master/python-shooter-screenshot.png?raw=true)

## Zadanie

Side scrolling shooter - klasyczna strzelanka, gdzie lecimy statkiem/innym obiektem cały czas w prawo i walczymy z nadlatującymi wrogami. Gra powinna zawierać kilka plansz, różne rodzaję wrogów, broni/bonusów i conajmniej jedną walkę z bossem.

## Technologię

Python 3 + Cocos2d

## Instalacja

### Wymagania

0. [python 3](https://www.python.org/)
1. [pip](https://pip.pypa.io/en/latest/installing.html)
2. [cocos2d](https://github.com/los-cocos/cocos)

Dla systemów Linux można użyć komand:

    [sudo] apt-get install libsdl2-dev libsdl2-image-dev libsdl2-ttf-dev libsdl2-mixer-dev

Dla OS X:

    brew install sdl2 sdl2_image sdl2_ttf sdl2_mixer

### Wymagane moduły Pythona

Dla instalacji modułów, użyć `pip`:

    pip install cocos2d

## Architektura

### Diagram klas

![class_diagram.png]

### Obrazki i warstwy

Ponieważ gra jest 2D, wszystko co jest narysowane jest obrazkiem. Żeby obrazek był narysowany bez własnego tła, on jest przedstawiony jako `Sprite`.

Wszystkie sprajty są umieszczone wewnątrz warstw. Warstwy są podzielone w taki sposób, żeby każda warstwa zawierała wyłącznie właściwe dla niej obiekty, czyli warstwa tła, warstwa gracza, warstwa wrogów i td.

### Plansza

Plansza musi się przesuwać żeby stworzyć efekt poruszania gracza. Ona jest warstwą, zawierającą dwa obrazki, które są umieszczone obók siebie i są przesuwane w jednolity sposób. W momencie, gdy jeden obrazek przestaje być widoczny, on jest umieszczony wraz za widocznym obrazkiem. To tworzy efekt nieskonczonej planszy.

Na diagramie klas plansza jest przedstawiona w postaci klas `BackgroundLayer` oraz `ParallaxLayer`.

### Bonusy

Każdy bonus to jest klasa, dziedziczona po klasie `Bonus`, która dziedziczy klasę `DestroyableSprite` (Sprite, który może zostać zniszczony), która jest rozszerzeniem klasy `CollidableSprite` (czyli Sprite, który może reagować na kolizje). Każda klasa-dziecko (`ArmorBonus`, `DamageBonus`, `RepairBonus`) definiuje swoje zachowanie przy kolizji ze spritem gracza. Domyślnie, klasa `Bonus` definiuje brak dowolnych efektów przy uderzeniu ze wrogiem.

### Gracz i wrogi

Gracz, wrogi i final boss są postaciami, które mogą strzelać i być zniszczone. W tym celu istnieje klasa `ShootingSprite`, która ma metodę `shoot()`, która tworzy rakiety _(klasa `Missle`, dziecko klasy `DestroyableSprite`, która definiuje zachowanie odejmowania punktów zdrowia przy uderzeniu z graczem/wrogiem)_. Rakiety są umieszczone na warstwie `EnemyLayer` lub `PlayerLayer`. Przy zniszczeniu rakiety, jest tworzony efekt wybuchu.
