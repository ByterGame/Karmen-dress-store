const filterListItems = document.querySelectorAll('.filter-list li');
const dressItems = document.querySelectorAll('.dress-item');

(function ($) {
    $(document).ready(function ($) {

        function animateValue(element, start, end, duration) {
            let startTimestamp = null;

            const step = (timestamp) => {
                if (!startTimestamp) startTimestamp = timestamp;
                const progress = Math.min((timestamp - startTimestamp) / duration, 1);
                element.textContent = `₽${(start + (end - start) * progress).toFixed(0)}`;

                if (progress < 1) {
                    requestAnimationFrame(step);
                }
            }
            requestAnimationFrame(step);
        }

        function updateTotal(element) {
            const quantityInput = element;
            const row = quantityInput.closest('tr');
            const price = parseFloat(quantityInput.getAttribute('data-cost'));
            const totalCell = row.querySelector('.product-total');

            const newQuantity = parseInt(quantityInput.value);
            const newTotal = price * newQuantity;
            const currentTotal = parseFloat(totalCell.textContent.replace('₽', ''));

            animateValue(totalCell, currentTotal, newTotal, 1500);

            const totalTotalCell = document.getElementById('total-data-cost');
            const currentTotalTotal = parseFloat(totalTotalCell.textContent.replace('₽', ''));
            let grandTotal = 0;
                document.querySelectorAll('.table-body-row').forEach(row => {
                    const cell = row.querySelector('.product-price');
                    const count = row.querySelector('.quantity-input');
                    const cellValue = parseFloat(cell.textContent.replace('₽', ''));
                    const countValue = parseInt(count.value) || 0;
                    grandTotal += !isNaN(cellValue) && !isNaN(countValue) ? cellValue * countValue : 0;
                });

            animateValue(totalTotalCell, currentTotalTotal, grandTotal, 1500);

            let itemCount = 0;
            document.querySelectorAll('.quantity-input').forEach(input => {
                itemCount += parseInt(input.value) || 0;
            });
            let finalShippingCost = 0;
            if (itemCount <= 0) {
                finalShippingCost = 0;
            } else {
                const shippingCost = 1000 / itemCount;
                finalShippingCost = shippingCost < 100 ? 0 : shippingCost;
            }
            const shippingCell = document.getElementById('total-shipping-cost');
            const currentShipping = parseFloat(shippingCell.textContent.replace('₽', ''));
            animateValue(shippingCell, currentShipping, finalShippingCost, 1500);

            const totalAllCell = document.getElementById('total-all-cost');

            const grandAllTotal = grandTotal + finalShippingCost;
            const currentAllTotal = parseFloat(totalAllCell.textContent.replace('₽', ''));
            animateValue(totalAllCell, currentAllTotal, grandAllTotal, 1500);
        }

        document.querySelectorAll('.quantity-input').forEach(input => {
            input.addEventListener('input', function() {
                updateTotal(this);
            });
        });

        $('.product-controls li:not(:last-child)').on('click', function () {
            var filterValue = $(this).attr('data-filter');

            $('.product-controls li').removeClass('active');
            $(this).addClass('active');

            if (filterValue === "") {
                $('#product-list .dress-item').show();
            } else {
                $('#product-list .dress-item').hide();
                $('#product-list .dress-item' + filterValue).show();
            }
        });

        $('#color-filter-select').on('change', function () {
            var color = $(this).val();

            $('.product-controls li').removeClass('active');

            if (color === "") {
                $('#product-list .dress-item').show();
            } else {
                $('#product-list .dress-item').hide();
                $('#product-list .dress-item[data-color="' + color + '"]').show();
            }
        });

        // testimonial sliders
        $(".testimonial-sliders").owlCarousel({
            items: 1,
            loop: true,
            autoplay: true,
            responsive: {
                0: {
                    items: 1,
                    nav: false
                },
                600: {
                    items: 1,
                    nav: false
                },
                1000: {
                    items: 1,
                    nav: false,
                    loop: true
                }
            }
        });

        // homepage slider
        $(".homepage-slider").owlCarousel({
            items: 1,
            loop: true,
            autoplay: true,
            nav: true,
            dots: false,
            navText: ['<i class="fas fa-angle-left"></i>', '<i class="fas fa-angle-right"></i>'],
            responsive: {
                0: {
                    items: 1,
                    nav: false,
                    loop: true
                },
                1000: {
                    items: 1,
                    nav: true,
                    loop: true
                },
                2000: {
                    items: 1,
                    nav: true,
                    loop: true
                }
            }
        });

        // logo carousel
        $(".logo-carousel-inner").owlCarousel({
            items: 4,
            loop: true,
            autoplay: true,
            margin: 30,
            responsive: {
                0: {
                    items: 1,
                    nav: false
                },
                600: {
                    items: 3,
                    nav: false
                },
                1000: {
                    items: 4,
                    nav: false,
                    loop: true
                }
            }
        });

        // count down
        if ($('.time-countdown').length) {
            $('.time-countdown').each(function () {
                var $this = $(this), finalDate = $(this).data('countdown');
                $this.countdown(finalDate, function (event) {
                    var $this = $(this).html(event.strftime('' + '<div class="counter-column"><div class="inner"><span class="count">%D</span>Days</div></div> ' + '<div class="counter-column"><div class="inner"><span class="count">%H</span>Hours</div></div>  ' + '<div class="counter-column"><div class="inner"><span class="count">%M</span>Mins</div></div>  ' + '<div class="counter-column"><div class="inner"><span class="count">%S</span>Secs</div></div>'));
                });
            });
        }

        // projects filters isotop
        $(".product-filters li").on('click', function () {

            $(".product-filters li").removeClass("active");
            $(this).addClass("active");

            var selector = $(this).attr('data-filter');

            $(".product-lists").isotope({
                filter: selector,
            });

        });

        // isotop inner
        $(".product-lists").isotope();

        // magnific popup
        $('.popup-youtube').magnificPopup({
            disableOn: 700,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false
        });

        // light box
        $('.image-popup-vertical-fit').magnificPopup({
            type: 'image',
            closeOnContentClick: true,
            mainClass: 'mfp-img-mobile',
            image: {
                verticalFit: true
            }
        });

        // homepage slides animations
        $(".homepage-slider").on("translate.owl.carousel", function () {
            $(".hero-text-tablecell .subtitle").removeClass("animated fadeInUp").css({'opacity': '0'});
            $(".hero-text-tablecell h1").removeClass("animated fadeInUp").css({
                'opacity': '0',
                'animation-delay': '0.3s'
            });
            $(".hero-btns").removeClass("animated fadeInUp").css({'opacity': '0', 'animation-delay': '0.5s'});
        });

        $(".homepage-slider").on("translated.owl.carousel", function () {
            $(".hero-text-tablecell .subtitle").addClass("animated fadeInUp").css({'opacity': '0'});
            $(".hero-text-tablecell h1").addClass("animated fadeInUp").css({'opacity': '0', 'animation-delay': '0.3s'});
            $(".hero-btns").addClass("animated fadeInUp").css({'opacity': '0', 'animation-delay': '0.5s'});
        });


        // stikcy js
        $("#sticker").sticky({
            topSpacing: 0
        });

        //mean menu
        $('.main-menu').meanmenu({
            meanMenuContainer: '.mobile-menu',
            meanScreenWidth: "992"
        });

        // search form
        $(".search-bar-icon").on("click", function () {
            $(".search-area").addClass("search-active");
        });

        $(".close-btn").on("click", function () {
            $(".search-area").removeClass("search-active");
        });

    });


    jQuery(window).on("load", function () {
        jQuery(".loader").fadeOut(1000);
    });

    document.getElementById('phone-input').addEventListener('input', function(e) {
        let input = e.target.value.replace(/\D/g, ''); // Удаляем все нечисловые символы

        if (!input.startsWith("7") && !input.startsWith("8")) {
            input = "7" + input;
        }

        if (e.inputType === 'deleteContentBackward') {
            return;
        }

        let formattedInput = '+7 ';
        if (input.length > 1) {
            formattedInput += '(' + input.substring(1, 4);
        }
        if (input.length >= 4) {
            formattedInput += ') ' + input.substring(4, 7);
        }
        if (input.length >= 7) {
            formattedInput += '-' + input.substring(7, 9);
        }
        if (input.length >= 9) {
            formattedInput += '-' + input.substring(9, 11);
        }

        e.target.value = formattedInput;
    });


//     const addressInput = document.getElementById('address');
// const suggestionsList = document.getElementById('suggestions');
//
// addressInput.addEventListener('input', () => {
//     const query = addressInput.value;
//
//     if (query.length > 3) {
//         fetch("https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json",
//                 "Accept": "application/json",
//                 "Authorization": "Token YOUR_API_KEY"
//             },
//             body: JSON.stringify({ "query": query })
//         })
//         .then(response => response.json())
//         .then(data => {
//             suggestionsList.innerHTML = "";  // Очистка предыдущих подсказок
//             const suggestions = data.suggestions;
//
//             suggestions.forEach(suggestion => {
//                 const item = document.createElement('li');
//                 item.textContent = suggestion.value;
//                 item.addEventListener('click', () => {
//                     addressInput.value = suggestion.value;  // Подставляем выбранное значение
//                     suggestionsList.innerHTML = "";  // Очищаем подсказки
//                 });
//                 suggestionsList.appendChild(item);
//             });
//         })
//         .catch(error => console.error("Error:", error));
//     } else {
//         suggestionsList.innerHTML = "";  // Убираем подсказки, если длина текста < 3
//     }
// });



}(jQuery));

