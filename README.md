# Discord Bot Role Management and Channel Creation - Commands Reference

This document provides a detailed list of available commands, flags, and sample inputs for the Discord bot.

## Table of Commands

| **Command**                           | **Description**                                                | **Flags**                              | **Sample Input** |
|---------------------------------------|----------------------------------------------------------------|----------------------------------------|------------------|
| `!create_roles`                       | Creates one or more roles in the server.                      | None                                   | `!create_roles Admin Moderator Member` |
| `!delete_roles`                       | Deletes one or more roles from the server.                    | None                                   | `!delete_roles Admin Moderator` |
| `!assignRole`                         | Assigns a specific role to one or more users.                 | None                                   | `!assignRole Admin John Jane` |
| `!remove_role`                        | Removes a specific role from one or more users.               | None                                   | `!remove_role Moderator John Jane` |
| `!create_categories_with_channels`    | Creates categories and channels with role-based permissions.  | `-m` (categories), `-r` (roles), `-ch` (channels) | `!create_categories_with_channels -m AdminCategory -r Admin Moderator -ch General Chat` |
|                                       |                                                                | `-m` (categories)                     | `-m Category1 Category2` |
|                                       |                                                                | `-r` (roles)                          | `-r Role1 Role2` |
|                                       |                                                                | `-ch` (channels)                      | `-ch Channel1 Channel2` |

## Explanation of Flags

- **`-m` (Categories)**:
  - Specifies the categories to create.
  - **Example**: `-m Category1 Category2`

- **`-r` (Roles)**:
  - Specifies the roles that will have access to the channels in the created categories.
  - **Example**: `-r Role1 Role2`

- **`-ch` (Channels)**:
  - Specifies the channels to create within the specified categories.
  - **Example**: `-ch Channel1 Channel2`

## Detailed Example Input

### Command: `!create_categories_with_channels -m AdminCategory -r Admin Moderator -ch General Chat`

- **`-m AdminCategory`**: Creates a category named `AdminCategory`.
- **`-r Admin Moderator`**: Grants access to the `Admin` and `Moderator` roles.
- **`-ch General Chat`**: Creates a channel named `General` under the `AdminCategory`.

---

