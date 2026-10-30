def dragon_category(power, stamina):
    if power==stamina:
        return "BALANCED"
    elif power>=2*stamina:
        return "OVERPOWERED"
    elif power*2<=stamina:
        return "UNBREAKABLE"
    elif power>stamina and power<2*stamina:
        return "MIGHTY"
    elif stamina>power and stamina<2*power:
        return "ENDURING"
power=int(input("Enter the power of the dragon: "))
stamina=int(input("Enter the stamina of the dragon: "))
print(dragon_category(power, stamina))