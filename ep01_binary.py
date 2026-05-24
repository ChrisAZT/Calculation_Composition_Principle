# ep01_binary.py
from manim import *
import random

# 全局配置参数
CONFIG = {
    "font": "SimHei",
    "color_opcode": RED_C,
    "color_operand": BLUE_C,
    "color_crystal": TEAL_C,
}

class CompArchEp1(Scene):
    def construct(self):
        # 镜头流转序列
        self.scene_01_question()
        self.scene_02_binary_concept()
        self.scene_03_instruction_demo()
        self.scene_04_applications()
        self.scene_05_crystal_logic()
        self.scene_06_next_episode()

    def scene_01_question(self):
        """S01: 提出问题 (0-8s)"""
        # [图形块] 键盘按键与手
        key_rect = RoundedRectangle(width=2, height=1.5, corner_radius=0.2, color=WHITE).shift(LEFT * 3)
        key_text = Text("Enter", font=CONFIG["font"], font_size=36).move_to(key_rect)
        key_group = VGroup(key_rect, key_text)

        hand = Polygon(
            ORIGIN, RIGHT*0.5+UP*1, RIGHT*1+UP*0.8, RIGHT*0.2+DOWN*0.5,
            color=GRAY, fill_opacity=0.5
        ).next_to(key_rect, UP+RIGHT, buff=0.1)

        # [图形块] CPU芯片 - 往里收缩，缩小尺寸
        cpu_rect = Square(side_length=2.2, color=GRAY_B, fill_opacity=0.2).shift(RIGHT * 3)
        cpu_inner = Square(side_length=1.2, color=GRAY_C, fill_opacity=0.5).move_to(cpu_rect)
        cpu_text = Text("CPU", font=CONFIG["font"], font_size=36).move_to(cpu_rect)
        cpu_group = VGroup(cpu_rect, cpu_inner, cpu_text)
        question_mark = Text("?", font=CONFIG["font"], font_size=60, color=YELLOW).next_to(cpu_rect, UP)

        # [动画块] 入场与动作传导
        self.play(FadeIn(key_group), FadeIn(cpu_group), run_time=2)
        self.play(hand.animate.shift(DOWN*0.5 + LEFT*0.5), run_time=0.5)

        ripple = Circle(radius=1.5, color=YELLOW).move_to(key_rect)
        beam = Line(key_rect.get_right(), cpu_rect.get_left(), color=YELLOW, stroke_width=6)

        self.play(Create(ripple), ripple.animate.scale(1.5).set_opacity(0), run_time=0.5)
        self.play(Create(beam), run_time=1)
        self.play(Write(question_mark), run_time=1)

        self.wait(1.5)

        self.play(
            FadeOut(key_group), FadeOut(hand), FadeOut(beam), FadeOut(question_mark),
            cpu_group.animate.scale(15).set_opacity(0), # CPU放大并最终透明
            run_time=1.5
        )
        self.clear() # 💥 核心修复：清理第一镜所有残留对象，打扫战场！

    def scene_02_binary_concept(self):
        """S02: 基础概念 (8-25s)"""
        action_text = Text("动 作", font=CONFIG["font"], font_size=60, color=WHITE).move_to(ORIGIN)

        self.play(FadeIn(action_text), run_time=1)
        self.wait(3)


        binary_matrix = VGroup()
        for i in range(8):
            row_str = "".join([str(random.choice([0,1])) for _ in range(16)])
            # 禁用微调以提高生成速度
            row = Text(row_str, font="Monospace", font_size=36, color=GREEN_C, disable_ligatures=True)
            binary_matrix.add(row)
        binary_matrix.arrange(DOWN, buff=0.2).move_to(ORIGIN)

        self.play(Transform(action_text, binary_matrix), run_time=2)
        self.wait(8)


        self.play(
            binary_matrix.animate.shift(LEFT * 15).set_opacity(0),
            run_time=2
        )
        self.clear() # 💥 核心修复：清空 S02

    def scene_03_instruction_demo(self):
        """S03: 举例演示 (25-55s)"""
        # [公式块] 算式 7 + 5，位置固定在上方
        eq = MathTex("7", "+", "5", font_size=96).move_to(UP * 2)

        self.play(Write(eq), run_time=2)
        self.wait(3)

        # [图形块] 机器指令区块
        opcode_box = Rectangle(width=2, height=1.2, color=CONFIG["color_opcode"], fill_opacity=0.8)
        opcode_text = Text("操作码", font=CONFIG["font"], font_size=24).move_to(opcode_box)
        opcode_group = VGroup(opcode_box, opcode_text)

        operand_box1 = Rectangle(width=1.5, height=1.2, color=CONFIG["color_operand"], fill_opacity=0.8)
        operand_text1 = Text("操作数(7)", font=CONFIG["font"], font_size=18).move_to(operand_box1)
        op_group1 = VGroup(operand_box1, operand_text1)

        operand_box2 = Rectangle(width=1.5, height=1.2, color=CONFIG["color_operand"], fill_opacity=0.8)
        operand_text2 = Text("操作数(5)", font=CONFIG["font"], font_size=18).move_to(operand_box2)
        op_group2 = VGroup(operand_box2, operand_text2)

        # 掉落到屏幕下方，绝不会溢出
        opcode_group.move_to(DOWN * 1.5 + LEFT * 1.5)
        self.play(
            eq[1].animate.move_to(opcode_group.get_center()).set_opacity(0),
            FadeIn(opcode_group),
            run_time=2
        )
        self.wait(2)

        op_group1.next_to(opcode_group, RIGHT, buff=0)
        op_group2.next_to(op_group1, RIGHT, buff=0)

        self.play(
            eq[0].animate.move_to(op_group1.get_center()).set_opacity(0),
            FadeIn(op_group1),
            eq[2].animate.move_to(op_group2.get_center()).set_opacity(0),
            FadeIn(op_group2),
            run_time=2
        )

        instruction_bar = VGroup(opcode_group, op_group1, op_group2)
        outline = Rectangle(width=instruction_bar.width, height=instruction_bar.height, color=WHITE).move_to(instruction_bar)

        self.play(Create(outline), run_time=1)
        self.wait(14)

        self.instruction_bar = VGroup(instruction_bar, outline)
        self.play(
            self.instruction_bar.animate.scale(0.3).move_to(ORIGIN),
            FadeOut(eq), # 清理头顶的算式残骸
            run_time=4
        )
        # 不调用 self.clear()，因为我们需要把 instruction_bar 传给下一镜

    def scene_04_applications(self):
        """S04: 实际应用 (55-85s)"""
        waterfall = VGroup()
        for i in range(12):
            line_str = "".join([str(random.choice([0,1])) for _ in range(35)])
            line = Text(line_str, font="Monospace", font_size=20, color=GREEN, disable_ligatures=True)
            waterfall.add(line)
        waterfall.arrange(DOWN, buff=0.15).move_to(ORIGIN)

        self.play(Transform(self.instruction_bar, waterfall), run_time=3)
        self.wait(4)

        # [图形块] 三个分类图标 - 坐标修正，统一缩小 0.7 倍防溢出
        icon_exe = VGroup(Square(fill_color=GRAY, fill_opacity=0.8), Text(".exe", font="Monospace", font_size=36)).scale(0.7).move_to(LEFT * 4)
        icon_jpg = VGroup(Square(fill_color=BLUE_E, fill_opacity=0.8), Circle(radius=0.3, color=YELLOW, fill_opacity=1).shift(UP*0.2+RIGHT*0.2), Polygon(LEFT*0.8+DOWN*0.8, RIGHT*0.8+DOWN*0.8, ORIGIN, color=GREEN_E, fill_opacity=1)).scale(0.7).move_to(ORIGIN)
        icon_mp4 = VGroup(Rectangle(width=2.5, height=1.5, fill_color=BLACK, fill_opacity=0.8, stroke_color=WHITE), Polygon(UP*0.3+LEFT*0.2, DOWN*0.3+LEFT*0.2, RIGHT*0.3, color=WHITE, fill_opacity=1)).scale(0.7).move_to(RIGHT * 4)

        self.play(
            FadeIn(icon_exe, shift=DOWN),
            FadeIn(icon_jpg, shift=DOWN),
            FadeIn(icon_mp4, shift=DOWN),
            waterfall.animate.set_opacity(0.15),
            run_time=3
        )
        self.wait(15)

        self.icons = VGroup(icon_exe, icon_jpg, icon_mp4)
        self.bg_waterfall = waterfall # 留给 S05

    def scene_05_crystal_logic(self):
        """S05: 升华总结 (85-100s)"""
        # [图形块] 发光晶体
        crystal = RegularPolygon(n=6, color=CONFIG["color_crystal"], stroke_width=4, fill_opacity=0.1)
        crystal.scale(2).move_to(ORIGIN)

        inner_lines = VGroup(
            Line(crystal.get_vertices()[0], crystal.get_vertices()[3]),
            Line(crystal.get_vertices()[1], crystal.get_vertices()[4]),
            Line(crystal.get_vertices()[2], crystal.get_vertices()[5]),
        ).set_color(CONFIG["color_crystal"]).set_opacity(0.5)

        crystal_group = VGroup(crystal, inner_lines)

        self.play(
            ReplacementTransform(self.bg_waterfall, crystal_group),
            FadeOut(self.icons), # 彻底删除图标残留
            run_time=2.5
        )

        self.play(crystal_group.animate.scale(1.1).set_opacity(0.8), rate_func=there_and_back, run_time=2)
        self.play(crystal_group.animate.scale(1.1).set_opacity(0.8), rate_func=there_and_back, run_time=2)

        self.wait(7.5)

        self.crystal = crystal_group

    def scene_06_next_episode(self):
        """S06: 下一期预告 (100-105s)"""
        # [图形/文本块] 冯诺依曼三要素，调整安全距离
        box_cpu = Rectangle(width=2, height=1.2, color=BLUE).move_to(UP * 1.5)
        box_mem = Rectangle(width=2, height=1.2, color=GREEN).move_to(DOWN * 1 + LEFT * 2.5)
        box_io = Rectangle(width=2, height=1.2, color=YELLOW).move_to(DOWN * 1 + RIGHT * 2.5)

        t_cpu = Text("CPU", font=CONFIG["font"], font_size=36).move_to(box_cpu)
        t_mem = Text("内存", font=CONFIG["font"], font_size=36).move_to(box_mem)
        t_io = Text("I/O", font=CONFIG["font"], font_size=36).move_to(box_io)

        module_group = VGroup(box_cpu, box_mem, box_io, t_cpu, t_mem, t_io)

        l1 = Line(box_cpu.get_bottom(), box_mem.get_top(), color=WHITE)
        l2 = Line(box_cpu.get_bottom(), box_io.get_top(), color=WHITE)
        lines = VGroup(l1, l2)

        # 调整标题位置，防止溢出下边缘
        title = Text("下期预告：冯·诺依曼结构", font=CONFIG["font"], font_size=42, color=YELLOW).move_to(DOWN * 3.2)

        # ⚠️ 修复转场：用 ReplacementTransform 平滑切除旧晶体
        self.play(ReplacementTransform(self.crystal, module_group), run_time=1.5)
        self.play(Create(lines), run_time=1)
        self.play(Write(title), run_time=1)

        self.wait(5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1) # 最终切黑