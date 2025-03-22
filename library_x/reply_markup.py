def r_kb_m_maker(ReplyKeyboardMarkup, KeyboardButton, l_event):
    km = []
    if l_event:  # Упрощаем проверку
        for q in range(0, len(l_event)-1, 2):
            km.append([
                KeyboardButton(text="/show_all_in {0:s}".format(l_event[q])),
                KeyboardButton(text="/show_all_in {0:s}".format(l_event[q+1]))
            ])
        
        if len(l_event) % 2 != 0:
            km.append([
                KeyboardButton(
                    text="/show_all_in {0:s}".format(l_event[-1])  # Используем -1 для последнего элемента
                )
            ])
    else:
        km.append([
            KeyboardButton(text="Эй!")
        ])
    
    return ReplyKeyboardMarkup(
        keyboard=km,
        resize_keyboard=True,
        one_time_keyboard=True,
        selective=True
    )
"""
def r_kb_m_maker(ReplyKeyboardMarkup, KeyboardButton, l_event):
    km = []
    if len(l_event) != 0:
         for q in range(0, len(l_event)-1, 2):
             km.append([
                 KeyboardButton(text="/show_all_in {0:s}".format(l_event[q])),
                 KeyboardButton(text="/show_all_in {0:s}".format(l_event[q+1]))
             ])
         if len(l_event) % 2 != 0:
             km.append([
                 KeyboardButton(
                     text="/show_all_in {0:s}".format(
                         l_event[   len(l_event)-1  ]
                     )
             )])
    elif len(l_event) == 0:
        km.append([
            KeyboardButton("Эй!")
        ])
    
    k_m = ReplyKeyboardMarkup(keyboard=km, resize_keyboard=True, one_time_keyboard=True, selective=True)
    return k_m
"""
