# MinecraftEdu & ComputerCraft: Teacher Survival Guide

## 1. Starting the Class (The Server)
You are the **Host**. The world lives on YOUR computer.

1.  **Launch MinecraftEdu Launcher.**
2.  **Select "Start Server".**
3.  **World Selection:** Choose `Tutorial World` or `Flat World` (if `Stunde 1` map is missing).
4.  **Settings:**
    *   *Game Mode:* Survival (so they can't fly/break everything instantly) OR Adventure.
    *   *Difficulty:* Peacefull (No monsters).
    *   *Teacher Password:* Set one (e.g., `1234`).
5.  **Launch Client:** Open MinecraftEdu Client -> Join Server -> `Local Server` (or type `localhost`).

## 2. Teacher Controls ("The God Menu")
Press **`P`** (or `M` depending on version shortcut) to open the Teacher Menu.

| Tab Icon | Function | Usage |
| :--- | :--- | :--- |
| **World Options** | World Settings | Set Time to "Day" and "Freeze Time" (stop night). Turn off Fire/TNT. |
| **Players** | **Control Center** | See list of kids. **Freeze**, **Teleport**, **Mute**, **Kick**. |
| **Give Items** | Inventory | Give Turtles, Remotes, Blocks to everyone at once. |
| **Teleport** | Movement | "Bring all to me" (Use this when explaining to stop chaos). |

## 3. ComputerCraft Basics (The Turtle)

### Getting a Turtle
1.  Open Teacher Menu -> Give Items.
2.  Search `Turtle` (Pick "Mining Turtle" - the one with a diamond pickaxe).
3.  Search `Remote` (called "Turtle Remote" or "Bedienpult").
4.  Click "Give to All".

### Using the Remote
1.  **Right-Click** the Turtle with the Remote in hand.
2.  **Yellow Interface:**
    *   **Big Arrows:** Direct Control (Move Now).
    *   **Grid (Bottom):** The Program. Drag arrows here to make a sequence.
    *   **Play Button:** Run the sequence.
3.  **Common Issue:** "My turtle won't move!"
    *   **Fuel:** Turtles need coal. (Teacher Mode: Set `turtle.refuel(infinity)` if possible, or just give them stacks of coal to put in the turtle inventory slot).
    *   *Fix:* Give students coal. Tell them to put it in the turtle's inventory (right click turtle without remote), then type `refuel all` in the black command box (if available) OR just assume Creative Mode turtles don't need fuel.

## 4. Troubleshooting
*   **"I can't build!"**: The world has "Build Protect" on.
    *   *Fix:* Teacher Menu -> World Options -> **Allow Building**.
    *   *Better Fix:* Assign them a specific "Build Zone" block (Allow Block).
*   **"Where are you?"**:
    *   *Fix:* Teacher Menu -> Teleport -> **Bring All Players to Me**.
