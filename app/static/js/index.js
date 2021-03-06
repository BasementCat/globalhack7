(function () {
    var url = '/api/search-resources?query=%QUERY&lang_code=' + window.lang_code;

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

    $('#id_resource').on('typeahead:selected typeahead:autocompleted', function(event, value) {
        // swap out readable label for resource ID values and set hidden category ID field before submit
        var resources = value.value;
        var resource_ids = resources.map(function (r) { return r.resource_id });
        var category_id = resources[0].category_id;
        $('#id_category').val(category_id);
        $(this).val(resource_ids);
        $('#search-resources').submit();
    });

    var $scroll_btns = $('.scroll-btn');
    $scroll_btns.click(function () {
        if ($(this).hasClass('right')) {
            $('.flag-container').animate( { scrollLeft: '+=215' }, 250);
        } else {
            $('.flag-container').animate( { scrollLeft: '-=215' }, 250);
        }
    });

    $('.need-have-switch').click(function () {
        $(this).addClass('active');
        $(this).siblings('.need-have-switch').removeClass('active');

        var $is_have_input = $(this).siblings('.is-have');
        if ($(this).hasClass('have')) {
            $is_have_input.val('true');
        } else {
            $is_have_input.val('false');
        }
    });


    (function(){
        var counter=0;
        $('.scroll-btn.left').on('click', function(){
            if (counter++>37) {
                $('ul.flags').prepend('<li><a href="#"><img src="/static/pirate.jpg" /></a></li>');
            }
        });
    })();
})();
