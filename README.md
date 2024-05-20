# projekt_1
First Project in Engeto Online Python Academy

# Textový analyzátor

Cílem projektu je vytvořit textový analyzátor - program, který se bude umět prokousat libovolně dlouhým textem a zjistit o něm různé informace.

Analyzovány budou předpřipravené texty, uložené v proměnné TEXTS.

## **Program obsahuje následující:**

1. Identifikace souboru - popis hlavičky (kontaktní údaje),
2. Vyžádá si od uživatele přihlašovací jméno a heslo,
3. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
4. Pokud je uživatel registrovaný, program umožní analyzovat texty,
5. Pokud uživatel není registrovaný, dostane upozornění a program se ukončí.


## Základní struktura programu

### **Registrováni jsou následující uživatelé:**

![uzivatele](https://github.com/BaraMaskova/projekt_1/assets/145649546/a30d6b10-93e2-4f22-8a65-75fc2b79f0a5)


### **Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:**

  1. Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí.

  2. Pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.


### **Pro vybraný text spočítá následující statistiky:**
  1. počet slov,
  2. počet slov začínajících velkým písmenem,
  3. počet slov psaných velkými písmeny,
  4. počet slov psaných malými písmeny,
  5. počet čísel (ne cifer),
  6. sumu všech čísel (ne cifer) v textu.

### **Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:**

![sloupcovy graf](https://github.com/BaraMaskova/projekt_1/assets/145649546/3de40a97-0b4d-4473-aaa9-4bbd205cbe87)

### **Po spuštění by měl průběh vypadat následovně:**

![program_registrovany_uzivatel](https://github.com/BaraMaskova/projekt_1/assets/145649546/b67afdd1-933d-49a0-8fb5-71bbb2b4f278)

### Pokud uživatel **není registrovaný:**

![program_neregistrovany_uzivatel](https://github.com/BaraMaskova/projekt_1/assets/145649546/f7e25832-215d-44bd-aa98-703f334d2125)

### Předpřipravené texty:

![pripravene texty](https://github.com/BaraMaskova/projekt_1/assets/145649546/c055f8ce-2a51-43d9-b6d6-5df5eb24a5ba)
