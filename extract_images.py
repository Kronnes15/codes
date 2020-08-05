'''This function crops images'''
def extract_images(path, gender, i):
    img=cv2.imread(path)
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=haar.detectMultiScale(gray, 1.5, 5)
    for x, y, w, h in faces:
        roi=img[y:y+h, x:x+w]
        cv2.imwrite('{}_{}.png'.format(gender, i), roi)