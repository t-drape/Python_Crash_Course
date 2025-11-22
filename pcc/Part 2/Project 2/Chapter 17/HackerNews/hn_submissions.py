import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

from operator import itemgetter

# Make an API call and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print("Status code:", r.status_code)

# Process info about each submission
submission_ids = r.json()

submission_dicts = []
plot_dicts = []
for sub_id in submission_ids[:30]:
	# Make a sperate API call for each submission.
	url = ('https://hacker-news.firebaseio.com/v0/item/' + str(sub_id) + '.json')
	sub_r = requests.get(url)
	print(sub_r.status_code)
	response_dict = sub_r.json()

	no_d = int(float(response_dict["descendants"]))
	link = response_dict["url"]
	plot_dict = {
		'value': no_d,
		'xlink': link,
	}
	plot_dicts.append(plot_dict)

	sub_dict = {
		'title': response_dict['title'],
		'link': 'https://news.ycombinator.com/item?id=' + str(sub_id),
		'comments': response_dict.get('descendants', 0)
	}
	submission_dicts.append(sub_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
 reverse=True)

plot_dicts = sorted(plot_dicts, key=itemgetter('value'), reverse=True)

names = []
for sub in submission_dicts:
	print("\nTitle:", sub['title'])
	print("Discussion link:", sub['link'])
	print('Comments:', sub['comments'])
	names.append(sub['title'])

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Trending Articles on HackerNews"
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file("Desktop/hn.svg")

