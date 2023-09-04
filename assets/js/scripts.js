document.addEventListener("DOMContentLoaded", function() {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.navbar ul');
    if (burger && nav) {
        burger.addEventListener('click', function() {
            nav.classList.toggle('nav-open');
        });
    } else {
        console.warn('burger or nav elements not found!');
    }

    function toggleResetButtonVisibility() {
        // get current filter values
        var search_query = $('#search-bar').val();
        var filter_year = $('#year-filter').val();
        var filter_author = $('#author-filter').val();
        var filter_type = $('#type-filter').val();

        // check if any filter is applied
        if (search_query || filter_year || filter_author || filter_type) {
            // if yes, show the reset button
            $('#reset-all-filters').show();
        } else {
            // if no, hide the reset button
            $('#reset-all-filters').hide();
        }
    }

    function updatePublications() {
        var search_query = $('#search-bar').val().toLowerCase();
        var filter_year = $('#year-filter').val();
        var filter_author = $('#author-filter').val().toLowerCase();
        var filter_type = $('#type-filter').val().toLowerCase();

        $('.publication').each(function() {
            var content = $(this).text().toLowerCase();
            var year = $(this).attr('data-year');
            var type = $(this).attr('data-type').toLowerCase();
            var authors = $(this).attr('data-author').split(';').map(author => author.trim().toLowerCase());
            var matches_search = !search_query || content.includes(search_query);
            var matches_filter_year = !filter_year || year == filter_year;
            var matches_filter_author = !filter_author || authors.includes(filter_author);
            var matches_filter_type = !filter_type || type.includes(filter_type);

            $(this).toggle(matches_search && matches_filter_year && matches_filter_author && matches_filter_type);
        });

        var visible_count = $('.publication:visible').length;
        $('#publication-count').text(visible_count + " publication(s) found!");
    }

    function toggleResetButtonVisibility() {
        // get current filter values
        var search_query = $('#search-bar').val();
        var filter_year = $('#year-filter').val();
        var filter_author = $('#author-filter').val();
        var filter_type = $('#type-filter').val();

        // check if any filter is applied
        if (search_query || filter_year || filter_author || filter_type) {
            // if yes, show the reset button
            $('#reset-all-filters').show();
        } else {
            // if no, hide the reset button
            $('#reset-all-filters').hide();
        }
    }

    $('#reset-all-filters').click(function() {
        $('#search-bar').val('');
        $('#year-filter').prop('selectedIndex', 0);
        $('#author-filter').val('');
        $('#type-filter').val('');
        updatePublications();
        toggleResetButtonVisibility();
        document.getElementById('publications').scrollTop = 0;
    });

    $('#search-bar, #year-filter, #author-filter, #type-filter').on('input change', function() {
        updatePublications();
        toggleResetButtonVisibility();
    });

    var years = {};
    $('.publication').each(function() {
        var year = $(this).attr('data-year');
        years[year] = (years[year] || 0) + 1;
    });
    var year_filter = $('#year-filter');
    year_filter.append('<option value="">All years</option>');
    Object.keys(years).sort().reverse().forEach(function(year) {
        year_filter.append('<option value="' + year + '">' + year + ' (' + years[year] + ')' + '</option>');
    });

    var types = {};
    $('.publication').each(function() {
        var type = $(this).attr('data-type');
        types[type] = (types[type] || 0) + 1;
    });
    var type_filter = $('#type-filter');
    type_filter.append('<option value="">All types</option>');
    Object.keys(types).sort().forEach(function(type) {
        type_filter.append('<option value="' + type + '">' + type + ' (' + types[type] + ')' + '</option>');
    });


    document.getElementById('filter-toggle-button').addEventListener('click', function() {
        var filterPanel = document.querySelector('.filter-panel');
        filterPanel.classList.toggle('expanded');
    });


    // When the user scrolls down 20px from the top of the document, show the button
    $('.main-content').scroll(function() {
        if ($('.main-content').scrollTop() > 20) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }
    });


    // When the user clicks on the button, scroll to the top of the document
    $('#back-to-top').click(function() {
        $('.main-content').animate({scrollTop : 0}, 800);
    });

    updatePublications();
});
