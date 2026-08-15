# SPDX-License-Identifier: GPL-3.0-or-later

import bpy
from bpy.props import IntProperty
from bpy.types import Operator, Panel


class QRN_OT_SetNodeWidth(Operator):
    """Set the width of every selected node"""

    bl_idname = "node.qrn_set_width"
    bl_label = "Set Node Width"
    bl_options = {"REGISTER", "UNDO"}

    width: IntProperty(name="Width", min=1, max=700, options={"SKIP_SAVE"})

    @classmethod
    def poll(cls, context):
        return bool(getattr(context, "selected_nodes", ()))

    def execute(self, context):
        for node in context.selected_nodes:
            node.width = self.width
        return {"FINISHED"}


class QRN_OT_ToggleHiddenSockets(Operator):
    """Toggle unused sockets on selected nodes"""

    bl_idname = "node.qrn_toggle_hidden_sockets"
    bl_label = "Toggle Hidden Sockets (Ctrl-H)"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return bpy.ops.node.hide_socket_toggle.poll()

    def execute(self, context):
        bpy.ops.node.hide_socket_toggle()
        return {"FINISHED"}


class QRN_PT_NodePanel(Panel):
    bl_label = "Resize Nodes"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Arrange"

    def draw(self, context):
        layout = self.layout

        if not getattr(context, "selected_nodes", ()):
            layout.label(text="(No nodes selected)", icon="GHOST_DISABLED")
            return

        layout.label(text="Set Node Width:")

        col = layout.column(align=True)
        col.scale_y = 1.25
        row = col.row(align=True)
        for width in (140, 240):
            operator = row.operator("node.qrn_set_width", text=str(width))
            operator.width = width

        row = col.row(align=True)
        for width in (340, 440, 540):
            operator = row.operator("node.qrn_set_width", text=str(width))
            operator.width = width

        split = col.split(factor=1 / 3, align=True)
        operator = split.operator("node.qrn_set_width", text="640")
        operator.width = 640
        operator = split.operator("node.qrn_set_width", text="700 (Max Width)")
        operator.width = 700

        row = layout.row(align=True)
        row.scale_y = 1.25
        row.operator("node.qrn_toggle_hidden_sockets")


classes = (
    QRN_OT_SetNodeWidth,
    QRN_OT_ToggleHiddenSockets,
    QRN_PT_NodePanel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
