from flask import Flask, request
import RPi.GPIO as GPIO

# 자기 자신의 파일명으로 객체 생성
app = Flask(__name__)

LED = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)


# ## 정적라우팅
##클라이언트가 URI로 "/"를 요청하면 옆에 있는 뷰함수가 자동호출# http://localhost:5000/
# @app.route("/")
# def helloworld():
#     return "Hello World"


# @app.route("/led/on") #http://localhost:5000/led/on
# def led_on():
#     GPIO.output(LED, GPIO.HIGH)
#     return "LED ON"


# @app.route("/led/off") #http://localhost:5000/led/off
# def led_off():
#     GPIO.output(LED, GPIO.LOW)
#     return "LED OFF"


# @app.route("/gpio/cleanup")
# def gpio_cleanip():
#     GPIO.cleanip()
#     return "GPIO CLEANUP"

## 자신의 파일을 직접 실행시켜 app.run()를 호출, 서버 실행
# if __name__ == "__main__":
#     app.run(host="0.0.0.0")

## 동적라우팅<산형 괄호>
# @app.route("/led/<state>")
# def led(state):
#     if state == "on":
#         GPIO.output(LED, GPIO.HIGH)
#     else:
#         GPIO.output(LED, GPIO.LOW)
#     return "LED " + state

# if __name__ == "__main__":
#     app.run(host="0.0.0.0")


## Flask를 이용한 LED 실습 (동적 라우팅<쿼리 스트링>)
@app.route("/led")
def led():
    state = request.args.get("state", "error")
    if state == "on":
        GPIO.output(LED, GPIO.HIGH)
        return "LED " + state
    elif state == "off":
        GPIO.output(LED, GPIO.LOW)
    elif state == "error":
        return "쿼리스트링 state가 전달되지 않았습니다."
    else:
        return "잘못된 쿼리스트링이 전달되었습니다."
    return "LED " + state


@app.route("/gpio/cleanup")
def gpio_cleanip():
    GPIO.cleanip()
    return "GPIO CLEANUP"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
