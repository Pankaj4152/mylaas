from text_image_toolkit.image import ImageResizer, ImageFilter

def test_resize():
    r = ImageResizer()
    assert "Resized image to" in r.resize("img", (50, 50))

def test_filter():
    f = ImageFilter()
    assert "Blurred" in f.blur("img")