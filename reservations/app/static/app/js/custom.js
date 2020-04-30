$(document).ready(function () {
    var menuProfileButton = $('#menu-user .dropdown #dropdownMenu2')
    var dropDownMenu = $('#menu-user .dropdown .dropdown-menu')

    menuProfileButton.mouseenter(function () {
        dropDownMenu.slideDown(300)
    })

    $("#menu-user").mouseleave(function () {
        dropDownMenu.slideUp(300)
    })

    $("#Update_profil").click(function () {
        $('form.hide').show(700);
        $('#Update_profil').hide();
    });

    $('#Cancel_update_profil').click(function () {
        $('#Update_profil').show();
        $('form.hide').hide(700);
    })
});