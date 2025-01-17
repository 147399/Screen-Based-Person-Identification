import face_recognition
import cv2
import os

def load_known_faces():
    known_encodings = []
    known_names = []
    
    for user_name in os.listdir("users"):
        user_folder = os.path.join("users", user_name)
        for image_file in os.listdir(user_folder):
            image_path = os.path.join(user_folder, image_file)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]
            known_encodings.append(encoding)
            known_names.append(user_name)
    
    return known_encodings, known_names

def recognize_user():
    known_encodings, known_names = load_known_faces()
    
    cap = cv2.VideoCapture(0)
    print("Tanıma işlemi başladı. Kameraya bakın...")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kameradan görüntü alınamıyor.")
            break
        
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        
        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name = "Bilinmiyor"
            
            if True in matches:
                match_index = matches.index(True)
                name = known_names[match_index]
            
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
        
        cv2.imshow("Tanıma Ekranı", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_user()
