""" Exporter Program"""

class Exporter(object):
    """ Class Exporter """

    def __init__(self, dataset):
        self.dataset = dataset


class BaseTextExporter(Exporter):
    """docstring for BaseTextExporter"""
    def __init__(self, dataset):
        super(BaseTextExporter, self).__init__(dataset)

    def __str__(self):
        # For instance
        return self.metadata_to_text() + "\n" + self.data_to_text()

    def metadata_to_text(self):
        """This writes the metadata to a given file"""
        return "Meta data text"


    def data_to_text(self):
        """ This writes the data to a given file """
        return "data text"

    def get_whole_text(self):
        return self.metadata_to_text() + "\n" + self.data_to_text()

    def write_to_file(self, file_handler, *args, **kwargs):
        file_handler.write(self.get_whole_text(), *args, **kwargs)

class BasePlotExporter(Exporter):
    """docstring for BasePlotExporter"""
    def __init__(self, dataset):
        super(BasePlotExporter, self).__init__(dataset)

    def plot(self, axis, *args, **kwargs):
        # Cases for error bars and labels
        axis.plot(self.dataset.x, self.dataset.y, *args, **kwargs)
