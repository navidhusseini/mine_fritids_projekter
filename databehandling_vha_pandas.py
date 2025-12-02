from pathlib import Path
from statistics import mean

data_mappe = Path("L10/Oktoberdata/")
df_oktober = sorted(data_mappe.glob("*.csv"))  # alle csv-filer i mappen

for fil in df_oktober:
    print(f"{fil.name}")


dagsdata = []

def læs_min_vejr_data(filer):
    dagsdata = []
    for fil in filer:
        try:
            nedbør, lufttemp2m, lufttemp_græs, jordtemp10cm, vindhastighed = [], [], [], [], [] # laver de her lister 

            with fil.open("r", encoding="utf-8") as f:
                for i, linje in enumerate(f):
                    if not linje.strip():
                        continue
                    if i == 0 and "time" in linje.lower():
                        continue  # spring header som bare er string overskrifter

                    dele = linje.strip().split(";")
                    if len(dele) < 6:
                        continue

                    try:
                        # time;prec;metp;megrtp;mesotp10;meanwv
                        _nedbør = float(dele[1])
                        _luft2m = float(dele[2])
                        _luft_græs = float(dele[3])
                        _jord10cm = float(dele[4])
                        _vind = float(dele[5])
                    except ValueError:
                        continue  # ignorer linjer med ikke-numeriske værdier

                    nedbør.append(_nedbør) # her appender jeg til den liste jeg har lavet ved oven.
                    lufttemp2m.append(_luft2m)
                    lufttemp_græs.append(_luft_græs)
                    jordtemp10cm.append(_jord10cm)
                    vindhastighed.append(_vind)
            # tjek for data filer (som f.eks d. 20)
            if not lufttemp2m:
                raise ValueError("tom fil")

            # Find datoen ud fra filnavnet, så kender vi datoen, ved hjælp af navnet på filen
            dato = fil.stem.split("_")[-1]

            dagsdata.append({
                "dato": dato,
                "nedbør": nedbør,
                "lufttemp2m": lufttemp2m,
                "lufttemp_græs": lufttemp_græs,
                "jordtemp10cm": jordtemp10cm,
                "vindhastighed": vindhastighed,
            })

            print(f"{fil.name} indlæst ({len(lufttemp2m)} målinger)") # checker lige

        except FileNotFoundError as fejl:
            print(f"kunne ikke finde filen: {fejl}")
            continue
        except ValueError as fejl:
            print(f"der er fejl i værdierne i  filen {fil.name}: {fejl}")
            continue
        except Exception as fejl:
            print(f"fejl. {fil.name}: {fejl}")
            continue

    return dagsdata



def skriv_oktober_samlet_fra_data(dagsdata, output_fil: Path):
    with output_fil.open("w", encoding="utf-8") as udskrivningsfilen: # 'w' = skriver en fil istedet for at læse
        udskrivningsfilen.write(";".join([
            "Dato",
            "luft2m_min","luft2m_max","luft2m_gns",
            "luft_græs_min","luft_græs_max","luft_græs_gns",
            "jord10cm_min","jord10cm_max","jord10cm_gns",
            "timer_frost_2m",
            "timer_nedbør","samlet_nedbør_mm",
            "vind_min","vind_max","vind_gns",
        ]) + "\n")

        for d in sorted(dagsdata, key=lambda x: x["dato"]): # så basically sortere jeg alle dage efter dagsdato og key=lambda gør at datofeltet bliver sorterings kriteriet
            luft2m = d["lufttemp2m"]
            luftg  = d["lufttemp_græs"]
            jord   = d["jordtemp10cm"]
            vind   = d["vindhastighed"]
            nedb   = d["nedbør"]


            # døgnstatistik, jeg bruger statistik library til at finde gennemsnit
            luft2m_min,luft2m_max,luft2m_gns = min(luft2m), max(luft2m), mean(luft2m)
            luftg_min,luftg_max,luftg_gns  = min(luftg),max(luftg),mean(luftg)
            jord_min,jord_max,jord_gns = min(jord),max(jord), mean(jord)

            timer_frost_2m = sum(t < 0.0 for t in luft2m)
            timer_nedbør = sum(n > 0.0 for n in nedb)
            samlet_nedbør= sum(nedb)

            vind_min, vind_max, vind_gns = min(vind), max(vind), mean(vind)


            #DESIGN OG FORMATERING
            linje = [
                d["dato"],
                f"{luft2m_min:.2f}", f"{luft2m_max:.2f}", f"{luft2m_gns:.2f}", # 2 m luft temp
                f"{luftg_min:.2f}",  f"{luftg_max:.2f}",  f"{luftg_gns:.2f}", # græs temp
                f"{jord_min:.2f}",   f"{jord_max:.2f}",   f"{jord_gns:.2f}", # jord temp
                str(int(timer_frost_2m)), # antal timer med frost i 2m
                str(int(timer_nedbør)), f"{samlet_nedbør:.2f}", # nedbør
                f"{vind_min:.2f}", f"{vind_max:.2f}", f"{vind_gns:.2f}", # vind
            ]
            udskrivningsfilen.write(";".join(linje) + "\n")


data_mappe = Path("L10/Oktoberdata/")
filer = sorted(data_mappe.glob("Foulum_2019-10-*.csv"))
dagsdata = læs_min_vejr_data(filer)
output_fil = Path("Foulum_oktober_2019.csv") 
skriv_oktober_samlet_fra_data(dagsdata, output_fil)
