# X4 Script-Befehlsreferenz

Automatisch generierte Liste aller XML-Tag-Befehle aus den vorhandenen Skriptverzeichnissen.

| Befehl | Vorkommen | Beispieldatei | Beschreibung |
| --- | --- | --- | --- |
| `DEPRECATED` | 1 | `08/md/modes.xml` | Deprecated. |
| `Research` | 1 | `08/md/x4ep1_mentor_subscription.xml` | Research. |
| `abort_build` | 4 | `08/aiscripts/order.build.equip.xml` | Bricht build ab (Attribute: container, build). |
| `abort_called_scripts` | 148 | `08/aiscripts/move.park.xml` | Bricht called scripts ab (Attribute: resume). |
| `abort_dismantling` | 1 | `08/aiscripts/order.salvage.crush.xml` | Bricht dismantling ab (Attribute: object). |
| `abort_scripts` | 6 | `08/md/factionlogic_economy.xml` | Bricht scripts ab (Attribute: entity). |
| `accept_offer` | 1 | `08/md/conversations.xml` | Accept offer (Attribute: cue). |
| `actions` | 14191 | `08/aiscripts/order.collect.ship.deployable.xml` | Actions. |
| `activate_default_ship_stance` | 6 | `08/aiscripts/fight.attack.object.fighter.xml` | Aktiviert default ship stance (Attribute: ship). |
| `activate_job_ship_orders` | 21 | `08/aiscripts/order.restock.subordinates.xml` | Aktiviert job ship orders (Attribute: ship). |
| `activate_mission` | 14 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Aktiviert mission (Attribute: cue). |
| `activate_platform_trigger` | 2 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Aktiviert platform trigger (Attribute: room, group, result). |
| `activate_ship_stance` | 9 | `08/aiscripts/fight.attack.object.fighter.xml` | Aktiviert ship stance (Attribute: ship, stance). |
| `activate_transporter` | 1 | `08/md/npc_state_machines.xml` | Aktiviert transporter (Attribute: start, destination, entity, result). |
| `activate_waiting_job_ship` | 1 | `08/aiscripts/build.shiptrader.xml` | Aktiviert waiting job ship (Attribute: ship). |
| `add` | 118 | `extensions/ego_dlc_split/ext_03/md/cinematiccamera.xml` | Add (Attribute: sel, name, value, pos). |
| `add_actor_to_post_location` | 8 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Fügt actor to post location hinzu (Attribute: actor). |
| `add_actor_to_room` | 127 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Fügt actor to room hinzu (Attribute: actor, slot). |
| `add_ammo` | 28 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Fügt ammo hinzu (Attribute: object, macro, amount). |
| `add_anomaly_destination` | 5 | `08/md/placedobjects.xml` | Fügt anomaly destination hinzu (Attribute: anomaly, destination). |
| `add_blueprints` | 55 | `08/md/story_research_xen_equipment.xml` | Fügt blueprints hinzu (Attribute: wares). |
| `add_boarding_attacker` | 3 | `08/md/showcases.xml` | Fügt boarding attacker hinzu (Attribute: attacker, operation, behavior). |
| `add_boarding_pod_to_operation` | 1 | `08/md/boarding.xml` | Fügt boarding pod to operation hinzu (Attribute: operation, ship). |
| `add_build_to_construct_ship` | 3 | `08/md/job_helper.xml` | Fügt build to construct ship hinzu (Attribute: result, object, buildobject, faction, price). |
| `add_build_to_expand_station` | 23 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | Fügt build to expand station hinzu (Attribute: object, buildobject, constructionplan). |
| `add_build_to_modify_ship` | 1 | `08/aiscripts/interrupt.restock.xml` | Fügt build to modify ship hinzu (Attribute: object, buildobject, ammo, units, price, result, immediate, internal). |
| `add_build_to_rebuild_fleet_ship` | 1 | `08/md/fleet_reconstitution.xml` | Fügt build to rebuild fleet ship hinzu (Attribute: result, object, fleetunit). |
| `add_build_to_recycle_ship` | 3 | `extensions/ego_dlc_terran/ext_03/md/yaki_supply.xml` | Fügt build to recycle ship hinzu (Attribute: result, buildobject, object, faction). |
| `add_cargo` | 162 | `extensions/ego_dlc_split/ext_03/md/scenario_advanced.xml` | Fügt cargo hinzu (Attribute: object, ware, exact). |
| `add_conversation_view` | 1 | `08/md/conversations.xml` | Fügt conversation view hinzu. |
| `add_default_production_wares` | 8 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Fügt default production wares hinzu (Attribute: object, lowerlimit, upperlimit). |
| `add_effect` | 71 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Fügt effect hinzu (Attribute: object, effect). |
| `add_encyclopedia_entry` | 29 | `08/md/gm_board_ship.xml` | Fügt encyclopedia entry hinzu (Attribute: value). |
| `add_equipment_mods` | 22 | `08/md/rml_destroy_rarelyonsight.xml` | Fügt equipment mods hinzu (Attribute: object). |
| `add_faction_relation` | 114 | `08/md/gm_ambush.xml` | Fügt faction relation hinzu (Attribute: faction, otherfaction, value, reason). |
| `add_holomap` | 12 | `08/md/gm_ambush.xml` | Fügt holomap hinzu (Attribute: name, rendertarget). |
| `add_holomap_text` | 10 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Fügt holomap text hinzu (Attribute: object, text). |
| `add_inventory` | 166 | `08/md/gm_ambush.xml` | Fügt inventory hinzu (Attribute: entity, ware). |
| `add_licence` | 101 | `08/md/playerreputation.xml` | Fügt licence hinzu (Attribute: faction, licencefaction, type). |
| `add_mass_traffic_quota` | 1 | `08/md/gm_killmasstraffic.xml` | Fügt mass traffic quota hinzu (Attribute: amount, job, zone, start, endtime, end). |
| `add_npc_line` | 1619 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Fügt npc line hinzu (Attribute: speaker, line, comment). |
| `add_object_velocity` | 7 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Fügt object velocity hinzu (Attribute: object). |
| `add_player_choice` | 676 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Fügt player choice hinzu (Attribute: text, section, comment). |
| `add_player_choice_return` | 39 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Fügt player choice return hinzu (Attribute: text). |
| `add_player_choice_sub` | 98 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Fügt player choice sub hinzu (Attribute: section, text, selectable, tooltip). |
| `add_player_choice_subconv` | 4 | `08/md/mainmenu.xml` | Fügt player choice subconv hinzu (Attribute: text, position, conversation, actor, baseparam, comment). |
| `add_player_discount` | 5 | `08/md/diplomacy.xml` | Fügt player discount hinzu (Attribute: name, id, amount, object, time, applytoshipsales). |
| `add_player_gravidar_access_request` | 4 | `08/md/diplomacy.xml` | Fügt player gravidar access request hinzu (Attribute: object). |
| `add_relation_boost` | 19 | `08/aiscripts/order.fight.escort.xml` | Fügt relation boost hinzu (Attribute: object, otherobject, value, decay, delay, silent). |
| `add_research` | 33 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Fügt research hinzu (Attribute: ware). |
| `add_skill` | 10 | `08/md/conversations.xml` | Fügt skill hinzu (Attribute: entity, type, exact). |
| `add_space_location_tag` | 1 | `08/md/factionlogic.xml` | Fügt space location tag hinzu (Attribute: space, tag). |
| `add_stock` | 1 | `08/md/npc_itemtrader.xml` | Fügt stock hinzu (Attribute: entity). |
| `add_terraforming_event` | 14 | `08/md/terraforming.xml` | Fügt terraforming event hinzu (Attribute: cluster, id). |
| `add_terraforming_project` | 85 | `extensions/ego_dlc_split/ext_03/md/terraforming.xml` | Fügt terraforming project hinzu (Attribute: cluster, id). |
| `add_to_group` | 899 | `08/aiscripts/order.collect.ship.xml` | Fügt to group hinzu (Attribute: groupname, object). |
| `add_trade_subscription` | 1 | `08/md/signal_leaks.xml` | Fügt trade subscription hinzu (Attribute: object). |
| `add_tradeware` | 128 | `extensions/ego_dlc_split/ext_03/md/inituniverse.xml` | Fügt tradeware hinzu (Attribute: object, ware, allowbuy, allowsell, lockavgprice). |
| `add_units` | 16 | `08/md/scenario_combat.xml` | Fügt units hinzu (Attribute: object, category, mk, exact). |
| `add_ware_reservation` | 3 | `08/aiscripts/order.mining.routine.xml` | Fügt ware reservation hinzu (Attribute: amount, type, reserver, object, duration, virtual, ware, replace). |
| `add_wares` | 12 | `08/md/rml_barterwares.xml` | Fügt wares hinzu (Attribute: object, ware, exact). |
| `add_watchdog_units_to_masstraffic` | 1 | `08/md/inituniverse.xml` | Fügt watchdog units to masstraffic hinzu (Attribute: object). |
| `add_weapon_to_weapongroup` | 8 | `08/md/scenario_combat.xml` | Fügt weapon to weapongroup hinzu (Attribute: weapon, weapongroup, primary). |
| `add_workforce` | 2 | `08/md/scenario_tutorials.xml` | Fügt workforce hinzu (Attribute: object, race, exact). |
| `advance_seed` | 10 | `08/md/diplomacy.xml` | Advance seed (Attribute: seed). |
| `aim_turret` | 1 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Aim turret (Attribute: turret, target). |
| `aiscript` | 175 | `08/aiscripts/order.collect.ship.deployable.xml` | Aiscript (Attribute: name, xsi, noNamespaceSchemaLocation). |
| `allow_conversation_escape` | 163 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Allow conversation escape (Attribute: enabled). |
| `ammo` | 7 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Ammo. |
| `ammunition` | 46 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Ammunition. |
| `angular` | 6 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Angular (Attribute: x, y, z). |
| `animate_chair` | 5 | `08/md/npc_state_machines.xml` | Animate chair (Attribute: slot, actor, chairtrigger). |
| `append_list_elements` | 287 | `extensions/ego_dlc_split/ext_03/md/cinematiccamera.xml` | Append list elements (Attribute: name, other). |
| `append_to_list` | 2115 | `08/aiscripts/order.deployobjectsatgates.xml` | Append to list (Attribute: name, exact). |
| `apply_attackstrength` | 15 | `08/aiscripts/fight.attack.object.capital.xml` | Apply attackstrength (Attribute: object, attacker, hullshield, hullonly, shieldonly, hullnoshield, module). |
| `apply_construction_sequence` | 16 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Apply construction sequence (Attribute: station, sequence, remove). |
| `apply_experience` | 71 | `08/aiscripts/order.wait.signal.xml` | Apply experience (Attribute: entity, experience, factor). |
| `apply_loadout` | 37 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Apply loadout (Attribute: object, flags, loadout). |
| `apply_player_influence` | 6 | `08/md/diplomacy.xml` | Apply player influence (Attribute: influence). |
| `assert` | 1024 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Assert (Attribute: value). |
| `assign_construction_vessel` | 2 | `08/aiscripts/order.build.deploy.xml` | Assign construction vessel (Attribute: object, buildmodule). |
| `assign_control_entity` | 55 | `08/md/npc_shadyguy.xml` | Assign control entity (Attribute: actor, object, post). |
| `assign_diplomacy_ship` | 2 | `08/md/diplomacy.xml` | Assign diplomacy ship (Attribute: ship, agent). |
| `assign_dismantling_target` | 6 | `08/aiscripts/order.salvage.routine.xml` | Assign dismantling target (Attribute: object, wreck). |
| `assign_hired_actor` | 2 | `08/md/conversations.xml` | Assign hired actor (Attribute: actor, target, post). |
| `assign_order_syncpoint_to_order` | 1 | `08/aiscripts/order.fight.tactical.xml` | Assign order syncpoint to order (Attribute: owner, order). |
| `assign_tow_target` | 5 | `08/aiscripts/order.salvage.collect.xml` | Assign tow target (Attribute: ship, object). |
| `attach_object_to_target` | 2 | `08/aiscripts/boarding.pod.xml` | Attach object to target (Attribute: object, target, keepoffset). |
| `attention` | 188 | `08/aiscripts/order.collect.ship.deployable.xml` | Attention (Attribute: min). |
| `author` | 1 | `08/md/finalisestations.xml` | Author (Attribute: name, alias, contact). |
| `basket` | 4 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Basket (Attribute: basket). |
| `behaviour` | 9 | `08/aiscripts/move.evade.xml` | Behaviour (Attribute: name). |
| `break` | 1092 | `08/aiscripts/order.collect.ship.xml` | Break. |
| `break_formation` | 3 | `08/aiscripts/move.gate.xml` | Break formation (Attribute: object). |
| `briefing` | 550 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Briefing. |
| `can_process_recyclable_object` | 3 | `08/aiscripts/order.salvage.deliver.xml` | Can process recyclable object (Attribute: module, object, result, trade). |
| `can_safely_extend_build_plot` | 1 | `08/md/factionlogic_economy.xml` | Can safely extend build plot (Attribute: object, negx, posx, negy, posy, negz, posz, result). |
| `cancel_all_orders` | 265 | `08/md/gm_ambush.xml` | Cancel all orders (Attribute: object). |
| `cancel_conversation` | 25 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Cancel conversation (Attribute: actor, force). |
| `cancel_cue` | 2379 | `08/md/gm_ambush.xml` | Cancel cue (Attribute: cue). |
| `cancel_order` | 146 | `08/aiscripts/order.deployobjectsatgates.xml` | Cancel order (Attribute: order). |
| `cancel_space_reservation` | 53 | `08/aiscripts/mining.collect.ship.capital.xml` | Cancel space reservation (Attribute: component, zone, index). |
| `capture_screen` | 3 | `08/md/terraforming.xml` | Capture screen (Attribute: directory). |
| `cargo` | 2 | `08/md/x4ep1_mentor_subscription.xml` | Cargo. |
| `cease_fire` | 66 | `08/aiscripts/fight.attack.object.capital.xml` | Cease fire (Attribute: object, weaponmode). |
| `center_holomap_view` | 1 | `08/md/scenario_advanced.xml` | Center holomap view (Attribute: zoomtofit). |
| `ch0_accept` | 1 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Ch0 accept. |
| `change` | 1 | `08/md/rml_destroy_entities.xml` | Change (Attribute: date, author, description). |
| `change_relation_on_attack` | 2 | `08/md/notifications.xml` | Change relation on attack (Attribute: attacker, attacked, method, weapon, result). |
| `change_relation_on_boarding` | 2 | `08/md/notifications.xml` | Change relation on boarding (Attribute: boarder, boarded, attempt, result). |
| `change_relation_on_kill` | 1 | `08/md/notifications.xml` | Change relation on kill (Attribute: killer, killed, method, result). |
| `check_age` | 25 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Check age (Attribute: min). |
| `check_all` | 728 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Check all. |
| `check_animation_state` | 5 | `08/md/npc_state_machines.xml` | Check animation state (Attribute: result, object, group, state). |
| `check_any` | 1550 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Check any. |
| `check_is_build_location_free` | 1 | `08/aiscripts/move.buildership.xml` | Check is build location free (Attribute: name, zone, macro, excluded). |
| `check_line_of_sight` | 11 | `08/aiscripts/masstraffic.watchdog.xml` | Check line of sight (Attribute: object, target, name). |
| `check_object` | 35 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Check object (Attribute: result, object). |
| `check_production_allowed` | 1 | `08/md/factionlogic_economy.xml` | Check production allowed (Attribute: result, object, ware). |
| `check_value` | 5877 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Check value (Attribute: value). |
| `check_walk_path` | 13 | `08/md/npc_state_machines.xml` | Check walk path (Attribute: actor, end, result). |
| `claim_ship` | 4 | `08/aiscripts/move.claim.xml` | Claim ship (Attribute: target, pilot). |
| `clamp_equipment_amount` | 1 | `08/aiscripts/interrupt.restock.xml` | Clamp equipment amount (Attribute: resultammo, resultunits, object, builder, ammo, units). |
| `clamp_trade_amount` | 13 | `08/aiscripts/order.trade.wareexchange.ship.xml` | Clamp trade amount (Attribute: trade, amount, buyer, seller, result, updatedeal). |
| `clear_actor_current_chair` | 1 | `08/md/npc_state_machines.xml` | Clear actor current chair (Attribute: actor). |
| `clear_actor_emotion` | 5 | `08/md/npc_usecases.xml` | Clear actor emotion. |
| `clear_actor_lookat` | 15 | `08/md/npc_usecases.xml` | Clear actor lookat. |
| `clear_actor_pod_arrival_time` | 2 | `08/md/npc_state_machines.xml` | Clear actor pod arrival time (Attribute: actor). |
| `clear_actor_roomslot` | 17 | `08/md/scenario_combat.xml` | Clear actor roomslot (Attribute: actor). |
| `clear_actor_tool` | 4 | `08/md/npc_state_machines.xml` | Clear actor tool (Attribute: actor). |
| `clear_buildanchor` | 2 | `08/aiscripts/build.shiptrader.xml` | Clear buildanchor (Attribute: buildprocessor). |
| `clear_collision_filter` | 1 | `08/aiscripts/mining.collect.drone.xml` | Clear collision filter (Attribute: object). |
| `clear_dismantling_target` | 5 | `08/aiscripts/order.salvage.routine.xml` | Clear dismantling target (Attribute: object, wreck). |
| `clear_entity_role` | 4 | `08/md/x4ep1_trade_subscriptions.xml` | Clear entity role (Attribute: entity). |
| `clear_entity_role_object` | 4 | `08/md/npc_state_machines.xml` | Clear entity role object (Attribute: entity). |
| `clear_faction_diplomacy_exclusion` | 31 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Clear faction diplomacy exclusion (Attribute: faction, otherfaction, flags). |
| `clear_fleet_ship_build_issues` | 1 | `08/md/fleet_reconstitution.xml` | Clear fleet ship build issues (Attribute: fleetunit). |
| `clear_fog_of_war` | 2 | `08/md/scenario_tutorials.xml` | Clear fog of war (Attribute: sector, range). |
| `clear_group` | 166 | `08/md/rml_barterwares.xml` | Clear group (Attribute: group). |
| `clear_list` | 69 | `08/aiscripts/lib.target.selection.xml` | Clear list (Attribute: list). |
| `clear_object_access_licence` | 1 | `extensions/ego_dlc_terran/ext_03/md/story_terran_core.xml` | Clear object access licence (Attribute: object). |
| `clear_object_name` | 3 | `08/md/x4ep1_mentor_subscription.xml` | Clear object name (Attribute: object). |
| `clear_object_sound_override` | 2 | `extensions/ego_dlc_terran/ext_03/md/story_yaki.xml` | Clear object sound override (Attribute: object, type). |
| `clear_order_failure` | 25 | `08/aiscripts/order.trade.routine.xml` | Clear order failure (Attribute: order). |
| `clear_recurring_order_failure` | 11 | `08/aiscripts/order.salvage.collect.xml` | Clear recurring order failure (Attribute: object, id). |
| `clear_ship_undocking` | 2 | `08/aiscripts/move.undock.xml` | Clear ship undocking (Attribute: ship). |
| `clear_shortage_reports` | 2 | `08/md/factionlogic.xml` | Clear shortage reports (Attribute: object). |
| `clear_table` | 65 | `08/aiscripts/fight.attack.object.capital.xml` | Clear table (Attribute: table). |
| `clear_tow_target` | 1 | `08/aiscripts/order.salvage.collect.xml` | Clear tow target (Attribute: ship, object). |
| `col` | 15 | `08/md/scenario_combat.xml` | Col (Attribute: idx, textcolor, text, bgcolor, fontsize, halign, valign). |
| `collect_asteroid` | 2 | `08/aiscripts/mining.collect.ship.medium.xml` | Collect asteroid (Attribute: object, asteroid). |
| `collect_deployable` | 3 | `08/aiscripts/move.collect.ship.smallship.xml` | Collect deployable (Attribute: object, deployable). |
| `collect_drop` | 1 | `08/aiscripts/move.collect.ship.smallship.xml` | Collect drop (Attribute: object, drop). |
| `collect_unit` | 4 | `08/aiscripts/fight.attack.object.capital.xml` | Collect unit (Attribute: object, unit). |
| `commandeer_object` | 33 | `08/md/gm_ambush.xml` | Commandeer object (Attribute: object). |
| `compatibilities` | 5 | `08/md/factionlogic_economy.xml` | Compatibilities. |
| `complete_diplomacy_action_operation` | 20 | `08/md/diplomacy.xml` | Complete diplomacy action operation (Attribute: operation, success, agentresult). |
| `complete_diplomacy_event_operation` | 1 | `08/md/diplomacy.xml` | Complete diplomacy event operation (Attribute: operation, outcome, agentresult). |
| `condition` | 5 | `08/md/terraforming.xml` | Condition (Attribute: stat, min). |
| `conditions` | 11773 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Conditions. |
| `connect_to_trade_location` | 1 | `08/aiscripts/move.park.xml` | Connect to trade location (Attribute: ship, tradedock, result). |
| `continue` | 120 | `08/aiscripts/fight.attack.object.capital.xml` | Continue. |
| `count_dockingbays` | 4 | `08/md/rml_transport_passengers_v2.xml` | Count dockingbays (Attribute: object, exact). |
| `count_gates` | 1 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | Count gates (Attribute: result, active, space, negate). |
| `count_gravidar_contacts` | 16 | `08/aiscripts/fight.attack.object.capital.xml` | Count gravidar contacts (Attribute: result, object, excluded, macro, maybeattackedby, functional, multiple). |
| `count_object_components` | 23 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | Count object components (Attribute: object, class, min). |
| `count_objects` | 2 | `08/md/scenario_advanced.xml` | Count objects (Attribute: result, class, space, min). |
| `count_rooms` | 4 | `08/md/npc_instantiation.xml` | Count rooms (Attribute: object, roomtype, exact). |
| `count_ships` | 19 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Count ships (Attribute: result, owner, space, min, masstraffic, checkoperational, class). |
| `count_stations` | 13 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Count stations (Attribute: trueowner, min, space). |
| `create_ai_unit` | 5 | `08/aiscripts/build.shiptrader.xml` | Create ai unit (Attribute: object). |
| `create_boarding_operation` | 1 | `08/md/showcases.xml` | Create boarding operation (Attribute: faction, target, result, approach, insertion). |
| `create_build_storage` | 1 | `08/md/inituniverse.xml` | Create build storage (Attribute: station). |
| `create_construction_sequence` | 23 | `extensions/ego_dlc_terran/ext_03/md/story_yaki.xml` | Create construction sequence (Attribute: macros, station, base). |
| `create_control_entity` | 25 | `08/aiscripts/build.shiptrader.xml` | Create control entity (Attribute: name, object, post). |
| `create_crate` | 10 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Create crate (Attribute: name, macro, slot). |
| `create_cue_actor` | 269 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Create cue actor (Attribute: name, cue, group). |
| `create_diplomacy_event_operation` | 2 | `08/md/diplomacy.xml` | Create diplomacy event operation (Attribute: result, event, agent, faction, otherfaction, source, owner). |
| `create_dynamic_interior` | 54 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Create dynamic interior (Attribute: object, corridor, room, name, interiorname, corridorname, roomname). |
| `create_factory` | 5 | `08/md/factionlogic_economy.xml` | Create factory (Attribute: name, modules, resultbasesequence, sector, race, owner, originalproduct). |
| `create_formation` | 6 | `08/aiscripts/order.fight.escort.xml` | Create formation (Attribute: leader, follower, formation, param, maxshipsperline, rollmembers, rollformation). |
| `create_god_factory` | 20 | `08/md/setup.xml` | Create god factory (Attribute: groupname, id). |
| `create_god_station` | 38 | `08/md/factionlogic_stations.xml` | Create god station (Attribute: name, id, state). |
| `create_group` | 517 | `extensions/ego_dlc_split/ext_03/md/x4ep1_war_subscriptions.xml` | Create group (Attribute: groupname). |
| `create_list` | 393 | `08/md/gm_ambush.xml` | Create list (Attribute: name). |
| `create_loadout` | 30 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Create loadout (Attribute: result). |
| `create_lockbox` | 10 | `08/md/placedobjects.xml` | Create lockbox (Attribute: name, macro, sector). |
| `create_mission` | 438 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Create mission (Attribute: cue, type, name, description, difficulty, faction, group, activate, comment). |
| `create_mission_thread` | 7 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Create mission thread (Attribute: cue, name, description, rewardtext). |
| `create_mission_thread_offer` | 4 | `08/md/mc_management.xml` | Create mission thread offer (Attribute: cue, actor, type, difficulty, threadtype, group). |
| `create_npc_from_template` | 7 | `08/aiscripts/lib.respond.foundabandonedship.xml` | Create npc from template (Attribute: name, object, slot, template, owner). |
| `create_npc_template` | 37 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Create npc template (Attribute: object, entity, role). |
| `create_object` | 173 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Create object (Attribute: name, groupname, macro, owner, sector). |
| `create_offer` | 86 | `08/md/gm_ambush.xml` | Create offer (Attribute: cue, location, distance, name, description, difficulty, actor). |
| `create_order` | 1059 | `08/aiscripts/move.park.xml` | Create order (Attribute: id, object, immediate). |
| `create_order_syncpoint` | 1 | `08/aiscripts/order.fight.tactical.xml` | Create order syncpoint (Attribute: owner). |
| `create_orientation` | 67 | `08/md/rml_barterwares.xml` | Create orientation (Attribute: name, orientation, refobject). |
| `create_platform_actor` | 2 | `08/md/inituniverse.xml` | Create platform actor (Attribute: room, post). |
| `create_position` | 640 | `08/aiscripts/order.collect.ship.xml` | Create position (Attribute: name, space, object). |
| `create_position_outside_boundingbox` | 1 | `08/aiscripts/move.nearby.xml` | Create position outside boundingbox (Attribute: name, distance, component). |
| `create_presentation_cluster` | 33 | `08/md/gm_ambush.xml` | Create presentation cluster (Attribute: name, background). |
| `create_prop` | 2 | `08/md/story_diplomacy_intro.xml` | Create prop (Attribute: name, slot, macro). |
| `create_random_position_in_boundingbox` | 1 | `08/aiscripts/masstraffic.watchdog.xml` | Create random position in boundingbox (Attribute: component, name). |
| `create_replacement_subordinates` | 1 | `08/aiscripts/order.restock.subordinates.xml` | Create replacement subordinates (Attribute: name, commander, buildobject, init, max, multiple). |
| `create_representative_actor` | 1 | `08/md/factionlogic.xml` | Create representative actor (Attribute: name, station, faction). |
| `create_rotation` | 46 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Create rotation (Attribute: name, yaw). |
| `create_ship` | 453 | `08/md/gm_ambush.xml` | Create ship (Attribute: name, macro, zone). |
| `create_ship--` | 2 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Create ship--. |
| `create_signal_leak` | 46 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Create signal leak (Attribute: groupname, macro, type, object). |
| `create_station` | 55 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | Create station (Attribute: rawname, name, sector, macro, owner). |
| `create_trade_computer` | 2 | `08/md/rml_barterwares.xml` | Create trade computer (Attribute: object). |
| `create_trade_offer` | 13 | `08/md/rml_barterwares.xml` | Create trade offer (Attribute: name, object, buyer, ware, amount, price, virtual, virtualmoney, playeronly). |
| `create_trade_order` | 13 | `08/md/rml_barterwares.xml` | Create trade order (Attribute: name, object, tradeoffer, amount, immediate). |
| `crew` | 6 | `extensions/ego_dlc_terran/ext_03/md/gs_terran2.xml` | Crew. |
| `cue` | 14685 | `extensions/ego_dlc_split/ext_03/md/x4ep1_war_subscriptions.xml` | Cue (Attribute: name, version, ref). |
| `cue_is_cancelled` | 3 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Cue is cancelled (Attribute: cue). |
| `cue_is_complete` | 37 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Cue is complete (Attribute: cue). |
| `cue_is_disabled` | 2 | `08/md/story_diplomacy_intro.xml` | Cue is disabled (Attribute: cue). |
| `cue_is_waiting` | 19 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | Cue is waiting (Attribute: cue). |
| `cues` | 5328 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Cues. |
| `cutscene` | 15 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Cutscene (Attribute: key, param). |
| `cutscene_event` | 96 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Cutscene event (Attribute: key, event). |
| `debug_text` | 10592 | `08/aiscripts/order.collect.ship.xml` | Debug text (Attribute: text). |
| `debug_to_file` | 17 | `08/aiscripts/build.shiptrader.xml` | Debug to file (Attribute: name, directory, text, append). |
| `delay` | 2169 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Delay (Attribute: exact). |
| `deliveries` | 4 | `08/md/terraforming.xml` | Deliveries. |
| `delivery` | 7 | `08/md/gm_getexactcrew.xml` | Delivery. |
| `deplete_yield` | 3 | `08/aiscripts/fight.attack.object.capital.xml` | Deplete yield (Attribute: sector, container, ware, amount). |
| `deploy_construction_vessel` | 1 | `08/aiscripts/order.build.deploy.xml` | Deploy construction vessel (Attribute: object, buildmodule). |
| `destroy_group` | 58 | `08/md/scenario_combat.xml` | Destroy group (Attribute: group, explosion). |
| `destroy_object` | 449 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Destroy object (Attribute: object). |
| `detach_from_masstraffic` | 10 | `08/aiscripts/order.trade.wareexchange.ship.xml` | Detach from masstraffic (Attribute: object, wait). |
| `diff` | 32 | `extensions/ego_dlc_split/ext_03/md/scenario_combat.xml` | Diff. |
| `disable_collision_response` | 9 | `08/aiscripts/boarding.pod.xml` | Disable collision response (Attribute: object). |
| `disable_collisions_between` | 16 | `08/aiscripts/move.park.xml` | Disable collisions between (Attribute: object, target). |
| `disable_travel_mode` | 2 | `08/md/scenario_tutorials.xml` | Disable travel mode (Attribute: ship, duration). |
| `disconnect_from_trade_location` | 10 | `08/aiscripts/move.park.xml` | Disconnect from trade location (Attribute: ship). |
| `disengage_construction_vessel` | 8 | `08/aiscripts/order.build.deploy.xml` | Disengage construction vessel (Attribute: object). |
| `dismiss_control_entity` | 26 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Dismiss control entity (Attribute: object, actor). |
| `dismiss_diplomacy_agent` | 1 | `08/md/npc_agent.xml` | Dismiss diplomacy agent (Attribute: agent). |
| `dismiss_pilot` | 1 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Dismiss pilot (Attribute: object). |
| `dispatch_marines` | 1 | `08/md/boarding.xml` | Dispatch marines (Attribute: operation, attacker, object, marines). |
| `do_all` | 2460 | `08/aiscripts/order.collect.ship.xml` | Do all (Attribute: exact, counter). |
| `do_any` | 654 | `extensions/ego_dlc_split/ext_03/md/x4ep1_war_subscriptions.xml` | Do any. |
| `do_else` | 6252 | `08/aiscripts/order.collect.ship.xml` | Do else. |
| `do_elseif` | 4419 | `extensions/ego_dlc_split/ext_03/md/factionlogic_stations.xml` | Do elseif (Attribute: value). |
| `do_for_each` | 1694 | `08/aiscripts/order.collect.ship.xml` | Do for each (Attribute: name, valuename, in). |
| `do_if` | 24024 | `extensions/ego_dlc_split/ext_03/md/factionlogic_stations.xml` | Do if (Attribute: value). |
| `do_while` | 161 | `08/aiscripts/move.park.xml` | Do while (Attribute: value). |
| `dock` | 1 | `08/aiscripts/order.dock.xml` | Dock (Attribute: ship). |
| `dock_masstraffic_drone` | 3 | `08/aiscripts/masstraffic.move.waitforsignal.xml` | Dock masstraffic drone (Attribute: object, destination). |
| `dock_player_ship_at` | 1 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Dock player ship at (Attribute: destination). |
| `documentation` | 4 | `08/md/finalisestations.xml` | Documentation. |
| `drop` | 87 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Drop (Attribute: ref). |
| `drop_cargo` | 9 | `08/aiscripts/move.flee.xml` | Drop cargo (Attribute: object, ware, exact). |
| `drop_illegal_cargo` | 2 | `08/aiscripts/order.trade.perform.xml` | Drop illegal cargo (Attribute: object, faction, groupname, wares, amounts). |
| `drop_illegal_inventory` | 1 | `08/aiscripts/lib.respond.inspected.xml` | Drop illegal inventory (Attribute: groupname, object, faction). |
| `drop_inventory` | 2 | `08/md/story_diplomacy_intro.xml` | Drop inventory (Attribute: object, ware, groupname, macro). |
| `edit_order_param` | 207 | `08/aiscripts/order.deployobjectsatgates.xml` | Edit order param (Attribute: order, param, value). |
| `editable` | 7 | `08/aiscripts/order.fight.tactical.xml` | Editable. |
| `eject_npcs` | 3 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Eject npcs (Attribute: object). |
| `eject_people` | 8 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Eject people (Attribute: object). |
| `enable_collision_response` | 4 | `08/aiscripts/move.undock.xml` | Enable collision response (Attribute: object). |
| `enable_collisions_between` | 14 | `08/aiscripts/move.park.xml` | Enable collisions between (Attribute: object, target). |
| `enable_lost_ship_replacement` | 2 | `08/md/fleet_reconstitution.xml` | Enable lost ship replacement. |
| `end` | 29 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | End (Attribute: value). |
| `end_boarding_operation` | 5 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | End boarding operation (Attribute: operation). |
| `end_repair_mass_traffic` | 2 | `08/aiscripts/engineer.ai.xml` | End repair mass traffic (Attribute: object). |
| `engine` | 69 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Engine (Attribute: macro, path). |
| `equip_weapon` | 3 | `08/md/showcases.xml` | Equip weapon (Attribute: object, macro). |
| `equipmentmods` | 5 | `extensions/ego_dlc_terran/ext_03/md/story_yaki.xml` | Equipmentmods. |
| `estimate_travel_time` | 29 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Estimate travel time (Attribute: result, start, target). |
| `evaluate_ammo_storage` | 3 | `08/aiscripts/lib.ammo.missiles.xml` | Evaluate ammo storage (Attribute: object, type, capacity, macros, amounts, wares). |
| `evaluate_deployable_storage` | 2 | `08/aiscripts/interrupt.restock.xml` | Evaluate deployable storage (Attribute: object, level). |
| `evaluate_diplomacy_event_operation_outcome` | 1 | `08/md/diplomacy.xml` | Evaluate diplomacy event operation outcome (Attribute: result, operation, seed). |
| `evaluate_missile_storage` | 2 | `08/aiscripts/interrupt.restock.xml` | Evaluate missile storage (Attribute: object, level). |
| `evaluate_unit_storage` | 5 | `08/aiscripts/interrupt.restock.xml` | Evaluate unit storage (Attribute: object, level). |
| `event_alert_level_changed` | 1 | `08/md/npc_state_machines.xml` | Event alert level changed (Attribute: object, check). |
| `event_autopilot_deactivated` | 1 | `08/md/notifications.xml` | Event autopilot deactivated. |
| `event_autopilot_target_set` | 2 | `08/md/scenario_tutorials.xml` | Event autopilot target set. |
| `event_boarding_operation_created` | 1 | `08/md/boarding.xml` | Event boarding operation created. |
| `event_boarding_operation_removed` | 2 | `08/md/showcases.xml` | Event boarding operation removed (Attribute: operation). |
| `event_boarding_operation_started` | 2 | `08/aiscripts/interrupt.disengage.xml` | Event boarding operation started. |
| `event_boarding_phase_changed` | 1 | `08/md/boarding.xml` | Event boarding phase changed (Attribute: operation). |
| `event_boost_stopped` | 1 | `08/aiscripts/move.nohighway.xml` | Event boost stopped (Attribute: object). |
| `event_briefing_cancelled` | 61 | `08/md/gm_ambush.xml` | Event briefing cancelled (Attribute: cue). |
| `event_briefing_started` | 61 | `08/md/gm_ambush.xml` | Event briefing started (Attribute: cue). |
| `event_briefing_submission_selected` | 58 | `08/md/gm_ambush.xml` | Event briefing submission selected (Attribute: cue). |
| `event_briefing_submission_unselected` | 58 | `08/md/gm_ambush.xml` | Event briefing submission unselected (Attribute: cue). |
| `event_build_added` | 3 | `08/aiscripts/build.shiptrader.xml` | Event build added (Attribute: object). |
| `event_build_cancelled` | 5 | `08/aiscripts/order.restock.subordinates.xml` | Event build cancelled (Attribute: object). |
| `event_build_finished` | 16 | `08/aiscripts/fight.attack.object.capital.xml` | Event build finished (Attribute: object). |
| `event_build_finished_components` | 4 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | Event build finished components (Attribute: object). |
| `event_build_loadout_applied` | 1 | `08/aiscripts/order.build.equip.xml` | Event build loadout applied (Attribute: object, build). |
| `event_build_started` | 7 | `08/aiscripts/order.restock.subordinates.xml` | Event build started (Attribute: object). |
| `event_character_animation_finished` | 23 | `08/md/npc_state_machines.xml` | Event character animation finished (Attribute: object). |
| `event_character_animation_started` | 7 | `08/md/scenario_combat.xml` | Event character animation started (Attribute: group, id). |
| `event_contained_object_changed_true_owner` | 3 | `08/md/rml_board_ship.xml` | Event contained object changed true owner (Attribute: space, owner). |
| `event_contained_object_relation_range_changed` | 5 | `08/aiscripts/fight.attack.object.capital.xml` | Event contained object relation range changed (Attribute: group, faction). |
| `event_contained_sector_changed_owner` | 1 | `08/md/setup.xml` | Event contained sector changed owner (Attribute: owner, space). |
| `event_contained_sector_changed_true_owner` | 1 | `08/md/finalisestations.xml` | Event contained sector changed true owner (Attribute: space). |
| `event_control_entity_added` | 14 | `08/aiscripts/fight.attack.object.capital.xml` | Event control entity added (Attribute: object, entity). |
| `event_control_entity_removed` | 11 | `08/aiscripts/fight.attack.object.capital.xml` | Event control entity removed (Attribute: object, entity). |
| `event_conversation_finished` | 136 | `08/md/rml_barterwares.xml` | Event conversation finished (Attribute: actor). |
| `event_conversation_next_section` | 331 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Event conversation next section (Attribute: actor). |
| `event_conversation_returned_to_section` | 50 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Event conversation returned to section (Attribute: actor). |
| `event_conversation_started` | 258 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Event conversation started (Attribute: actor). |
| `event_cue_activated` | 3 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Event cue activated (Attribute: cue). |
| `event_cue_cancelled` | 57 | `08/md/rml_transport_passengers_v2.xml` | Event cue cancelled (Attribute: cue). |
| `event_cue_completed` | 290 | `08/md/gm_ambush.xml` | Event cue completed (Attribute: cue). |
| `event_cue_signalled` | 5667 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Event cue signalled. |
| `event_cutscene_ready` | 1 | `08/md/npc_usecases.xml` | Event cutscene ready (Attribute: cutscene). |
| `event_cutscene_signal` | 1 | `extensions/ego_dlc_terran/ext_03/md/story_terran_prelude.xml` | Event cutscene signal (Attribute: name). |
| `event_cutscene_started` | 28 | `extensions/ego_dlc_terran/ext_03/md/gs_terran2.xml` | Event cutscene started (Attribute: cutscene). |
| `event_cutscene_stopped` | 41 | `08/md/rml_barterwares.xml` | Event cutscene stopped (Attribute: cutscene). |
| `event_diplomacy_action_operation_aborted` | 20 | `08/md/diplomacy.xml` | Event diplomacy action operation aborted (Attribute: operation). |
| `event_diplomacy_action_operation_completed` | 1 | `08/md/diplomacy.xml` | Event diplomacy action operation completed. |
| `event_diplomacy_action_operation_started` | 22 | `08/md/diplomacy.xml` | Event diplomacy action operation started. |
| `event_diplomacy_event_operation_completed` | 1 | `08/md/diplomacy.xml` | Event diplomacy event operation completed. |
| `event_diplomacy_event_operation_option_chosen` | 1 | `08/md/diplomacy.xml` | Event diplomacy event operation option chosen (Attribute: operation). |
| `event_diplomacy_event_operation_started` | 1 | `08/md/diplomacy.xml` | Event diplomacy event operation started. |
| `event_entity_entered` | 2 | `08/md/scenario_combat.xml` | Event entity entered (Attribute: space). |
| `event_entity_left` | 3 | `08/md/cover.xml` | Event entity left (Attribute: space). |
| `event_entity_transport_finished` | 1 | `08/md/npc_state_machines.xml` | Event entity transport finished (Attribute: entity). |
| `event_faction_activated` | 3 | `08/md/setup.xml` | Event faction activated. |
| `event_faction_deactivated` | 33 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Event faction deactivated (Attribute: faction). |
| `event_faction_headquarters_changed` | 1 | `08/md/rml_escort_ambiguous.xml` | Event faction headquarters changed. |
| `event_faction_police_changed` | 3 | `08/aiscripts/order.move.recon.xml` | Event faction police changed (Attribute: faction). |
| `event_faction_relation_changed` | 35 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_war_terran.xml` | Event faction relation changed (Attribute: faction, otherfaction). |
| `event_faction_representative_changed` | 2 | `08/md/playerreputation.xml` | Event faction representative changed (Attribute: faction). |
| `event_game_loaded` | 29 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | Event game loaded. |
| `event_game_saved` | 1 | `08/md/notifications.xml` | Event game saved (Attribute: success). |
| `event_game_started` | 2 | `08/md/npc_usecases.xml` | Event game started. |
| `event_god_created_factory` | 2 | `08/md/finalisestations.xml` | Event god created factory (Attribute: space). |
| `event_god_created_object` | 1 | `08/md/rml_locate_object.xml` | Event god created object (Attribute: space). |
| `event_god_created_station` | 1 | `08/md/inituniverse.xml` | Event god created station (Attribute: space). |
| `event_gravidar_has_scanned` | 16 | `08/aiscripts/fight.attack.object.capital.xml` | Event gravidar has scanned (Attribute: object). |
| `event_guidance_disabled` | 2 | `08/md/rml_buildstation.xml` | Event guidance disabled (Attribute: cue). |
| `event_guidance_enabled` | 6 | `08/md/x4ep1_mentor_subscription.xml` | Event guidance enabled (Attribute: cue). |
| `event_inventory_added` | 13 | `08/md/story_research_xen_equipment.xml` | Event inventory added (Attribute: object). |
| `event_inventory_removed` | 4 | `08/md/rml_craft_item.xml` | Event inventory removed (Attribute: object). |
| `event_job_ship_activated` | 2 | `extensions/ego_dlc_terran/ext_03/md/story_terran_core.xml` | Event job ship activated. |
| `event_lasertower_launched` | 2 | `08/md/rml_deployinplace.xml` | Event lasertower launched (Attribute: space). |
| `event_lock_acquired` | 1 | `08/aiscripts/interrupt.missilelock.xml` | Event lock acquired (Attribute: target). |
| `event_lock_initiated` | 2 | `08/aiscripts/interrupt.missilelock.xml` | Event lock initiated (Attribute: target). |
| `event_lockbox_opened` | 2 | `08/md/scenario_tutorials.xml` | Event lockbox opened (Attribute: object). |
| `event_long_range_scan_ping` | 11 | `extensions/ego_dlc_terran/ext_03/md/story_yaki.xml` | Event long range scan ping (Attribute: group). |
| `event_long_range_scan_sent` | 6 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Event long range scan sent (Attribute: group). |
| `event_masstraffic_ship_removed` | 4 | `08/aiscripts/order.move.recon.xml` | Event masstraffic ship removed (Attribute: object). |
| `event_mine_launched` | 2 | `08/md/rml_deployinplace.xml` | Event mine launched (Attribute: space). |
| `event_mission_aborted` | 106 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Event mission aborted (Attribute: cue). |
| `event_navbeacon_launched` | 5 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Event navbeacon launched (Attribute: space). |
| `event_npc_created` | 2 | `08/md/scenario_tutorials.xml` | Event npc created. |
| `event_npc_slots_validated` | 6 | `08/md/gm_transport_passengers.xml` | Event npc slots validated (Attribute: object, check). |
| `event_npc_walk_finished` | 2 | `08/md/npc_state_machines.xml` | Event npc walk finished (Attribute: object). |
| `event_object_abandoned` | 37 | `08/aiscripts/order.fight.escort.xml` | Event object abandoned (Attribute: object, check). |
| `event_object_activated_weapon` | 1 | `08/aiscripts/fight.attack.object.bigtarget.xml` | Event object activated weapon (Attribute: object). |
| `event_object_approaching_waypoint` | 11 | `08/aiscripts/boarding.pod.xml` | Event object approaching waypoint (Attribute: object). |
| `event_object_arrived_at_waypoint` | 4 | `08/md/factiongoal_patrolcoordinationservice.xml` | Event object arrived at waypoint (Attribute: object). |
| `event_object_attacked` | 102 | `08/aiscripts/fight.attack.object.capital.xml` | Event object attacked (Attribute: object). |
| `event_object_attacked_object` | 20 | `08/aiscripts/mining.collect.ship.capital.xml` | Event object attacked object (Attribute: object, attacked). |
| `event_object_bomb_attached` | 4 | `extensions/ego_dlc_terran/ext_03/md/story_yaki.xml` | Event object bomb attached (Attribute: object). |
| `event_object_build_storage_moved` | 1 | `08/aiscripts/order.build.deploy.xml` | Event object build storage moved (Attribute: object, check). |
| `event_object_built_ship` | 1 | `extensions/ego_dlc_terran/ext_03/md/story_yaki.xml` | Event object built ship (Attribute: group). |
| `event_object_built_station` | 1 | `08/aiscripts/build.buildstorage.xml` | Event object built station (Attribute: object). |
| `event_object_changed_assignment` | 10 | `08/aiscripts/order.fight.escort.xml` | Event object changed assignment (Attribute: object). |
| `event_object_changed_attention` | 76 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Event object changed attention (Attribute: object). |
| `event_object_changed_cluster` | 23 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Event object changed cluster (Attribute: object). |
| `event_object_changed_contested_state` | 1 | `08/md/factionlogic.xml` | Event object changed contested state (Attribute: group, contested). |
| `event_object_changed_object` | 23 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Event object changed object (Attribute: object). |
| `event_object_changed_owner` | 49 | `08/md/rml_barterwares.xml` | Event object changed owner (Attribute: object, previous). |
| `event_object_changed_room` | 54 | `08/md/scenario_combat.xml` | Event object changed room (Attribute: object). |
| `event_object_changed_sector` | 165 | `08/aiscripts/fight.attack.object.capital.xml` | Event object changed sector (Attribute: object). |
| `event_object_changed_state` | 1 | `08/md/npc_state_machines.xml` | Event object changed state (Attribute: object, state). |
| `event_object_changed_subordinategroup` | 1 | `08/aiscripts/order.fight.tactical.xml` | Event object changed subordinategroup (Attribute: object). |
| `event_object_changed_true_owner` | 82 | `08/md/gm_ambush.xml` | Event object changed true owner (Attribute: group, owner). |
| `event_object_changed_zone` | 82 | `08/aiscripts/fight.attack.object.capital.xml` | Event object changed zone (Attribute: object). |
| `event_object_claimed` | 2 | `extensions/ego_dlc_terran/ext_03/md/story_yaki.xml` | Event object claimed (Attribute: claimed). |
| `event_object_collected_ware` | 2 | `08/md/rml_harvest_resources.xml` | Event object collected ware (Attribute: group). |
| `event_object_collided` | 5 | `08/aiscripts/masstraffic.watchdog.xml` | Event object collided (Attribute: object, comment). |
| `event_object_commander_set` | 6 | `08/aiscripts/order.fight.escort.xml` | Event object commander set (Attribute: group). |
| `event_object_construction_sequence_created` | 17 | `extensions/ego_dlc_terran/ext_03/md/story_yaki.xml` | Event object construction sequence created (Attribute: object). |
| `event_object_deactivated_weapon` | 1 | `08/aiscripts/fight.attack.object.bigtarget.xml` | Event object deactivated weapon (Attribute: object). |
| `event_object_defencedronemode_changed` | 2 | `08/aiscripts/fight.attack.object.capital.xml` | Event object defencedronemode changed (Attribute: object). |
| `event_object_defencedrones_armed` | 2 | `08/aiscripts/fight.attack.object.capital.xml` | Event object defencedrones armed (Attribute: object). |
| `event_object_defencedrones_disarmed` | 2 | `08/aiscripts/fight.attack.object.capital.xml` | Event object defencedrones disarmed (Attribute: object). |
| `event_object_destroyed` | 670 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Event object destroyed (Attribute: object). |
| `event_object_dismantled_object` | 1 | `08/aiscripts/order.salvage.crush.xml` | Event object dismantled object (Attribute: object). |
| `event_object_dock_assigned` | 12 | `08/aiscripts/order.fight.escort.xml` | Event object dock assigned (Attribute: object). |
| `event_object_dock_assigned_at` | 1 | `08/md/npc_instantiation.xml` | Event object dock assigned at (Attribute: group). |
| `event_object_dock_too_far` | 1 | `08/md/notifications.xml` | Event object dock too far (Attribute: group). |
| `event_object_dock_unassigned` | 1 | `08/aiscripts/order.dock.xml` | Event object dock unassigned (Attribute: object). |
| `event_object_dock_unassigned_from` | 2 | `08/aiscripts/build.shiptrader.xml` | Event object dock unassigned from (Attribute: container, comment). |
| `event_object_docked` | 62 | `08/md/rml_barterwares.xml` | Event object docked (Attribute: object). |
| `event_object_docked_at` | 32 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Event object docked at (Attribute: container). |
| `event_object_docking_aborted` | 2 | `08/aiscripts/order.rescue.ship.xml` | Event object docking aborted (Attribute: object). |
| `event_object_docking_denied` | 5 | `08/aiscripts/order.fight.escort.xml` | Event object docking denied (Attribute: object). |
| `event_object_docking_impossible` | 3 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Event object docking impossible (Attribute: group). |
| `event_object_docking_queued` | 1 | `08/md/notifications.xml` | Event object docking queued (Attribute: group). |
| `event_object_docking_started` | 5 | `08/md/cinematiccamera.xml` | Event object docking started (Attribute: object). |
| `event_object_dropped_objects` | 19 | `08/aiscripts/fight.attack.object.station.xml` | Event object dropped objects (Attribute: object). |
| `event_object_drops_found` | 1 | `08/aiscripts/order.plunder.xml` | Event object drops found (Attribute: object). |
| `event_object_enemy_found` | 13 | `08/aiscripts/fight.attack.object.capital.xml` | Event object enemy found (Attribute: object, comment). |
| `event_object_entered` | 7 | `extensions/ego_dlc_terran/ext_03/md/story_yaki.xml` | Event object entered (Attribute: space). |
| `event_object_entered_anomaly` | 1 | `08/aiscripts/interrupt.changedsector.xml` | Event object entered anomaly (Attribute: object). |
| `event_object_entered_gate` | 2 | `08/aiscripts/interrupt.changedsector.xml` | Event object entered gate (Attribute: object). |
| `event_object_entered_live_view` | 1 | `08/md/scenario_tutorials.xml` | Event object entered live view (Attribute: group). |
| `event_object_formation_update_failed` | 2 | `08/aiscripts/order.fight.escort.xml` | Event object formation update failed (Attribute: object). |
| `event_object_formation_update_succeeded` | 2 | `08/aiscripts/order.fight.escort.xml` | Event object formation update succeeded (Attribute: object). |
| `event_object_hull_above_function_threshold` | 22 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Event object hull above function threshold (Attribute: object, check). |
| `event_object_hull_below_function_threshold` | 26 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Event object hull below function threshold (Attribute: object, check). |
| `event_object_hull_damaged` | 13 | `08/md/scenario_combat.xml` | Event object hull damaged (Attribute: group). |
| `event_object_hull_repaired` | 8 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Event object hull repaired (Attribute: group). |
| `event_object_incoming_missile` | 8 | `08/aiscripts/fight.attack.object.capital.xml` | Event object incoming missile (Attribute: object). |
| `event_object_interiors_despawning` | 29 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Event object interiors despawning (Attribute: object). |
| `event_object_killed_object` | 6 | `08/md/setup.xml` | Event object killed object (Attribute: group). |
| `event_object_known_to_player` | 5 | `08/md/placedobjects.xml` | Event object known to player (Attribute: object). |
| `event_object_launched_lasertower` | 2 | `08/aiscripts/order.deploy.staticdefensestrategy.xml` | Event object launched lasertower (Attribute: object). |
| `event_object_launched_mine` | 2 | `08/aiscripts/order.deploy.staticdefensestrategy.xml` | Event object launched mine (Attribute: object). |
| `event_object_launched_missile` | 2 | `08/aiscripts/fight.attack.object.fighter.xml` | Event object launched missile (Attribute: object). |
| `event_object_launched_resourceprobe` | 1 | `08/md/scenario_tutorials.xml` | Event object launched resourceprobe (Attribute: group). |
| `event_object_launched_satellite` | 3 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Event object launched satellite (Attribute: object). |
| `event_object_left` | 3 | `08/md/rml_deployinplace.xml` | Event object left (Attribute: group). |
| `event_object_left_live_view` | 4 | `08/aiscripts/order.fight.lasertower.xml` | Event object left live view (Attribute: object, check). |
| `event_object_miningdronemode_changed` | 1 | `08/aiscripts/fight.attack.object.capital.xml` | Event object miningdronemode changed (Attribute: object). |
| `event_object_miningdrones_armed` | 3 | `08/aiscripts/fight.attack.object.capital.xml` | Event object miningdrones armed (Attribute: object). |
| `event_object_miningdrones_disarmed` | 1 | `08/aiscripts/fight.attack.object.capital.xml` | Event object miningdrones disarmed (Attribute: object). |
| `event_object_money_updated` | 1 | `08/aiscripts/trade.station.xml` | Event object money updated (Attribute: object). |
| `event_object_moved_into_internal_storage` | 2 | `08/aiscripts/order.dock.xml` | Event object moved into internal storage (Attribute: object). |
| `event_object_order_cancelled` | 14 | `08/aiscripts/orders.base.xml` | Event object order cancelled (Attribute: object, immediate). |
| `event_object_order_finished` | 11 | `extensions/ego_dlc_terran/ext_03/md/story_yaki.xml` | Event object order finished (Attribute: object). |
| `event_object_order_param_edited` | 1 | `08/aiscripts/order.fight.tactical.xml` | Event object order param edited (Attribute: object). |
| `event_object_order_ready` | 14 | `08/aiscripts/orders.base.xml` | Event object order ready (Attribute: object, order). |
| `event_object_order_syncpoint_released` | 2 | `08/aiscripts/orders.base.xml` | Event object order syncpoint released (Attribute: object). |
| `event_object_picked_up` | 2 | `08/aiscripts/drone.pickup.xml` | Event object picked up (Attribute: object). |
| `event_object_picked_up_object` | 1 | `08/md/gmc_supervised_mining.xml` | Event object picked up object (Attribute: group). |
| `event_object_processingmodule_available` | 1 | `08/aiscripts/order.salvage.deliver.xml` | Event object processingmodule available (Attribute: object). |
| `event_object_production_finished` | 1 | `08/md/factionlogic_economy.xml` | Event object production finished (Attribute: group). |
| `event_object_props_despawning` | 3 | `08/md/gm_transport_passengers.xml` | Event object props despawning (Attribute: object). |
| `event_object_relation_range_changed` | 11 | `08/aiscripts/fight.attack.object.capital.xml` | Event object relation range changed (Attribute: group, faction). |
| `event_object_removed_from_formation` | 2 | `08/aiscripts/order.fight.escort.xml` | Event object removed from formation (Attribute: object). |
| `event_object_retrieved_from_internal_storage` | 1 | `08/md/lib_generic.xml` | Event object retrieved from internal storage (Attribute: object). |
| `event_object_salvage_claim_lost` | 1 | `08/aiscripts/order.salvage.crush.xml` | Event object salvage claim lost (Attribute: object). |
| `event_object_shield_damaged` | 8 | `08/md/scenario_combat.xml` | Event object shield damaged (Attribute: group). |
| `event_object_signalled` | 340 | `08/aiscripts/move.park.xml` | Event object signalled (Attribute: object, param). |
| `event_object_started_to_dock_at` | 1 | `08/md/npc_state_machines.xml` | Event object started to dock at (Attribute: container). |
| `event_object_started_to_undock_from` | 1 | `08/md/npc_state_machines.xml` | Event object started to undock from (Attribute: container). |
| `event_object_subordinate_added` | 6 | `08/aiscripts/fight.attack.object.station.xml` | Event object subordinate added (Attribute: object). |
| `event_object_subordinate_promoted` | 3 | `extensions/ego_dlc_terran/ext_03/md/story_terran_core.xml` | Event object subordinate promoted (Attribute: group). |
| `event_object_subordinate_removed` | 1 | `08/aiscripts/order.fight.tactical.xml` | Event object subordinate removed (Attribute: object). |
| `event_object_target_invalid` | 8 | `08/aiscripts/move.park.xml` | Event object target invalid (Attribute: object). |
| `event_object_took_area_damage` | 1 | `08/md/notifications.xml` | Event object took area damage (Attribute: group). |
| `event_object_towed_recyclable_near_furnace` | 1 | `08/aiscripts/order.salvage.deliver.xml` | Event object towed recyclable near furnace (Attribute: object). |
| `event_object_transportdronemode_changed` | 1 | `08/aiscripts/fight.attack.object.capital.xml` | Event object transportdronemode changed (Attribute: object). |
| `event_object_transportdrones_armed` | 1 | `08/aiscripts/fight.attack.object.capital.xml` | Event object transportdrones armed (Attribute: object). |
| `event_object_transportdrones_disarmed` | 1 | `08/aiscripts/fight.attack.object.capital.xml` | Event object transportdrones disarmed (Attribute: object). |
| `event_object_triggered` | 1 | `08/md/rml_race_timetrial.xml` | Event object triggered (Attribute: object). |
| `event_object_undocked` | 24 | `08/md/scenario_combat.xml` | Event object undocked (Attribute: group). |
| `event_object_undocked_from` | 14 | `extensions/ego_dlc_terran/ext_03/md/gs_terran2.xml` | Event object undocked from (Attribute: container). |
| `event_object_undocking_cleared` | 1 | `08/aiscripts/move.undock.xml` | Event object undocking cleared (Attribute: object). |
| `event_object_undocking_started` | 3 | `08/md/scenario_combat.xml` | Event object undocking started (Attribute: group). |
| `event_object_weapon_ammo_changed` | 1 | `08/md/scenario_tutorials.xml` | Event object weapon ammo changed (Attribute: group). |
| `event_object_weaponmode_changed` | 6 | `08/aiscripts/fight.attack.object.capital.xml` | Event object weaponmode changed (Attribute: object). |
| `event_offer_accepted` | 1 | `08/md/genericmissions.xml` | Event offer accepted (Attribute: cue). |
| `event_platform_actor_created` | 2 | `08/md/npc_itemtrader.xml` | Event platform actor created. |
| `event_player_activated_cockpit_view` | 3 | `08/md/scenario_tutorials.xml` | Event player activated cockpit view. |
| `event_player_activated_external_target_view` | 1 | `08/md/scenario_tutorials.xml` | Event player activated external target view. |
| `event_player_activated_external_view` | 1 | `08/md/scenario_tutorials.xml` | Event player activated external view. |
| `event_player_activated_floating_view` | 1 | `08/md/scenario_tutorials.xml` | Event player activated floating view. |
| `event_player_activated_platform_trigger` | 1 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Event player activated platform trigger (Attribute: component, group). |
| `event_player_activated_weapon` | 6 | `08/md/scenario_tutorials.xml` | Event player activated weapon. |
| `event_player_activated_weapongroup` | 4 | `08/md/scenario_tutorials.xml` | Event player activated weapongroup (Attribute: primary). |
| `event_player_alert` | 1 | `08/md/notifications.xml` | Event player alert. |
| `event_player_assigned_hired_actor` | 2 | `08/md/conversations.xml` | Event player assigned hired actor. |
| `event_player_attacked_object` | 4 | `08/md/scenario_combat.xml` | Event player attacked object (Attribute: attacked). |
| `event_player_blueprint_added` | 10 | `08/md/tutorial_stations_shipyard.xml` | Event player blueprint added (Attribute: ware, comment). |
| `event_player_bomb_attached` | 12 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Event player bomb attached. |
| `event_player_boost_charging_started` | 1 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Event player boost charging started. |
| `event_player_boost_started` | 5 | `08/md/scenario_combat.xml` | Event player boost started. |
| `event_player_boost_stopped` | 3 | `08/md/scenario_advanced.xml` | Event player boost stopped. |
| `event_player_build_added` | 1 | `08/md/lib_generic.xml` | Event player build added (Attribute: container). |
| `event_player_build_finished` | 3 | `08/md/tutorial_stations_shipyard.xml` | Event player build finished. |
| `event_player_build_finished_components` | 10 | `08/md/upkeep.xml` | Event player build finished components (Attribute: comment). |
| `event_player_build_plot_changed` | 1 | `08/md/rml_buildstation.xml` | Event player build plot changed (Attribute: comment). |
| `event_player_build_started` | 2 | `08/md/story_ventures.xml` | Event player build started. |
| `event_player_built_ship` | 2 | `08/md/notifications.xml` | Event player built ship. |
| `event_player_built_station` | 2 | `08/md/inituniverse.xml` | Event player built station. |
| `event_player_changed_activity` | 21 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Event player changed activity (Attribute: activity). |
| `event_player_changed_target` | 24 | `08/aiscripts/fight.attack.object.capital.xml` | Event player changed target. |
| `event_player_collect_ware_failed` | 1 | `08/md/notifications.xml` | Event player collect ware failed. |
| `event_player_collected_ammo` | 4 | `extensions/ego_dlc_terran/ext_03/md/story_yaki.xml` | Event player collected ammo (Attribute: macro). |
| `event_player_collected_ware` | 5 | `08/md/scenario_tutorials.xml` | Event player collected ware. |
| `event_player_commission_added` | 1 | `08/md/notifications.xml` | Event player commission added. |
| `event_player_crafted_ammo` | 1 | `08/md/notifications.xml` | Event player crafted ammo. |
| `event_player_created_signal_leaks` | 6 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Event player created signal leaks. |
| `event_player_cycled_active_weapon_ammo` | 1 | `08/md/scenario_tutorials.xml` | Event player cycled active weapon ammo. |
| `event_player_detected_object` | 1 | `08/md/scenario_tutorials.xml` | Event player detected object. |
| `event_player_discount_added` | 1 | `08/md/notifications.xml` | Event player discount added. |
| `event_player_discovered_mission_offer` | 1 | `08/md/genericmissions.xml` | Event player discovered mission offer (Attribute: cue). |
| `event_player_discovered_object` | 5 | `08/md/scenario_tutorials.xml` | Event player discovered object. |
| `event_player_ejected` | 2 | `08/md/notifications.xml` | Event player ejected. |
| `event_player_ejecting` | 1 | `08/md/notifications.xml` | Event player ejecting. |
| `event_player_entered_anomaly` | 3 | `08/md/x4ep1_mentor_subscription.xml` | Event player entered anomaly (Attribute: exit). |
| `event_player_entered_gate` | 1 | `08/md/story_diplomacy_intro.xml` | Event player entered gate. |
| `event_player_fired_empty_weapon_group` | 2 | `08/md/tutorial_global.xml` | Event player fired empty weapon group. |
| `event_player_hacked_object` | 3 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Event player hacked object. |
| `event_player_influence_updated` | 1 | `08/md/diplomacy.xml` | Event player influence updated. |
| `event_player_interaction` | 23 | `08/md/rml_barterwares.xml` | Event player interaction (Attribute: param, param2). |
| `event_player_killed_object` | 9 | `08/md/gm_killmasstraffic.xml` | Event player killed object. |
| `event_player_launched_missile` | 1 | `08/md/scenario_tutorials.xml` | Event player launched missile. |
| `event_player_licence_added` | 6 | `08/md/tutorial_stations_shipyard.xml` | Event player licence added (Attribute: licence, comment). |
| `event_player_lost_volatile_wares` | 1 | `08/md/notifications.xml` | Event player lost volatile wares. |
| `event_player_money_updated` | 3 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Event player money updated. |
| `event_player_opened_crate` | 7 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Event player opened crate. |
| `event_player_opened_lockbox` | 1 | `08/md/notifications.xml` | Event player opened lockbox. |
| `event_player_out_of_ammo` | 1 | `08/md/notifications.xml` | Event player out of ammo. |
| `event_player_owned_attacked` | 2 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Event player owned attacked. |
| `event_player_owned_attacked_object` | 2 | `08/md/story_diplomacy_intro.xml` | Event player owned attacked object. |
| `event_player_owned_destroyed` | 2 | `08/md/notifications.xml` | Event player owned destroyed. |
| `event_player_owned_dropped_objects` | 2 | `08/md/scenario_tutorials.xml` | Event player owned dropped objects. |
| `event_player_owned_killed_object` | 1 | `08/md/rml_destroy_rarelyonsight.xml` | Event player owned killed object (Attribute: comment). |
| `event_player_owned_money_updated` | 2 | `08/md/scenario_tutorials.xml` | Event player owned money updated. |
| `event_player_paid_build_plot_changed` | 3 | `08/md/rml_buildstation.xml` | Event player paid build plot changed. |
| `event_player_production_cancelled` | 8 | `08/md/x4ep1_mentor_subscription.xml` | Event player production cancelled (Attribute: research). |
| `event_player_production_finished` | 7 | `08/md/x4ep1_mentor_subscription.xml` | Event player production finished (Attribute: research). |
| `event_player_production_started` | 8 | `08/md/x4ep1_mentor_subscription.xml` | Event player production started (Attribute: research). |
| `event_player_recyclable_processed` | 1 | `08/md/notifications.xml` | Event player recyclable processed. |
| `event_player_recyclable_processing_started` | 1 | `08/md/notifications.xml` | Event player recyclable processing started. |
| `event_player_relation_changed` | 29 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_war_terran.xml` | Event player relation changed (Attribute: faction). |
| `event_player_repaired_object` | 1 | `08/md/rml_repairobject.xml` | Event player repaired object. |
| `event_player_repaired_signal_leak` | 40 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Event player repaired signal leak. |
| `event_player_research_unlocked` | 7 | `08/md/story_research_xen_equipment.xml` | Event player research unlocked (Attribute: ware). |
| `event_player_ship_hit` | 2 | `08/md/npc_usecases.xml` | Event player ship hit (Attribute: comment). |
| `event_player_signal_unlock_failed` | 5 | `08/md/tutorial_modes.xml` | Event player signal unlock failed. |
| `event_player_signal_unlock_finished` | 53 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Event player signal unlock finished. |
| `event_player_signal_unlock_impossible` | 6 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Event player signal unlock impossible. |
| `event_player_signal_unlock_started` | 3 | `08/md/tutorial_modes.xml` | Event player signal unlock started. |
| `event_player_started_control` | 21 | `08/md/rml_barterwares.xml` | Event player started control. |
| `event_player_stopped_control` | 17 | `08/md/rml_barterwares.xml` | Event player stopped control. |
| `event_player_teleport_successful` | 25 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Event player teleport successful (Attribute: comment). |
| `event_player_toggled_cockpit` | 2 | `08/md/scenario_tutorials.xml` | Event player toggled cockpit. |
| `event_player_towed_recyclable_near_furnace` | 1 | `08/md/notifications.xml` | Event player towed recyclable near furnace. |
| `event_player_trade_completed` | 2 | `08/md/rml_largesupply.xml` | Event player trade completed. |
| `event_player_travelmode_charge_aborted` | 1 | `08/md/scenario_tutorials.xml` | Event player travelmode charge aborted. |
| `event_player_travelmode_charge_started` | 6 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Event player travelmode charge started. |
| `event_player_travelmode_started` | 10 | `08/md/scenario_combat.xml` | Event player travelmode started. |
| `event_player_travelmode_stopped` | 4 | `08/md/scenario_combat.xml` | Event player travelmode stopped. |
| `event_player_unlocked_platform_trigger` | 3 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Event player unlocked platform trigger (Attribute: component, group). |
| `event_player_warning` | 1 | `08/md/notifications.xml` | Event player warning. |
| `event_region_asteroid_mined` | 1 | `08/md/khaak_activity.xml` | Event region asteroid mined (Attribute: group). |
| `event_resourceprobe_launched` | 5 | `08/md/rml_deployinplace.xml` | Event resourceprobe launched (Attribute: space). |
| `event_satellite_launched` | 8 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Event satellite launched (Attribute: space). |
| `event_scan_aborted` | 2 | `08/md/scenario_tutorials.xml` | Event scan aborted (Attribute: scanner, scanned). |
| `event_scan_finished` | 10 | `08/aiscripts/order.fight.lasertower.xml` | Event scan finished (Attribute: scanned). |
| `event_scan_started` | 1 | `08/md/scenario_tutorials.xml` | Event scan started (Attribute: scanner, scanned). |
| `event_sector_resource_depleted` | 2 | `08/md/khaak_activity.xml` | Event sector resource depleted (Attribute: sector, check). |
| `event_space_reservation_expired` | 2 | `08/aiscripts/interrupt.lostreservation.xml` | Event space reservation expired (Attribute: object, check). |
| `event_speak_finished` | 418 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Event speak finished (Attribute: actor, line, comment). |
| `event_speak_line_finished` | 8 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Event speak line finished (Attribute: actor, line, comment). |
| `event_speak_timer_triggered` | 1 | `08/md/npc_usecases.xml` | Event speak timer triggered (Attribute: actor, page, line). |
| `event_station_built` | 2 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Event station built. |
| `event_terraforming_event_started` | 1 | `08/md/terraforming.xml` | Event terraforming event started (Attribute: group, project). |
| `event_terraforming_habitability_changed` | 1 | `08/md/terraforming.xml` | Event terraforming habitability changed (Attribute: group). |
| `event_terraforming_project_available` | 2 | `08/md/terraforming.xml` | Event terraforming project available (Attribute: group). |
| `event_terraforming_project_completed` | 5 | `08/md/terraforming.xml` | Event terraforming project completed (Attribute: group). |
| `event_terraforming_project_failed` | 4 | `08/md/terraforming.xml` | Event terraforming project failed (Attribute: group). |
| `event_terraforming_project_started` | 3 | `08/md/x4ep1_mentor_subscription.xml` | Event terraforming project started (Attribute: cluster). |
| `event_terraforming_project_started_production` | 4 | `08/md/x4ep1_mentor_subscription.xml` | Event terraforming project started production (Attribute: cluster). |
| `event_terraforming_project_succeeded` | 40 | `extensions/ego_dlc_terran/ext_03/md/terraforming.xml` | Event terraforming project succeeded (Attribute: cluster, project). |
| `event_terraforming_stat_added` | 5 | `08/md/terraforming.xml` | Event terraforming stat added (Attribute: group, stat). |
| `event_terraforming_stat_changed` | 28 | `08/md/terraforming.xml` | Event terraforming stat changed (Attribute: group, stat). |
| `event_terraforming_stat_removed` | 5 | `08/md/terraforming.xml` | Event terraforming stat removed (Attribute: group, stat). |
| `event_trade_cancelled` | 5 | `08/aiscripts/order.trade.wareexchange.ship.xml` | Event trade cancelled (Attribute: seller). |
| `event_trade_completed` | 11 | `08/md/rml_barterwares.xml` | Event trade completed (Attribute: seller). |
| `event_trade_started` | 1 | `08/md/rml_trade_wares.xml` | Event trade started (Attribute: tradeoffer, comment). |
| `event_ui_triggered` | 569 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Event ui triggered (Attribute: screen, control). |
| `event_unit_destroyed` | 1 | `08/aiscripts/order.salvage.crush.xml` | Event unit destroyed (Attribute: object). |
| `event_universe_generated` | 3 | `extensions/ego_dlc_terran/ext_03/md/story_terran_core.xml` | Event universe generated. |
| `event_venture_mission_aborted` | 1 | `08/aiscripts/order.wait.venture.xml` | Event venture mission aborted. |
| `event_venture_mission_completed` | 2 | `08/aiscripts/order.wait.venture.xml` | Event venture mission completed. |
| `event_venture_ship_added` | 1 | `08/md/setup.xml` | Event venture ship added. |
| `event_venture_ship_removed` | 1 | `08/md/setup.xml` | Event venture ship removed. |
| `event_weapon_fired` | 10 | `08/md/scenario_combat.xml` | Event weapon fired (Attribute: group). |
| `event_weapon_overheated` | 2 | `08/md/scenario_combat.xml` | Event weapon overheated (Attribute: group). |
| `execute_custom_trade` | 2 | `08/aiscripts/order.plunder.xml` | Execute custom trade (Attribute: ware, amount, seller, buyer, commandaction, sinceversion). |
| `execute_recyclable_trade` | 1 | `08/aiscripts/order.salvage.deliver.xml` | Execute recyclable trade (Attribute: module, tradepartner, trade, result). |
| `execute_trade` | 3 | `08/aiscripts/order.trade.wareexchange.ship.xml` | Execute trade (Attribute: tradeoffer, tradepartner, amount, result, custom). |
| `existing_people` | 10 | `08/aiscripts/move.claim.xml` | Existing people (Attribute: people). |
| `extend_build_plot` | 1 | `08/md/factionlogic_economy.xml` | Extend build plot (Attribute: object, negx, posx, negy, posy, negz, posz). |
| `fade_screen` | 30 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Fade screen (Attribute: fadeout, fadein, realtime). |
| `failed` | 1 | `08/aiscripts/build.shiptrader.xml` | Failed (Attribute: added). |
| `fillamount` | 8 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Fillamount (Attribute: exact). |
| `fillpercent` | 58 | `extensions/ego_dlc_split/ext_03/md/setup_gamestarts.xml` | Fillpercent (Attribute: exact). |
| `find_active_repair_mass_traffic` | 1 | `08/aiscripts/engineer.ai.xml` | Sucht active repair mass traffic (Attribute: object, result). |
| `find_actor_interaction_point` | 1 | `08/md/npc_state_machines.xml` | Sucht actor interaction point (Attribute: posname, rotname, actor, object, slot). |
| `find_asteroid_in_cluster` | 14 | `08/aiscripts/fight.attack.object.capital.xml` | Sucht asteroid in cluster (Attribute: name, cluster, refobject, canpickup, multiple, maxdistance). |
| `find_buy_offer` | 39 | `08/aiscripts/fight.attack.object.station.xml` | Sucht buy offer (Attribute: result, buyer, unbundle, multiple). |
| `find_closest_dockingbay` | 1 | `08/aiscripts/move.autopilot.xml` | Sucht closest dockingbay (Attribute: name, object, ship, allowplayeronly). |
| `find_closest_gravidar_obscuring_position` | 3 | `08/aiscripts/order.fight.patrol.xml` | Sucht closest gravidar obscuring position (Attribute: result, sector). |
| `find_closest_octree_object` | 2 | `08/md/placedobjects.xml` | Sucht closest octree object (Attribute: name, refobject). |
| `find_closest_resource` | 27 | `08/aiscripts/fight.attack.object.capital.xml` | Sucht closest resource (Attribute: wares, zone, position, ware, refobject). |
| `find_closest_station_part` | 1 | `08/aiscripts/masstraffic.watchdog.xml` | Sucht closest station part (Attribute: refobject, station, name). |
| `find_closest_undiscovered_position` | 2 | `08/aiscripts/order.move.recon.xml` | Sucht closest undiscovered position (Attribute: result, sector, range, chance). |
| `find_cluster` | 28 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Sucht cluster (Attribute: name, macro, required, comment). |
| `find_cluster_in_range` | 96 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Sucht cluster in range (Attribute: name, object, mindistance, maxdistance). |
| `find_crate_slot` | 13 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Sucht crate slot (Attribute: name, object, tags, multiple). |
| `find_dockingbay` | 154 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Sucht dockingbay (Attribute: name, object, required). |
| `find_gate` | 38 | `08/aiscripts/order.deployobjectsatgates.xml` | Sucht gate (Attribute: name, space, active, multiple). |
| `find_gravidar_contact` | 32 | `08/aiscripts/fight.attack.object.capital.xml` | Sucht gravidar contact (Attribute: name, object, class, checkoperational, docked, multiple). |
| `find_highway` | 1 | `08/md/lib_generic.xml` | Sucht highway (Attribute: name, space, multiple, excluded). |
| `find_highway_entry_gate` | 6 | `08/md/x4ep1_war_subscriptions.xml` | Sucht highway entry gate (Attribute: name, superhighwaygate, space, multiple, append). |
| `find_highway_exit_gate` | 2 | `08/md/lib_generic.xml` | Sucht highway exit gate (Attribute: name, superhighwaygate, active, space, multiple, append). |
| `find_inventoryworkbench_slot` | 1 | `08/md/scenario_tutorials.xml` | Sucht inventoryworkbench slot (Attribute: name, object). |
| `find_module` | 8 | `08/aiscripts/lib.target.selection.xml` | Sucht module (Attribute: name, object, checkoperational, indestructible, invulnerable, sortbydistanceto, excluded, multiple, append). |
| `find_npc_slot` | 120 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Sucht npc slot (Attribute: name, object, tags). |
| `find_npc_waypoint` | 76 | `08/md/scenario_combat.xml` | Sucht npc waypoint (Attribute: name, object, tags). |
| `find_object` | 127 | `08/aiscripts/order.deployobjectsatgates.xml` | Sucht object (Attribute: name, space, trueowner, deployablecategory). |
| `find_object_component` | 433 | `extensions/ego_dlc_split/ext_03/md/x4ep1_war_subscriptions.xml` | Sucht object component (Attribute: groupname, object, class, multiple). |
| `find_object_surface` | 17 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Sucht object surface (Attribute: posname, rotname, object, height). |
| `find_player_transporter_slot` | 9 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Sucht player transporter slot (Attribute: name, object). |
| `find_pos_in_mass_traffic_at_time` | 1 | `08/aiscripts/masstraffic.generic.xml` | Sucht pos in mass traffic at time (Attribute: name, object, time, zone). |
| `find_prop_slot` | 2 | `08/md/story_diplomacy_intro.xml` | Sucht prop slot (Attribute: name, room, tags). |
| `find_recyclable_in_cluster` | 2 | `08/aiscripts/order.salvage.routine.xml` | Sucht recyclable in cluster (Attribute: name, cluster, cantow, candismantle, multiple). |
| `find_requested_job_ship` | 2 | `08/md/factionlogic_staticdefense.xml` | Sucht requested job ship (Attribute: name, requester, multiple). |
| `find_resource` | 4 | `08/aiscripts/order.mining.routine.xml` | Sucht resource (Attribute: sector, position, wares, ware, refobject, minamount, useundiscovered). |
| `find_room` | 22 | `08/md/cinematiccamera.xml` | Sucht room (Attribute: name, object, walkable). |
| `find_sector` | 356 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | Sucht sector (Attribute: name, macro, required). |
| `find_sector_in_range` | 45 | `08/aiscripts/lib.find.sectors.inrange.xml` | Sucht sector in range (Attribute: distances, multiple, object, mindistance, maxdistance, known). |
| `find_sell_offer` | 23 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Sucht sell offer (Attribute: tradepartner, wares, space, result, multiple, usereservations). |
| `find_ship` | 131 | `08/md/gm_board_ship.xml` | Sucht ship (Attribute: name, space, macro). |
| `find_ship_by_true_owner` | 97 | `08/md/gm_ambush.xml` | Sucht ship by true owner (Attribute: name, groupname, space, class, primarypurpose, commandeerable, faction, sortbygatedistanceto). |
| `find_signalleak_location` | 33 | `08/md/placedobjects.xml` | Sucht signalleak location (Attribute: name, container). |
| `find_station` | 294 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | Sucht station (Attribute: name, space, multiple). |
| `find_station_by_true_owner` | 218 | `extensions/ego_dlc_split/ext_03/md/x4ep1_war_subscriptions.xml` | Sucht station by true owner (Attribute: name, space, faction, defencestation, multiple, sortbydistanceto). |
| `find_tradeoffer_parking_slot` | 5 | `08/aiscripts/move.park.xml` | Sucht tradeoffer parking slot (Attribute: name, object, includeoccupied). |
| `find_waiting_job_ship` | 2 | `08/md/job_helper.xml` | Sucht waiting job ship (Attribute: name, owner, hasbuildingtask, multiple, append). |
| `find_waiting_subordinate` | 1 | `08/md/job_helper.xml` | Sucht waiting subordinate (Attribute: name, owner, hasbuildingtask, multiple). |
| `find_zone` | 110 | `08/md/gm_ambush.xml` | Sucht zone (Attribute: name, space). |
| `flicker_object_lights` | 19 | `08/md/x4ep1_mentor_subscription.xml` | Flicker object lights (Attribute: object, duration, strength, range). |
| `force` | 120 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Force (Attribute: name). |
| `force_cue` | 86 | `08/md/gm_ambush.xml` | Force cue (Attribute: cue). |
| `force_player_speed` | 19 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | Force player speed (Attribute: speed). |
| `generate_loadout` | 68 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Generate loadout (Attribute: macro, macros, result, flags). |
| `generate_shortage_reports` | 10 | `08/aiscripts/order.mining.routine.xml` | Generate shortage reports (Attribute: object, type, relevantwares). |
| `get_attackstrength` | 10 | `08/aiscripts/fight.attack.object.capital.xml` | Gibt attackstrength zurück (Attribute: object, target, allowanyturret, usedrones, useforwardweapons). |
| `get_building_position` | 4 | `08/aiscripts/move.buildership.xml` | Gibt building position zurück (Attribute: name, object, macro, space). |
| `get_character_definition` | 36 | `extensions/ego_dlc_split/ext_03/md/terraforming.xml` | Gibt character definition zurück (Attribute: macro, faction, tags). |
| `get_closest_highway_offset` | 2 | `08/md/lib_create_ships.xml` | Gibt closest highway offset zurück (Attribute: highway, result, space). |
| `get_construction_plan` | 8 | `08/md/factionlogic_stations.xml` | Gibt construction plan zurück (Attribute: result, rawname, faction, tags, multiple). |
| `get_control_entities` | 7 | `08/aiscripts/order.fight.lasertower.xml` | Gibt control entities zurück (Attribute: groupname, object). |
| `get_crew_exchange_lists` | 1 | `08/aiscripts/order.trade.crewexchange.xml` | Gibt crew exchange lists zurück (Attribute: object, trade). |
| `get_docking_approach_pos` | 2 | `08/aiscripts/move.flee.dock.xml` | Gibt docking approach pos zurück (Attribute: position, rotation, dock, ship). |
| `get_factions_by_relation` | 27 | `08/md/cinematiccamera.xml` | Gibt factions by relation zurück (Attribute: faction, relation, result). |
| `get_factions_by_tag` | 7 | `08/md/cinematiccamera.xml` | Gibt factions by tag zurück (Attribute: result, tag). |
| `get_floor_position` | 2 | `08/md/story_diplomacy_intro.xml` | Gibt floor position zurück (Attribute: object). |
| `get_gate_approach_pos` | 1 | `08/aiscripts/move.autopilot.xml` | Gibt gate approach pos zurück (Attribute: ship, gate, position, rotation). |
| `get_global_path` | 18 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Gibt global path zurück (Attribute: multiple, component, uselocalhighways). |
| `get_highest_resource_yield` | 30 | `08/md/gm_find_resources.xml` | Gibt highest resource yield zurück (Attribute: result, sector, ware, yieldname, comment). |
| `get_jump_path` | 6 | `08/aiscripts/order.restock.subordinates.xml` | Gibt jump path zurück (Attribute: component, multiple). |
| `get_loadout` | 1 | `08/md/showcases.xml` | Gibt loadout zurück (Attribute: result, loadout, macro). |
| `get_module_definition` | 28 | `08/md/gm_buildstation.xml` | Gibt module definition zurück (Attribute: macro, tags, set, multiple). |
| `get_module_set_macro` | 16 | `08/md/factionlogic_stations.xml` | Gibt module set macro zurück (Attribute: result, race, type, comment). |
| `get_object_value` | 2 | `08/md/job_helper.xml` | Gibt object value zurück (Attribute: result, object, pricetable). |
| `get_regions` | 1 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Gibt regions zurück. |
| `get_resource_gatherrate` | 3 | `08/aiscripts/fight.attack.object.capital.xml` | Gibt resource gatherrate zurück (Attribute: name, refobject, sector, ware). |
| `get_room_definition` | 134 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Gibt room definition zurück (Attribute: macro, tags, race). |
| `get_safe_pos` | 226 | `08/aiscripts/move.park.xml` | Gibt safe pos zurück (Attribute: result, zone, radius, value, ignored, directionobject, angle). |
| `get_satellite_coverage` | 1 | `08/md/rml_achievecoverage.xml` | Gibt satellite coverage zurück (Attribute: result, sector, radius). |
| `get_ship_build_wares` | 1 | `08/md/job_helper.xml` | Gibt ship build wares zurück (Attribute: object, result, otherfaction, requireblueprints, canbuild). |
| `get_ship_definition` | 45 | `08/md/gm_ambush.xml` | Gibt ship definition zurück (Attribute: reference, faction, size, tags). |
| `get_ship_definition_macros` | 2 | `08/md/lib_create_ships.xml` | Gibt ship definition macros zurück (Attribute: id, result). |
| `get_station_definition` | 4 | `08/md/factionlogic_stations.xml` | Gibt station definition zurück (Attribute: macro, faction, tags, multiple). |
| `get_subordinate_jobs` | 3 | `08/aiscripts/order.restock.subordinates.xml` | Gibt subordinate jobs zurück (Attribute: jobs, amount, commander, init). |
| `get_subordinate_macro` | 3 | `08/aiscripts/order.restock.subordinates.xml` | Gibt subordinate macro zurück (Attribute: name, commander, init, multiple). |
| `get_suitable_job` | 27 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | Gibt suitable job zurück (Attribute: result, faction, exceedquota, multiple). |
| `get_suitable_storage_modules` | 1 | `08/md/factionlogic_economy.xml` | Gibt suitable storage modules zurück (Attribute: result, production, storage, macros). |
| `get_threat_score` | 32 | `08/md/factiongoal_invade_space.xml` | Gibt threat score zurück (Attribute: result, class, purpose). |
| `get_trade_parking_pos` | 3 | `08/aiscripts/move.park.xml` | Gibt trade parking pos zurück (Attribute: ship, tradedock, space, approach, position). |
| `get_units_in_mass_traffic` | 1 | `08/aiscripts/engineer.ai.xml` | Gibt units in mass traffic zurück (Attribute: masstraffic, category, amounts). |
| `get_ware_definition` | 43 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | Gibt ware definition zurück (Attribute: result, faction, flags). |
| `get_ware_reservation` | 4 | `08/aiscripts/move.park.xml` | Gibt ware reservation zurück (Attribute: object, type, ware, reserver, result). |
| `get_wares_illegal_to` | 1 | `08/aiscripts/order.trade.routine.xml` | Gibt wares illegal to zurück (Attribute: result, faction). |
| `get_waypoint_path` | 1 | `08/aiscripts/order.dock.xml` | Gibt waypoint path zurück (Attribute: space, tags, start_tags, posname, rotname, group). |
| `get_zone_at_position` | 12 | `08/aiscripts/move.idle.xml` | Gibt zone at position zurück (Attribute: name, sector, value). |
| `get_zone_exit_pos` | 3 | `08/aiscripts/move.nohighway.xml` | Gibt zone exit pos zurück (Attribute: zone, destination, position, rotation, radius). |
| `groups` | 5 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Groups. |
| `handler` | 728 | `08/aiscripts/order.collect.ship.deployable.xml` | Handler (Attribute: ref). |
| `history` | 1 | `08/md/rml_destroy_entities.xml` | History. |
| `icon` | 2 | `08/aiscripts/order.trade.routine.xml` | Icon (Attribute: name, condition). |
| `immediate` | 3 | `extensions/ego_dlc_terran/ext_03/md/story_yaki.xml` | Immediate (Attribute: result). |
| `include_actions` | 1598 | `extensions/ego_dlc_split/ext_03/md/x4ep1_war_subscriptions.xml` | Include actions (Attribute: ref). |
| `include_interrupt_actions` | 221 | `08/aiscripts/fight.attack.object.capital.xml` | Include interrupt actions (Attribute: ref). |
| `init` | 85 | `08/aiscripts/move.park.xml` | Init. |
| `initialise_control_entity` | 3 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Initialise control entity (Attribute: actor). |
| `initialise_terraforming` | 11 | `extensions/ego_dlc_split/ext_03/md/terraforming.xml` | Initialise terraforming (Attribute: cluster, partname). |
| `input_param` | 599 | `08/aiscripts/order.collect.ship.deployable.xml` | Input param (Attribute: name, value). |
| `install_software` | 12 | `extensions/ego_dlc_split/ext_03/md/setup_gamestarts.xml` | Install software (Attribute: object, software). |
| `int` | 3 | `08/md/gm_buildstation.xml` | Int. |
| `interaction` | 19 | `08/md/rml_barterwares.xml` | Interaction (Attribute: text, param, param2). |
| `interpolate_value` | 5 | `08/md/genericmissions.xml` | Interpolate value (Attribute: value, result). |
| `interrupt` | 158 | `08/aiscripts/move.park.xml` | Interrupt. |
| `interrupt_after_time` | 94 | `08/aiscripts/move.park.xml` | Interrupt after time (Attribute: time). |
| `interrupt_speak` | 3 | `extensions/ego_dlc_terran/ext_03/md/gs_terran2.xml` | Interrupt speak (Attribute: actor, priority). |
| `interrupts` | 138 | `08/aiscripts/order.collect.ship.deployable.xml` | Interrupts. |
| `is_in_quadrant` | 25 | `08/aiscripts/fight.attack.object.capital.xml` | Is in quadrant (Attribute: result, object, target, front). |
| `item` | 2 | `08/md/rml_transport_passengers.xml` | Item (Attribute: date, author, description, priority). |
| `label` | 510 | `08/aiscripts/order.collect.ship.xml` | Label (Attribute: name). |
| `launch_countermeasures` | 8 | `08/aiscripts/fight.attack.object.capital.xml` | Launch countermeasures (Attribute: object, virtual). |
| `launch_crew_transfer_pod` | 1 | `08/md/conversations.xml` | Launch crew transfer pod (Attribute: name, object, destination, macro, arrivaltime). |
| `launch_distressdrone` | 2 | `08/aiscripts/interrupt.attacked.xml` | Launch distressdrone (Attribute: name, object, attacker, macro). |
| `launch_drone` | 15 | `08/aiscripts/fight.attack.object.capital.xml` | Launch drone (Attribute: name, object, category, exact). |
| `launch_lasertower` | 2 | `08/aiscripts/move.flee.xml` | Launch lasertower (Attribute: name, object). |
| `launch_masstraffic_drone` | 4 | `08/aiscripts/fight.attack.object.capital.xml` | Launch masstraffic drone (Attribute: name, object, category, pickup, target). |
| `launch_mine` | 3 | `08/aiscripts/order.deployobjectatposition.xml` | Launch mine (Attribute: object, macro). |
| `launch_navbeacon` | 1 | `08/aiscripts/order.deployobjectatposition.xml` | Launch navbeacon (Attribute: object, macro). |
| `launch_repair_drones` | 1 | `08/aiscripts/engineer.ai.xml` | Launch repair drones (Attribute: object, target, components, result). |
| `launch_resourceprobe` | 4 | `08/aiscripts/order.deployobjectatposition.xml` | Launch resourceprobe (Attribute: object, macro). |
| `launch_satellite` | 5 | `08/aiscripts/order.deployobjectatposition.xml` | Launch satellite (Attribute: object, macro). |
| `leave_control_position` | 1 | `08/md/story_research_welfare_1.xml` | Leave control position. |
| `leave_formation` | 35 | `08/aiscripts/order.fight.escort.xml` | Leave formation (Attribute: object). |
| `level` | 171 | `08/md/gm_ambush.xml` | Level (Attribute: exact). |
| `library` | 1242 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Library (Attribute: name). |
| `limits` | 5 | `08/md/factionlogic_economy.xml` | Limits (Attribute: production). |
| `linear` | 15 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Linear (Attribute: x, y, z). |
| `loadout` | 293 | `extensions/ego_dlc_split/ext_03/md/scenario_combat.xml` | Loadout (Attribute: ref). |
| `location` | 63 | `08/aiscripts/order.collect.ship.deployable.xml` | Location (Attribute: condition, object, additionalobjects). |
| `lock_all_firstperson_input` | 2 | `08/md/scenario_tutorials.xml` | Lock all firstperson input. |
| `lock_all_flight_input` | 5 | `08/md/scenario_tutorials.xml` | Lock all flight input. |
| `lock_all_holomap_input` | 3 | `08/md/scenario_tutorials.xml` | Lock all holomap input. |
| `lock_all_shooting_input` | 3 | `08/md/scenario_tutorials.xml` | Lock all shooting input. |
| `lock_flight_strafe_input` | 3 | `08/md/scenario_tutorials.xml` | Lock flight strafe input. |
| `lock_flight_throttle_input` | 5 | `08/md/scenario_tutorials.xml` | Lock flight throttle input. |
| `lock_getup` | 3 | `08/md/scenario_tutorials.xml` | Lock getup. |
| `lock_primary_shooting_input` | 3 | `08/md/scenario_tutorials.xml` | Lock primary shooting input. |
| `lock_secondary_shooting_input` | 1 | `08/md/scenario_tutorials.xml` | Lock secondary shooting input. |
| `macro` | 20 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Macro (Attribute: ref). |
| `macros` | 30 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Macros. |
| `marines` | 2 | `08/md/showcases.xml` | Marines (Attribute: amounts, skills). |
| `match` | 532 | `08/aiscripts/order.collect.ship.deployable.xml` | Match (Attribute: shiptype, negate). |
| `match_any` | 72 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Match any. |
| `match_any_cargo` | 8 | `08/md/gm_scan.xml` | Match any cargo (Attribute: wares). |
| `match_any_wares` | 5 | `08/aiscripts/order.plunder.xml` | Match any wares (Attribute: wares). |
| `match_attention` | 4 | `08/md/placedobjects.xml` | Match attention (Attribute: min, negate). |
| `match_basket_wares` | 1 | `08/md/factionlogic_economy.xml` | Match basket wares (Attribute: wares). |
| `match_buyer` | 12 | `08/aiscripts/order.trade.middleman.xml` | Match buyer (Attribute: tradesknownto). |
| `match_buyoffer` | 1 | `08/md/rml_largesupply.xml` | Match buyoffer (Attribute: wares). |
| `match_cargo` | 1 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Match cargo. |
| `match_child` | 21 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_war_terran.xml` | Match child (Attribute: class, checkoperational, haswalkableroom). |
| `match_content` | 96 | `extensions/ego_dlc_split/ext_03/md/x4ep1_war_subscriptions.xml` | Match content (Attribute: class, state, min). |
| `match_context` | 52 | `08/aiscripts/fight.attack.object.capital.xml` | Match context (Attribute: macro). |
| `match_distance` | 167 | `08/aiscripts/order.deployobjectsatgates.xml` | Match distance (Attribute: value, space, max). |
| `match_dock` | 244 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Match dock (Attribute: size). |
| `match_gate_distance` | 4 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Match gate distance (Attribute: object, min). |
| `match_hull` | 9 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Match hull (Attribute: min). |
| `match_is_in_view_of` | 17 | `08/aiscripts/masstraffic.watchdog.xml` | Match is in view of (Attribute: object, vertical, horizontal). |
| `match_loadout` | 2 | `08/md/lib_generic.xml` | Match loadout (Attribute: wares). |
| `match_parent` | 32 | `08/aiscripts/fight.attack.object.capital.xml` | Match parent (Attribute: class). |
| `match_pilot` | 3 | `08/md/placedobjects.xml` | Match pilot (Attribute: class). |
| `match_products` | 14 | `08/md/npc_shadyguy.xml` | Match products (Attribute: wares, negate). |
| `match_relation_of` | 19 | `08/aiscripts/fight.attack.object.station.xml` | Match relation of (Attribute: faction, relation). |
| `match_relation_to` | 152 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | Match relation to (Attribute: object, relation, comparison). |
| `match_requires_licence` | 2 | `extensions/ego_dlc_terran/ext_03/md/story_terran_core.xml` | Match requires licence (Attribute: requireslicence). |
| `match_resources` | 4 | `08/md/x4ep1_war_subscriptions.xml` | Match resources (Attribute: wares). |
| `match_revealed_percentage` | 5 | `08/md/gm_scan.xml` | Match revealed percentage (Attribute: max). |
| `match_secrecy_level` | 4 | `08/md/gm_scan.xml` | Match secrecy level (Attribute: exact). |
| `match_seller` | 8 | `08/aiscripts/order.trade.middleman.xml` | Match seller (Attribute: tradesknownto). |
| `match_selloffer` | 1 | `08/md/factiongoal_plunder.xml` | Match selloffer (Attribute: wares). |
| `match_shield` | 2 | `08/md/x4ep1_war_subscriptions.xml` | Match shield (Attribute: exact, comment). |
| `match_size` | 1 | `08/aiscripts/masstraffic.watchdog.xml` | Match size (Attribute: max). |
| `match_use_blacklist` | 20 | `08/aiscripts/order.trade.middleman.xml` | Match use blacklist (Attribute: group, type, object). |
| `match_wares` | 1 | `08/aiscripts/fight.attack.object.capital.xml` | Match wares. |
| `matching_people` | 2 | `08/aiscripts/order.transferworkers.xml` | Matching people (Attribute: newroles, races, amounts). |
| `mdscript` | 238 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Mdscript (Attribute: name, xsi, noNamespaceSchemaLocation). |
| `mintotalvolume` | 1 | `08/aiscripts/trade.find.free.xml` | Mintotalvolume (Attribute: max). |
| `missileresult` | 7 | `08/aiscripts/fight.attack.object.capital.xml` | Missileresult (Attribute: ammo, hullshield, hullonly, shieldonly, hullnoshield). |
| `mission` | 5 | `08/md/mc_management.xml` | Mission (Attribute: step, name, type, faction, reward, rewardtext, duration). |
| `mods` | 1 | `08/md/mc_management.xml` | Mods (Attribute: list). |
| `move_docking` | 2 | `08/aiscripts/boarding.pod.return.xml` | Move docking (Attribute: object, dock, flightbehaviour). |
| `move_gate` | 2 | `08/aiscripts/move.gate.xml` | Move gate (Attribute: object, gate, abortpath). |
| `move_navmesh` | 1 | `08/aiscripts/masstraffic.flee.xml` | Move navmesh (Attribute: object, destination, flightbehaviour, finishonapproach, forcesteering). |
| `move_order` | 4 | `08/aiscripts/orders.base.tradecomputer.xml` | Move order (Attribute: order, newindex, result, chance). |
| `move_strafe` | 5 | `08/aiscripts/move.park.xml` | Move strafe (Attribute: object, destination, forcerotation). |
| `move_to` | 157 | `08/aiscripts/move.park.xml` | Move to (Attribute: destination, object). |
| `move_undocking` | 3 | `08/aiscripts/move.undock.xml` | Move undocking (Attribute: object, dock, chance). |
| `move_waypoints` | 4 | `08/aiscripts/move.undock.xml` | Move waypoints (Attribute: object, destination, tags, starttags, finishonapproach, relativemovement, flightbehaviour, forcesteering, commandaction, abortpath). |
| `muffle_sound` | 3 | `08/md/cinematiccamera.xml` | Muffle sound (Attribute: strength, duration). |
| `name` | 28 | `extensions/ego_dlc_terran/ext_03/md/story_terran_core.xml` | Name (Attribute: name). |
| `notify_universe_generated` | 1 | `08/md/finalisestations.xml` | Notify universe generated. |
| `null` | 2 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Null. |
| `objective` | 917 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Objective (Attribute: step, action, object). |
| `offeramount` | 5 | `08/aiscripts/trade.station.xml` | Offeramount (Attribute: tradepartner, min). |
| `offervolume` | 1 | `08/aiscripts/trade.find.free.xml` | Offervolume (Attribute: min, tradepartner). |
| `offset` | 7 | `08/md/placedobjects.xml` | Offset. |
| `offsetrotation` | 11 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Offsetrotation (Attribute: value). |
| `on_abort` | 62 | `08/aiscripts/move.park.xml` | On abort. |
| `on_attentionchange` | 2 | `08/aiscripts/fight.attack.object.capital.xml` | On attentionchange. |
| `open_conversation_menu` | 54 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Open conversation menu (Attribute: menu, param). |
| `open_lockbox` | 1 | `08/aiscripts/order.collect.ship.lockbox.xml` | Open lockbox (Attribute: object, lockbox). |
| `open_menu` | 32 | `08/md/cinematiccamera.xml` | Open menu (Attribute: menu, param). |
| `order` | 85 | `08/aiscripts/order.collect.ship.deployable.xml` | Order (Attribute: id, name, description, category, allowinloop). |
| `order.move.recon` | 7 | `08/aiscripts/order.move.recon.xml` | Order.move.recon. |
| `organise_job_ship_subordinates` | 1 | `08/aiscripts/order.restock.subordinates.xml` | Organise job ship subordinates (Attribute: commander). |
| `orientation` | 69 | `08/aiscripts/move.park.xml` | Orientation (Attribute: orientation, refobject). |
| `owner` | 726 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Owner (Attribute: exact). |
| `page` | 121 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Page (Attribute: exact). |
| `paint` | 56 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Paint (Attribute: ware). |
| `param` | 22067 | `08/aiscripts/order.collect.ship.deployable.xml` | Param (Attribute: name, default, type, text, comment). |
| `params` | 570 | `08/aiscripts/order.collect.ship.deployable.xml` | Params. |
| `patch` | 1903 | `08/aiscripts/order.collect.ship.xml` | Patch (Attribute: sinceversion). |
| `patches` | 13 | `08/md/npc_shadyguy.xml` | Patches. |
| `pause_spacesuit_oxygen` | 2 | `08/md/lib_generic.xml` | Pause spacesuit oxygen (Attribute: object). |
| `people` | 100 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | People (Attribute: ref). |
| `person` | 37 | `extensions/ego_dlc_split/ext_03/md/setup_gamestarts.xml` | Person (Attribute: role). |
| `pickup_target` | 5 | `08/aiscripts/mining.collect.ship.medium.xml` | Pickup target (Attribute: ship, target, prepare). |
| `pilot` | 358 | `08/md/gm_ambush.xml` | Pilot (Attribute: actor). |
| `play_cutscene` | 189 | `08/md/gm_ambush.xml` | Play cutscene (Attribute: key, rendertarget). |
| `play_music` | 46 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Play music (Attribute: music, comment). |
| `play_sound` | 27 | `08/md/scenario_combat.xml` | Play sound (Attribute: sound, object). |
| `position` | 621 | `08/aiscripts/move.park.xml` | Position (Attribute: value). |
| `precache_actor_animation_hint` | 10 | `08/md/npc_state_machines.xml` | Precache actor animation hint (Attribute: actor, type, slot). |
| `precache_hint` | 17 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Precache hint (Attribute: target, includechildren). |
| `predecessor` | 66 | `extensions/ego_dlc_split/ext_03/md/terraforming.xml` | Predecessor (Attribute: id). |
| `predecessors` | 45 | `extensions/ego_dlc_split/ext_03/md/terraforming.xml` | Predecessors. |
| `price` | 6 | `08/aiscripts/order.trade.single.xml` | Price (Attribute: max, tradepartner). |
| `process_build` | 6 | `08/aiscripts/build.shiptrader.xml` | Process build (Attribute: result, build, object, buildprocessor). |
| `process_recyclable_object` | 1 | `08/md/notifications.xml` | Process recyclable object (Attribute: module, object, trade). |
| `progress` | 54 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Progress (Attribute: progress, max). |
| `project` | 5 | `08/md/terraforming.xml` | Project (Attribute: id, group, name, description). |
| `quit_gameover` | 2 | `08/md/scenario_combat.xml` | Quit gameover. |
| `quit_to_game` | 1 | `08/md/scenario_tutorials.xml` | Quit to game (Attribute: game, params). |
| `quit_to_load_latest_save` | 1 | `08/md/scenario_tutorials.xml` | Quit to load latest save. |
| `quit_to_startmenu` | 2 | `08/md/scenario_combat.xml` | Quit to startmenu. |
| `raise_lua_event` | 8 | `08/aiscripts/build.shiptrader.xml` | Raise lua event (Attribute: name). |
| `rangecenter` | 2 | `08/aiscripts/order.move.recon.xml` | Rangecenter (Attribute: object). |
| `recruit_diplomacy_agent` | 1 | `08/md/npc_agent.xml` | Recruit diplomacy agent (Attribute: agent). |
| `refposition` | 16 | `08/aiscripts/order.move.recon.xml` | Refposition (Attribute: value, object, max). |
| `reinitialise_control_entities` | 5 | `08/md/lib_generic.xml` | Reinitialise control entities (Attribute: object). |
| `reinstate_fleet_ship` | 1 | `08/aiscripts/order.move.wait.object.xml` | Reinstate fleet ship (Attribute: object). |
| `relativeprice` | 7 | `08/aiscripts/order.trade.middleman.xml` | Relativeprice (Attribute: min, tradepartner). |
| `release_commandeered_object` | 37 | `08/md/factiongoal_patrolcoordinationservice.xml` | Release commandeered object (Attribute: object). |
| `release_detached_subordinate_group` | 2 | `08/aiscripts/lib.request.orders.xml` | Release detached subordinate group (Attribute: commander, subordinategroupid). |
| `release_npc_template_from_crew_exchange` | 1 | `08/md/conversations.xml` | Release npc template from crew exchange (Attribute: object, template). |
| `remove` | 2 | `extensions/ego_dlc_terran/ext_03/md/scenario_advanced.xml` | Remove (Attribute: sel, name, ware, silent). |
| `remove_actor_from_room` | 49 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Entfernt actor from room (Attribute: actor). |
| `remove_all_cue_actors` | 1 | `08/md/npc_shadyguy.xml` | Entfernt all cue actors (Attribute: cue). |
| `remove_ammo` | 8 | `08/aiscripts/fight.attack.object.capital.xml` | Entfernt ammo (Attribute: object, macro, amount). |
| `remove_anomaly_destination` | 2 | `08/md/story_research_welfare_1.xml` | Entfernt anomaly destination (Attribute: anomaly, destination). |
| `remove_boarding_pod_from_operation` | 2 | `08/md/boarding.xml` | Entfernt boarding pod from operation (Attribute: operation, ship). |
| `remove_build` | 3 | `08/aiscripts/order.build.equip.xml` | Entfernt build (Attribute: object, build). |
| `remove_cargo` | 12 | `extensions/ego_dlc_terran/ext_03/md/story_yaki.xml` | Entfernt cargo (Attribute: object, ware, exact). |
| `remove_cue_actor` | 24 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Entfernt cue actor (Attribute: cue, actor). |
| `remove_docking_request` | 20 | `08/aiscripts/orders.base.xml` | Entfernt docking request (Attribute: ship, container). |
| `remove_dynamic_interior` | 22 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Entfernt dynamic interior (Attribute: interior, object). |
| `remove_effect` | 5 | `08/md/modes.xml` | Entfernt effect (Attribute: object, effect). |
| `remove_encyclopedia_entry` | 3 | `08/md/crisis_xenon_khaak_combo.xml` | Entfernt encyclopedia entry (Attribute: type, item). |
| `remove_from_group` | 320 | `extensions/ego_dlc_split/ext_03/md/x4ep1_war_subscriptions.xml` | Entfernt from group (Attribute: group, object). |
| `remove_from_list` | 289 | `08/aiscripts/order.deployobjectsatgates.xml` | Entfernt from list (Attribute: name, exact). |
| `remove_from_player_squad` | 1 | `08/md/conversations.xml` | Entfernt from player squad (Attribute: object). |
| `remove_help` | 530 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Entfernt help (Attribute: line). |
| `remove_help_overlay` | 447 | `08/md/tutorial_modes.xml` | Entfernt help overlay (Attribute: id). |
| `remove_holomap` | 96 | `08/md/gm_ambush.xml` | Entfernt holomap. |
| `remove_holomap_text` | 4 | `08/md/scenario_tutorials.xml` | Entfernt holomap text (Attribute: object). |
| `remove_inventory` | 34 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Entfernt inventory (Attribute: ware). |
| `remove_job_ship_request` | 5 | `08/md/factionsubgoal_recon.xml` | Entfernt job ship request (Attribute: ship). |
| `remove_licence` | 7 | `08/md/setup.xml` | Entfernt licence (Attribute: faction, type, licencefaction). |
| `remove_mission` | 547 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Entfernt mission (Attribute: cue, type). |
| `remove_npc_template` | 28 | `08/md/rml_transport_passengers_v2.xml` | Entfernt npc template (Attribute: object, template). |
| `remove_object_account` | 6 | `08/aiscripts/interrupt.stoporder.xml` | Entfernt object account (Attribute: object, transfer). |
| `remove_object_commander` | 14 | `08/aiscripts/order.assign.commander.xml` | Entfernt object commander (Attribute: object). |
| `remove_offer` | 125 | `08/md/gm_ambush.xml` | Entfernt offer (Attribute: cue). |
| `remove_overlay_text` | 3 | `08/md/cinematiccamera.xml` | Entfernt overlay text (Attribute: force). |
| `remove_player_discount` | 3 | `08/md/notifications.xml` | Entfernt player discount (Attribute: id, faction). |
| `remove_player_gravidar_access_request` | 4 | `08/md/diplomacy.xml` | Entfernt player gravidar access request (Attribute: object). |
| `remove_representative` | 2 | `08/md/factionlogic.xml` | Entfernt representative (Attribute: faction). |
| `remove_research` | 4 | `08/md/x4ep1_mentor_subscription.xml` | Entfernt research (Attribute: ware). |
| `remove_retrieval_request` | 1 | `08/md/scenario_combat.xml` | Entfernt retrieval request (Attribute: ship). |
| `remove_space_location_tag` | 1 | `08/md/factionlogic.xml` | Entfernt space location tag (Attribute: space, tag). |
| `remove_terraforming_event` | 5 | `08/md/terraforming.xml` | Entfernt terraforming event (Attribute: cluster, id). |
| `remove_terraforming_project` | 6 | `08/md/terraforming.xml` | Entfernt terraforming project (Attribute: cluster, id). |
| `remove_terraforming_stat` | 5 | `08/md/terraforming.xml` | Entfernt terraforming stat (Attribute: cluster, id). |
| `remove_trade_offer` | 16 | `08/md/rml_barterwares.xml` | Entfernt trade offer (Attribute: object, tradeoffer). |
| `remove_tradeware` | 6 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Entfernt tradeware (Attribute: object, ware). |
| `remove_undocking_request` | 2 | `08/aiscripts/move.undock.xml` | Entfernt undocking request (Attribute: ship). |
| `remove_units` | 1 | `08/md/story_paranid.xml` | Entfernt units (Attribute: object, category, mk, exact). |
| `remove_userdata` | 1 | `08/md/scenario_tutorials.xml` | Entfernt userdata (Attribute: name). |
| `remove_value` | 3925 | `08/aiscripts/order.collect.ship.xml` | Entfernt value (Attribute: name). |
| `remove_ware_reservation` | 13 | `08/aiscripts/order.trade.wareexchange.ship.xml` | Entfernt ware reservation (Attribute: object, reserver, ware, amount, virtual, mission). |
| `remove_weapon` | 1 | `08/md/showcases.xml` | Entfernt weapon (Attribute: object, macro). |
| `remove_weapon_from_all_weapongroups` | 2 | `08/md/scenario_tutorials.xml` | Entfernt weapon from all weapongroups (Attribute: weapon). |
| `rename_all_worlds` | 2 | `08/md/story_paranid.xml` | Rename all worlds (Attribute: cluster, page, oldline, newline). |
| `replace` | 829 | `extensions/ego_dlc_split/ext_03/md/scenario_combat.xml` | Replace (Attribute: sel). |
| `report_illegal_activity` | 2 | `08/aiscripts/masstraffic.watchdog.xml` | Report illegal activity (Attribute: object, target). |
| `request_docking` | 11 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Request docking (Attribute: allowplayeronly, ship, container, queuedresult, grantedresult). |
| `request_gate` | 1 | `08/aiscripts/move.gate.xml` | Request gate (Attribute: ship, gate, unlock, result). |
| `request_job_ship` | 10 | `08/md/factionsubgoal_recon.xml` | Request job ship (Attribute: name, job, requester, zone). |
| `request_retrieval` | 6 | `08/md/scenario_combat.xml` | Request retrieval (Attribute: queuedresult, grantedresult, ship). |
| `request_store_ship` | 7 | `08/aiscripts/build.shiptrader.xml` | Request store ship (Attribute: object, size, faction). |
| `request_undocking` | 2 | `08/aiscripts/move.undock.xml` | Request undocking (Attribute: ship, queuedresult, grantedresult, highpriority). |
| `requires` | 79 | `08/aiscripts/order.collect.ship.deployable.xml` | Requires. |
| `reserve_space` | 4 | `08/aiscripts/order.build.deploy.xml` | Reserve space (Attribute: space, component, duration, index, safezone). |
| `reset_adaptive_steering` | 1 | `08/md/scenario_tutorials.xml` | Reset adaptive steering. |
| `reset_avoid_collisions` | 16 | `08/aiscripts/masstraffic.move.waitforsignal.xml` | Reset avoid collisions (Attribute: object). |
| `reset_control_mode_messages` | 1 | `08/md/scenario_tutorials.xml` | Reset control mode messages. |
| `reset_cue` | 1340 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Reset cue (Attribute: cue). |
| `reset_flight_behaviour` | 9 | `08/aiscripts/move.flightbehaviour.xml` | Reset flight behaviour (Attribute: object). |
| `reset_relation_boost` | 43 | `08/aiscripts/fight.attack.object.capital.xml` | Reset relation boost (Attribute: object, otherobject). |
| `reset_weapongroups` | 2 | `08/aiscripts/order.fight.attack.object.xml` | Reset weapongroups (Attribute: object). |
| `resize_list` | 8 | `08/md/factionlogic_economy.xml` | Resize list (Attribute: list, count). |
| `restore_object` | 7 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Restore object (Attribute: object, recursive). |
| `result` | 24 | `08/aiscripts/fight.attack.object.capital.xml` | Result (Attribute: hullshield, hullonly, shieldonly, hullnoshield). |
| `resume` | 872 | `08/aiscripts/order.collect.ship.xml` | Resume (Attribute: label). |
| `return` | 543 | `08/aiscripts/order.collect.ship.xml` | Return (Attribute: value). |
| `return_to_masstraffic` | 7 | `08/aiscripts/masstraffic.watchdog.xml` | Return to masstraffic (Attribute: object). |
| `return_units` | 1 | `08/aiscripts/move.collect.drone.xml` | Return units (Attribute: object, macro). |
| `retval` | 33 | `08/aiscripts/lib.target.selection.xml` | Retval (Attribute: name, value). |
| `reward_player` | 71 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Reward player (Attribute: money). |
| `rotation` | 324 | `08/aiscripts/move.park.xml` | Rotation (Attribute: value). |
| `row` | 10 | `08/md/scenario_combat.xml` | Row (Attribute: fromtop, reloffsety). |
| `run_actions` | 1464 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Run actions (Attribute: ref). |
| `run_interrupt_script` | 5 | `08/aiscripts/masstraffic.handler.attacked.xml` | Run interrupt script (Attribute: name). |
| `run_order_script` | 2 | `08/aiscripts/orders.base.xml` | Run order script (Attribute: order). |
| `run_script` | 324 | `08/aiscripts/order.collect.ship.deployable.xml` | Run script (Attribute: name). |
| `safepos` | 416 | `08/md/gm_ambush.xml` | Safepos (Attribute: value, radius). |
| `save_retval` | 13 | `08/aiscripts/order.fight.attack.inrange.xml` | Save retval (Attribute: name, variable). |
| `select` | 547 | `08/md/gm_ambush.xml` | Select (Attribute: faction, tags). |
| `select_flight_behaviour` | 5 | `08/aiscripts/move.evade.xml` | Select flight behaviour (Attribute: entity, evasive, result). |
| `set_active_mission_waypoint_known` | 1 | `08/md/conversations.xml` | Setzt active mission waypoint known. |
| `set_actor_current_chair` | 6 | `08/md/npc_state_machines.xml` | Setzt actor current chair (Attribute: actor, roomslot). |
| `set_actor_emotion` | 2 | `08/md/npc_usecases.xml` | Setzt actor emotion (Attribute: actor, emotion). |
| `set_actor_lookat` | 11 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Setzt actor lookat (Attribute: actor, component). |
| `set_actor_pod_arrival_time` | 2 | `08/md/conversations.xml` | Setzt actor pod arrival time. |
| `set_actor_roomslot` | 11 | `08/md/npc_state_machines.xml` | Setzt actor roomslot (Attribute: actor, roomslot). |
| `set_actor_tool` | 10 | `08/md/npc_state_machines.xml` | Setzt actor tool (Attribute: actor, name). |
| `set_adaptive_steering_forced` | 1 | `08/md/scenario_tutorials.xml` | Setzt adaptive steering forced. |
| `set_alert_level` | 22 | `08/aiscripts/fight.attack.object.capital.xml` | Setzt alert level (Attribute: object, level). |
| `set_ambient_sound_state` | 4 | `extensions/ego_dlc_terran/ext_03/md/gs_terran2.xml` | Setzt ambient sound state (Attribute: active). |
| `set_avoid_collisions` | 19 | `08/aiscripts/move.park.xml` | Setzt avoid collisions (Attribute: object, bigobjects, smallobjects). |
| `set_boarding_phase` | 1 | `08/md/boarding.xml` | Setzt boarding phase (Attribute: operation, phase). |
| `set_build_plot` | 12 | `08/md/x4ep1_mentor_subscription.xml` | Setzt build plot (Attribute: object, paid, x, y, z). |
| `set_buildanchor` | 2 | `08/aiscripts/build.shiptrader.xml` | Setzt buildanchor (Attribute: object, buildprocessor). |
| `set_cockpit_tint` | 11 | `08/md/modes.xml` | Setzt cockpit tint (Attribute: resettodefault, sethudcolors). |
| `set_command` | 85 | `08/aiscripts/move.park.xml` | Setzt command (Attribute: command, param). |
| `set_command_action` | 90 | `08/aiscripts/move.park.xml` | Setzt command action (Attribute: commandaction). |
| `set_control_mode_messages_disabled` | 1 | `08/md/scenario_tutorials.xml` | Setzt control mode messages disabled. |
| `set_conversation_return_section` | 15 | `08/md/gm_scan.xml` | Setzt conversation return section (Attribute: section). |
| `set_cover_owner` | 30 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Setzt cover owner (Attribute: object). |
| `set_current_loop_order` | 4 | `08/aiscripts/orders.base.tradecomputer.xml` | Setzt current loop order (Attribute: order, check, result). |
| `set_diplomacy_action_hidden` | 9 | `08/md/diplomacy.xml` | Setzt diplomacy action hidden (Attribute: action, hidden). |
| `set_diplomacy_gift_known` | 18 | `08/md/diplomacy.xml` | Setzt diplomacy gift known (Attribute: faction, ware). |
| `set_diplomat` | 1 | `08/md/diplomacy.xml` | Setzt diplomat (Attribute: faction, representative). |
| `set_drone_armed` | 2 | `08/md/scenario_advanced.xml` | Setzt drone armed (Attribute: object, category, armed). |
| `set_drone_mode` | 1 | `08/md/scenario_advanced.xml` | Setzt drone mode (Attribute: object, category, mode). |
| `set_drop_object` | 12 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Setzt drop object (Attribute: object, drop). |
| `set_drop_persistence` | 2 | `08/md/rml_find_object.xml` | Setzt drop persistence (Attribute: object, persistent, comment). |
| `set_dynamic_interior_persistent` | 6 | `08/md/rml_transport_passengers_v2.xml` | Setzt dynamic interior persistent (Attribute: object, interior, persistent). |
| `set_dynamic_interior_private` | 10 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Setzt dynamic interior private (Attribute: object, interior, private). |
| `set_emergency_eject_active` | 5 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Setzt emergency eject active (Attribute: active). |
| `set_entity_overrides` | 96 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Setzt entity overrides (Attribute: entity, title). |
| `set_entity_page` | 2 | `08/md/scenario_combat.xml` | Setzt entity page (Attribute: entity, page). |
| `set_entity_role` | 44 | `08/md/scenario_combat.xml` | Setzt entity role (Attribute: entity, role). |
| `set_entity_role_object` | 42 | `08/md/scenario_combat.xml` | Setzt entity role object (Attribute: entity, object). |
| `set_entity_traits` | 303 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Setzt entity traits (Attribute: entity, missionactor, remote, customhandler). |
| `set_entity_type` | 44 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Setzt entity type (Attribute: entity, type). |
| `set_faction_active` | 8 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Setzt faction active (Attribute: faction, active). |
| `set_faction_diplomacy_active` | 5 | `08/md/terraforming.xml` | Setzt faction diplomacy active (Attribute: faction, active). |
| `set_faction_diplomacy_events_allowed` | 2 | `08/md/diplomacy.xml` | Setzt faction diplomacy events allowed (Attribute: faction, allow). |
| `set_faction_diplomacy_exclusion` | 28 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | Setzt faction diplomacy exclusion (Attribute: faction, otherfaction, flags). |
| `set_faction_headquarters` | 2 | `08/md/factionlogic.xml` | Setzt faction headquarters (Attribute: faction, station, headquarters, comment). |
| `set_faction_identity` | 8 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Setzt faction identity (Attribute: faction, name, description, shortname, prefixname, spacename, homespacename, icon). |
| `set_faction_known` | 134 | `extensions/ego_dlc_split/ext_03/md/setup_gamestarts.xml` | Setzt faction known (Attribute: faction, known). |
| `set_faction_mood` | 2 | `08/md/factionlogic.xml` | Setzt faction mood (Attribute: faction, type, level). |
| `set_faction_police` | 3 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Setzt faction police (Attribute: faction, policefaction). |
| `set_faction_relation` | 98 | `extensions/ego_dlc_split/ext_03/md/setup_gamestarts.xml` | Setzt faction relation (Attribute: faction, otherfaction, value). |
| `set_faction_relation_locked` | 21 | `08/md/scenario_combat.xml` | Setzt faction relation locked (Attribute: faction, locked). |
| `set_fleet_ship_build_issue_flags` | 3 | `08/md/fleet_reconstitution.xml` | Setzt fleet ship build issue flags (Attribute: fleetunit, flags). |
| `set_flight_behaviour` | 8 | `08/aiscripts/masstraffic.watchdog.xml` | Setzt flight behaviour (Attribute: object, flightbehaviour). |
| `set_flight_control_model` | 13 | `08/aiscripts/move.flee.dock.xml` | Setzt flight control model (Attribute: object, flightcontrolmodel). |
| `set_holomap_max_zoom` | 2 | `08/md/scenario_tutorials.xml` | Setzt holomap max zoom (Attribute: value). |
| `set_holomap_target` | 10 | `08/md/scenario_tutorials.xml` | Setzt holomap target (Attribute: object). |
| `set_holomap_zoom` | 16 | `08/md/scenario_tutorials.xml` | Setzt holomap zoom (Attribute: value). |
| `set_job_active` | 112 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | Setzt job active (Attribute: job, activate). |
| `set_job_ship_mainsector` | 2 | `08/aiscripts/order.move.recon.xml` | Setzt job ship mainsector (Attribute: ship, sector). |
| `set_known` | 83 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Setzt known (Attribute: object, known). |
| `set_loadout_level` | 1 | `08/aiscripts/build.shiptrader.xml` | Setzt loadout level (Attribute: object, exact). |
| `set_marine_status` | 3 | `08/md/boarding.xml` | Setzt marine status (Attribute: operation, template, status). |
| `set_module_loadout_level` | 3 | `08/md/finalisestations.xml` | Setzt module loadout level (Attribute: object, exact). |
| `set_npc_template_role` | 5 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Setzt npc template role (Attribute: object, template, role). |
| `set_npc_template_traits` | 5 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Setzt npc template traits (Attribute: object, template, customhandler). |
| `set_object_access_licence` | 2 | `extensions/ego_dlc_terran/ext_03/md/story_terran_core.xml` | Setzt object access licence (Attribute: object, licence). |
| `set_object_account` | 4 | `08/md/scenario_tutorials.xml` | Setzt object account (Attribute: object). |
| `set_object_active` | 50 | `08/aiscripts/masstraffic.watchdog.xml` | Setzt object active (Attribute: object, activate). |
| `set_object_capturable` | 11 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Setzt object capturable (Attribute: object, capturable). |
| `set_object_commander` | 60 | `08/aiscripts/fight.attack.object.capital.xml` | Setzt object commander (Attribute: object, commander). |
| `set_object_description` | 15 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Setzt object description (Attribute: object, page, line). |
| `set_object_docking_enabled` | 26 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Setzt object docking enabled (Attribute: object, enabled). |
| `set_object_encyclopedia_visibility` | 1 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Setzt object encyclopedia visibility (Attribute: object, visible). |
| `set_object_foe_list` | 3 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Setzt object foe list (Attribute: object, factions). |
| `set_object_forced_radar_visible` | 2 | `08/md/x4ep1_mentor_subscription.xml` | Setzt object forced radar visible (Attribute: object, visible). |
| `set_object_hackable` | 1 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Setzt object hackable (Attribute: object, hackable). |
| `set_object_hacked` | 14 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Setzt object hacked (Attribute: object, duration). |
| `set_object_hull` | 97 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Setzt object hull (Attribute: object, min, max, profile). |
| `set_object_hull_unrepairable` | 10 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Setzt object hull unrepairable (Attribute: object, unrepairable). |
| `set_object_long_range_scanned` | 3 | `08/md/scenario_tutorials.xml` | Setzt object long range scanned (Attribute: object, scanned). |
| `set_object_min_hull` | 238 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Setzt object min hull (Attribute: object, exact, comment). |
| `set_object_min_shield` | 39 | `08/md/scenario_combat.xml` | Setzt object min shield (Attribute: object, exact, comment). |
| `set_object_name` | 156 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | Setzt object name (Attribute: object, page, line, comment). |
| `set_object_npc_assignment_restricted` | 14 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Setzt object npc assignment restricted (Attribute: object, restricted). |
| `set_object_radar_visible` | 68 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Setzt object radar visible (Attribute: object, visible). |
| `set_object_relation_behaviour` | 85 | `08/md/scenario_combat.xml` | Setzt object relation behaviour (Attribute: object, disable). |
| `set_object_scanned` | 7 | `extensions/ego_dlc_terran/ext_03/md/story_yaki.xml` | Setzt object scanned (Attribute: object). |
| `set_object_sellable` | 6 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Setzt object sellable (Attribute: object, sellable). |
| `set_object_shield` | 14 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Setzt object shield (Attribute: object, min, max). |
| `set_object_signal_response` | 2 | `08/md/gm_rescue_ship_lib.xml` | Setzt object signal response (Attribute: object, signal, response). |
| `set_object_sound_override` | 5 | `extensions/ego_dlc_terran/ext_03/md/story_yaki.xml` | Setzt object sound override (Attribute: object, volume, type). |
| `set_object_unlock_state` | 3 | `08/md/placedobjects.xml` | Setzt object unlock state (Attribute: object, state). |
| `set_object_velocity` | 3 | `08/md/scenario_tutorials.xml` | Setzt object velocity (Attribute: object). |
| `set_objective` | 1071 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Setzt objective (Attribute: cue, step, action, customaction). |
| `set_objective_from_briefing` | 162 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Setzt objective from briefing (Attribute: cue, step). |
| `set_order_failed` | 104 | `08/aiscripts/order.collect.ship.xml` | Setzt order failed (Attribute: order, text, comment). |
| `set_order_state` | 26 | `08/aiscripts/move.park.xml` | Setzt order state (Attribute: order, state). |
| `set_order_syncpoint_reached` | 28 | `08/aiscripts/order.deployobjectsatgates.xml` | Setzt order syncpoint reached (Attribute: order). |
| `set_owner` | 117 | `08/md/rml_barterwares.xml` | Setzt owner (Attribute: object, faction). |
| `set_player_activity` | 4 | `08/md/modes.xml` | Setzt player activity (Attribute: activity). |
| `set_player_persistent_docking_request` | 1 | `08/aiscripts/order.rescue.ship.xml` | Setzt player persistent docking request (Attribute: persistent). |
| `set_player_target` | 1 | `08/md/scenario_tutorials.xml` | Setzt player target (Attribute: object). |
| `set_playership_throttle` | 13 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Setzt playership throttle (Attribute: value, comment). |
| `set_production_paused` | 5 | `08/md/factionlogic_economy.xml` | Setzt production paused (Attribute: object, paused). |
| `set_region_object_persistence` | 10 | `08/aiscripts/mining.collect.ship.capital.xml` | Setzt region object persistence (Attribute: object). |
| `set_relation_boost` | 196 | `08/md/gm_ambush.xml` | Setzt relation boost (Attribute: object, silent, otherobject, value, decay, delay). |
| `set_requested_job_ship_timeout` | 9 | `08/md/factionsubgoal_recon.xml` | Setzt requested job ship timeout (Attribute: ship, timeout). |
| `set_room_locked` | 13 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Setzt room locked (Attribute: room, locked). |
| `set_ship_expiration_time` | 6 | `08/aiscripts/order.restock.subordinates.xml` | Setzt ship expiration time (Attribute: ship, time). |
| `set_ship_safepos_allowed` | 17 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Setzt ship safepos allowed (Attribute: ship, allow). |
| `set_ship_undocking` | 1 | `08/aiscripts/move.undock.xml` | Setzt ship undocking (Attribute: ship). |
| `set_ship_wares_absolute` | 2 | `extensions/ego_dlc_split/ext_03/md/setup_dlc_split.xml` | Setzt ship wares absolute (Attribute: object, wares). |
| `set_skill` | 43 | `08/md/scenario_tutorials.xml` | Setzt skill (Attribute: entity, type, exact). |
| `set_space_faction_logic_allowed` | 14 | `08/md/setup.xml` | Setzt space faction logic allowed (Attribute: allow, space). |
| `set_spacesuit_oxygen` | 1 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Setzt spacesuit oxygen (Attribute: object, percent). |
| `set_stock_reference` | 4 | `08/md/npc_shadyguy.xml` | Setzt stock reference (Attribute: entity, stock). |
| `set_subordinate_group_assignment` | 4 | `extensions/ego_dlc_terran/ext_03/md/story_terran_core.xml` | Setzt subordinate group assignment (Attribute: object, commander, subordinategroupid, assignment). |
| `set_subordinate_group_protected_position` | 2 | `extensions/ego_dlc_terran/ext_03/md/story_terran_core.xml` | Setzt subordinate group protected position (Attribute: commander, subordinategroupid, value). |
| `set_subordinate_group_protected_sector` | 2 | `extensions/ego_dlc_terran/ext_03/md/story_terran_core.xml` | Setzt subordinate group protected sector (Attribute: commander, subordinategroupid, sector). |
| `set_terraforming_mission_activated` | 8 | `08/md/terraforming.xml` | Setzt terraforming mission activated (Attribute: cluster, missioncue). |
| `set_terraforming_mission_completed` | 15 | `08/md/terraforming.xml` | Setzt terraforming mission completed (Attribute: cluster). |
| `set_terraforming_mission_deactivated` | 8 | `08/md/terraforming.xml` | Setzt terraforming mission deactivated (Attribute: cluster). |
| `set_terraforming_stat` | 69 | `extensions/ego_dlc_split/ext_03/md/terraforming.xml` | Setzt terraforming stat (Attribute: cluster, id, value). |
| `set_to_default_flight_control_model` | 48 | `08/aiscripts/move.evade.xml` | Setzt to default flight control model (Attribute: object). |
| `set_tradeoffers_enabled` | 9 | `08/aiscripts/order.wait.signal.xml` | Setzt tradeoffers enabled (Attribute: object, enabled). |
| `set_trigger_activation_wares` | 6 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Setzt trigger activation wares (Attribute: room, group, ware, amount, consumeonuse). |
| `set_triggers_locked` | 17 | `08/md/scenario_combat.xml` | Setzt triggers locked (Attribute: object, group, locked). |
| `set_turret_targets` | 47 | `08/aiscripts/fight.attack.object.capital.xml` | Setzt turret targets (Attribute: object, target, weaponmode). |
| `set_turrets_armed` | 1 | `08/md/scenario_tutorials.xml` | Setzt turrets armed (Attribute: object, armed). |
| `set_userdata` | 101 | `08/md/scenario_combat.xml` | Setzt userdata (Attribute: name, value). |
| `set_value` | 35134 | `extensions/ego_dlc_split/ext_03/md/factionlogic_stations.xml` | Setzt value (Attribute: name, exact). |
| `set_weapon_mode` | 8 | `08/aiscripts/fight.attack.object.station.xml` | Setzt weapon mode (Attribute: weapon, weaponmode). |
| `set_world_atmosphere` | 6 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Setzt world atmosphere (Attribute: cluster, partname, page, line, comment). |
| `set_world_name` | 10 | `08/md/terraforming.xml` | Setzt world name (Attribute: cluster, partname, page, line, comment). |
| `set_world_population` | 14 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Setzt world population (Attribute: cluster, partname, page, line, amount). |
| `set_world_settlements` | 23 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Setzt world settlements (Attribute: cluster, partname, page, line, comment). |
| `set_wreck_persistence` | 3 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Setzt wreck persistence (Attribute: object, persistent). |
| `shield` | 44 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Shield (Attribute: macro, path). |
| `shields` | 54 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Shields (Attribute: macro, path, group). |
| `ship` | 18 | `extensions/ego_dlc_terran/ext_03/md/story_yaki.xml` | Ship (Attribute: ware). |
| `ships` | 1 | `08/md/rml_deliver_fleet.xml` | Ships (Attribute: list). |
| `shoot` | 2 | `08/md/crisis_xenon_khaak_combo.xml` | Shoot (Attribute: object, primary, secondary). |
| `shoot_at` | 24 | `08/aiscripts/fight.attack.object.capital.xml` | Shoot at (Attribute: object, target, largetarget, additional_targets, fixedtarget). |
| `show_help` | 607 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Show help (Attribute: line, log, position, force, width, duration, comment, allowclose). |
| `show_help_multi` | 145 | `extensions/ego_dlc_terran/ext_03/md/story_yaki.xml` | Show help multi (Attribute: allowclose, position, force). |
| `show_help_overlay` | 376 | `08/md/tutorial_modes.xml` | Show help overlay (Attribute: id, highlightonly). |
| `show_interactive_notification` | 1 | `08/md/notifications.xml` | Show interactive notification (Attribute: caption, text). |
| `show_notification` | 256 | `08/md/gm_ambush.xml` | Show notification (Attribute: text, sound, comment). |
| `show_overlay_text` | 3 | `08/md/scenario_combat.xml` | Show overlay text (Attribute: relwidth, reloffsetx, reloffsety, fadein, fadeout). |
| `shuffle_group` | 19 | `extensions/ego_dlc_split/ext_03/md/x4ep1_war_subscriptions.xml` | Shuffle group (Attribute: group). |
| `shuffle_list` | 326 | `08/aiscripts/order.deployobjectsatgates.xml` | Shuffle list (Attribute: list). |
| `signal_cue` | 4976 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Signal cue (Attribute: cue). |
| `signal_cue_instantly` | 4362 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Signal cue instantly (Attribute: cue, param). |
| `signal_objects` | 549 | `08/aiscripts/order.deployobjectsatgates.xml` | Signal objects (Attribute: object, param, param2, param3, comment). |
| `skill` | 546 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Skill (Attribute: type, min, max). |
| `skills` | 110 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Skills. |
| `software` | 125 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Software. |
| `sort_collectables_by_value` | 1 | `08/aiscripts/order.plunder.xml` | Sort collectables by value (Attribute: name, collectables, object). |
| `sort_group` | 13 | `08/md/rml_barterwares.xml` | Sort group (Attribute: group, sortbyvalue, sortdescending). |
| `sort_list` | 46 | `extensions/ego_dlc_split/ext_03/md/x4ep1_war_subscriptions.xml` | Sort list (Attribute: list, sortbyvalue). |
| `sort_people` | 1 | `08/md/boarding.xml` | Sort people (Attribute: name, object, templatelist, sorter). |
| `sort_trades` | 8 | `08/aiscripts/order.mining.routine.xml` | Sort trades (Attribute: name, tradelist, sorter). |
| `spacereservation` | 40 | `08/aiscripts/move.park.xml` | Spacereservation (Attribute: component, index, duration, safezone). |
| `spawn_docked` | 2 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Spawn docked (Attribute: ship, dock). |
| `spawn_drop` | 2 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Spawn drop (Attribute: object, drop). |
| `spawn_waiting_job_ship` | 1 | `08/md/story_diplomacy_intro.xml` | Spawn waiting job ship (Attribute: ship, sector). |
| `speak` | 778 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Speak (Attribute: actor, priority). |
| `start` | 24 | `08/aiscripts/order.restock.subordinates.xml` | Start (Attribute: object). |
| `start_actor_sequence` | 60 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Start actor sequence (Attribute: actor, type, behavior, transition, immediate). |
| `start_actor_walk` | 12 | `08/md/npc_state_machines.xml` | Start actor walk (Attribute: actor, target, roomslot, speed, triggeranimation). |
| `start_attack` | 6 | `08/aiscripts/masstraffic.watchdog.xml` | Start attack (Attribute: object, target). |
| `start_boarding_operation` | 1 | `08/md/showcases.xml` | Start boarding operation (Attribute: operation). |
| `start_boost` | 2 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Start boost (Attribute: object). |
| `start_conversation` | 47 | `08/md/rml_barterwares.xml` | Start conversation (Attribute: actor, conversation). |
| `start_diplomacy_event_operation` | 1 | `08/md/diplomacy.xml` | Start diplomacy event operation (Attribute: operation). |
| `start_dismantling` | 1 | `08/aiscripts/order.salvage.crush.xml` | Start dismantling (Attribute: object, wreck). |
| `start_observation` | 1 | `08/aiscripts/masstraffic.watchdog.xml` | Start observation (Attribute: object, target, range). |
| `start_player_autopilot` | 1 | `08/md/story_paranid.xml` | Start player autopilot (Attribute: destination). |
| `start_script` | 23 | `08/aiscripts/fight.attack.object.capital.xml` | Start script (Attribute: name, object). |
| `start_towing_object` | 1 | `08/aiscripts/order.salvage.collect.xml` | Start towing object (Attribute: ship, object). |
| `startposition` | 2 | `08/md/rml_trackship.xml` | Startposition (Attribute: value). |
| `stocklevel` | 1 | `08/aiscripts/trade.station.xml` | Stocklevel (Attribute: min). |
| `stop_actor_walk` | 3 | `08/md/npc_state_machines.xml` | Stop actor walk (Attribute: actor). |
| `stop_attack` | 6 | `08/aiscripts/masstraffic.watchdog.xml` | Stop attack (Attribute: object, target). |
| `stop_boost` | 11 | `08/aiscripts/move.evade.xml` | Stop boost (Attribute: object). |
| `stop_cutscene` | 204 | `08/md/gm_ambush.xml` | Stop cutscene (Attribute: key). |
| `stop_firing_at_target` | 2 | `08/aiscripts/lib.target.selection.singletarget.xml` | Stop firing at target (Attribute: object, target). |
| `stop_interactive_notification` | 1 | `08/md/notifications.xml` | Stop interactive notification (Attribute: id). |
| `stop_moving` | 69 | `08/aiscripts/order.trade.wareexchange.ship.xml` | Stop moving (Attribute: object). |
| `stop_music` | 4 | `extensions/ego_dlc_terran/ext_03/md/gs_terran2.xml` | Stop music. |
| `stop_observation` | 11 | `08/aiscripts/masstraffic.watchdog.xml` | Stop observation (Attribute: object, target). |
| `stop_player_autopilot` | 15 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Stop player autopilot. |
| `stop_shooting` | 17 | `08/aiscripts/fight.attack.object.capital.xml` | Stop shooting (Attribute: object). |
| `stop_towing_object` | 10 | `08/aiscripts/order.salvage.collect.xml` | Stop towing object (Attribute: ship). |
| `storage` | 1 | `08/md/lib_generic.xml` | Storage (Attribute: skiptimeout). |
| `store_trade_offer_snapshot` | 4 | `08/aiscripts/order.trade.wareexchange.ship.xml` | Store trade offer snapshot (Attribute: object). |
| `substitute_text` | 431 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Substitute text (Attribute: text, source, comment). |
| `t` | 1448 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | T (Attribute: id). |
| `targetposition` | 3 | `08/md/rml_trackship.xml` | Targetposition (Attribute: value). |
| `teleport` | 1 | `08/md/scenario_advanced.xml` | Teleport (Attribute: version, encoding, sector). |
| `teleport_player` | 11 | `08/md/scenario_combat.xml` | Teleport player (Attribute: object, instant, force). |
| `text` | 1705 | `extensions/ego_dlc_terran/ext_03/md/x4ep1_trade_terran.xml` | Text (Attribute: line, comment). |
| `thruster` | 29 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Thruster (Attribute: macro). |
| `todo` | 2 | `08/md/rml_transport_passengers.xml` | Todo. |
| `totalvolume` | 2 | `08/aiscripts/trade.find.free.xml` | Totalvolume (Attribute: min). |
| `transfer_marine_to_operation` | 3 | `08/md/boarding.xml` | Transfer marine to operation (Attribute: operation, object, template, status). |
| `transfer_marines_from_operation` | 1 | `08/md/boarding.xml` | Transfer marines from operation (Attribute: operation, object, marines). |
| `transfer_money` | 31 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Transfer money (Attribute: from, to, amount). |
| `transfer_people` | 15 | `08/aiscripts/build.shiptrader.xml` | Transfer people (Attribute: build). |
| `transform_position` | 7 | `08/aiscripts/order.fight.tactical.xml` | Transform position (Attribute: refposition, refrotation, name). |
| `trigger_animation` | 83 | `08/md/scenario_combat.xml` | Trigger animation (Attribute: object, group, trigger). |
| `trigger_autosave` | 2 | `extensions/ego_dlc_terran/ext_03/md/story_terraforming.xml` | Trigger autosave (Attribute: comment). |
| `turret` | 18 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Turret (Attribute: macro, path). |
| `turrets` | 47 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Turrets (Attribute: macro, path, group, exact). |
| `unassign_diplomacy_ship` | 1 | `08/md/npc_agent.xml` | Unassign diplomacy ship (Attribute: agent). |
| `undock` | 5 | `extensions/ego_dlc_terran/ext_03/md/story_hq_discovery.xml` | Undock (Attribute: ship). |
| `unit` | 37 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Unit (Attribute: macro, exact). |
| `units` | 17 | `08/md/rml_buildstation.xml` | Units. |
| `unlock_achievement` | 107 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Unlock achievement (Attribute: name, comment). |
| `unlock_all_firstperson_input` | 1 | `08/md/scenario_tutorials.xml` | Unlock all firstperson input. |
| `unlock_all_flight_input` | 4 | `08/md/scenario_tutorials.xml` | Unlock all flight input. |
| `unlock_all_holomap_input` | 3 | `08/md/scenario_tutorials.xml` | Unlock all holomap input. |
| `unlock_all_shooting_input` | 1 | `08/md/scenario_tutorials.xml` | Unlock all shooting input. |
| `unlock_firstperson_crouch_input` | 1 | `08/md/scenario_tutorials.xml` | Unlock firstperson crouch input. |
| `unlock_firstperson_jump_input` | 1 | `08/md/scenario_tutorials.xml` | Unlock firstperson jump input. |
| `unlock_firstperson_look_input` | 1 | `08/md/scenario_tutorials.xml` | Unlock firstperson look input. |
| `unlock_firstperson_walk_input` | 1 | `08/md/scenario_tutorials.xml` | Unlock firstperson walk input. |
| `unlock_flight_steering_input` | 2 | `08/md/scenario_tutorials.xml` | Unlock flight steering input. |
| `unlock_flight_strafe_input` | 2 | `08/md/scenario_tutorials.xml` | Unlock flight strafe input. |
| `unlock_flight_throttle_input` | 3 | `08/md/scenario_tutorials.xml` | Unlock flight throttle input. |
| `unlock_getup` | 5 | `08/md/scenario_tutorials.xml` | Unlock getup. |
| `unlock_holomap_rotation_input` | 1 | `08/md/scenario_tutorials.xml` | Unlock holomap rotation input. |
| `unlock_holomap_zoom_input` | 3 | `08/md/scenario_tutorials.xml` | Unlock holomap zoom input. |
| `unlock_primary_shooting_input` | 2 | `08/md/scenario_tutorials.xml` | Unlock primary shooting input. |
| `unlock_secondary_shooting_input` | 1 | `08/md/scenario_tutorials.xml` | Unlock secondary shooting input. |
| `unpause_spacesuit_oxygen` | 1 | `08/md/lib_generic.xml` | Unpause spacesuit oxygen (Attribute: object). |
| `update_mission` | 451 | `08/md/gm_ambush.xml` | Update mission (Attribute: cue). |
| `update_mission_thread` | 5 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Update mission thread (Attribute: cue, group). |
| `update_mission_thread_offer` | 3 | `08/md/x4ep1_war_subscriptions.xml` | Update mission thread offer (Attribute: cue, space). |
| `update_objective_progress` | 8 | `08/md/x4ep1_mentor_subscription.xml` | Update objective progress (Attribute: cue, progress, max). |
| `update_offer` | 27 | `extensions/ego_dlc_terran/ext_03/md/story_covert_operations.xml` | Update offer (Attribute: cue, group). |
| `update_signal_leak_voice` | 11 | `08/md/gm_board_ship.xml` | Update signal leak voice (Attribute: object, page, lines). |
| `update_trade` | 2 | `08/aiscripts/order.trade.wareexchange.ship.xml` | Update trade (Attribute: trade, amount, desiredamount). |
| `variation` | 12 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Variation (Attribute: exact). |
| `version` | 1 | `08/md/finalisestations.xml` | Version (Attribute: date, status, number). |
| `virtualmacros` | 29 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Virtualmacros. |
| `voice` | 8 | `extensions/ego_dlc_split/ext_03/md/story_split.xml` | Voice (Attribute: page, lines). |
| `wait` | 468 | `08/aiscripts/order.collect.ship.xml` | Wait (Attribute: min, max). |
| `ware` | 3 | `08/aiscripts/fight.attack.object.capital.xml` | Ware (Attribute: ware). |
| `wares` | 3 | `08/md/x4ep1_mentor_subscription.xml` | Wares (Attribute: list). |
| `warp` | 91 | `08/md/gm_ambush.xml` | Warp (Attribute: object, sector). |
| `weapon` | 85 | `extensions/ego_dlc_split/ext_03/md/gs_split1.xml` | Weapon (Attribute: macro, path). |
| `write_incoming_message` | 85 | `extensions/ego_dlc_terran/ext_03/md/gs_terran2.xml` | Write incoming message (Attribute: title, text, source, highpriority, read). |
| `write_to_logbook` | 135 | `extensions/ego_dlc_terran/ext_03/md/gs_terran2.xml` | Write to logbook (Attribute: category, faction, title, text). |
