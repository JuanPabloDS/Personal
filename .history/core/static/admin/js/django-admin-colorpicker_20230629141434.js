document.addEventListener("DOMContentLoaded", function() {
    var colorPickers = document.querySelectorAll(".color-picker");
    colorPickers.forEach(function(picker) {
      var textField = picker.previousSibling;
      picker.addEventListener("change", function() {
        textField.value = picker.value;
      });
    });
  });