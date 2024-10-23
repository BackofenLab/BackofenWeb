---
layout: default
title: Teaching
---



<div class="container">

  <div class="row justify-content-center">
    {% assign term_hashes = site.data.semesters | keys | sort | reverse %}
    {% for term_hash in term_hashes %}
      {% assign term = site.data.semesters[term_hash] %}

        {% for lecture in term.lectures %}
          <div class="col-xl-6 mb-4 d-flex justify-content-center">
            <div class="lecture-card" style="width: 800px;">
              {% include lecture-card.html lecture=lecture %}
            </div>
          </div>
        {% endfor %}

    {% endfor %}
  </div>
</div>