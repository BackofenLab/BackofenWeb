---
layout: default
title: Teaching
---



<div>
{% assign term_hashes = site.data.semesters | keys | sort | reverse %}
{% for term_hash in term_hashes %}
  {% assign term = site.data.semesters[term_hash] %}

    {% for lecture in term.lectures %}
      {% include lecture-card.html lecture=lecture %}
    {% endfor %}

{% endfor %}
</div>