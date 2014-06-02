$(function() {
    image_path = $('div.cover_image div a').html();
    image = document.createElement('img');
    image.src = "/assets/" + image_path;
    image.alt = "image preview";
    image.height = "120";
    image.width ="120";
    $('div.cover_image div a').html(image);
    $('div.cover_image div a img').css("border", "1px solid #000");
});