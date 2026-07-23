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
    # Functions
    # -------------------------

    def visit_FunctionDef(self, node):

        args = ", ".join(
            arg.arg for arg in node.args.args
        )

        self.write(
            f"def {node.name}({args}):"
        )

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1


    # -------------------------
    # Classes
    # -------------------------

    def visit_ClassDef(self, node):

        self.write(
            f"class {node.name}:"
        )

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1


    # -------------------------
    # Variables
    # -------------------------

    def visit_Assign(self, node):

        self.write(
            ast.unparse(node)
        )


    # -------------------------
    # Simple expressions
    # -------------------------

    def visit_Expr(self, node):

        self.write(
            ast.unparse(node)
        )


    # -------------------------
    # IF / ELSE / ELIF
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

            # elif
            if (
                len(node.orelse) == 1
                and isinstance(node.orelse[0], ast.If)
            ):

                self.write(
                    f"elif {ast.unparse(node.orelse[0].test)}:"
                )

                self.level += 1

                for item in node.orelse[0].body:
                    self.visit(item)

                self.level -= 1


            # else
            else:

                self.write("else:")

                self.level += 1

                for item in node.orelse:
                    self.visit(item)

                self.level -= 1


    # -------------------------
    # FOR loop
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
    # WHILE loop
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
    # RETURN
    # -------------------------

    def visit_Return(self, node):

        if node.value:

            self.write(
                f"return {ast.unparse(node.value)}"
            )

        else:

            self.write("return")


    # -------------------------
    # PASS
    # -------------------------

    def visit_Pass(self, node):

        self.write("pass")


    # -------------------------
    # BREAK
    # -------------------------

    def visit_Break(self, node):

        self.write("break")


    # -------------------------
    # CONTINUE
    # -------------------------

    def visit_Continue(self, node):

        self.write("continue")
        
    def visit_Import(self, node):

        self.write(
            ast.unparse(node)
        )
        
    def visit_ImportFrom(self, node):

        self.write(
            ast.unparse(node)
        )
        
    def visit_For(self, node):

        self.write(
            f"for {ast.unparse(node.target)} in {ast.unparse(node.iter)}:"
        )

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1
    
    def visit_For(self, node):

        self.write(
            f"for {ast.unparse(node.target)} in {ast.unparse(node.iter)}:"
    )

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1
        
    def visit_While(self, node):

        self.write(
            f"while {ast.unparse(node.test)}:"
        )

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1


    def visit_Return(self, node):

        self.write(
            ast.unparse(node)
        )
        
    def visit_Try(self, node):

        self.write("try:")

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1


        for handler in node.handlers:

            if handler.type:
                self.write(
                    f"except {ast.unparse(handler.type)}:"
                )
            else:
                self.write(
                    "except:"
                )

            self.level += 1

            for item in handler.body:
                self.visit(item)

            self.level -= 1


        if node.finalbody:

            self.write("finally:")

            self.level += 1

            for item in node.finalbody:
                self.visit(item)

            self.level -= 1
    
        def visit_Try(self, node):

            self.write("try:")

            self.level += 1

            for item in node.body:
                self.visit(item)

                self.level -= 1


                for handler in node.handlers:

                    if handler.type:
                        self.write(
                            f"except {ast.unparse(handler.type)}:"
                    )
                    else:
                        self.write(
                        "except:"
                        )

                self.level += 1

                for item in handler.body:
                    self.visit(item)

                self.level -= 1


            if node.finalbody:

                self.write("finally:")

                self.level += 1

                for item in node.finalbody:
                    self.visit(item)

                self.level -= 1