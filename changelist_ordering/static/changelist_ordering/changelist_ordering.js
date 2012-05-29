changeListOrdering.jQuery(function($){
    function resetGrid(){
            $('#result_list tbody tr:even').removeClass('row2 row1').addClass('row1');
            $('#result_list tbody tr:odd').removeClass('row2 row1').addClass('row2');
    }
    $( "#result_list tbody" ).sortable({
        handle: '.drag_handle',
        items: 'tr',
        axis: 'y',
        start: function(event, ui){
            var h = new Array();
            $('#result_list thead tr > *').each(function(element){
                h.push($(this).outerWidth());
            });
            $('> *', ui.helper).each(function(i, element){
                $(element).outerWidth(h[i]);
            });
        },
        update: function() {
            var position = new Array();

            $( "#result_list tbody tr").each(function(i, element) {
                position.push(extract_item_id($('.page_marker', element).attr('id'))) ;
            });
            $.ajax({
                type: 'Post',
                url: '.',
                data: {
                    '__cmd': 'change_ordering',
                    'position': JSON.stringify(position)
                },
                success:  function(data) {
                    resetGrid();
                }
            });
        }
    });
});