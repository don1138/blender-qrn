# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Quick Resize Node",
    "author": "Don Schnitzius",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Node Editor > Sidebar > Arrange",
    "description": "Set Active Node to a Fixed Width",
    "warning": "",
    "doc_url": "",
    "category": "Node",
}


"""
VERSION HISTORY

1.0 – 20/09/22
    – Create Addon
"""

import bpy
from bpy.types import Operator, Panel

class RN_PT_NodePanel(Panel):
    bl_label = "Resize Node"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Arrange"

    def draw(self, context):
        if context.active_node is not None:
            layout = self.layout
            row = layout.row()
            node = context.space_data.node_tree.nodes.active
            layout.label(text="Set Node Width:")
            if node and node.select:
                # Set Button Width
                row = layout.row(align=True)
                row.operator('node.button_140')
                row.operator('node.button_240')
                row.operator('node.button_340')
                row.operator('node.button_440')
            else:
                layout.label(text="(No Node Selected)", icon='GHOST_DISABLED')

class RN_OT__NodeButton140(Operator):

    'Set node width to 140'
    bl_idname = 'node.button_140'
    bl_label = '140'

    def execute(self, context):
        node = context.space_data.node_tree.nodes.active
        node.width = 140
        return {'FINISHED'}

class RN_OT__NodeButton240(Operator):

    'Set node width to 240'
    bl_idname = 'node.button_240'
    bl_label = '240'

    def execute(self, context):
        node = context.space_data.node_tree.nodes.active
        node.width = 240
        return {'FINISHED'}

class RN_OT__NodeButton340(Operator):

    'Set node width to 340'
    bl_idname = 'node.button_340'
    bl_label = '340'

    def execute(self, context):
        node = context.space_data.node_tree.nodes.active
        node.width = 340
        return {'FINISHED'}

class RN_OT__NodeButton440(Operator):

    'Set node width to 440'
    bl_idname = 'node.button_440'
    bl_label = '440'

    def execute(self, context):
        node = context.space_data.node_tree.nodes.active
        node.width = 440
        return {'FINISHED'}

classes = [
    RN_PT_NodePanel,
    RN_OT__NodeButton140,
    RN_OT__NodeButton240,
    RN_OT__NodeButton340,
    RN_OT__NodeButton440,
]

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()