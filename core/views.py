from django.shortcuts import render, redirect, get_object_or_404
from .models import Knihy, Uzivatele, Vypujcky

# 1. Hlavní katalog
def katalog(request):
    knihy = Knihy.objects.all()
    return render(request, 'core/index.html', {'knihy': knihy})

# 2. Detail knížky - TADY BYLA CHYBA, TEĎ UŽ TO FUNGUJE
def detail_knihy(request, kniha_id):
    kniha = get_object_or_404(Knihy, id=kniha_id)
    uzivatele = Uzivatele.objects.all()
    
    if request.method == "POST":
        # 1. Vytáhneme z formuláře to ID (v tvém případě '3')
        id_uzivatele = request.POST.get('uzivatel') 
        
        # 2. MUSÍME toho uživatele nejdřív vytáhnout z databáze jako objekt!
        skutecny_uzivatel = get_object_or_404(Uzivatele, pk=id_uzivatele)
        
        # 3. A do create dosadíme ten SKUTEČNÝ OBJEKT
        Vypujcky.objects.create(
            kniha=kniha,
            uzivatel=skutecny_uzivatel  # <-- Sem nesmí přijít text '3', ale ten objekt
        )
        return redirect('seznam_vypujcek')

    return render(request, 'core/detail.html', {'kniha': kniha, 'uzivatele': uzivatele})

# 3. Stránka se všemi půjčenými knihami
def seznam_vypujcek(request):
    vypujcky = Vypujcky.objects.all()
    return render(request, 'core/vypujcka.html', {'vypujcky': vypujcky})