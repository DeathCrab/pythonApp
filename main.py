from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import numpy as np


class UncertaintyApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical')

        self.root.add_widget(Label(text='Type A Uncertainty'))
        self.num_measurements_input = TextInput(hint_text='Enter number of measurements', multiline=False)
        self.root.add_widget(self.num_measurements_input)
        self.measurements_input = TextInput(hint_text='Enter measurements separated by commas', multiline=False)
        self.root.add_widget(self.measurements_input)

        self.root.add_widget(Label(text='Type B Uncertainty'))
        self.num_parameters_input = TextInput(hint_text='Enter number of parameters', multiline=False)
        self.root.add_widget(self.num_parameters_input)
        self.uncertainties_input = TextInput(hint_text='Enter uncertainties separated by commas', multiline=False)
        self.root.add_widget(self.uncertainties_input)

        self.calculate_button = Button(text='Calculate Uncertainty')
        self.calculate_button.bind(on_press=self.calculate_uncertainty)
        self.root.add_widget(self.calculate_button)

        self.result_label = Label(text='')
        self.root.add_widget(self.result_label)

        return self.root

    def calculate_uncertainty(self, instance):
        try:
            num_measurements = int(self.num_measurements_input.text)
            measurements = list(map(float, self.measurements_input.text.split(',')))
            avg = np.mean(measurements)
            std_dev = np.std(measurements, ddof=1)

            num_parameters = int(self.num_parameters_input.text)
            uncertainties = list(map(float, self.uncertainties_input.text.split(',')))
            type_b_uncertainty = np.sqrt(np.sum(np.array(uncertainties) ** 2))

            total_uncertainty = np.sqrt(std_dev ** 2 + type_b_uncertainty ** 2)

            self.result_label.text = f"Total uncertainty: {total_uncertainty}"
        except Exception as e:
            self.result_label.text = f"Error: {str(e)}"


if __name__ == '__main__':
    UncertaintyApp().run()
