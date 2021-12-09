from rest_framework import status, serializers
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
import requests
from rest_pandas import PandasView

from bored_and_joke.serializers import BoredAndJokeForGetSerializer, BoredAndJokeForCSVSerializer
from bored_and_joke.models import BoredAndJoke
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework_csv import renderers as r


@api_view(['GET'])
def get_bored_and_joke(request, tipo):
    allowed_types = ["education", "recreational", "social", "diy",
                     "charity", "cooking", "relaxation", "music", "busywork"]
    if tipo not in allowed_types:
        return Response({"error": "Este tipo no es válido"}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        bored_api_response = requests.get(f'http://www.boredapi.com/api/activity?type={tipo}')
        if bored_api_response.status_code == 200:
            bored_api_data = bored_api_response.json()
            bored_and_joke = {
                'type': tipo,
                'actividad': bored_api_data['activity'],
                'key': bored_api_data['key']
            }
            joke_api_response = requests.get(f'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw&contains={tipo}')
            if joke_api_response.status_code == 200:
                joke_api_data = joke_api_response.json()
                if joke_api_data['error'] is True:
                    # TODO mejorar este error, es decir que sea uno apropiado
                    raise serializers.ValidationError({"error": "No se encontró una chiste"})
                if joke_api_data['type'] == 'twopart':
                    joke = joke_api_data['setup'] + '->' + joke_api_data['delivery']
                else:
                    joke = joke_api_data['joke']
                bored_and_joke['chiste'] = joke
                serializer = BoredAndJokeForGetSerializer(data=bored_and_joke)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Error al obtener el joke"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Error al obtener el juego"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@renderer_classes([r.CSVRenderer])
def bored_csv(request):
    bored_and_jokes = BoredAndJoke.objects.all()
    content = [
        {'type': bored_and_joke.type,
         'actividad': bored_and_joke.actividad,
         'key': bored_and_joke.key,
         'chiste': bored_and_joke.chiste}
        for bored_and_joke in bored_and_jokes
    ]
    return Response(content)




