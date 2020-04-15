$(document).ready(function () {
    var menuProfileButton = $('#menu-user .dropdown #dropdownMenu2')
    var dropDownMenu = $('#menu-user .dropdown .dropdown-menu')

    menuProfileButton.mouseenter(function () {
        dropDownMenu.slideDown(300)
    })

    $("#menu-user").mouseleave(function () {
        dropDownMenu.slideUp(300)
    })
});