import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime
import random


class WordLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("单词学习管理系统")
        self.root.geometry("1000x700")

        # 数据存储
        self.new_words = []  # 新学单词
        self.review_words = []  # 复习单词
        self.cut_words = []  # 斩的单词
        self.current_review_index = 0
        self.current_cut_index = 0

        # 文件路径
        self.data_file = "word_data.json"

        # 加载数据
        self.load_data()

        # 创建主框架
        self.create_widgets()

    def create_widgets(self):
        """创建界面组件"""
        # 创建Notebook（标签页）
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # 新学区域
        self.new_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.new_frame, text='新学区域')
        self.create_new_learning_zone()

        # 复习区域
        self.review_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.review_frame, text='复习区域')
        self.create_review_zone()

        # 斩的区域
        self.cut_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.cut_frame, text='斩的区域')
        self.create_cut_zone()

    def create_new_learning_zone(self):
        """创建新学区域界面"""
        # 标题
        title_label = tk.Label(self.new_frame, text="新学单词录入",
                               font=('Arial', 16, 'bold'))
        title_label.pack(pady=20)

        # 单词输入区域
        input_frame = tk.Frame(self.new_frame)
        input_frame.pack(pady=20, padx=20)

        # 英文单词输入
        tk.Label(input_frame, text="英文单词:", font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=10, sticky='w')
        self.word_entry = tk.Entry(input_frame, width=30, font=('Arial', 12))
        self.word_entry.grid(row=0, column=1, padx=5, pady=10)

        # 中文释义输入
        tk.Label(input_frame, text="中文释义:", font=('Arial', 12)).grid(row=1, column=0, padx=5, pady=10, sticky='w')
        self.meaning_entry = tk.Entry(input_frame, width=30, font=('Arial', 12))
        self.meaning_entry.grid(row=1, column=1, padx=5, pady=10)

        # 添加按钮
        add_button = tk.Button(self.new_frame, text="添加到复习区域",
                               command=self.add_to_review,
                               font=('Arial', 12), bg='lightblue',
                               width=20, height=2)
        add_button.pack(pady=20)

        # 添加多个按钮框架
        button_frame = tk.Frame(self.new_frame)
        button_frame.pack(pady=10)

        clear_button = tk.Button(button_frame, text="清空输入",
                                 command=self.clear_input,
                                 font=('Arial', 10), width=15)
        clear_button.grid(row=0, column=0, padx=5)

        show_all_button = tk.Button(button_frame, text="查看所有单词",
                                    command=self.show_all_words,
                                    font=('Arial', 10), width=15)
        show_all_button.grid(row=0, column=1, padx=5)

        # 显示新学单词列表
        list_frame = tk.Frame(self.new_frame)
        list_frame.pack(pady=20, padx=20, fill='both', expand=True)

        tk.Label(list_frame, text="新学单词列表:", font=('Arial', 12, 'bold')).pack(anchor='w')

        # 创建滚动条和列表框
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.new_word_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set,
                                           font=('Arial', 10), height=15)
        self.new_word_listbox.pack(fill='both', expand=True)
        scrollbar.config(command=self.new_word_listbox.yview)

        # 更新显示
        self.update_new_word_list()

    def create_review_zone(self):
        """创建复习区域界面"""
        # 顶部状态栏
        status_frame = tk.Frame(self.review_frame, bg='lightgray')
        status_frame.pack(fill='x', pady=5)

        self.review_status_label = tk.Label(status_frame,
                                            text="0/0",
                                            font=('Arial', 12, 'bold'),
                                            bg='lightgray')
        self.review_status_label.pack(side=tk.RIGHT, padx=10)

        # 单词显示区域
        self.review_display_frame = tk.Frame(self.review_frame, bg='white', height=300)
        self.review_display_frame.pack(fill='both', expand=True, padx=20, pady=20)
        self.review_display_frame.pack_propagate(False)

        # 单词显示
        self.review_word_label = tk.Label(self.review_display_frame,
                                          text="",
                                          font=('Arial', 24, 'bold'),
                                          bg='white')
        self.review_word_label.pack(pady=50)

        self.review_meaning_label = tk.Label(self.review_display_frame,
                                             text="",
                                             font=('Arial', 18),
                                             bg='white', fg='gray')
        self.review_meaning_label.pack(pady=20)

        # 按钮区域
        button_frame = tk.Frame(self.review_frame)
        button_frame.pack(pady=20)

        # 显示汉译按钮
        show_meaning_btn = tk.Button(button_frame, text="显示汉译",
                                     command=self.show_meaning,
                                     font=('Arial', 12), width=15, height=2,
                                     bg='lightgreen')
        show_meaning_btn.grid(row=0, column=0, padx=5, pady=5)

        # 跳过按钮
        skip_btn = tk.Button(button_frame, text="跳过",
                             command=self.skip_word,
                             font=('Arial', 12), width=15, height=2,
                             bg='lightyellow')
        skip_btn.grid(row=0, column=1, padx=5, pady=5)

        # 斩的按钮
        cut_btn = tk.Button(button_frame, text="斩",
                            command=self.cut_word,
                            font=('Arial', 12), width=15, height=2,
                            bg='lightcoral')
        cut_btn.grid(row=0, column=2, padx=5, pady=5)

        # 不会按钮
        dont_know_btn = tk.Button(button_frame, text="不会",
                                  command=self.dont_know_word,
                                  font=('Arial', 12), width=15, height=2,
                                  bg='orange')
        dont_know_btn.grid(row=1, column=1, padx=5, pady=5)

        # 开始复习按钮
        start_review_btn = tk.Button(self.review_frame, text="开始复习",
                                     command=self.start_review,
                                     font=('Arial', 12), bg='lightblue',
                                     width=20, height=2)
        start_review_btn.pack(pady=10)

        # 复习统计
        stats_frame = tk.Frame(self.review_frame)
        stats_frame.pack(pady=10)

        tk.Label(stats_frame, text=f"总复习单词数: {len(self.review_words)}",
                 font=('Arial', 10)).pack(side=tk.LEFT, padx=10)

    def create_cut_zone(self):
        """创建斩的区域界面"""
        # 顶部状态栏
        status_frame = tk.Frame(self.cut_frame, bg='lightgray')
        status_frame.pack(fill='x', pady=5)

        self.cut_status_label = tk.Label(status_frame,
                                         text="0/0",
                                         font=('Arial', 12, 'bold'),
                                         bg='lightgray')
        self.cut_status_label.pack(side=tk.RIGHT, padx=10)

        # 单词显示区域
        self.cut_display_frame = tk.Frame(self.cut_frame, bg='white', height=300)
        self.cut_display_frame.pack(fill='both', expand=True, padx=20, pady=20)
        self.cut_display_frame.pack_propagate(False)

        # 单词显示
        self.cut_word_label = tk.Label(self.cut_display_frame,
                                       text="",
                                       font=('Arial', 24, 'bold'),
                                       bg='white')
        self.cut_word_label.pack(pady=50)

        self.cut_meaning_label = tk.Label(self.cut_display_frame,
                                          text="",
                                          font=('Arial', 18),
                                          bg='white', fg='gray')
        self.cut_meaning_label.pack(pady=20)

        # 按钮区域
        button_frame = tk.Frame(self.cut_frame)
        button_frame.pack(pady=20)

        # 显示汉译按钮
        cut_show_meaning_btn = tk.Button(button_frame, text="显示汉译",
                                         command=self.show_cut_meaning,
                                         font=('Arial', 12), width=15, height=2,
                                         bg='lightgreen')
        cut_show_meaning_btn.grid(row=0, column=0, padx=5, pady=5)

        # 跳过按钮
        cut_skip_btn = tk.Button(button_frame, text="跳过",
                                 command=self.skip_cut_word,
                                 font=('Arial', 12), width=15, height=2,
                                 bg='lightyellow')
        cut_skip_btn.grid(row=0, column=1, padx=5, pady=5)

        # 恢复复习按钮（从斩的区域移除）
        restore_btn = tk.Button(button_frame, text="恢复复习",
                                command=self.restore_word,
                                font=('Arial', 12), width=15, height=2,
                                bg='lightblue')
        restore_btn.grid(row=0, column=2, padx=5, pady=5)

        # 开始复习按钮
        start_cut_review_btn = tk.Button(self.cut_frame, text="开始复习斩的单词",
                                         command=self.start_cut_review,
                                         font=('Arial', 12), bg='lightblue',
                                         width=20, height=2)
        start_cut_review_btn.pack(pady=10)

        # 斩的单词统计
        stats_frame = tk.Frame(self.cut_frame)
        stats_frame.pack(pady=10)

        tk.Label(stats_frame, text=f"斩的单词总数: {len(self.cut_words)}",
                 font=('Arial', 10)).pack(side=tk.LEFT, padx=10)

    def add_to_review(self):
        """添加新单词到复习区域"""
        word = self.word_entry.get().strip()
        meaning = self.meaning_entry.get().strip()

        if not word or not meaning:
            messagebox.showwarning("输入错误", "请填写完整的单词和释义！")
            return

        # 创建新单词对象
        new_word = {
            'word': word,
            'meaning': meaning,
            'weight': 0,  # 初始权重
            'dont_know_count': 0,  # 不会次数
            'added_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'last_reviewed': None
        }

        # 添加到复习列表
        self.review_words.append(new_word)
        self.save_data()

        # 清空输入框
        self.clear_input()

        # 更新显示
        self.update_new_word_list()

        messagebox.showinfo("成功", f"已添加单词: {word}")

    def clear_input(self):
        """清空输入框"""
        self.word_entry.delete(0, tk.END)
        self.meaning_entry.delete(0, tk.END)

    def update_new_word_list(self):
        """更新新单词列表显示"""
        self.new_word_listbox.delete(0, tk.END)
        for word in self.review_words[-20:]:  # 显示最近20个
            self.new_word_listbox.insert(tk.END, f"{word['word']} - {word['meaning']}")

    def show_all_words(self):
        """显示所有单词"""
        if not self.review_words and not self.cut_words:
            messagebox.showinfo("单词列表", "还没有添加任何单词！")
            return

        all_words_window = tk.Toplevel(self.root)
        all_words_window.title("所有单词列表")
        all_words_window.geometry("600x400")

        # 创建Notebook
        notebook = ttk.Notebook(all_words_window)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # 复习单词标签页
        review_tab = ttk.Frame(notebook)
        notebook.add(review_tab, text=f"复习单词 ({len(self.review_words)})")

        review_listbox = tk.Listbox(review_tab, font=('Arial', 10))
        review_scrollbar = tk.Scrollbar(review_tab)
        review_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        review_listbox.pack(fill='both', expand=True)
        review_scrollbar.config(command=review_listbox.yview)
        review_listbox.config(yscrollcommand=review_scrollbar.set)

        for word in self.review_words:
            review_listbox.insert(tk.END,
                                  f"{word['word']:20} - {word['meaning']:20} "
                                  f"(权重: {word['weight']}, 不会次数: {word['dont_know_count']})")

        # 斩的单词标签页
        cut_tab = ttk.Frame(notebook)
        notebook.add(cut_tab, text=f"斩的单词 ({len(self.cut_words)})")

        cut_listbox = tk.Listbox(cut_tab, font=('Arial', 10))
        cut_scrollbar = tk.Scrollbar(cut_tab)
        cut_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        cut_listbox.pack(fill='both', expand=True)
        cut_scrollbar.config(command=cut_listbox.yview)
        cut_listbox.config(yscrollcommand=cut_scrollbar.set)

        for word in self.cut_words:
            cut_listbox.insert(tk.END,
                               f"{word['word']:20} - {word['meaning']:20} "
                               f"(斩的时间: {word.get('cut_date', '未知')})")

    def start_review(self):
        """开始复习"""
        if not self.review_words:
            messagebox.showinfo("提示", "没有需要复习的单词！")
            return

        # 按权重排序（不会次数多的优先）
        self.review_words.sort(key=lambda x: (-x['weight'], x.get('dont_know_count', 0)))

        self.current_review_index = 0
        self.show_next_review_word()

    def show_next_review_word(self):
        """显示下一个复习单词"""
        if self.current_review_index >= len(self.review_words):
            messagebox.showinfo("完成", "本次复习已完成！")
            self.review_word_label.config(text="")
            self.review_meaning_label.config(text="")
            self.review_status_label.config(text="0/0")
            return

        current_word = self.review_words[self.current_review_index]
        self.review_word_label.config(text=current_word['word'])
        self.review_meaning_label.config(text="???")

        # 更新状态
        self.review_status_label.config(
            text=f"{self.current_review_index + 1}/{len(self.review_words)}"
        )

    def show_meaning(self):
        """显示汉译"""
        if self.current_review_index < len(self.review_words):
            current_word = self.review_words[self.current_review_index]
            self.review_meaning_label.config(text=current_word['meaning'])

    def skip_word(self):
        """跳过当前单词"""
        if self.current_review_index < len(self.review_words):
            # 标记为已复习
            current_word = self.review_words[self.current_review_index]
            current_word['last_reviewed'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            self.current_review_index += 1
            self.show_next_review_word()

    def dont_know_word(self):
        """标记为不会"""
        if self.current_review_index < len(self.review_words):
            current_word = self.review_words[self.current_review_index]

            # 增加权重和不会次数
            current_word['weight'] += 1
            current_word['dont_know_count'] = current_word.get('dont_know_count', 0) + 1
            current_word['last_reviewed'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # 显示汉译
            self.review_meaning_label.config(text=current_word['meaning'])

            # 等待用户查看后自动下一个
            self.root.after(2000, self.auto_next_after_dont_know)

    def auto_next_after_dont_know(self):
        """不会之后自动下一个"""
        self.current_review_index += 1
        self.save_data()  # 保存数据
        self.show_next_review_word()

    def cut_word(self):
        """斩的单词（移到斩的区域）"""
        if self.current_review_index < len(self.review_words):
            current_word = self.review_words[self.current_review_index]

            # 添加斩的时间
            current_word['cut_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            current_word['weight'] = -100  # 设为最低权重

            # 从复习列表移除，添加到斩的列表
            self.review_words.pop(self.current_review_index)
            self.cut_words.append(current_word)

            self.save_data()

            # 如果还有单词，显示下一个
            if self.current_review_index < len(self.review_words):
                self.show_next_review_word()
            else:
                messagebox.showinfo("完成", "单词已斩，本次复习已完成！")
                self.review_word_label.config(text="")
                self.review_meaning_label.config(text="")
                self.review_status_label.config(text="0/0")

    def start_cut_review(self):
        """开始复习斩的单词"""
        if not self.cut_words:
            messagebox.showinfo("提示", "没有需要复习的斩的单词！")
            return

        # 按斩的时间排序（越早斩的权重越高）
        self.cut_words.sort(key=lambda x: x.get('cut_date', '2000-01-01'))

        self.current_cut_index = 0
        self.show_next_cut_word()

    def show_next_cut_word(self):
        """显示下一个斩的单词"""
        if self.current_cut_index >= len(self.cut_words):
            messagebox.showinfo("完成", "斩的单词复习已完成！")
            self.cut_word_label.config(text="")
            self.cut_meaning_label.config(text="")
            self.cut_status_label.config(text="0/0")
            return

        current_word = self.cut_words[self.current_cut_index]
        self.cut_word_label.config(text=current_word['word'])
        self.cut_meaning_label.config(text="???")

        # 更新状态
        self.cut_status_label.config(
            text=f"{self.current_cut_index + 1}/{len(self.cut_words)}"
        )

    def show_cut_meaning(self):
        """显示斩的单词的汉译"""
        if self.current_cut_index < len(self.cut_words):
            current_word = self.cut_words[self.current_cut_index]
            self.cut_meaning_label.config(text=current_word['meaning'])

    def skip_cut_word(self):
        """跳过当前斩的单词"""
        if self.current_cut_index < len(self.cut_words):
            self.current_cut_index += 1
            self.show_next_cut_word()

    def restore_word(self):
        """从斩的区域恢复到复习区域"""
        if self.current_cut_index < len(self.cut_words):
            current_word = self.cut_words[self.current_cut_index]

            # 恢复权重
            current_word['weight'] = 0
            if 'cut_date' in current_word:
                del current_word['cut_date']

            # 移回复习列表
            self.cut_words.pop(self.current_cut_index)
            self.review_words.append(current_word)

            self.save_data()

            # 显示下一个
            if self.current_cut_index < len(self.cut_words):
                self.show_next_cut_word()
            else:
                messagebox.showinfo("完成", "单词已恢复，本次复习已完成！")
                self.cut_word_label.config(text="")
                self.cut_meaning_label.config(text="")
                self.cut_status_label.config(text="0/0")

    def save_data(self):
        """保存数据到文件"""
        data = {
            'review_words': self.review_words,
            'cut_words': self.cut_words,
            'last_saved': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存数据时出错: {e}")

    def load_data(self):
        """从文件加载数据"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.review_words = data.get('review_words', [])
                    self.cut_words = data.get('cut_words', [])
            except Exception as e:
                print(f"加载数据时出错: {e}")
                # 使用默认数据
                self.review_words = []
                self.cut_words = []


def main():
    root = tk.Tk()
    app = WordLearningApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()