from django.contrib.syndication.views import Feed
from django.urls import reverse
from app.models import Show

# Show the 2 last shows
class LastShowFeed(Feed):
    title = "Derniers shows encodés"
    link = "/showrss/"
    description = "last show on the site"

    def items(self):
        return Show.objects.order_by('-date_created')[:2]

    def item_title(self,item):
        return item.title

    def item_description(self, item):
        return item.description

#show representation
class RepresentationFeed(Feed):
    title = "Représentations "
    link = "/representationrss/"
    description = "last representation on the site"

    def items(self):
        return Representation.objects.order_by('location')

    def item_title(self,item):
        return item.title

    def item_description(self, item):
        return item.description
