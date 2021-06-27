$(document).ready(function () {
    const door_type_div = $('#div_id_door_type');
    const pass_width_div = $('#div_id_pass_width');
    const pass_height_div = $('#div_id_pass_height');
    const total_width_div = $('#div_id_total_width');
    const total_height_div = $('#div_id_total_height');
    const mechanism_width_div = $('#div_id_mechanism_width');
    const ustluk_div = $('#div_id_ustluk');
    const glass_div = $('#div_id_glass');
    const opening_direction_div = $('#div_id_opening_direction');
    const color_div = $('#div_id_color');
    const options_div = $('#div_id_options');
    const radar_activations_div = $('#div_id_radar_activations');

    let selected_door = '';

    const doors = [
        {
            name: "Düz",
            types: [
                {
                    name:  "TEK HAREKETLİ",
                    short: "th_standart",
                    image: "/static/img/sld/th_standart.png",
                },
                {
                    name:  "TEK SBT. + TEK HRK.",
                    short: "ts_th_standart",
                    image: "/static/img/sld/ts_th_standart.png",
                },
                {
                    name:  "İKİ HAREKETLİ",
                    short: "ih_standart",
                    image: "/static/img/sld/ih_standart.png",
                },
                {
                    name:  "İKİ SBT. + İKİ HRK.",
                    short: "is_ih_standart",
                    image: "/static/img/sld/is_ih_standart.png",
                },
            ]
        },
        {
            name: "Cam",
            types: [
                {
                    name:  "TEK HAREKETLİ",
                    short: "th_cam",
                    image: "/static/img/sld/th_cam.png",
                },
                {
                    name:  "TEK SBT. + TEK HRK.",
                    short: "ts_th_cam",
                    image: "/static/img/sld/ts_th_cam.png",
                },
                {
                    name:  "İKİ HAREKETLİ",
                    short: "ih_cam",
                    image: "/static/img/sld/ih_cam.png",
                },
                {
                    name:  "İKİ SBT. + İKİ HRK.",
                    short: "is_ih_cam",
                    image: "/static/img/sld/is_ih_cam.png",
                },
            ]
        },
        {
            name: "Teleskopik",
            types: [
                {
                    name:  "İKİ HAREKETLİ",
                    short: "ih_teleskop",
                    image: "/static/img/sld/ih_teleskop.png",
                },
                {
                    name:  "İKİ HRK. + İKİ SBT.",
                    short: "ih_is_teleskop",
                    image: "/static/img/sld/ts_ih_is_teleskop.png",
                },
                {
                    name:  "DÖRT HAREKETLİ",
                    short: "dh_teleskop",
                    image: "/static/img/sld/dh_teleskop.png",
                },
                {
                    name:  "DÖRT HRK. + İKİ SBT.",
                    short: "dh_is_teleskop",
                    image: "/static/img/sld/is_dh_is_teleskop.png",
                },
            ]
        },
    ];

    const glass_type_list = [
        '4+4 Bombeli Şeffaf Lamine',
        '5+5 Bombeli Şeffaf Lamine',
        '6+6 Bombeli Şeffaf Lamine',
        '4+4 Bombeli Opak Lamine',
        '5+5 Bombeli Opak Lamine',
        '6+6 Bombeli Opak Lamine',
    ];

    const color_list = [
        'Ral Boy',
        'Mat Eloksa',
        'Renkli Mat Eloksal',
        '304 Kalite Mat',
        '304 Kalite Ayna',
        '304 Kalite Satina',
        '316 Kalite Mat',
        '316 Kalite Ayna',
        '316 Kalite Satina',
    ];

    const options_list = [
        {
            name:  'El Terminali',
            short: 'el_terminali',
        },
        {
            name:  'Acil Stop',
            short: 'acil_stop',
        },
        {
            name:  'Elektronik Kilit',
            short: 'elektronik_kilit',
        },
        {
            name:  'Batarya',
            short: 'batarya',
        },
        {
            name: 'Konum Anahtarı Standart',
            short: 'konum_anahtari_standart',
        },
        {
            name:  'Konum Anahtarı Sıva Üstü',
            short: 'konum_anahtarı_sivaustu',
        },
    ];

    const radar_activation_list = [
        {
            name: 'Mikrodalga Radar',
            short: 'mikrodalga_radar'
        },
        {
            name: 'Combine Safety - Activation',
            short: 'combine_safety_activation'
        },
        {
            name: 'Yaklaşım Sensörü ',
            short: 'yaklasim_sensoru'
        },
        {
            name: 'Emniyet Fotoseli',
            short: 'emniyet_fotoseli'
        }
    ];

    total_width_div.hide();
    total_height_div.hide();
    mechanism_width_div.hide();
    ustluk_div.hide();
    glass_div.hide();
    color_div.hide();
    options_div.hide();
    radar_activations_div.hide();

    glass_div.find('input').removeAttr('required');
    color_div.find('input').removeAttr('required');


    // Renkler
    let color_selectbox = door_type_div.clone().attr('id', 'colors');
    color_selectbox.find('select').removeAttr('id');
    color_selectbox.find('select').attr('name', 'colors').removeAttr('required');;
    color_selectbox.find('label').text('Renkler').removeClass('requiredField');

    color_div.before(color_selectbox);
    color_selectbox.find('option').not(':first').remove();


    $(color_list).each(function (i, color) {
        color_selectbox.find('option').last().after(`<option value="${color}">${color}</option>`)
    });

    // checkbox
    const different_color_label = $('<label/>', {
        text: '  Farklı bir renk girmek istiyorum.',
        id: 'add-different-color'
    });

    $('<input/>', {
        type: 'checkbox',
    }).prependTo(different_color_label);

    color_div.before(different_color_label);

    color_selectbox.find('select').change(function () {
        color_div.find('input').val($(this).val());
    });

    $('#add-different-color input').change(function () {
        if(color_div.is(':hidden')){
            color_div.show();
            color_selectbox.hide();
            color_div.find('input').val('');
        } else {
            color_div.hide();
            color_selectbox.show();
            color_selectbox.find('select').change();
        }
    });


    // Camlar

    let glasses_selectbox = door_type_div.clone().attr('id', 'glasses');
    glasses_selectbox.find('select').attr('name', 'glasses').removeAttr('required').removeAttr('id');
    glasses_selectbox.find('label').text('Standart Camlar').removeClass('requiredField');


    glass_div.before(glasses_selectbox);
    glasses_selectbox.find('option').not(':first').remove();


    $(glass_type_list).each(function (i, glass) {
        glasses_selectbox.find('option').last().after(`<option value="${glass}">${glass}</option>`)
    });

    // checkbox
    const different_glass_label = $('<label/>', {
        text: '  Farklı bir cam girmek istiyorum.',
        id: 'add-different-glass'
    });

    $('<input/>', {
        type: 'checkbox',
    }).prependTo(different_glass_label);

    glass_div.before(different_glass_label);

    glasses_selectbox.find('select').change(function () {
        glass_div.find('input').val($(this).val());
    });

    $('#add-different-glass input').change(function () {
        if(glass_div.is(':hidden')){
            glass_div.show();
            glasses_selectbox.hide();
            glass_div.find('input').val('');
        } else {
            glass_div.hide();
            glasses_selectbox.show();
            glasses_selectbox.find('select').change();
        }
    });
    // Camlar


    // Kapı tiplerini alma
    let door_name_list = [];

    $.each(doors, function (i, door) {
        door_name_list.push(door['name'])
    });
    // Yeni bi select box oluşturma
    let door_name = door_type_div.clone().attr('id', 'door_name');
    door_name.find('select').removeAttr('id');
    door_name.find('select').attr('name', 'door_name');
    door_type_div.after(door_name);
    door_type_div.hide();


    // select box doldurma işlemleri.
    door_name.find('option').not(':first').remove();

    $(door_name_list).each(function (i, door) {
        door_name.find('option').last().after(`<option value="${door}">${door}</option>`)
    });

    door_name.find('select').change(function () {
        $('.types').remove();

        let name = $(this).val();
        let door = doors.find(door => door.name === name);
        let types_div = $('<div/>',{
            'class': 'types form-group'
        }).insertAfter(door_name);

        $(door.types).each(function (i, typ) {
            // TODO edit image url with varibale
            let bg = $('<div/>', {
                'class': 'background',
                'style': 'background-image: url(' + typ.image + ')'
            }).appendTo(types_div);

            bg.append(`<p>${typ.name}</p>`);

            $('<input/>', {
                'name': 'type-of-door',
                'value': typ.short,
                'type': 'radio',
            }).appendTo(bg);
        });

        $('input[name=type-of-door]').click(function(){
            selected_door = $(this).val();
            $('select[name=door_type] option').removeAttr('selected');
            $('select[name=door_type] option[value='+ selected_door +']').prop('selected', 'selected');

            if(selected_door == 'th_standart' || selected_door == 'ih_standart'){

                total_width_div.hide();
                total_height_div.show();
                mechanism_width_div.show();
                ustluk_div.hide();

                total_width_div.find('input').val('');
                total_height_div.find('input').val('');

                pass_height_div.find('input').change(function () {
                    total_height_div.find('input').val(parseInt($(this).val()) + 110);
                });
                pass_width_div.find('input').change(function () {
                    mechanism_width_div.find('input').val(parseInt($(this).val()));
                });

            }
            else if (selected_door == 'ts_th_standart' || selected_door == 'is_ih_standart'){
                mechanism_width_div.hide();
                total_height_div.show();
                total_width_div.show();
                ustluk_div.show();

                ustluk_div.find('input').checked = false;
                mechanism_width_div.find('input').val('');

                // toplam yükseklik ve genişliği hesaplama
                pass_height_div.find('input').change(function () {
                    total_height_div.find('input').val(parseInt($(this).val()) + 110);
                });
                pass_width_div.find('input').change(function () {
                    total_width_div.find('input').val($(this).val());
                });

            } // else if

            if(selected_door == 'ts_th_standart'  || selected_door == 'th_standart'){
                opening_direction_div.show();
            }
            else{
                opening_direction_div.hide();
                opening_direction_div.find('option:selected').prop('selected', false).removeAttr('selected');
                opening_direction_div.find('option:first').prop('selected', 'selected');

            }
        });

        $('input[name=pass_height]').change(function () {
            if ((selected_door == 'ts_th_standart' ||
                selected_door == 'is_ih_standart') &&
                !ustluk_div.find('input').first().checked){
                // calculation of pass_heigth
            }
        });
    });

    // options
    // elementlerin oluşturulması
    const options_form_group = $('<div/>', {
        class: 'form-group'
    });
    options_div.after(options_form_group);
    $('<label/>', {class: 'col-form-label', text:'Opsiyonlar'}).appendTo(options_form_group);

    $(options_list).each(function (i, option) {
        if (i % 2 == 0){
            options_form_group.append($('<div/>', {class: 'specifications door-options', id: `option-${i / 2}`}));
        }
        let option_div= $('<div/>', {
            class: 'specific',
        }).appendTo($(`#option-${Math.floor(i / 2)}`));

        $('<div/>', {
            class: 'bg',
            style: `background-image: url(/static/img/sld/options/${option.short}.png`,
        }).appendTo($(option_div));

        let option_label = $('<label/>').appendTo(option_div);

        option_label.append(`<p>${option.name}</p>`);

        $('<input/>',{
            value: option.short,
            type: 'checkbox'
        }).appendTo(option_label);

    });

    // options secilenleri alma işlemi
    $('.door-options input').click(function () {
        let input = options_div.find('input');
        let curr_value = $(this).val();

        if(this.checked){
            if(input.val() == '')
                input.val(curr_value);
            else
                input.val(input.val() + ' ' + curr_value);
        }
        else {
            input.val(input.val().replace(curr_value, '').replace('  ', ' '));
        }
    });
    // radar ve aktivaston
    // elementlerin oluşturulması
    const radar_form_group = $('<div/>', {
        class: 'form-group'
    });
    radar_activations_div.after(radar_form_group);
    $('<label/>', {class: 'col-form-label', text:'Radar Ve Aktivasyonlar'}).appendTo(radar_form_group);

    $(radar_activation_list).each(function (i, radar) {
        if (i % 2 == 0){
            radar_form_group.append($('<div/>', {class: 'specifications door-radars', id: `radar-${i / 2}`}));
        }
        let radar_div= $('<div/>', {
            class: 'specific',
        }).appendTo($(`#radar-${Math.floor(i / 2)}`));

        $('<div/>', {
            class: 'bg',
            style: `background-image: url(/static/img/sld/radars/${radar.short}.png`,
        }).appendTo($(radar_div));

        let radar_label = $('<label/>').appendTo(radar_div);

        radar_label.append(`<p>${radar.name}</p>`);

        $('<input/>',{
            name: 'door-image',
            value: radar.short,
            type: 'checkbox'
        }).appendTo(radar_label);

    });

    // options secilenleri alma işlemi
    $('.door-radars input').change(function () {
        let curr_value = $(this).val()
        let input = radar_activations_div.find('input');

        if(this.checked){
            if(input.val() == '')
                input.val(curr_value);
            else
                input.val(input.val() + ' ' + curr_value);
        }
        else {
            input.val(input.val().replace(curr_value, '').replace('  ', ' '));
        }
        if(curr_value == 'mikrodalga_radar' || curr_value == 'yaklasim_sensoru'){
            let emniyet_fotoseli = $('.door-radars input[value=emniyet_fotoseli]');
            this.checked ? emniyet_fotoseli.prop('checked', true).change() : emniyet_fotoseli.prop('checked', false).change();
        }
        if(curr_value == 'emniyet_fotoseli'){
            let combine_safety = $('.door-radars input[value=combine_safety_activation]');
            this.checked ? combine_safety.prop('disabled', true) : combine_safety.prop('disabled', false);
        }
        if(curr_value == 'combine_safety_activation'){
            let emniyet_fotoseli = $('.door-radars input[value=emniyet_fotoseli]');
            this.checked ? emniyet_fotoseli.prop('disabled', true) : emniyet_fotoseli.prop('disabled', false);
        }
    });


    $('form').submit(function (e) {
        let submit_status = true;
        if(glass_div.find('input').val() === ''){
            alert('Cam tipi boş bırakılamaz.');
            submit_status=false;
        }

        if(color_div.find('input').val() === '') {
            alert('Renk boş bırakılamaz.');
            submit_status = false;
        }
        if(!submit_status)
            e.preventDefault();

    });
});
