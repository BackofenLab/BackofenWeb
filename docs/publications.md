---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
title:  Publications
---


<div class="publications">

<div class="search-and-filter-panel">
   <!-- Search Bar and Reset Button -->
  <div class="search-bar">
    <input type="text" id="search-bar" placeholder="Search..." />
    <div id="reset-all-filters"></div>
  </div>

  <!-- Filter Panel -->
  <button id="filter-toggle-button">Show Filters</button>
  <div class="filter-panel">
    <!-- Filter by Year -->
    <div class="filter-container">
      <div class="select-container">
        <select id="year-filter">
          <!-- Years will be added here dynamically -->
        </select>
      </div>
    </div>
    <!-- Filter by Author -->
    <div class="filter-container">
      <div class="select-container">
        <select id="author-filter">
            <option value="">All authors</option>
            <option value="Rolf Backofen">Rolf Backofen</option>
            <option value="Alexander Mitrofanov">Alexander Mitrofanov</option>
            <option value="Alireza Heidari">Alireza Heidari</option>
            <option value="Anika Erxleben">Anika Erxleben</option>
            <option value="Anup Kumar">Anup Kumar</option>
            <option value="Bérénice Batut">Bérénice Batut</option>
            <option value="Björn Grüning">Björn Grüning</option>
            <option value="David López Tabernero">David López Tabernero</option>
            <option value="Dilmurat Yusuf">Dilmurat Yusuf</option>
            <option value="Dominik Rabsch">Dominik Rabsch</option>
            <option value="Engy Nasr">Engy Nasr</option>
            <option value="José Manuel Dominguez">José Manuel Dominguez</option>
            <option value="Omer S. Alkhnbashi">Omer S. Alkhnbashi</option>
            <option value="Martin Raden">Martin Raden, nee Mann</option>
            <option value="Michael Uhl">Michael Uhl</option>
            <option value="Paul Zierep">Paul Zierep</option>
            <option value="Pavankumar Videm">Pavankumar Videm</option>
            <option value="Rick Gelhausen">Rick Gelhausen</option>
            <option value="Sanjay Kumar Srikakulam">Sanjay Kumar Srikakulam</option>
            <option value="Sebastian Schaaf">Sebastian Schaaf</option>
            <option value="Stefan Mautner">Stefan Mautner</option>
            <option value="Sven Hauns">Sven Hauns</option>
            <option value="Teresa Müller">Teresa Müller</option>
            <option value="Van Dinh Tran">Van Dinh Tran</option>
        </select>
      </div>
    </div>
    <!-- Filter by Type -->
    <div class="filter-container">
      <div class="select-container">
        <select id="type-filter">
          <!-- Types will be added here dynamically -->
        </select>
      </div>
    </div>
  </div>
  <!-- Publication Count -->
  <div id="publication-count">Publication count will be updated here...</div>

</div>

  <!-- Publication List -->
  {% include pub-list.html %}

  <button id="back-to-top" title="Back to top">↑</button>
</div>
