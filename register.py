import cv2
import os

def save_user_images(user_name):
    directory = f"users/{user_name}"
    os.makedirs(directory, exist_ok=True)
    
    cap = cv2.VideoCapture(0)
    print("Yüz görüntülerinizi kaydetmek için kameraya bakın...")
    
    count = 0
    while count < 10:  # 10 görüntü kaydedilecek
        ret, frame = cap.read()
        if not ret:
            print("Kameradan görüntü alınamıyor.")
            break
        
        cv2.imshow("Yüzünüzü kaydediyoruz", frame)
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('c'):  # 'c' tuşuna basarak görüntü kaydedilir
            file_path = os.path.join(directory, f"{count}.jpg")
            cv2.imwrite(file_path, frame)
            print(f"Görüntü kaydedildi: {file_path}")
            count += 1
        
        if key == ord('q'):  # 'q' ile çıkış
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print("Kayıt işlemi tamamlandı.")

if __name__ == "__main__":
    user_name = input("Kullanıcı adınızı girin: ")
    save_user_images(user_name)
