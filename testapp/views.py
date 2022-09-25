from django.http import HttpResponse
from django.shortcuts import render

from testapp.models import ModelA, ModelB
from model_bakery import baker


# Create your views here.
def test(request):
    queryset = ModelB.objects\
        .all()
    for b in queryset:
        b.parent
    # queryset = ModelA.objects\
    #     .prefetch_related('modelb_set') \
    #     .all()
    # for a in queryset:
    #    list( a.modelb_set.all())

    return render(request, 'testapp/index.html')


def seed(request):

    for i in range(100):
        model_a = baker.make(ModelA)
        model_a.save()

        for i in range(5):
            model_b = baker.make(ModelB)
            model_b.save()
    return HttpResponse("Done seeding!")
