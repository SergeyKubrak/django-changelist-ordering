/* Extract an object id (numeric) from a DOM id. Assumes that a "-" is used
   as delimiter. Returns either the id found or 0 if something went wrong.

       extract_item_id('foo_bar_baz-327') -> 327
 */
function extract_item_id(elem_id) {
    var i = elem_id.indexOf('-');
    if(i >= 0)
        return parseInt(elem_id.slice(i+1), 10);

    return 0;
}

/* Setup django csrf-token for ajax calls, necessary since Django 1.2.5 */
/* See http://docs.djangoproject.com/en/1.2/releases/1.2.5/#csrf-exception-for-ajax-requests */

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});
