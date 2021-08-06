from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

import re

class OperatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cart = [] #all the prodcut
        self.qty = [] # all the qty of the product in the cart

    def update_purchases(self):
        pcode = self.ids.code_inp.text
        product_container = self.ids.products

        if pcode == '1234':
            details = BoxLayout(size_hint_y=None, height=30, pos_hint={'top': 1})
            product_container.add_widget(details)

            code = Label(text=pcode, size_hint_x=0.25, color=(0.06, 0.45, 0.45, 1))
            name = Label(text='Product One', size_hint_x=0.3, color=(0.06, 0.45, 0.45, 1))
            qty = Label(text='1', size_hint_x=0.1, color=(0.06, 0.45, 0.45, 1))
            disc = Label(text='0.00', size_hint_x=0.1, color=(0.06, 0.45, 0.45, 1))
            price = Label(text='0.00', size_hint_x=0.1, color=(0.06, 0.45, 0.45, 1))
            total = Label(text='0.00', size_hint_x=0.15, color=(0.06, 0.45, 0.45, 1))

            details.add_widget(code)
            details.add_widget(name)
            details.add_widget(qty)
            details.add_widget(disc)
            details.add_widget(price)
            details.add_widget(total)

            # Update preview
            pname = 'Product One'
            pprice = 1.00
            pqty = str(1)
            purchase_total = '`\n\nTotal\t\t\t\t\t\t\t0.00'
            preview = self.ids.receipt_preview
            prev_text = preview.text
            _prev = prev_text.find('`')
            if _prev > 0:
                prev_text = prev_text[:_prev]

            ptarget = -1
            for i,c in enumerate(self.cart):
                if c == pcode:
                    ptarget = i

            if ptarget >= 0:
                pqty = self.qty[ptarget]+1
                self.qty[ptarget] = pqty
                expr = '%s\t\tx\d\t'%(pname) #expression for regular expression, the product we are going to place in here
                rexpr = pname+'\t\tx'+str(pqty)+'\t'
                nu_text = re.sub(expr,rexpr,prev_text)
                preview.text = nu_text

            else:
                self.cart.append(pcode)
                self.qty.append(1)
                nu_preview = '\n'.join([prev_text,pname+'\t\tx'+pqty+'\t\t'+str(pprice),purchase_total])
                preview.text = nu_preview


class MainoperatorApp(App):
    def build(self):
        return OperatorWindow()


if __name__ == "__main__":
    oa = MainoperatorApp()
    oa.run()
