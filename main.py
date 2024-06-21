from preprocessing import preprocess_video

def main():
    face_predictor_path = "/content/data/misc/shape_predictor_68_face_landmarks.dat"
    mean_face_path = "/content/data/misc/20words_mean_face.npy"
    origin_clip_path = "/content/data/clip.mp4"
    mouth_roi_path = "/content/data/roi.mp4"
    
    preprocess_video(origin_clip_path, mouth_roi_path, face_predictor_path, mean_face_path)

if __name__ == "__main__":
    main()
