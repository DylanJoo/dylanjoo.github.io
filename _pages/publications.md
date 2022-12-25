---
layout: single
title: "Publications"
permalink: /publications/
author_profile: true
---

<br>*Text-to-text Multi-view Learning For Passage Re-ranking*
<br><sub>**Jia-Huei Ju**, Jheng-Hong Yang, Chuan-Ju Wang</sub>
<br><sub> SIGIR 2021 // [paper](https://dl.acm.org/doi/10.1145/3404835.3463048) [slide]()</sub>

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
