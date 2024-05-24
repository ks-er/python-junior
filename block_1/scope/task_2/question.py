"""
Что будет выведено после выполнения кода? Почему?
"""

def transmit_to_space(message):
   
    def data_transmitter(): #2 определение функции data_transmitter
        print(message) #4 выводим message, оно пришло в параметре - выводим Test message

    data_transmitter() #3 вызов data_transmitter #5 после попадаем сюда, 
        #но возвращаемого значения у transmit_to_space нет


print(transmit_to_space("Test message")) #1 вызов transmit_to_space #6 возврат из метода transmit_to_space
    # со значением None (не было возвращаемого значения) и в итоге выводится на экран None

# в терминале
# Test message
# None
