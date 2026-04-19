# Implementimi i Beale dhe Grille Cipher

Ky projekt përmban dy algoritme klasike të kriptografisë të implementuara në Python. Programet mundësojnë enkriptimin dhe dekriptimin e mesazheve përmes terminalit.

---

## 1. Përshkrimi i Algoritmeve

### Beale Cipher - Shifrimi me libër
Kjo metodë përdor një libër si çelës për të fshehur mesazhin.
- **Si punon:** Programi numëron fjalët e librës. Kur duam të enkriptojmë një shkronjë, programi gjen një fjalë që fillon me atë shkronjë dhe shënon numrin e rradhës së asaj fjale.
- **Pse është i mirë:** Sepse një shkronjë mund të zëvendësohet me shumë numra të ndryshëm, kështu që dikush që e sheh kodin nuk mund ta gjejë kollaj modelin.

### Grille Cipher
Grille Cipher është një shifrim transpozicioni që përdor një rrjetë me vrima.
- Programi gjeneron një rrjetë rastësore për një matricë të madhësisë N x N.
- Mesazhi shkruhet nëpër vrimat e rrjetës, pastaj rrjeta rrotullohet 90 shkallë katër herë deri sa të mbushen të gjitha kutitë.
- Ky proces e shpërndan mesazhin në mënyrë të çrregullt nëpër matricë.

## 2. Udhëzimet e Ekzekutimit

Për të ekzekutuar programet, ndiqni këto hapa në VS Code:

1. Hapni një terminal të ri.
2. Sigurohuni që keni Python të instaluar: `python --version`.
3. Ekzekutoni Beale Cipher:
   python beale.py

4. Ekzekutoni Grille Cipher:
   python grille.py

## 3. Shembuj të Rezultateve

### Shembull për Beale Cipher:
- Mesazhi për enkriptim: "tung server"
- Rezultati i enkriptuar: 102 121 21 10 / 68 87 11 113 77 112
- Rezultati i dekriptuar: TUNG SERVER

### Shembull për Grille Cipher:
- Madhësia e matrices: 4
- Mesazhi për enkriptim: "sekret"
- Rezultati i enkriptuar: SXEXKXRXXRXXEXTX
- Rezultati i dekriptuar: sekret

## Sqarime
- Te Beale Cipher, karakteri "/" përdoret si ndarës për hapësirat.
- Te Grille Cipher, shkronja "X" shtohet automatikisht në fund të mesazhit për të plotësuar hapësirat boshe të matricës.
- Për Grille Cipher, dekriptimi duhet të bëhet brenda të njëjtit cikël ekzekutimi që është bërë enkriptimi, pasi vrimat e rrjetës gjenerohen në mënyrë rastësore dhe nuk ruhen në skedar të jashtëm.