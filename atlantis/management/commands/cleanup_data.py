from django.core.management.base import BaseCommand
from atlantis.models import Character, Protagonist, Antagonist, Supporting  # Replace 'your_app' with the name of your app

class Command(BaseCommand):
    help = 'Remove all characters except specified ones'

    def handle(self, *args, **options):
        # List of characters to keep
        characters_to_keep = [
            ("Milo Thatch", "Protagonist"),
            ("Princess Kidagakash 'Kida'", "Protagonist"),
            ("Audrey Rocio Ramirez", "Supporting"),
            ("Commander Lyle Tiberius Rourke", "Antagonist"),
            ("Helga Katrina Sinclair", "Antagonist"),
            ("Vincenzo \"Vinny\" Santorini", "Supporting"),
            ("Gaetan \"The Mole\" Molière", "Supporting"),
            ("King Kashekim Nedakh", "Supporting"),
            ("Preston B. Whitmore", "Supporting"),
            ("Wilhelmina Bertha Packard", "Supporting"),
            ("Jebidiah Allardyce \"Cookie\" Farnsworth", "Supporting"),
            ("Dr. Joshua Strongbear Sweet", "Supporting"),
            ("Fenton Q. Harcourt", "Supporting"),
        ]

        # Create a set of names to keep
        names_to_keep = {name for name, role in characters_to_keep}

        # Get all characters
        all_characters = Character.objects.all()

        # Loop through characters and delete those not in the keep list
        for character in all_characters:
            if character.name not in names_to_keep:
                character.delete()

        self.stdout.write(self.style.SUCCESS('Successfully removed characters except the specified ones.'))