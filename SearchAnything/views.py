from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import SearchSerializers
from rest_framework.renderers import TemplateHTMLRenderer

import requests
import urllib.request
from bs4 import BeautifulSoup


class SearchAPI(APIView):
    serializer_class = SearchSerializers
    def get(self,request,format=None):
        name = request.GET['sname']
        if name:
            querry = name+" logo"
            shorty = querry[0:4]
            url = 'https://www.google.com/search?rlz=1C1CHBF_enIN809IN809&sxsrf=ALeKk00RgUMDXPD31AEQzd4ek0gOXwXfFA%3A1591504144872&ei=EG3cXpn1NILdrQGx5af4Bw&q={}+images&oq={}&gs_lcp=CgZwc3ktYWIQAxgAMgQIABBDMgcIABCxAxBDMgQIABBDMgQIABBDMgQIABBDMgcIABCxAxBDMgcIABCxAxBDMgQIABBDMgQIABBDMgcIABCxAxBDOgQIABBHOgQIIxAnOgoIABCDARAUEIcCOgUIABCDAToFCAAQsQM6BwgAEBQQhwI6BwgjEOoCECc6BQgAEJECOgcIABCDARBDUL0xWI9NYPZeaAFwAngEgAH_AYgB2A6SAQUwLjguMpgBAKABAaoBB2d3cy13aXqwAQo&sclient=psy-ab'.format(querry,shorty)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            count = ""
            for i in soup.findAll('a')[:20]:
                if 'www.google.com' in i['href']:
                    count = i['href']
                    break
            resp = requests.get(count)
            soup = BeautifulSoup(resp.text, "html.parser")
            lis = []
            for i in soup.findAll('img'):
                if "/images/branding/searchlogo/1x/googlelogo_desk_heirloom_color_150x55dp.gif" == i['src']:
                    pass
                else:
                    lis.append(i['src'])
            return Response({'SAUAbj':lis})
        else:
            return Response({'SAUAbj':"Oopse! No result"})
    def post(self,request):
        fs = SearchSerializers(data = request.data)
        if fs.is_valid():
            name = fs.data.get('sname')
            querry = name
            shorty = querry[0:4]
            url = 'https://www.google.com/search?rlz=1C1CHBF_enIN809IN809&sxsrf=ALeKk00RgUMDXPD31AEQzd4ek0gOXwXfFA%3A1591504144872&ei=EG3cXpn1NILdrQGx5af4Bw&q={}+images&oq={}&gs_lcp=CgZwc3ktYWIQAxgAMgQIABBDMgcIABCxAxBDMgQIABBDMgQIABBDMgQIABBDMgcIABCxAxBDMgcIABCxAxBDMgQIABBDMgQIABBDMgcIABCxAxBDOgQIABBHOgQIIxAnOgoIABCDARAUEIcCOgUIABCDAToFCAAQsQM6BwgAEBQQhwI6BwgjEOoCECc6BQgAEJECOgcIABCDARBDUL0xWI9NYPZeaAFwAngEgAH_AYgB2A6SAQUwLjguMpgBAKABAaoBB2d3cy13aXqwAQo&sclient=psy-ab'.format(querry,shorty)
            response = requests.get(url)

            soup = BeautifulSoup(response.text, "html.parser")

            count = ""

            for i in soup.findAll('a')[:20]:
            	if 'www.google.com' in i['href']:
            		count = i['href']
            		break

            resp = requests.get(count)

            soup = BeautifulSoup(resp.text, "html.parser")

            lis = []

            for i in soup.findAll('img'):
            	if "/images/branding/searchlogo/1x/googlelogo_desk_heirloom_color_150x55dp.gif" == i['src']:
            		pass
            	else:
            		lis.append(i['src'])
            return Response({'SAUAbj':lis})
        else:
            return Response(fs.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        return Response({'method':'put'})

def index(request):
    return render(request,'index.html')
