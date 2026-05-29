// Show selected PDF file name

document.addEventListener("DOMContentLoaded", function () {

    var pdfInput = document.getElementById("pdf-input");

    var fileNameEl = document.getElementById("pdf-file-name");



    if (pdfInput && fileNameEl) {

        pdfInput.addEventListener("change", function () {

            if (pdfInput.files.length > 0) {

                fileNameEl.textContent = "Selected: " + pdfInput.files[0].name;

            } else {

                fileNameEl.textContent = "";

            }

        });

    }



    // Auto-dismiss flash messages after 6 seconds

    var flashMessages = document.querySelectorAll(".flash");

    flashMessages.forEach(function (msg) {

        setTimeout(function () {

            msg.style.transition = "opacity 0.5s";

            msg.style.opacity = "0";

            setTimeout(function () {

                msg.remove();

            }, 500);

        }, 6000);

    });

});

