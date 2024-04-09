import cv2
import face_recognition

image = cv2.imread('keanu.jpg') # test fotosu
image = cv2.resize(image, (640,480))

reevers_img = face_recognition.load_image_file('keanu.jpg') # fotoyu kaydetmek için yükleme
reevers_img_encoding = face_recognition.face_encodings(reevers_img)[0] # burada yüzlerin encodinglerini bulur. kaç tane yüz varsa ona göre index numarası girmeliyiz

test_img = face_recognition.load_image_file('test.jpg')
face_location = face_recognition.face_locations(test_img)
face_encoding = face_recognition.face_encodings(test_img, face_location)

(topleftx, toplefty, bottomrightx, bottomrighty) = face_location[0]
matched_faces = face_recognition.compare_faces(reevers_img_encoding, face_encoding)

if True in matched_faces:
    cv2.rectangle(image, (topleftx, toplefty), (bottomrightx, bottomrighty), (0,255,0), 2)
    cv2.imshow("fkdsgj", image)
    cv2.waitKey(0)