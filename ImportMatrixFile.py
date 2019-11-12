def import_matrix_file(series_number, file_path):
    import access2thematrix

    # import tkinter as tk
    # from tkinter.filedialog import askopenfilename

    # root = tk.Tk()
    # root.withdraw()  # prevents the default window  to open.
    # file_path = (askopenfilename())  # show an "Open" dialog box and return the path to the selected file

    mtrx_data = access2thematrix.MtrxData()
    traces, message = mtrx_data.open(file_path)
    im, _ = mtrx_data.select_image(traces[series_number])
    image = im.data

    # dict = {0: "up forward", 1: "up retrace", 2: "down forward", 3: "down retrace"}
    print("Image has been uploaded to variables image and im")

    return image, im
