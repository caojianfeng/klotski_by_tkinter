#!/usr/bin/env python3

# http://effbot.org/tkinterbook/grid.htm

import tkinter as tk

wall_size = 12
cell_size = 50


def create_map(window):
    # 边墙
    frame = tk.Frame(window, bg='grey')
    frame.pack(fill='both', expand=True)

    # 出口
    frame_exit = tk.Frame(frame,
                          width=2*cell_size,
                          height=wall_size,
                          bg='#99ff33')
    frame_exit.pack(side='bottom')

    # 内部道路
    frame_center = tk.Frame(frame, width=4*cell_size,
                            height=5*cell_size, bg='white')
    frame_center.pack(side='bottom',
                      padx=wall_size)
    return frame_center


def create_block(root, text, color, width, height, row, column):
    block = tk.LabelFrame(root, width=cell_size*width,
                          height=cell_size*height,
                          text=text, bg=color)
    block.grid(row=row,
               column=column,
               sticky="news",
               columnspan=width,
               rowspan=height
               )
    return block


def create_blocks(frame_center):

    block_ma = create_block(frame_center,
                            text="张飞", color='#3399ff',
                            width=1, height=2,
                            row=0, column=0)

    block_cao = create_block(frame_center,
                             text="曹操", color='#ff9933',
                             width=2, height=2,
                             row=0, column=1)

    block_ma = create_block(frame_center,
                            text="马超", color='#3399ff',
                            width=1, height=2,
                            row=0, column=3)

    block_huang = create_block(frame_center,
                               text="黄忠", color='#3399ff',
                               width=1, height=2,
                               row=2, column=0)

    block_guan = create_block(frame_center,
                              text="关羽", color='#33ff99',
                              width=2, height=1,
                              row=2, column=1)

    block_zhao = create_block(frame_center,
                              text="赵云", color='#3399ff',
                              width=1, height=2,
                              row=2, column=3)

    block_zu1 = create_block(frame_center,
                             text="卒", color='#9999ff',
                             width=1, height=1,
                             row=4, column=0)

    block_zu2 = create_block(frame_center,
                             text="卒", color='#9999ff',
                             width=1, height=1,
                             row=3, column=1)

    block_zu3 = create_block(frame_center,
                             text="卒", color='#9999ff',
                             width=1, height=1,
                             row=3, column=2)

    block_zu4 = create_block(frame_center,
                             text="卒", color='#9999ff',
                             width=1, height=1,
                             row=4, column=3)


def main():
    window = tk.Tk()
    window.title('KLOTSKI_华容道')
    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()
    ww = 4*cell_size+2*wall_size
    wh = 5*cell_size+2*wall_size
    window.geometry(f'{ww}x{wh}-{int((sw-ww)/2)}-{int((sh-wh)/2)}')

    frame_center = create_map(window)
    create_blocks(frame_center)

    window.mainloop()


if __name__ == "__main__":
    main()
