# Blender QRN

**Assign a Fixed Width to Selected Nodes.**

![Blender QLE Screenshot](https://github.com/don1138/blender-qrn/blob/master/blender-qrn.jpg)

## Installation

Download the latest ZIP from **Releases**, or `resize_nodes.py` from repository, and install addon.

## Usage

This addon creates a panel named **Resize Node** under ``Shader Editor > Sidebar > Arrange``.

Select one or more Nodes to activate the buttons.

### 👉 Fixed Widths
  + **140**
  + **240**
  + **340**
  + **440**
  + **550**
  + **640**
  + **700 (Max Width)** - The least practical option, so obviously it deserves the largest button. 😊

### 👉 Toggle Hidden Sockets
  + Node height get maximized to show all sockets, or minimized to show only used/essential sockets.

***

## Backstory

In **Blender 2.83**, when adding a **Node Wrangler Texture Setup**, the **Mapping Node** comes in at 240 wide – much too fat – so I have to manually slim it down to 140 every 😖 single 😖 time 😖. I couldn't find a way to change the default width on this node and save it in the startup file, so I duplicated the **Node Arrange** addon and hacked it to make this.

*Seconds after writing the previous line, I realized I could just edit ``node_wrangler.py`` and solve my initial grief.* :facepalm:.

But no matter – The buttons are still a convenient shortcut for tweaking Node widths and soothing my mild OCD.

This addon pairs well with 3DSinghVFX's work-in-progress [**Align Nodes**](https://github.com/3DSinghVFX/align_nodes).

## Version History

**1.1**
  + Changed scope from **Active** to **All Selected**
  + Added Button for **Toggle Hidden Sockets**

***

<p align="center">
  <img align="center" src="https://badges.pufler.dev/created/don1138/blender-qrn?style=for-the-badge&colorA=222&colorB=48684b" alt="Repo Created">
  <img align="center" src="https://badges.pufler.dev/updated/don1138/blender-qrn?style=for-the-badge&colorA=222&colorB=48684b" alt="Repo Updated">
</p>
