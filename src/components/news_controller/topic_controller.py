import sysfrom PyQt5.QtWidgets import \    QGridLayout, QVBoxLayout, \    QHBoxLayout, QLineEdit, QMessageBox, \    QApplicationfrom src.components.news_controller.news_controller import NewsControllerfrom src.components.window import Windowfrom src.widget_utils import fill_layout, create_btn, create_labelclass TopicController(Window):    def __init__(self, data, link_func, lines_func, manual=True):        super().__init__()        self.data = data        self.link_func = link_func        self.lines_func = lines_func        self.layout = QVBoxLayout(self)        if manual:            manual_layout = self.add_link_input()            self.layout.addLayout(manual_layout)        grid = self.add_topics()        self.layout.addLayout(grid)    def add_link_input(self):        manual_label = create_label('Enter Link', font_size=13, style='header')        manual_layout = QHBoxLayout()        manual_line = QLineEdit()        manual_btn = create_topic_btn('Add', lambda: self.send_link(manual_line.text()), large=False)        fill_layout(manual_layout, manual_label, manual_line, manual_btn)        return manual_layout    def add_topics(self):        grid = QGridLayout()        grid.setSpacing(20)        index = 0        for topic, articles in self.data.items():            topic = topic.capitalize()            on_click = lambda _, t=topic, a=articles: self.load_topic(t, a)            btn = create_topic_btn(topic, on_click)            grid.addWidget(btn, index // 2, index % 2)            index += 1        return grid    def send_link(self, link):        try:            self.link_func(link)            self.close()        except Exception as inst:            print(inst)            msg = QMessageBox()            msg.setIcon(QMessageBox.Information)            msg.setText('Error: Check Link and Try Again')            msg.setStandardButtons(QMessageBox.Ok)            msg.show()    def load_topic(self, topic, articles):        try:            NewsController(topic, articles, self.lines_func).show()        except Exception as inst:            print(inst)def create_topic_btn(name, on_click, large=True):    btn = create_btn(name, on_click, font_size=12, style='secondary')    if large:        btn.setMinimumSize(150, 50)    return btnif __name__ == '__main__':    test_data = {        'world': [],        'life': [],        'tech': [],        'money': [],        'business': [],        'travel': []    }    func = lambda: print("asdf")    app = QApplication(sys.argv)    ex = TopicController(test_data, func, func)    ex.show()    sys.exit(app.exec_())