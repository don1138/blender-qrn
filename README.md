# Blender QRN (Quick Resize Nodes)

**Assign a Fixed Width to Selected Nodes.**

![Blender QRN 1.4.0](https://github.com/don1138/blender-qrn/blob/master/blender-qrn-140.jpg)

## Installation

Download the latest ZIP from **Releases**, or `resize_nodes.py` from repository, and install addon.

## Usage

This addon creates a panel named **Resize Node** under ``Shader Editor > Sidebar > Arrange``.

Select one or more Nodes to activate the buttons.

### 👉 Fixed Widths - Version 1.4.0
Blender 3.6 LTS locks the maximum width of nodes to 400, so the settings have been updated accordingly.
  + **140**
  + **240**
  + **340**
  + **200**
  + **400 (Max Width)** - The least practical option, so obviously it deserves the largest button. 😊

### 👉 Fixed Widths - Version 1.3.0
  + **140**
  + **240**
  + **340**
  + **440**
  + **550**
  + **640**
  + **200**
  + **700 (Max Width)** - The least practical option, so obviously it deserves the largest button. 😊

![Blender QRN 1.3.0](https://github.com/don1138/blender-qrn/blob/master/blender-qrn-130.jpg)

### 👉 Toggle Hidden Sockets
  + Node height get maximized to show all sockets, or minimized to show only used/essential sockets.

## Backstory

In **Blender 2.83**, when adding a **Node Wrangler Texture Setup**, the **Mapping Node** comes in at 240 wide – much too fat – so I have to manually slim it down to 140 every 😖 single 😖 time 😖. I couldn't find a way to change the default width on this node and save it in the startup file, so I duplicated the **Node Arrange** addon and hacked it to make this.

*Seconds after writing the previous line, I realized I could just edit ``node_wrangler.py`` and solve my initial grief.* :facepalm:.

But no matter – The buttons are still a convenient shortcut for tweaking Node widths and soothing my mild OCD.

This addon pairs well with 3DSinghVFX's work-in-progress [**Align Nodes**](https://github.com/3DSinghVFX/align_nodes).

<br><br>

<p align="center">
  <img alt="GitHub latest commit" src="https://img.shields.io/github/last-commit/don1138/blender-qrn">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/don1138/blender-qrn">
  <img alt="Github all releases" src="https://img.shields.io/github/downloads/don1138/blender-qrn/total.svg"><br>
  <img src="https://repobeats.axiom.co/api/embed/351f5fa19ab389a826f0c22830d40fea54f1d7ca.svg" alt="Repobeats analytics image">
</p>

