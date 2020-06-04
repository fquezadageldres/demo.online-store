$(document).ready(function() {
    $('#reload').click(function() {
        location.reload();
    })
    $(document).on('change', '.btn-file :file', function() {
        var input = $(this),
            label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
        input.trigger('fileselect', [label]);
    });

    $('.btn-file :file').on('fileselect', function(event, label) {

        var input = $(this).parents('.input-group').find(':text'),
            log = label;

        if (input.length) {
            input.val(log);
        } else {
            if (log) alert(log);
        }

    });

    function readURL(input) {

        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function(e) {
                $('#img-upload').attr('src', e.target.result);

            }

            reader.readAsDataURL(input.files[0]);
        }
    }

    function upload_img() {
        $('#form').change(function(e) {
            e.preventDefault();
            var formData = new FormData(this);
            var div = $('#response').html();

            $.ajax({
                type: 'POST',
                url: 'p003_predict',
                data: formData,
                cache: false,
                contentType: false,
                processData: false,
                success: function(data) {
                    $('#form').addClass("hidden")
                    $('#predict').html(data.msg);
                    $('#cat').html('Gato: ' + data.cat + '%');
                    $('#dog').html('Perro: ' + data.dog + '%');
                    $('#other').html('Otra cosa: ' + data.other + '%');
                    $('#response').removeClass("hidden")
                },
                error: function(data) {
                    console.log(error);
                }
            });
        });
    }

    $("#imgInp").change(function() {
        readURL(this);
        upload_img();
    });
});