with open("hisobot.json") as file:
    import json
    hodim = json.load(file)
    print("1.Hodimlar ma'lumotlarini ko'rish\n2.Maoshga ko'ra tartiblash\n3.Ma'lum bir lavozimdagi hodimlarni "
          "ko'rish\n4.Eng ko'p ishlaydigan lavozim")
    tanlov = int(input("Tanlovni kiriting : "))

    if tanlov == 1:
        for i in hodim:
            print(i, end="\n")
    elif tanlov == 2:
        maosh_tartiblash = sorted(hodim, key=lambda x: x["maosh"], reverse=True)
        print("\nMaosh bo'yicha tartiblash\n\n")
        for i in maosh_tartiblash:
            print(i)
    elif tanlov == 3:
        lavozims = []
        for i in hodim:
            if i["lavozim"] not in lavozims:
                lavozims.append(i["lavozim"])
        for i in lavozims:
            print(i)
        kirit = input("Qaysi lavozimdagi hodimlarni ko'rmoqchisiz : ")
        natija = []
        print(f"\n{kirit} lavozimidagi ishchilar : \n\n")
        for i in hodim:
            if i["lavozim"].lower() == kirit.lower():
                natija.append(i)
        for i in natija:
            print(i)
    elif tanlov == 4:
        lavozimlar = {}
        for i in hodim:
            if i["lavozim"] not in lavozimlar.keys():
                lavozimlar[i["lavozim"]] = 1
            else:
                lavozimlar[i["lavozim"]] += 1
        saralangan_lavozimlar = sorted(lavozimlar.items(), key=lambda x: x[1])
        eng_kop_lavozim = saralangan_lavozimlar[-1]
        print(f"eng kop ishchi ishlaydigan lavozim bu : {eng_kop_lavozim[0]} {eng_kop_lavozim[1]} ta ishchi")
    else:
        print("Siz hato tanlov kiritdingiz !")
