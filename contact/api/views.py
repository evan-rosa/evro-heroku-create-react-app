from rest_framework import viewsets

from contact.models import Contact
from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
