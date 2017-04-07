
"""
"""

# Native
import array
import os



class Decryption(object):
    """
    """

    magic_bytes = [70, 67, 90]
    # :ByteArray;
    var_11 = None
    # :uint;
    var_12 = 0
    # :uint;
    var_14 = 0
    # :uint;
    bytes_length = 0
    # :uint;
    var_16 = 0

    byte_array = None

    def __init__(self, byte_array):
        """
        """

        self.byte_array = byte_array
        self.byte_array_length = len(self.byte_array)

    def method_11(self): #void
        """
        """

        if self.var_11:
            self.var_11.clear()

        if self.byte_array:
            self.byte_array.clear()

        self.magic_bytes = None
        self.var_11 = None
        self.byte_array = None

        return None

    def decrypt(self): #ByteArray
        """
        """

        if self.method_14():
            return self.byte_array

        self.var_12 = self.method_15()
        self.var_16 = self.method_13()
        self.var_14 = 0

        while self.var_14 < self.var_12:

            _loc1_ = self.var_14
            _loc2_ = self.byte_array[_loc1_] ^ self.var_16

            self.byte_array[_loc1_] = _loc2_
            self.var_14 = self.var_14 + 1

        return self.byte_array[0:self.byte_array_length - 4]

    def method_13(self):# int
        """
        """

        self.var_16 = self.var_12

        while self.var_16 > 255:
            self.var_16 = self.var_16 >> 1

        return self.var_16

    def method_14(self):# Boolean
        """
        This pretty much just checks if the byte array has already been decrypted
        """

        if self.byte_array[2] != 83:
            return False

        if self.byte_array[1] != 87:
            return False

        first = self.byte_array[0]

        return self.magic_bytes.indexOf(first) >= 0

    def method_15(self): #unit
        """
        """

        return self.byte_array[self.byte_array_length - 1] << 24 | self.byte_array[self.byte_array_length - 2] << 16 | self.byte_array[self.byte_array_length - 3] << 8 | self.byte_array[self.byte_array_length - 4]




if __name__ == '__main__':

    source = array.array('B')

    path = 'Main.swf'

    size = os.path.getsize(path)
    # Expects Main.swf to be in the same dir as you are calling this script
    with open(path, mode='rb') as fd:
        source.fromfile(fd, size)

    decryption = Decryption(source)
    decrypted = decryption.decrypt()

    with open('Main.decrypted.swf', mode='wb+') as fd:
        fd.write(bytearray(decrypted))
