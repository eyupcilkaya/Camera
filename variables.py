class Variables:

    def __init__(self):
        print("...Initializing Camera Datas")
        self._img = ''
        self._relay_state = ""
        self.__t1 = ""
        self.__t2 = ""
        self.__p = ""

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

    def set_sensor_val(self, t1, t2, p):
        self.__t1 = t1
        self.__t2 = t2
        self.__p = p

    def get_sensor_val(self):
        return self.__t1, self.__t2, self.__p
