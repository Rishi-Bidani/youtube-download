from colorama import Fore


class TableMaker:
    def __init__(self, num_columns, max_for_each_column, color_for_heading="WHITE"):
        self.num_columns = num_columns
        self.max_for_each_column = max_for_each_column  # has to be a list
        self.color_for_heading = color_for_heading.upper()  # BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
        self.heading_dict = {}
        self.top_line_2 = []
        self.bottom_line_2 = []
        self.bottom_line_func_2 = []
        self.all_headings = []

    def heading(self, list_of_headings):
        for i in range(self.num_columns):
            heading = "heading" + f'{i}'
            self.all_headings.append(heading)
            self.heading_dict[f'{heading}'] = (f'{list_of_headings[i]}', len(f'{list_of_headings[i]}'),
                                               self.max_for_each_column[i])
            top_line = ("╔" + "═" * self.heading_dict[heading][2] + "══╗")
            bottom_line = ("•" + "-" * self.heading_dict[heading][2] + "--•")
            bottom_line_func = ("-" + "-" * self.heading_dict[heading][2] + "---")
            self.top_line_2.append(top_line)
            self.bottom_line_2.append(bottom_line)
            self.bottom_line_func_2.append(bottom_line_func)
        for k in range(len(self.top_line_2)):
            print(self.top_line_2[k], end=" ")
        print()
        for j in range(len(self.heading_dict)):
            print("║ " + getattr(Fore, self.color_for_heading) + self.heading_dict['heading' + f'{j}'][0] + (" " * (
                    self.heading_dict['heading' + f'{j}'][2] - self.heading_dict['heading' + f'{j}'][1] + 1)),
                  sep=" ", end=Fore.WHITE + "║ ")
        print()
        for k in range(len(self.top_line_2)):
            print(Fore.WHITE + self.bottom_line_2[k], end=" ")
        print()

    def items(self, list_of_items):
        item_dict = {}
        all_items = []
        for i in range(self.num_columns):
            item = "item" + f'{i}'
            all_items.append(item)
            item_dict[f'{item}'] = (f'{list_of_items[i]}', len(f'{list_of_items[i]}'))
        for j in range(len(item_dict)):
            print("║ " + item_dict['item' + f'{j}'][0] + (" " * (
                    self.max_for_each_column[j] - item_dict["item" + f'{j}'][1] + 1)), sep=" ",
                  end="║ ")
        print()

    def bottomline(self):
        for k in range(len(self.top_line_2)):
            print(self.bottom_line_func_2[k], end=" ")
        print()