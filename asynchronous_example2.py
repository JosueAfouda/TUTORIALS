import time
import asyncio

async def prepareCafe():
    print("Debut prepareCafe()")
    await asyncio.sleep(3) # On suppose que cette taâche prend 3 secondes
    print("Fin prepareCafe()")
    return "Le café est prêt"

async def ToasterPain():
    print("Debut ToasterPain()")
    await asyncio.sleep(2) # On suppose que cette taâche prend 2 secondes
    print("Fin ToasterPain()")
    return "Le pain toasté est prêt"

async def main():
    start_time = time.time()

    tache_cafe = asyncio.create_task(prepareCafe())
    tache_toast = asyncio.create_task(ToasterPain())

    resultat_cafe = await tache_cafe
    resultat_toast = await tache_toast

    end_time = time.time()
    duree = end_time - start_time

    print(f"Resulat de prepareCafe : {resultat_cafe}")
    print(f"Resultat de ToasterPain : {resultat_toast}")
    print(f"Temps total d'exécution : {duree:.2f} secondes")

if __name__ == "__main__":
    asyncio.run(main())
