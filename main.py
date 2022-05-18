from module.imageBlurLoop import blurImageWithLoop
from module.imageUnblur import unblurImageWithLoop

#blurImageWithLoop()
#unblurImageWithLoop()


def startCode():
    action = input(f'What operation do you want to perform \nFor Blur type 1 \nFor UnBlur type 2\n')
    if(action == '1'):
        blurImageWithLoop()
    elif(action == '2'):
        unblurImageWithLoop()
    else:
        print('Invalid Input')
        startCode()

startCode()