---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
title:  Bioinformatics
---

# Bioinformatics Group Freiburg

<hr>
<div class="row mt-5">
  <div class="col-lg-6 d-flex flex-column align-items-center">

  {% include contact-card.html
              header="Head of the Group"
              name="Prof. Dr. Rolf Backofen"
              email="backofen@informatik.uni-freiburg.de"
              phone="+49 (0) 761 / 203 - 7461"
  %}

  {% include contact-card.html
              header="Secretary"
              name="Monika Degen-Hellmuth"
              email="degenhel@informatik.uni-freiburg.de"
              phone="+49 (0) 761 / 203 - 7460"
  %}

  {% include contact-card.html
              header="Address"
              name=""
              chair="Bioinformatics Group"
              department="Department of Computer Science"
              university="Albert-Ludwigs-University Freiburg"
              street="Georges-Köhler-Allee 106"
              postcode="79110 Freiburg"
              country="Germany"
              icon="../assets/images/windrose.gif"
              link="../404.html"
              linktext="Location"
  %}
  </div>
  <div class="col-lg-6">

    <a href="http://www.bioinf.uni-freiburg.de/Research/index.html?en"><img src="{{ site.baseurl }}/assets/images/group-m.jpg" alt="Group"> </a>

  </div>
</div>


# News and information

<hr>
<div class="row mt-5">
    <div class="col-lg-9">
      {% include news-item.html
            date="June 2022"
            text="Deep Learning helps improve gene therapies and antiviral drugs"
            link="https://kommunikation.uni-freiburg.de/pm-en/press-releases-2022/deep-learning-helps-improve-gene-therapies-and-antiviral-drugs?set_language=en"
            link_text="News of the Technical Faculty"
      %}
      <!--- -->
      {% include news-item.html
            date="March 2022"
            text="Neues CRISPR-Element steuert Virenabwehr"
            link="http://news.tf.uni-freiburg.de/single-news/artikel/554/neues-crispr-element-steuert-virenabwehr.html?tx_ttnews%5Byear%5D=2022&tx_ttnews%5Bmonth%5D=03&cHash=7fcf76d6b3d3bb81698119f6bda6d0d0"
            link_text="News of the Technical Faculty"
      %}
      <!--- -->
      {% include news-item.html
            date="Feb 2022"
            text="IT-Sicherheitsmanagement der Univeristät Freiburg durch TÜV SÜD zertifiziert"
            link="http://news.tf.uni-freiburg.de/single-news/artikel/554/it-sicherheitsmanagement-der-universitaet-freiburg-durch-tuev-sued-zertifiziert.html?tx_ttnews%5Byear%5D=2022&tx_ttnews%5Bmonth%5D=02&cHash=fe7539014702eacc90c5bf550d530195"
            link_text="News of the Technical Faculty"
      %}
      <!--- -->
      {% capture text_with_links %}
          Im Rahmen der <a href="https://www.tf.uni-freiburg.de/studium/studieninteressierte/schueler/schueler#Sch_ler-Ingenieur-Akademie__SIA_" class="news-link">Schüler-Ingenieur-Akademie (SIA)</a> führen wir interessierte Schüerinnen und Schüler in unserem Workshop <a href="http://www.bioinf.uni-freiburg.de/Lehre/Courses/2012_WS/Workshop/" class="news-link">'Bioinformatik - finde einen Gendefekt'</a> in allgemeine Tätigkeiten und Aufgaben der Bioinformatikforschung ein.
      {% endcapture %}
      {% include news-item.html
            date="Feb 2022"
            text=text_with_links
      %}
      <!--- -->
      {% include news-item.html
            date="June 2019"
            text="Our work together with the collaborators from the German Cancer Research Center and the Faculty of Medicine has been published in Nature Communication."
            link="https://www.nature.com/articles/s41467-019-10489-2"
            link_text="Nature Communication"
      %}
      <!--- -->
      {% capture text_with_links %}
          The <a href="https://usegalaxy-eu.github.io/freiburg/" class="news-link">Freiburg Galaxy Team</a> offers an easy accessible, reproducible, and transparent framework for life science data analysis.
      {% endcapture %}
      {% include news-item.html
            text=text_with_links
      %}
      <!--- -->
      {% capture text_with_links %}
          Check out our <a href="http://rna.informatik.uni-freiburg.de/" class="news-link">Freiburg RNA tools web server!</a>
      {% endcapture %}
      {% include news-item.html
            text=text_with_links
      %}
      <!--- -->
      {% capture text_with_links %}
          Our <a href="http://modpepint.informatik.uni-freiburg.de/" class="news-link">MoDPepInt web server</a> released featuring domain-peptide interaction prediction for <a href="http://modpepint.informatik.uni-freiburg.de/SH2PepInt/" class="news-link">SH2</a>, <a href="http://modpepint.informatik.uni-freiburg.de/SH3PepInt/" class="news-link">SH3</a> and <a href="http://modpepint.informatik.uni-freiburg.de/PDZPepInt/" class="news-link">PDZ</a> domains.
      {% endcapture %}
      {% include news-item.html
            text=text_with_links
      %}
      <!--- -->
      {% capture link_url %}{{ site.baseurl }}/404.html{% endcapture %}
      {% include news-item.html
            text="Topics for theses or projects available."
            link=link_url
            link_text="Available Projects"
      %}
    </div>
    <div class="col-lg-3 galaxy-iframe">
      <iframe src="https://usegalaxy-eu.github.io/widgets/news.html" style="border: 0px; background: #f2f3f2; height: 540px;"></iframe>
    </div>
</div>