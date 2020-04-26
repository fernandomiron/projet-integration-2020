from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from app.models.show import Show 

class TestShowListViews(TestCase):
    # Set up non-modified objects used by all test methods
    @classmethod
    def setUpTestData(cls):
        number_of_shows = 15
        for pk in range(number_of_shows):
            Show.objects.create(
                slug = f"show-{pk}",
                title = f"The show n°{pk}",
                poster_url = "https://placeholder.com/250",
                bookable = True,
                price = 10,
                description = f"description n°{pk}",
                created_at = timezone.now()
            )
        
    # setup clean data for every test method
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('app:shows-list')

    # test url
    def test_show_list_view_url_exists_at_desired_location(self):
        response = self.client.get('/app/shows-list/')
        self.assertEqual(response.status_code, 200)

    # test template
    def test_show_list_view_uses_correct_template(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/show/index.html')