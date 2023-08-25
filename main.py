import cv2
import detecthands as dh2
import gamestage
import mediapipe as mp
mp_hands = mp.solutions.hands
# initialize a game instance
# big loop. put the with hands stuff here?
    #run the mp model on a frame and be returned a cv2 image: image = runModel()
    #image = run_detection_model()
    #update_game(cv2image we receive)
    #uddate_view(image)
radius = 20
colour = (255, 102, 0)
thickness = 2

game = gamestage.GameStage(1, 1920, 1080)
cap = cv2.VideoCapture(0)
counter = 0
while True:
    # this is the controller component of MVC. We run the model on a given frame, and get back results data, as well as the image of it
    model_results = dh2.run_model(cap)
    image = model_results[0]
    results = model_results[1]
    image_height, image_width, _ = image.shape
    
    #print(image_width)
    #print(image_height)
    
    # essentially updating the game with all the new circles here
    game.check_circles(results, image_width, image_height)
    
    # "updating" the view ie drawing the still existing circles and updating viewfinder
    dh2.redraw_circles(image, game)
    
    if game.check_game_over():
        break
    
    if counter == 0:
        game.add_circle()
    elif counter == 60:
         counter = -1
    counter += 1
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

        
cap.release()