import ast


class FormatterEngine(ast.NodeVisitor):

    def __init__(self, indent_size=4):
        self.indent_size = indent_size
        self.level = 0
        self.lines = []


    def format(self, tree):

        self.lines = []
        self.level = 0

        self.visit(tree)

        return "\n".join(self.lines)


    def write(self, text):

        indent = " " * (
            self.level * self.indent_size
        )

        self.lines.append(
            indent + text
        )


    # -------------------------
    # MODULE
    # -------------------------

    def visit_Module(self, node):

        for item in node.body:
            self.visit(item)


    # -------------------------
    # CLASS
    # -------------------------

    def visit_ClassDef(self, node):

        if node.bases:

            bases = ", ".join(
                ast.unparse(base)
                for base in node.bases
            )

            header = f"class {node.name}({bases}):"

        else:

            header = f"class {node.name}:"


        self.write(header)

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1


    # -------------------------
    # FUNCTION
    # -------------------------

    def visit_FunctionDef(self, node):

    # decorators
        for decorator in node.decorator_list:
            self.write(
                f"@{ast.unparse(decorator)}"
            )

        args = ast.unparse(node.args)

        if node.returns:
            returns = ast.unparse(node.returns)
            signature = f"def {node.name}({args}) -> {returns}:"
        else:
            signature = f"def {node.name}({args}):"

        self.write(signature)

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1

    def visit_AsyncFunctionDef(self, node):

        for decorator in node.decorator_list:
            self.write(
                "@" + ast.unparse(decorator)
            )

        args = ast.unparse(node.args)

        self.write(
            f"async def {node.name}({args}):"
        )

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1
        
    def visit_Await(self, node):

        self.write(
            "await " + ast.unparse(node.value)
        )
    def visit_match_case(self, node):

        pattern = ast.unparse(node.pattern)

        if node.guard:
            self.write(
                f"case {pattern} if {ast.unparse(node.guard)}:"
            )
        else:
            self.write(
                f"case {pattern}:"
            )

        self.level += 1

        for stmt in node.body:
            self.visit(stmt)

        self.level -= 1
        # -------------------------
    # MATCH / CASE
    # -------------------------

    def visit_Match(self, node):

        self.write(
            f"match {ast.unparse(node.subject)}:"
        )

        self.level += 1

        for case in node.cases:
            self.visit(case)

            self.level -= 1   
    
    # RETURN
    # -------------------------

    def visit_Return(self, node):

        if node.value:

            self.write(
                f"return {ast.unparse(node.value)}"
            )

        else:

            self.write("return")

    def visit_Delete(self, node):
        targets = ", ".join(
            ast.unparse(target)
            for target in node.targets
        )

        self.write(f"del {targets}")
        # -------------------------
    # RAISE
    # -------------------------

    def visit_Raise(self, node):

        if node.exc:
            text = f"raise {ast.unparse(node.exc)}"
        else:
            text = "raise"

        if node.cause:
            text += f" from {ast.unparse(node.cause)}"

        self.write(text)
            
            # -------------------------
    # YIELD
    # -------------------------

    def visit_Yield(self, node):

        if node.value:

            self.write(
                f"yield {ast.unparse(node.value)}"
            )

        else:

            self.write(
                "yield"
            )
            
        # -------------------------
    # ASSERT
    # -------------------------

    def visit_Assert(self, node):

        if node.msg:

            self.write(
                f"assert {ast.unparse(node.test)}, {ast.unparse(node.msg)}"
            )

        else:

            self.write(
                f"assert {ast.unparse(node.test)}"
            )
            
            # -------------------------
    # BREAK
    # -------------------------

    def visit_Break(self, node):

        self.write(
            "break"
        )

        # -------------------------
    # GLOBAL
    # -------------------------

    def visit_Global(self, node):

        self.write(
            f"global {', '.join(node.names)}"
        )


    # -------------------------
    # NONLOCAL
    # -------------------------

    def visit_Nonlocal(self, node):

        self.write(
            f"nonlocal {', '.join(node.names)}"
        )
    # -------------------------
    # CONTINUE
    # -------------------------

    def visit_Continue(self, node):

        self.write(
            "continue"
        )
    # -------------------------
    # EXPRESSIONS
    # -------------------------

    def visit_Expr(self, node):

        self.write(
            ast.unparse(node.value)
        )


    # -------------------------
    # IF
    # -------------------------

    def visit_If(self, node):

        self.write(
            f"if {ast.unparse(node.test)}:"
        )

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1


        if node.orelse:

            self.write("else:")

            self.level += 1

            for item in node.orelse:
                self.visit(item)

            self.level -= 1


    # -------------------------
    # FOR
    # -------------------------

    def visit_For(self, node):

        self.write(
            f"for {ast.unparse(node.target)} in {ast.unparse(node.iter)}:"
        )

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1


        # -------------------------
    # ASYNC FOR
    # -------------------------

    def visit_AsyncFor(self, node):

        target = ast.unparse(node.target)
        iterator = ast.unparse(node.iter)

        self.write(
            f"async for {target} in {iterator}:"
        )

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1
    # -------------------------
    # WHILE
    # -------------------------

    def visit_While(self, node):

        self.write(
            f"while {ast.unparse(node.test)}:"
        )

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1


    # -------------------------
    # TRY
    # -------------------------
    def visit_Try(self, node):

        self.write("try:")

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1


        for handler in node.handlers:

            text = f"except {ast.unparse(handler.type)}"

            if handler.name:
                text += f" as {handler.name}"

            text += ":"

            self.write(text)

            self.level += 1

            for item in handler.body:
                self.visit(item)

            self.level -= 1


        if node.orelse:

            self.write("else:")

            self.level += 1

            for item in node.orelse:
                self.visit(item)

            self.level -= 1


        if node.finalbody:

            self.write("finally:")

            self.level += 1

            for item in node.finalbody:
                self.visit(item)

            self.level -= 1
            
    def visit_TryStar(self, node):

        self.write("try:")

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1


        for handler in node.handlers:
  
            text = f"except* {ast.unparse(handler.type)}"

            if handler.name:
                text += f" as {handler.name}"

            text += ":"

            self.write(text)

            self.level += 1

        for item in handler.body:
            self.visit(item)

            self.level -= 1

    def visit_TryStar(self, node):

        self.write("try:")

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1

        for handler in node.handlers:

            text = f"except* {ast.unparse(handler.type)}"

            if handler.name:
                text += f" as {handler.name}"

            text += ":"

            self.write(text)

            self.level += 1

            for item in handler.body:
                self.visit(item)

            self.level -= 1

        # -------------------------
    # ASYNC WITH
    # -------------------------

    def visit_AsyncWith(self, node):

        item = node.items[0]

        expression = ast.unparse(
            item.context_expr
        )

        self.write(
            f"async with {expression}:"
        )

        self.level += 1

        for stmt in node.body:
            self.visit(stmt)

        self.level -= 1
        
    def visit_With(self, node):

        expressions = []

        for item in node.items:
            expression = ast.unparse(item.context_expr)

            if item.optional_vars:
                expression += f" as {ast.unparse(item.optional_vars)}"

            expressions.append(expression)

        self.write(
            f"with {', '.join(expressions)}:"
    )

        self.level += 1

        for stmt in node.body:
            self.visit(stmt)

        self.level -= 1
    # -------------------------
    # IMPORTS
    # -------------------------

    def visit_Import(self, node):

        self.write(
            ast.unparse(node)
        )


    def visit_ImportFrom(self, node):

        self.write(
            ast.unparse(node)
        )

        # -------------------------
    # ASSIGN
    # -------------------------

    def visit_Assign(self, node):

        self.write(
            ast.unparse(node)
        )
        
        # -------------------------
    # VARIABLE ANNOTATION
    # -------------------------

    def visit_AnnAssign(self, node):

        target = ast.unparse(node.target)
        annotation = ast.unparse(node.annotation)

        if node.value:
            value = ast.unparse(node.value)

            self.write(
                f"{target}: {annotation} = {value}"
            )
        else:
            self.write(
                f"{target}: {annotation}"
            )
    # -------------------------
    # PASS
    # -------------------------

    def visit_Pass(self, node):

        self.write("pass")
        
