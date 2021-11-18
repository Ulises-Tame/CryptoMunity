$('#thumbs').delegate('img', 'click', function() {
    var $this = $(this);
    // Clear formatting
    $('#thumbs img').removeClass('border-highlight');

    // Highlight with coloured border
    $this.addClass('border-highlight');
    
    // Changes the value of the form field "animal" to the file name shown in the image.
    $('[name="img"]').val($this.attr('id').substring($this.attr('id')) 
                            );
});