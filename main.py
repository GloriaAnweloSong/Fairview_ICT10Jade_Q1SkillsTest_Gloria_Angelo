from pyscript import document, display

def create_order(e):
    document.getElementById("ST_output").innerHTML = ""

    tea1 = document.getElementById("input1")
    tea2 = document.getElementById("input2")
    tea3 = document.getElementById("input3")

    subtotal1 = float(tea1.value) * tea1.checked
    subtotal2 = float(tea2.value) * tea2.checked
    subtotal3 = float(tea3.value) * tea3.checked

    subtotal = subtotal1 + subtotal2 + subtotal3

    display(f'You have to pay a total of ${subtotal}', target="ST_output")