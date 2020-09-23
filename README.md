# Blender QRN

**Assign a Fixed Width to the Active Node in the Shader Editor.**

![Blender QLE Screenshot](https://github.com/don1138/blender-qrn/blob/master/blender-qrn.jpg)

In Blender 2.83, when adding a Node Wrangler Texture Setup, the Mapping Node comes in at 240 wide – much too fat – so I have to manually slim it down to 140 every 😖 single 😖 time 😖. I couldn't find a way to change the default width on this node and save it in the startup file, so I duplicated the Node Arrange addon and hacked it to make this.

*Seconds after writing the previous line, I realized I could just edit ``node_wrangler.py`` and solve my initial grief.* :facepalm:.

But no matter – The buttons are still a convenient shortcut for tweaking Node widths and soothing my mild OCD.

## Installation

Download the latest ZIP from **Releases**, or `resize_node.py` from repository, and install addon.

## Usage

This addon creates a panel named **Resize Node** under ``Shader Editor > Sidebar > Arrange``.

  + Select a Node to activate the buttons.
  + Available Widths: 140 • 240 • 340 • 440

***

<p align="center">
  <img align="center" src="https://badges.pufler.dev/created/don1138/blender-qrn?style=for-the-badge&colorA=222&colorB=48684b" alt="Repo Created">
  <img align="center" src="https://badges.pufler.dev/updated/don1138/blender-qrn?style=for-the-badge&colorA=222&colorB=48684b" alt="Repo Updated">
</p>
