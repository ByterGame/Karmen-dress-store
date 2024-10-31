const filterListItems = document.querySelectorAll('.filter-list li');
const dressItems = document.querySelectorAll('.dress-item');

(function ($) {
    $(document).ready(function ($) {
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


$(document).ready(function () {
    // Закрытие окна входа при нажатии на ссылку открытия окна регистрации
    $('#loginModal').on('click', '[data-target="#registrationModal"]', function () {
        $('#loginModal').modal('hide'); // Закрыть текущее окно входа
    });
});

$(document).ready(function () {
    $('#register-form').on('submit', function (event) {
        event.preventDefault();
        const form = $(this);

        // Очистка предыдущих ошибок перед отправкой
        form.find('.error-message').remove();
        form.find('.is-invalid').removeClass('is-invalid');

        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: form.serialize(),
            success: function (response) {
                if (response.status === 'success') {
                    //alert('Account created successfully!');
                    //location.reload(); // обновление страницы после успешной регистрации
                    $('#registrationModal').modal('hide'); // Закрываем окно регистрации
                    $('#loginModal').modal('show'); // Открываем окно входа
                } else {
                    // Отображение ошибок в форме
                    $.each(response.errors, function (field, messages) {
                        if (field === '__all__') {
                            $('#register-form').prepend(`<div class="error-message text-danger">${messages[0]}</div>`);
                        } else {
                            const input = form.find(`[name="${field}"]`);
                            input.addClass('is-invalid');
                            input.after(`<div class="error-message text-danger">${messages[0]}</div>`);
                        }
                    });
                }
            },
            error: function () {
                alert('An unexpected error occurred. Please try again.');
            }
        });
    });
});

$(document).ready(function () {
    $('#login-form').on('submit', function (event) {
        event.preventDefault(); // предотвратить обычную отправку формы
        const form = $(this);

        // Очистите предыдущие ошибки перед отправкой
        form.find('.error-message').remove();
        form.find('.is-invalid').removeClass('is-invalid');

        $.ajax({
            type: 'POST',
            url: form.attr('action'), // путь к представлению
            data: form.serialize(),
            success: function (response) {
                if (response.status === 'success') {
                    //alert('Successfully logged in!');
                    location.reload();
                } else {
                    // Отображение ошибок в форме
                    $.each(response.errors, function (field, messages) {
                        if (field === '__all__') {
                            $('#login-form').prepend(`<div class="error-message text-danger">${messages[0]}</div>`);
                        } else {
                            const input = form.find(`[name="${field}"]`);
                            input.addClass('is-invalid');
                            input.after(`<div class="error-message text-danger">${messages[0]}</div>`);
                        }
                    });
                }
            },
            error: function () {
                alert('An unexpected error occurred. Please try again.');
            }
        });
    });
});


$(document).on('click', '.add-to-cart', function(e) {
    e.preventDefault();

    const dressId = $(this).data('dress-id');

    $.ajax({
    url: "{% url 'add_to_cart' %}",
    type: "POST",
    data: {
    'dress_id': dressId,
    'csrfmiddlewaretoken': '{{ csrf_token }}'
},
    success: function(response) {
    if (response.status === 'success') {
    alert(response.message);
} else {
    alert(response.message);
}
},
    error: function() {
    alert('Произошла ошибка. Попробуйте снова.');
}
});
});