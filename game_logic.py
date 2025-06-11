class GameLogic:
    def __init__(self, picture, my_window):
        self.picture = picture
        self.my_window = my_window
        self.total_score = 0
        self.opponent_total_score = 0

    def player_draw(self, score_label):
        self.picture.show_card()
        score = self.picture.count_score(self.picture.current_card)
        self.total_score += score
        score_label.config(text=int(self.total_score))

    def opponent_draw(self, opponent_score_label):
        if self.opponent_total_score <= 16 and self.total_score <= 21:
            self.picture.show_oponent_card()
            self.opponent_game_score(opponent_score_label)

    def opponent_game_score(self, opponent_score_label):
        if self.opponent_total_score < 17:
            if len(self.picture.oponent_image_labels) > 0 and self.picture.hidden_card:
                if not getattr(self.picture, "hidden_card_added", False):
                    opponent_score_value = self.picture.count_score(self.picture.hidden_card)
                    self.opponent_total_score += opponent_score_value
                    self.picture.hidden_card_added = True
            score = self.picture.count_score(self.picture.current_card)
            self.opponent_total_score += score
            opponent_score_label.config(text=int(self.opponent_total_score))

    def deal_initial_cards(self, score_label, opponent_score_label, first_button, second_button, third_button):
        self.picture.reset_cards()
        self.total_score = 0
        self.opponent_total_score = 0
        score_label.config(text="Score")
        opponent_score_label.config(text="Bot score")
        self.picture.show_card()
        self.player_draw(score_label)
        self.picture.show_card()
        self.player_draw(score_label)
        self.picture.show_oponent_card()
        self.opponent_game_score(opponent_score_label)
        self.picture.show_oponent_card()
        self.opponent_game_score(opponent_score_label)
        first_button.place(x=30, y=380)
        second_button.place(x=200, y=380)
        third_button.place_forget()

    def end_game(self, score_label, opponent_score_label, first_button, second_button, third_button):
        first_button.place_forget()
        second_button.place_forget()
        third_button.place_forget()
        text_result = ""
        if self.total_score == self.opponent_total_score:
            text_result = "DRAW"
        elif self.total_score > self.opponent_total_score and self.total_score <= 21:
            text_result = "WIN!!!"
        elif self.total_score < self.opponent_total_score and self.opponent_total_score <= 21:
            text_result = "LOSS"
        elif self.opponent_total_score > 21:
            text_result = "WIN!!!"
        elif self.total_score > 21:
            text_result = "LOSS"

        if text_result == "WIN!!!":
            result_bg = "#FFD700"
            result_fg = "#232946"
        elif text_result == "LOSS":
            result_bg = "#e74c3c"
            result_fg = "#ffffff"
        else:
            result_bg = "#818DF5"
            result_fg = "#ffffff"

        result_label = Label(
            self.my_window,
            text=text_result,
            width=10,
            bg=result_bg,
            fg=result_fg,
            relief="ridge",
            font=("Helvetica", 18, "bold"),
            bd=4,
            padx=12,
            pady=8
        )
        result_label.place(x=200, y=170)
        opponent_score_label.config(text=int(self.opponent_total_score))