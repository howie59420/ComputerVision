import cv2
from keras.models import load_model
import numpy as np
import random
import time

options=['rock','paper','scissors','none']

def get_computer_choice():
    return random.choice(options[:-1])

def get_prediction():
    
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    input('The camera is ready, press enter to continue.')

     #the below is setting up a  3 seconds countdown for prep to show choice  
    for i in range(3, 0, -1):
        print(f'Get Ready in {i} secs ')
        time.sleep(1)
    print('GO !')
    

    start_time=time.time() 
    while time.time()<(start_time+3): 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):break

    #After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows() 
    #index selection of the available choices from list called options
    return options[np.argmax(prediction)]
    
        

def get_winner():
    computer_choice=get_computer_choice()
    user_choice=get_prediction()

    if computer_choice==user_choice:
        print(f'Draw, keep going! computer was {computer_choice}')
        return('draw')

    elif (computer_choice=='rock' and user_choice=='paper') \
        or (computer_choice=='paper' and user_choice=='scissors') \
        or (computer_choice=='scissors' and user_choice=='rock'):
       print(f'You win,computer was {computer_choice}')
       return('win')
    
    else:
        print(f'You lose,computer was {computer_choice}')
        return('lose')

def play():
    to_play=input('Do you want to play? y/n: ').lower()
    if to_play=='y':

        user_wins=0
        computer_wins=0

        while user_wins<3:
            result=get_winner()
            if result=='win':
                user_wins+=1
            elif result=='lose':
                computer_wins+=1
            else:
                user_wins=user_wins

            print(f'user has {user_wins} wins, computer has {computer_wins} wins.')

    else:
        exit()
        
play()

    





