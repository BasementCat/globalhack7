(function () {
    var url = '/api/resources?query=%QUERY&lang_code=' + window.lang_code;

    var bloodhound_resources = new Bloodhound({
        datumTokenizer: function (datum) {
            return Bloodhound.tokenizers.whitespace(datum);
        },
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        remote: {
            url: url,
            wildcard: '%QUERY',
            filter: function(data) {
                return $.map(data, function(resources, label) {
                    return {
                        value: resources,
                        label: label,
                    }
                }.bind(this));
            }.bind(this)
        },
    });

    bloodhound_resources.initialize();

    $('.typeahead').typeahead({
        hint: true,
        highlight: true,
        minLength: 1
    },
    {
        displayKey: 'label',
        templates: {
            suggestion: function(suggestion) {
                return '<p>' + suggestion.label + '</p>';
            }
        },
        name: 'resources',
        source: bloodhound_resources.ttAdapter()
    });

    $('#resource').on('typeahead:selected', function(event, value) {
        var resources = value.resources;
    });

    var $scroll_btns = $('.scroll-btn');
    $scroll_btns.click(function () {
        if ($(this).hasClass('right')) {
            $('.flag-container').animate( { scrollLeft: '+=215' }, 250);
        } else {
            $('.flag-container').animate( { scrollLeft: '-=215' }, 250);
        }
    });
})();
