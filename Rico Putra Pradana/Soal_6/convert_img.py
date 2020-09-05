import cv2

img = {
    1: 'img/bu_tejo.jpg',
    2: 'img/yao_ming.jpg',
    3: 'img/gabut.jpg'
}

class ImageConverter:
    def __init__(self, selected_img):
        self.selected_img = cv2.imread(img.get(selected_img))

    def save_image(self, converted_img):
        cv2.imwrite('img_converted/a.png', converted_img)

    def convert_to_gray(self):
        img_gray = cv2.cvtColor(self.selected_img, cv2.COLOR_BGR2GRAY)
        return img_gray
    
    def show_img(self, img):
        cv2.imshow('Output', img)
        cv2.waitKey(0)