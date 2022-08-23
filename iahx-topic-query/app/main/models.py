from django.db import models


class TopicQuery(models.Model):
    class Meta:
        verbose_name = "Tópico / Query"
        verbose_name_plural = "Tópicos / Queries"

    instance_id = models.CharField("ID da instância", max_length=75, blank=False)
    filter_id = models.CharField("ID do filtro", max_length=75, blank=False)
    topic_id = models.CharField("ID do tópico", max_length=75, blank=False)
    query_url = models.URLField("URL para estratégia de busca", blank=False)