$(document).on('click', '.navbar-toggler', function () {
    $toggle = $(this);

    if (materialKit.misc.navbar_menu_visible == 1) {
        $('body').removeClass('nav-open');
        materialKit.misc.navbar_menu_visible = 0;
        $('#bodyClick').remove();
        setTimeout(function () {
            $toggle.removeClass('toggled');
        }, 550);

        $('body').removeClass('nav-open-absolute');
    } else {
        setTimeout(function () {
            $toggle.addClass('toggled');
        }, 580);


        div = '<div id="bodyClick"></div>';
        $(div).appendTo("body").click(function () {
            $('body').removeClass('nav-open');

            if ($('nav').hasClass('navbar-absolute')) {
                $('body').removeClass('nav-open-absolute');
            }
            materialKit.misc.navbar_menu_visible = 0;
            $('#bodyClick').remove();
            setTimeout(function () {
                $toggle.removeClass('toggled');
            }, 550);
        });

        if ($('nav').hasClass('navbar-absolute')) {
            $('html').addClass('nav-open-absolute');
        }

        $('body').addClass('nav-open');
        materialKit.misc.navbar_menu_visible = 1;
    }
});

materialKit = {
    misc: {
        navbar_menu_visible: 0,
        window_width: 0,
        transparent: true,
        fixedTop: false,
        navbar_initialized: false,
        isWindow: document.documentMode || /Edge/.test(navigator.userAgent)
    }
};

$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
})

document.addEventListener("DOMContentLoaded", function () {
    const links = document.querySelectorAll("[data-toggle='modal']");

    links.forEach(link => {
        link.addEventListener("click", function (event) {
            // Закрыть любое открытое модальное окно
            const openModal = document.querySelector(".modal.show");
            if (openModal) {
                $(openModal).modal("hide");
            }
        });
    });
});