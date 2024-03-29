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


"""
VERSION HISTORY

1.4.0 - 06/60/23 
  - Bender 3.6.0 Compatability
    - Remove 440, 540, 640
    - Replace 700 with 400

1.3.0 - 01/31/23 
  - Add new width: 200

1.2.1 - 12/17/22 
  - Code refactoring
  - PEP8 formatting

1.2.0 - 18/03/22
  - Moved label "Set Node Width" inside IF statement

1.1.0 - 20/09/22
  - Changed scope from Active to All Selected
  - Added Button for Toggle Hidden Sockets

1.0 - 20/09/22
  - Create Addon
"""


bl_info = {
    "name"       : "QRN (Quick Resize Node)",
    "author"     : "Don Schnitzius",
    "version"    : (1, 4, 0),
    "blender"    : (3, 6, 0),
    "location"   : "Node Editor > Sidebar > Arrange",
    "description": "Assign a Fixed Width to Selected Nodes",
    "warning"    : "",
    "doc_url"   : "https://github.com/don1138/blender-qrn",
    "support"    : "COMMUNITY",
    "category"   : "Node",
}


import bpy
from bpy.types import Operator, Panel


def get_active_tree(context):
    tree = context.space_data.node_tree
    path = []
    if tree.nodes.active:
        while tree.nodes.active != context.active_node:
            tree = tree.nodes.active.node_tree
            path.append(tree)
    return tree, path


def get_nodes_links(context):
    tree, path = get_active_tree(context)
    return tree.nodes, tree.links


class RN_PT_NodePanel(Panel):
    bl_label = "Resize Nodes"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Arrange"

    def draw(self, context):
        if context.active_node is None:
            return
        layout = self.layout
        node = context.space_data.node_tree.nodes.active
        if node and node.select:
            self.draw_panel(layout)
        else:
            layout.label(text="(No Node Selected)", icon='GHOST_DISABLED')

    def draw_panel(self, layout):
        row = layout.row(align=True)
        row.label(text="Set Node Width:")

        row = layout.row(align=True)
        row.operator('node.button_140')
        row.operator('node.button_240')
        row.operator('node.button_340')

        row = layout.row(align=True)
        row.operator('node.button_200')
        row.scale_x = 2.0
        row.operator('node.button_400')

        row = layout.row(align=True)
        row.operator('node.button_toggle_hidden')


class RN_OT__NodeButton140(Operator):
    """Set node width to 140"""
    bl_idname = 'node.button_140'
    bl_label = '140'

    def execute(self, context):
        # node = context.space_data.node_tree.nodes.active
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                node.width = 140
        return {'FINISHED'}


class RN_OT__NodeButton240(Operator):
    """Set node width to 240"""
    bl_idname = 'node.button_240'
    bl_label = '240'

    def execute(self, context):
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                node.width = 240
        return {'FINISHED'}


class RN_OT__NodeButton340(Operator):
    """Set node width to 340"""
    bl_idname = 'node.button_340'
    bl_label = '340'

    def execute(self, context):
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                node.width = 340
        return {'FINISHED'}


class RN_OT__NodeButton400(Operator):
    """Set node width to 400"""
    bl_idname = 'node.button_400'
    bl_label = '400 (Max Width)'

    def execute(self, context):
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                node.width = 400
        return {'FINISHED'}


class RN_OT__NodeButton200(Operator):
    """Set node width to 200"""
    bl_idname = 'node.button_200'
    bl_label = '200'

    def execute(self, context):
        nodes, links = get_nodes_links(context)
        for node in nodes:
            if node.select == True:
                node.width = 200
        return {'FINISHED'}


class RN_OT__NodeButtonHideToggle(Operator):
    """Toggle Hidden Node Sockets"""
    bl_idname = 'node.button_toggle_hidden'
    bl_label = 'Toggle Hidden Sockets (⌃H)'

    def execute(self, context):
        bpy.ops.node.hide_socket_toggle()
        return {'FINISHED'}


classes = [
    RN_PT_NodePanel,
    RN_OT__NodeButton140,
    RN_OT__NodeButton200,
    RN_OT__NodeButton240,
    RN_OT__NodeButton340,
    RN_OT__NodeButton400,
    RN_OT__NodeButtonHideToggle
]


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
