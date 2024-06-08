
def r_kb_m_maker(ReplyKeyboardMarkup, KeyboardButton, l_event):
    k_m = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, selective=True)
    if len(l_event) != 0:
         for q in range(0, len(l_event)-1, 2):
             k_m.row(
                 KeyboardButton("/show_all_in {0:s}".format(l_event[q])),
                 KeyboardButton("/show_all_in {0:s}".format(l_event[q+1]))
             )
         if len(l_event) % 2 != 0:
             k_m.add(
                 KeyboardButton(
                     "/show_all_in {0:s}".format(
                         l_event[   len(l_event)-1  ]
                     )
             ))
    elif len(l_event) == 0:
        k_m.add(
            KeyboardButton("Эй!")
        )

    return k_m