# Beale-Cipher-and-Grille-Cipher

## Projekti: Beale Cipher & Grille Cipher
#### Përshkrimi

Ky projekt implementon dy algoritme klasike të kriptografisë:

 -Beale Cipher (bazuar në tekst referencë)
 -Grille Cipher (me matricë dhe rotacion)

Programi mundëson enkriptimin dhe dekriptimin e mesazheve përmes një ndërfaqeje në terminal.

Si të ekzekutohet programi

Kërkesat
 Python 3.x

#### Hapat
 1.Klono repository:
git clone https://github.com/oltamorina24/Beale-Cipher-and-Grille-Cipher.git

 2.Hyr në folder:
  cd beale-grille-cipher
 3.Ekzekuto programin:
 python main.py


## Algoritmet e implementuara
### 1. Beale Cipher

#### Përshkrimi

Beale Cipher përdor një tekst referencë si çelës. Çdo shkronjë e mesazhit zëvendësohet me indeksin e një fjale nga teksti që fillon me atë shkronjë.

Si funksionon
Teksti referencë ndahet në fjalë
Për çdo shkronjë të mesazhit gjendet një fjalë që fillon me atë shkronjë
Ruhet indeksi i asaj fjale
Hapësirat përfaqësohen me /

Shembull (real nga programi)
Input:
test

Output:
23 11 54 11

Dekriptim:
TEST

### 2. Grille Cipher
#### Përshkrimi

Grille Cipher përdor një matricë NxN dhe një maskë me vrima (grille). Mesazhi shkruhet në pozicionet e vrimave dhe grille rrotullohet për të mbushur të gjithë matricën.

Si funksionon
 -Zgjedhet madhësia e matrices (numër çift)
 -Gjenerohen vrimat në mënyrë të rastësishme
 -Mesazhi vendoset në pozicionet e vrimave
 -Grille rrotullohet 4 herë (0°, 90°, 180°, 270°)

Shembull (real nga programi)
Input:
hello

Output:
HLOXELXXXXXXXX

Dekriptim:
hello

## Shembuj të ekzekutimit
### BEALE CIPHER
1. Enkripto
2. Dekripto


Zgjedhja: 1

Shkruaj mesazhin: hello

Mesazhi i enkriptuar:
12 45 33 33 78

Zgjedhja: 2

Jep kodin: 12 45 33 33 78
Mesazhi i dekoduar:
HELLO

### Grille Cipher


#### 1. Enkriptim


Zgjedh opsionin: 1

Madhësia: 4

Mesazhi: hello

Mesazhi i enkriptuar: HLOXELXXXXXXXX

Zgjedh opsionin: 2

Mesazhi i dekriptuar: hello


Struktura e projektit
project/
│
├── beale.py
├── grille.py
├── main.py
├── README.md
└── .gitignore


.gitignore
__pycache__/
*.pyc
*.pyo
*.log
.env
.vscode/
.idea/

Kufizime
Beale Cipher varet nga teksti referencë (nëse mungon shkronja → përdoret ?)
Grille Cipher kërkon të njëjtën grille për dekriptim
Në këtë implementim, grille nuk ruhet në file (nëse programi mbyllet, dekriptimi nuk mund të bëhet)

## Përfundim

Ky projekt demonstron:

 -Implementimin korrekt të algoritmeve kriptografike
 -Njohuri teorike mbi kriptimin klasik
 -Aftësi praktike në Python
 -Organizim të kodit dhe përdorim të GitHub