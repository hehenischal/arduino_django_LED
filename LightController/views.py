import serial
import time
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from decouple import config


SERIAL_PORT = config('SERIAL_PORT')  
BAUD_RATE = int(config('BAUD_RATE')) 

def send_command(command):
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(int(config('SERIAL_PORT_OPEN_DELAY')))  

        ser.write(f"{command}\n".encode('utf-8'))
        print(f"Sent command: {command}")

        response = ser.readline().decode('utf-8').strip()
        print(f"Response from Arduino: {response}")

        ser.close()
    except PermissionError as e:
        print(f"PermissionError: {e}. Make sure the port is not in use by another program.")
    except serial.SerialException as e:
        print(f"SerialException: {e}. Failed to open port {SERIAL_PORT}.")
    except Exception as e:
        print(f"Error: {e}")

def index(request):
    return render(request,'index.html')

@csrf_exempt
def lighton(request):
    if request.method == 'POST':
        send_command('lightOn')
        return HttpResponse(f'<button class="btn btn-danger" hx-post="{reverse("lightoff")}" hx-trigger="click" hx-target = "this" hx-swap = "outerHTML"><i class="fas fa-lightbulb"></i> Turn Light Off</button>')
    else:
        return HttpResponse('Invalid request')
    
@csrf_exempt
def lightoff(request):
    if request.method == 'POST':
        send_command('lightOff')
        return HttpResponse(f'<button class="btn btn-success" hx-post="{(reverse("lighton"))}" hx-trigger="click" hx-target = "this" hx-swap = "outerHTML"><i class="fas fa-lightbulb"></i> Turn On Light</button>')
    else:
        return HttpResponse('Invalid request')