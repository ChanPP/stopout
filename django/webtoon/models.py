from django.db import models
from webtoon import crawler


class Webtoon(models.Model):
    webtoon_id = models.CharField(max_length=10)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}'

    def get_episode_list(self):
        episode_list = crawler.EpisodeData.get_episode_list(self.webtoon_id, 1)
        # print(episode_list)
        for episode in episode_list:
            # if Episode.objects.filter(episode_id=Episode['episode_id']).exists():
            #     continue

            Episode.objects.create(
                webtoon=self,
                episode_id=episode['episode_id'],
                title=episode['title'],
                rating=episode['rating'],
                created_date=episode['created_date'],
                thumbnail=episode['thumbnail'],
            )


class Episode(models.Model):
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE)
    episode_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    created_date = models.CharField(max_length=200)
    thumbnail = models.TextField(null=False)

    def __str__(self):
        return self.title

