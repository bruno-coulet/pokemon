        if self.rect.collidepoint(mx, my):  # Use the collidepoint method on the instance
            pg.draw.polygon(screen, HOVER_COLOR,[(PREV_BTN_X,PREV_BTN_Y),(PREV_BTN_X+50,PREV_BTN_Y+50),(PREV_BTN_X+50,PREV_BTN_Y-50)])
        else:
            # pg.draw.polygon(screen, self.color, [(NEXT_BTN_X,NEXT_BTN_Y),(NEXT_BTN_X+50,NEXT_BTN_Y+50),(NEXT_BTN_X+50,NEXT_BTN_Y-50)])
            pg.draw.polygon(screen, self.color, [(PREV_BTN_X,PREV_BTN_Y),(PREV_BTN_X+50,PREV_BTN_Y+50),(PREV_BTN_X+50,PREV_BTN_Y-50)])