import factory
import factory.fuzzy

from raporty_siecobywatelska_pl.questionnaire.factory import GroupFactory
from raporty_siecobywatelska_pl.exploration.models import Exploration


class ExplorationFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence('title-letter-{0}'.format)
    description = factory.Sequence('quote-{0}'.format)

    group_1 = factory.RelatedFactory(GroupFactory, "exploration")
    group_2 = factory.RelatedFactory(GroupFactory, "exploration")
    group_3 = factory.RelatedFactory(GroupFactory, "exploration")

    @factory.post_generation
    def institutions(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for institution in extracted:
                self.institutions.add(institution)

    class Meta:
        model = Exploration
