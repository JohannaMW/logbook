$(document).ready(function() {
var selectedColor= "";
var definedColors = [
        "#f1f075",
        "#eaf7ca",
        "#c5e967",
        "#a3e46b",
        "#7ec9b1",
        "#b7ddf3",
        "#63b6e5",
        "#3ca0d3",
        "#1087bf",
        "#548cba",
        "#677da7",
        "#9c89cc",
        "#c091e6",
        "#d27591",
        "#f86767",
        "#e7857f",
        "#fa946e",
        "#f5c272",
        "#ede8e4",
        "#ffffff",
        "#cccccc",
        "#6c6c6c",
        "#1f1f1f"
    ];

    var selectColor = function() {
        $('body').on('click', '.color_choice', function (e) {
            console.log("you have clicked it!");
            selectedColor = $(e.target).css('background-color');
            var hexColor = rgb2hex(selectedColor);
            $("#id_marker_color").val(hexColor);
            console.log(hexColor);
        });
    };

    var selectImage = function() {
        $('button').on('click', function () {
            console.log("you have clicked the button!");
            var selectedImage = $(this).text();
            var symbol = selectedImage.toLowerCase();
            $("#id_marker_symbol").val(symbol);
            console.log(symbol);
        });
    };

    var hideFormFields = function () {

    };

  /*  var hideImageFields = function () {
        for (var i=0; i< imageFields.length; i++) {
            console.log(imageFields[i]);
            $('#'+imageFields[i]).hide();
            $("label[for=" + imageFields[i] + "]").hide();

        }
    };

    var fileUpload = function () {
        $("input:image").on('change', function () {
            var index = $(this).index();
            console.log(index);
            $('#'+index+1).show();
        });

    };*/

    var addColorBox = function (color) {
        // render color fields
        $('#colors').append(
                '<div class="color_choice" style="background-color:' + color + '"></div>'
        )};


    var prepColorPicker = function(){
        for (var i=0; i<definedColors.length; i++) {
            addColorBox(definedColors[i]);
        };
    };

    function rgb2hex(rgb) {
    rgb = rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
    function hex(x) {
        return ("0" + parseInt(x).toString(16)).slice(-2);
    }
    return "#" + hex(rgb[1]) + hex(rgb[2]) + hex(rgb[3]);
}

    prepColorPicker();
    selectColor();
    selectImage();
   // hideImageFields();
});
