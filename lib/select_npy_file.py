import tkinter.filedialog


def SelectNpyFile(init_dir):
    select_file_path = tkinter.filedialog.askopenfilename(
        filetypes=[
            ("バイナリファイル", "*.npy"),
        ],
        title="select sampling data",
        initialdir=init_dir,
        multiple=False,
    )
    return select_file_path
