import random

class BealeCipher:

    def __init__(self):
        reference = """
        Ne nje fshat gazmor te vendosur buze nje pylli jetonte nje vogelushe e hirshme
        me nenen e vet ishte shume e bukur kishte nje fytyre te trendafilte porsi nje
        molle sy te kalter si qielli i pranveres dhe floke kacurrela e te verdhe si
        gruri i pjekur pertej pyllit banonte gjyshja e saj nje plake simpatike qe e
        donte shume te mbesen se ciles kur mbushi shtate vjec i kishte dhuruar nje
        mantel fort te bukur me nje kapuc te kuq sa here qe dilte nga shtepia
        vogelushes i pelqente ta vishte ate prandaj gjithe banoret e fshatit ia
        vendosen emrin kesulkuqja sapo mbaronte punet e shtepise vajza vraponte ne
        pyll ku jetonin kafshe te vockla me te cilat kishte miqesi cdo mengjes
        heret ajo i merrte me radhe per te pare nese kishin ushqim te mjaftueshem
        nese putra e ketrushit ishte sheruar dhe nese lepurushet kishin pushuar
        se bezdisuri iriqin plak ne nje mengjes pranvere nje lepurush i bardhe
        arriti duke gulquar te shtepiza e kesulkuqes dhe i tha me dergoi gjyshja
        e jote ka zene krevatin ka kolle dhe i jane mbaruar ushqimet duhet te
        nxitosh per tek ajo nena pergatiti me kujdes nje shporte te vogel plot
        me gjera te mira ne te cilen vuri edhe nje shurup per kollen afer
        shtepise xhaxhai po lexonte nje poezi per yllin gjersa ora po kalonte
        me vrap rruges udha ishte e gjate por drita e diellit ndriconte mbi
        cdo lule e peme
        """
        self.reference_words = reference.lower().split()

    def encrypt(self, message):
        message = message.lower()
        result = []

        for char in message:
            if char == " ":
                result.append("/")
                continue

            indices = [i for i, word in enumerate(self.reference_words) if word.startswith(char)]

            if indices:
                result.append(str(random.choice(indices)))
            else:
                result.append("?")

        return " ".join(result)

    def decrypt(self, ciphertext):
        parts = ciphertext.split()
        result = []

        for part in parts:
            if part == "/":
                result.append(" ")
            elif part == "?":
                result.append("?")
            else:
                idx = int(part)
                if idx < len(self.reference_words):
                    result.append(self.reference_words[idx][0])
                else:
                    result.append("?")

        return "".join(result)
def main():


def main():
    cipher = BealeCipher()

    while True:
        print("\nBEALE CIPHER")
        print("1. Enkripto")
        print("2. Dekripto")
        print("3. Dil")

        choice = input("Zgjedhja: ")

        if choice == "1":
            text = input("Shkruaj mesazhin: ")
            encrypted = cipher.encrypt(text)

            print("\nMesazhi i enkriptuar:")
            print(encrypted)

        elif choice == "2":
            code = input("Jep kodin: ")
            decrypted = cipher.decrypt(code)

            print("\nMesazhi i dekoduar:")
            print(decrypted.upper())
        elif choice == "3":
            print("\nProgrami perfundoi!")
            break

        else:
            print("Opsion i pavlefshem")


if __name__ == "__main__":
    main()