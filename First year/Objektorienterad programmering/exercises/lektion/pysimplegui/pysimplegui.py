import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
  [sg.Text('Hello')],
  [sg.Button('Avsluta')]
]

window = sg.Window('Mitt första PySimpleGUI fönster', layout, size=(500, 100))
#window.read()

#event loop
while True:
  event, values = window.read()
  if event in (sg.WIN_CLOSED, 'Avsluta'):
    print('Avslutar GUI:t')
    break
window.close()