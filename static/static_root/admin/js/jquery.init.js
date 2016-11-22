/* Puts the included jQuery into our own namespace using noConflict and passing
 * it 'true'. This ensures that the included jQuery doesn't pollute the global
 * namespace (i.e. this preserves pre-existing values for both window.$ and
 * window.jQuery).
 */
var django = django || {};
<<<<<<< HEAD
django.jQuery = jQuery.noConflict(true);
=======
django.jQuery = jQuery.noConflict(true);
>>>>>>> ee2cfbc3c6252a8fc1b79b7bb9ae76fd07f22d15
