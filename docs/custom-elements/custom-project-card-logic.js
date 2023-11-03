var $grid = $('.grid').isotope({
    // options
    itemSelector: '.grid-item',
    layoutMode: 'masonry',
});

var $buttonGroup = $('.filters');
$buttonGroup.on('click', 'input', function(event) {
    var $button = $(event.currentTarget);
    var filterValue = $button.attr('data-filter');
    $grid.isotope({
        filter: filterValue
    });
});