$(document).ready(function() {
var currentColor = "";
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

    var addColorBox = function(color){
        $('#colors').append(
            '<div class="color_choice" style="background-color:' + color + '"></div>'
        )
    };



    var prepCanvas = function(){
        for (var i=0; i<definedColors.length; i++) {
            // Add each pre-defined color to the page
            addColorBox(definedColors[i]);
        };
    };

     var selectColor = function(){
        $('body').on('click', '.color_choice', function(e){
            currentColor = $(e.target).css('background-color');

        });
    };
    prepCanvas();
});
