from django.shortcuts import render, get_object_or_404
from .models import Film
from django.http import HttpResponse


def lista_filmow(request):
    filmy = Film.objects.all()
    return render(request, 'filmy/lista_filmow.html', {'filmy': filmy})


def szczegoly_filmu(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    return render(request, 'filmy/szczegoly_filmu.html', {'film': film})


def dodaj_film(request):
    if request.method == 'POST':
        tytul = request.POST.get('tytul')
        opis = request.POST.get('opis')
        rok_produkcji = request.POST.get('rok_produkcji')
        rezyser = request.POST.get('rezyser')

        nowy_film = Film.objects.create(
            tytul=tytul,
            opis=opis,
            rok_produkcji=rok_produkcji,
            rezyser=rezyser
        )
        return HttpResponse(f'Dodano nowy film: {nowy_film.tytul}')

    return render(request, 'filmy/dodaj_film.html')


def filtruj_filmy(request):
    if request.method == 'GET':
        rezyser = request.GET.get('rezyser', '')
        rok_produkcji = request.GET.get('rok_produkcji', '')
        nazwa = request.GET.get('nazwa', '')

        filmy = Film.objects.all()

        if rezyser:
            filmy = filmy.filter(rezyser__icontains=rezyser)

        if rok_produkcji:
            filmy = filmy.filter(rok_produkcji=rok_produkcji)

        if nazwa:
            filmy = filmy.filter(tytul__icontains=nazwa)

        return render(request, 'filmy/filtruj_filmy.html', {'filmy': filmy})

    return render(request, 'filmy/filtruj_filmy.html')