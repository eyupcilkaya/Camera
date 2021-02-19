
class Variables():

    def __init__(self):
        print("...Initializing Camera Datas")
        self._img = ''
        self._relay_state = ""

    def get_cam_data(self):
        return self._img

    def set_cam_data(self, img):
        self._img = img

    def clear_cam_data(self):
        pass

    def cam_data_lenght(self):
        pass

    def get_relay_val(self):
        return self._relay_state

    def set_relay_val(self, state_val):
        self._relay_state = state_val