#!/usr/bin/env python3
# coding=utf-8
# title          :rules.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/11/30 下午8:52
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script


class Rule:
    """
    所有规则基类
    """
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True


class HeadingRule(Rule):
    """
    标题一行，70字符，不以:结尾
    """
    type = "heading"

    def condition(self, block):
        return '\n' not in block and len(block) <= 70 and not block[-1] == ":"


class TitleRule(HeadingRule):
    """
    文档第一个块，且是大标题
    """
    type = "title"
    first = True

    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadingRule.condition(self, block)


class ListItemRule(Rule):
    """
    列表项以连字符串开始，格式化时需要移除。
    """
    type = "listitem"

    def condition(self, block):
        return block[0] == "-"

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True


class ListRule(ListItemRule):
    """
    从非列表项开始，在最后一个连续的列表项后结束
    """
    type = "list"
    inside = False

    def condition(self, block):
        return True

    def action(self, block, handler):
        # 未处理列表时inside为False，且ListItemRule.condition返回非空值
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
        # 处理列表时inside为True，ListIteimRule.condition返回非空值
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False


class ParagraphRule(Rule):
    """
    段落是其他规则没应用的块。
    """
    type = "paragraph"

    def condition(self, block):
        return True
