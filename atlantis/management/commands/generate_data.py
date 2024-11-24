import random
from django.core.management.base import BaseCommand
from faker import Faker
from atlantis.models import Character, Protagonist, Antagonist, Supporting  # Replace 'your_app' with the name of your app

class Command(BaseCommand):
    help = 'Generate fake data for Character, Protagonist, Antagonist, and Supporting models'

    def handle(self, *args, **options):
        fake = Faker()

        # Generate 500 characters
        for _ in range(500):
            # Create a Character instance
            character = Character.objects.create(
                name=fake.name(),
                description=fake.text(),
                role=random.choice(['protagonist', 'antagonist', 'supporting'])
            )

            # Randomly assign Protagonist, Antagonist, or Supporting roles
            role_type = random.choice(['protagonist', 'antagonist', 'supporting'])

            if role_type == 'protagonist':
                Protagonist.objects.create(
                    character=character,
                    team_name=fake.company()
                )
            elif role_type == 'antagonist':
                Antagonist.objects.create(
                    character=character,
                    team_name=fake.company()
                )
            else:
                Supporting.objects.create(
                    character=character,
                    team_name=fake.company()
                )

        self.stdout.write(self.style.SUCCESS('Successfully generated 500 characters with roles.'))