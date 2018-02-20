$(document).ready(function() {
    'use strict';
 
	$('.same-height').matchHeight({
        byRow: true,
        property: 'height',
        target: null,
        remove: false
    });
    $('.same-height2').matchHeight({
        byRow: true,
        property: 'height',
        target: null,
        remove: false
    });
    
    $(".reload-group").find("select, input").change(function () {
	   if($(this).val()) {
			var values = [];
			$(".reload-group").find("select, input").each(function () {
				values.push($(this).attr("id") + "=" + $(this).val());	
			});   
            $(".ftg-page-loader").show();
            var anchor = $(this).parents(".reload-group").data("anchor");
			location.href = "?" + values.join("&") + "#" + anchor;
	   }
    });
    
    /*-----------------------------------------------------------------------------------*/
    /*	SCROLL NAVIGATION HIGHLIGHT
    /*-----------------------------------------------------------------------------------*/
    var headerWrapper = parseInt($('.navbar').outerHeight(), 10);
    var header_height = $('.navbar').outerHeight();
    var shrinked_header_height = 65;
    var firstStyle = {
        'padding-top': '' + shrinked_header_height + 'px',
        'margin-top': '-' + shrinked_header_height + 'px'
    };
    $('.onepage section').css(firstStyle);
    var secondStyle = {
        'padding-top': '' + header_height + 'px',
        'margin-top': '-' + header_height + 'px'
    };
    $('.onepage section:first-of-type').css(secondStyle);
    var offsetTolerance = -(header_height);
    //Detecting user's scroll
    $(window).scroll(function() {
        //Check scroll position
        var scrollPosition = parseInt($(this).scrollTop(), 10);
        //Move trough each menu and check its position with scroll position then add current class
        $('.onepage .navbar ul.navbar-nav a').not('.menu-logo a').each(function() {
            var thisHref = $(this).attr('href');
            var thisTruePosition = parseInt($(thisHref).offset().top, 10);
            var thisPosition = thisTruePosition - headerWrapper - offsetTolerance;
            if (scrollPosition >= thisPosition) {
                $('.onepage .current').removeClass('current');
                $('.onepage .navbar ul.navbar-nav a[href=' + thisHref + ']').parent('li').addClass('current');
            }
        });
        //If we're at the bottom of the page, move pointer to the last section
        var bottomPage = parseInt($(document).height(), 10) - parseInt($(window).height(), 10);
        if (scrollPosition == bottomPage || scrollPosition >= bottomPage) {
            $('.onepage .current').removeClass('current');
            $('.onepage .navbar ul.navbar-nav a:last').parent('li').addClass('current');
        }
    });
    /*-----------------------------------------------------------------------------------*/
    /*	STICKY HEADER
    /*-----------------------------------------------------------------------------------*/
    var options = {
        offset: 350,
        offsetSide: 'top',
        classes: {
            clone: 'banner--clone fixed',
            stick: 'banner--stick',
            unstick: 'banner--unstick'
        },
        onStick: function() {
            $($.SmartMenus.Bootstrap.init);
        }
    };
    var banner = new Headhesive('.navbar', options);
    $('.offset').css('padding-top', $('.navbar').height() + 'px');
    $(window).resize(function() {
        $('.offset').css('padding-top', $('.navbar').height() + 'px');
    });
    $('.onepage .navbar .nav li a').on('click', function() {
        $('.navbar .navbar-collapse.in').collapse('hide');
        $('.nav-bars').removeClass('is-active');
    });
    /*-----------------------------------------------------------------------------------*/
    /*	HAMBURGER MENU ICON
    /*-----------------------------------------------------------------------------------*/
    $(".nav-bars").on( "click", function() {
        $(".nav-bars").toggleClass("is-active");
    });
    /*-----------------------------------------------------------------------------------*/
    /*	LOCALSCROLL
    /*-----------------------------------------------------------------------------------*/
    $('.navbar, .scroll').localScroll({
        hash: false
    });
    /*-----------------------------------------------------------------------------------*/
    /*	SWIPER
    /*-----------------------------------------------------------------------------------*/

    $('.swiper-container.blog-carousel').each(function() {
        $(this).swiper({
            pagination: '.blog-carousel-wrapper .swiper-pagination',
            nextButton: '.blog-carousel-wrapper .swiper-button-next',
            prevButton: '.blog-carousel-wrapper .swiper-button-prev',
            slidesPerView: 3,
            breakpoints: {
                668: {
                    slidesPerView: 1
                },
                768: {
                    slidesPerView: 2
                },
                1024: {
                    slidesPerView: 3
                }
            },
            centeredSlides: false,
            paginationClickable: true,
            spaceBetween: 30,
            grabCursor: true
        });
        var $swipers = $(this);
    });
    $('.swiper-container.image-blog-wide').each(function() {
        $(this).swiper({
            pagination: '.image-blog-wide-wrapper .swiper-pagination',
            nextButton: '.image-blog-wide-wrapper .swiper-button-next',
            prevButton: '.image-blog-wide-wrapper .swiper-button-prev',
            slidesPerView: 4,
            breakpoints: {
                668: {
                    slidesPerView: 1
                },
                1441: {
                    slidesPerView: 2
                },
                1921: {
                    slidesPerView: 3
                }
            },
            centeredSlides: false,
            paginationClickable: true,
            spaceBetween: 6,
            grabCursor: true
        });
        var $swipers = $(this);
    });
    $('.swiper-container.image-blog').each(function() {
        $(this).swiper({
            pagination: '.image-blog-wrapper .swiper-pagination',
            nextButton: '.image-blog-wrapper .swiper-button-next',
            prevButton: '.image-blog-wrapper .swiper-button-prev',
            slidesPerView: 3,
            breakpoints: {
                668: {
                    slidesPerView: 1
                },
                768: {
                    slidesPerView: 2
                },
                1024: {
                    slidesPerView: 3
                }
            },
            centeredSlides: false,
            paginationClickable: true,
            spaceBetween: 6,
            grabCursor: true
        });
        var $swipers = $(this);
    });
    $('.swiper-container.image-carousel').each(function() {
        $(this).swiper({
            pagination: '.image-carousel-wrapper .swiper-pagination',
            nextButton: '.image-carousel-wrapper .swiper-button-next',
            prevButton: '.image-carousel-wrapper .swiper-button-prev',
            slidesPerView: "auto",
            centeredSlides: false,
            pagination: false,
            spaceBetween: 6,
            grabCursor: true
        });
        var $swipers = $(this);
    });
    /*-----------------------------------------------------------------------------------*/
    /*	GO TO TOP
    /*-----------------------------------------------------------------------------------*/
    $.scrollUp({
        scrollName: 'scrollUp',
        // Element ID
        scrollDistance: 300,
        // Distance from top/bottom before showing element (px)
        scrollFrom: 'top',
        // 'top' or 'bottom'
        scrollSpeed: 300,
        // Speed back to top (ms)
        easingType: 'linear',
        // Scroll to top easing (see http://easings.net/)
        animation: 'fade',
        // Fade, slide, none
        animationInSpeed: 200,
        // Animation in speed (ms)
        animationOutSpeed: 200,
        // Animation out speed (ms)
        scrollText: '<span class="btn btn-square"><i class="ion-android-arrow-up"></i></span>',
        // Text for element, can contain HTML
        scrollTitle: false,
        // Set a custom <a> title if required. Defaults to scrollText
        scrollImg: false,
        // Set true to use image
        activeOverlay: false,
        // Set CSS color to display scrollUp active point, e.g '#00FFFF'
        zIndex: 1001 // Z-Index for the overlay
    });
    /*-----------------------------------------------------------------------------------*/
    /*	TAB COLLAPSE
    /*-----------------------------------------------------------------------------------*/
    $('#tab1').tabCollapse({
        tabsClass: 'hidden-sm hidden-xs',
        accordionClass: 'visible-sm visible-xs'
    });
    $('#tab1').on('shown-accordion.bs.tabcollapse', function() {
        $('.panel-group').find('.panel-default:has(".in")').addClass('panel-active');
        $('.panel-group').on('shown.bs.collapse', function(e) {
            $(e.target).closest('.panel-default').addClass(' panel-active');
        }).on('hidden.bs.collapse', function(e) {
            $(e.target).closest('.panel-default').removeClass(' panel-active');
        });
    });
    /*-----------------------------------------------------------------------------------*/
    /*	TOGGLE
    /*-----------------------------------------------------------------------------------*/
    $('.panel-group').find('.panel-default:has(".in")').addClass('panel-active');
    $('.panel-group').on('shown.bs.collapse', function(e) {
        $(e.target).closest('.panel-default').addClass(' panel-active');
    }).on('hidden.bs.collapse', function(e) {
        $(e.target).closest('.panel-default').removeClass(' panel-active');
    });
    /*-----------------------------------------------------------------------------------*/
    /*	PROGRESS BAR
    /*-----------------------------------------------------------------------------------*/
    $('.progress-list .progress .bar').progressBar({
        shadow: false,
        percentage: false,
        animation: true,
        height: 12
    });
    /*-----------------------------------------------------------------------------------*/
    /*	DATA REL
    /*-----------------------------------------------------------------------------------*/
    $('a[data-rel]').each(function() {
        $(this).attr('rel', $(this).data('rel'));
    });
    /*-----------------------------------------------------------------------------------*/
    /*	TOOLTIP
    /*-----------------------------------------------------------------------------------*/
    if ($("[rel=tooltip]").length) {
        $("[rel=tooltip]").tooltip();
    }
    /*-----------------------------------------------------------------------------------*/
    /*	PRETTIFY
    /*-----------------------------------------------------------------------------------*/
    window.prettyPrint && prettyPrint();
    /*-----------------------------------------------------------------------------------*/
    /*	LAZY LOAD GOOGLE MAPS
    /*-----------------------------------------------------------------------------------*/
    ;
    (function($, window, document, undefined) {
        var $window = $(window),
            mapInstances = [],
            $pluginInstance = $('.google-map').lazyLoadGoogleMaps({
                callback: function(container, map) {
                    var $container = $(container),
                        center = new google.maps.LatLng($container.attr('data-lat'), $container.attr('data-lng'));

                    map.setOptions({
                        center: center,
                        zoom: 15,
                        zoomControl: true,
                        zoomControlOptions: {
                            style: google.maps.ZoomControlStyle.DEFAULT,
                        },
                        disableDoubleClickZoom: false,
                        mapTypeControl: true,
                        mapTypeControlOptions: {
                            style: google.maps.MapTypeControlStyle.DROPDOWN_MENU,
                        },
                        scaleControl: true,
                        scrollwheel: false,
                        streetViewControl: true,
                        draggable: true,
                        overviewMapControl: false,
                        mapTypeId: google.maps.MapTypeId.ROADMAP
                    });
                    new google.maps.Marker({
                        position: center,
                        map: map
                    });

                    $.data(map, 'center', center);
                    mapInstances.push(map);

                    var updateCenter = function() {
                        $.data(map, 'center', map.getCenter());
                    };
                    google.maps.event.addListener(map, 'dragend', updateCenter);
                    google.maps.event.addListener(map, 'zoom_changed', updateCenter);
                    google.maps.event.addListenerOnce(map, 'idle', function() {
                        $container.addClass('is-loaded');
                    });
                }
            });

        $window.on('resize', $pluginInstance.debounce(1000, function() {
            $.each(mapInstances, function() {
                this.setCenter($.data(this, 'center'));
            });
        }));

    })(jQuery, window, document);
    /*-----------------------------------------------------------------------------------*/
    /*	INSTAGRAM
    /*-----------------------------------------------------------------------------------*/
    var instagramFeed = new Instafeed({
        target: 'instafeed-widget',
        get: 'user',
        limit: 6,
        userId: 1215763826,
        accessToken: '1215763826.f1627ea.dad6ca96bd7642519b573d52c3ef467f',
        resolution: 'low_resolution',
        template: '<div class="item col-xs-4 col-sm-6 col-md-4"><figure class="overlay small"><a href="{{link}}" target="_blank"><img src="{{image}}" /></a></figure></div>',
        after: function() {
            $('#instafeed-widget figure.overlay a').prepend('<span class="over"><span></span></span>');
        }
    });
    $('#instafeed-widget').each(function() {
        instagramFeed.run();
    });

    var instagramFeed2 = new Instafeed({
        target: 'instafeed-full',
        get: 'user',
        limit: 9,
        userId: 1215763826,
        accessToken: '1215763826.f1627ea.dad6ca96bd7642519b573d52c3ef467f',
        resolution: 'standard_resolution',
        template: '<div class="item col-sm-4"><figure class="overlay instagram"><a href="{{link}}" target="_blank"><img src="{{image}}" /></a></figure></div>',
        after: function() {
            $('#instafeed-full figure.overlay a').prepend('<span class="over"><span></span></span>');
        }
    });
    $('#instafeed-full').each(function() {
        instagramFeed2.run();
    });

    var instagramFeed3 = new Instafeed({
        target: 'instafeed',
        get: 'user',
        limit: 6,
        userId: 1215763826,
        accessToken: '1215763826.f1627ea.dad6ca96bd7642519b573d52c3ef467f',
        resolution: 'low_resolution',
        template: '<div class="item col-xs-6 col-sm-4 col-md-2"><figure class="overlay instagram"><a href="{{link}}" target="_blank"><img src="{{image}}" /></a></figure></div>',
        after: function() {
            $('#instafeed figure.overlay a').prepend('<span class="over"><span></span></span>');
        }
    });
    $('#instafeed').each(function() {
        instagramFeed3.run();
    });
    /*-----------------------------------------------------------------------------------*/
    /*	FITVIDS VIDEO
    /*-----------------------------------------------------------------------------------*/
    $('.player').fitVids();
    /*-----------------------------------------------------------------------------------*/
    /*	COUNTER UP
    /*-----------------------------------------------------------------------------------*/
    $('.fcounter').counterUp({
        delay: 50,
        time: 1000
    });
    /*-----------------------------------------------------------------------------------*/
    /*	PARALLAX MOBILE
    /*-----------------------------------------------------------------------------------*/
    if (navigator.userAgent.match(/Android/i) || navigator.userAgent.match(/webOS/i) || navigator.userAgent.match(/iPhone/i) || navigator.userAgent.match(/iPad/i) || navigator.userAgent.match(/iPod/i) || navigator.userAgent.match(/BlackBerry/i)) {
        $('.parallax').addClass('mobile');
    }
    /*-----------------------------------------------------------------------------------*/
    /*	BACKGROUND VIDEO PARALLAX
    /*-----------------------------------------------------------------------------------*/
    $('#video-fish').backgroundVideo({
        $outerWrap: $('.outer-wrap'),
        pauseVideoOnViewLoss: false,
        parallaxOptions: {
            effect: 1.9
        }
    });
    /*-----------------------------------------------------------------------------------*/
    /*	LOADER
    /*-----------------------------------------------------------------------------------*/
    $(".pageloader").lsPreloader({

        backgroundColor: "#252525",
        logoImage: "style/images/logo-light.png",
        minimumTime: .5,
        progressHeight: "0",
        progressColor: "#fff",
        percentFontSize: "18px"

    });
    /*-----------------------------------------------------------------------------------*/
    /*	VANILLA
    /*-----------------------------------------------------------------------------------*/
    var myForm;
    myForm = new VanillaForm($("form.vanilla-form"));
    /*-----------------------------------------------------------------------------------*/
    /*	COLLAGEPLUS
    /*-----------------------------------------------------------------------------------*/
    collage();


    function collage() {
        $('.collage').removeWhitespace().collagePlus({
            'fadeSpeed': 5000,
            'targetHeight': 300,
            'effect': 'effect-2',
            'direction': 'vertical',
            'allowPartialLastRow': true
        });
    };
    
    
    
    // This is just for the case that the browser window is resized
    var resizeTimer = null;
    $(window).on('resize', function() {
        // hide all the images until we resize them
        $('.collage .collage-image-wrapper').css("opacity", 0);
        // set a timer to re-apply the plugin
        if (resizeTimer) clearTimeout(resizeTimer);
        resizeTimer = setTimeout(collage, 200);
    });
});