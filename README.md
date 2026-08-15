# Blender QRN (Quick Resize Nodes)

**Assign a Fixed Width to Selected Nodes.**

![Blender QRN 1.5.0](https://github.com/don1138/blender-qrn/blob/master/blender-qrn-150.jpg)

## Installation

1. Download the latest Extension ZIP from **Releases**. Do not extract it.
2. In Blender, open **Edit > Preferences > Get Extensions**.
3. Open the menu in the upper-right corner and choose **Install from Disk**.
4. Select the downloaded ZIP.

Requires Blender 4.5 or newer. Tested with Blender 4.5 LTS and 5.2 LTS.

## Usage

This extension creates a **Resize Nodes** panel under **Sidebar > Arrange** in the Shader Editor, Texture Node Editor, Geometry Node Editor, and Compositor.

Select one or more nodes to activate the width controls.

### 👉 Fixed Widths

+ **140**
+ **240**
+ **340**
+ **440**
+ **550**
+ **640**
+ **700 (Max Width)** - The least practical option, so obviously it deserves the largest button. 😊

### 👉 Toggle Hidden Sockets

+ Shows or hides unconnected sockets on the selected nodes.

## Backstory

In **Blender 2.83**, when adding a **Node Wrangler Texture Setup**, the **Mapping Node** comes in at 240 wide – much too fat – so I have to manually slim it down to 140 every 😖 single 😖 time 😖. I couldn't find a way to change the default width on this node and save it in the startup file, so I duplicated the **Node Arrange** addon and hacked it to make this.

*Seconds after writing the previous line, I realized I could just edit ``node_wrangler.py`` and solve my initial grief.* :facepalm:.

But no matter – The buttons are still a convenient shortcut for tweaking Node widths and soothing my mild OCD.

<br><br>

<p align="center">
  <img alt="GitHub latest commit" src="https://img.shields.io/github/last-commit/don1138/blender-qrn">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/don1138/blender-qrn">
  <img alt="Github all releases" src="https://img.shields.io/github/downloads/don1138/blender-qrn/total.svg"><br>
  <img src="https://repobeats.axiom.co/api/embed/351f5fa19ab389a826f0c22830d40fea54f1d7ca.svg" alt="Repobeats analytics image">
</p>
