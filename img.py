def loadImg(path, x=1, y=1):
    '''
    @params:
    path :: string :: image path relative to root folder, drop leading and trailing / chars
    x :: int :: relative width scaling of image
    y :: int :: relative height scaling of image
    '''
    img = pg.image.load(path)
    wTransform = img.get_width() * x
    hTransform = img.get_height() * y
    img = pg.transform.scale(img, (wTransform, hTransform))
    return img, img.get_rect()

def moveImgRelCentre(screen, img, imgRect, x, y):
    '''
    Left = -x | Right = +x
      Up = -y | Down  = +y
    '''
    size = screen.get_size()
    centre = [dim/2 for dim in size]
    imgDim = img.get_width(), img.get_height()
    leftEdge, topEdge = centre[0] - (imgDim[0]/2) + x, centre[1] - (imgDim[1]/2) + y
    outputRect = pg.Rect((leftEdge, topEdge, imgDim[0], imgDim[1]))
    screen.blit(img, outputRect)
    return outputRect