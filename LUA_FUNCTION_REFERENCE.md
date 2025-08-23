# X4 Lua-Funktionsreferenz

Automatisch generierte Liste aller in den Skripten definierten Lua-Funktionen.

| Funktion | Vorkommen | Beispieldatei | Beschreibung |
| --- | --- | --- | --- |
| `AddGlobalAccess` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Fügt global access hinzu (Parameter: funcname, functionimpl). |
| `CallEventScripts` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt call event scripts aus (Parameter: eventName, argument1). |
| `CallHotkeyScripts` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt call hotkey scripts aus (Parameter: action). |
| `CallTabScrollScripts` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt call tab scroll scripts aus (Parameter: action). |
| `CallUpdateScripts` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt call update scripts aus. |
| `CallWidgetEventScripts` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt call widget event scripts aus (Parameter: widget, eventName, ...). |
| `GetLiveData` | 1 | `08/ui/addons/ego_targetmonitor/targetmonitor.lua` | Gibt live data zurück (Parameter: placeholder, component, templateConnectionName). |
| `GetTargetMonitorDetails` | 1 | `08/ui/addons/ego_targetmonitor/targetmonitor.lua` | Gibt target monitor details zurück (Parameter: component, templateConnectionName, isSofttarget). |
| `Helper.activateEditBox` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Aktiviert edit box (Parameter: tableobj, row, col, cursorpos, shiftstartpos). |
| `Helper.activateSliderCellInput` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Aktiviert slider cell input (Parameter: tableobj, row, col). |
| `Helper.addConversationReturnHandler` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Fügt conversation return handler hinzu (Parameter: menu). |
| `Helper.addDelayedOneTimeCallbackOnUpdate` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Fügt delayed one time callback on update hinzu (Parameter: callback, blockinput, delaytime). |
| `Helper.addDisplayedMenu` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Fügt displayed menu hinzu (Parameter: array, index, offset). |
| `Helper.addShipComparison` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Fügt ship comparison hinzu (Parameter: id, macro, upgradeplan). |
| `Helper.addTableDescRowDataMap` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Fügt table desc row data map hinzu (Parameter: menu, desc, rowdatamap). |
| `Helper.addTableIndexRowDataMap` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Fügt table index row data map hinzu (Parameter: menu, tableidx, rowdatamap). |
| `Helper.buttonAddContact` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button add contact aus (Parameter: menu, userid, block). |
| `Helper.buttonAddForumUser` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button add forum user aus (Parameter: menu, instance, userid, block). |
| `Helper.buttonCancelTrade` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button cancel trade aus (Parameter: menu, container, tradeid). |
| `Helper.buttonCancelTradeActive` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button cancel trade active aus (Parameter: menu, container, tradeid). |
| `Helper.buttonContactMessage` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button contact message aus (Parameter: menu, id, name). |
| `Helper.buttonCreateFriendListContext` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button create friend list context aus (Parameter: menu). |
| `Helper.buttonDropWares` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button drop wares aus (Parameter: menu). |
| `Helper.buttonEditTradeRule` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button edit trade rule aus (Parameter: menu, traderuleid). |
| `Helper.buttonExpandTransactionEntry` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button expand transaction entry aus (Parameter: buttondata, row, refreshCallback). |
| `Helper.buttonImportFriendList` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button import friend list aus (Parameter: menu). |
| `Helper.buttonImportFriendListActive` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button import friend list active aus (Parameter: menu). |
| `Helper.buttonMuteContact` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button mute contact aus (Parameter: menu, userid, mute). |
| `Helper.buttonRemoveContact` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button remove contact aus (Parameter: menu, userid). |
| `Helper.buttonReportContact` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button report contact aus (Parameter: menu, userid, reason). |
| `Helper.buttonRightBar` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button right bar aus (Parameter: container, currentmode, callback, selfcallback, mode, row). |
| `Helper.buttonStorageBuyProductWare` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button storage buy product ware aus (Parameter: menu, container64, ware, haslimitoverride, currentlimit). |
| `Helper.buttonStorageBuyTradeWare` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button storage buy trade ware aus (Parameter: menu, container64, ware, istradewarebought). |
| `Helper.buttonStorageSellResourceWare` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button storage sell resource ware aus (Parameter: menu, container64, ware, haslimitoverride, currentlimit). |
| `Helper.buttonStorageSellTradeWare` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button storage sell trade ware aus (Parameter: menu, container64, ware, istradewaresold). |
| `Helper.buttonTransactionLogZoom` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button transaction log zoom aus (Parameter: direction, refreshCallback). |
| `Helper.buttonVentureContactsSubMode` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button venture contacts sub mode aus (Parameter: menu, mode, col, instance). |
| `Helper.callExtensionFunction` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt call extension function aus (Parameter: extensionid, functionname, ...). |
| `Helper.callLoadoutFunction` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt call loadout function aus (Parameter: upgradeplan, crewplan, func, clear, loadoutType). |
| `Helper.cancelEditBoxInput` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cancel edit box input aus (Parameter: tableobj, row, col). |
| `Helper.checkDiscardStationEditorChanges` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt check discard station editor changes aus (Parameter: menu, dueToClose). |
| `Helper.checkTopLevelConditions` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt check top level conditions aus (Parameter: entry). |
| `Helper.checkboxBuyLimitOverride` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt checkbox buy limit override aus (Parameter: menu, container, ware, row, currentlimit, checked). |
| `Helper.checkboxSellLimitOverride` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt checkbox sell limit override aus (Parameter: menu, container, ware, row, currentlimit, checked). |
| `Helper.checkboxSetTradeRuleOverride` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt checkbox set trade rule override aus (Parameter: menu, container, type, ware, checked). |
| `Helper.checkboxStorageLevelOverride` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt checkbox storage level override aus (Parameter: menu, container, ware, row, currentlimit, checked). |
| `Helper.checkboxStorageWarePriceOverride` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt checkbox storage ware price override aus (Parameter: menu, container, ware, row, buysellswitch, price, checked). |
| `Helper.clearBuyLimit` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Leert buy limit (Parameter: menu, container64, ware). |
| `Helper.clearChatUpdateHandler` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Leert chat update handler. |
| `Helper.clearDataForRefresh` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Leert data for refresh (Parameter: menu, layer). |
| `Helper.clearFrame` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Leert frame (Parameter: menu, layer). |
| `Helper.clearMenu` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Leert menu (Parameter: menu). |
| `Helper.clearSellLimit` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Leert sell limit (Parameter: menu, container64, ware). |
| `Helper.clearShipComparisonData` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Leert ship comparison data. |
| `Helper.clearStationEditorState` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Leert station editor state. |
| `Helper.clearTableConnectionColumn` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Leert table connection column (Parameter: menu, col). |
| `Helper.closeDropDownOptions` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Schließt drop down options (Parameter: tableobj, row, col). |
| `Helper.closeInteractMenu` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Schließt interact menu. |
| `Helper.closeMenu` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Schließt menu (Parameter: menu, dueToClose, allowAutoMenu, sound). |
| `Helper.closeMenuAndCancel` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Schließt menu and cancel (Parameter: menu). |
| `Helper.closeMenuAndOpenNewMenu` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Schließt menu and open new menu (Parameter: menu, newname, param, noreturn, quickaccess). |
| `Helper.closeMenuAndReturn` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Schließt menu and return (Parameter: menu, returnparam). |
| `Helper.closeMenuForNewConversation` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Schließt menu for new conversation (Parameter: menu, conversation, actor, convparam, disablereturn). |
| `Helper.closeMenuForSection` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Schließt menu for section (Parameter: menu, nextsection, choiceparam). |
| `Helper.closeMenuForSubConversation` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Schließt menu for sub conversation (Parameter: menu, nextconversation, nextactor, convparam). |
| `Helper.closeMenuForSubSection` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Schließt menu for sub section (Parameter: menu, nextsection, choiceparam). |
| `Helper.closeMinimizedMenus` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Schließt minimized menus. |
| `Helper.comparePositions` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt compare positions aus (Parameter: pos1, pos2, deviation). |
| `Helper.confirmEditBoxInput` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt confirm edit box input aus (Parameter: tableobj, row, col). |
| `Helper.contactSearchHelper` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt contact search helper aus (Parameter: entry, text). |
| `Helper.convertColorToText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt convert color to text aus (Parameter: color). |
| `Helper.convertComponentIDs` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt convert component ids aus (Parameter: input). |
| `Helper.convertGameTimeToXTimeString` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt convert game time to xtime string aus (Parameter: time, dateonly). |
| `Helper.convertLoadout` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt convert loadout aus (Parameter: object, macro, loadout, softwaredata, loadoutType). |
| `Helper.convertLoadoutStats` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt convert loadout stats aus (Parameter: stats). |
| `Helper.createButton` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt button (Parameter: text, icon, noscaling, active, offsetx, offsety, width, height, color, hotkey, icon2, mouseovertext, helpoverlayid). |
| `Helper.createButtonIcon` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt button icon (Parameter: icon, swapicon, red, green, blue, alpha, width, height, offsetx, offsety). |
| `Helper.createComponentClassLookup` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt component class lookup. |
| `Helper.createDropDown` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt drop down (Parameter: options, startoption, text, icon, noscaling, active, offsetx, offsety, width, height, color, hotkey, mouseovertext, optionwidth, allowmouseoverinteraction, optionheight). |
| `Helper.createDropWaresContext` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt drop wares context (Parameter: menu, frame, instance). |
| `Helper.createEditBox` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt edit box (Parameter: text, noscaling, offsetx, offsety, width, height, color, hotkey, closemenuonback, mouseovertext, defaulttext, texthidden). |
| `Helper.createFrameHandle` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt frame handle (Parameter: menu, properties). |
| `Helper.createLSOStorageNode` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt lsostorage node (Parameter: menu, container, ware, planned, hasstorage, iscargo). |
| `Helper.createPlayerInfoConfig` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt player info config. |
| `Helper.createRightSideBar` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt right side bar (Parameter: frame, container, condition, currentmode, callback, selfcallback). |
| `Helper.createScriptValueWrapper` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt script value wrapper (Parameter: type, value). |
| `Helper.createSliderCell` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt slider cell (Parameter: text, noscaling, offsetx, offsety, width, height, bgcolor, valuecolor, scale, mouseovertext). |
| `Helper.createTextInfo` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt text info (Parameter: text, alignment, fontname, fontsize, red, green, blue, alpha, offsetx, offsety). |
| `Helper.createTopLevelConfig` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt top level config. |
| `Helper.createTopLevelTab` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt top level tab (Parameter: menu, id, frame, overrideText, locked, noreturn). |
| `Helper.createTransactionLog` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt transaction log (Parameter: frame, container, tableProperties, refreshCallback, selectionData). |
| `Helper.createUserQuestionContext` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt user question context (Parameter: menu, frame). |
| `Helper.createVentureContactContext` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt venture contact context (Parameter: menu, frame). |
| `Helper.createVentureContacts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt venture contacts (Parameter: menu, frame, instance, width, x, y, globalx, globaly). |
| `Helper.createVentureContactsHeader` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt venture contacts header (Parameter: menu, frame, instance, x, y). |
| `Helper.createVentureContactsTab` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt venture contacts tab (Parameter: menu, frame, instance, mode, width, x, y, globalx, globaly). |
| `Helper.diffpercent` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt diffpercent aus (Parameter: x, isbuyoffer). |
| `Helper.disableAutoMouseEmulation` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt disable auto mouse emulation aus (Parameter: menu). |
| `Helper.displaySkill` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt display skill aus (Parameter: skill, usebold, noemptystars). |
| `Helper.displayStars` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt display stars aus (Parameter: progress, total, usebold, noemptystars). |
| `Helper.drawCircle` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Zeichnet circle (Parameter: radius, centerx, centery, z, color, noscaling). |
| `Helper.drawEllipse` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Zeichnet ellipse (Parameter: radiusx, radiusy, centerx, centery, z, color, noscaling). |
| `Helper.drawLine` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Zeichnet line (Parameter: startpos, endpos, thickness, z, color, noscaling). |
| `Helper.drawRectangle` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Zeichnet rectangle (Parameter: width, height, offsetx, offsety, angle, z, color, noscaling). |
| `Helper.drawTriangle` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Zeichnet triangle (Parameter: width, height, offsetx, offsety, angle, z, color, noscaling). |
| `Helper.dropdownAssignment` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt dropdown assignment aus (Parameter: _, ship, subordinategroupid, commander, newassignment). |
| `Helper.dropdownDropWaresLockbox` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt dropdown drop wares lockbox aus (Parameter: menu, id). |
| `Helper.dropdownTradeRule` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt dropdown trade rule aus (Parameter: menu, container, type, ware, id). |
| `Helper.editboxTransactionLogPage` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt editbox transaction log page aus (Parameter: text, textchanged, refreshCallback). |
| `Helper.editboxVentureContactsPage` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt editbox venture contacts page aus (Parameter: menu, instance, text, textchanged). |
| `Helper.editboxVentureContactsPageActivated` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt editbox venture contacts page activated aus (Parameter: menu, widget, instance). |
| `Helper.editboxVentureFindForumUser` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt editbox venture find forum user aus (Parameter: menu, instance, text, textchanged). |
| `Helper.enableAutoMouseEmulation` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt enable auto mouse emulation aus (Parameter: menu). |
| `Helper.estimateString` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt estimate string aus (Parameter: estimated). |
| `Helper.evaluateTopLevelParam` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt evaluate top level param aus (Parameter: params). |
| `Helper.evaluateTopLevelParamHelper` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt evaluate top level param helper aus (Parameter: param). |
| `Helper.ffiClearNewHelper` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt ffi clear new helper aus. |
| `Helper.ffiColor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt ffi color aus (Parameter: color). |
| `Helper.ffiNewHelper` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt ffi new helper aus (Parameter: ...). |
| `Helper.ffiNewString` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt ffi new string aus (Parameter: string). |
| `Helper.ffiVLA` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt ffi vla aus (Parameter: result, vlaType, vlaSizeFunction, vlaFunction, ...). |
| `Helper.findFrameLayer` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt find frame layer aus (Parameter: menu, widget). |
| `Helper.findUpgradeType` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt find upgrade type aus (Parameter: type). |
| `Helper.findUpgradeTypeByGroupType` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt find upgrade type by group type aus (Parameter: grouptype). |
| `Helper.floor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt floor aus (Parameter: x, digits). |
| `Helper.formatOptionalShortcut` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt format optional shortcut aus (Parameter: format, inputtype, inputid, fallback). |
| `Helper.formatTimeLeft` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt format time left aus (Parameter: timeleft). |
| `Helper.getBlackLists` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt black lists zurück. |
| `Helper.getClassText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt class text zurück (Parameter: class). |
| `Helper.getContainerWareType` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt container ware type zurück (Parameter: container, ware). |
| `Helper.getCurrentRowData` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt current row data zurück (Parameter: menu, uitable). |
| `Helper.getDisplayableGateDestinationSpace` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt displayable gate destination space zurück (Parameter: gate). |
| `Helper.getETAString` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt etastring zurück (Parameter: name, eta). |
| `Helper.getEmptyCellDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt empty cell descriptor zurück. |
| `Helper.getFightRules` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt fight rules zurück. |
| `Helper.getHoloMapColors` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt holo map colors zurück. |
| `Helper.getInputMouseOverText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt input mouse over text zurück (Parameter: input). |
| `Helper.getInstalledModInfo` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt installed mod info zurück (Parameter: type, component, context, group, isgroup). |
| `Helper.getLimitedWareAmount` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt limited ware amount zurück (Parameter: ware). |
| `Helper.getLoadoutHelper` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt loadout helper zurück (Parameter: getLoadout, getLoadoutCounts, ...). |
| `Helper.getLoadoutHelper2` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt loadout helper2 zurück (Parameter: getLoadout, getLoadoutCounts, loadoutType, ...). |
| `Helper.getMacroTurretModes` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt macro turret modes zurück (Parameter: turret, forall). |
| `Helper.getMenu` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt menu zurück (Parameter: name). |
| `Helper.getOrderParameterWares` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt order parameter wares zurück (Parameter: inputparams). |
| `Helper.getPassedTime` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt passed time zurück (Parameter: time). |
| `Helper.getPassedUTCTime` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt passed utctime zurück (Parameter: time). |
| `Helper.getPlayerLogoColor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt player logo color zurück. |
| `Helper.getProjectEntry` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt project entry zurück (Parameter: cluster, buffer, isevent). |
| `Helper.getRelativeRenderTargetSize` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt relative render target size zurück (Parameter: menu, layer, rendertarget). |
| `Helper.getResourceBufferAmount` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt resource buffer amount zurück (Parameter: container, ware, storageinfo_amounts, accuracy). |
| `Helper.getShipComparisonMacro` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt ship comparison macro zurück (Parameter: id). |
| `Helper.getShipComparisonUpgradeplan` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt ship comparison upgradeplan zurück (Parameter: id). |
| `Helper.getSlotSizeText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt slot size text zurück (Parameter: slotsize). |
| `Helper.getStorageAmount` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt storage amount zurück (Parameter: container, nodedata, storageinfo_amounts, storageinfo_capacity, accuracy, showvolume). |
| `Helper.getSuitableControlEntities` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt suitable control entities zurück (Parameter: object, getshiptrader, onlynpcs). |
| `Helper.getSyncPointName` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt sync point name zurück (Parameter: id). |
| `Helper.getTopLevelMenuIndex` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt top level menu index zurück (Parameter: index, offset). |
| `Helper.getTurretModes` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt turret modes zurück (Parameter: turret, forall, helpoverlayprefix, counter). |
| `Helper.getUTCTime` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt utctime zurück (Parameter: time). |
| `Helper.getWorkforceConsumption` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt workforce consumption zurück (Parameter: container, ware). |
| `Helper.graphDataSelection` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt graph data selection aus (Parameter: data, refreshCallback). |
| `Helper.handleCreatedTables` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt handle created tables aus (Parameter: menu, tables). |
| `Helper.handleTableDesc` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt handle table desc aus (Parameter: menu, descriptors). |
| `Helper.hasExtension` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt has extension aus (Parameter: extensionid). |
| `Helper.hasVentureRewards` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt has venture rewards aus. |
| `Helper.indentText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt indent text aus (Parameter: text, indentstring, textboxwidth, font, fontsize). |
| `Helper.interpolatePriceColor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt interpolate price color aus (Parameter: ware, price, isselloffer, darkbasecolor). |
| `Helper.isComponentClass` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Prüft ob component class (Parameter: class1, class2). |
| `Helper.isOnlineGame` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Prüft ob online game. |
| `Helper.isPlayerCovered` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Prüft ob player covered. |
| `Helper.isTradeRestricted` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Prüft ob trade restricted (Parameter: container, ware). |
| `Helper.minimizeMenu` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt minimize menu aus (Parameter: menu, text). |
| `Helper.modPropertyEval2Float` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt mod property eval2 float aus (Parameter: basevalue, value, color, value2, color2). |
| `Helper.modPropertyEval2UINT` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt mod property eval2 uint aus (Parameter: basevalue, value, color, value2, color2). |
| `Helper.modPropertyEvalFloat` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt mod property eval float aus (Parameter: basevalue, value). |
| `Helper.modPropertyEvalUINT` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt mod property eval uint aus (Parameter: basevalue, value). |
| `Helper.onCheckUsername` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt on check username aus (Parameter: menu, result). |
| `Helper.onCollapseLSOStorageNode` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt on collapse lsostorage node aus (Parameter: menu, nodedata). |
| `Helper.onConversationReturned` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt on conversation returned aus (Parameter: eventname, sectionname). |
| `Helper.onExpandLSOStorageNode` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt on expand lsostorage node aus (Parameter: menu, container, _, ftable, _, nodedata). |
| `Helper.onPlatformFriendsLookedUp` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt on platform friends looked up aus (Parameter: menu). |
| `Helper.onReceiveContacts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt on receive contacts aus (Parameter: menu). |
| `Helper.onSliderChangedLSOStorageNode` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt on slider changed lsostorage node aus (Parameter: container, node, nodedata, slideridx, value). |
| `Helper.onTransactionLogEditBoxActivated` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt on transaction log edit box activated aus (Parameter: widget). |
| `Helper.onTransactionLogRowChanged` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt on transaction log row changed aus (Parameter: rowdata). |
| `Helper.onTransactionLogUpdate` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt on transaction log update aus. |
| `Helper.openInteractMenu` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Öffnet interact menu (Parameter: menu, param). |
| `Helper.orderedKeys` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt ordered keys aus (Parameter: t, sorter). |
| `Helper.orderedNext` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt ordered next aus (Parameter: t, state). |
| `Helper.orderedNextByWareName` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt ordered next by ware name aus (Parameter: t, state). |
| `Helper.orderedPairs` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt ordered pairs aus (Parameter: t). |
| `Helper.orderedPairsByWareName` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt ordered pairs by ware name aus (Parameter: t). |
| `Helper.parseAICommand` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt parse aicommand aus (Parameter: entity). |
| `Helper.percent` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt percent aus (Parameter: x, digits). |
| `Helper.playerInfoConfigTextLeft` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt player info config text left aus (Parameter: _, width, ismultiverse). |
| `Helper.playerInfoConfigTextRight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt player info config text right aus (Parameter: _, ismultiverse). |
| `Helper.registerExtension` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt register extension aus (Parameter: extensionid, hook). |
| `Helper.registerMenu` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt register menu aus (Parameter: menu). |
| `Helper.registerStationEditorChanges` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt register station editor changes aus. |
| `Helper.registerStationEditorState` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt register station editor state aus (Parameter: menu). |
| `Helper.registerVentureContactCallbacks` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt register venture contact callbacks aus (Parameter: menu). |
| `Helper.removeAllButtonScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt all button scripts (Parameter: menu, layer). |
| `Helper.removeAllCheckBoxScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt all check box scripts (Parameter: menu, layer). |
| `Helper.removeAllDropDownScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt all drop down scripts (Parameter: menu, layer). |
| `Helper.removeAllEditBoxScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt all edit box scripts (Parameter: menu, layer). |
| `Helper.removeAllFlowchartNodeScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt all flowchart node scripts (Parameter: menu, layer). |
| `Helper.removeAllGraphScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt all graph scripts (Parameter: menu, layer). |
| `Helper.removeAllKeyBindings` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt all key bindings (Parameter: menu). |
| `Helper.removeAllMenuScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt all menu scripts (Parameter: menu, layer). |
| `Helper.removeAllScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt all scripts (Parameter: scriptMap, menu, layer). |
| `Helper.removeAllSliderCellScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt all slider cell scripts (Parameter: menu, layer). |
| `Helper.removeAllTabScrollCallbacks` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt all tab scroll callbacks (Parameter: menu). |
| `Helper.removeAllWidgetScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt all widget scripts (Parameter: menu, layer). |
| `Helper.removeButtonScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt button scripts (Parameter: menu, tableobj, row, col). |
| `Helper.removeCheckBoxScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt check box scripts (Parameter: menu, tableobj, row, col). |
| `Helper.removeDropDownScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt drop down scripts (Parameter: menu, tableobj, row, col). |
| `Helper.removeEditBoxScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt edit box scripts (Parameter: menu, tableobj, row, col). |
| `Helper.removeFlowchartNodeScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt flowchart node scripts (Parameter: menu, flowchartid, row, col). |
| `Helper.removeFlowchartScript` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt flowchart script (Parameter: flowchartid, row, col, type, script). |
| `Helper.removeGraphScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt graph scripts (Parameter: menu, tableobj, row, col). |
| `Helper.removeKeyBinding` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt key binding (Parameter: script). |
| `Helper.removeMenuScript` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt menu script (Parameter: obj, handleType, script). |
| `Helper.removeScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt scripts (Parameter: scriptMap, menu, widget, row, col). |
| `Helper.removeShipComparison` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt ship comparison (Parameter: id). |
| `Helper.removeSliderCellScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt slider cell scripts (Parameter: menu, tableobj, row, col). |
| `Helper.removeTabScrollCallback` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt tab scroll callback (Parameter: menu, script). |
| `Helper.removeTableScript` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Entfernt table script (Parameter: tableobj, row, col, type, script). |
| `Helper.resetInteractMenuCallbacks` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt interact menu callbacks zurück. |
| `Helper.resetUpdateHandler` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt update handler zurück. |
| `Helper.restoreMenu` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt restore menu aus (Parameter: menu). |
| `Helper.returnFromInteractMenu` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt return from interact menu aus (Parameter: uitable, ...). |
| `Helper.revOrderedNext` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt rev ordered next aus (Parameter: t, state). |
| `Helper.revOrderedPairs` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt rev ordered pairs aus (Parameter: t). |
| `Helper.round` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt round aus (Parameter: x, digits). |
| `Helper.roundStr` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt round str aus (Parameter: x, digits). |
| `Helper.scaleFont` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt scale font aus (Parameter: fontname, fontsize, enabled). |
| `Helper.scaleX` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt scale x aus (Parameter: x, enabled). |
| `Helper.scaleY` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt scale y aus (Parameter: y, enabled). |
| `Helper.scrollTopLevel` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt scroll top level aus (Parameter: menu, id, offset). |
| `Helper.scrollTopLevelInternal` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt scroll top level internal aus (Parameter: menu, index, offset, noreturn). |
| `Helper.sendChatWindowCallback` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt send chat window callback aus (Parameter: param). |
| `Helper.setButtonScript` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt button script (Parameter: menu, id, tableobj, row, col, script, onRightClickScript, onDblClickScript). |
| `Helper.setBuyLimit` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt buy limit (Parameter: menu, container64, ware, limit). |
| `Helper.setCellContent` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt cell content (Parameter: menu, tableID, descriptor, row, column, norelease, type, id, ...). |
| `Helper.setChatUpdateHandler` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt chat update handler (Parameter: menu). |
| `Helper.setCheckBoxScript` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt check box script (Parameter: menu, id, tableobj, row, col, script). |
| `Helper.setDropDownScript` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt drop down script (Parameter: menu, id, tableobj, row, col, activateScript, confirmScript, removedScript). |
| `Helper.setEditBoxScript` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt edit box script (Parameter: menu, id, tableobj, row, col, script, textchangedscript, activatedscript, cursorchangedscript). |
| `Helper.setGraphScript` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt graph script (Parameter: menu, id, tableobj, row, col, script). |
| `Helper.setIntersectorDefence` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt intersector defence (Parameter: controllable, group, reset, sectorid, pos_in). |
| `Helper.setKeyBinding` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt key binding (Parameter: menu, script). |
| `Helper.setMenuScript` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt menu script (Parameter: menu, layer, obj, handleType, script). |
| `Helper.setScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt scripts (Parameter: menu, layer, frame, children). |
| `Helper.setSellLimit` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt sell limit (Parameter: menu, container64, ware, limit). |
| `Helper.setSliderCellScript` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt slider cell script (Parameter: menu, id, tableobj, row, col, changedScript, activateScript, deactivateScript, onRightClickScript, confirmScript). |
| `Helper.setSliderCellValue` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt slider cell value (Parameter: tableobj, row, col, value, newmaxselect). |
| `Helper.setTabScrollCallback` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt tab scroll callback (Parameter: menu, script). |
| `Helper.setupDAGLayout` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt setup daglayout aus (Parameter: nodes). |
| `Helper.showVentureFriendListContext` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Zeigt venture friend list context (Parameter: menu, frame). |
| `Helper.slidercellBuyLimitOverride` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt slidercell buy limit override aus (Parameter: menu, container, ware, value, sellslider). |
| `Helper.slidercellDropWares` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt slidercell drop wares aus (Parameter: menu, ware, value). |
| `Helper.slidercellSellLimitOverride` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt slidercell sell limit override aus (Parameter: menu, container, ware, value, buyslider). |
| `Helper.slidercellStorageLevelOverride` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt slidercell storage level override aus (Parameter: menu, container, ware, value, buyslider, sellslider). |
| `Helper.slidercellStorageWarePriceOverride` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt slidercell storage ware price override aus (Parameter: container, ware, buysellswitch, value). |
| `Helper.sortClass` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort class aus (Parameter: a, b, invert). |
| `Helper.sortComponentName` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort component name aus (Parameter: a, b). |
| `Helper.sortDate` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort date aus (Parameter: a, b, invert). |
| `Helper.sortETA` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort eta aus (Parameter: a, b). |
| `Helper.sortEntityTypeAndName` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort entity type and name aus (Parameter: a, b). |
| `Helper.sortFactionName` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort faction name aus (Parameter: a, b). |
| `Helper.sortHullAndName` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort hull and name aus (Parameter: a, b, invert). |
| `Helper.sortID` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort id aus (Parameter: a, b). |
| `Helper.sortMacroName` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort macro name aus (Parameter: a, b). |
| `Helper.sortMacroRaceAndShortname` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort macro race and shortname aus (Parameter: a, b). |
| `Helper.sortName` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort name aus (Parameter: a, b, invert). |
| `Helper.sortNameAndObjectID` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort name and object id aus (Parameter: a, b, invert). |
| `Helper.sortNameSectorAndObjectID` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort name sector and object id aus (Parameter: a, b, invert). |
| `Helper.sortPlayerMacro` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort player macro aus (Parameter: a, b). |
| `Helper.sortRelationAndName` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort relation and name aus (Parameter: a, b, invert). |
| `Helper.sortShipsByClassAndPurpose` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort ships by class and purpose aus (Parameter: a, b, invert). |
| `Helper.sortSlots` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort slots aus (Parameter: a, b). |
| `Helper.sortUniverseIDName` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort universe idname aus (Parameter: a, b). |
| `Helper.sortWareName` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort ware name aus (Parameter: a, b). |
| `Helper.sortWareSortOrder` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt sort ware sort order aus (Parameter: a, b). |
| `Helper.substituteText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt substitute text aus (Parameter: str, substitutions). |
| `Helper.tableCopy` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table copy aus (Parameter: orig, levels). |
| `Helper.tableLength` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table length aus (Parameter: value). |
| `Helper.textArrayHelper` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt text array helper aus (Parameter: texts, func, keyword). |
| `Helper.timeDuration` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt time duration aus (Parameter: x). |
| `Helper.transactionLogSearchHelper` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt transaction log search helper aus (Parameter: entry, text). |
| `Helper.unlockInfo` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt unlock info aus (Parameter: unlocked, cellcontent). |
| `Helper.unregisterStationEditorChanges` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt unregister station editor changes aus. |
| `Helper.unregisterVentureContactCallbacks` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt unregister venture contact callbacks aus. |
| `Helper.updateButtonColor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Aktualisiert button color (Parameter: tableobj, row, col, newcolor). |
| `Helper.updateCellText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Aktualisiert cell text (Parameter: tableobj, row, col, newtext, newcolor). |
| `Helper.updateEditBoxText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Aktualisiert edit box text (Parameter: tableobj, row, col, newtext). |
| `Helper.updateLSOStorageNode` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Aktualisiert lsostorage node (Parameter: menu, node, container, ware). |
| `Helper.updateStorageLevel` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Aktualisiert storage level (Parameter: menu, container, ware, value, buyslider, sellslider). |
| `Helper.updateTradeRules` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Aktualisiert trade rules. |
| `Helper.updateVenturePlatforms` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Aktualisiert venture platforms. |
| `Helper.ventureEndTimeLeftText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt venture end time left text aus (Parameter: endtime). |
| `Helper.ventureOperationTimeLeftText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt venture operation time left text aus. |
| `Helper.ventureSeasonTimeLeftText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt venture season time left text aus. |
| `Helper.ventureTimeLeft` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt venture time left aus (Parameter: timeleft). |
| `MakeGlobalAvailable` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt make global available aus (Parameter: objectname). |
| `RegisterEvent` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt register event aus (Parameter: eventName, scriptFunction). |
| `RemoveScript` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Entfernt script (Parameter: widget, handle, scriptFunction). |
| `SetEGOGlobals` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt egoglobals (Parameter: env). |
| `SetScript` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt script (Parameter: widget, handle, scriptFunction). |
| `ToReprString` | 1 | `08/ui/addons/ego_debug/debug.lua` | Führt to repr string aus (Parameter: value, recursiondepth, indent). |
| `UnregisterEvent` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt unregister event aus (Parameter: eventName, scriptFunction). |
| `View.clearMenus` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Leert menus (Parameter: types). |
| `View.createView` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Erstellt view. |
| `View.generateFrameDescriptors` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Führt generate frame descriptors aus. |
| `View.getMenu` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Gibt menu zurück (Parameter: types). |
| `View.hasMenu` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Führt has menu aus (Parameter: types). |
| `View.hasPlayerControls` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Führt has player controls aus. |
| `View.hideFrame` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Versteckt frame (Parameter: frame). |
| `View.hideView` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Versteckt view. |
| `View.isCloseOnUnhandledClick` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Prüft ob close on unhandled click. |
| `View.isExclusiveInteractions` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Prüft ob exclusive interactions. |
| `View.isSurpressDisplayErrors` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Prüft ob surpress display errors. |
| `View.keepCrosshairVisible` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Führt keep crosshair visible aus. |
| `View.keepHUDVisible` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Führt keep hudvisible aus. |
| `View.minimizeFrame` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Führt minimize frame aus (Parameter: frame, text). |
| `View.minimizeMenu` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Führt minimize menu aus (Parameter: id, text). |
| `View.registerMenu` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Führt register menu aus (Parameter: id, type, callback, clearCallback, framedescriptors, exclusiveInteractions, closeOnUnhandledClick, surpressDisplayErrors, playerControls, useMiniWidgetSystem, startAnimation, keepHUDVisible, keepCrosshairVisible, showTickerPermanently, menuname). |
| `View.restoreFrame` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Führt restore frame aus (Parameter: frame). |
| `View.restoreMenu` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Führt restore menu aus (Parameter: id). |
| `View.showTickerPermanently` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Zeigt ticker permanently. |
| `View.startAnimation` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Startet animation. |
| `View.unregisterMenu` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Führt unregister menu aus (Parameter: id, releaseFrameDescriptor). |
| `View.updateMenu` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Aktualisiert menu (Parameter: menu). |
| `View.useMiniWidgetSystem` | 1 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Führt use mini widget system aus. |
| `abortScan` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt abort scan aus. |
| `activateAdditionalIcon` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktiviert additional icon (Parameter: iconEntry). |
| `activateAimTargetElement` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktiviert aim target element. |
| `activateBar` | 5 | `08/ui/core/lua/infobar4.lua` | Aktiviert bar (Parameter: text). |
| `activateBar2` | 1 | `08/ui/core/lua/infobar3.lua` | Aktiviert bar2 (Parameter: state). |
| `activateCollectable` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktiviert collectable (Parameter: targetElement, mode). |
| `activateCommanderElement` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktiviert commander element (Parameter: targetElement). |
| `activateCompass` | 1 | `08/ui/core/lua/compass.lua` | Aktiviert compass. |
| `activateCrosshair` | 2 | `08/ui/core/lua/crosshair handling.lua` | Aktiviert crosshair. |
| `activateDebugLine` | 1 | `08/ui/core/lua/debugline.lua` | Aktiviert debug line. |
| `activateDebugOutline` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktiviert debug outline (Parameter: targetElement). |
| `activateDronePanel` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktiviert drone panel. |
| `activateDroneType` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktiviert drone type (Parameter: dronePanelEntry). |
| `activateFactionLadder` | 1 | `08/ui/core/lua/monitors.lua` | Aktiviert faction ladder. |
| `activateFill` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktiviert fill (Parameter: targetElement). |
| `activateHullShield` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktiviert hull shield (Parameter: targetElement). |
| `activateIcon` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktiviert icon (Parameter: targetElement). |
| `activateIconElements` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktiviert icon elements (Parameter: targetElement). |
| `activateInteractElement` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktiviert interact element. |
| `activateMessageTickerBar` | 1 | `08/ui/core/lua/monitors.lua` | Aktiviert message ticker bar (Parameter: line, blinking). |
| `activateMessageTickerText` | 1 | `08/ui/core/lua/monitors.lua` | Aktiviert message ticker text (Parameter: line). |
| `activateMissileIncoming` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktiviert missile incoming. |
| `activateMissileLock` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktiviert missile lock. |
| `activateMissionArrow` | 2 | `08/ui/core/lua/crosshair handling.lua` | Aktiviert mission arrow. |
| `activateMonitor` | 1 | `08/ui/core/lua/monitors.lua` | Aktiviert monitor (Parameter: state). |
| `activateOutline` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktiviert outline (Parameter: targetElement). |
| `activateOverlay` | 2 | `08/ui/core/lua/monitors.lua` | Aktiviert overlay. |
| `activateOxygenBar` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktiviert oxygen bar. |
| `activatePlayerShieldbar` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktiviert player shieldbar. |
| `activateProgressbar` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktiviert progressbar. |
| `activatePromo` | 1 | `08/ui/core/lua/promo.lua` | Aktiviert promo. |
| `activateRadarPicking` | 1 | `08/ui/core/lua/monitors.lua` | Aktiviert radar picking. |
| `activateRectangleElements` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktiviert rectangle elements (Parameter: targetElement, normalMode, showRelationBrackets). |
| `activateSeparateRadar` | 1 | `08/ui/core/lua/monitors.lua` | Aktiviert separate radar (Parameter: force). |
| `activateSeta` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktiviert seta (Parameter: mode). |
| `activateSofttarget` | 1 | `08/ui/core/lua/firstperson_crosshair.lua` | Aktiviert softtarget. |
| `activateState` | 1 | `08/ui/core/lua/monitors.lua` | Aktiviert state (Parameter: state, allowPlaySound, refresh). |
| `activateTargetArrow` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktiviert target arrow. |
| `activateTargetIndicator` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktiviert target indicator (Parameter: targetElement, color). |
| `activateTargetMonitorRadar` | 1 | `08/ui/core/lua/monitors.lua` | Aktiviert target monitor radar. |
| `activateTargetRectangle` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktiviert target rectangle (Parameter: targetElement). |
| `activateWeaponPanel` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktiviert weapon panel. |
| `activationScan` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt activation scan aus. |
| `addDebugMessage` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Fügt debug message hinzu (Parameter: id, insertionPos, allowTimestampModification). |
| `addFlowchartEdge` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Fügt flowchart edge hinzu. |
| `addFlowchartWareNode` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Fügt flowchart ware node hinzu. |
| `addHullShieldRows` | 1 | `08/ui/addons/ego_targetmonitor/targetmonitor.lua` | Fügt hull shield rows hinzu. |
| `addRow` | 1 | `08/ui/addons/ego_targetmonitor/targetmonitor.lua` | Fügt row hinzu. |
| `addRowText` | 1 | `08/ui/addons/ego_targetmonitor/targetmonitor.lua` | Fügt row text hinzu. |
| `addStorageWarningPlaceholders` | 1 | `08/ui/addons/ego_targetmonitor/targetmonitor.lua` | Fügt storage warning placeholders hinzu. |
| `addTwoRows` | 1 | `08/ui/addons/ego_targetmonitor/targetmonitor.lua` | Fügt two rows hinzu. |
| `addonSystem.insertEventScript` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt insert event script aus (Parameter: eventName, scriptFunction). |
| `addonSystem.insertHotkeyScript` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt insert hotkey script aus (Parameter: scriptFunction). |
| `addonSystem.insertTabScrollScript` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt insert tab scroll script aus (Parameter: scriptFunction). |
| `addonSystem.insertUpdateScript` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt insert update script aus (Parameter: scriptFunction). |
| `addonSystem.insertWidgetEventScript` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt insert widget event script aus (Parameter: widget, eventName, scriptFunction). |
| `addonSystem.isValidWidgetScriptHandle` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Prüft ob valid widget script handle (Parameter: handle). |
| `addonSystem.removeEventScript` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Entfernt event script (Parameter: eventName, scriptFunction). |
| `addonSystem.removeHotkeyScript` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Entfernt hotkey script (Parameter: scriptFunction). |
| `addonSystem.removeTabScrollScript` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Entfernt tab scroll script (Parameter: scriptFunction). |
| `addonSystem.removeUpdateScript` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Entfernt update script (Parameter: scriptFunction). |
| `addonSystem.removeWidgetEventScript` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Entfernt widget event script (Parameter: widget, eventName, scriptFunction). |
| `addonSystem.removeWidgetScript` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Entfernt widget script (Parameter: widget, handle, scriptFunction). |
| `addonSystem.setWidgetScript` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt widget script (Parameter: widget, handle, scriptFunction). |
| `aligned` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt aligned aus. |
| `bcdump` | 1 | `08/ui/core/lua/jit/bc.lua` | Führt bcdump aus. |
| `bcline` | 1 | `08/ui/core/lua/jit/bc.lua` | Führt bcline aus. |
| `bclist` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt bclist aus. |
| `bclistoff` | 1 | `08/ui/core/lua/jit/bc.lua` | Führt bclistoff aus. |
| `bcliston` | 1 | `08/ui/core/lua/jit/bc.lua` | Führt bcliston aus. |
| `bcsave` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt bcsave aus. |
| `bcsave_c` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt bcsave c aus. |
| `bcsave_elfobj` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt bcsave elfobj aus. |
| `bcsave_machobj` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt bcsave machobj aus. |
| `bcsave_obj` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt bcsave obj aus. |
| `bcsave_peobj` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt bcsave peobj aus. |
| `bcsave_raw` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt bcsave raw aus. |
| `bcsave_tail` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt bcsave tail aus. |
| `bctargets` | 1 | `08/ui/core/lua/jit/bc.lua` | Führt bctargets aus. |
| `calculateHalfMaxHorizontalScreenExtents` | 1 | `08/ui/core/lua/dialogmenu.lua` | Berechnet half max horizontal screen extents (Parameter: element). |
| `calculateHalfMaxVerticalScreenExtents` | 1 | `08/ui/core/lua/dialogmenu.lua` | Berechnet half max vertical screen extents (Parameter: element). |
| `calculateTargetPriority` | 1 | `08/ui/core/lua/targetsystem.lua` | Berechnet target priority (Parameter: x2d, y2d, cameraDistance). |
| `callbacks.onAutotargetStateChanged` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on autotarget state changed aus. |
| `callbacks.onConnectElement` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on connect element aus (Parameter: targetSystem, messageID, posID). |
| `callbacks.onDisconnectElement` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on disconnect element aus (Parameter: targetSystem). |
| `callbacks.onEnableConfidenceBasedAutoTargetting` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on enable confidence based auto targetting aus (Parameter: _, enabled). |
| `callbacks.onEnableDebugMousePickRendering` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on enable debug mouse pick rendering aus (Parameter: _, enabled). |
| `callbacks.onEnableDebugOutlines` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on enable debug outlines aus (Parameter: _, enabled). |
| `callbacks.onEnableSofttargetDebugValue` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on enable softtarget debug value aus (Parameter: _, enabled). |
| `callbacks.onEnterInteractMenu` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on enter interact menu aus. |
| `callbacks.onGamePlanChange` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on game plan change aus (Parameter: _, gameplan). |
| `callbacks.onHUDRenderStateChanged` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on hudrender state changed aus (Parameter: _, state). |
| `callbacks.onInputModeChanged` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on input mode changed aus (Parameter: _, mode). |
| `callbacks.onInteractMenuHidden` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on interact menu hidden aus (Parameter: _, messageID). |
| `callbacks.onInteractMenuShown` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on interact menu shown aus (Parameter: _, messageID). |
| `callbacks.onMiddleMouseClick` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on middle mouse click aus (Parameter: element, delayed, modifiers). |
| `callbacks.onMiddleMouseClickRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on middle mouse click radar aus (Parameter: element, delayed, modifiers). |
| `callbacks.onMiddleMouseDblClick` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on middle mouse dbl click aus (Parameter: element, delayed, modifiers). |
| `callbacks.onMiddleMouseDblClickRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on middle mouse dbl click radar aus (Parameter: element, delayed, modifiers). |
| `callbacks.onMiddleMouseDown` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on middle mouse down aus (Parameter: element, delayed, modifiers). |
| `callbacks.onMiddleMouseDownRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on middle mouse down radar aus (Parameter: element, delayed, modifiers). |
| `callbacks.onMouseClick` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on mouse click aus (Parameter: element, delayed, modifiers). |
| `callbacks.onMouseClickRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on mouse click radar aus (Parameter: element, delayed, modifiers). |
| `callbacks.onMouseDblClick` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on mouse dbl click aus (Parameter: element, delayed, modifiers). |
| `callbacks.onMouseDblClickRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on mouse dbl click radar aus (Parameter: element, delayed, modifiers). |
| `callbacks.onMouseDown` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on mouse down aus (Parameter: element, delayed, modifiers). |
| `callbacks.onMouseDownRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on mouse down radar aus (Parameter: element, delayed, modifiers). |
| `callbacks.onMouseOut` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on mouse out aus. |
| `callbacks.onMouseOutRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on mouse out radar aus. |
| `callbacks.onMouseOver` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on mouse over aus (Parameter: element). |
| `callbacks.onMouseOverRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on mouse over radar aus. |
| `callbacks.onPlayerKilled` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on player killed aus. |
| `callbacks.onRightMouseClick` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on right mouse click aus (Parameter: element, delayed, modifiers). |
| `callbacks.onRightMouseClickRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on right mouse click radar aus (Parameter: element, delayed, modifiers). |
| `callbacks.onRightMouseDblClick` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on right mouse dbl click aus (Parameter: element, delayed, modifiers). |
| `callbacks.onRightMouseDblClickRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on right mouse dbl click radar aus (Parameter: element, delayed, modifiers). |
| `callbacks.onRightMouseDown` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on right mouse down aus (Parameter: element, delayed, modifiers). |
| `callbacks.onRightMouseDownRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on right mouse down radar aus (Parameter: element, delayed, modifiers). |
| `callbacks.onSetMousePickingBorder` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on set mouse picking border aus (Parameter: _, value). |
| `callbacks.onSetObstructedByOwnComponents` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on set obstructed by own components aus (Parameter: _, enabled). |
| `callbacks.onSetTargetConeMaxArea` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on set target cone max area aus (Parameter: _, value). |
| `callbacks.onSetTargetConeMaxDistance` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on set target cone max distance aus (Parameter: _, value). |
| `callbacks.onSetTargetConeMidArea` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on set target cone mid area aus (Parameter: _, value). |
| `callbacks.onSetTargetConeMidDistance` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on set target cone mid distance aus (Parameter: _, value). |
| `callbacks.onSetTargetConeMinArea` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on set target cone min area aus (Parameter: _, value). |
| `callbacks.onSetTargetConeMinDistance` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on set target cone min distance aus (Parameter: _, value). |
| `callbacks.onSetTargetConeThreshold` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on set target cone threshold aus (Parameter: _, value). |
| `callbacks.onSide1MouseClick` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on side1 mouse click aus (Parameter: element, delayed, modifiers). |
| `callbacks.onSide1MouseClickRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on side1 mouse click radar aus (Parameter: element, delayed, modifiers). |
| `callbacks.onSide1MouseDblClick` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on side1 mouse dbl click aus (Parameter: element, delayed, modifiers). |
| `callbacks.onSide1MouseDblClickRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on side1 mouse dbl click radar aus (Parameter: element, delayed, modifiers). |
| `callbacks.onSide1MouseDown` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on side1 mouse down aus (Parameter: element, delayed, modifiers). |
| `callbacks.onSide1MouseDownRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on side1 mouse down radar aus (Parameter: element, delayed, modifiers). |
| `callbacks.onSide2MouseClick` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on side2 mouse click aus (Parameter: element, delayed, modifiers). |
| `callbacks.onSide2MouseClickRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on side2 mouse click radar aus (Parameter: element, delayed, modifiers). |
| `callbacks.onSide2MouseDblClick` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on side2 mouse dbl click aus (Parameter: element, delayed, modifiers). |
| `callbacks.onSide2MouseDblClickRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on side2 mouse dbl click radar aus (Parameter: element, delayed, modifiers). |
| `callbacks.onSide2MouseDown` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on side2 mouse down aus (Parameter: element, delayed, modifiers). |
| `callbacks.onSide2MouseDownRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on side2 mouse down radar aus (Parameter: element, delayed, modifiers). |
| `callbacks.onSofttargetChanged` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on softtarget changed aus (Parameter: _, newSofttargetMessageID). |
| `callbacks.onSofttargetManagerActive` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on softtarget manager active aus. |
| `callbacks.onSofttargetManagerInactive` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on softtarget manager inactive aus. |
| `callbacks.onUpdateColorMap` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on update color map aus. |
| `callbacks.onUseFactionColorChanged` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt on use faction color changed aus. |
| `cameraDistanceSorter` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt camera distance sorter aus (Parameter: a, b). |
| `canMessageBeSofttarget` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt can message be softtarget aus (Parameter: targetElement). |
| `changePendingSofttarget` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt change pending softtarget aus (Parameter: newSofttarget). |
| `changePriorityMissionTarget` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt change priority mission target aus (Parameter: newPriorityMissionTarget). |
| `changeState` | 2 | `08/ui/core/lua/monitors.lua` | Führt change state aus (Parameter: state, force, allowPlaySound, refresh, keepCutscene). |
| `check` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt check aus. |
| `checkMessageTickerActivation` | 1 | `08/ui/core/lua/monitors.lua` | Führt check message ticker activation aus. |
| `checkPendingSofttargetChange` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt check pending softtarget change aus (Parameter: newSofttarget, previousSofttarget). |
| `checkRadarActivation` | 1 | `08/ui/core/lua/monitors.lua` | Führt check radar activation aus (Parameter: force). |
| `checkSofttargetChange` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt check softtarget change aus (Parameter: forceTarget, newTargetMessageID). |
| `checkarg` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt checkarg aus. |
| `checkmodname` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt checkmodname aus. |
| `clearDataOnVersionChange` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Leert data on version change. |
| `clearprefixes` | 1 | `08/ui/core/lua/jit/dis_x86.lua` | Führt clearprefixes aus. |
| `clickDialogButton` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt click dialog button aus (Parameter: button). |
| `closeCurrentState` | 1 | `08/ui/core/lua/monitors.lua` | Schließt current state (Parameter: force). |
| `closeMenu` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Schließt menu (Parameter: menu, resultfunc, allowAutoMenu). |
| `colorDroneType` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt color drone type aus (Parameter: dronePanelEntry, droneTypeDetails). |
| `colorize_ansi` | 1 | `08/ui/core/lua/jit/dump.lua` | Führt colorize ansi aus. |
| `colorize_html` | 1 | `08/ui/core/lua/jit/dump.lua` | Führt colorize html aus. |
| `colorize_text` | 1 | `08/ui/core/lua/jit/dump.lua` | Führt colorize text aus. |
| `condfmt` | 1 | `08/ui/core/lua/jit/dis_ppc.lua` | Führt condfmt aus. |
| `connectTargetElement` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt connect target element aus (Parameter: targetElement, messageID, posID). |
| `constructPlaceholderText` | 1 | `08/ui/core/lua/monitors.lua` | Führt construct placeholder text aus (Parameter: chunks, component, connection). |
| `constructTargetElementData` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt construct target element data aus. |
| `convertHorizontalAlignment` | 1 | `08/ui/core/lua/overlay.lua` | Führt convert horizontal alignment aus (Parameter: alignment). |
| `convertVerticalAlignment` | 1 | `08/ui/core/lua/overlay.lua` | Führt convert vertical alignment aus (Parameter: alignment). |
| `copyColor` | 1 | `08/ui/core/lua/monitors.lua` | Führt copy color aus (Parameter: color). |
| `create` | 5 | `08/ui/core/lua/jit/dis_mips.lua` | Führt create aus. |
| `create64` | 1 | `08/ui/core/lua/jit/dis_x86.lua` | Führt create64 aus. |
| `createAxisPropertyInfo` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt axis property info (Parameter: axisproperty). |
| `createCustomHooks` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt custom hooks. |
| `createDescriptors` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Erstellt descriptors. |
| `createFrameTexturePropertyInfo` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt frame texture property info (Parameter: textureproperty). |
| `createHeaderDescription` | 1 | `08/ui/addons/ego_targetmonitor/targetmonitor.lua` | Erstellt header description. |
| `createHotkeyPropertyInfo` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt hotkey property info (Parameter: cell, hotkeyproperty, width, height, scaling). |
| `createIconPropertyInfo` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt icon property info (Parameter: cell, iconproperty). |
| `createOverlayPropertyInfo` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt overlay property info (Parameter: widget). |
| `createSink` | 1 | `08/ui/core/lua/targetsystem.lua` | Erstellt sink (Parameter: sinkname, numElements). |
| `createTargetElement` | 1 | `08/ui/core/lua/targetsystem.lua` | Erstellt target element (Parameter: anarkElement, elementID). |
| `createTargetSystemClones` | 1 | `08/ui/core/lua/targetsystem.lua` | Erstellt target system clones (Parameter: master). |
| `createTextDescription` | 1 | `08/ui/addons/ego_targetmonitor/targetmonitor.lua` | Erstellt text description. |
| `createTextPropertyInfo` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Erstellt text property info (Parameter: cell, textproperty). |
| `create_el` | 1 | `08/ui/core/lua/jit/dis_mips.lua` | Erstellt el. |
| `create_r6` | 1 | `08/ui/core/lua/jit/dis_mips.lua` | Erstellt r6. |
| `create_r6_el` | 1 | `08/ui/core/lua/jit/dis_mips.lua` | Erstellt r6 el. |
| `ctlsub` | 2 | `08/ui/core/lua/jit/bc.lua` | Führt ctlsub aus. |
| `deactivateAdditionalIcon` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert additional icon (Parameter: iconEntry). |
| `deactivateAimTargetElement` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert aim target element. |
| `deactivateBar` | 5 | `08/ui/core/lua/infobar4.lua` | Deaktiviert bar. |
| `deactivateBar2` | 1 | `08/ui/core/lua/infobar3.lua` | Deaktiviert bar2 (Parameter: type). |
| `deactivateBottomText` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert bottom text (Parameter: targetElement). |
| `deactivateCollectable` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert collectable (Parameter: targetElement). |
| `deactivateCommanderElement` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert commander element (Parameter: targetElement). |
| `deactivateCompass` | 1 | `08/ui/core/lua/compass.lua` | Deaktiviert compass. |
| `deactivateCrosshair` | 2 | `08/ui/core/lua/crosshair handling.lua` | Deaktiviert crosshair. |
| `deactivateCutscene` | 1 | `08/ui/core/lua/monitors.lua` | Deaktiviert cutscene. |
| `deactivateDebugLine` | 1 | `08/ui/core/lua/debugline.lua` | Deaktiviert debug line. |
| `deactivateDebugOutline` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert debug outline (Parameter: targetElement). |
| `deactivateDronePanel` | 1 | `08/ui/core/lua/crosshair handling.lua` | Deaktiviert drone panel. |
| `deactivateDroneType` | 1 | `08/ui/core/lua/crosshair handling.lua` | Deaktiviert drone type (Parameter: dronePanelEntry). |
| `deactivateFactionLadder` | 1 | `08/ui/core/lua/monitors.lua` | Deaktiviert faction ladder. |
| `deactivateFill` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert fill (Parameter: targetElement). |
| `deactivateHullShield` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert hull shield (Parameter: targetElement). |
| `deactivateIcon` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert icon (Parameter: targetElement). |
| `deactivateIconElements` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert icon elements (Parameter: targetElement). |
| `deactivateInteractElement` | 1 | `08/ui/core/lua/crosshair handling.lua` | Deaktiviert interact element. |
| `deactivateInteraction` | 1 | `08/ui/core/lua/monitors.lua` | Deaktiviert interaction. |
| `deactivateMessageTickerLine` | 1 | `08/ui/core/lua/monitors.lua` | Deaktiviert message ticker line (Parameter: line). |
| `deactivateMissileIncoming` | 1 | `08/ui/core/lua/crosshair handling.lua` | Deaktiviert missile incoming. |
| `deactivateMissileLock` | 1 | `08/ui/core/lua/crosshair handling.lua` | Deaktiviert missile lock. |
| `deactivateMissileLocks` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert missile locks. |
| `deactivateMissionArrow` | 2 | `08/ui/core/lua/crosshair handling.lua` | Deaktiviert mission arrow. |
| `deactivateMonitor` | 1 | `08/ui/core/lua/monitors.lua` | Deaktiviert monitor (Parameter: playSound). |
| `deactivateOffScreenBox` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert off screen box (Parameter: targetElement). |
| `deactivateOutline` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert outline (Parameter: targetElement). |
| `deactivateOverlay` | 2 | `08/ui/core/lua/monitors.lua` | Deaktiviert overlay. |
| `deactivateOxygenBar` | 1 | `08/ui/core/lua/crosshair handling.lua` | Deaktiviert oxygen bar. |
| `deactivatePlayerShieldbar` | 1 | `08/ui/core/lua/crosshair handling.lua` | Deaktiviert player shieldbar. |
| `deactivateProgressbar` | 1 | `08/ui/core/lua/crosshair handling.lua` | Deaktiviert progressbar (Parameter: type). |
| `deactivatePromo` | 1 | `08/ui/core/lua/promo.lua` | Deaktiviert promo. |
| `deactivateRadarPicking` | 1 | `08/ui/core/lua/monitors.lua` | Deaktiviert radar picking. |
| `deactivateRectangleElements` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert rectangle elements (Parameter: targetElement). |
| `deactivateSeparateRadar` | 1 | `08/ui/core/lua/monitors.lua` | Deaktiviert separate radar. |
| `deactivateSeta` | 1 | `08/ui/core/lua/crosshair handling.lua` | Deaktiviert seta (Parameter: force). |
| `deactivateSideText` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert side text (Parameter: targetElement). |
| `deactivateSideText2` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert side text2 (Parameter: targetElement). |
| `deactivateSofttarget` | 1 | `08/ui/core/lua/firstperson_crosshair.lua` | Deaktiviert softtarget. |
| `deactivateState` | 1 | `08/ui/core/lua/monitors.lua` | Deaktiviert state (Parameter: state, refresh, keepCutscene). |
| `deactivateTargetArrow` | 1 | `08/ui/core/lua/crosshair handling.lua` | Deaktiviert target arrow. |
| `deactivateTargetIndicator` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert target indicator (Parameter: targetElement). |
| `deactivateTargetMonitorNotification` | 1 | `08/ui/core/lua/monitors.lua` | Deaktiviert target monitor notification. |
| `deactivateTargetMonitorRadar` | 1 | `08/ui/core/lua/monitors.lua` | Deaktiviert target monitor radar. |
| `deactivateTargetRectangle` | 1 | `08/ui/core/lua/targetsystem.lua` | Deaktiviert target rectangle (Parameter: targetElement). |
| `deactivateWeaponPanel` | 1 | `08/ui/core/lua/crosshair handling.lua` | Deaktiviert weapon panel. |
| `decode_imm13` | 1 | `08/ui/core/lua/jit/dis_arm64.lua` | Führt decode imm13 aus. |
| `deg2rad` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt deg2rad aus (Parameter: angle). |
| `detectmodname` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt detectmodname aus. |
| `detecttype` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt detecttype aus. |
| `disableDroneTypeInteractions` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt disable drone type interactions aus (Parameter: dronePanelEntry). |
| `disass` | 5 | `08/ui/core/lua/jit/dis_mips.lua` | Führt disass aus. |
| `disass64` | 1 | `08/ui/core/lua/jit/dis_x86.lua` | Führt disass64 aus. |
| `disass_block` | 5 | `08/ui/core/lua/jit/dis_mips.lua` | Führt disass block aus. |
| `disass_el` | 1 | `08/ui/core/lua/jit/dis_mips.lua` | Führt disass el aus. |
| `disass_ins` | 4 | `08/ui/core/lua/jit/dis_mips.lua` | Führt disass ins aus. |
| `disass_r6` | 1 | `08/ui/core/lua/jit/dis_mips.lua` | Führt disass r6 aus. |
| `disass_r6_el` | 1 | `08/ui/core/lua/jit/dis_mips.lua` | Führt disass r6 el aus. |
| `disconnectElement` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt disconnect element aus (Parameter: targetElement). |
| `dispatch` | 1 | `08/ui/core/lua/jit/dis_x86.lua` | Führt dispatch aus. |
| `dispatchmap` | 1 | `08/ui/core/lua/jit/dis_x86.lua` | Führt dispatchmap aus. |
| `displayAimTargetElement` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt display aim target element aus (Parameter: targetElement). |
| `displayInactiveMissionLine` | 1 | `08/ui/core/lua/monitors.lua` | Führt display inactive mission line aus (Parameter: numInactiveMissions). |
| `displayMissionBar` | 1 | `08/ui/core/lua/monitors.lua` | Führt display mission bar aus (Parameter: text). |
| `displayMissionDetails` | 1 | `08/ui/core/lua/monitors.lua` | Führt display mission details aus (Parameter: missionInfo, blinking). |
| `docmd` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt docmd aus. |
| `dump_ir` | 1 | `08/ui/core/lua/jit/dump.lua` | Führt dump ir aus. |
| `dump_mcode` | 1 | `08/ui/core/lua/jit/dump.lua` | Führt dump mcode aus. |
| `dump_record` | 1 | `08/ui/core/lua/jit/dump.lua` | Führt dump record aus. |
| `dump_snap` | 1 | `08/ui/core/lua/jit/dump.lua` | Führt dump snap aus. |
| `dump_texit` | 1 | `08/ui/core/lua/jit/dump.lua` | Führt dump texit aus. |
| `dump_trace` | 2 | `08/ui/core/lua/jit/dump.lua` | Führt dump trace aus. |
| `dumpcallargs` | 1 | `08/ui/core/lua/jit/dump.lua` | Führt dumpcallargs aus. |
| `dumpcallfunc` | 1 | `08/ui/core/lua/jit/dump.lua` | Führt dumpcallfunc aus. |
| `dumpoff` | 2 | `08/ui/core/lua/jit/dump.lua` | Führt dumpoff aus. |
| `dumpon` | 2 | `08/ui/core/lua/jit/dump.lua` | Führt dumpon aus. |
| `dumpwrite` | 1 | `08/ui/core/lua/jit/dump.lua` | Führt dumpwrite aus. |
| `enableDroneTypeInteractions` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt enable drone type interactions aus (Parameter: dronePanelEntry). |
| `enableRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt enable radar aus (Parameter: enable). |
| `enableSeparateRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt enable separate radar aus (Parameter: enable). |
| `estimateString` | 1 | `08/ui/addons/ego_targetmonitor/targetmonitor.lua` | Führt estimate string aus. |
| `exp` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt exp aus. |
| `f16` | 2 | `08/ui/core/lua/jit/bcsave.lua` | Führt f16 aus (Parameter: x). |
| `f32` | 2 | `08/ui/core/lua/jit/bcsave.lua` | Führt f32 aus. |
| `fillsymtab` | 1 | `08/ui/core/lua/jit/dump.lua` | Führt fillsymtab aus. |
| `fillsymtab_tr` | 1 | `08/ui/core/lua/jit/dump.lua` | Führt fillsymtab tr aus. |
| `finalizeFlowchartCellSlots` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt finalize flowchart cell slots aus (Parameter: cell, slottype, edges, colorprop, rankprop, slotfield). |
| `finalizeTableColumnWidths` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt finalize table column widths aus (Parameter: ftable). |
| `finishScan` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt finish scan aus. |
| `fixFunctionInput` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt fix function input aus. |
| `fmt_hex32` | 1 | `08/ui/core/lua/jit/dis_arm64.lua` | Führt fmt hex32 aus. |
| `fmterr` | 2 | `08/ui/core/lua/jit/dump.lua` | Führt fmterr aus. |
| `fmtfunc` | 2 | `08/ui/core/lua/jit/dump.lua` | Führt fmtfunc aus. |
| `fmtload` | 1 | `08/ui/core/lua/jit/dis_arm.lua` | Führt fmtload aus. |
| `fmtvload` | 1 | `08/ui/core/lua/jit/dis_arm.lua` | Führt fmtvload aus. |
| `fmtvr` | 1 | `08/ui/core/lua/jit/dis_arm.lua` | Führt fmtvr aus. |
| `fofs` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt fofs aus (Parameter: x). |
| `formatk` | 1 | `08/ui/core/lua/jit/dump.lua` | Führt formatk aus. |
| `getAimAtTargetIndicatorPosition` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt aim at target indicator position zurück (Parameter: targetElement). |
| `getCameraDistanceBasedParameterValue` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt camera distance based parameter value zurück (Parameter: cameraDistance, minvalue). |
| `getCellHeight` | 1 | `08/ui/core/lua/overlay.lua` | Gibt cell height zurück (Parameter: width, celldata). |
| `getColor` | 9 | `08/ui/core/lua/infobar4.lua` | Gibt color zurück. |
| `getColors` | 6 | `08/ui/core/lua/crosshair handling.lua` | Gibt colors zurück. |
| `getComponentHUDIcon` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt component hudicon zurück (Parameter: targetElement). |
| `getComponentIcon` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt component icon zurück (Parameter: targetElement). |
| `getCounterMeasurePosition` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt counter measure position zurück (Parameter: counterMeasureElement). |
| `getCurrentCrosshairMessage` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt current crosshair message zurück. |
| `getCurrentType` | 1 | `08/ui/core/lua/infobar3.lua` | Gibt current type zurück (Parameter: isexternal). |
| `getDebugMessage` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Gibt debug message zurück (Parameter: messageID). |
| `getDistanceText` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt distance text zurück (Parameter: distance). |
| `getHeaderName` | 1 | `08/ui/addons/ego_targetmonitor/targetmonitor.lua` | Gibt header name zurück. |
| `getIconSize` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt icon size zurück (Parameter: onScreen, useRectangleElementSize, ismouseover). |
| `getLEDColor` | 1 | `08/ui/core/lua/monitors.lua` | Gibt ledcolor zurück (Parameter: LEDElementNumber, relationLEDValue). |
| `getMinTargetDelay` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt min target delay zurück (Parameter: hasCurrentTarget). |
| `getOverlayCellData` | 1 | `08/ui/core/lua/overlay.lua` | Gibt overlay cell data zurück. |
| `getPOIIcon` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt poiicon zurück (Parameter: targetElement, poiType). |
| `getPointerID` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt pointer id zurück (Parameter: actionPointer, isSofttarget, hasVisibleAction, isInstantAction, isInactiveState, interactMenuOpen). |
| `getRectanglePositions` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt rectangle positions zurück (Parameter: targetElement). |
| `getSectionBaseParam` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Gibt section base param zurück (Parameter: menu). |
| `getShipOrLaserTowerSize` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt ship or laser tower size zurück (Parameter: targetElement). |
| `getSquareDistanceToCenter` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt square distance to center zurück (Parameter: targetElement). |
| `getTargetConeRatio` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt target cone ratio zurück (Parameter: x2d, y2d, cameraDistance, addThreshold). |
| `getTargetDataForDisplay` | 1 | `08/ui/addons/ego_targetmonitor/targetmonitor.lua` | Gibt target data for display zurück. |
| `getTargetElementByMessageID` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt target element by message id zurück (Parameter: messageID). |
| `getTargetElementByTargetSystem` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt target element by target system zurück (Parameter: targetSystem). |
| `getTargetElementPosition` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt target element position zurück (Parameter: targetElement). |
| `getTargetElementScale` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt target element scale zurück (Parameter: targetElement). |
| `getTargetIcon` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt target icon zurück (Parameter: targetElement). |
| `getTargetMonitorDetailsBridge` | 1 | `08/ui/core/lua/monitors.lua` | Gibt target monitor details bridge zurück (Parameter: componentID, connectionName, issofttarget). |
| `getTargetPriority` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt target priority zurück (Parameter: targetElement). |
| `getTextChunks` | 1 | `08/ui/core/lua/monitors.lua` | Gibt text chunks zurück (Parameter: text). |
| `getUIElementScreenPosition` | 1 | `08/ui/core/lua/targetsystem.lua` | Gibt uielement screen position zurück (Parameter: targetElement). |
| `getWareStorageName` | 1 | `08/ui/addons/ego_targetmonitor/targetmonitor.lua` | Gibt ware storage name zurück. |
| `get_be` | 1 | `08/ui/core/lua/jit/dis_mips.lua` | Gibt be zurück. |
| `get_le` | 1 | `08/ui/core/lua/jit/dis_mips.lua` | Gibt le zurück. |
| `getimm` | 1 | `08/ui/core/lua/jit/dis_x86.lua` | Führt getimm aus. |
| `getmrm` | 1 | `08/ui/core/lua/jit/dis_x86.lua` | Führt getmrm aus. |
| `h_list` | 1 | `08/ui/core/lua/jit/bc.lua` | Führt h list aus. |
| `handleMouseClick` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt handle mouse click aus (Parameter: element, delayed, mousebuttonid, modifiers). |
| `handleMouseClickRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt handle mouse click radar aus (Parameter: mousebuttonid, modifiers). |
| `handleMouseDown` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt handle mouse down aus (Parameter: element, delayed, mousebuttonid, modifiers). |
| `handleMouseDownRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt handle mouse down radar aus (Parameter: mousebuttonid, modifiers). |
| `hasActions` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt has actions aus (Parameter: targetElement). |
| `hasEntityInventory` | 1 | `08/ui/addons/ego_targetmonitor/targetmonitor.lua` | Führt has entity inventory aus. |
| `hasInventory` | 1 | `08/ui/addons/ego_targetmonitor/targetmonitor.lua` | Führt has inventory aus. |
| `hasPossibleActions` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt has possible actions aus (Parameter: targetElement). |
| `hasVisibleActions` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt has visible actions aus (Parameter: targetElement). |
| `hideAimTargetElement` | 1 | `08/ui/core/lua/targetsystem.lua` | Versteckt aim target element. |
| `hideBar` | 1 | `08/ui/core/lua/subchannelbar.lua` | Versteckt bar. |
| `hideCells` | 1 | `08/ui/core/lua/overlay.lua` | Versteckt cells. |
| `hideCompass` | 1 | `08/ui/core/lua/compass.lua` | Versteckt compass. |
| `hideDebugLine` | 1 | `08/ui/core/lua/debugline.lua` | Versteckt debug line. |
| `hideDebugLog` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Versteckt debug log. |
| `hideDebugOutline` | 1 | `08/ui/core/lua/targetsystem.lua` | Versteckt debug outline (Parameter: targetElement). |
| `hideDialogMenu` | 1 | `08/ui/core/lua/dialogmenu.lua` | Versteckt dialog menu. |
| `hideEnvironmentInfo` | 1 | `08/ui/core/lua/monitors.lua` | Versteckt environment info. |
| `hideFPSCounter` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Versteckt fpscounter. |
| `hideMissionDetails` | 1 | `08/ui/core/lua/monitors.lua` | Versteckt mission details. |
| `hideMouseOverText` | 1 | `08/ui/core/lua/dialogmenu.lua` | Versteckt mouse over text. |
| `hideNotorietyBar` | 1 | `08/ui/core/lua/monitors.lua` | Versteckt notoriety bar. |
| `hideOverlay` | 1 | `08/ui/core/lua/overlay.lua` | Versteckt overlay. |
| `hidePromo` | 1 | `08/ui/core/lua/promo.lua` | Versteckt promo. |
| `hideSkipNote` | 1 | `08/ui/core/lua/subchannelbar.lua` | Versteckt skip note. |
| `hideSofttarget` | 1 | `08/ui/core/lua/monitors.lua` | Versteckt softtarget. |
| `hideTargetMonitorNotification` | 1 | `08/ui/core/lua/monitors.lua` | Versteckt target monitor notification. |
| `incomplete` | 1 | `08/ui/core/lua/jit/dis_x86.lua` | Führt incomplete aus. |
| `init` | 38 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Führt init aus. |
| `initButtonList` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt init button list aus (Parameter: buttons). |
| `initCells` | 1 | `08/ui/core/lua/overlay.lua` | Führt init cells aus. |
| `initDebugLogData` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt init debug log data aus. |
| `initDronePanel` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt init drone panel aus. |
| `initDynamicTargetElementData` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt init dynamic target element data aus (Parameter: targetElement, messageDetails). |
| `initEnvironmentObjectSupport` | 1 | `08/ui/core/lua/monitors.lua` | Führt init environment object support aus (Parameter: contract). |
| `initIcon` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt init icon aus (Parameter: targetElement, displayState, selectedActionIcon, activeActionIcon, inactiveActionIcon). |
| `initMissionBarScale` | 1 | `08/ui/core/lua/monitors.lua` | Führt init mission bar scale aus. |
| `initMousePicking` | 2 | `08/ui/core/lua/dialogmenu.lua` | Führt init mouse picking aus. |
| `initNotifications` | 1 | `08/ui/core/lua/monitors.lua` | Führt init notifications aus. |
| `initNotorietyData` | 1 | `08/ui/core/lua/monitors.lua` | Führt init notoriety data aus (Parameter: description). |
| `initPlayerHullShield` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt init player hull shield aus. |
| `initPointerPicking` | 1 | `08/ui/core/lua/monitors.lua` | Führt init pointer picking aus. |
| `initProverb` | 1 | `08/ui/core/lua/loading.lua` | Führt init proverb aus (Parameter: textElement, numProverbs). |
| `initRadarPicking` | 1 | `08/ui/core/lua/monitors.lua` | Führt init radar picking aus. |
| `initScale` | 14 | `08/ui/core/lua/crosshair handling.lua` | Führt init scale aus (Parameter: anchorElement). |
| `initSeta` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt init seta aus (Parameter: hasSeta). |
| `initTableCell` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt init table cell aus (Parameter: cell, widgettype, properties). |
| `initTargetElement` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt init target element aus (Parameter: targetElement, displayState, selectedActionIcon, activeActionIcon, inactiveActionIcon). |
| `initVRTexts` | 1 | `08/ui/core/lua/loading.lua` | Führt init vrtexts aus. |
| `initWeaponPanel` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt init weapon panel aus. |
| `insertInput` | 2 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt insert input aus. |
| `isBlinkingLED` | 1 | `08/ui/core/lua/monitors.lua` | Prüft ob blinking led (Parameter: LEDElementNumber, relationLEDValue, boostActive). |
| `isCrosshairTarget` | 1 | `08/ui/core/lua/targetsystem.lua` | Prüft ob crosshair target (Parameter: targetElement). |
| `isCurrentAimTargetElementActive` | 1 | `08/ui/core/lua/targetsystem.lua` | Prüft ob current aim target element active (Parameter: targetElement). |
| `isDebugLogActive` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Prüft ob debug log active. |
| `isFirstPersonMode` | 1 | `08/ui/core/lua/targetsystem.lua` | Prüft ob first person mode. |
| `isHighestState` | 1 | `08/ui/core/lua/monitors.lua` | Prüft ob highest state (Parameter: state). |
| `isIconPropertyFunctionCell` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Prüft ob icon property function cell (Parameter: cell, iconproperty). |
| `isInTargetCone` | 1 | `08/ui/core/lua/targetsystem.lua` | Prüft ob in target cone (Parameter: x, y, cameraDistance, addThreshold, message). |
| `isInWeaponRange` | 1 | `08/ui/core/lua/targetsystem.lua` | Prüft ob in weapon range (Parameter: targetElement). |
| `isInactiveTargetElementState` | 1 | `08/ui/core/lua/targetsystem.lua` | Prüft ob inactive target element state (Parameter: targetElement). |
| `isObstructed` | 1 | `08/ui/core/lua/targetsystem.lua` | Prüft ob obstructed (Parameter: targetElement). |
| `isSeparateRadarEnabled` | 1 | `08/ui/core/lua/monitors.lua` | Prüft ob separate radar enabled. |
| `isShipPOI` | 1 | `08/ui/core/lua/targetsystem.lua` | Prüft ob ship poi (Parameter: targetElement). |
| `isSmallShip` | 1 | `08/ui/core/lua/targetsystem.lua` | Prüft ob small ship (Parameter: targetElement). |
| `isSomethingToDisplay` | 1 | `08/ui/core/lua/monitors.lua` | Prüft ob something to display (Parameter: details). |
| `isTargetElementPendingDeletion` | 1 | `08/ui/core/lua/targetsystem.lua` | Prüft ob target element pending deletion (Parameter: targetElement). |
| `isTargetMonitorRadarEnabled` | 1 | `08/ui/core/lua/monitors.lua` | Prüft ob target monitor radar enabled. |
| `isTargetable` | 1 | `08/ui/core/lua/targetsystem.lua` | Prüft ob targetable (Parameter: targetElement). |
| `isTextPropertyFunctionCell` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Prüft ob text property function cell (Parameter: cell, textproperty). |
| `isValidTargetMonitorDetailsBridgeData` | 1 | `08/ui/core/lua/monitors.lua` | Prüft ob valid target monitor details bridge data (Parameter: details). |
| `leaveDialogMenu` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt leave dialog menu aus (Parameter: button). |
| `lerpColorModeColor` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt lerp color mode color aus (Parameter: colorEntry, colorMode, t). |
| `makeTargetElementKnown` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt make target element known aus (Parameter: targetElement). |
| `maprs_popS` | 1 | `08/ui/core/lua/jit/dis_mips.lua` | Führt maprs pop s aus. |
| `maprs_popST` | 1 | `08/ui/core/lua/jit/dis_mips.lua` | Führt maprs pop st aus. |
| `maprs_popTS` | 1 | `08/ui/core/lua/jit/dis_mips.lua` | Führt maprs pop ts aus. |
| `match_reg` | 1 | `08/ui/core/lua/jit/dis_arm64.lua` | Führt match reg aus. |
| `menu.accountSetEstimate` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt account set estimate aus (Parameter: container, isbuildstorage). |
| `menu.actionOperationTime` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Führt action operation time aus (Parameter: endtime). |
| `menu.addCapacityRow` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Fügt capacity row hinzu (Parameter: data). |
| `menu.addClusterOffsetRow` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Fügt cluster offset row hinzu (Parameter: ftable, name, coord). |
| `menu.addConsumableEntry` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Fügt consumable entry hinzu (Parameter: basesection, consumabledata, object, callback). |
| `menu.addCrewSection` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Fügt crew section hinzu (Parameter: mode, inputtable, inputobject, instance, infocrew, operatorinfo, aipilot, isplayerowned). |
| `menu.addDetailRow` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Fügt detail row hinzu (Parameter: ftable, col1, col2, col3, offsetx, iswordwrap, properties1, properties2, properties3). |
| `menu.addDetailRows` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Fügt detail rows hinzu (Parameter: ftable). |
| `menu.addEngineDetailRow` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Fügt engine detail row hinzu (Parameter: ftable, name, thruster, hasdefaultloadout). |
| `menu.addEntry` | 1 | `08/ui/addons/ego_detailmonitor/menu_transporter.lua` | Fügt entry hinzu (Parameter: ftable, target, indent, parentcomponent). |
| `menu.addEquipmentModInfoRow` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Fügt equipment mod info row hinzu (Parameter: inputtable, modclass, installedmod, name). |
| `menu.addHQ` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Fügt hq hinzu. |
| `menu.addIndexEntry` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Fügt index entry hinzu (Parameter: array, item, name, rowdata, indent, numentries, expanded). |
| `menu.addInfoSubmenuRow` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Fügt info submenu row hinzu (Parameter: instance, inputtable, inputrow, inputrowdata, isheader, withbutton, buttonactive, indent, indentsize, inputfont, mouseovertext, interactive). |
| `menu.addInternallyStoredShips` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Fügt internally stored ships hinzu (Parameter: id). |
| `menu.addInventoryWareEntry` | 2 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Fügt inventory ware entry hinzu (Parameter: ftable, ware, waredata, iscrafting, isresource, hideprice, isonline). |
| `menu.addMappedButtonData` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Fügt mapped button data hinzu (Parameter: array, found, input, controltype, controlcode). |
| `menu.addMissionRow` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Fügt mission row hinzu (Parameter: ftable, missionentry, indented, seqidx). |
| `menu.addMissionToList` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Fügt mission to list hinzu (Parameter: entry). |
| `menu.addNameRows` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Fügt name rows hinzu (Parameter: ftable, component). |
| `menu.addObjectOffsetRow` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Fügt object offset row hinzu (Parameter: ftable, name, coord, suffix, converttodeg). |
| `menu.addPositionalOffsetRow` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Fügt positional offset row hinzu (Parameter: ftable, name, coord, suffix, converttodeg). |
| `menu.addProductionMethodDetails` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Fügt production method details hinzu (Parameter: ftable, resourcestring, methodstring, showtime, showamount). |
| `menu.addRowDockedShips` | 1 | `08/ui/addons/ego_detailmonitor/menu_platformundock.lua` | Fügt row docked ships hinzu (Parameter: object, shiptable, indent). |
| `menu.addSatellite` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Fügt satellite hinzu (Parameter: sector, id, x, z). |
| `menu.addSavegameRow` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Fügt savegame row hinzu (Parameter: ftable, savegame, name, slot). |
| `menu.addSectionTitle` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Fügt section title hinzu (Parameter: ftable, section, first). |
| `menu.addSelectedComponent` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Fügt selected component hinzu (Parameter: component, clear, noupdate). |
| `menu.addSelectedComponents` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Fügt selected components hinzu (Parameter: components, clear). |
| `menu.addShipToBoardingOperation` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Fügt ship to boarding operation hinzu (Parameter: shipid, shipdata). |
| `menu.addUndoStep` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Fügt undo step hinzu (Parameter: upgradeplan, crew). |
| `menu.addWareInfoButtonRow` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Fügt ware info button row hinzu (Parameter: data). |
| `menu.agentActionIconColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Führt agent action icon color aus. |
| `menu.allowResetView` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt allow reset view aus. |
| `menu.applyFilterSettings` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Wendet filter settings an (Parameter: noupdate). |
| `menu.applySettings` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Wendet settings an. |
| `menu.areTurretsArmed` | 3 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt are turrets armed aus (Parameter: defensible). |
| `menu.budgetHeaderName` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt budget header name aus (Parameter: budgetid). |
| `menu.budgetHeaderText` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt budget header text aus (Parameter: budgetid). |
| `menu.buttonAbort` | 1 | `08/ui/addons/ego_detailmonitor/menu_missionbriefing.lua` | Führt button abort aus (Parameter: confirmed). |
| `menu.buttonAbortAction` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Führt button abort action aus (Parameter: agentid, confirmed, unique, exclusivefactionidx, cooldown). |
| `menu.buttonAbortProject` | 1 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Führt button abort project aus. |
| `menu.buttonAccept` | 1 | `08/ui/addons/ego_detailmonitor/menu_missionbriefing.lua` | Führt button accept aus. |
| `menu.buttonAccountAllEstimates` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button account all estimates aus. |
| `menu.buttonAccountCancel` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button account cancel aus. |
| `menu.buttonAccountConfirm` | 3 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button account confirm aus. |
| `menu.buttonAccountToEstimate` | 3 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button account to estimate aus (Parameter: container, isbuildstorage). |
| `menu.buttonActivate` | 1 | `08/ui/addons/ego_detailmonitor/menu_missionbriefing.lua` | Führt button activate aus. |
| `menu.buttonActivateDeployables` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button activate deployables aus (Parameter: isactive). |
| `menu.buttonActiveSubordinateGroupLaunch` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button active subordinate group launch aus (Parameter: inputobject, i). |
| `menu.buttonAddControl` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button add control aus (Parameter: row, data). |
| `menu.buttonAddModifier` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button add modifier aus (Parameter: row, modifier). |
| `menu.buttonAddModule` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button add module aus (Parameter: macro, row, col). |
| `menu.buttonAddPurchase` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button add purchase aus (Parameter: hasupgrades, hasrepairs). |
| `menu.buttonAddSector` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Führt button add sector aus (Parameter: cluster). |
| `menu.buttonAddShip` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_comparison.lua` | Führt button add ship aus. |
| `menu.buttonAddSplinePoint` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Führt button add spline point aus (Parameter: i). |
| `menu.buttonArmTurrets` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button arm turrets aus (Parameter: armed). |
| `menu.buttonAssignCommander` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button assign commander aus (Parameter: assignment, group). |
| `menu.buttonAssignConstructionVessel` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button assign construction vessel aus. |
| `menu.buttonAssignFleetUnitCommander` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button assign fleet unit commander aus (Parameter: assignment, group). |
| `menu.buttonAttack` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button attack aus (Parameter: clear). |
| `menu.buttonAttackInRange` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button attack in range aus. |
| `menu.buttonAttackMultiple` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button attack multiple aus (Parameter: clear). |
| `menu.buttonAttackSurfaceElements` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button attack surface elements aus (Parameter: target, targetclass, clear). |
| `menu.buttonAutoPilot` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt button auto pilot aus. |
| `menu.buttonBehaviourInspection` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button behaviour inspection aus. |
| `menu.buttonBlacklistAddFaction` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button blacklist add faction aus (Parameter: x, y). |
| `menu.buttonBlacklistAddMacro` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button blacklist add macro aus (Parameter: x, y). |
| `menu.buttonBlacklistCheckChanges` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button blacklist check changes aus. |
| `menu.buttonBlacklistConfirm` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button blacklist confirm aus. |
| `menu.buttonBlacklistRemove` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button blacklist remove aus. |
| `menu.buttonBlacklistRemoveFaction` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button blacklist remove faction aus (Parameter: faction). |
| `menu.buttonBlacklistRemoveMacro` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button blacklist remove macro aus (Parameter: spaceid). |
| `menu.buttonBlacklistReset` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button blacklist reset aus. |
| `menu.buttonBoard` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button board aus. |
| `menu.buttonBoardingAddShip` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button boarding add ship aus. |
| `menu.buttonBoardingRemoveShip` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button boarding remove ship aus (Parameter: shipid). |
| `menu.buttonBoolProperty` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt button bool property aus (Parameter: property). |
| `menu.buttonBuyPlot` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button buy plot aus. |
| `menu.buttonBuyShip` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt button buy ship aus. |
| `menu.buttonCPRemoveCancel` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button cpremove cancel aus. |
| `menu.buttonCPRemoveConfirm` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button cpremove confirm aus. |
| `menu.buttonCancel` | 3 | `08/ui/addons/ego_detailmonitor/menu_trader_blueprintsorlicences.lua` | Führt button cancel aus. |
| `menu.buttonCancelAllConstruction` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button cancel all construction aus. |
| `menu.buttonCancelCancel` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button cancel cancel aus. |
| `menu.buttonCancelConfirm` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button cancel confirm aus. |
| `menu.buttonCancelConstruction` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button cancel construction aus. |
| `menu.buttonCancelLoadout` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button cancel loadout aus. |
| `menu.buttonCancelResearch` | 1 | `08/ui/addons/ego_detailmonitor/menu_research.lua` | Führt button cancel research aus (Parameter: techdata). |
| `menu.buttonCancelTrade` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button cancel trade aus. |
| `menu.buttonCancelTradeActive` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button cancel trade active aus (Parameter: tradeid). |
| `menu.buttonCancelWeaponConfig` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button cancel weapon config aus. |
| `menu.buttonChangeAssignment` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button change assignment aus (Parameter: assignment, group). |
| `menu.buttonChangeFleetUnitAssignment` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button change fleet unit assignment aus (Parameter: assignment, group). |
| `menu.buttonChangeLogo` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button change logo aus. |
| `menu.buttonChangeLogoCancel` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button change logo cancel aus. |
| `menu.buttonChangeOverrideOrder` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button change override order aus (Parameter: idstring, attacker). |
| `menu.buttonClaim` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button claim aus (Parameter: selectedship). |
| `menu.buttonClearCustomShipName` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button clear custom ship name aus. |
| `menu.buttonClearEditbox` | 2 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button clear editbox aus (Parameter: row). |
| `menu.buttonClearWeaponConfig` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button clear weapon config aus. |
| `menu.buttonClosePrivateChat` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt button close private chat aus (Parameter: idx). |
| `menu.buttonCollapseStats` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button collapse stats aus. |
| `menu.buttonCollect` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button collect aus. |
| `menu.buttonCollectDeployable` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button collect deployable aus (Parameter: clear). |
| `menu.buttonCollectDeployables` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button collect deployables aus (Parameter: clear). |
| `menu.buttonCollectLockbox` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button collect lockbox aus. |
| `menu.buttonCollectRadius` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button collect radius aus. |
| `menu.buttonComm` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button comm aus. |
| `menu.buttonConfirm` | 4 | `08/ui/addons/ego_detailmonitor/menu_trader_blueprintsorlicences.lua` | Führt button confirm aus. |
| `menu.buttonConfirmColor` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button confirm color aus. |
| `menu.buttonConfirmConvertVentureSave` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button confirm convert venture save aus. |
| `menu.buttonConfirmLoadout` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button confirm loadout aus. |
| `menu.buttonConfirmMoney` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button confirm money aus. |
| `menu.buttonConfirmPlannedDefaultOrderActive` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button confirm planned default order active aus (Parameter: instance, isvalid). |
| `menu.buttonConfirmPurchaseEdit` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button confirm purchase edit aus (Parameter: hasupgrades, hasrepairs). |
| `menu.buttonConfirmTrade` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button confirm trade aus. |
| `menu.buttonConfirmTradeLoop` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button confirm trade loop aus. |
| `menu.buttonConfirmUserQuestion` | 3 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button confirm user question aus. |
| `menu.buttonConfirmWeaponConfig` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button confirm weapon config aus. |
| `menu.buttonConstructionCommunity` | 2 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt button construction community aus. |
| `menu.buttonContactMessage` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt button contact message aus (Parameter: menu, userid, username). |
| `menu.buttonContainerInfo` | 2 | `08/ui/addons/ego_detailmonitor/menu_transactionlog.lua` | Führt button container info aus (Parameter: controllable). |
| `menu.buttonContextEncyclopedia` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button context encyclopedia aus (Parameter: selectedUpgrade). |
| `menu.buttonContextModifiedConfirm` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button context modified confirm aus. |
| `menu.buttonContextRemapConfirm` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button context remap confirm aus. |
| `menu.buttonContextRemoveControllerInputConfirm` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button context remove controller input confirm aus. |
| `menu.buttonContextResearch` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button context research aus. |
| `menu.buttonContextSetLogo` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button context set logo aus (Parameter: logo). |
| `menu.buttonContextTrade` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button context trade aus (Parameter: wareexchange). |
| `menu.buttonContextTradeLoop` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button context trade loop aus. |
| `menu.buttonControl` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button control aus (Parameter: row, data). |
| `menu.buttonConvertVentureSave` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button convert venture save aus. |
| `menu.buttonCopyModule` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button copy module aus (Parameter: module, copysequence). |
| `menu.buttonCover` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt button cover aus (Parameter: faction). |
| `menu.buttonCrewTransfer` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button crew transfer aus (Parameter: othership). |
| `menu.buttonCrewTransferConfirm` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button crew transfer confirm aus. |
| `menu.buttonCrewTransferExtend` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button crew transfer extend aus (Parameter: i, j). |
| `menu.buttonCrewTransferToggleList` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button crew transfer toggle list aus. |
| `menu.buttonCustomShipNameAppendLoadout` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button custom ship name append loadout aus. |
| `menu.buttonCustomShipNameAppendShip` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button custom ship name append ship aus (Parameter: name). |
| `menu.buttonDecline` | 1 | `08/ui/addons/ego_detailmonitor/menu_missionbriefing.lua` | Führt button decline aus. |
| `menu.buttonDefaultOrderConfirm` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button default order confirm aus (Parameter: instance). |
| `menu.buttonDefaultOrderDiscard` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button default order discard aus (Parameter: instance). |
| `menu.buttonDeleteAllOrders` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button delete all orders aus (Parameter: instance). |
| `menu.buttonDeleteModifier` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button delete modifier aus (Parameter: modifier, source, code, lastkey). |
| `menu.buttonDeleteSave` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button delete save aus. |
| `menu.buttonDeliverWares` | 2 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button deliver wares aus (Parameter: missionid). |
| `menu.buttonDeploy` | 2 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button deploy aus (Parameter: type, macro, amount). |
| `menu.buttonDeployAtPosition` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button deploy at position aus (Parameter: type, macro, amount). |
| `menu.buttonDeployToStation` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button deploy to station aus (Parameter: selectedbuilder, clear, target). |
| `menu.buttonDepositAll` | 1 | `08/ui/addons/ego_detailmonitor/menu_trader_inventory.lua` | Führt button deposit all aus. |
| `menu.buttonDepositAllActive` | 1 | `08/ui/addons/ego_detailmonitor/menu_trader_inventory.lua` | Führt button deposit all active aus. |
| `menu.buttonDepositInventoryAtHQ` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button deposit inventory at hq aus. |
| `menu.buttonDiscardShoppingListAndEditGroup` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button discard shopping list and edit group aus (Parameter: group, shipid). |
| `menu.buttonDismantleMod` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button dismantle mod aus (Parameter: type, component, context, group). |
| `menu.buttonDock` | 2 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button dock aus (Parameter: clear, ventureplatform). |
| `menu.buttonDockAtPlayer` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button dock at player aus (Parameter: clear). |
| `menu.buttonDockRequest` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button dock request aus. |
| `menu.buttonDockToTrade` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button dock to trade aus. |
| `menu.buttonDockedShipInfo` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt button docked ship info aus. |
| `menu.buttonDrag` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt button drag aus. |
| `menu.buttonDropInventory` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button drop inventory aus (Parameter: pilot). |
| `menu.buttonDropPilotInventory` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button drop pilot inventory aus (Parameter: pilot, wares). |
| `menu.buttonEditBlacklist` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button edit blacklist aus (Parameter: blacklistid). |
| `menu.buttonEditColor` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button edit color aus (Parameter: colorid). |
| `menu.buttonEditFightRule` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button edit fight rule aus (Parameter: fightruleid). |
| `menu.buttonEditLoadout` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button edit loadout aus (Parameter: module). |
| `menu.buttonEditPurchase` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button edit purchase aus (Parameter: idx). |
| `menu.buttonEditShip` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_comparison.lua` | Führt button edit ship aus (Parameter: id). |
| `menu.buttonEditTradeRule` | 3 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button edit trade rule aus (Parameter: traderuleid). |
| `menu.buttonEncyclopedia` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button encyclopedia aus. |
| `menu.buttonEncyclopediaLink` | 1 | `08/ui/addons/ego_detailmonitor/menu_missionbriefing.lua` | Führt button encyclopedia link aus (Parameter: briefingobjective). |
| `menu.buttonEndGuidance` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button end guidance aus. |
| `menu.buttonEquipmentFilter` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button equipment filter aus (Parameter: offsety). |
| `menu.buttonExpand` | 5 | `08/ui/addons/ego_detailmonitor/menu_trader_blueprintsorlicences.lua` | Führt button expand aus (Parameter: tag). |
| `menu.buttonExpandMissionGroup` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button expand mission group aus (Parameter: id, row, contextCallback). |
| `menu.buttonExpandProperty` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt button expand property aus (Parameter: id). |
| `menu.buttonExpandStats` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button expand stats aus. |
| `menu.buttonExplore` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button explore aus (Parameter: clear). |
| `menu.buttonExploreUpdate` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button explore update aus (Parameter: clear). |
| `menu.buttonExport` | 2 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt button export aus (Parameter: checked). |
| `menu.buttonExtend` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt button extend aus (Parameter: groupID, row). |
| `menu.buttonExtendCategory` | 1 | `08/ui/addons/ego_detailmonitor/menu_transporter.lua` | Führt button extend category aus (Parameter: category). |
| `menu.buttonExtendConstruction` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button extend construction aus (Parameter: name). |
| `menu.buttonExtendDockedShips` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button extend docked ships aus (Parameter: name, isstation). |
| `menu.buttonExtendEntry` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button extend entry aus (Parameter: index, row). |
| `menu.buttonExtendInfo` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button extend info aus (Parameter: buttondata, instance). |
| `menu.buttonExtendModuleType` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button extend module type aus (Parameter: station, type). |
| `menu.buttonExtendOrder` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button extend order aus (Parameter: controllable, orderidx, instance, row, col). |
| `menu.buttonExtendProperty` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button extend property aus (Parameter: name). |
| `menu.buttonExtendResourceEntry` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button extend resource entry aus (Parameter: index, row). |
| `menu.buttonExtendSubordinate` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button extend subordinate aus (Parameter: name, group). |
| `menu.buttonExtensionGlobalSync` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button extension global sync aus. |
| `menu.buttonExtensionUISecurityMode` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button extension uisecurity mode aus. |
| `menu.buttonExternal` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button external aus. |
| `menu.buttonFightRuleCheckChanges` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button fight rule check changes aus. |
| `menu.buttonFightRuleConfirm` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button fight rule confirm aus. |
| `menu.buttonFightRuleRemove` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button fight rule remove aus. |
| `menu.buttonFightRuleReset` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button fight rule reset aus. |
| `menu.buttonFilterSwitch` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button filter switch aus (Parameter: mode, row, col). |
| `menu.buttonFireConstructionVessel` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button fire construction vessel aus (Parameter: builder, orderidx). |
| `menu.buttonFireCrew` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button fire crew aus (Parameter: instance, object). |
| `menu.buttonFlee` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button flee aus (Parameter: attacker, clear). |
| `menu.buttonFleetManagement` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button fleet management aus (Parameter: controllable, enable). |
| `menu.buttonFlightAssist` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt button flight assist aus. |
| `menu.buttonFollow` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button follow aus (Parameter: clear). |
| `menu.buttonForceBuild` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button force build aus. |
| `menu.buttonFormationShape` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button formation shape aus (Parameter: shape, subordinates). |
| `menu.buttonGetSupplies` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button get supplies aus. |
| `menu.buttonGetUp` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt button get up aus. |
| `menu.buttonGoTo` | 1 | `08/ui/addons/ego_detailmonitor/menu_transporter.lua` | Führt button go to aus. |
| `menu.buttonGoToShip` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt button go to ship aus. |
| `menu.buttonGraphMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt button graph mode aus (Parameter: mode). |
| `menu.buttonGuidance` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button guidance aus (Parameter: useoffset). |
| `menu.buttonHire` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button hire aus. |
| `menu.buttonIllegalWares` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button illegal wares aus (Parameter: x, y). |
| `menu.buttonImport` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button import aus (Parameter: checked). |
| `menu.buttonInfo` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button info aus. |
| `menu.buttonInfoLogbookClear` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button info logbook clear aus (Parameter: instance). |
| `menu.buttonInfoLogbookClearQuestion` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button info logbook clear question aus (Parameter: instance). |
| `menu.buttonInfoSubMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button info sub mode aus (Parameter: mode, col, instance, confirmed). |
| `menu.buttonInputProfileRemove` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button input profile remove aus (Parameter: profile, slot). |
| `menu.buttonInputProfileSave` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button input profile save aus (Parameter: profile). |
| `menu.buttonInstallMod` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button install mod aus (Parameter: type, component, ware, price, context, group, dismantle). |
| `menu.buttonInstallPaintMod` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button install paint mod aus. |
| `menu.buttonInteract` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button interact aus (Parameter: selectedData, button, row, col, posx, posy). |
| `menu.buttonInteractionButton` | 1 | `08/ui/addons/ego_detailmonitor/menu_missionbriefing.lua` | Führt button interaction button aus. |
| `menu.buttonInventoryCancel` | 2 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button inventory cancel aus. |
| `menu.buttonInventoryCraft` | 2 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button inventory craft aus. |
| `menu.buttonInventoryDrop` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button inventory drop aus. |
| `menu.buttonInventoryDropAll` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button inventory drop all aus (Parameter: illegalonly). |
| `menu.buttonInventoryEncyclopedia` | 2 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button inventory encyclopedia aus (Parameter: ware). |
| `menu.buttonInventorySubMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button inventory sub mode aus (Parameter: mode, col). |
| `menu.buttonLeftBar` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button left bar aus (Parameter: mode, row, overrideMode, overrideSlot). |
| `menu.buttonLeftBarColor` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button left bar color aus (Parameter: mode, active, missing). |
| `menu.buttonLeftBarLoadout` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button left bar loadout aus (Parameter: mode, row). |
| `menu.buttonLiveStream` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button live stream aus. |
| `menu.buttonLogbookCategory` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button logbook category aus (Parameter: name, category, col). |
| `menu.buttonLogbookClear` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button logbook clear aus (Parameter: category). |
| `menu.buttonLogbookClearQuestion` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button logbook clear question aus. |
| `menu.buttonLogbookInteraction` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button logbook interaction aus (Parameter: entry). |
| `menu.buttonMapContextKnownStations` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt button map context known stations aus (Parameter: macro, checked). |
| `menu.buttonMapContextSatelliteCoverage` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt button map context satellite coverage aus (Parameter: macro, checked). |
| `menu.buttonMapContextSelectSector` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt button map context select sector aus (Parameter: macro, remove). |
| `menu.buttonMapEditorClusterCopyActive` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button map editor cluster copy active aus. |
| `menu.buttonMarkAsHostile` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button mark as hostile aus. |
| `menu.buttonMessageCategory` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button message category aus (Parameter: name, category, col). |
| `menu.buttonMessagesInteraction` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button messages interaction aus (Parameter: entry). |
| `menu.buttonMessagesRead` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button messages read aus. |
| `menu.buttonMessagesToggleCutsceneFullscreen` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button messages toggle cutscene fullscreen aus. |
| `menu.buttonMining` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button mining aus (Parameter: ware, clear). |
| `menu.buttonMissionAbort` | 2 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button mission abort aus (Parameter: missionid). |
| `menu.buttonMissionAccept` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button mission accept aus (Parameter: offerid). |
| `menu.buttonMissionActivate` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button mission activate aus. |
| `menu.buttonMissionBriefing` | 2 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button mission briefing aus (Parameter: missionid, isoffer). |
| `menu.buttonMissionDeliverWares` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button mission deliver wares aus. |
| `menu.buttonMissionInteractionButton` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button mission interaction button aus. |
| `menu.buttonMissionOfferAccept` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button mission offer accept aus. |
| `menu.buttonMissionOfferBriefing` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button mission offer briefing aus. |
| `menu.buttonMissionOfferSubMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button mission offer sub mode aus (Parameter: mode, col). |
| `menu.buttonMissionSetActive` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button mission set active aus (Parameter: missionid). |
| `menu.buttonMissionSetInactive` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button mission set inactive aus. |
| `menu.buttonMissionShow` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button mission show aus (Parameter: missionid). |
| `menu.buttonMissionSubMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button mission sub mode aus (Parameter: mode, col). |
| `menu.buttonModCategory` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button mod category aus (Parameter: category, row, col). |
| `menu.buttonModifyShip` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt button modify ship aus. |
| `menu.buttonModuleFilter` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button module filter aus (Parameter: offsety). |
| `menu.buttonMoveWait` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button move wait aus (Parameter: clear). |
| `menu.buttonMultiSelectConfirm` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt button multi select confirm aus (Parameter: property). |
| `menu.buttonNavBeaconCheat` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button nav beacon cheat aus. |
| `menu.buttonNewGame` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt button new game aus. |
| `menu.buttonNewOrder` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button new order aus (Parameter: orderid, default, instance). |
| `menu.buttonNewPlot` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button new plot aus. |
| `menu.buttonNextChannel` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt button next channel aus. |
| `menu.buttonNodus` | 1 | `08/ui/addons/ego_detailmonitor/menu_scenario_selection.lua` | Führt button nodus aus (Parameter: ftable, input, row, col). |
| `menu.buttonNodusDblClick` | 1 | `08/ui/addons/ego_detailmonitor/menu_scenario_selection.lua` | Führt button nodus dbl click aus (Parameter: scenarioid). |
| `menu.buttonObjectSorter` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button object sorter aus (Parameter: sorttype). |
| `menu.buttonObjectSubMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button object sub mode aus (Parameter: mode, col). |
| `menu.buttonOnlineHelp` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button online help aus (Parameter: helplink). |
| `menu.buttonOnlineLogin` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button online login aus. |
| `menu.buttonOnlineLogout` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button online logout aus. |
| `menu.buttonOnlineRegister` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button online register aus. |
| `menu.buttonOpenStore` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button open store aus (Parameter: extensionsource). |
| `menu.buttonOrderDown` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button order down aus (Parameter: order, instance, modified). |
| `menu.buttonOrderUp` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button order up aus (Parameter: order, instance, modified). |
| `menu.buttonOverwriteSave` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button overwrite save aus. |
| `menu.buttonOwnerCheat` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button owner cheat aus. |
| `menu.buttonPaintMod` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button paint mod aus. |
| `menu.buttonPauseProcessingModules` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt button pause processing modules aus (Parameter: processingmodules, pause). |
| `menu.buttonPauseProductionModules` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt button pause production modules aus (Parameter: productionmodules, pause). |
| `menu.buttonPerformPlayerAction` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button perform player action aus (Parameter: id, type). |
| `menu.buttonPersonnelCancelTransfer` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button personnel cancel transfer aus (Parameter: controllable, person). |
| `menu.buttonPersonnelCommWithActor` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button personnel comm with actor aus (Parameter: actor). |
| `menu.buttonPersonnelFireNPC` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button personnel fire npc aus (Parameter: controllable, entity, person). |
| `menu.buttonPersonnelFireNPCConfirm` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button personnel fire npcconfirm aus (Parameter: controllable, entity, person, name). |
| `menu.buttonPersonnelReplacePilot` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button personnel replace pilot aus (Parameter: ship, oldpilot, newpilot). |
| `menu.buttonPlayerAlertAddClass` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button player alert add class aus (Parameter: x, y). |
| `menu.buttonPlayerAlertAddFaction` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button player alert add faction aus (Parameter: x, y). |
| `menu.buttonPlayerAlertAddSpace` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button player alert add space aus (Parameter: x, y). |
| `menu.buttonPlayerAlertCheckChanges` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button player alert check changes aus. |
| `menu.buttonPlayerAlertConfirm` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button player alert confirm aus. |
| `menu.buttonPlayerAlertRemove` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button player alert remove aus. |
| `menu.buttonPlayerAlertRemoveClass` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button player alert remove class aus (Parameter: class). |
| `menu.buttonPlayerAlertRemoveFaction` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button player alert remove faction aus (Parameter: faction). |
| `menu.buttonPlayerAlertRemoveSpace` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button player alert remove space aus (Parameter: spaceid). |
| `menu.buttonPlayerAlertReset` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button player alert reset aus. |
| `menu.buttonPlayerAlertSoundTest` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button player alert sound test aus. |
| `menu.buttonPlayerDockToTrade` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button player dock to trade aus (Parameter: clear). |
| `menu.buttonPlayerSquadAttackPlayerTarget` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button player squad attack player target aus (Parameter: clear). |
| `menu.buttonPlayerSquadStopAndHoldFire` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button player squad stop and hold fire aus (Parameter: clear). |
| `menu.buttonPlayerSquadWithdrawAndHold` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button player squad withdraw and hold aus (Parameter: clear). |
| `menu.buttonPlayerSquadWithdrawFromCombat` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button player squad withdraw from combat aus (Parameter: clear). |
| `menu.buttonPrevChannel` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt button prev channel aus. |
| `menu.buttonPrimaryModifier` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button primary modifier aus (Parameter: modifier, source, code). |
| `menu.buttonPrivacyPolicy` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button privacy policy aus. |
| `menu.buttonProceedWithOrders` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button proceed with orders aus. |
| `menu.buttonPropertySorter` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button property sorter aus (Parameter: sorttype). |
| `menu.buttonPropertySubMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button property sub mode aus (Parameter: mode, col). |
| `menu.buttonProtect` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button protect aus (Parameter: clear). |
| `menu.buttonPutIntoStorage` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button put into storage aus (Parameter: container, ship). |
| `menu.buttonReadAll` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Führt button read all aus. |
| `menu.buttonRecallSubordinates` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button recall subordinates aus (Parameter: component, subordinates, level). |
| `menu.buttonReleaseSyncPoint` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button release sync point aus (Parameter: syncpointinfo). |
| `menu.buttonReloadImportable` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button reload importable aus. |
| `menu.buttonReloadLobby` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button reload lobby aus. |
| `menu.buttonReloadSaveGames` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button reload save games aus. |
| `menu.buttonRemoveAllOrders` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button remove all orders aus (Parameter: removedefaultorder, removeassignment, removedockorder). |
| `menu.buttonRemoveAssignment` | 2 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button remove assignment aus (Parameter: removeall). |
| `menu.buttonRemoveBuildStorage` | 2 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button remove build storage aus. |
| `menu.buttonRemoveControl` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button remove control aus (Parameter: row, data). |
| `menu.buttonRemoveFleetUnit` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button remove fleet unit aus. |
| `menu.buttonRemoveListParam` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button remove list param aus (Parameter: order, param, index, instance). |
| `menu.buttonRemoveModule` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button remove module aus (Parameter: module, removesequence). |
| `menu.buttonRemoveOrder` | 2 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button remove order aus. |
| `menu.buttonRemoveOrderSyncPoint` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button remove order sync point aus (Parameter: orderidx, instance). |
| `menu.buttonRemovePlayerProperty` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt button remove player property aus (Parameter: id). |
| `menu.buttonRemovePlot` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button remove plot aus (Parameter: station, confirmed, removebuildstorage). |
| `menu.buttonRemovePurchase` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button remove purchase aus (Parameter: idx). |
| `menu.buttonRemoveSearchEntry` | 3 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button remove search entry aus (Parameter: index). |
| `menu.buttonRemoveShip` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_comparison.lua` | Führt button remove ship aus (Parameter: id). |
| `menu.buttonRename` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button rename aus (Parameter: isfleet). |
| `menu.buttonRenameConfirm` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button rename confirm aus (Parameter: isconfirmed). |
| `menu.buttonReportMessage` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt button report message aus (Parameter: timestamp, author). |
| `menu.buttonReportUser` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt button report user aus (Parameter: userid). |
| `menu.buttonRequestShip` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button request ship aus. |
| `menu.buttonRescueInRange` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button rescue in range aus (Parameter: clear). |
| `menu.buttonRescueShip` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button rescue ship aus (Parameter: clear). |
| `menu.buttonReset` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt button reset aus. |
| `menu.buttonResetAll` | 1 | `08/ui/addons/ego_detailmonitor/menu_trader_inventory.lua` | Führt button reset all aus. |
| `menu.buttonResetAllActive` | 1 | `08/ui/addons/ego_detailmonitor/menu_trader_inventory.lua` | Führt button reset all active aus. |
| `menu.buttonResetBudget` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt button reset budget aus (Parameter: budgetid). |
| `menu.buttonResetControl` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button reset control aus (Parameter: row, data). |
| `menu.buttonResetCrew` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button reset crew aus. |
| `menu.buttonResetGlobalStandingOrders` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button reset global standing orders aus. |
| `menu.buttonResetModuleRotation` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button reset module rotation aus (Parameter: module). |
| `menu.buttonResetNotificationSettings` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button reset notification settings aus. |
| `menu.buttonResetView` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button reset view aus. |
| `menu.buttonResourceProbeCheat` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button resource probe cheat aus. |
| `menu.buttonRetrieveAll` | 1 | `08/ui/addons/ego_detailmonitor/menu_trader_inventory.lua` | Führt button retrieve all aus. |
| `menu.buttonRetrieveAllActive` | 1 | `08/ui/addons/ego_detailmonitor/menu_trader_inventory.lua` | Führt button retrieve all active aus. |
| `menu.buttonRightBar` | 5 | `08/ui/addons/ego_detailmonitor/menu_transactionlog.lua` | Führt button right bar aus (Parameter: newmenu, params). |
| `menu.buttonRightBarSelf` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button right bar self aus. |
| `menu.buttonSalvageCollect` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button salvage collect aus (Parameter: clear). |
| `menu.buttonSalvageCrush` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button salvage crush aus (Parameter: clear). |
| `menu.buttonSalvageDeliver` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button salvage deliver aus (Parameter: clear, ware, tradeoffer). |
| `menu.buttonSalvageDeliver_NoTrade` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button salvage deliver no trade aus. |
| `menu.buttonSalvageInRadius` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button salvage in radius aus. |
| `menu.buttonSatelliteCheat` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button satellite cheat aus. |
| `menu.buttonSave` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button save aus (Parameter: overwrite). |
| `menu.buttonSaveLoadout` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button save loadout aus (Parameter: overwrite). |
| `menu.buttonSelectBlueprint` | 1 | `08/ui/addons/ego_detailmonitor/menu_trader_blueprintsorlicences.lua` | Führt button select blueprint aus (Parameter: ware, price). |
| `menu.buttonSelectContextSetList` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button select context set list aus (Parameter: data). |
| `menu.buttonSelectFaction` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Führt button select faction aus (Parameter: factionid). |
| `menu.buttonSelectGroupUpgrade` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button select group upgrade aus (Parameter: type, group, macro, row, col, keepcontext). |
| `menu.buttonSelectHandler` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button select handler aus. |
| `menu.buttonSelectLicence` | 1 | `08/ui/addons/ego_detailmonitor/menu_trader_blueprintsorlicences.lua` | Führt button select licence aus (Parameter: licence, price). |
| `menu.buttonSelectObject` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Führt button select object aus (Parameter: actionid, paramidx, paramdata). |
| `menu.buttonSelectPaintMod` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button select paint mod aus (Parameter: entry, row, col). |
| `menu.buttonSelectRepair` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button select repair aus (Parameter: row, col, objectstring, keepcontext). |
| `menu.buttonSelectResearch` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt button select research aus (Parameter: techdata, mainIdx, col). |
| `menu.buttonSelectSector` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button select sector aus. |
| `menu.buttonSelectSlot` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button select slot aus (Parameter: slot, row, col). |
| `menu.buttonSelectSubordinateGroup` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button select subordinate group aus. |
| `menu.buttonSelectUpgradeMacro` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button select upgrade macro aus (Parameter: type, slot, macro, row, col, keepcontext, skipvolatilecheck). |
| `menu.buttonSelfDestructDeployables` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button self destruct deployables aus (Parameter: selecteddeployable). |
| `menu.buttonSellShips` | 2 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button sell ships aus. |
| `menu.buttonSetAllInputFeedbackTextOption` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button set all input feedback text option aus (Parameter: option). |
| `menu.buttonSetAllInputFeedbackVoiceOption` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button set all input feedback voice option aus (Parameter: option). |
| `menu.buttonSetDefaultTheme` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button set default theme aus (Parameter: mode, themeid, row, col). |
| `menu.buttonSetEventOption` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Führt button set event option aus (Parameter: checked). |
| `menu.buttonSetFilterLayer` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button set filter layer aus (Parameter: mode, row, col). |
| `menu.buttonSetInterSectorDefence` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button set inter sector defence aus (Parameter: groups, reset). |
| `menu.buttonSetMoneyToEstimate` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button set money to estimate aus. |
| `menu.buttonSetOrderParam` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button set order param aus (Parameter: order, param, index, value, instance). |
| `menu.buttonSetPlayerLogo` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button set player logo aus (Parameter: logo, row, col). |
| `menu.buttonShipConfig` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button ship config aus (Parameter: mode). |
| `menu.buttonShipInfo` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt button ship info aus. |
| `menu.buttonShowEncyclopedia` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Führt button show encyclopedia aus (Parameter: mode, library, id, objectid). |
| `menu.buttonShowEvent` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Führt button show event aus (Parameter: actionoperationid, eventoperationid). |
| `menu.buttonShowGraph` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt button show graph aus. |
| `menu.buttonShowObjectOnMap` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Führt button show object on map aus (Parameter: object, showzone). |
| `menu.buttonShowTopLevel` | 1 | `08/ui/addons/ego_detailmonitor/menu_toplevel.lua` | Führt button show top level aus. |
| `menu.buttonShowUpkeepMissions` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button show upkeep missions aus. |
| `menu.buttonSlotColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button slot color aus (Parameter: slot, haserror). |
| `menu.buttonSoundTest` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button sound test aus (Parameter: optionid). |
| `menu.buttonStartAction` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Führt button start action aus (Parameter: checked). |
| `menu.buttonStartGame` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button start game aus (Parameter: option). |
| `menu.buttonStartGameActive` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button start game active aus. |
| `menu.buttonStartOrders` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button start orders aus (Parameter: instance). |
| `menu.buttonStartProject` | 1 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Führt button start project aus (Parameter: projectid). |
| `menu.buttonStartResearch` | 1 | `08/ui/addons/ego_detailmonitor/menu_research.lua` | Führt button start research aus (Parameter: techdata). |
| `menu.buttonStationConfig` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button station config aus. |
| `menu.buttonStationOverview` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button station overview aus. |
| `menu.buttonStopBehaviourInspection` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button stop behaviour inspection aus. |
| `menu.buttonStopMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt button stop mode aus. |
| `menu.buttonSubMissionAbort` | 1 | `08/ui/addons/ego_detailmonitor/menu_missionbriefing.lua` | Führt button sub mission abort aus. |
| `menu.buttonSubordinateGroupInterSectorDefence` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button subordinate group inter sector defence aus (Parameter: group, reset). |
| `menu.buttonSyncPointAutoRelease` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button sync point auto release aus. |
| `menu.buttonTacticalAttack` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button tactical attack aus (Parameter: ships, clear). |
| `menu.buttonTeleport` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button teleport aus. |
| `menu.buttonTerraforming` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Führt button terraforming aus (Parameter: cluster, name). |
| `menu.buttonTimeFrame` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt button time frame aus (Parameter: type). |
| `menu.buttonTitleExport` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button title export aus. |
| `menu.buttonTitleImport` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button title import aus. |
| `menu.buttonTitleSave` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt button title save aus. |
| `menu.buttonTitleSaveLoadout` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button title save loadout aus. |
| `menu.buttonTitleSettings` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt button title settings aus. |
| `menu.buttonToggleEncyclopediaMode` | 3 | `08/ui/addons/ego_detailmonitor/menu_ship_comparison.lua` | Führt button toggle encyclopedia mode aus (Parameter: mode). |
| `menu.buttonToggleMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_help.lua` | Führt button toggle mode aus (Parameter: mode). |
| `menu.buttonToggleMultiverseMap` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button toggle multiverse map aus. |
| `menu.buttonToggleObjectList` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button toggle object list aus (Parameter: objectlistparam, confirmed, override). |
| `menu.buttonTogglePlayerInfo` | 2 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button toggle player info aus (Parameter: mode). |
| `menu.buttonToggleRightBar` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button toggle right bar aus (Parameter: searchlistmode, confirmed). |
| `menu.buttonToggleSpawnTable` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Führt button toggle spawn table aus (Parameter: spawntableparam). |
| `menu.buttonTrade` | 2 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button trade aus (Parameter: wareexchange, tradepartner, loop). |
| `menu.buttonTradeRuleAddFaction` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button trade rule add faction aus (Parameter: x, y). |
| `menu.buttonTradeRuleCheckChanges` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button trade rule check changes aus. |
| `menu.buttonTradeRuleConfirm` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button trade rule confirm aus. |
| `menu.buttonTradeRuleRemove` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button trade rule remove aus. |
| `menu.buttonTradeRuleRemoveFaction` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button trade rule remove faction aus (Parameter: faction). |
| `menu.buttonTradeRuleReset` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button trade rule reset aus. |
| `menu.buttonTransactionLog` | 2 | `08/ui/addons/ego_detailmonitor/menu_transactionlog.lua` | Führt button transaction log aus (Parameter: controllable). |
| `menu.buttonTravelMode` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button travel mode aus (Parameter: activate). |
| `menu.buttonTriggerSyncPoint` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button trigger sync point aus. |
| `menu.buttonUndock` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt button undock aus. |
| `menu.buttonUpdateBoardingOperation` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button update boarding operation aus (Parameter: alreadystarted). |
| `menu.buttonUpgrade` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button upgrade aus (Parameter: clear). |
| `menu.buttonUserQuestionCancel` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button user question cancel aus. |
| `menu.buttonUserQuestionConfirm` | 2 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button user question confirm aus. |
| `menu.buttonUserQuestionNegative` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button user question negative aus. |
| `menu.buttonUserQuestionPositive` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt button user question positive aus. |
| `menu.buttonVenturePatron` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button venture patron aus. |
| `menu.buttonVentureReportShip` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button venture report ship aus. |
| `menu.buttonVentureReportUser` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button venture report user aus. |
| `menu.buttonVentureSeasonSubMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button venture season sub mode aus (Parameter: mode, col, instance). |
| `menu.buttonWarDeclarationConfirm` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt button war declaration confirm aus (Parameter: faction). |
| `menu.buttonWarpCheat` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt button warp cheat aus. |
| `menu.buttonWeaponConfig` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt button weapon config aus (Parameter: component, orderidx, usedefault, instance). |
| `menu.butttonWarDeclaration` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt buttton war declaration aus (Parameter: faction). |
| `menu.callback` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt callback aus (Parameter: param). |
| `menu.callbackAccessibilityDefaults` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback accessibility defaults aus. |
| `menu.callbackAccessibilityGlobalLightScale` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback accessibility global light scale aus (Parameter: value). |
| `menu.callbackAccessibilityLongRangeScan` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback accessibility long range scan aus. |
| `menu.callbackAccessibilityReducedSpeedMode` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback accessibility reduced speed mode aus (Parameter: uivalue). |
| `menu.callbackAccessibilitySignalLeak` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback accessibility signal leak aus. |
| `menu.callbackAccessibilityStardustIntensity` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback accessibility stardust intensity aus (Parameter: uivalue). |
| `menu.callbackContinue` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback continue aus. |
| `menu.callbackDefaults` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback defaults aus. |
| `menu.callbackDeleteSave` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback delete save aus (Parameter: filename). |
| `menu.callbackDisplayDefaults` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback display defaults aus. |
| `menu.callbackExit` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback exit aus (Parameter: quit). |
| `menu.callbackExtensionDefaults` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback extension defaults aus. |
| `menu.callbackExtensionSettingEnabled` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback extension setting enabled aus (Parameter: overrideextension). |
| `menu.callbackExtensionSettingSync` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback extension setting sync aus. |
| `menu.callbackExtensionSettingWorkshop` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback extension setting workshop aus. |
| `menu.callbackGameAimAssist` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game aim assist aus (Parameter: id, option). |
| `menu.callbackGameAutoZoomReset` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game auto zoom reset aus. |
| `menu.callbackGameAutoroll` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game autoroll aus. |
| `menu.callbackGameAutosave` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game autosave aus. |
| `menu.callbackGameAutosaveInterval` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game autosave interval aus (Parameter: id, option). |
| `menu.callbackGameBoost` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game boost aus. |
| `menu.callbackGameCockpitCamera` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game cockpit camera aus (Parameter: value). |
| `menu.callbackGameCollision` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game collision aus. |
| `menu.callbackGameControlModeMessages` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game control mode messages aus. |
| `menu.callbackGameDefaults` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game defaults aus. |
| `menu.callbackGameEmergencyEject` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game emergency eject aus. |
| `menu.callbackGameEnemyAttack` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game enemy attack aus (Parameter: id, option). |
| `menu.callbackGameEnemyNearby` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game enemy nearby aus (Parameter: id, option). |
| `menu.callbackGameHUDScale` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game hudscale aus (Parameter: id, option). |
| `menu.callbackGameInputFeedback` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game input feedback aus (Parameter: id, option). |
| `menu.callbackGameMenuWidthScale` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game menu width scale aus (Parameter: value). |
| `menu.callbackGameMenuWidthScaleConfirm` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game menu width scale confirm aus. |
| `menu.callbackGameMenuWidthScaleReset` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game menu width scale reset aus. |
| `menu.callbackGameMouseOver` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game mouse over aus. |
| `menu.callbackGameMouselook` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game mouselook aus. |
| `menu.callbackGameRadar` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game radar aus (Parameter: id, option). |
| `menu.callbackGameResetUserQuestions` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game reset user questions aus. |
| `menu.callbackGameRumble` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game rumble aus (Parameter: value). |
| `menu.callbackGameShootAtCursor` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game shoot at cursor aus. |
| `menu.callbackGameSpeakTargetName` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game speak target name aus. |
| `menu.callbackGameStartmenuBackground` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game startmenu background aus (Parameter: id, option). |
| `menu.callbackGameStartmenuBackgroundConfirm` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game startmenu background confirm aus. |
| `menu.callbackGameStopInMenu` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game stop in menu aus. |
| `menu.callbackGameSubtitles` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game subtitles aus (Parameter: id, option). |
| `menu.callbackGameUIScale` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game uiscale aus (Parameter: value). |
| `menu.callbackGameUIScaleConfirm` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game uiscale confirm aus. |
| `menu.callbackGameUIScaleReset` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game uiscale reset aus. |
| `menu.callbackGameVelocityIndicator` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback game velocity indicator aus. |
| `menu.callbackGamestartGalaxyMacro` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gamestart galaxy macro aus (Parameter: customgamestart, propertyid, option). |
| `menu.callbackGamestartPlayerMacro` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gamestart player macro aus (Parameter: customgamestart, propertyid, option). |
| `menu.callbackGfxAA` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx aa aus (Parameter: id, option). |
| `menu.callbackGfxAACancel` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx aacancel aus. |
| `menu.callbackGfxAAConfirm` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx aaconfirm aus. |
| `menu.callbackGfxAdapter` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx adapter aus (Parameter: id, option). |
| `menu.callbackGfxAdaptiveSampling` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx adaptive sampling aus (Parameter: id, option). |
| `menu.callbackGfxAutoGPU` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx auto gpu aus. |
| `menu.callbackGfxCaptureHQ` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx capture hq aus. |
| `menu.callbackGfxChromaticAberration` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx chromatic aberration aus. |
| `menu.callbackGfxDLSS` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx dlss aus (Parameter: id, option). |
| `menu.callbackGfxDLSSAutoFrameGen` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx dlssauto frame gen aus. |
| `menu.callbackGfxDLSSCancel` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx dlsscancel aus. |
| `menu.callbackGfxDLSSConfirm` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx dlssconfirm aus. |
| `menu.callbackGfxDLSSFrameGen` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx dlssframe gen aus (Parameter: id, option). |
| `menu.callbackGfxDLSSFrameGenCancel` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx dlssframe gen cancel aus. |
| `menu.callbackGfxDLSSFrameGenConfirm` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx dlssframe gen confirm aus. |
| `menu.callbackGfxDLSSMode` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx dlssmode aus (Parameter: id, option). |
| `menu.callbackGfxDLSSModeCancel` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx dlssmode cancel aus. |
| `menu.callbackGfxDLSSModeConfirm` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx dlssmode confirm aus. |
| `menu.callbackGfxDefaults` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx defaults aus. |
| `menu.callbackGfxDistortion` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx distortion aus. |
| `menu.callbackGfxEffectDistance` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx effect distance aus (Parameter: value). |
| `menu.callbackGfxEnvMapProbes` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx env map probes aus (Parameter: id, option). |
| `menu.callbackGfxEnvMapProbesInsideGlassFade` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx env map probes inside glass fade aus (Parameter: value). |
| `menu.callbackGfxFOV` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx fov aus (Parameter: value). |
| `menu.callbackGfxFSR1` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx fsr1 aus (Parameter: id, option). |
| `menu.callbackGfxFrameRate` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx frame rate aus (Parameter: value). |
| `menu.callbackGfxFullscreen` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx fullscreen aus (Parameter: id, option). |
| `menu.callbackGfxFullscreenCancel` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx fullscreen cancel aus. |
| `menu.callbackGfxFullscreenConfirm` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx fullscreen confirm aus. |
| `menu.callbackGfxGPU` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx gpu aus (Parameter: id, option). |
| `menu.callbackGfxGamma` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx gamma aus (Parameter: value). |
| `menu.callbackGfxGlow` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx glow aus (Parameter: id, option). |
| `menu.callbackGfxLOD` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx lod aus (Parameter: value). |
| `menu.callbackGfxLUT` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx lut aus (Parameter: id, option). |
| `menu.callbackGfxPOM` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx pom aus (Parameter: id, option). |
| `menu.callbackGfxPresentMode` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx present mode aus (Parameter: id, option). |
| `menu.callbackGfxPreset` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx preset aus (Parameter: id, option). |
| `menu.callbackGfxRadar` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx radar aus (Parameter: id, option). |
| `menu.callbackGfxResolution` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx resolution aus (Parameter: id, option). |
| `menu.callbackGfxResolutionCancel` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx resolution cancel aus. |
| `menu.callbackGfxResolutionConfirm` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx resolution confirm aus. |
| `menu.callbackGfxSSAO` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx ssao aus (Parameter: id, option). |
| `menu.callbackGfxSSR` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx ssr aus (Parameter: id, option). |
| `menu.callbackGfxScreenDisplay` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx screen display aus. |
| `menu.callbackGfxShaderQuality` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx shader quality aus (Parameter: id, option). |
| `menu.callbackGfxShadows` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx shadows aus (Parameter: id, option). |
| `menu.callbackGfxSoftShadows` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx soft shadows aus. |
| `menu.callbackGfxTexture` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx texture aus (Parameter: id, option). |
| `menu.callbackGfxUIGlow` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx uiglow aus (Parameter: id, option). |
| `menu.callbackGfxUIGlowIntensity` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx uiglow intensity aus (Parameter: value). |
| `menu.callbackGfxUpscalingCancel` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx upscaling cancel aus. |
| `menu.callbackGfxUpscalingConfirm` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx upscaling confirm aus. |
| `menu.callbackGfxVolumetric` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback gfx volumetric aus (Parameter: id, option). |
| `menu.callbackInputGamepadMode` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input gamepad mode aus (Parameter: id, option). |
| `menu.callbackInputInvert` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input invert aus (Parameter: rangeid, configname). |
| `menu.callbackInputJoystickBidirectionalThrottle` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input joystick bidirectional throttle aus. |
| `menu.callbackInputJoystickDeadzone` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input joystick deadzone aus (Parameter: value). |
| `menu.callbackInputJoystickSteeringAdaptive` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input joystick steering adaptive aus. |
| `menu.callbackInputMouseCapture` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input mouse capture aus. |
| `menu.callbackInputMouseSteeringAdaptive` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input mouse steering adaptive aus. |
| `menu.callbackInputMouseSteeringInvert` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input mouse steering invert aus (Parameter: configname). |
| `menu.callbackInputMouseSteeringLine` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input mouse steering line aus. |
| `menu.callbackInputMouseSteeringPersistent` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input mouse steering persistent aus. |
| `menu.callbackInputOpenTrackSupport` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input open track support aus. |
| `menu.callbackInputProfileLoad` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input profile load aus (Parameter: profile). |
| `menu.callbackInputProfileRemove` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input profile remove aus (Parameter: slot). |
| `menu.callbackInputProfileSave` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input profile save aus (Parameter: profile). |
| `menu.callbackInputSensitivity` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input sensitivity aus (Parameter: rangeid, configname, value). |
| `menu.callbackInputTrackerAngleFactor` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input tracker angle factor aus (Parameter: value). |
| `menu.callbackInputTrackerDeadzoneAngle` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input tracker deadzone angle aus (Parameter: value). |
| `menu.callbackInputTrackerDeadzonePosition` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input tracker deadzone position aus (Parameter: value). |
| `menu.callbackInputTrackerGazeAngleFactor` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input tracker gaze angle factor aus (Parameter: value). |
| `menu.callbackInputTrackerGazeDeadzone` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input tracker gaze deadzone aus (Parameter: value). |
| `menu.callbackInputTrackerGazeFilterStrength` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input tracker gaze filter strength aus (Parameter: value). |
| `menu.callbackInputTrackerHeadFilterStrength` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input tracker head filter strength aus (Parameter: value). |
| `menu.callbackInputTrackerMode` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input tracker mode aus (Parameter: id, option). |
| `menu.callbackInputTrackerPositionFactor` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input tracker position factor aus (Parameter: value). |
| `menu.callbackInputVivePointingDevice` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback input vive pointing device aus (Parameter: id, option). |
| `menu.callbackJoystick` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback joystick aus (Parameter: slot, guid). |
| `menu.callbackOnlineAllowInvites` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback online allow invites aus. |
| `menu.callbackOnlineAllowPrivateMessages` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback online allow private messages aus. |
| `menu.callbackOnlineOperationUpdates` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback online operation updates aus (Parameter: id, option). |
| `menu.callbackOnlinePreferredLanguage` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback online preferred language aus (Parameter: id, option). |
| `menu.callbackOnlinePromotion` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback online promotion aus (Parameter: id, option). |
| `menu.callbackOnlineSeason` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback online season aus. |
| `menu.callbackOnlineSeasonSummary` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback online season summary aus (Parameter: id, option). |
| `menu.callbackOnlineSeasonUpdates` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback online season updates aus (Parameter: id, option). |
| `menu.callbackOnlineVisitorNames` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback online visitor names aus. |
| `menu.callbackPrivacyCrash` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback privacy crash aus. |
| `menu.callbackPrivacyUserID` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback privacy user id aus. |
| `menu.callbackResetTimelines` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback reset timelines aus. |
| `menu.callbackReturnToHub` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback return to hub aus. |
| `menu.callbackSave` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback save aus (Parameter: savegame, name). |
| `menu.callbackSfxDefaults` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback sfx defaults aus. |
| `menu.callbackSfxDevice` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback sfx device aus (Parameter: id, option). |
| `menu.callbackSfxSetting` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback sfx setting aus (Parameter: sfxtype, value). |
| `menu.callbackSfxSound` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback sfx sound aus. |
| `menu.callbackThirdPersonFlight` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback third person flight aus (Parameter: id, option). |
| `menu.callbackTimelines` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt callback timelines aus. |
| `menu.canCollectCrates` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt can collect crates aus (Parameter: haspilot). |
| `menu.canSalvage` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt can salvage aus (Parameter: haspilot). |
| `menu.cheatAllResearch` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt cheat all research aus. |
| `menu.checkAllRacesSelected` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt check all races selected aus. |
| `menu.checkCPNameID` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt check cpname id aus. |
| `menu.checkCommanderRepairOrders` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt check commander repair orders aus (Parameter: shipidstring). |
| `menu.checkCompatibility` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt check compatibility aus (Parameter: macro, objectmakerraces). |
| `menu.checkConstructionPlan` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt check construction plan aus (Parameter: source, id, limitedmodulesused, onlineitems, isHQ). |
| `menu.checkCurrentBuildTasks` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt check current build tasks aus. |
| `menu.checkCurrentSlot` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt check current slot aus (Parameter: slots, slot). |
| `menu.checkDeliverWaresCargo` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt check deliver wares cargo aus. |
| `menu.checkEquipment` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt check equipment aus (Parameter: removedEquipment, currentEquipment, newEquipment, repairedEquipment, data, object). |
| `menu.checkExportActive` | 2 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt check export active aus (Parameter: overwrite). |
| `menu.checkForConflicts` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt check for conflicts aus (Parameter: newinputtype, newinputcode, newinputsgn, checkall). |
| `menu.checkForConflictsInternal` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt check for conflicts internal aus (Parameter: controlsorder, returnvalue, newinputtype, newinputcode, newinputsgn, checkall). |
| `menu.checkForDiplomaticActionParamObject` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt check for diplomatic action param object aus (Parameter: component). |
| `menu.checkForModifier` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt check for modifier aus (Parameter: modifier, checkonly). |
| `menu.checkForNewCaptains` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt check for new captains aus (Parameter: forcerefresh). |
| `menu.checkForOrderParamObject` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt check for order param object aus (Parameter: component). |
| `menu.checkForSelectComponent` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt check for select component aus (Parameter: component). |
| `menu.checkFunctionMapping` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt check function mapping aus (Parameter: newinputtype, newinputcode, newinputsgn). |
| `menu.checkInput` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt check input aus (Parameter: inputtable, entry, input, newinput, checkonly). |
| `menu.checkInputSource` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt check input source aus (Parameter: sourceid). |
| `menu.checkLicence` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt check licence aus (Parameter: macro, rawicon, issoftware, rawmouseovertext). |
| `menu.checkLoadoutNameID` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt check loadout name id aus. |
| `menu.checkLoadoutOverwriteActive` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt check loadout overwrite active aus. |
| `menu.checkLoadoutSaveNewActive` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt check loadout save new active aus. |
| `menu.checkMissionNPCRequirement` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt check mission npcrequirement aus (Parameter: missionnpcrequirements, controllable, seed, numskills). |
| `menu.checkMod` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt check mod aus (Parameter: type, component, isgroup). |
| `menu.checkModifier` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt check modifier aus (Parameter: inputtable, entry, modifier, input, checkonly). |
| `menu.checkOverwriteActive` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt check overwrite active aus. |
| `menu.checkParent` | 1 | `08/ui/addons/ego_detailmonitor/menu_platformundock.lua` | Führt check parent aus (Parameter: ship, dockedshipsbyID, missingdockedships). |
| `menu.checkPlayerProperty` | 1 | `08/ui/addons/ego_detailmonitor/menu_transporter.lua` | Führt check player property aus (Parameter: transporter). |
| `menu.checkRacesSelected` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt check races selected aus (Parameter: race). |
| `menu.checkSaveNewActive` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt check save new active aus. |
| `menu.checkTransferDetails` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt check transfer details aus (Parameter: i, instance). |
| `menu.checkboxAssignCaptain` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox assign captain aus (Parameter: origin). |
| `menu.checkboxBlacklistDefault` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt checkbox blacklist default aus (Parameter: group, checked). |
| `menu.checkboxBlacklistHazard` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt checkbox blacklist hazard aus (Parameter: _, checked). |
| `menu.checkboxBlacklistRelation` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt checkbox blacklist relation aus (Parameter: _, checked). |
| `menu.checkboxBlacklistUseFactionWhitelist` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt checkbox blacklist use faction whitelist aus (Parameter: _, checked). |
| `menu.checkboxBlacklistUseMacroWhitelist` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt checkbox blacklist use macro whitelist aus (Parameter: _, checked). |
| `menu.checkboxControlDblClick` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt checkbox control dbl click aus (Parameter: data, checked). |
| `menu.checkboxCrewExchangeCaptains` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox crew exchange captains aus. |
| `menu.checkboxCrewTransfer` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox crew transfer aus (Parameter: id, i, j, origin, seed, isorigin). |
| `menu.checkboxFightRuleDefault` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt checkbox fight rule default aus (Parameter: group, checked). |
| `menu.checkboxGraphData` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Führt checkbox graph data aus (Parameter: id, type, i). |
| `menu.checkboxKnownFaction` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt checkbox known faction aus (Parameter: faction, checked). |
| `menu.checkboxKnownStations` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt checkbox known stations aus (Parameter: sector, checked). |
| `menu.checkboxMapEditorSector` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt checkbox map editor sector aus (Parameter: sector, value). |
| `menu.checkboxMultiSelect` | 2 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt checkbox multi select aus (Parameter: option, checked). |
| `menu.checkboxMute` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt checkbox mute aus (Parameter: _, checked). |
| `menu.checkboxNotification` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt checkbox notification aus (Parameter: notificationgroupdata, id, checked). |
| `menu.checkboxOnlinePrivacyPolicy` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt checkbox online privacy policy aus (Parameter: _, value). |
| `menu.checkboxOnlineRemember` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt checkbox online remember aus (Parameter: _, value). |
| `menu.checkboxOrderPlayerOverride` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox order player override aus (Parameter: order, param, paramdata, overrideparam, overrideparamdata, checked). |
| `menu.checkboxOrderPlayerOverrideValue` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox order player override value aus (Parameter: order, overrideparam, listidx, value). |
| `menu.checkboxOrdersSetAsk` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox orders set ask aus (Parameter: factionorcontrollable, signalid, mode). |
| `menu.checkboxOrdersSetBlacklistOverride` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox orders set blacklist override aus (Parameter: controllable, type, checked). |
| `menu.checkboxOrdersSetCargoReservations` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox orders set cargo reservations aus (Parameter: ship, checked). |
| `menu.checkboxOrdersSetFightRuleOverride` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox orders set fight rule override aus (Parameter: controllable, type, checked). |
| `menu.checkboxOrdersSetOverride` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox orders set override aus (Parameter: controllable, signalid, mode, checked). |
| `menu.checkboxOrdersSetResupplyOverride` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox orders set resupply override aus (Parameter: controllable, checked). |
| `menu.checkboxPlayerAlertRepeat` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt checkbox player alert repeat aus (Parameter: _, checked). |
| `menu.checkboxProductionSingle` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt checkbox production single aus (Parameter: macro, checked). |
| `menu.checkboxSatelliteCoverage` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt checkbox satellite coverage aus (Parameter: sector, checked). |
| `menu.checkboxScheduleVentureExtensionDownload` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt checkbox schedule venture extension download aus (Parameter: _, value). |
| `menu.checkboxSelectAllRaces` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt checkbox select all races aus (Parameter: _, checked). |
| `menu.checkboxSelectCaptain` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt checkbox select captain aus (Parameter: row). |
| `menu.checkboxSelectContextSetList` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt checkbox select context set list aus (Parameter: entry, checked). |
| `menu.checkboxSelectContextToggleList` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt checkbox select context toggle list aus (Parameter: checked). |
| `menu.checkboxSelectRace` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt checkbox select race aus (Parameter: race, checked). |
| `menu.checkboxSelectSoftware` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt checkbox select software aus (Parameter: type, slot, software, row, keepcontext). |
| `menu.checkboxSelected` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt checkbox selected aus (Parameter: idx, row, col). |
| `menu.checkboxSetBuildRuleOverride` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox set build rule override aus (Parameter: container, checked, curglobal). |
| `menu.checkboxSetSectorList` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox set sector list aus (Parameter: sector, checked). |
| `menu.checkboxSetTradeRuleOverride` | 3 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox set trade rule override aus (Parameter: container, type, checked, ware). |
| `menu.checkboxSetWareList` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox set ware list aus (Parameter: ware, checked). |
| `menu.checkboxSetWeaponConfig` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox set weapon config aus (Parameter: system, value). |
| `menu.checkboxSetWorkforceFill` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt checkbox set workforce fill aus (Parameter: container). |
| `menu.checkboxStorageWarePriceOverride` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox storage ware price override aus (Parameter: container, ware, buysellswitch, price, checked). |
| `menu.checkboxSubordinateGroupAttackOnSight` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt checkbox subordinate group attack on sight aus (Parameter: group, checked). |
| `menu.checkboxSubordinateGroupReinforceFleet` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt checkbox subordinate group reinforce fleet aus (Parameter: group, checked). |
| `menu.checkboxSubordinateGroupRespondToDistressCalls` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt checkbox subordinate group respond to distress calls aus (Parameter: group, checked). |
| `menu.checkboxSubordinateGroupResupplyAtFleet` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt checkbox subordinate group resupply at fleet aus (Parameter: group, checked). |
| `menu.checkboxSupplyAuto` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt checkbox supply auto aus (Parameter: container64, type, checked). |
| `menu.checkboxToggleGlobalWarePriceModifier` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt checkbox toggle global ware price modifier aus. |
| `menu.checkboxToggleMultiSelect` | 2 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt checkbox toggle multi select aus (Parameter: checked). |
| `menu.checkboxToggleSectorList` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox toggle sector list aus (Parameter: checked). |
| `menu.checkboxToggleWareList` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt checkbox toggle ware list aus (Parameter: checked). |
| `menu.checkboxTradeRuleDefault` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt checkbox trade rule default aus (Parameter: group, checked). |
| `menu.checkboxTradeRuleUseWhitelist` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt checkbox trade rule use whitelist aus (Parameter: _, checked). |
| `menu.checkboxUseLadderContacts` | 2 | `08/ui/addons/ego_detailmonitor/menu_scenario_debriefing.lua` | Führt checkbox use ladder contacts aus (Parameter: _, checked). |
| `menu.checkboxWeaponGroup` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt checkbox weapon group aus (Parameter: objectid, weaponid, primary, group, active). |
| `menu.checkboxWeaponGroupColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt checkbox weapon group color aus (Parameter: groupidx, primary). |
| `menu.cleanup` | 34 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt cleanup aus. |
| `menu.cleanupCutsceneRenderTarget` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt cleanup cutscene render target aus. |
| `menu.cleanupFactionRelationsAllowedByStory` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt cleanup faction relations allowed by story aus (Parameter: oldstoryid, newstoryid). |
| `menu.cleanupHelper` | 1 | `08/ui/addons/ego_detailmonitor/menu_timeline.lua` | Führt cleanup helper aus. |
| `menu.cleanupKnownSectorsAllowedByStory` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt cleanup known sectors allowed by story aus (Parameter: oldstoryid, newstoryid). |
| `menu.cleanupRenderTarget` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Führt cleanup render target aus. |
| `menu.clearExtraSubordinates` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Leert extra subordinates (Parameter: selectedfleetunit, selectedreplacingcomponent). |
| `menu.clearHelp` | 1 | `08/ui/addons/ego_helptext/helptext.lua` | Leert help (Parameter: reason). |
| `menu.clearMouseCursorOverrides` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Leert mouse cursor overrides. |
| `menu.clearSelectedComponents` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Leert selected components. |
| `menu.clearUndoStack` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Leert undo stack. |
| `menu.close` | 2 | `08/ui/addons/ego_detailmonitor/menu_toplevel.lua` | Führt close aus. |
| `menu.closeContextMenu` | 13 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Schließt context menu. |
| `menu.closeMenu` | 11 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Schließt menu (Parameter: dueToClose). |
| `menu.closeTabs` | 1 | `08/ui/addons/ego_detailmonitor/menu_toplevel.lua` | Schließt tabs. |
| `menu.closeUserQuestionMenu` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Schließt user question menu. |
| `menu.compareTradeWareSelection` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt compare trade ware selection aus. |
| `menu.componentSorter` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt component sorter aus (Parameter: sorttype). |
| `menu.confirm` | 1 | `08/ui/addons/ego_detailmonitor/menu_userquestion.lua` | Führt confirm aus. |
| `menu.confirmModuleChangesActive` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt confirm module changes active aus. |
| `menu.contextChangeLogoButtonIcon2` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt context change logo button icon2 aus (Parameter: logo). |
| `menu.contextChangeLogoButtonIcon2Color` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt context change logo button icon2 color aus (Parameter: logo). |
| `menu.convertClusterGridToCoord` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Führt convert cluster grid to coord aus (Parameter: q, r). |
| `menu.convertDate` | 1 | `08/ui/addons/ego_detailmonitor/menu_timeline.lua` | Führt convert date aus (Parameter: date). |
| `menu.copyDefaultOrderForPlanning` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt copy default order for planning aus (Parameter: instance). |
| `menu.countPlayerProperty` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt count player property aus (Parameter: id, count, moneybudget, peoplebudget, totalcount). |
| `menu.createAccounts` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Erstellt accounts (Parameter: frame, tableProperties, tabOrderOffset). |
| `menu.createActionConfigContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Erstellt action config context (Parameter: frame). |
| `menu.createAgentDetailsContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Erstellt agent details context (Parameter: frame). |
| `menu.createAgents` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Erstellt agents (Parameter: frame, tableProperties). |
| `menu.createBoardingContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt boarding context (Parameter: frame, target, boarders). |
| `menu.createButtonTable` | 2 | `08/ui/addons/ego_detailmonitor/menu_scenario_debriefing.lua` | Erstellt button table (Parameter: frame, tablewidth, xoffset, yoffset). |
| `menu.createCPExportContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Erstellt cpexport context. |
| `menu.createCPImportContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Erstellt cpimport context. |
| `menu.createCPRemoveContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Erstellt cpremove context. |
| `menu.createCPSaveContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Erstellt cpsave context. |
| `menu.createChangeLogoContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt change logo context (Parameter: frame). |
| `menu.createCheats` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt cheats (Parameter: frame). |
| `menu.createComparisonTable` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_comparison.lua` | Erstellt comparison table (Parameter: frame). |
| `menu.createComponentTable` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Erstellt component table (Parameter: frame). |
| `menu.createConstructionRow` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt construction row (Parameter: ftable, component, construction, iteration). |
| `menu.createConstructionSection` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt construction section (Parameter: instance, id, ftable, name, constructions). |
| `menu.createConstructionSubSection` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt construction sub section (Parameter: ftable, component, constructions). |
| `menu.createContentTable` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Erstellt content table (Parameter: frame, position). |
| `menu.createContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Erstellt context (Parameter: x, y). |
| `menu.createContextFrame` | 6 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Erstellt context frame (Parameter: data, x, y, width, nomouseout). |
| `menu.createContextMenu` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Erstellt context menu. |
| `menu.createContextMenuDirectInput` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Erstellt context menu direct input (Parameter: frame). |
| `menu.createContextMenuEditColor` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Erstellt context menu edit color (Parameter: frame). |
| `menu.createContextMenuFirstGame` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Erstellt context menu first game (Parameter: frame). |
| `menu.createContextMenuInfo` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Erstellt context menu info (Parameter: frame). |
| `menu.createContextMenuModified` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Erstellt context menu modified (Parameter: frame). |
| `menu.createContextMenuRemap` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Erstellt context menu remap (Parameter: frame). |
| `menu.createContextMenuRemoveControllerInput` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Erstellt context menu remove controller input (Parameter: frame). |
| `menu.createContextMenuUISecurity` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Erstellt context menu uisecurity (Parameter: frame). |
| `menu.createContextMenuUserQuestion` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Erstellt context menu user question (Parameter: frame). |
| `menu.createContextMenuVentureExtension` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Erstellt context menu venture extension (Parameter: frame). |
| `menu.createCraftableEntry` | 2 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Erstellt craftable entry (Parameter: ware). |
| `menu.createCrafting` | 2 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Erstellt crafting (Parameter: frame, tableProperties). |
| `menu.createCrewInfoSubmenu` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt crew info submenu (Parameter: inputframe, instance). |
| `menu.createCrewTransferContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt crew transfer context (Parameter: frame). |
| `menu.createDescTable` | 2 | `08/ui/addons/ego_detailmonitor/menu_scenario_debriefing.lua` | Erstellt desc table (Parameter: frame, tablewidth, xoffset, yoffset). |
| `menu.createEmbassy` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Erstellt embassy (Parameter: frame, tableProperties). |
| `menu.createEmpire` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Erstellt empire (Parameter: frame, tableProperties). |
| `menu.createEmptyFrame` | 2 | `08/ui/addons/ego_detailmonitor/menu_scenario_debriefing.lua` | Erstellt empty frame. |
| `menu.createEquipmentContext` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Erstellt equipment context. |
| `menu.createEquipmentFilterContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Erstellt equipment filter context. |
| `menu.createEquipmentModEntry` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Erstellt equipment mod entry (Parameter: ftable, modclass, moddata). |
| `menu.createEquipmentMods` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Erstellt equipment mods (Parameter: frame, tableProperties). |
| `menu.createEquipmentPropertyEntry` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Erstellt equipment property entry (Parameter: ftable, modclass, property). |
| `menu.createEventCompletedContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Erstellt event completed context (Parameter: frame). |
| `menu.createEventContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Erstellt event context (Parameter: frame). |
| `menu.createEvents` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Erstellt events (Parameter: frame, tableProperties). |
| `menu.createExportTable` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Erstellt export table (Parameter: frame). |
| `menu.createFactionDetailsContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Erstellt faction details context (Parameter: frame). |
| `menu.createFactions` | 2 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Erstellt factions (Parameter: frame, tableProperties). |
| `menu.createFilterMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt filter mode (Parameter: ftable, numCols). |
| `menu.createFilterparamWareContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt filterparam ware context (Parameter: frame). |
| `menu.createFleetUnitRow` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt fleet unit row (Parameter: instance, ftable, fleetunit, iteration, commanderlocation, numdisplayed, sorter). |
| `menu.createFrame` | 3 | `08/ui/addons/ego_detailmonitor/menu_transactionlog.lua` | Erstellt frame (Parameter: toprow, selectedrow). |
| `menu.createGraph` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Erstellt graph (Parameter: width, height, x, y). |
| `menu.createHireContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt hire context (Parameter: frame). |
| `menu.createHireMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt hire mode (Parameter: ftable, numCols). |
| `menu.createIndex` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Erstellt index. |
| `menu.createInfo2Frame` | 2 | `08/ui/addons/ego_detailmonitor/menu_scenario_debriefing.lua` | Erstellt info2 frame. |
| `menu.createInfoContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt info context (Parameter: frame). |
| `menu.createInfoFrame` | 10 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt info frame. |
| `menu.createInfoFrame2` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt info frame2. |
| `menu.createInfoSubmenu` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt info submenu (Parameter: inputframe, instance). |
| `menu.createInventory` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Erstellt inventory (Parameter: frame, tableProperties, mode, tabOrderOffset). |
| `menu.createInventoryContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_crafting.lua` | Erstellt inventory context (Parameter: wareinfo, x, y). |
| `menu.createInventoryHeader` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Erstellt inventory header (Parameter: frame, tableProperties). |
| `menu.createLadderTable` | 2 | `08/ui/addons/ego_detailmonitor/menu_scenario_debriefing.lua` | Erstellt ladder table (Parameter: frame, tablewidth, xoffset, yoffset, maxVisibleHeight). |
| `menu.createLegend` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt legend. |
| `menu.createLegendMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt legend mode (Parameter: ftable, numCols). |
| `menu.createLoadoutInfoSubmenu` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt loadout info submenu (Parameter: inputframe, instance). |
| `menu.createLoadoutSaveContext` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Erstellt loadout save context. |
| `menu.createLogbook` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Erstellt logbook (Parameter: frame, tableProperties). |
| `menu.createLogbookHeader` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Erstellt logbook header (Parameter: frame, tableProperties). |
| `menu.createLogbookInfoSubmenu` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt logbook info submenu (Parameter: inputframe, instance). |
| `menu.createMacroSearchTable` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Erstellt macro search table (Parameter: frame). |
| `menu.createMainFrame` | 5 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt main frame (Parameter: firsttime, height, refresh). |
| `menu.createMessages` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Erstellt messages (Parameter: frame, tableProperties). |
| `menu.createMissionContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt mission context (Parameter: frame). |
| `menu.createMissionInfoSection` | 1 | `08/ui/addons/ego_detailmonitor/menu_missionbriefing.lua` | Erstellt mission info section (Parameter: frame). |
| `menu.createMissionMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt mission mode (Parameter: frame). |
| `menu.createMissionModeHeader` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt mission mode header (Parameter: frame, instance). |
| `menu.createModuleContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Erstellt module context. |
| `menu.createModuleFilterContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Erstellt module filter context. |
| `menu.createModuleSection` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt module section (Parameter: instance, ftable, component, iteration). |
| `menu.createNewEventContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Erstellt new event context (Parameter: frame). |
| `menu.createNewOrderContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt new order context (Parameter: frame, instance). |
| `menu.createObjectList` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt object list (Parameter: frame, instance). |
| `menu.createObjectivesSection` | 1 | `08/ui/addons/ego_detailmonitor/menu_missionbriefing.lua` | Erstellt objectives section (Parameter: frame). |
| `menu.createOnlineModeContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt online mode context (Parameter: frame). |
| `menu.createOptionsFrame` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Erstellt options frame (Parameter: extrawide). |
| `menu.createOrderQueue` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt order queue (Parameter: frame, mode, instance). |
| `menu.createOrderparamFormationShapeContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt orderparam formation shape context (Parameter: frame, instance). |
| `menu.createOrderparamSectorContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt orderparam sector context (Parameter: frame, instance). |
| `menu.createOrderparamWareContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt orderparam ware context (Parameter: frame, instance). |
| `menu.createOrdersMenuHeader` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt orders menu header (Parameter: frame, instance). |
| `menu.createOverwriteQuestionContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Erstellt overwrite question context. |
| `menu.createPersonnelInfo` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Erstellt personnel info (Parameter: frame, tableProperties). |
| `menu.createPlayerInfo` | 4 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt player info (Parameter: frame, width, height, offsetx, offsety). |
| `menu.createPlotMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt plot mode (Parameter: inputframe). |
| `menu.createPropertyOwned` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt property owned (Parameter: frame, instance). |
| `menu.createPropertyRow` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt property row (Parameter: instance, ftable, component, iteration, commanderlocation, showmodules, hidesubordinates, numdisplayed, sorter). |
| `menu.createPropertySection` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt property section (Parameter: instance, id, ftable, name, array, nonetext, showmodules, numdisplayed, hidesubordinates, sorter). |
| `menu.createRenameContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt rename context (Parameter: frame). |
| `menu.createRenderTarget` | 1 | `08/ui/addons/ego_detailmonitor/menu_missionbriefing.lua` | Erstellt render target (Parameter: frame). |
| `menu.createRendertargetAndDescription` | 1 | `08/ui/addons/ego_detailmonitor/menu_timeline.lua` | Erstellt rendertarget and description (Parameter: frame, timelineTable). |
| `menu.createReportContext` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Erstellt report context (Parameter: frame). |
| `menu.createResponsesForControllable` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt responses for controllable (Parameter: ftable, controllable, textproperties, mode, yoffset, instance). |
| `menu.createRewardSection` | 1 | `08/ui/addons/ego_detailmonitor/menu_missionbriefing.lua` | Erstellt reward section (Parameter: frame). |
| `menu.createRightBar` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt right bar (Parameter: frame, width, height, offsetx, offsety). |
| `menu.createScenarioTable` | 2 | `08/ui/addons/ego_detailmonitor/menu_scenario_debriefing.lua` | Erstellt scenario table (Parameter: frame, yoffset). |
| `menu.createSearchField` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt search field (Parameter: frame, width, height, offsetx, offsety, refresh). |
| `menu.createSearchFieldContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt search field context (Parameter: frame). |
| `menu.createSelectContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt select context (Parameter: frame). |
| `menu.createSelectedShips` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt selected ships (Parameter: frame). |
| `menu.createSellShipsContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt sell ships context (Parameter: frame). |
| `menu.createSettingsContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Erstellt settings context. |
| `menu.createSideBar` | 5 | `08/ui/addons/ego_detailmonitor/menu_ship_comparison.lua` | Erstellt side bar (Parameter: frame). |
| `menu.createSlotContext` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Erstellt slot context. |
| `menu.createSpawnTable` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Erstellt spawn table (Parameter: frame). |
| `menu.createStandingOrdersMenu` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt standing orders menu (Parameter: frame, instance). |
| `menu.createStats` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Erstellt stats (Parameter: frame, tableProperties). |
| `menu.createStatsTable` | 2 | `08/ui/addons/ego_detailmonitor/menu_scenario_debriefing.lua` | Erstellt stats table (Parameter: frame, tablewidth, xoffset, yoffset). |
| `menu.createSubSectionTable` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Erstellt sub section table (Parameter: frame, position). |
| `menu.createSubordinateSection` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt subordinate section (Parameter: instance, ftable, component, isfleetunit, isstation, iteration, location, numdisplayed, sorter, isplayerowned, isally). |
| `menu.createTable` | 3 | `08/ui/addons/ego_detailmonitor/menu_toplevel.lua` | Erstellt table (Parameter: frame, tableProperties). |
| `menu.createTimelineTable` | 1 | `08/ui/addons/ego_detailmonitor/menu_timeline.lua` | Erstellt timeline table (Parameter: frame). |
| `menu.createTitleBar` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Erstellt title bar (Parameter: frame). |
| `menu.createTitleTable` | 2 | `08/ui/addons/ego_detailmonitor/menu_scenario_debriefing.lua` | Erstellt title table (Parameter: frame). |
| `menu.createTopLevel` | 11 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Erstellt top level. |
| `menu.createTradeContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt trade context (Parameter: frame). |
| `menu.createTradeLoopContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt trade loop context (Parameter: frame). |
| `menu.createUserQuestionContext` | 5 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt user question context (Parameter: frame). |
| `menu.createUserQuestionFrame` | 2 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Erstellt user question frame. |
| `menu.createVentureSeason` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt venture season (Parameter: frame, instance). |
| `menu.createVentureSeasonHeader` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt venture season header (Parameter: frame, instance). |
| `menu.createWeaponConfigContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Erstellt weapon config context (Parameter: frame, instance). |
| `menu.crewTransferAllowed` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt crew transfer allowed aus. |
| `menu.crewTransferColorHelper` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt crew transfer color helper aus (Parameter: origin, tierentry, basecolor). |
| `menu.crewTransferSorter` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt crew transfer sorter aus (Parameter: a, b). |
| `menu.crewTransferTotalColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt crew transfer total color aus (Parameter: origin). |
| `menu.crewTransferWarningText` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt crew transfer warning text aus (Parameter: leftname, rightname, row). |
| `menu.customOption` | 1 | `08/ui/addons/ego_detailmonitor/menu_userquestion.lua` | Führt custom option aus (Parameter: optionid, optionparameters). |
| `menu.deactivateEncyclopediaMode` | 3 | `08/ui/addons/ego_detailmonitor/menu_ship_comparison.lua` | Deaktiviert encyclopedia mode. |
| `menu.deactivateModulesMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Deaktiviert modules mode. |
| `menu.deactivateObjectList` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Deaktiviert object list (Parameter: confirmed). |
| `menu.deactivatePlayerInfo` | 3 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Deaktiviert player info. |
| `menu.deactivateSearchTable` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Deaktiviert search table. |
| `menu.deactivateUpgradeMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Deaktiviert upgrade mode. |
| `menu.deactivateUpgradetypeMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Deaktiviert upgradetype mode. |
| `menu.defaultInteraction` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt default interaction aus (Parameter: component, posrot, posrotvalid, offsetx, offsety, modified). |
| `menu.descriptionBonusContent` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt description bonus content aus. |
| `menu.descriptionExtension` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt description extension aus. |
| `menu.detailIcon` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Führt detail icon aus (Parameter: isrendertargeticon). |
| `menu.detailIconColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Führt detail icon color aus (Parameter: isrendertargeticon). |
| `menu.detailText` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Führt detail text aus. |
| `menu.determineInitialSlot` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt determine initial slot aus. |
| `menu.determineNeededRepairs` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt determine needed repairs aus (Parameter: ship). |
| `menu.display` | 13 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt display aus. |
| `menu.displayAmmoSlot` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display ammo slot aus (Parameter: ftable, type, macro, total, capacity, first). |
| `menu.displayBonusContent` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display bonus content aus. |
| `menu.displayChat` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt display chat aus. |
| `menu.displayColorLibrary` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display color library aus. |
| `menu.displayCondition` | 1 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Führt display condition aus (Parameter: ftable, condition, stat, hastitle). |
| `menu.displayContextFrame` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display context frame aus (Parameter: mode, width, x, y). |
| `menu.displayControlRow` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display control row aus (Parameter: ftable, controlsgroup, controltype, code, context, mouseovertext, mappable, allowmouseaxis, first, checklastnonkeyboard, compassmenusupport, mouseonly, mousewheelonly, mouseaxisonly). |
| `menu.displayControls` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display controls aus (Parameter: optionParameter). |
| `menu.displayCredits` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display credits aus (Parameter: option). |
| `menu.displayCrewSlot` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display crew slot aus (Parameter: ftable, idx, data, buttonWidth, price, first). |
| `menu.displayDefaultBehaviour` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt display default behaviour aus (Parameter: ftable, mode, titlerow, instance). |
| `menu.displayDefaultBehaviourFailure` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt display default behaviour failure aus (Parameter: ftable, mode, titlerow, instance, planned). |
| `menu.displayEffect` | 1 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Führt display effect aus (Parameter: ftable, effect, issideeffect, hastitle). |
| `menu.displayEmptyMenu` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display empty menu aus (Parameter: cleanup). |
| `menu.displayEmptySlots` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display empty slots aus (Parameter: frame). |
| `menu.displayExportContext` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt display export context aus. |
| `menu.displayExtensionRow` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display extension row aus (Parameter: ftable, extension, extensionSetting). |
| `menu.displayExtensions` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display extensions aus. |
| `menu.displayFailureParam` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt display failure param aus (Parameter: ftable, failureidx, paramidx, param, listidx, instance). |
| `menu.displayGameModified` | 1 | `08/ui/addons/ego_gameoptions/gamemodified.lua` | Führt display game modified aus. |
| `menu.displayHelp` | 1 | `08/ui/addons/ego_helptext/helptext.lua` | Führt display help aus. |
| `menu.displayHint` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt display hint aus (Parameter: text). |
| `menu.displayIndexRow` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Führt display index row aus (Parameter: inputtable, entry). |
| `menu.displayInit` | 2 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display init aus (Parameter: text). |
| `menu.displayInputFeedback` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display input feedback aus. |
| `menu.displayInputFeedbackRow` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display input feedback row aus (Parameter: ftable, controltype, controlcode, configentry). |
| `menu.displayInputModifiers` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display input modifiers aus. |
| `menu.displayInputProfiles` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display input profiles aus (Parameter: optionParameter). |
| `menu.displayJoysticks` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display joysticks aus. |
| `menu.displayLanguageOptions` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display language options aus. |
| `menu.displayLeftBar` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display left bar aus (Parameter: frame). |
| `menu.displayLobby` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display lobby aus. |
| `menu.displayMainFrame` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display main frame aus. |
| `menu.displayMapContext` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt display map context aus (Parameter: offset, sectormacro, sectorpos). |
| `menu.displayMapEditor` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display map editor aus. |
| `menu.displayMenu` | 6 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt display menu aus (Parameter: firsttime). |
| `menu.displayModBlueprint` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display mod blueprint aus (Parameter: ftable, type, slot, slotdata, modclass, moddata, hasinstalledmod, installedmodware, isgroup). |
| `menu.displayModSlot` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display mod slot aus (Parameter: ftable, type, modclass, slot, slotdata, isgroup). |
| `menu.displayModifyPaintSlots` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display modify paint slots aus (Parameter: frame). |
| `menu.displayModifyPlan` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display modify plan aus (Parameter: frame). |
| `menu.displayModifySlots` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display modify slots aus (Parameter: frame). |
| `menu.displayModuleInfo` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt display module info aus (Parameter: frame). |
| `menu.displayModuleRow` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt display module row aus (Parameter: ftable, index, entry, added, removed). |
| `menu.displayModules` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt display modules aus (Parameter: frame, firsttime). |
| `menu.displayMultiSelection` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt display multi selection aus (Parameter: property). |
| `menu.displayNewGame` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display new game aus (Parameter: createAsServer, displayTimelinesScenarios, displayTutorials). |
| `menu.displayOnlineLogin` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display online login aus. |
| `menu.displayOnlineSeason` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display online season aus (Parameter: option). |
| `menu.displayOnlineUpdate` | 1 | `08/ui/addons/ego_gameoptions/onlineupdate.lua` | Führt display online update aus. |
| `menu.displayOption` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display option aus (Parameter: ftable, option, numCols). |
| `menu.displayOptions` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display options aus (Parameter: optionParameter). |
| `menu.displayOptionsInfo` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display options info aus (Parameter: optionParameter). |
| `menu.displayOrderFailureSection` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt display order failure section aus (Parameter: ftable, instance). |
| `menu.displayOrderParam` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt display order param aus (Parameter: ftable, orderidx, order, paramidx, param, listidx, instance). |
| `menu.displayPlan` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display plan aus (Parameter: frame). |
| `menu.displayPlannedDefaultBehaviour` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt display planned default behaviour aus (Parameter: ftable, mode, titlerow, instance). |
| `menu.displayPlayerPropertyEntry` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt display player property entry aus (Parameter: ftable, entry, iteration). |
| `menu.displaySavegameOptions` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display savegame options aus (Parameter: optionParameter). |
| `menu.displaySlots` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display slots aus (Parameter: frame, firsttime). |
| `menu.displaySoftwareSlot` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display software slot aus (Parameter: ftable, type, slot, slotdata). |
| `menu.displayStats` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display stats aus (Parameter: frame). |
| `menu.displayTimelines` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display timelines aus. |
| `menu.displayUpgradeResources` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display upgrade resources aus (Parameter: ftable, resources, upgradeamount). |
| `menu.displayUserQuestion` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt display user question aus (Parameter: question, callback, negCallback, timer, waitforgfx, editboxHook, editboxNote, infotext). |
| `menu.displayWeaponAmmoSelection` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display weapon ammo selection aus (Parameter: ftable, upgradetype, slot, data). |
| `menu.displayWeaponModeSelection` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt display weapon mode selection aus (Parameter: ftable, upgradetype, slot, data). |
| `menu.dockButtonBGColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt dock button bgcolor aus. |
| `menu.dockButtonHighlightColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt dock button highlight color aus. |
| `menu.dockButtonTextColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt dock button text color aus. |
| `menu.draw` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt draw aus. |
| `menu.drawLobby` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Zeichnet lobby. |
| `menu.dropdownAssignEventAgent` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Führt dropdown assign event agent aus (Parameter: eventoperationid, agentid). |
| `menu.dropdownBehaviourFormation` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt dropdown behaviour formation aus (Parameter: _, shape). |
| `menu.dropdownBlacklistType` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt dropdown blacklist type aus (Parameter: _, newtype). |
| `menu.dropdownBoardingSetAction` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt dropdown boarding set action aus (Parameter: ship, newaction). |
| `menu.dropdownBoardingSetRisk` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt dropdown boarding set risk aus (Parameter: newrisklevel, phaseindex). |
| `menu.dropdownBuildRule` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt dropdown build rule aus (Parameter: container, id). |
| `menu.dropdownChangeOverrideOrder` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt dropdown change override order aus (Parameter: idstring, attacker, instance). |
| `menu.dropdownChangePurchaseAmount` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt dropdown change purchase amount aus (Parameter: idx, amountstring). |
| `menu.dropdownColorMapping` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt dropdown color mapping aus (Parameter: i, newrefid). |
| `menu.dropdownControl` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt dropdown control aus (Parameter: row, data, id). |
| `menu.dropdownCrewTransferSelectMission` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt dropdown crew transfer select mission aus (Parameter: person, missionid). |
| `menu.dropdownCurrentFaction` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt dropdown current faction aus (Parameter: _, option). |
| `menu.dropdownDate` | 1 | `08/ui/addons/ego_detailmonitor/menu_timeline.lua` | Führt dropdown date aus (Parameter: _, newid). |
| `menu.dropdownDefaultLoadout` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt dropdown default loadout aus (Parameter: _, level). |
| `menu.dropdownDeploy` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt dropdown deploy aus (Parameter: _, idstring). |
| `menu.dropdownDroneStartOption` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt dropdown drone start option aus (Parameter: ship, type). |
| `menu.dropdownFightRuleFactionSetting` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt dropdown fight rule faction setting aus (Parameter: faction, id). |
| `menu.dropdownHireRole` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt dropdown hire role aus (Parameter: _, idstring). |
| `menu.dropdownImport` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt dropdown import aus (Parameter: filename). |
| `menu.dropdownInventoryLockbox` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt dropdown inventory lockbox aus (Parameter: _, id). |
| `menu.dropdownLoad` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt dropdown load aus (Parameter: _, id). |
| `menu.dropdownLoadout` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt dropdown loadout aus (Parameter: _, loadoutid). |
| `menu.dropdownLoadoutRemoved` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt dropdown loadout removed aus (Parameter: _, loadoutid). |
| `menu.dropdownMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt dropdown mode aus (Parameter: _, id). |
| `menu.dropdownModuleSet` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt dropdown module set aus (Parameter: _, idstring). |
| `menu.dropdownNewSyncPoint` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt dropdown new sync point aus (Parameter: orderidx, idstring). |
| `menu.dropdownOrdersBlacklist` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt dropdown orders blacklist aus (Parameter: controllable, type, id). |
| `menu.dropdownOrdersBuildRule` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt dropdown orders build rule aus (Parameter: _, id). |
| `menu.dropdownOrdersCargoReservations` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt dropdown orders cargo reservations aus (Parameter: ship, id). |
| `menu.dropdownOrdersFightRule` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt dropdown orders fight rule aus (Parameter: controllable, type, id). |
| `menu.dropdownOrdersResupply` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt dropdown orders resupply aus (Parameter: controllable, id). |
| `menu.dropdownOrdersSetResponse` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt dropdown orders set response aus (Parameter: _, newresponseid, factionorcontrollable, signalid, mode). |
| `menu.dropdownPlayerAlertPurpose` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt dropdown player alert purpose aus (Parameter: _, newpurpose). |
| `menu.dropdownPlayerAlertSound` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt dropdown player alert sound aus (Parameter: _, newsound). |
| `menu.dropdownPlayerAlertSpace` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt dropdown player alert space aus (Parameter: _, newspace). |
| `menu.dropdownPlayerPropertyAddStation` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt dropdown player property add station aus (Parameter: entryid, cpid, isHQentry, isNewStation). |
| `menu.dropdownPlayerPropertySetCount` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt dropdown player property set count aus (Parameter: entryid, count, macro, oldcount). |
| `menu.dropdownPlayerPropertySetSector` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt dropdown player property set sector aus (Parameter: entryid, sector, offset). |
| `menu.dropdownProductionMethod` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Führt dropdown production method aus (Parameter: _, id). |
| `menu.dropdownProperty` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt dropdown property aus (Parameter: property, row, option). |
| `menu.dropdownRemovedCP` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt dropdown removed cp aus (Parameter: _, id). |
| `menu.dropdownRemovedColorProfile` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt dropdown removed color profile aus (Parameter: _, filename). |
| `menu.dropdownRemovedLoadout` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt dropdown removed loadout aus (Parameter: _, loadoutid). |
| `menu.dropdownSelectFaction` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Führt dropdown select faction aus (Parameter: actionid, i, factionid). |
| `menu.dropdownSelectWare` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Führt dropdown select ware aus (Parameter: actionid, i, wareid). |
| `menu.dropdownSetInputFeedbackTextOption` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt dropdown set input feedback text option aus (Parameter: option, controltype, controlcode). |
| `menu.dropdownSetInputFeedbackVoiceOption` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt dropdown set input feedback voice option aus (Parameter: option, controltype, controlcode). |
| `menu.dropdownShip` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt dropdown ship aus (Parameter: _, shipid). |
| `menu.dropdownShipClass` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt dropdown ship class aus (Parameter: _, class). |
| `menu.dropdownStoryState` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt dropdown story state aus (Parameter: groupid, storyid). |
| `menu.dropdownTimelinesCharacter` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt dropdown timelines character aus (Parameter: timelinesgamestart, id). |
| `menu.dropdownTradeRule` | 3 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt dropdown trade rule aus (Parameter: container, type, id, ware, refresh). |
| `menu.dropdownVentureExtensionDownload` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt dropdown venture extension download aus (Parameter: _, id). |
| `menu.editboxActivated` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt editbox activated aus. |
| `menu.editboxBlacklistNameChanged` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt editbox blacklist name changed aus (Parameter: _, text). |
| `menu.editboxCPNameUpdateText` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt editbox cpname update text aus (Parameter: _, text). |
| `menu.editboxChangePlayerFactionName` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt editbox change player faction name aus (Parameter: _, text, textchanged). |
| `menu.editboxChangePlayerName` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt editbox change player name aus (Parameter: _, text, textchanged). |
| `menu.editboxClusterCoord` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Führt editbox cluster coord aus (Parameter: _, text, textchanged). |
| `menu.editboxColorDefinitionSearchUpdateText` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt editbox color definition search update text aus (Parameter: widget, text, textchanged). |
| `menu.editboxColorMappingSearchUpdateText` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt editbox color mapping search update text aus (Parameter: widget, text, textchanged). |
| `menu.editboxControlsSearchUpdateText` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt editbox controls search update text aus (Parameter: widget, text, textchanged). |
| `menu.editboxCustomShipName` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt editbox custom ship name aus (Parameter: _, text). |
| `menu.editboxCustomShipNameDeactivated` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt editbox custom ship name deactivated aus (Parameter: _, text, textchanged). |
| `menu.editboxFightRuleNameChanged` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt editbox fight rule name changed aus (Parameter: _, text). |
| `menu.editboxInfoLogbookPage` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt editbox info logbook page aus (Parameter: instance, text, textchanged). |
| `menu.editboxInfoLogbookPageActivated` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt editbox info logbook page activated aus (Parameter: widget, instance). |
| `menu.editboxInputProfileSave` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt editbox input profile save aus (Parameter: profile, text). |
| `menu.editboxLoadoutNameUpdateText` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt editbox loadout name update text aus (Parameter: _, text). |
| `menu.editboxLogbookPage` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt editbox logbook page aus (Parameter: _, text, textchanged). |
| `menu.editboxMessageChanged` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt editbox message changed aus (Parameter: _, text). |
| `menu.editboxMessageCursorChanged` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt editbox message cursor changed aus (Parameter: _, cursorpos, shiftstartpos). |
| `menu.editboxModuleSearchUpdateText` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt editbox module search update text aus (Parameter: widget, text, textchanged). |
| `menu.editboxNameUpdateText` | 2 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt editbox name update text aus (Parameter: _, text). |
| `menu.editboxOnlinePassword` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt editbox online password aus (Parameter: widgetid, text). |
| `menu.editboxOnlinePasswordDeactivated` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt editbox online password deactivated aus (Parameter: _, text, textchanged, isconfirmed). |
| `menu.editboxOnlineUsername` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt editbox online username aus (Parameter: widgetid, text). |
| `menu.editboxOnlineUsernameDeactivated` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt editbox online username deactivated aus (Parameter: _, text, textchanged, isconfirmed, wastableclick). |
| `menu.editboxPersonnelPage` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt editbox personnel page aus (Parameter: _, text, textchanged). |
| `menu.editboxPlayerAlertIDCodeChanged` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt editbox player alert idcode changed aus (Parameter: _, text). |
| `menu.editboxPlayerAlertMessageChanged` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt editbox player alert message changed aus (Parameter: _, text). |
| `menu.editboxPlayerAlertNameChanged` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt editbox player alert name changed aus (Parameter: _, text). |
| `menu.editboxPlayerPropertyName` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt editbox player property name aus (Parameter: id, text). |
| `menu.editboxProperty` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt editbox property aus (Parameter: property, text). |
| `menu.editboxSaveName` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt editbox save name aus (Parameter: _, text). |
| `menu.editboxSearchUpdateText` | 3 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt editbox search update text aus (Parameter: _, text, textchanged). |
| `menu.editboxSendMessage` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt editbox send message aus (Parameter: _, text, textchanged, isconfirmed, wastableclick). |
| `menu.editboxTradeRuleNameChanged` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt editbox trade rule name changed aus (Parameter: _, text). |
| `menu.editboxUpdateTransactionSearchString` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt editbox update transaction search string aus (Parameter: _, text, textchanged). |
| `menu.editboxUserQuestionTextChanged` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt editbox user question text changed aus (Parameter: _, text). |
| `menu.empireCanShowObject` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt empire can show object aus (Parameter: object). |
| `menu.employeeSearchHelper` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt employee search helper aus (Parameter: entry, text). |
| `menu.errorSavegame` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt error savegame aus (Parameter: savegame). |
| `menu.errorSavegameInfo` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt error savegame info aus. |
| `menu.etaSorter` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt eta sorter aus (Parameter: a, b). |
| `menu.evaluateShipOptions` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt evaluate ship options aus. |
| `menu.eventIconColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Führt event icon color aus. |
| `menu.eventOperationTime` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Führt event operation time aus (Parameter: endtime). |
| `menu.excludeMonitorZone` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt exclude monitor zone aus (Parameter: frame, monitorexclusionzone, framewidth, frameheight, origFrameX, origFrameY, mouseOutBoxExtension, noright). |
| `menu.expandAccountNode` | 1 | `08/ui/addons/ego_detailmonitor/menu_research.lua` | Führt expand account node aus (Parameter: _, ftable, _, data). |
| `menu.expandModSlot` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt expand mod slot aus (Parameter: type, slot, row). |
| `menu.expandNode` | 2 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Führt expand node aus (Parameter: _, ftable, _, data). |
| `menu.expandNodeCurrentFaction` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt expand node current faction aus (Parameter: _, ftable, _, data). |
| `menu.expandNodeFaction` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt expand node faction aus (Parameter: _, ftable, _, data). |
| `menu.expandNodeResearch` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt expand node research aus (Parameter: _, ftable, _, data). |
| `menu.expandPersonnel` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt expand personnel aus (Parameter: id, row). |
| `menu.expandUpgrade` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt expand upgrade aus (Parameter: idx, ware, category, row). |
| `menu.expandWeaponMod` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt expand weapon mod aus (Parameter: class, property, row). |
| `menu.extendEntry` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt extend entry aus (Parameter: container, index, force, exclusive). |
| `menu.extendModuleType` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt extend module type aus (Parameter: station, type, notoggle). |
| `menu.extendOrder` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt extend order aus (Parameter: controllable, orderidx, instance). |
| `menu.extendResourceEntry` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt extend resource entry aus (Parameter: id). |
| `menu.extendSectionAndRefresh` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt extend section and refresh aus (Parameter: rowdata). |
| `menu.extensionSorter` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt extension sorter aus (Parameter: a, b). |
| `menu.filterColorDefinition` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt filter color definition aus (Parameter: colordef, text). |
| `menu.filterColorMapping` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt filter color mapping aus (Parameter: colormapping, text). |
| `menu.filterControl` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt filter control aus (Parameter: controltype, code, text). |
| `menu.filterIndexCategory` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Führt filter index category aus (Parameter: text, entry, first). |
| `menu.filterMining` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt filter mining aus (Parameter: value, noupdate). |
| `menu.filterMiningResources` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt filter mining resources aus (Parameter: setting, override). |
| `menu.filterModuleByText` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt filter module by text aus (Parameter: module, texts). |
| `menu.filterName` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt filter name aus (Parameter: id). |
| `menu.filterOther` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt filter other aus (Parameter: value, noupdate). |
| `menu.filterOtherMisc` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt filter other misc aus (Parameter: setting, override, noupdate). |
| `menu.filterOtherShip` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt filter other ship aus (Parameter: setting, override). |
| `menu.filterOtherStation` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt filter other station aus (Parameter: setting, override). |
| `menu.filterSoftwareByText` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt filter software by text aus (Parameter: software, text). |
| `menu.filterThinkAlert` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt filter think alert aus (Parameter: setting, override, noupdate). |
| `menu.filterThinkDiplomacy` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt filter think diplomacy aus (Parameter: setting, override, noupdate). |
| `menu.filterTradeOffer` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt filter trade offer aus (Parameter: setting). |
| `menu.filterTradePlayerOffer` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt filter trade player offer aus (Parameter: setting, override, noupdate). |
| `menu.filterTradePrice` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt filter trade price aus (Parameter: setting). |
| `menu.filterTradeRelation` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt filter trade relation aus (Parameter: setting, override). |
| `menu.filterTradeStorage` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt filter trade storage aus (Parameter: setting). |
| `menu.filterTradeVolume` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt filter trade volume aus (Parameter: setting, override, noupdate). |
| `menu.filterTradeWares` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt filter trade wares aus (Parameter: setting, override, noupdate). |
| `menu.filterUpdate` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt filter update aus (Parameter: _, params). |
| `menu.filterUpgradeByText` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt filter upgrade by text aus (Parameter: mode, upgrade, texts). |
| `menu.findAccountTransaction` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt find account transaction aus (Parameter: station). |
| `menu.findArrayEntry` | 1 | `08/ui/addons/ego_detailmonitor/menu_transporter.lua` | Führt find array entry aus (Parameter: array, component). |
| `menu.findConstructionPlanEntry` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt find construction plan entry aus (Parameter: idx). |
| `menu.findEntryByShipIcon` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt find entry by ship icon aus (Parameter: array, icon, color). |
| `menu.findGroupIndex` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt find group index aus (Parameter: path, group). |
| `menu.findInventoryWare` | 2 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt find inventory ware aus (Parameter: array, ware). |
| `menu.findMacroIdx` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt find macro idx aus (Parameter: array, macro). |
| `menu.findProject` | 1 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Führt find project aus (Parameter: ftable, project). |
| `menu.findProperty` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt find property aus (Parameter: propertyid). |
| `menu.findPropertyName` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt find property name aus (Parameter: propertyid). |
| `menu.findStorageNode` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt find storage node aus (Parameter: edge). |
| `menu.findTech` | 2 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt find tech aus (Parameter: ftable, tech). |
| `menu.findUpgradeMacro` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt find upgrade macro aus (Parameter: loctype, macro). |
| `menu.findWare` | 1 | `08/ui/addons/ego_detailmonitor/menu_trader_inventory.lua` | Führt find ware aus (Parameter: ware). |
| `menu.findWareIdx` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt find ware idx aus (Parameter: array, ware). |
| `menu.fixInputConflicts` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt fix input conflicts aus (Parameter: newinput, checkall). |
| `menu.fixInputConflictsInternal` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt fix input conflicts internal aus (Parameter: controlsorder, newinput, checkall). |
| `menu.fleetUnitBuildProgress` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt fleet unit build progress aus (Parameter: replacement, buildercomponent, commanderlocation). |
| `menu.formatEffectValue` | 1 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Führt format effect value aus (Parameter: effect). |
| `menu.formatRange` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Führt format range aus (Parameter: range). |
| `menu.formatWareAmount` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt format ware amount aus (Parameter: currentamount, futureamount, maxcapacity). |
| `menu.getAccountPlayerMoney` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Gibt account player money zurück. |
| `menu.getAccountWarningColor` | 2 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt account warning color zurück. |
| `menu.getAccountWarningText` | 2 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt account warning text zurück. |
| `menu.getAddedPeopleFromBuildTask` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Gibt added people from build task zurück (Parameter: container, taskid). |
| `menu.getAgentShip` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Gibt agent ship zurück (Parameter: agentindex). |
| `menu.getAgentStatus` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Gibt agent status zurück (Parameter: agentindex, notimer). |
| `menu.getAmmoDataByWare` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt ammo data by ware zurück (Parameter: ware). |
| `menu.getAmmoDataIdxByWare` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt ammo data idx by ware zurück (Parameter: ware). |
| `menu.getAmmoOrderAmountByWare` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt ammo order amount by ware zurück (Parameter: ware). |
| `menu.getAmmoTypeNameByWare` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt ammo type name by ware zurück (Parameter: ware). |
| `menu.getAmmoUsage` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Gibt ammo usage zurück (Parameter: type). |
| `menu.getAmountTextWidth` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt amount text width zurück (Parameter: amounttext). |
| `menu.getBudgetSuffix` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Gibt budget suffix zurück (Parameter: budget). |
| `menu.getBuildProgress` | 3 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt build progress zurück (Parameter: station, name, component). |
| `menu.getBuildResources` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Gibt build resources zurück (Parameter: ware). |
| `menu.getBuildTime` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt build time zurück (Parameter: buildingprocessor, component, ismissingresources). |
| `menu.getCPWares` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Gibt cpwares zurück (Parameter: cpid). |
| `menu.getCanCancelConstructionCount` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Gibt can cancel construction count zurück. |
| `menu.getCargoOrderAmountByWare` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt cargo order amount by ware zurück (Parameter: ware). |
| `menu.getCargoTransportTypes` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt cargo transport types zurück (Parameter: container, aftertradeorders). |
| `menu.getCategoryColor` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Gibt category color zurück (Parameter: category). |
| `menu.getChatColor` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Gibt chat color zurück (Parameter: author, authorid, userid). |
| `menu.getChatMessages` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Gibt chat messages zurück. |
| `menu.getChevrons` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Gibt chevrons zurück (Parameter: origchance, chance). |
| `menu.getColorMapColor` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Gibt color map color zurück (Parameter: color). |
| `menu.getConstructionPlans` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Gibt construction plans zurück. |
| `menu.getContainerAlertLevel` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt container alert level zurück (Parameter: component). |
| `menu.getContainerNameAndColors` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt container name and colors zurück (Parameter: container, iteration, issquadleader, showScanLevel, showbehaviourinspection). |
| `menu.getControlName` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Gibt control name zurück (Parameter: controltype, controlcode). |
| `menu.getControlsData` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Gibt controls data zurück. |
| `menu.getData` | 2 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt data zurück (Parameter: numdatapoints). |
| `menu.getDataAndDisplay` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Gibt data and display zurück (Parameter: upgradeplan, crew, newedit, firsttime, noundo, settings). |
| `menu.getDataIdxByNPC` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt data idx by npc zurück (Parameter: npc). |
| `menu.getDataIdxByWare` | 2 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt data idx by ware zurück (Parameter: ware). |
| `menu.getDefaultControlConflicts` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Gibt default control conflicts zurück (Parameter: defaultmappings, conflicts). |
| `menu.getDefaultControlsData` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Gibt default controls data zurück. |
| `menu.getDefaultShipName` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Gibt default ship name zurück. |
| `menu.getDefinitionColor` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Gibt definition color zurück (Parameter: colorid). |
| `menu.getDescriptionText` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Gibt description text zurück. |
| `menu.getDiplomacyInventory` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Gibt diplomacy inventory zurück. |
| `menu.getDormantStat` | 1 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Gibt dormant stat zurück (Parameter: stat). |
| `menu.getDropDownOption` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Gibt drop down option zurück (Parameter: weapon). |
| `menu.getDropDownTurretModeOption` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt drop down turret mode option zurück (Parameter: defensibleorturret, context, path, group). |
| `menu.getEmployeeList` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Gibt employee list zurück. |
| `menu.getEncyclopediaValue` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Gibt encyclopedia value zurück (Parameter: library, item). |
| `menu.getExplicitSavegameName` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Gibt explicit savegame name zurück (Parameter: savegame, checklastsave). |
| `menu.getExtensionGroup` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Gibt extension group zurück (Parameter: extension). |
| `menu.getExtraText` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Gibt extra text zurück (Parameter: columnwidth, basetext, fullbasetext, macro, price, component, upgradetype). |
| `menu.getFactions` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Gibt factions zurück. |
| `menu.getFilterOption` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt filter option zurück (Parameter: id, savegame). |
| `menu.getFilterThinkAlertOptions` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt filter think alert options zurück. |
| `menu.getFilterTradePlayerOfferOptions` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt filter trade player offer options zurück (Parameter: buysellswitch). |
| `menu.getFilterTradeVolumeOptions` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt filter trade volume options zurück. |
| `menu.getFilterTradeWaresOptions` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt filter trade wares options zurück. |
| `menu.getFleetUnitSubordinates` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt fleet unit subordinates zurück (Parameter: instance, controllable, checkrendered). |
| `menu.getFlowchartDummyProductionNodes` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt flowchart dummy production nodes zurück. |
| `menu.getFlowchartProductionNodes` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt flowchart production nodes zurück. |
| `menu.getGroupIdxByID` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt group idx by id zurück (Parameter: id). |
| `menu.getImportablePlans` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Gibt importable plans zurück. |
| `menu.getInputDeviceIcon` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Gibt input device icon zurück (Parameter: device). |
| `menu.getInputName` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Gibt input name zurück (Parameter: source, code, signum). |
| `menu.getInventoryName` | 2 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Gibt inventory name zurück (Parameter: ware, waredata, showunread). |
| `menu.getKnownValue` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Gibt known value zurück (Parameter: property, item). |
| `menu.getLanguageData` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Gibt language data zurück. |
| `menu.getLastUnprocessedSubordinate` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Gibt last unprocessed subordinate zurück (Parameter: shipidstring, list_processed). |
| `menu.getLatestOnlineSave` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Gibt latest online save zurück. |
| `menu.getLeftBarEntry` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Gibt left bar entry zurück (Parameter: mode). |
| `menu.getLeftBarLoadoutEntry` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Gibt left bar loadout entry zurück (Parameter: mode). |
| `menu.getLoadoutSummary` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Gibt loadout summary zurück (Parameter: upgradeplan, crew, repairplan, paintmodware). |
| `menu.getLockedStories` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Gibt locked stories zurück. |
| `menu.getManualOrder` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt manual order zurück (Parameter: macro, auto). |
| `menu.getMappedButtons` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Gibt mapped buttons zurück (Parameter: buttons, compassmenubutton, displayed, input, mappable). |
| `menu.getMappingColor` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Gibt mapping color zurück (Parameter: mappingid). |
| `menu.getMessageReceiverID` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Gibt message receiver id zurück (Parameter: userid, groupid). |
| `menu.getMinFleetUnitSubordinateCommanderDistance` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt min fleet unit subordinate commander distance zurück (Parameter: instance, replacementcandidate, fleetunit, firstcommandercomponent). |
| `menu.getMissileAmount` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt missile amount zurück (Parameter: defenceinfo_high). |
| `menu.getMissionContextTime` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt mission context time zurück. |
| `menu.getMissionData` | 1 | `08/ui/addons/ego_detailmonitor/menu_missionbriefing.lua` | Gibt mission data zurück. |
| `menu.getMissionIDInfoHelper` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt mission idinfo helper zurück (Parameter: missionID). |
| `menu.getMissionInfoFromPerson` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt mission info from person zurück (Parameter: seed, origin). |
| `menu.getMissionInfoHelper` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt mission info helper zurück (Parameter: mission). |
| `menu.getMissionTimeAndDifficulty` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt mission time and difficulty zurück (Parameter: missionid, difficulty). |
| `menu.getModQuality` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Gibt mod quality zurück (Parameter: category). |
| `menu.getModUpgradeMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Gibt mod upgrade mode zurück (Parameter: upgradetype). |
| `menu.getModuleData` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt module data zurück (Parameter: object64). |
| `menu.getModules` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Gibt modules zurück (Parameter: uitype, moduletype, races, connectionmoduleraces). |
| `menu.getMonitorExtents` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Gibt monitor extents zurück (Parameter: monitoroffset, uianchorindex, visframe). |
| `menu.getMultiSelectEntryName` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Gibt multi select entry name zurück (Parameter: property, entry). |
| `menu.getNPCs` | 1 | `08/ui/addons/ego_detailmonitor/menu_transporter.lua` | Gibt npcs zurück (Parameter: room, ships, issubtarget). |
| `menu.getNewSavegameName` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Gibt new savegame name zurück (Parameter: savegame). |
| `menu.getNumDefendingCrew` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt num defending crew zurück (Parameter: objectid). |
| `menu.getNumEntries` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Gibt num entries zurück (Parameter: category). |
| `menu.getNumNonKeyboardInputs` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Gibt num non keyboard inputs zurück (Parameter: controltype, code). |
| `menu.getNumOperationalTurrets` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt num operational turrets zurück (Parameter: objectid, numtotalturrets). |
| `menu.getNumSelectedComponents` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt num selected components zurück. |
| `menu.getOrderInfo` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt order info zurück (Parameter: ship, gettargetname). |
| `menu.getParamValue` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt param value zurück (Parameter: type, value, inputparams). |
| `menu.getPlayerMacroIcon` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Gibt player macro icon zurück (Parameter: gamestart). |
| `menu.getPlayerSquad` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Gibt player squad zurück. |
| `menu.getPresetLoadouts` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Gibt preset loadouts zurück. |
| `menu.getPrimaryJunctionEdgeColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt primary junction edge color zurück (Parameter: edges). |
| `menu.getPrivateMessages` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Gibt private messages zurück (Parameter: receiverid, receivername, groupid, timestamp). |
| `menu.getProcessingCycleTime` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt processing cycle time zurück (Parameter: modules). |
| `menu.getProductionCycleTime` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt production cycle time zurück (Parameter: modules). |
| `menu.getProductionEfficiency` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt production efficiency zurück (Parameter: modules). |
| `menu.getProductionEfficiencyProducts` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt production efficiency products zurück (Parameter: ware, macro, producing). |
| `menu.getProductionHullEfficiency` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt production hull efficiency zurück (Parameter: modules). |
| `menu.getProductionRemainingTime` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt production remaining time zurück (Parameter: ware, modules, macro). |
| `menu.getProductionWorkforceEfficiency` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt production workforce efficiency zurück (Parameter: modules). |
| `menu.getProducts` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Gibt products zurück (Parameter: funcware). |
| `menu.getPropertyOwnedFleetData` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt property owned fleet data zurück (Parameter: instance, component, macro, maxentries). |
| `menu.getPropertyOwnedFleetDataInternal` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt property owned fleet data internal zurück (Parameter: instance, component, macro, shiptyperanks, shiptypedata). |
| `menu.getPropertyOwnedGroupIcons` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt property owned group icons zurück (Parameter: instance, component, subordinates). |
| `menu.getPropertyOwnedGroupIcons_getData` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt property owned group icons get data zurück (Parameter: instance, component, shipstates, shipstatesdata, sectorbase). |
| `menu.getRegionDefinitions` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Gibt region definitions zurück. |
| `menu.getReservationsAmountByWareType` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt reservations amount by ware type zurück (Parameter: contextcomponent). |
| `menu.getReservationsAmountTotal` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt reservations amount total zurück (Parameter: contextcomponent). |
| `menu.getReservationsVolumeByTransportType` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt reservations volume by transport type zurück (Parameter: contextcomponent). |
| `menu.getResources` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Gibt resources zurück (Parameter: funcware). |
| `menu.getSelectedComponentCategories` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt selected component categories zurück. |
| `menu.getShipBuildProgress` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt ship build progress zurück (Parameter: ship, name). |
| `menu.getShipIconWidth` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt ship icon width zurück. |
| `menu.getShipList` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt ship list zurück (Parameter: includePlayerOccupiedShip, includeShipsWithOrderLoops). |
| `menu.getSpline` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Gibt spline zurück. |
| `menu.getStoryDependencies` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Gibt story dependencies zurück (Parameter: property, knownitem). |
| `menu.getSubMissionTimer` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt sub mission timer zurück (Parameter: submissionentry). |
| `menu.getSubTargetName` | 1 | `08/ui/addons/ego_detailmonitor/menu_transporter.lua` | Gibt sub target name zurück (Parameter: subtarget). |
| `menu.getSubordinates` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt subordinates zurück (Parameter: controllable, controllable64, checkrendered, classid). |
| `menu.getSubordinatesInFleetUnitGroups` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Gibt subordinates in fleet unit groups zurück (Parameter: commanderfleetunit, assignment, singlegroup). |
| `menu.getSubordinatesInGroups` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Gibt subordinates in groups zurück (Parameter: commander, isstation, assignment, singlegroup). |
| `menu.getSuccessText` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Gibt success text zurück (Parameter: successchance). |
| `menu.getSupplyIdx` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt supply idx zurück (Parameter: array, macro). |
| `menu.getSupplyResourceMax` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt supply resource max zurück (Parameter: ware, raw). |
| `menu.getSupplyResourceValue` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Gibt supply resource value zurück (Parameter: ware). |
| `menu.getSystemInfo` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Gibt system info zurück (Parameter: cluster). |
| `menu.getTradeContextInitialStorageData` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt trade context initial storage data zurück (Parameter: container, transporttypes, aftertradeorders). |
| `menu.getTradeContextRowContent` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt trade context row content zurück (Parameter: waredata). |
| `menu.getTradeContextShipStorageContent` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt trade context ship storage content zurück (Parameter: othership). |
| `menu.getTradeContextStorableAmountAfterTradeOrders` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt trade context storable amount after trade orders zurück (Parameter: ship, ware, ammotypename). |
| `menu.getTradeOfferByID` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt trade offer by id zurück (Parameter: id). |
| `menu.getTradeWareFilter` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt trade ware filter zurück (Parameter: force). |
| `menu.getTransportTagsFromString` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt transport tags from string zurück (Parameter: s). |
| `menu.getTruncatedOptionText` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Gibt truncated option text zurück (Parameter: text, indicatortext, width). |
| `menu.getUpgradeData` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Gibt upgrade data zurück (Parameter: upgradeplan). |
| `menu.getUpgradeTypeText` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Gibt upgrade type text zurück (Parameter: upgradetype). |
| `menu.getWareButtonColorAndScript` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Gibt ware button color and script zurück (Parameter: filteroptionlist, setting, contextware). |
| `menu.handlePlannedDefaultOrder` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt handle planned default order aus (Parameter: instance, confirmed, callback). |
| `menu.handlePlannedDefaultOrderRendertargetSelect` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt handle planned default order rendertarget select aus (Parameter: confirmed). |
| `menu.handleSubSectionOption` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt handle sub section option aus (Parameter: data, skipdelay). |
| `menu.hasContext` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt has context aus (Parameter: contexts). |
| `menu.hasContextSimple` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt has context simple aus (Parameter: context). |
| `menu.hasShipOrRoomMissionTarget` | 1 | `08/ui/addons/ego_detailmonitor/menu_transporter.lua` | Führt has ship or room mission target aus (Parameter: subtarget). |
| `menu.hasUnreadEntries` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Führt has unread entries aus. |
| `menu.hireReasonLookup` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt hire reason lookup aus (Parameter: reason, isbulk). |
| `menu.hotkey` | 8 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt hotkey aus (Parameter: action). |
| `menu.iconNewGame` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt icon new game aus. |
| `menu.importMenuParameters` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt import menu parameters aus. |
| `menu.info` | 1 | `08/ui/addons/ego_detailmonitor/menu_help.lua` | Führt info aus. |
| `menu.infoBoxColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt info box color aus. |
| `menu.infoChangeObjectName` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info change object name aus (Parameter: objectid, text, textchanged). |
| `menu.infoCombineLoadoutComponents` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info combine loadout components aus (Parameter: components). |
| `menu.infoHandler` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt info handler aus. |
| `menu.infoSetWeaponGroup` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info set weapon group aus (Parameter: objectid, weaponid, primary, group, active). |
| `menu.infoSubmenuCancelTransfer` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info submenu cancel transfer aus (Parameter: controllable, person). |
| `menu.infoSubmenuCombineCrewTables` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info submenu combine crew tables aus (Parameter: instance). |
| `menu.infoSubmenuConfirmCrewChanges` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info submenu confirm crew changes aus (Parameter: instance). |
| `menu.infoSubmenuConfirmDrops` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info submenu confirm drops aus (Parameter: object, instance). |
| `menu.infoSubmenuFireAllNPCConfirm` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info submenu fire all npcconfirm aus (Parameter: controllable, instance). |
| `menu.infoSubmenuFireNPC` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info submenu fire npc aus (Parameter: controllable, entity, person, instance). |
| `menu.infoSubmenuFireNPCConfirm` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info submenu fire npcconfirm aus (Parameter: controllable, entity, person, instance). |
| `menu.infoSubmenuPrepareCrewInfo` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info submenu prepare crew info aus (Parameter: instance). |
| `menu.infoSubmenuReplacePilot` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info submenu replace pilot aus (Parameter: ship, oldpilot, newpilot, checkonly, contextmenu, instance). |
| `menu.infoSubmenuSetManagerAccountToEstimate` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info submenu set manager account to estimate aus (Parameter: i, instance). |
| `menu.infoSubmenuUpdateCrewChanges` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info submenu update crew changes aus (Parameter: instance, newamount, slidertable, sliderindex, istier, tierindex, sliderupdatetable). |
| `menu.infoSubmenuUpdateDrops` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info submenu update drops aus (Parameter: ware, oldamount, newamount, instance). |
| `menu.infoSubmenuUpdateManagerAccount` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info submenu update manager account aus (Parameter: i, instance). |
| `menu.infoSubmenuUpdateProductionTime` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info submenu update production time aus (Parameter: object64, moduleindex). |
| `menu.infoSubmenuUpdateTransferAmount` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info submenu update transfer amount aus (Parameter: instance, value, idx, containercash). |
| `menu.infoText` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt info text aus. |
| `menu.infoUpdatePeople` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info update people aus. |
| `menu.infoWeaponGroupCheckBoxColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt info weapon group check box color aus (Parameter: objectid, groupidx, primary). |
| `menu.infologbookSearchHelper` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt infologbook search helper aus (Parameter: entry, text, text2). |
| `menu.initCrewTransferData` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt init crew transfer data aus. |
| `menu.initData` | 2 | `08/ui/addons/ego_detailmonitor/menu_trader_blueprintsorlicences.lua` | Führt init data aus. |
| `menu.initEmpireData` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt init empire data aus. |
| `menu.initEncyclopediaValue` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt init encyclopedia value aus. |
| `menu.initExtendedEntry` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt init extended entry aus (Parameter: container). |
| `menu.initFactions` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt init factions aus. |
| `menu.initKnownValue` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt init known value aus. |
| `menu.initManagerSkills` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt init manager skills aus (Parameter: property, entryid). |
| `menu.initPlotList` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt init plot list aus. |
| `menu.initPropertyValue` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt init property value aus (Parameter: property). |
| `menu.initResearch` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt init research aus. |
| `menu.initSatellites` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt init satellites aus. |
| `menu.initStoryValue` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt init story value aus. |
| `menu.initTradeContextData` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt init trade context data aus. |
| `menu.initWareData` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Führt init ware data aus (Parameter: funcware). |
| `menu.initializeBoardingData` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt initialize boarding data aus (Parameter: target). |
| `menu.inputProfileDescription` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt input profile description aus. |
| `menu.insertAssignSubActions` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt insert assign sub actions aus (Parameter: section, assignment, callback, groups, isstation, unique, currentgroup, mouseovertextadd). |
| `menu.insertComponent` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt insert component aus (Parameter: array, objectarray, component, pricetype). |
| `menu.insertInteractionContent` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt insert interaction content aus (Parameter: section, entry). |
| `menu.insertLuaAction` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt insert lua action aus (Parameter: actiontype, istobedisplayed). |
| `menu.insertWare` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt insert ware aus (Parameter: array, objectarray, category, ware, count, pricetype). |
| `menu.isAmmoCompatible` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Prüft ob ammo compatible (Parameter: type, ammomacro). |
| `menu.isBudgetIDOverBudget` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Prüft ob budget idover budget (Parameter: budgetid). |
| `menu.isBudgetOverBudget` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Prüft ob budget over budget (Parameter: budget). |
| `menu.isCommander` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Prüft ob commander (Parameter: component, fleetunit, group). |
| `menu.isConstructionContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Prüft ob construction context (Parameter: component). |
| `menu.isConstructionExtended` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Prüft ob construction extended (Parameter: name). |
| `menu.isControlDefault` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Prüft ob control default (Parameter: controltype, code). |
| `menu.isCurrentSelectionWhiteListed` | 1 | `08/ui/addons/ego_detailmonitor/menu_platformundock.lua` | Prüft ob current selection white listed. |
| `menu.isDataSelectionChanged` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Prüft ob data selection changed. |
| `menu.isDockButtonActive` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Prüft ob dock button active. |
| `menu.isDockContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Prüft ob dock context (Parameter: component). |
| `menu.isDockedShipsExtended` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Prüft ob docked ships extended (Parameter: name, isstation). |
| `menu.isEncyclopediaValueItemChanged` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Prüft ob encyclopedia value item changed (Parameter: checklibrary, checkitem). |
| `menu.isEntryExtended` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Prüft ob entry extended (Parameter: container, index). |
| `menu.isEquipmentModExpanded` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Prüft ob equipment mod expanded (Parameter: class, property). |
| `menu.isGroupExpanded` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Prüft ob group expanded (Parameter: groupID). |
| `menu.isInfoExtended` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Prüft ob info extended (Parameter: buttondata, instance). |
| `menu.isInfoModeValidFor` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Prüft ob info mode valid for (Parameter: object, mode). |
| `menu.isInputSourceKeyboardMouse` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Prüft ob input source keyboard mouse (Parameter: source). |
| `menu.isKnownValueItemChanged` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Prüft ob known value item changed (Parameter: property, checkitem). |
| `menu.isMakerRaceAllowed` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Prüft ob maker race allowed (Parameter: makerraces, objectmakerraces). |
| `menu.isModSlotExpanded` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Prüft ob mod slot expanded (Parameter: type, slot). |
| `menu.isModuleTypeExtended` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Prüft ob module type extended (Parameter: station, type). |
| `menu.isObjectValid` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Prüft ob object valid (Parameter: object, optclass, optrealclass). |
| `menu.isOptionSelectionChanged` | 2 | `08/ui/addons/ego_gameoptions/customgame.lua` | Prüft ob option selection changed. |
| `menu.isOrderExtended` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Prüft ob order extended (Parameter: controllable, orderidx, instance, default). |
| `menu.isPersonTransferPossible` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Prüft ob person transfer possible (Parameter: person). |
| `menu.isPersonnelExpanded` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Prüft ob personnel expanded (Parameter: id). |
| `menu.isPropertyExtended` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Prüft ob property extended (Parameter: name). |
| `menu.isResearchAvailable` | 2 | `08/ui/addons/ego_gameoptions/customgame.lua` | Prüft ob research available (Parameter: tech, mainIdx, col). |
| `menu.isResourceEntryExtended` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Prüft ob resource entry extended (Parameter: id, default). |
| `menu.isSectorSelectionChanged` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Prüft ob sector selection changed. |
| `menu.isSelectedComponent` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Prüft ob selected component (Parameter: component). |
| `menu.isShipAlreadyBoarding` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Prüft ob ship already boarding (Parameter: shipid). |
| `menu.isSubordinateExtended` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Prüft ob subordinate extended (Parameter: name, group). |
| `menu.isUndockButtonActive` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Prüft ob undock button active. |
| `menu.isUpgradeExpanded` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Prüft ob upgrade expanded (Parameter: idx, ware, category). |
| `menu.isValidSaveSelected` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Prüft ob valid save selected. |
| `menu.isVentureExtensionRestartRequired` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Prüft ob venture extension restart required. |
| `menu.isWareSelectionChanged` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Prüft ob ware selection changed. |
| `menu.ladderPending` | 2 | `08/ui/addons/ego_detailmonitor/menu_scenario_debriefing.lua` | Führt ladder pending aus. |
| `menu.loadGameCallback` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Lädt game callback (Parameter: filename, checked). |
| `menu.loadSaveCallback` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Lädt save callback (Parameter: _, filename). |
| `menu.logbookSearchHelper` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt logbook search helper aus (Parameter: entry, text). |
| `menu.logoButtonIcon2` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt logo button icon2 aus (Parameter: logo). |
| `menu.logoButtonIcon2Color` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt logo button icon2 color aus (Parameter: logo). |
| `menu.macroSearchColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Führt macro search color aus. |
| `menu.macroSearchText` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Führt macro search text aus. |
| `menu.messageCategoryIcon` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt message category icon aus (Parameter: entry). |
| `menu.messageHelper` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt message helper aus (Parameter: numQuery, startIdx, category). |
| `menu.messageSidebarIcon` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt message sidebar icon aus. |
| `menu.messageSidebarIconColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt message sidebar icon color aus. |
| `menu.missionListSorter` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt mission list sorter aus (Parameter: a, b). |
| `menu.missionOfferSorter` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt mission offer sorter aus (Parameter: a, b). |
| `menu.moduleHeightHelper` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt module height helper aus (Parameter: ftable, prevfullheight). |
| `menu.moduleSorter` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt module sorter aus (Parameter: a, b). |
| `menu.mouseOverTextGfxUpscaling` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt mouse over text gfx upscaling aus. |
| `menu.movePerson` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Bewegt person (Parameter: origin, i, j, person, k). |
| `menu.nameAccessibility` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name accessibility aus. |
| `menu.nameColorBlind` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name color blind aus. |
| `menu.nameConnection` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name connection aus. |
| `menu.nameContinue` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name continue aus. |
| `menu.nameDisplay` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name display aus. |
| `menu.nameExtension` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name extension aus. |
| `menu.nameExtensionSettingEnabled` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name extension setting enabled aus. |
| `menu.nameExtensionSettings` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name extension settings aus. |
| `menu.nameGfx` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name gfx aus. |
| `menu.nameInput` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name input aus. |
| `menu.nameLanguage` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name language aus. |
| `menu.nameLogin` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name login aus. |
| `menu.nameModifier` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name modifier aus (Parameter: name, row, col). |
| `menu.nameNewAssignment` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name new assignment aus (Parameter: nokeyboard, nocontroller). |
| `menu.nameOnline` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name online aus. |
| `menu.nameOnlineSeason` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name online season aus. |
| `menu.nameReturnToHub` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name return to hub aus. |
| `menu.nameSettings` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name settings aus. |
| `menu.nameUserQuestion` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt name user question aus. |
| `menu.newGameCallback` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt new game callback aus (Parameter: option, checked). |
| `menu.newWareReservationCallback` | 3 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Führt new ware reservation callback aus (Parameter: _, data). |
| `menu.nextHelp` | 1 | `08/ui/addons/ego_helptext/helptext.lua` | Führt next help aus. |
| `menu.nodevalueProject` | 2 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Führt nodevalue project aus (Parameter: project). |
| `menu.onActiveProjectCleared` | 1 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Führt on active project cleared aus. |
| `menu.onAnnouncementReceived` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt on announcement received aus (Parameter: _, message). |
| `menu.onButtonDown` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on button down aus. |
| `menu.onButtonOver` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt on button over aus (Parameter: uitable, row, col, button). |
| `menu.onButtonOverSound` | 2 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt on button over sound aus (Parameter: uitable, row, col, button, input). |
| `menu.onButtonRightMouseClick` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on button right mouse click aus. |
| `menu.onButtonUp` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on button up aus. |
| `menu.onChatMessageReceived` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt on chat message received aus. |
| `menu.onChatReported` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt on chat reported aus (Parameter: _, timestamp). |
| `menu.onClearHelp` | 1 | `08/ui/addons/ego_helptext/helptext.lua` | Führt on clear help aus (Parameter: event, id). |
| `menu.onClientStarted` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt on client started aus. |
| `menu.onCloseElement` | 34 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt on close element aus (Parameter: dueToClose, layer, allowAutoMenu). |
| `menu.onColChanged` | 3 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Führt on col changed aus (Parameter: row, col). |
| `menu.onCollapseDummy` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt on collapse dummy aus (Parameter: nodedata). |
| `menu.onCollapseSupply` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt on collapse supply aus (Parameter: nodedata). |
| `menu.onConvEnds` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt on conv ends aus. |
| `menu.onCutsceneReady` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt on cutscene ready aus (Parameter: _, cutsceneid). |
| `menu.onCutsceneStopped` | 6 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt on cutscene stopped aus (Parameter: _, cutsceneID). |
| `menu.onDropDownActivated` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt on drop down activated aus. |
| `menu.onEditBoxActivated` | 5 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt on edit box activated aus. |
| `menu.onEditboxRightMouseClick` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on editbox right mouse click aus. |
| `menu.onEditboxUpdateText` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt on editbox update text aus (Parameter: editbox, text, textchanged, wasconfirmed). |
| `menu.onExpandAccount` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt on expand account aus (Parameter: _, ftable, _, nodedata). |
| `menu.onExpandBuildModule` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt on expand build module aus (Parameter: _, ftable, _, nodedata, buildmodule). |
| `menu.onExpandCondensateShield` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt on expand condensate shield aus (Parameter: _, ftable, _, nodedata). |
| `menu.onExpandDestroyedModule` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt on expand destroyed module aus (Parameter: _, ftable, _, nodedata, module). |
| `menu.onExpandDummy` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt on expand dummy aus (Parameter: _, ftable, _, nodedata). |
| `menu.onExpandPlannedBuildModule` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt on expand planned build module aus (Parameter: _, ftable, _, nodedata, buildmodule). |
| `menu.onExpandProcessing` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt on expand processing aus (Parameter: _, ftable, _, nodedata, processingmodules). |
| `menu.onExpandProduction` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt on expand production aus (Parameter: _, ftable, _, nodedata, productionmodules). |
| `menu.onExpandResearch` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt on expand research aus (Parameter: _, ftable, _, nodedata, researchmodule). |
| `menu.onExpandSupply` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt on expand supply aus (Parameter: _, ftable, _, nodedata). |
| `menu.onExpandSupplyResource` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt on expand supply resource aus (Parameter: _, ftable, _, nodedata). |
| `menu.onExpandTerraforming` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt on expand terraforming aus (Parameter: _, ftable, _, nodedata, project). |
| `menu.onExpandTradeWares` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt on expand trade wares aus (Parameter: frame, ftable, ftable2, nodedata). |
| `menu.onExpandWorkforce` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt on expand workforce aus (Parameter: _, ftable, _, nodedata). |
| `menu.onExtensionSettingChanged` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt on extension setting changed aus. |
| `menu.onFlowchartNodeCollapsed` | 4 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt on flowchart node collapsed aus (Parameter: node, frame). |
| `menu.onFlowchartNodeExpanded` | 4 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt on flowchart node expanded aus (Parameter: node, frame, ftable, ftable2). |
| `menu.onGameModified` | 1 | `08/ui/addons/ego_gameoptions/gamemodified.lua` | Führt on game modified aus. |
| `menu.onGamePlanChange` | 3 | `08/ui/addons/ego_detailmonitor/menu_toplevel.lua` | Führt on game plan change aus (Parameter: _, mode). |
| `menu.onGameSaved` | 2 | `08/ui/addons/ego_gameoptions/onlineupdate.lua` | Führt on game saved aus (Parameter: _, success). |
| `menu.onGfxBusy` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt on gfx busy aus. |
| `menu.onGfxDone` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt on gfx done aus. |
| `menu.onHotkey` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt on hotkey aus (Parameter: action). |
| `menu.onInputModeChanged` | 13 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt on input mode changed aus (Parameter: _, mode). |
| `menu.onInteractMenuCallback` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on interact menu callback aus (Parameter: type, param). |
| `menu.onInteractiveElementChanged` | 4 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on interactive element changed aus (Parameter: element). |
| `menu.onInventoryRowChange` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt on inventory row change aus (Parameter: row, rowdata, input, mode). |
| `menu.onLoadingDone` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on loading done aus. |
| `menu.onMinimizeMenu` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on minimize menu aus. |
| `menu.onMissionOfferRemoved` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on mission offer removed aus (Parameter: event, id). |
| `menu.onMissionRemoved` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on mission removed aus (Parameter: event, id). |
| `menu.onOnlineLogin` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt on online login aus (Parameter: _, serializedArg). |
| `menu.onOpenSubMenu` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt on open sub menu aus (Parameter: _, submenu). |
| `menu.onPlayerActivityChanged` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt on player activity changed aus. |
| `menu.onPlayerCameraModeChanged` | 1 | `08/ui/addons/ego_detailmonitor/menu_followcamera.lua` | Führt on player camera mode changed aus (Parameter: _, mode). |
| `menu.onPropertyDropDownActivated` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt on property drop down activated aus (Parameter: property, row, dropdown). |
| `menu.onRenderTargetCombinedScrollDown` | 5 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt on render target combined scroll down aus (Parameter: step). |
| `menu.onRenderTargetCombinedScrollUp` | 5 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt on render target combined scroll up aus (Parameter: step). |
| `menu.onRenderTargetDoubleClick` | 3 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on render target double click aus (Parameter: modified). |
| `menu.onRenderTargetMiddleMouseDown` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on render target middle mouse down aus. |
| `menu.onRenderTargetMiddleMouseUp` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on render target middle mouse up aus. |
| `menu.onRenderTargetMouseDown` | 5 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt on render target mouse down aus (Parameter: modified). |
| `menu.onRenderTargetMouseUp` | 5 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt on render target mouse up aus (Parameter: modified). |
| `menu.onRenderTargetRightMouseDown` | 5 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt on render target right mouse down aus. |
| `menu.onRenderTargetRightMouseUp` | 5 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt on render target right mouse up aus (Parameter: modified). |
| `menu.onRenderTargetSelect` | 4 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt on render target select aus (Parameter: modified). |
| `menu.onRestoreMenu` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on restore menu aus. |
| `menu.onRestoreState` | 9 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt on restore state aus (Parameter: state). |
| `menu.onRowChanged` | 27 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt on row changed aus. |
| `menu.onRowChangedSound` | 2 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt on row changed sound aus (Parameter: row, rowdata, uitable, layer, modified, input, source). |
| `menu.onSaveState` | 9 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt on save state aus. |
| `menu.onSelectElement` | 26 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt on select element aus (Parameter: uitable, modified, row, isdblclick, input). |
| `menu.onShowCutscene` | 1 | `08/ui/addons/ego_movie/movie.lua` | Führt on show cutscene aus (Parameter: _, detailmonitorCutsceneID). |
| `menu.onShowHelp` | 1 | `08/ui/addons/ego_helptext/helptext.lua` | Führt on show help aus (Parameter: event, params). |
| `menu.onShowHelpMulti` | 1 | `08/ui/addons/ego_helptext/helptext.lua` | Führt on show help multi aus (Parameter: event, params). |
| `menu.onShowMenu` | 33 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt on show menu aus (Parameter: _, _, serializedArg). |
| `menu.onShowMenuSound` | 9 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt on show menu sound aus. |
| `menu.onSliderCellActivated` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on slider cell activated aus. |
| `menu.onSliderCellConfirm` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt on slider cell confirm aus. |
| `menu.onSliderCellDown` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on slider cell down aus. |
| `menu.onTabScroll` | 13 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt on tab scroll aus (Parameter: direction). |
| `menu.onTableMouseOut` | 8 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt on table mouse out aus (Parameter: uitable, row). |
| `menu.onTableMouseOver` | 8 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt on table mouse over aus (Parameter: uitable, row). |
| `menu.onTableRightMouseClick` | 7 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt on table right mouse click aus (Parameter: uitable, row, posx, posy). |
| `menu.onTableScrollBarDown` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on table scroll bar down aus. |
| `menu.onTableScrollBarUp` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt on table scroll bar up aus. |
| `menu.onTimelinesRankingsReceived` | 2 | `08/ui/addons/ego_detailmonitor/menu_scenario_debriefing.lua` | Führt on timelines rankings received aus (Parameter: _, success). |
| `menu.onTimelinesScoreUploaded` | 1 | `08/ui/addons/ego_detailmonitor/menu_scenario_debriefing.lua` | Führt on timelines score uploaded aus. |
| `menu.onUpdate` | 34 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt on update aus. |
| `menu.onVersionIncompatible` | 2 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt on version incompatible aus. |
| `menu.openComm` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Öffnet comm (Parameter: component). |
| `menu.openCommWithActor` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Öffnet comm with actor (Parameter: actor). |
| `menu.openDetails` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Öffnet details (Parameter: component). |
| `menu.openOtherMenu` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Öffnet other menu (Parameter: menuname). |
| `menu.openPlayerPropertyShipConfig` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Öffnet player property ship config (Parameter: row, entryid, macro, commanderid, peopledef, peoplefillpercentage, count). |
| `menu.openShipConfig` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Öffnet ship config. |
| `menu.openSubmenu` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Öffnet submenu (Parameter: optionParameter, selectedOption). |
| `menu.orderAmountHelper` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt order amount helper aus (Parameter: sellid, buyid, newvalue). |
| `menu.orderAssignCommander` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order assign commander aus (Parameter: component, commander, assignment, group, informfleetmanager). |
| `menu.orderAttack` | 2 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order attack aus (Parameter: component, target, clear, immediate). |
| `menu.orderAttackInRange` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order attack in range aus (Parameter: component, sector, offset, clear). |
| `menu.orderAttackMultiple` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt order attack multiple aus (Parameter: component, maintarget, secondarytargets, clear). |
| `menu.orderAttackSurfaceElements` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order attack surface elements aus (Parameter: component, target, targetclasses, clear). |
| `menu.orderCollect` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order collect aus (Parameter: component, drop, sector, offset, clear). |
| `menu.orderCollectDeployable` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order collect deployable aus (Parameter: component, deployable, sector, offset, clear). |
| `menu.orderCollectDeployables` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt order collect deployables aus (Parameter: component, deployables, clear). |
| `menu.orderCollectLockbox` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order collect lockbox aus (Parameter: component, lockbox, clear). |
| `menu.orderCollectRadius` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order collect radius aus (Parameter: component, sector, offset, clear). |
| `menu.orderDeployAtPosition` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order deploy at position aus (Parameter: component, sector, offset, macro, amount, clear). |
| `menu.orderDeployToStation` | 2 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order deploy to station aus (Parameter: component, station, clear). |
| `menu.orderDepositInventoryAtHQ` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order deposit inventory at hq aus (Parameter: component, clear). |
| `menu.orderDock` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order dock aus (Parameter: component, target, clear, ventureplatform). |
| `menu.orderExplore` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order explore aus (Parameter: component, sectororgate, sector, offset, clear). |
| `menu.orderExploreUpdate` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order explore update aus (Parameter: component, sectororgate, sector, offset, clear). |
| `menu.orderFollow` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order follow aus (Parameter: component, targetobject, clear). |
| `menu.orderGetSupplies` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order get supplies aus (Parameter: component, clear). |
| `menu.orderIconText` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order icon text aus (Parameter: orderid). |
| `menu.orderMining` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order mining aus (Parameter: component, ware, sector, offset, clear). |
| `menu.orderMoveWait` | 2 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order move wait aus (Parameter: component, sector, offset, targetobject, playerprecise, clear). |
| `menu.orderPlayerDockToTrade` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order player dock to trade aus (Parameter: component, target, clear). |
| `menu.orderProtect` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order protect aus (Parameter: component, target, clear). |
| `menu.orderRemove` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order remove aus (Parameter: ship, removedefaultorder, removeassignment, removedockorder). |
| `menu.orderRescueInRange` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order rescue in range aus (Parameter: component, sector, offset, clear). |
| `menu.orderRescueShip` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order rescue ship aus (Parameter: component, targetobject, clear). |
| `menu.orderSalvageCollect` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order salvage collect aus (Parameter: component, target, clear). |
| `menu.orderSalvageCrush` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order salvage crush aus (Parameter: component, target, clear). |
| `menu.orderSalvageDeliver` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order salvage deliver aus (Parameter: component, target, tradeoffer, amount, clear). |
| `menu.orderSalvageDeliver_NoTrade` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order salvage deliver no trade aus (Parameter: component, target, clear). |
| `menu.orderSalvageInRadius` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order salvage in radius aus (Parameter: component, sector, offset, clear). |
| `menu.orderStopAndHoldFire` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order stop and hold fire aus (Parameter: component, clear, immediate). |
| `menu.orderTacticalAttack` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order tactical attack aus (Parameter: component, target, clear, immediate). |
| `menu.orderWithdrawAndHold` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order withdraw and hold aus (Parameter: component, clear, immediate). |
| `menu.orderWithdrawFromCombat` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt order withdraw from combat aus (Parameter: component, clear, immediate, attacker). |
| `menu.overrideOrderIcon` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt override order icon aus (Parameter: normalcolor, usetext, icon, prefix, postfix). |
| `menu.performCrewExchange` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt perform crew exchange aus (Parameter: checkonly). |
| `menu.personName` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt person name aus (Parameter: person, origin, target). |
| `menu.playerBuildMethod` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt player build method aus (Parameter: current, customoptions). |
| `menu.playerMacro` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt player macro aus (Parameter: current, customoptions). |
| `menu.playerMoney` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt player money aus (Parameter: start). |
| `menu.playerPaintThemes` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt player paint themes aus (Parameter: current, customoptions). |
| `menu.playerUndocked` | 1 | `08/ui/addons/ego_detailmonitor/menu_toplevel.lua` | Führt player undocked aus. |
| `menu.playerresearchActive` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt playerresearch active aus. |
| `menu.playerresearchMouseOver` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt playerresearch mouse over aus. |
| `menu.plotCourse` | 2 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt plot course aus (Parameter: object, offset). |
| `menu.plotInitiateConstruction` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt plot initiate construction aus (Parameter: station). |
| `menu.plotModeUpdatePrice` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt plot mode update price aus. |
| `menu.plotModeUpdateValue` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt plot mode update value aus (Parameter: dimension, valchange). |
| `menu.populateUpkeepMissionData` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt populate upkeep mission data aus. |
| `menu.precursorSorter` | 2 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt precursor sorter aus (Parameter: a, b). |
| `menu.prefixIconTopLevel` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt prefix icon top level aus (Parameter: type). |
| `menu.prepareActions` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt prepare actions aus. |
| `menu.prepareComponentCrewInfo` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt prepare component crew info aus (Parameter: object). |
| `menu.prepareComponentUpgradeSlots` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt prepare component upgrade slots aus (Parameter: object, slots, ammo, software, changeupgradeplan). |
| `menu.prepareData` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt prepare data aus. |
| `menu.prepareEconomyWares` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt prepare economy wares aus. |
| `menu.prepareInfoContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt prepare info context aus (Parameter: rowdata, instance). |
| `menu.prepareKnownSectors` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt prepare known sectors aus. |
| `menu.prepareMacroCrewInfo` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt prepare macro crew info aus (Parameter: macro). |
| `menu.prepareMacroUpgradeSlots` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt prepare macro upgrade slots aus (Parameter: macro). |
| `menu.prepareMissionContextData` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt prepare mission context data aus (Parameter: missionid, missionofferid, width). |
| `menu.prepareModWares` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt prepare mod wares aus. |
| `menu.prepareSections` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt prepare sections aus. |
| `menu.prepareTexts` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt prepare texts aus. |
| `menu.prevHelp` | 1 | `08/ui/addons/ego_helptext/helptext.lua` | Führt prev help aus. |
| `menu.processRepairsFor` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt process repairs for aus (Parameter: shipidstring, orderindex). |
| `menu.processSelectedPlayerShips` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt process selected player ships aus. |
| `menu.propertyColor` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt property color aus (Parameter: property). |
| `menu.recursiveSort` | 1 | `08/ui/addons/ego_detailmonitor/menu_platformundock.lua` | Führt recursive sort aus (Parameter: object). |
| `menu.refresh` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt refresh aus. |
| `menu.refreshContextFrame` | 3 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt refresh context frame aus (Parameter: setrow, setcol, noborder). |
| `menu.refreshCrewInfo` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt refresh crew info aus. |
| `menu.refreshInfo2Frame` | 2 | `08/ui/addons/ego_detailmonitor/menu_scenario_debriefing.lua` | Führt refresh info2 frame aus. |
| `menu.refreshInfoFrame` | 7 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt refresh info frame aus (Parameter: setrow, setcol, setrow2, setcol2). |
| `menu.refreshInfoFrame2` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt refresh info frame2 aus (Parameter: setrow, setcol). |
| `menu.refreshMainFrame` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Führt refresh main frame aus. |
| `menu.refreshMenu` | 4 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt refresh menu aus. |
| `menu.refreshPlan` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt refresh plan aus. |
| `menu.refreshTitleBar` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt refresh title bar aus. |
| `menu.regionSearchText` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Führt region search text aus. |
| `menu.registerDirectInput` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt register direct input aus. |
| `menu.relationColor` | 2 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt relation color aus (Parameter: faction). |
| `menu.relationSorter` | 1 | `08/ui/addons/ego_detailmonitor/menu_diplomacy.lua` | Führt relation sorter aus (Parameter: a, b). |
| `menu.relationText` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt relation text aus (Parameter: relation, width). |
| `menu.remapInput` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt remap input aus (Parameter: newinputtype, newinputcode, newinputsgn, checked). |
| `menu.remapInputInternal` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt remap input internal aus (Parameter: newinputtype, newinputcode, newinputsgn, newinputtoggle, nosave). |
| `menu.removeAllMappings` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Entfernt all mappings (Parameter: save). |
| `menu.removeExtendedOrder` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Entfernt extended order (Parameter: controllable, orderidx, instance). |
| `menu.removeFactionRelation` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Entfernt faction relation (Parameter: relations, faction, otherfaction). |
| `menu.removeFactionRelationHelper` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Entfernt faction relation helper (Parameter: faction). |
| `menu.removeFilterOption` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Entfernt filter option (Parameter: setting, id, index). |
| `menu.removeHQ` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Entfernt hq. |
| `menu.removeInput` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Entfernt input. |
| `menu.removeMouseCursorOverride` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Entfernt mouse cursor override (Parameter: priority). |
| `menu.removeOrder` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Entfernt order (Parameter: orderidx, instance). |
| `menu.removeRepairedComponent` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Entfernt repaired component (Parameter: object, component). |
| `menu.removeSelectedComponent` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Entfernt selected component (Parameter: component). |
| `menu.repairandupgrade` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt repairandupgrade aus (Parameter: shoppinglistentry, object, macro, hasupgrades, haspaid, objectprice, objectcrewprice, objectcustomname). |
| `menu.requestLanguageID` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt request language id aus (Parameter: id). |
| `menu.researchStateText` | 2 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt research state text aus (Parameter: researchmodule). |
| `menu.researchTimeText` | 2 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt research time text aus (Parameter: researchmodule, researchtime). |
| `menu.resetAndCloseMenu` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Setzt and close menu zurück. |
| `menu.resetDefaultLoadout` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Setzt default loadout zurück. |
| `menu.resetInfoSubmenu` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Setzt info submenu zurück (Parameter: i, instance). |
| `menu.resetOrderParamMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Setzt order param mode zurück. |
| `menu.resetPlotSize` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Setzt plot size zurück. |
| `menu.restoreFlowchartState` | 4 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt restore flowchart state aus (Parameter: name, flowchart). |
| `menu.restoreTableState` | 3 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Führt restore table state aus (Parameter: name, ftable). |
| `menu.returnToHub` | 1 | `08/ui/addons/ego_detailmonitor/menu_scenario_debriefing.lua` | Führt return to hub aus (Parameter: gamestartid). |
| `menu.roleSorter` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt role sorter aus (Parameter: a, b, invert). |
| `menu.round` | 1 | `08/ui/addons/ego_helptext/helptext.lua` | Führt round aus (Parameter: x, digits). |
| `menu.saveEncyclopediaValue` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Speichert encyclopedia value. |
| `menu.saveFlowchartState` | 4 | `08/ui/addons/ego_gameoptions/customgame.lua` | Speichert flowchart state (Parameter: name, flowchart). |
| `menu.saveKnownValue` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Speichert known value (Parameter: property). |
| `menu.saveMouseOverText` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Speichert mouse over text. |
| `menu.saveMultiSelect` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Speichert multi select (Parameter: property). |
| `menu.saveStoryValue` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Speichert story value (Parameter: property). |
| `menu.saveTableState` | 3 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Speichert table state (Parameter: name, ftable, row, col). |
| `menu.savegameInfoVersion` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt savegame info version aus. |
| `menu.scaleFont` | 1 | `08/ui/addons/ego_helptext/helptext.lua` | Führt scale font aus (Parameter: fontname, fontsize). |
| `menu.scaleX` | 1 | `08/ui/addons/ego_helptext/helptext.lua` | Führt scale x aus (Parameter: x). |
| `menu.scaleY` | 1 | `08/ui/addons/ego_helptext/helptext.lua` | Führt scale y aus (Parameter: y). |
| `menu.searchTextChanged` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt search text changed aus (Parameter: _, text, textchanged). |
| `menu.searchTextConfirmed` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt search text confirmed aus (Parameter: _, text, textchanged). |
| `menu.selectCV` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Wählt cv aus (Parameter: component). |
| `menu.selectEntry` | 1 | `08/ui/addons/ego_detailmonitor/menu_help.lua` | Wählt entry aus (Parameter: entry). |
| `menu.selectMapMacroSlot` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Wählt map macro slot aus. |
| `menu.selectModeInfoText` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Wählt mode info text aus (Parameter: text). |
| `menu.selectableContinue` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt selectable continue aus. |
| `menu.selectableGameMenuWidthScaleConfirm` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt selectable game menu width scale confirm aus. |
| `menu.selectableGameResetUserQuestions` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt selectable game reset user questions aus. |
| `menu.selectableGameStartmenuBackgroundConfirm` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt selectable game startmenu background confirm aus. |
| `menu.selectableGameUIScaleConfirm` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt selectable game uiscale confirm aus. |
| `menu.selectableGfxAdapter` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt selectable gfx adapter aus. |
| `menu.selectableGfxFullscreen` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt selectable gfx fullscreen aus. |
| `menu.selectableGfxGPU` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt selectable gfx gpu aus. |
| `menu.selectableGfxResolution` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt selectable gfx resolution aus. |
| `menu.selectableGfxUIGlowIntensity` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt selectable gfx uiglow intensity aus. |
| `menu.selectableGfxUpscaling` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt selectable gfx upscaling aus. |
| `menu.selectableOnlineSeason` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt selectable online season aus. |
| `menu.serverDiscoveredCallback` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt server discovered callback aus (Parameter: _, server). |
| `menu.setCategory` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Setzt category (Parameter: category). |
| `menu.setCustomShipName` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Setzt custom ship name. |
| `menu.setEncyclopediaValue` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Setzt encyclopedia value (Parameter: library, item, value). |
| `menu.setFactionRelation` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Setzt faction relation (Parameter: relations, faction, otherfaction, relation). |
| `menu.setFilterOption` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Setzt filter option (Parameter: mode, setting, id, value, index). |
| `menu.setInfoSubmenuObjectAndRefresh` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Setzt info submenu object and refresh (Parameter: component). |
| `menu.setInputFeedbackTextOption` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Setzt input feedback text option (Parameter: option, controltype, controlcode). |
| `menu.setInputFeedbackVoiceOption` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Setzt input feedback voice option (Parameter: option, controltype, controlcode). |
| `menu.setKnownValue` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Setzt known value (Parameter: property, item, value). |
| `menu.setMissingUpgrade` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Setzt missing upgrade (Parameter: ware, amount, allownewentry). |
| `menu.setMouseCursor` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Setzt mouse cursor. |
| `menu.setMouseCursorOverride` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Setzt mouse cursor override (Parameter: cursor, priority). |
| `menu.setObject` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Setzt object (Parameter: rowdata). |
| `menu.setOrderImmediate` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Setzt order immediate (Parameter: component, orderidx). |
| `menu.setOrderParamFromMode` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Setzt order param from mode (Parameter: controllable, order, param, index, value, instance). |
| `menu.setPlayerMacro` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Setzt player macro (Parameter: customgamestart, propertyid, option). |
| `menu.setPlayerPaintTheme` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Setzt player paint theme (Parameter: customgamestart, propertyid, option). |
| `menu.setPlayerSector` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Setzt player sector (Parameter: gamestartid, propertyid, sector, noreset). |
| `menu.setSectorFilter` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Setzt sector filter. |
| `menu.setSelectedMapComponents` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Setzt selected map components. |
| `menu.setStationManager` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Setzt station manager (Parameter: property, entryid, manager). |
| `menu.setStoriesLocked` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Setzt stories locked (Parameter: lookuptable, sector). |
| `menu.setTextFilter` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Setzt text filter. |
| `menu.setTradeWares` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Setzt trade wares. |
| `menu.setupCrewInfoSubmenuRows` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt setup crew info submenu rows aus (Parameter: mode, inputtable, inputobject, instance). |
| `menu.setupEmpireDescription` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt setup empire description aus (Parameter: table_bottomright). |
| `menu.setupEmpireRenderTarget` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt setup empire render target aus. |
| `menu.setupEmpireRows` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt setup empire rows aus (Parameter: mode, properties_table_center, tabOrderOffset, table_center). |
| `menu.setupFlowchartData` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt setup flowchart data aus. |
| `menu.setupGroupData` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt setup group data aus (Parameter: object, macro, groups, changeupgradeplan). |
| `menu.setupInfoSubmenuRows` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt setup info submenu rows aus (Parameter: mode, inputtable, inputobject, instance). |
| `menu.setupInventoryRenderTarget` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt setup inventory render target aus. |
| `menu.setupLoadoutInfoSubmenuRows` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt setup loadout info submenu rows aus (Parameter: mode, inputtable, inputobject, instance). |
| `menu.setupLogbookInfoSubmenuRows` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt setup logbook info submenu rows aus (Parameter: inputtable, inputobject, instance, isvalid). |
| `menu.setupMessageRenderTarget` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt setup message render target aus. |
| `menu.setupPersonnelRenderTarget` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt setup personnel render target aus. |
| `menu.setupRenderTarget` | 1 | `08/ui/addons/ego_detailmonitor/menu_encyclopedia.lua` | Führt setup render target aus (Parameter: renderobject, isicon, paintmod, iscomponent). |
| `menu.shipTextColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_platformundock.lua` | Führt ship text color aus (Parameter: ship). |
| `menu.shipValue` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt ship value aus (Parameter: current). |
| `menu.showConstructionMap` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Zeigt construction map. |
| `menu.showEntry` | 1 | `08/ui/addons/ego_detailmonitor/menu_trader_blueprintsorlicences.lua` | Zeigt entry (Parameter: entry, tag, indent). |
| `menu.showInteractMenu` | 1 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Zeigt interact menu (Parameter: param). |
| `menu.showMissionContext` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Zeigt mission context (Parameter: missionid, isoffer). |
| `menu.skillSorter` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt skill sorter aus (Parameter: a, b, invert). |
| `menu.slidercellAccount` | 2 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt slidercell account aus (Parameter: _, value). |
| `menu.slidercellAccountChanged` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt slidercell account changed aus (Parameter: station, row, value, functable). |
| `menu.slidercellBoardingAssignedMarines` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt slidercell boarding assigned marines aus (Parameter: ship, marinelevel, newvalue). |
| `menu.slidercellBuildPriceFactor` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt slidercell build price factor aus (Parameter: container64, value). |
| `menu.slidercellCrewTransfer` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt slidercell crew transfer aus (Parameter: i, j, value). |
| `menu.slidercellFaction` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt slidercell faction aus (Parameter: faction, value). |
| `menu.slidercellGlobalWarePriceFactor` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt slidercell global ware price factor aus (Parameter: row, value). |
| `menu.slidercellInventoryCraft` | 2 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt slidercell inventory craft aus (Parameter: _, value). |
| `menu.slidercellInventoryDrop` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt slidercell inventory drop aus (Parameter: ware, value). |
| `menu.slidercellMoney` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt slidercell money aus (Parameter: _, value). |
| `menu.slidercellMultiSelect` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt slidercell multi select aus (Parameter: property, entryid, row, value). |
| `menu.slidercellNumberProperty` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt slidercell number property aus (Parameter: property, row, value). |
| `menu.slidercellPlayerAlertInterval` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt slidercell player alert interval aus (Parameter: _, value). |
| `menu.slidercellPlotValue` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt slidercell plot value aus (Parameter: _, value, dimension, fullsize). |
| `menu.slidercellPositionChanged` | 1 | `08/ui/addons/ego_detailmonitor/menu_followcamera.lua` | Führt slidercell position changed aus (Parameter: name, value). |
| `menu.slidercellSelectAmount` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt slidercell select amount aus (Parameter: type, slot, macro, row, value). |
| `menu.slidercellSelectCrewAmount` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt slidercell select crew amount aus (Parameter: slot, tier, row, istier, value). |
| `menu.slidercellSelectGroupAmount` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt slidercell select group amount aus (Parameter: type, group, row, keepcontext, value). |
| `menu.slidercellSetOrderParam` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt slidercell set order param aus (Parameter: order, param, index, value, instance). |
| `menu.slidercellShipAmmo` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt slidercell ship ammo aus (Parameter: sellid, buyid, ware, ammoamount, value). |
| `menu.slidercellShipCargo` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt slidercell ship cargo aus (Parameter: sellid, buyid, ware, cargoamount, value). |
| `menu.slidercellStorageWarePriceOverride` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt slidercell storage ware price override aus (Parameter: container, ware, buysellswitch, value). |
| `menu.slidercellSupplyAmount` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt slidercell supply amount aus (Parameter: container64, macro, auto, type, idx, value). |
| `menu.slidercellSupplyAmountActivated` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt slidercell supply amount activated aus (Parameter: macro). |
| `menu.slidercellTradeConfirmed` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt slidercell trade confirmed aus (Parameter: ware). |
| `menu.slidercellWarePriceOverride` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt slidercell ware price override aus (Parameter: ware, row, value). |
| `menu.snapToClusterGrid` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Führt snap to cluster grid aus (Parameter: offset). |
| `menu.sortActiveEntries` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt sort active entries aus (Parameter: a, b). |
| `menu.sortAmmo` | 2 | `08/ui/addons/ego_detailmonitor/menu_trader_blueprintsorlicences.lua` | Führt sort ammo aus (Parameter: a, b). |
| `menu.sortByActiveAndName` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt sort by active and name aus (Parameter: a, b). |
| `menu.sortByActiveAndWareName` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt sort by active and ware name aus (Parameter: a, b). |
| `menu.sortByComponentName` | 1 | `08/ui/addons/ego_detailmonitor/menu_platformundock.lua` | Führt sort by component name aus (Parameter: a, b). |
| `menu.sortBySkillinTiers` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt sort by skillin tiers aus (Parameter: result). |
| `menu.sortClasses` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt sort classes aus (Parameter: a, b). |
| `menu.sortComponentListHelper` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt sort component list helper aus (Parameter: components, sorter). |
| `menu.sortGameStartmenuBackground` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt sort game startmenu background aus (Parameter: a, b). |
| `menu.sortLicences` | 2 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt sort licences aus (Parameter: a, b). |
| `menu.sortMappingsByRef` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt sort mappings by ref aus (Parameter: a, b). |
| `menu.sortMessages` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt sort messages aus (Parameter: a, b). |
| `menu.sortShipsByClassAndPurpose` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt sort ships by class and purpose aus (Parameter: a, b). |
| `menu.sortShipsByClassAndPurposeReverse` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt sort ships by class and purpose reverse aus (Parameter: a, b). |
| `menu.sortSlots` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt sort slots aus (Parameter: a, b). |
| `menu.sortSubTargets` | 1 | `08/ui/addons/ego_detailmonitor/menu_transporter.lua` | Führt sort sub targets aus (Parameter: a, b). |
| `menu.sortTargets` | 1 | `08/ui/addons/ego_detailmonitor/menu_transporter.lua` | Führt sort targets aus (Parameter: a, b). |
| `menu.sortTechName` | 2 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt sort tech name aus (Parameter: a, b). |
| `menu.sortWareGroupsByTier` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt sort ware groups by tier aus (Parameter: a, b). |
| `menu.sorterModules` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt sorter modules aus (Parameter: type, a, b). |
| `menu.startMapEditorWithCopy` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Startet map editor with copy. |
| `menu.startScenario` | 2 | `08/ui/addons/ego_detailmonitor/menu_scenario_debriefing.lua` | Startet scenario (Parameter: scenario). |
| `menu.stationSearchText` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Führt station search text aus. |
| `menu.storeCurrentPlots` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt store current plots aus. |
| `menu.storePlanTableState` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt store plan table state aus. |
| `menu.submenuHandler` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt submenu handler aus (Parameter: optionParameter). |
| `menu.submissionTimer` | 1 | `08/ui/addons/ego_detailmonitor/menu_missionbriefing.lua` | Führt submission timer aus (Parameter: submissionentry). |
| `menu.supplyUpdate` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Führt supply update aus (Parameter: _, container). |
| `menu.swapExtendedOrder` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt swap extended order aus (Parameter: controllable, oldorderidx, neworderidx, instance). |
| `menu.syncMapFilterWithConfig` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt sync map filter with config aus. |
| `menu.tabIconColor` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Führt tab icon color aus (Parameter: messageindex). |
| `menu.tallyTotalPrice` | 2 | `08/ui/addons/ego_detailmonitor/menu_trader_blueprintsorlicences.lua` | Führt tally total price aus. |
| `menu.target` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt target aus (Parameter: component, allowfirstperson, fallbackcomponent). |
| `menu.teleport` | 1 | `08/ui/addons/ego_detailmonitor/menu_platformundock.lua` | Führt teleport aus. |
| `menu.terraformingErrorText` | 2 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Führt terraforming error text aus (Parameter: project). |
| `menu.textButton` | 1 | `08/ui/addons/ego_detailmonitor/menu_help.lua` | Führt text button aus. |
| `menu.toggleAllNotificationSettings` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Schaltet all notification settings um (Parameter: notificationgroupdata, checked). |
| `menu.toggleChatWindow` | 1 | `08/ui/addons/ego_chatwindow/chatwindow.lua` | Schaltet chat window um (Parameter: noeditboxactivation). |
| `menu.toggleSelectedComponent` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Schaltet selected component um (Parameter: component). |
| `menu.toggleStoryHQ` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Schaltet story hq um (Parameter: storyid). |
| `menu.tradeContextCostAndStorageUpdateHelper` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt trade context cost and storage update helper aus (Parameter: storagetype, ware). |
| `menu.undoHelper` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt undo helper aus (Parameter: undo). |
| `menu.undockButtonBGColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt undock button bgcolor aus. |
| `menu.undockButtonHighlightColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt undock button highlight color aus. |
| `menu.undockButtonTextColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_docked.lua` | Führt undock button text color aus. |
| `menu.universeSector` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Führt universe sector aus (Parameter: current). |
| `menu.unmoveNewPostNPCHelper` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt unmove new post npchelper aus (Parameter: seed, origin). |
| `menu.unmovePerson` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt unmove person aus (Parameter: origin, i, j, person, k). |
| `menu.unregisterDirectInput` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt unregister direct input aus. |
| `menu.updateAccountNode` | 2 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Aktualisiert account node (Parameter: node). |
| `menu.updateBudgets` | 1 | `08/ui/addons/ego_gameoptions/customgame.lua` | Aktualisiert budgets. |
| `menu.updateBuildNode` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Aktualisiert build node (Parameter: node, buildmodule). |
| `menu.updateConstructionPlans` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Aktualisiert construction plans. |
| `menu.updateDeliveredWares` | 2 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Aktualisiert delivered wares (Parameter: project). |
| `menu.updateDroneInfo` | 2 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Aktualisiert drone info (Parameter: project). |
| `menu.updateEdgeColorRecursively` | 2 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Aktualisiert edge color recursively (Parameter: edge, color). |
| `menu.updateExpandedNode` | 3 | `08/ui/addons/ego_detailmonitor/menu_terraforming.lua` | Aktualisiert expanded node. |
| `menu.updateHolomap` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Aktualisiert holomap. |
| `menu.updateMapAndInfoFrame` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Aktualisiert map and info frame. |
| `menu.updateMissionOfferList` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Aktualisiert mission offer list (Parameter: clear). |
| `menu.updateMissions` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Aktualisiert missions. |
| `menu.updateMouseCursor` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Aktualisiert mouse cursor. |
| `menu.updateOverride` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Aktualisiert override (Parameter: container64). |
| `menu.updatePlotData` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Aktualisiert plot data (Parameter: station, donotrefresh). |
| `menu.updatePlotSize` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Aktualisiert plot size (Parameter: dimension, axis, valchange). |
| `menu.updatePlotSliders` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Aktualisiert plot sliders. |
| `menu.updatePlotWidgets` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Aktualisiert plot widgets. |
| `menu.updatePos` | 1 | `08/ui/addons/ego_detailmonitor/menu_followcamera.lua` | Aktualisiert pos. |
| `menu.updateProcessingNode` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Aktualisiert processing node (Parameter: node, processingmodules). |
| `menu.updateProductionNode` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Aktualisiert production node (Parameter: node, productionmodules). |
| `menu.updateRenderedComponents` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Aktualisiert rendered components. |
| `menu.updateResearchNode` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Aktualisiert research node (Parameter: node, researchmodule). |
| `menu.updateSelectedComponents` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Aktualisiert selected components (Parameter: modified, keepselection, changedComponent, changedrow). |
| `menu.updateSelectedRows` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Aktualisiert selected rows. |
| `menu.updateShipStatus` | 1 | `08/ui/addons/ego_detailmonitor/menu_platformundock.lua` | Aktualisiert ship status (Parameter: datatable). |
| `menu.updateShipStatusText` | 1 | `08/ui/addons/ego_detailmonitor/menu_platformundock.lua` | Aktualisiert ship status text (Parameter: datatable). |
| `menu.updateSliders` | 1 | `08/ui/addons/ego_detailmonitor/menu_followcamera.lua` | Aktualisiert sliders. |
| `menu.updateSpline` | 1 | `08/ui/addons/ego_detailmonitor/menu_mapeditor.lua` | Aktualisiert spline. |
| `menu.updateSubordinateGroupInfo` | 2 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Aktualisiert subordinate group info (Parameter: controllable). |
| `menu.updateSupplyResourceNode` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Aktualisiert supply resource node (Parameter: node, ware). |
| `menu.updateTableSelection` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Aktualisiert table selection (Parameter: lastcomponent). |
| `menu.updateTerraformingNode` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_overview.lua` | Aktualisiert terraforming node (Parameter: node, project). |
| `menu.updateTradeContextDimensions` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Aktualisiert trade context dimensions (Parameter: numwarerows, numinforows). |
| `menu.updateTradeCost` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Aktualisiert trade cost. |
| `menu.updateTradeData` | 1 | `08/ui/addons/ego_detailmonitor/menu_trader_inventory.lua` | Aktualisiert trade data (Parameter: ware, newamount). |
| `menu.upgradeMapFilterSaveVersion` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt upgrade map filter save version aus. |
| `menu.upgradeMapFilterVersion` | 1 | `08/ui/addons/ego_detailmonitor/menu_map.lua` | Führt upgrade map filter version aus. |
| `menu.upgradeQueueVersion` | 1 | `08/ui/addons/ego_helptext/helptext.lua` | Führt upgrade queue version aus. |
| `menu.upgradeSettingsVersion` | 2 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt upgrade settings version aus. |
| `menu.valueAccessibilityGlobalLightScale` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value accessibility global light scale aus. |
| `menu.valueAccessibilityReducedSpeedMode` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value accessibility reduced speed mode aus. |
| `menu.valueAccessibilityStardustIntensity` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value accessibility stardust intensity aus. |
| `menu.valueExtensionGlobalSync` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value extension global sync aus. |
| `menu.valueExtensionSettingEnabled` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value extension setting enabled aus. |
| `menu.valueExtensionSettingSync` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value extension setting sync aus. |
| `menu.valueExtensionStatus` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value extension status aus (Parameter: extension). |
| `menu.valueGameAimAssist` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value game aim assist aus. |
| `menu.valueGameAutosaveInterval` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value game autosave interval aus. |
| `menu.valueGameCockpitCamera` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value game cockpit camera aus. |
| `menu.valueGameEnemyAttack` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value game enemy attack aus. |
| `menu.valueGameEnemyNearby` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value game enemy nearby aus. |
| `menu.valueGameHUDScale` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value game hudscale aus. |
| `menu.valueGameInputFeedback` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value game input feedback aus. |
| `menu.valueGameMenuWidthScale` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value game menu width scale aus. |
| `menu.valueGameRadar` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value game radar aus. |
| `menu.valueGameRumble` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value game rumble aus. |
| `menu.valueGameStartmenuBackground` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value game startmenu background aus. |
| `menu.valueGameSubtitles` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value game subtitles aus. |
| `menu.valueGameThirdPersonFlight` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value game third person flight aus. |
| `menu.valueGameUIScale` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value game uiscale aus. |
| `menu.valueGfxAA` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx aa aus. |
| `menu.valueGfxAdapter` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx adapter aus. |
| `menu.valueGfxAdaptiveSampling` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx adaptive sampling aus. |
| `menu.valueGfxDLSS` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx dlss aus. |
| `menu.valueGfxDLSSFrameGen` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx dlssframe gen aus. |
| `menu.valueGfxDLSSMode` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx dlssmode aus. |
| `menu.valueGfxEffectDistance` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx effect distance aus. |
| `menu.valueGfxEnvMapProbes` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx env map probes aus. |
| `menu.valueGfxEnvMapProbesInsideGlassFade` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx env map probes inside glass fade aus. |
| `menu.valueGfxFOV` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx fov aus. |
| `menu.valueGfxFSR1` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx fsr1 aus. |
| `menu.valueGfxFrameRate` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx frame rate aus. |
| `menu.valueGfxFullscreen` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx fullscreen aus. |
| `menu.valueGfxGPU` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx gpu aus. |
| `menu.valueGfxGamma` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx gamma aus. |
| `menu.valueGfxGlow` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx glow aus. |
| `menu.valueGfxHMDResolution` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx hmdresolution aus. |
| `menu.valueGfxLOD` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx lod aus. |
| `menu.valueGfxLUT` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx lut aus (Parameter: accessibility). |
| `menu.valueGfxPOM` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx pom aus. |
| `menu.valueGfxPresentMode` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx present mode aus. |
| `menu.valueGfxPreset` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx preset aus. |
| `menu.valueGfxRadar` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx radar aus. |
| `menu.valueGfxResolution` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx resolution aus. |
| `menu.valueGfxSSAO` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx ssao aus. |
| `menu.valueGfxSSR` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx ssr aus. |
| `menu.valueGfxShaderQuality` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx shader quality aus. |
| `menu.valueGfxShadows` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx shadows aus. |
| `menu.valueGfxTexture` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx texture aus. |
| `menu.valueGfxUIGlow` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx uiglow aus. |
| `menu.valueGfxUIGlowIntensity` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx uiglow intensity aus. |
| `menu.valueGfxVolumetric` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value gfx volumetric aus. |
| `menu.valueInputGamepadMode` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value input gamepad mode aus. |
| `menu.valueInputInvert` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value input invert aus (Parameter: rangeid). |
| `menu.valueInputJoystickDeadzone` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value input joystick deadzone aus. |
| `menu.valueInputMouseSteeringInvert` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value input mouse steering invert aus (Parameter: configname). |
| `menu.valueInputOpenTrackStatus` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value input open track status aus. |
| `menu.valueInputOpenTrackSupport` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value input open track support aus. |
| `menu.valueInputSensitivity` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value input sensitivity aus (Parameter: rangeid). |
| `menu.valueInputTrackerAngleFactor` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value input tracker angle factor aus. |
| `menu.valueInputTrackerDeadzoneAngle` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value input tracker deadzone angle aus. |
| `menu.valueInputTrackerDeadzonePosition` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value input tracker deadzone position aus. |
| `menu.valueInputTrackerGazeAngleFactor` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value input tracker gaze angle factor aus. |
| `menu.valueInputTrackerGazeDeadzone` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value input tracker gaze deadzone aus. |
| `menu.valueInputTrackerGazeFilterStrength` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value input tracker gaze filter strength aus. |
| `menu.valueInputTrackerHeadFilterStrength` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value input tracker head filter strength aus. |
| `menu.valueInputTrackerMode` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value input tracker mode aus. |
| `menu.valueInputTrackerPositionFactor` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value input tracker position factor aus. |
| `menu.valueInputVivePointingDevice` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value input vive pointing device aus. |
| `menu.valueOnlineAllowInvites` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value online allow invites aus. |
| `menu.valueOnlineAllowPrivateMessages` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value online allow private messages aus. |
| `menu.valueOnlineOperationUpdates` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value online operation updates aus. |
| `menu.valueOnlinePreferredLanguage` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value online preferred language aus. |
| `menu.valueOnlinePromotion` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value online promotion aus. |
| `menu.valueOnlineSeasonSummary` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value online season summary aus. |
| `menu.valueOnlineSeasonUpdates` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value online season updates aus. |
| `menu.valueSfxDevice` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value sfx device aus. |
| `menu.valueSfxSetting` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt value sfx setting aus (Parameter: sfxtype). |
| `menu.ventureModuleUnavailableMouseOverText` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt venture module unavailable mouse over text aus. |
| `menu.viewCreated` | 27 | `08/ui/addons/ego_interactmenu/menu_interactmenu.lua` | Führt view created aus (Parameter: layer, ...). |
| `menu.wareNameSorter` | 1 | `08/ui/addons/ego_detailmonitor/menu_station_configuration.lua` | Führt ware name sorter aus (Parameter: a, b). |
| `menu.warningColor` | 1 | `08/ui/addons/ego_detailmonitor/menu_ship_configuration.lua` | Führt warning color aus (Parameter: normalcolor). |
| `menu.warningColorBlind` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt warning color blind aus. |
| `menu.warningDisplay` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt warning display aus. |
| `menu.warningExtensionSettings` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt warning extension settings aus. |
| `menu.warningExtensions` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt warning extensions aus. |
| `menu.warningGfx` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt warning gfx aus. |
| `menu.warningIconColorBlind` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt warning icon color blind aus. |
| `menu.warningIconDisplay` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt warning icon display aus. |
| `menu.warningIconExtension` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt warning icon extension aus. |
| `menu.warningIconGfx` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt warning icon gfx aus. |
| `menu.warningIconInput` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt warning icon input aus. |
| `menu.warningIconLanguage` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt warning icon language aus. |
| `menu.warningIconOnline` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt warning icon online aus. |
| `menu.warningInput` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt warning input aus. |
| `menu.warningOnline` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt warning online aus. |
| `menu.warningSettings` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt warning settings aus. |
| `menu.workplaceSorter` | 1 | `08/ui/addons/ego_detailmonitor/menu_playerinfo.lua` | Führt workplace sorter aus (Parameter: a, b, invert). |
| `normalizeAngle` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt normalize angle aus (Parameter: angle). |
| `onActiveWeaponGroupChanged` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on active weapon group changed aus (Parameter: _, primaryGroup, group). |
| `onBoostInput` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on boost input aus (Parameter: _, success). |
| `onButtonSelectDown` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on button select down aus. |
| `onButtonSelectLeft` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on button select left aus. |
| `onButtonSelectRight` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on button select right aus. |
| `onButtonSelectUp` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on button select up aus. |
| `onChangedEnvironmentObject` | 1 | `08/ui/core/lua/monitors.lua` | Führt on changed environment object aus. |
| `onChatRead` | 1 | `08/ui/core/lua/monitors.lua` | Führt on chat read aus. |
| `onChatReceived` | 1 | `08/ui/core/lua/monitors.lua` | Führt on chat received aus. |
| `onClear` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on clear aus. |
| `onConversationFinished` | 2 | `08/ui/core/lua/firstperson_crosshair.lua` | Führt on conversation finished aus. |
| `onConversationStarted` | 1 | `08/ui/core/lua/firstperson_crosshair.lua` | Führt on conversation started aus. |
| `onCopy` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on copy aus. |
| `onCutsceneReady` | 1 | `08/ui/core/lua/monitors.lua` | Führt on cutscene ready aus (Parameter: _, cutsceneID). |
| `onCutsceneStopped` | 1 | `08/ui/core/lua/monitors.lua` | Führt on cutscene stopped aus (Parameter: _, cutsceneID). |
| `onDebugLog` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on debug log aus (Parameter: _, errorMessageID). |
| `onDebugLogViewCreated` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on debug log view created aus (Parameter: frames). |
| `onDialog1MouseClick` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog1 mouse click aus (Parameter: _, delayed). |
| `onDialog1MouseOver` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog1 mouse over aus. |
| `onDialog1POVOver` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog1 povover aus. |
| `onDialog2MouseClick` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog2 mouse click aus (Parameter: _, delayed). |
| `onDialog2MouseOver` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog2 mouse over aus. |
| `onDialog2POVOver` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog2 povover aus. |
| `onDialog3MouseClick` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog3 mouse click aus (Parameter: _, delayed). |
| `onDialog3MouseOver` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog3 mouse over aus. |
| `onDialog3POVOver` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog3 povover aus. |
| `onDialog4MouseClick` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog4 mouse click aus (Parameter: _, delayed). |
| `onDialog4MouseOver` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog4 mouse over aus. |
| `onDialog4POVOver` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog4 povover aus. |
| `onDialog5MouseClick` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog5 mouse click aus (Parameter: _, delayed). |
| `onDialog5MouseOver` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog5 mouse over aus. |
| `onDialog5POVOver` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog5 povover aus. |
| `onDialog6MouseClick` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog6 mouse click aus (Parameter: _, delayed). |
| `onDialog6MouseOver` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog6 mouse over aus. |
| `onDialog6POVOver` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on dialog6 povover aus. |
| `onDroneClick` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on drone click aus (Parameter: i). |
| `onDroneModeClick` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on drone mode click aus (Parameter: i). |
| `onDroneModeOut` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on drone mode out aus (Parameter: i). |
| `onDroneModeOver` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on drone mode over aus (Parameter: i). |
| `onDroneOut` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on drone out aus (Parameter: i). |
| `onDroneOver` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on drone over aus (Parameter: i). |
| `onEnableMouseOverText` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on enable mouse over text aus (Parameter: _, enable). |
| `onEnableRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on enable radar aus (Parameter: _, enable). |
| `onEnableSeparateRadar` | 1 | `08/ui/core/lua/monitors.lua` | Führt on enable separate radar aus (Parameter: _, enable). |
| `onEnterDialogMenu` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on enter dialog menu aus. |
| `onExternalTargetView` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on external target view aus (Parameter: active). |
| `onExternalTargetViewActive` | 1 | `08/ui/core/lua/monitors.lua` | Führt on external target view active aus. |
| `onExternalTargetViewInactive` | 1 | `08/ui/core/lua/monitors.lua` | Führt on external target view inactive aus. |
| `onFirstButton` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on first button aus. |
| `onFlightControlStarted` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on flight control started aus. |
| `onFlightControlStopped` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on flight control stopped aus. |
| `onFrameCounterViewCreated` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on frame counter view created aus (Parameter: frames). |
| `onFrameHandleViewCreated` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt on frame handle view created aus (Parameter: framehandle, frames). |
| `onGamePaused` | 1 | `08/ui/core/lua/monitors.lua` | Führt on game paused aus. |
| `onGamePlanChange` | 6 | `08/ui/core/lua/crosshair handling.lua` | Führt on game plan change aus (Parameter: _, gameplan). |
| `onGameUnpaused` | 1 | `08/ui/core/lua/monitors.lua` | Führt on game unpaused aus. |
| `onHideCompass` | 1 | `08/ui/core/lua/compass.lua` | Führt on hide compass aus (Parameter: _, source). |
| `onHideDebugLine` | 1 | `08/ui/core/lua/debugline.lua` | Führt on hide debug line aus. |
| `onHideDebugLog` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on hide debug log aus. |
| `onHideFPS` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on hide fps aus (Parameter: _, hide). |
| `onHideFPSCounter` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on hide fpscounter aus. |
| `onHideInfoBar` | 4 | `08/ui/core/lua/infobar4.lua` | Führt on hide info bar aus. |
| `onHidePromo` | 1 | `08/ui/core/lua/promo.lua` | Führt on hide promo aus. |
| `onHotkey` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on hotkey aus (Parameter: action). |
| `onIncomingMail` | 1 | `08/ui/core/lua/monitors.lua` | Führt on incoming mail aus. |
| `onInputModeChanged` | 2 | `08/ui/core/lua/crosshair handling.lua` | Führt on input mode changed aus (Parameter: _, mode). |
| `onInteractionHidden` | 2 | `08/ui/core/lua/crosshair handling.lua` | Führt on interaction hidden aus (Parameter: _, interactionID). |
| `onInteractionShown` | 2 | `08/ui/core/lua/crosshair handling.lua` | Führt on interaction shown aus (Parameter: _, interactionID, interactionText). |
| `onInventoryWaresAdded` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on inventory wares added aus. |
| `onLastButton` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on last button aus. |
| `onLeaveDialogMenu` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on leave dialog menu aus. |
| `onLoadingDone` | 1 | `08/ui/core/lua/loading.lua` | Führt on loading done aus. |
| `onMailRead` | 1 | `08/ui/core/lua/monitors.lua` | Führt on mail read aus. |
| `onMissileIncoming` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on missile incoming aus. |
| `onMissileLockInitiated` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on missile lock initiated aus. |
| `onMissileLockLost` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on missile lock lost aus. |
| `onMissionInfoUpdate` | 1 | `08/ui/core/lua/monitors.lua` | Führt on mission info update aus. |
| `onMissionObjectiveBarUpdate` | 1 | `08/ui/core/lua/monitors.lua` | Führt on mission objective bar update aus. |
| `onMissionPosIDConnected` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on mission pos idconnected aus (Parameter: _, posID). |
| `onMissionPosIDDisconnected` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on mission pos iddisconnected aus (Parameter: _, posID). |
| `onMouseClick` | 1 | `08/ui/core/lua/promo.lua` | Führt on mouse click aus. |
| `onMouseClickMessageTickerChatNotification` | 1 | `08/ui/core/lua/monitors.lua` | Führt on mouse click message ticker chat notification aus (Parameter: _, delayed). |
| `onMouseClickMessageTickerFooter` | 1 | `08/ui/core/lua/monitors.lua` | Führt on mouse click message ticker footer aus (Parameter: _, delayed). |
| `onMouseClickMessageTickerNotification` | 1 | `08/ui/core/lua/monitors.lua` | Führt on mouse click message ticker notification aus (Parameter: _, delayed). |
| `onMouseClickMessageTickerRow1` | 1 | `08/ui/core/lua/monitors.lua` | Führt on mouse click message ticker row1 aus (Parameter: _, delayed). |
| `onMouseClickTargetMonitor` | 1 | `08/ui/core/lua/monitors.lua` | Führt on mouse click target monitor aus (Parameter: _, delayed). |
| `onMouseDown` | 1 | `08/ui/core/lua/compass.lua` | Führt on mouse down aus (Parameter: i). |
| `onMouseOut` | 2 | `08/ui/core/lua/compass.lua` | Führt on mouse out aus (Parameter: i). |
| `onMouseOver` | 1 | `08/ui/core/lua/promo.lua` | Führt on mouse over aus. |
| `onMouseUp` | 1 | `08/ui/core/lua/compass.lua` | Führt on mouse up aus (Parameter: i). |
| `onNextButton` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on next button aus. |
| `onNotificationFreed` | 1 | `08/ui/core/lua/monitors.lua` | Führt on notification freed aus (Parameter: _, notificationID). |
| `onNumMissionsChanged` | 1 | `08/ui/core/lua/monitors.lua` | Führt on num missions changed aus (Parameter: _, numMissions). |
| `onPlayerActivityChanged` | 2 | `08/ui/core/lua/crosshair handling.lua` | Führt on player activity changed aus. |
| `onPrevButton` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on prev button aus. |
| `onPriorityMissiontargetChanged` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on priority missiontarget changed aus (Parameter: _, posID). |
| `onReducedSpeedModeActivated` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on reduced speed mode activated aus. |
| `onReducedSpeedModeDeactivated` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on reduced speed mode deactivated aus. |
| `onReenable` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on reenable aus. |
| `onRefreshTargetMonitor` | 1 | `08/ui/core/lua/monitors.lua` | Führt on refresh target monitor aus (Parameter: _, componentID, connectionname). |
| `onResetHUDColors` | 2 | `08/ui/core/lua/crosshair handling.lua` | Führt on reset hudcolors aus. |
| `onScanAborted` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on scan aborted aus. |
| `onScanFinished` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on scan finished aus. |
| `onScanStarted` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on scan started aus. |
| `onSetaActivated` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on seta activated aus. |
| `onSetaDeactivated` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on seta deactivated aus. |
| `onShootInput` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on shoot input aus. |
| `onShowCompass` | 1 | `08/ui/core/lua/compass.lua` | Führt on show compass aus (Parameter: _, source). |
| `onShowDebugLine` | 1 | `08/ui/core/lua/debugline.lua` | Führt on show debug line aus (Parameter: _, text, timeout). |
| `onShowGameOver` | 1 | `08/ui/core/lua/gameover.lua` | Führt on show game over aus (Parameter: _, duration). |
| `onShowInfoBar` | 4 | `08/ui/core/lua/infobar4.lua` | Führt on show info bar aus (Parameter: _, type). |
| `onShowNotification` | 1 | `08/ui/core/lua/monitors.lua` | Führt on show notification aus (Parameter: _, notificationID). |
| `onShowPromo` | 1 | `08/ui/core/lua/promo.lua` | Führt on show promo aus. |
| `onSkipScreenshot` | 1 | `08/ui/core/lua/loading.lua` | Führt on skip screenshot aus. |
| `onSofttargetChanged` | 3 | `08/ui/core/lua/crosshair handling.lua` | Führt on softtarget changed aus (Parameter: _, newsofttargetmessageid, posID). |
| `onStartDialog` | 2 | `08/ui/core/lua/dialogmenu.lua` | Führt on start dialog aus (Parameter: _, time). |
| `onStopDialog` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt on stop dialog aus (Parameter: _, time). |
| `onTeleportSucceeded` | 2 | `08/ui/core/lua/crosshair handling.lua` | Führt on teleport succeeded aus. |
| `onTickerOnlyMode` | 1 | `08/ui/core/lua/monitors.lua` | Führt on ticker only mode aus (Parameter: _, enabled, showpermanently). |
| `onToggleAssert` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on toggle assert aus (Parameter: button). |
| `onToggleAssertPopUp` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on toggle assert pop up aus (Parameter: button). |
| `onToggleErrorPopUp` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on toggle error pop up aus (Parameter: button). |
| `onToggleOptionalAssert` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on toggle optional assert aus (Parameter: button). |
| `onToggleOptionalAssertPopUp` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on toggle optional assert pop up aus (Parameter: button). |
| `onToggleRadarMode` | 1 | `08/ui/core/lua/monitors.lua` | Führt on toggle radar mode aus. |
| `onToggleShowFPSButton` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt on toggle show fpsbutton aus (Parameter: button). |
| `onTurretClick` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on turret click aus (Parameter: i). |
| `onTurretModeClick` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on turret mode click aus (Parameter: i). |
| `onTurretModeOut` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on turret mode out aus (Parameter: i). |
| `onTurretModeOver` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on turret mode over aus (Parameter: i). |
| `onTurretOut` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on turret out aus (Parameter: i). |
| `onTurretOver` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on turret over aus (Parameter: i). |
| `onUnlock` | 4 | `08/ui/core/lua/crosshair handling.lua` | Führt on unlock aus. |
| `onUpdate` | 4 | `08/ui/addons/ego_viewhelper/viewhelper.lua` | Führt on update aus. |
| `onUpdateColorMap` | 1 | `08/ui/core/lua/monitors.lua` | Führt on update color map aus. |
| `onUpdateHUDColors` | 2 | `08/ui/core/lua/crosshair handling.lua` | Führt on update hudcolors aus (Parameter: _, colorstring). |
| `onVRPointerChanged` | 1 | `08/ui/core/lua/vr_pointer.lua` | Führt on vrpointer changed aus (Parameter: _, enabled). |
| `onVoiceOutput` | 1 | `08/ui/core/lua/subchannelbar.lua` | Führt on voice output aus (Parameter: _, text). |
| `onWeaponGroupChanged` | 1 | `08/ui/core/lua/crosshair handling.lua` | Führt on weapon group changed aus. |
| `parse_fpimm8` | 1 | `08/ui/core/lua/jit/dis_arm64.lua` | Führt parse fpimm8 aus. |
| `parse_immpc` | 1 | `08/ui/core/lua/jit/dis_arm64.lua` | Führt parse immpc aus. |
| `performSelectSofttargetOnClick` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt perform select softtarget on click aus (Parameter: element, delayed, instantinteract, interactwithselectedtarget). |
| `precacheScreenshots` | 1 | `08/ui/core/lua/extro.lua` | Führt precache screenshots aus. |
| `prefer_bfx` | 1 | `08/ui/core/lua/jit/dis_arm64.lua` | Führt prefer bfx aus. |
| `prepareLiveUpdateText` | 1 | `08/ui/core/lua/monitors.lua` | Führt prepare live update text aus (Parameter: info, element, component, connection). |
| `printsnap` | 1 | `08/ui/core/lua/jit/dump.lua` | Führt printsnap aus. |
| `processConnectionList` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt process connection list aus. |
| `processEnterInteractMenuEvent` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt process enter interact menu event aus. |
| `processInteractionDescriptor` | 1 | `08/ui/core/lua/monitors.lua` | Führt process interaction descriptor aus (Parameter: details, isNotification). |
| `processLiveUpdateValues` | 1 | `08/ui/core/lua/monitors.lua` | Führt process live update values aus. |
| `processMessageTickerNotifications` | 1 | `08/ui/core/lua/monitors.lua` | Führt process message ticker notifications aus. |
| `processOverlay` | 1 | `08/ui/core/lua/monitors.lua` | Führt process overlay aus (Parameter: details, isNotification). |
| `processSofttargetChange` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt process softtarget change aus. |
| `prof_annotate` | 1 | `08/ui/core/lua/jit/p.lua` | Führt prof annotate aus. |
| `prof_cb` | 1 | `08/ui/core/lua/jit/p.lua` | Führt prof cb aus. |
| `prof_finish` | 1 | `08/ui/core/lua/jit/p.lua` | Führt prof finish aus. |
| `prof_start` | 1 | `08/ui/core/lua/jit/p.lua` | Führt prof start aus. |
| `prof_top` | 1 | `08/ui/core/lua/jit/p.lua` | Führt prof top aus. |
| `prototype.confidence.calculate` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt calculate aus (Parameter: targetElement). |
| `prototype.confidence.calculateAngle` | 1 | `08/ui/core/lua/targetsystem.lua` | Berechnet angle (Parameter: targetElement). |
| `prototype.confidence.calculateCurrentTarget` | 1 | `08/ui/core/lua/targetsystem.lua` | Berechnet current target (Parameter: targetElement). |
| `prototype.confidence.calculateDistance` | 1 | `08/ui/core/lua/targetsystem.lua` | Berechnet distance (Parameter: targetElement). |
| `putop` | 5 | `08/ui/core/lua/jit/dis_mips.lua` | Führt putop aus. |
| `putpat` | 1 | `08/ui/core/lua/jit/dis_x86.lua` | Führt putpat aus. |
| `queueNotification` | 1 | `08/ui/core/lua/monitors.lua` | Führt queue notification aus (Parameter: notificationID, priority). |
| `readfile` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt readfile aus. |
| `registerMouseButton` | 1 | `08/ui/core/lua/compass.lua` | Führt register mouse button aus (Parameter: element, i). |
| `regname` | 5 | `08/ui/core/lua/jit/dis_mips.lua` | Führt regname aus. |
| `regname64` | 1 | `08/ui/core/lua/jit/dis_x86.lua` | Führt regname64 aus. |
| `removeAllPointerOverrides` | 1 | `08/ui/core/lua/targetsystem.lua` | Entfernt all pointer overrides. |
| `removeAutoLock` | 1 | `08/ui/core/lua/dialogmenu.lua` | Entfernt auto lock. |
| `removeFill` | 1 | `08/ui/core/lua/targetsystem.lua` | Entfernt fill (Parameter: targetElement). |
| `removeOldestMessage` | 1 | `08/ui/core/lua/monitors.lua` | Entfernt oldest message. |
| `removeOutline` | 1 | `08/ui/core/lua/targetsystem.lua` | Entfernt outline (Parameter: targetElement). |
| `removeSofttargetLockRequest` | 1 | `08/ui/core/lua/targetsystem.lua` | Entfernt softtarget lock request. |
| `removeStateRequest` | 1 | `08/ui/core/lua/monitors.lua` | Entfernt state request (Parameter: state, force). |
| `requestSofttargetLock` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt request softtarget lock aus. |
| `requestState` | 1 | `08/ui/core/lua/monitors.lua` | Führt request state aus (Parameter: state, force). |
| `resetElement` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt element zurück (Parameter: targetElement). |
| `resetScheduledShowDialogMenu` | 1 | `08/ui/core/lua/dialogmenu.lua` | Setzt scheduled show dialog menu zurück. |
| `resetTargetSystem` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt target system zurück. |
| `resolutionsort` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt resolutionsort aus (Parameter: a, b). |
| `resolveInput` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt resolve input aus. |
| `resolveOrFixFunctionInput` | 1 | `08/ui/addons/ego_gameoptions/gameoptions.lua` | Führt resolve or fix function input aus. |
| `ridsp_name` | 1 | `08/ui/core/lua/jit/dump.lua` | Führt ridsp name aus. |
| `savefile` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt savefile aus. |
| `scaleFont` | 1 | `08/ui/core/lua/monitors.lua` | Führt scale font aus (Parameter: size). |
| `scheduleAutoLock` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt schedule auto lock aus (Parameter: time). |
| `scheduleShowDialogMenu` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt schedule show dialog menu aus. |
| `selectDialogButton` | 1 | `08/ui/core/lua/dialogmenu.lua` | Wählt dialog button aus (Parameter: button). |
| `self:faceCamera` | 1 | `08/ui/core/lua/billboard.lua` | Führt self:face camera aus. |
| `self:faceCameraGlobalY` | 1 | `08/ui/core/lua/billboard.lua` | Führt self:face camera global y aus. |
| `self:getAttributeVector` | 1 | `08/ui/core/lua/billboard.lua` | Führt self:get attribute vector aus (Parameter: inElement, inAttribute, inVector). |
| `self:matchRotation` | 1 | `08/ui/core/lua/billboard.lua` | Führt self:match rotation aus. |
| `self:matchRotationGlobalY` | 1 | `08/ui/core/lua/billboard.lua` | Führt self:match rotation global y aus. |
| `self:onActivate` | 4 | `08/ui/core/lua/counteract rotation.lua` | Führt self:on activate aus. |
| `self:onAttributesChanged` | 1 | `08/ui/core/lua/write text.lua` | Führt self:on attributes changed aus. |
| `self:onDeactivate` | 3 | `08/ui/core/lua/counteract rotation.lua` | Führt self:on deactivate aus. |
| `self:onInitialize` | 24 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt self:on initialize aus. |
| `self:onRotationChanged` | 1 | `08/ui/core/lua/counteract rotation.lua` | Führt self:on rotation changed aus. |
| `self:onSourceAttributeChanged` | 1 | `08/ui/core/lua/propagate attribute.lua` | Führt self:on source attribute changed aus. |
| `self:onUpdate` | 19 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt self:on update aus. |
| `self:setAttributeVector` | 1 | `08/ui/core/lua/billboard.lua` | Führt self:set attribute vector aus (Parameter: inElement, inAttribute, inVector). |
| `setAutoCrosshairTargetSelection` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt auto crosshair target selection (Parameter: enable). |
| `setBarState` | 1 | `08/ui/core/lua/crosshair handling.lua` | Setzt bar state (Parameter: barEntry, mode, isActive, reloadPercent, heatState, heatPercent, nextShotHeatPercent, isAutoReloading). |
| `setBottomText` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt bottom text (Parameter: targetElement, text). |
| `setCellOpacities` | 1 | `08/ui/core/lua/overlay.lua` | Setzt cell opacities. |
| `setCellOpacity` | 1 | `08/ui/core/lua/overlay.lua` | Setzt cell opacity (Parameter: cell, celldata). |
| `setCentralElementsPosition` | 1 | `08/ui/core/lua/crosshair handling.lua` | Setzt central elements position (Parameter: external). |
| `setCheckedText` | 1 | `08/ui/core/lua/monitors.lua` | Setzt checked text (Parameter: element, text). |
| `setColorHelper` | 7 | `08/ui/core/lua/crosshair handling.lua` | Setzt color helper (Parameter: element, parent, color). |
| `setColoredText` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt colored text (Parameter: textComponent, textElement, curText, newText, color). |
| `setDecoColors` | 2 | `08/ui/core/lua/crosshair handling.lua` | Setzt deco colors (Parameter: activitycolor). |
| `setDecoColorsWithIntensity` | 2 | `08/ui/core/lua/crosshair handling.lua` | Setzt deco colors with intensity (Parameter: intensity). |
| `setDialogButtonColor` | 1 | `08/ui/core/lua/dialogmenu.lua` | Setzt dialog button color (Parameter: buttonTableEntry, selectable, immediate, selected). |
| `setDisplayMode` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt display mode (Parameter: targetElement, mode, onScreen). |
| `setElementColorAlpha` | 1 | `08/ui/core/lua/compass.lua` | Setzt element color alpha (Parameter: anarkMaterial, color). |
| `setElementTextColor` | 2 | `08/ui/core/lua/compass.lua` | Setzt element text color (Parameter: anarkTextElement, color). |
| `setExternalFirstPersonMode` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt external first person mode. |
| `setFirstPersonAutoTargeting` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt first person auto targeting (Parameter: enable). |
| `setFirstPersonMode` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt first person mode. |
| `setGamepadMode` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt gamepad mode (Parameter: autotargetingModeActive). |
| `setHintText` | 1 | `08/ui/core/lua/loading.lua` | Setzt hint text (Parameter: hint). |
| `setIconPos` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt icon pos (Parameter: element, x, y). |
| `setJoystickMode` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt joystick mode (Parameter: autotargetingModeActive). |
| `setKnown` | 1 | `08/ui/addons/ego_targetmonitor/targetmonitor.lua` | Setzt known. |
| `setMissileLockColor` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt missile lock color (Parameter: missileLockEntry, state, relation). |
| `setMissileLockState` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt missile lock state (Parameter: missileLockEntry, state, relation). |
| `setMouseMode` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt mouse mode. |
| `setMouseOverPosition` | 1 | `08/ui/core/lua/dialogmenu.lua` | Setzt mouse over position. |
| `setMouseOverTextEnabled` | 1 | `08/ui/core/lua/dialogmenu.lua` | Setzt mouse over text enabled (Parameter: enable). |
| `setMultilineLeftRightText` | 1 | `08/ui/core/lua/monitors.lua` | Setzt multiline left right text (Parameter: lefttext, righttext, width, indentation). |
| `setObstructionBasedColor` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt obstruction based color (Parameter: targetElement, colorMode, t). |
| `setPercentage` | 1 | `08/ui/core/lua/loading.lua` | Setzt percentage (Parameter: percentage). |
| `setPointerOverride` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt pointer override (Parameter: targetElement, pointerID). |
| `setPosition` | 3 | `08/ui/core/lua/infobar3.lua` | Setzt position (Parameter: external). |
| `setProgressText` | 1 | `08/ui/core/lua/loading.lua` | Setzt progress text (Parameter: text). |
| `setShipMode` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt ship mode. |
| `setSideText` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt side text (Parameter: targetElement, text). |
| `setSideText2` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt side text2 (Parameter: targetElement, text). |
| `setSpaceMode` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt space mode. |
| `setTableColumnWidthData` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Setzt table column width data (Parameter: ftable, col, width, percent, min, weight, scaling). |
| `setTargetElementColor` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt target element color (Parameter: targetElement, targetElementColor, iconColor, textColor, outlineColor). |
| `setTextColor` | 6 | `08/ui/core/lua/crosshair handling.lua` | Setzt text color (Parameter: textelement, color). |
| `setTextElement` | 1 | `08/ui/core/lua/monitors.lua` | Setzt text element (Parameter: element, info, component, connection, setliveupdate). |
| `setTextLine` | 1 | `08/ui/core/lua/monitors.lua` | Setzt text line (Parameter: lefttext, righttext, component, connection). |
| `setTextWithLineBreaks` | 1 | `08/ui/core/lua/monitors.lua` | Setzt text with line breaks (Parameter: lines, maxlines, width, font, fontsize, indentation). |
| `setTouchControllerMode` | 1 | `08/ui/core/lua/targetsystem.lua` | Setzt touch controller mode. |
| `setTurretColor` | 1 | `08/ui/core/lua/crosshair handling.lua` | Setzt turret color (Parameter: turretIconEntry, isActive, damageState). |
| `setTurretMode` | 1 | `08/ui/core/lua/crosshair handling.lua` | Setzt turret mode (Parameter: turretModeEntry, mode). |
| `setWeaponColor` | 1 | `08/ui/core/lua/crosshair handling.lua` | Setzt weapon color (Parameter: weaponIconEntry, isActive, damageState, isdisabledbystance). |
| `setupDAGLayoutHelper:assignPositions` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt setup daglayout helper:assign positions aus. |
| `setupDAGLayoutHelper:attemptBuildTiers` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt setup daglayout helper:attempt build tiers aus (Parameter: remainingnodes). |
| `setupDAGLayoutHelper:buildJunctions` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt setup daglayout helper:build junctions aus. |
| `setupDAGLayoutHelper:buildTiers` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt setup daglayout helper:build tiers aus. |
| `setupDAGLayoutHelper:getBestRowAssignment` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt setup daglayout helper:get best row assignment aus (Parameter: node, connections, minrow, maxrow). |
| `setupDAGLayoutHelper:getNextTier` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt setup daglayout helper:get next tier aus (Parameter: remainingnodes). |
| `setupDAGLayoutHelper:getTierNodeIndexMedian` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt setup daglayout helper:get tier node index median aus (Parameter: nodes, tieridx). |
| `setupDAGLayoutHelper:improveRowAssignments` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt setup daglayout helper:improve row assignments aus (Parameter: tieridx, topnodeidx, toprow, bottomnodeidx, bottomrow, numusedrows). |
| `setupDAGLayoutHelper:init` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt setup daglayout helper:init aus (Parameter: nodes). |
| `setupDAGLayoutHelper:insertEmptyRowsAboveVirtualNodes` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt setup daglayout helper:insert empty rows above virtual nodes aus (Parameter: realnode, righttieridx, numemptyrows). |
| `setupDAGLayoutHelper:insertEmptyTierRows` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt setup daglayout helper:insert empty tier rows aus (Parameter: abovenode, numemptyrows). |
| `setupDAGLayoutHelper:insertVirtualNode` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt setup daglayout helper:insert virtual node aus (Parameter: tieridx, predecessor, successor). |
| `setupDAGLayoutHelper:process` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt setup daglayout helper:process aus (Parameter: nodes). |
| `setupDAGLayoutHelper:reduceEdgeCrossings` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt setup daglayout helper:reduce edge crossings aus. |
| `setupDAGLayoutHelper:removeCyclicEdge` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt setup daglayout helper:remove cyclic edge aus (Parameter: remainingnodes). |
| `shouldDisplayNotorietyBar` | 1 | `08/ui/core/lua/monitors.lua` | Führt should display notoriety bar aus (Parameter: details). |
| `showBar` | 1 | `08/ui/core/lua/subchannelbar.lua` | Zeigt bar. |
| `showCell` | 1 | `08/ui/core/lua/overlay.lua` | Zeigt cell (Parameter: idx, x, y, width, height, celldata). |
| `showCompass` | 1 | `08/ui/core/lua/compass.lua` | Zeigt compass. |
| `showDebugLine` | 1 | `08/ui/core/lua/debugline.lua` | Zeigt debug line. |
| `showDebugLog` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Zeigt debug log. |
| `showDebugOutline` | 1 | `08/ui/core/lua/targetsystem.lua` | Zeigt debug outline (Parameter: targetElement). |
| `showDialogMenu` | 1 | `08/ui/core/lua/dialogmenu.lua` | Zeigt dialog menu. |
| `showEnvironmentInfo` | 1 | `08/ui/core/lua/monitors.lua` | Zeigt environment info (Parameter: targetid). |
| `showFPSCounter` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Zeigt fpscounter. |
| `showFill` | 1 | `08/ui/core/lua/targetsystem.lua` | Zeigt fill (Parameter: targetElement, color, animated). |
| `showGameOver` | 1 | `08/ui/core/lua/gameover.lua` | Zeigt game over (Parameter: duration). |
| `showMouseOverText` | 1 | `08/ui/core/lua/dialogmenu.lua` | Zeigt mouse over text (Parameter: button). |
| `showNotification` | 1 | `08/ui/core/lua/monitors.lua` | Zeigt notification (Parameter: notificationID). |
| `showNotorietyBar` | 1 | `08/ui/core/lua/monitors.lua` | Zeigt notoriety bar (Parameter: details). |
| `showOutline` | 1 | `08/ui/core/lua/targetsystem.lua` | Zeigt outline (Parameter: targetElement, color). |
| `showOverlay` | 1 | `08/ui/core/lua/overlay.lua` | Zeigt overlay. |
| `showPromo` | 1 | `08/ui/core/lua/promo.lua` | Zeigt promo. |
| `showSkipNote` | 1 | `08/ui/core/lua/subchannelbar.lua` | Zeigt skip note. |
| `showSofttarget` | 1 | `08/ui/core/lua/monitors.lua` | Zeigt softtarget (Parameter: softtargetid, softtargetconnectionname). |
| `sortDebugLog` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt sort debug log aus (Parameter: startIndex). |
| `start` | 1 | `08/ui/core/lua/jit/p.lua` | Führt start aus. |
| `startScan` | 1 | `08/ui/core/lua/crosshair handling.lua` | Startet scan. |
| `startSofttargetInteraction` | 1 | `08/ui/core/lua/targetsystem.lua` | Startet softtarget interaction. |
| `switchButton` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt switch button aus (Parameter: direction). |
| `switchScreenshot` | 2 | `08/ui/core/lua/extro.lua` | Führt switch screenshot aus (Parameter: newScreen). |
| `switchTargetMonitorNotification` | 1 | `08/ui/core/lua/monitors.lua` | Führt switch target monitor notification aus. |
| `test1` | 1 | `08/ui/core/lua/unittests.lua` | Führt test1 aus. |
| `test2` | 1 | `08/ui/core/lua/unittests.lua` | Führt test2 aus. |
| `toggleDebugLog` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Schaltet debug log um. |
| `toggleRadarMode` | 1 | `08/ui/core/lua/monitors.lua` | Schaltet radar mode um. |
| `truncateLeftRightText` | 1 | `08/ui/core/lua/monitors.lua` | Führt truncate left right text aus (Parameter: lefttext, righttext, width). |
| `unknown` | 5 | `08/ui/core/lua/jit/dis_mips.lua` | Führt unknown aus. |
| `unlockInfo` | 1 | `08/ui/addons/ego_targetmonitor/targetmonitor.lua` | Führt unlock info aus. |
| `unmapDialogButton` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt unmap dialog button aus (Parameter: button). |
| `unselectDialogButton` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt unselect dialog button aus (Parameter: button). |
| `unselectMouseJoystickButton` | 1 | `08/ui/core/lua/dialogmenu.lua` | Führt unselect mouse joystick button aus. |
| `unsetPointerOverride` | 1 | `08/ui/core/lua/targetsystem.lua` | Führt unset pointer override aus (Parameter: targetElement). |
| `updateActiveState` | 1 | `08/ui/core/lua/monitors.lua` | Aktualisiert active state (Parameter: force, refresh, allowPlaySound, keepCutscene). |
| `updateActivityColor` | 2 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert activity color. |
| `updateAimTargetElement` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert aim target element (Parameter: targetElement, isOnScreen). |
| `updateAllOutlines` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert all outlines. |
| `updateAllPointerOverrides` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert all pointer overrides. |
| `updateArrowState` | 2 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert arrow state (Parameter: arrowElement, wasHidden, isHidden). |
| `updateBoostBar` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert boost bar. |
| `updateBottomText` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert bottom text (Parameter: targetElement, onScreen, bottomText, targetElementPosX, targetElementPosY). |
| `updateButtons` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Aktualisiert buttons (Parameter: optionalAssertButton, assertButton, errorPopUpButton, optionalAssertPopUpButton, assertPopUpButton, showFPSButton). |
| `updateChatNotification` | 1 | `08/ui/core/lua/monitors.lua` | Aktualisiert chat notification. |
| `updateCheckEngineLight` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert check engine light. |
| `updateColor` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert color (Parameter: targetElement, relation, onScreen). |
| `updateControllerSelection` | 1 | `08/ui/core/lua/compass.lua` | Aktualisiert controller selection. |
| `updateCountermeasures` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert countermeasures. |
| `updateCoverLine` | 1 | `08/ui/core/lua/monitors.lua` | Aktualisiert cover line. |
| `updateDebugMessage` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Aktualisiert debug message (Parameter: messageNumber). |
| `updateDebugOutlines` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert debug outlines. |
| `updateDialogMenuButtons` | 1 | `08/ui/core/lua/dialogmenu.lua` | Aktualisiert dialog menu buttons (Parameter: oldButton, newButton). |
| `updateDronePanel` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert drone panel (Parameter: force). |
| `updateDroneType` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert drone type (Parameter: dronePanelEntry, droneTypeDetails, force). |
| `updateDynamicRectangleIcons` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert dynamic rectangle icons (Parameter: targetElement). |
| `updateElementPosition` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert element position (Parameter: element, x, y, z, yaw, pitch, roll, scale). |
| `updateFPS` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Aktualisiert fps. |
| `updateFactionColor` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert faction color (Parameter: targetElement). |
| `updateHullShield` | 2 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert hull shield. |
| `updateIcon` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert icon (Parameter: targetElement). |
| `updateIconSize` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert icon size (Parameter: targetElement, onScreen). |
| `updateIndicatorScalePositionAndActivation` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert indicator scale position and activation (Parameter: mode). |
| `updateIndicators` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert indicators. |
| `updateInteractiveText` | 1 | `08/ui/core/lua/monitors.lua` | Aktualisiert interactive text. |
| `updateMailNotification` | 1 | `08/ui/core/lua/monitors.lua` | Aktualisiert mail notification. |
| `updateMatchSpeedElement` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert match speed element (Parameter: matchSpeed, targetSpeed, normalTargetSpeed). |
| `updateMessageStartTimes` | 1 | `08/ui/core/lua/monitors.lua` | Aktualisiert message start times (Parameter: curtime, pausedtime). |
| `updateMessageTicker` | 1 | `08/ui/core/lua/monitors.lua` | Aktualisiert message ticker. |
| `updateMessages` | 1 | `08/ui/core/lua/monitors.lua` | Aktualisiert messages. |
| `updateMissileLock` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert missile lock (Parameter: missileLockEntry, lockPercentage, counterMeasureTarget). |
| `updateMissileLockColor` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert missile lock color (Parameter: relation). |
| `updateMissileLocks` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert missile locks. |
| `updateMissionArrow` | 2 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert mission arrow. |
| `updateMissionDetails` | 1 | `08/ui/core/lua/monitors.lua` | Aktualisiert mission details (Parameter: blinking). |
| `updateMousePosition` | 1 | `08/ui/core/lua/compass.lua` | Aktualisiert mouse position. |
| `updateMouseSteeringLine` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert mouse steering line. |
| `updateNotorietyLadder` | 1 | `08/ui/core/lua/monitors.lua` | Aktualisiert notoriety ladder (Parameter: notorietyFactionDetails, notorietyComponentDetails). |
| `updateOffScreenBox` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert off screen box (Parameter: targetElement, onScreen). |
| `updateOutline` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert outline (Parameter: targetElement). |
| `updateOxygenBar` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert oxygen bar. |
| `updatePointerOverride` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert pointer override (Parameter: targetElement, actionPointer, isSofttarget, isInstantAction). |
| `updateProgressbar` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert progressbar. |
| `updateRadar` | 1 | `08/ui/core/lua/monitors.lua` | Aktualisiert radar. |
| `updateRadarExtents` | 1 | `08/ui/core/lua/monitors.lua` | Aktualisiert radar extents. |
| `updateRadarTarget` | 1 | `08/ui/core/lua/monitors.lua` | Aktualisiert radar target (Parameter: focusComponent). |
| `updateRectangleElements` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert rectangle elements (Parameter: targetElement). |
| `updateReenableButton` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Aktualisiert reenable button. |
| `updateRelation` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert relation (Parameter: targetElement, newRelation, newOwningFactionID). |
| `updateRelationStatusData` | 1 | `08/ui/core/lua/monitors.lua` | Aktualisiert relation status data (Parameter: notorietyComponentDetails). |
| `updateScenarioTexts` | 1 | `08/ui/core/lua/loading.lua` | Aktualisiert scenario texts. |
| `updateScreenshots` | 2 | `08/ui/core/lua/extro.lua` | Aktualisiert screenshots. |
| `updateSelectedButton` | 1 | `08/ui/core/lua/dialogmenu.lua` | Aktualisiert selected button (Parameter: angle). |
| `updateSelection` | 1 | `08/ui/core/lua/dialogmenu.lua` | Aktualisiert selection. |
| `updateSeta` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert seta. |
| `updateSideText` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert side text (Parameter: targetElement, onScreen, distance). |
| `updateSideText2` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert side text2 (Parameter: targetElement). |
| `updateSideTextPosition` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert side text position (Parameter: targetElement, targetElementPosX, targetElementPosY). |
| `updateSofttargetLock` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert softtarget lock (Parameter: currentTargetIsHighestPriority). |
| `updateSofttargetManager` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert softtarget manager (Parameter: targetElements). |
| `updateSofttargetManagerActivationState` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert softtarget manager activation state. |
| `updateSofttargetTargetElement` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert softtarget target element (Parameter: messageID). |
| `updateSpeedbar` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert speedbar. |
| `updateState` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert state (Parameter: targetElement, force). |
| `updateStates` | 1 | `08/ui/core/lua/dialogmenu.lua` | Aktualisiert states. |
| `updateTargetArrow` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert target arrow. |
| `updateTargetElement` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert target element (Parameter: targetElement). |
| `updateTargetElementData` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert target element data (Parameter: targetElements). |
| `updateTargetElementPosition` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert target element position (Parameter: targetElement). |
| `updateTargetMonitorDisplay` | 1 | `08/ui/core/lua/monitors.lua` | Aktualisiert target monitor display (Parameter: details, enableTargetMonitorRadar, isNotification). |
| `updateTargetMonitorNotifications` | 1 | `08/ui/core/lua/monitors.lua` | Aktualisiert target monitor notifications. |
| `updateTargetText` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert target text. |
| `updateText` | 2 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert text. |
| `updateVelocityIndicator` | 1 | `08/ui/core/lua/targetsystem.lua` | Aktualisiert velocity indicator. |
| `updateWeaponGroup` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert weapon group (Parameter: element, group, playSound). |
| `updateWeaponPanel` | 1 | `08/ui/core/lua/crosshair handling.lua` | Aktualisiert weapon panel. |
| `upgradeData` | 1 | `08/ui/addons/ego_debuglog/debuglog.lua` | Führt upgrade data aus. |
| `usage` | 1 | `08/ui/core/lua/jit/bcsave.lua` | Führt usage aus. |
| `widgetHelpers.boxtext:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt boxtext:create descriptor aus. |
| `widgetHelpers.button:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button:create descriptor aus. |
| `widgetHelpers.cell:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:create descriptor aus. |
| `widgetHelpers.checkbox:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt checkbox:create descriptor aus. |
| `widgetHelpers.dropdown:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt dropdown:create descriptor aus. |
| `widgetHelpers.editbox:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt editbox:create descriptor aus. |
| `widgetHelpers.flowchart:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:create descriptor aus. |
| `widgetHelpers.flowchart:getFullSizeAndScrollBarData` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:get full size and scroll bar data aus. |
| `widgetHelpers.flowchartedge:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartedge:create descriptor aus. |
| `widgetHelpers.flowchartjunction:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartjunction:create descriptor aus. |
| `widgetHelpers.flowchartnode:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:create descriptor aus. |
| `widgetHelpers.flowchartnode:onSliderChanged` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:on slider changed aus (Parameter: slideridx, slidervalue). |
| `widgetHelpers.flowchartnode:setScripts` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:set scripts aus. |
| `widgetHelpers.graph:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt graph:create descriptor aus. |
| `widgetHelpers.icon:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt icon:create descriptor aus. |
| `widgetHelpers.rendertarget:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt rendertarget:create descriptor aus. |
| `widgetHelpers.shieldhullbar:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt shieldhullbar:create descriptor aus. |
| `widgetHelpers.slidercell:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt slidercell:create descriptor aus. |
| `widgetHelpers.statusbar:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt statusbar:create descriptor aus. |
| `widgetHelpers.table:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:create descriptor aus. |
| `widgetHelpers.text:createDescriptor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt text:create descriptor aus. |
| `widgetPrototypes.boxtext:getMinTextHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt boxtext:get min text height aus (Parameter: scaling). |
| `widgetPrototypes.boxtext:getTextHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt boxtext:get text height aus (Parameter: scaling). |
| `widgetPrototypes.button:getHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button:get height aus (Parameter: raw). |
| `widgetPrototypes.button:setHotkey` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button:set hotkey aus (Parameter: hotkey, properties). |
| `widgetPrototypes.button:setIcon` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button:set icon aus (Parameter: icon, properties). |
| `widgetPrototypes.button:setIcon2` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button:set icon2 aus (Parameter: icon, properties). |
| `widgetPrototypes.button:setText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button:set text aus (Parameter: text, properties). |
| `widgetPrototypes.button:setText2` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt button:set text2 aus (Parameter: text, properties). |
| `widgetPrototypes.cell:createBoxText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:create box text aus (Parameter: text, properties). |
| `widgetPrototypes.cell:createButton` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:create button aus (Parameter: properties). |
| `widgetPrototypes.cell:createCheckBox` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:create check box aus (Parameter: checked, properties). |
| `widgetPrototypes.cell:createDropDown` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:create drop down aus (Parameter: options, properties). |
| `widgetPrototypes.cell:createEditBox` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:create edit box aus (Parameter: properties). |
| `widgetPrototypes.cell:createGraph` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:create graph aus (Parameter: properties). |
| `widgetPrototypes.cell:createIcon` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:create icon aus (Parameter: icon, properties). |
| `widgetPrototypes.cell:createObjectShieldHullBar` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:create object shield hull bar aus (Parameter: object, properties). |
| `widgetPrototypes.cell:createShieldHullBar` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:create shield hull bar aus (Parameter: shield, hull, properties). |
| `widgetPrototypes.cell:createSliderCell` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:create slider cell aus (Parameter: properties). |
| `widgetPrototypes.cell:createStatusBar` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:create status bar aus (Parameter: properties). |
| `widgetPrototypes.cell:createText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:create text aus (Parameter: text, properties). |
| `widgetPrototypes.cell:getColSpanWidth` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:get col span width aus. |
| `widgetPrototypes.cell:getHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:get height aus. |
| `widgetPrototypes.cell:getOffsetX` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:get offset x aus. |
| `widgetPrototypes.cell:getWidth` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:get width aus. |
| `widgetPrototypes.cell:setBackgroundColSpan` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:set background col span aus (Parameter: bgcolspan). |
| `widgetPrototypes.cell:setColSpan` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt cell:set col span aus (Parameter: colspan). |
| `widgetPrototypes.dropdown:setHotkey` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt dropdown:set hotkey aus (Parameter: hotkey, properties). |
| `widgetPrototypes.dropdown:setIconProperties` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt dropdown:set icon properties aus (Parameter: properties). |
| `widgetPrototypes.dropdown:setText2Properties` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt dropdown:set text2 properties aus (Parameter: properties). |
| `widgetPrototypes.dropdown:setTextProperties` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt dropdown:set text properties aus (Parameter: properties). |
| `widgetPrototypes.editbox:getHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt editbox:get height aus. |
| `widgetPrototypes.editbox:setHotkey` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt editbox:set hotkey aus (Parameter: hotkey, properties). |
| `widgetPrototypes.editbox:setText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt editbox:set text aus (Parameter: text, properties). |
| `widgetPrototypes.flowchart:addJunction` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:add junction aus (Parameter: row, col, properties). |
| `widgetPrototypes.flowchart:addNode` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:add node aus (Parameter: row, col, customdata, properties). |
| `widgetPrototypes.flowchart:collapseAllNodes` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:collapse all nodes aus. |
| `widgetPrototypes.flowchart:getCaptionHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:get caption height aus (Parameter: col). |
| `widgetPrototypes.flowchart:getCell` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:get cell aus (Parameter: row, col, celltype). |
| `widgetPrototypes.flowchart:getColMinWidth` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:get col min width aus (Parameter: col). |
| `widgetPrototypes.flowchart:getFullHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:get full height aus. |
| `widgetPrototypes.flowchart:getMaxVisibleHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:get max visible height aus. |
| `widgetPrototypes.flowchart:getMinFullWidth` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:get min full width aus. |
| `widgetPrototypes.flowchart:getRowHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:get row height aus (Parameter: row). |
| `widgetPrototypes.flowchart:getVisibleHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:get visible height aus. |
| `widgetPrototypes.flowchart:getVisibleWidth` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:get visible width aus. |
| `widgetPrototypes.flowchart:hasHorizontalScrollBar` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:has horizontal scroll bar aus. |
| `widgetPrototypes.flowchart:hasScrollBar` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:has scroll bar aus. |
| `widgetPrototypes.flowchart:setColBackgroundColor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:set col background color aus (Parameter: col, bgcolor). |
| `widgetPrototypes.flowchart:setColWidthMin` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:set col width min aus (Parameter: col, minwidth, extensionweight, scaling). |
| `widgetPrototypes.flowchart:setColumnCaption` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:set column caption aus (Parameter: col, text, properties). |
| `widgetPrototypes.flowchart:setDefaultEdgeProperties` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:set default edge properties aus (Parameter: properties). |
| `widgetPrototypes.flowchart:setDefaultIconProperties` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:set default icon properties aus (Parameter: properties). |
| `widgetPrototypes.flowchart:setDefaultNodeProperties` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:set default node properties aus (Parameter: properties). |
| `widgetPrototypes.flowchart:setDefaultTextProperties` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchart:set default text properties aus (Parameter: properties). |
| `widgetPrototypes.flowchartcell:addEdgeTo` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartcell:add edge to aus (Parameter: destcell, properties). |
| `widgetPrototypes.flowchartedge:updateColor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartedge:update color aus (Parameter: color). |
| `widgetPrototypes.flowchartjunction:getCellMinHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartjunction:get cell min height aus. |
| `widgetPrototypes.flowchartjunction:getCellMinWidth` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartjunction:get cell min width aus. |
| `widgetPrototypes.flowchartnode:collapse` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:collapse aus. |
| `widgetPrototypes.flowchartnode:expand` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:expand aus. |
| `widgetPrototypes.flowchartnode:getCellMinHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:get cell min height aus. |
| `widgetPrototypes.flowchartnode:getCellMinWidth` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:get cell min width aus. |
| `widgetPrototypes.flowchartnode:getExpandedFrame` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:get expanded frame aus. |
| `widgetPrototypes.flowchartnode:setStatusIcon` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:set status icon aus (Parameter: icon, properties). |
| `widgetPrototypes.flowchartnode:setStatusText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:set status text aus (Parameter: text, properties). |
| `widgetPrototypes.flowchartnode:setText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:set text aus (Parameter: text, properties). |
| `widgetPrototypes.flowchartnode:updateMaxValue` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:update max value aus (Parameter: value). |
| `widgetPrototypes.flowchartnode:updateOutlineColor` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:update outline color aus (Parameter: color). |
| `widgetPrototypes.flowchartnode:updateSlider1` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:update slider1 aus (Parameter: value). |
| `widgetPrototypes.flowchartnode:updateSlider2` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:update slider2 aus (Parameter: value). |
| `widgetPrototypes.flowchartnode:updateSliderStep` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:update slider step aus (Parameter: step). |
| `widgetPrototypes.flowchartnode:updateStatus` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:update status aus (Parameter: text, icon, bgicon, color, mouseovertext). |
| `widgetPrototypes.flowchartnode:updateText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:update text aus (Parameter: text, color). |
| `widgetPrototypes.flowchartnode:updateValue` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt flowchartnode:update value aus (Parameter: value). |
| `widgetPrototypes.frame:addFlowchart` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt frame:add flowchart aus (Parameter: numrows, numcolumns, properties). |
| `widgetPrototypes.frame:addRenderTarget` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt frame:add render target aus (Parameter: properties). |
| `widgetPrototypes.frame:addTable` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt frame:add table aus (Parameter: numcolumns, properties). |
| `widgetPrototypes.frame:display` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt frame:display aus. |
| `widgetPrototypes.frame:getAvailableHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt frame:get available height aus. |
| `widgetPrototypes.frame:getUsedHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt frame:get used height aus. |
| `widgetPrototypes.frame:setBackground` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt frame:set background aus (Parameter: icon, properties). |
| `widgetPrototypes.frame:setBackground2` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt frame:set background2 aus (Parameter: icon, properties). |
| `widgetPrototypes.frame:setOverlay` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt frame:set overlay aus (Parameter: icon, properties). |
| `widgetPrototypes.frame:update` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt frame:update aus. |
| `widgetPrototypes.graph:addDataRecord` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt graph:add data record aus (Parameter: properties). |
| `widgetPrototypes.graph:selectDataPoint` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt graph:select data point aus (Parameter: recordIdx, dataIdx, selected). |
| `widgetPrototypes.graph:setDefaultDataRecordProperties` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt graph:set default data record properties aus (Parameter: properties). |
| `widgetPrototypes.graph:setTitle` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt graph:set title aus (Parameter: title, properties). |
| `widgetPrototypes.graph:setXAxis` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt graph:set xaxis aus (Parameter: properties). |
| `widgetPrototypes.graph:setXAxisLabel` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt graph:set xaxis label aus (Parameter: label, properties). |
| `widgetPrototypes.graph:setYAxis` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt graph:set yaxis aus (Parameter: properties). |
| `widgetPrototypes.graph:setYAxisLabel` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt graph:set yaxis label aus (Parameter: label, properties). |
| `widgetPrototypes.graphdatarecord:addData` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt graphdatarecord:add data aus (Parameter: x, y, icon, mouseovertext, inactive). |
| `widgetPrototypes.icon:getHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt icon:get height aus (Parameter: raw). |
| `widgetPrototypes.icon:setText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt icon:set text aus (Parameter: text, properties). |
| `widgetPrototypes.icon:setText2` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt icon:set text2 aus (Parameter: text, properties). |
| `widgetPrototypes.row:getHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt row:get height aus. |
| `widgetPrototypes.slidercell:getHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt slidercell:get height aus. |
| `widgetPrototypes.slidercell:setText` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt slidercell:set text aus (Parameter: text, properties). |
| `widgetPrototypes.slidercell:updateMaxSelectValue` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt slidercell:update max select value aus (Parameter: value). |
| `widgetPrototypes.slidercell:updateMaxValue` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt slidercell:update max value aus (Parameter: value). |
| `widgetPrototypes.slidercell:updateMinSelectValue` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt slidercell:update min select value aus (Parameter: value). |
| `widgetPrototypes.slidercell:updateMinValue` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt slidercell:update min value aus (Parameter: value). |
| `widgetPrototypes.table:addConnection` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:add connection aus (Parameter: row, col, clearCol). |
| `widgetPrototypes.table:addEmptyRow` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:add empty row aus (Parameter: height, scaling, color, borderbelow). |
| `widgetPrototypes.table:addRow` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:add row aus (Parameter: rowdata, properties). |
| `widgetPrototypes.table:getFullHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:get full height aus. |
| `widgetPrototypes.table:getMaxVisibleHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:get max visible height aus. |
| `widgetPrototypes.table:getVisibleHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:get visible height aus. |
| `widgetPrototypes.table:hasScrollBar` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:has scroll bar aus. |
| `widgetPrototypes.table:setColWidth` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:set col width aus (Parameter: col, width, scaling). |
| `widgetPrototypes.table:setColWidthMin` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:set col width min aus (Parameter: col, width, weight, scaling). |
| `widgetPrototypes.table:setColWidthMinPercent` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:set col width min percent aus (Parameter: col, width, weight). |
| `widgetPrototypes.table:setColWidthPercent` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:set col width percent aus (Parameter: col, width). |
| `widgetPrototypes.table:setDefaultBackgroundColSpan` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:set default background col span aus (Parameter: col, bgcolspan). |
| `widgetPrototypes.table:setDefaultCellProperties` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:set default cell properties aus (Parameter: widgettype, properties). |
| `widgetPrototypes.table:setDefaultColSpan` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:set default col span aus (Parameter: col, colspan). |
| `widgetPrototypes.table:setDefaultComplexCellProperties` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:set default complex cell properties aus (Parameter: widgettype, complexproperty, properties). |
| `widgetPrototypes.table:setSelectedCol` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:set selected col aus (Parameter: col). |
| `widgetPrototypes.table:setSelectedRow` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:set selected row aus (Parameter: row). |
| `widgetPrototypes.table:setShiftStartEnd` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:set shift start end aus (Parameter: startrow, endrow). |
| `widgetPrototypes.table:setTopRow` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt table:set top row aus (Parameter: row). |
| `widgetPrototypes.text:getMinTextHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt text:get min text height aus (Parameter: scaling). |
| `widgetPrototypes.text:getTextHeight` | 1 | `08/ui/addons/ego_detailmonitorhelper/helper.lua` | Führt text:get text height aus (Parameter: scaling). |
| `widgetSystem.activateEditBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktiviert edit box (Parameter: editboxID, cursorpos, shiftstartpos). |
| `widgetSystem.activateEditBoxInternal` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktiviert edit box internal (Parameter: frameElement, editboxID, editboxElement, cursorpos, shiftstartpos). |
| `widgetSystem.activateSliderCellInput` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktiviert slider cell input (Parameter: slidercellID). |
| `widgetSystem.activateSliderCellInputInternal` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktiviert slider cell input internal (Parameter: slidercellID, slidercellElement). |
| `widgetSystem.addDeferredElementInitializer` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Fügt deferred element initializer hinzu (Parameter: element, initializer, precedence, totalCount, numInitAtStartup, numInitPerFrame). |
| `widgetSystem.addFlowchartConnector` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Fügt flowchart connector hinzu (Parameter: connectorTable, x, y, xUseHalfPixel, yUseHalfPixel, size, color). |
| `widgetSystem.addHelpOverlay` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Fügt help overlay hinzu (Parameter: frameElement, widgetID, x, y, width, height, standardbutton, backgroundcolspanwidth, overrideinfo). |
| `widgetSystem.addToAssociationList` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Fügt to association list hinzu (Parameter: widgetID, elementEntry, rootAnarkElement, parentX, parentY, parentWidth, textComponent, activeSlide, inactiveSlide, curSlide). |
| `widgetSystem.calculateFixedRowHeight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Berechnet fixed row height (Parameter: tableID, tableElement). |
| `widgetSystem.calculateMinRowHeight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Berechnet min row height (Parameter: tableID, tableElement). |
| `widgetSystem.calculateRowsToMoveByBottomRow` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Berechnet rows to move by bottom row (Parameter: tableID, tableElement, newBottomRow). |
| `widgetSystem.calculateRowsToMoveByPixelDiff` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Berechnet rows to move by pixel diff (Parameter: tableID, tableElement, pixeldiff). |
| `widgetSystem.calculateRowsToMoveByTopRow` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Berechnet rows to move by top row (Parameter: tableID, tableElement, newTopRow). |
| `widgetSystem.calculateSliderScrollBarPageStep` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Berechnet slider scroll bar page step (Parameter: singleStepSliderWidth, sliderWidth, granularity). |
| `widgetSystem.cancelEditBoxInput` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt cancel edit box input aus (Parameter: editboxID). |
| `widgetSystem.cancelEditBoxInputInternal` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt cancel edit box input internal aus (Parameter: editboxID, editboxElement). |
| `widgetSystem.cancelSliderCellInputInternal` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt cancel slider cell input internal aus (Parameter: slidercellID, slidercellElement). |
| `widgetSystem.checkElementByRootAnarkElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt check element by root anark element aus (Parameter: type, widgetElement, rootAnarkElement). |
| `widgetSystem.clearHelpOverlays` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Leert help overlays (Parameter: frameElement). |
| `widgetSystem.closeDropDownOptions` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Schließt drop down options (Parameter: dropdownID). |
| `widgetSystem.combinedScrollDownRenderTarget` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt combined scroll down render target aus (Parameter: renderTargetID, step). |
| `widgetSystem.combinedScrollUpRenderTarget` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt combined scroll up render target aus (Parameter: renderTargetID, step). |
| `widgetSystem.confirmEditBoxInput` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt confirm edit box input aus (Parameter: editboxID). |
| `widgetSystem.confirmEditBoxInputInternal` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt confirm edit box input internal aus (Parameter: editboxID, editboxElement, isconfirmed, wastableclick). |
| `widgetSystem.confirmSliderCellInputInternal` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt confirm slider cell input internal aus (Parameter: slidercellID, slidercellElement). |
| `widgetSystem.convertAlignment` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt convert alignment aus (Parameter: alignment). |
| `widgetSystem.convertColumnWidth` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt convert column width aus (Parameter: columnWidths, columnWidthsInPercent, tablewidth). |
| `widgetSystem.deactivateDirectInputElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Deaktiviert direct input elements. |
| `widgetSystem.deactivateEditBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Deaktiviert edit box (Parameter: editboxID, editboxElement, isconfirmed, wastableclick). |
| `widgetSystem.deactivateSliderCellInput` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Deaktiviert slider cell input (Parameter: slidercellElement). |
| `widgetSystem.drawCircle` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeichnet circle (Parameter: id, radiusx, radiusy, centerx, centery, z, color). |
| `widgetSystem.drawFlowchartBackground` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeichnet flowchart background (Parameter: anarkElement, x, y, width, height, backgroundelementname, materialname, color, slide). |
| `widgetSystem.drawFlowchartConnectors` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeichnet flowchart connectors (Parameter: flowchartNodeElement, connectorTable). |
| `widgetSystem.drawFlowchartContent` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeichnet flowchart content (Parameter: frameElement, flowchartID, flowchartElement). |
| `widgetSystem.drawFlowchartEdge` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeichnet flowchart edge (Parameter: frameElement, flowchartEdgeID, flowchartEdgeElement, edge, flowchartData). |
| `widgetSystem.drawFlowchartJunction` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeichnet flowchart junction (Parameter: flowchartNodeID, flowchartNodeElement). |
| `widgetSystem.drawFlowchartNode` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeichnet flowchart node (Parameter: flowchartNodeID, flowchartNodeElement). |
| `widgetSystem.drawRect` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeichnet rect (Parameter: id, width, height, offsetx, offsety, angle, z, color). |
| `widgetSystem.drawTableCells` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeichnet table cells (Parameter: frameElement, tableID, tableElement, firstRow, lastRow, curRow, firsttime, modified). |
| `widgetSystem.drawTableSection` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeichnet table section (Parameter: frameElement, tableID, tableElement, firstRow, lastRow, displayedRows, cellposy, curtableheight, cellIndexOffset, isFixedRowSection, firsttime). |
| `widgetSystem.drawTriangle` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeichnet triangle (Parameter: id, width, height, offsetx, offsety, angle, z, color). |
| `widgetSystem.findEditBoxWordAtPos` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt find edit box word at pos aus (Parameter: editboxElement, curpos). |
| `widgetSystem.getBackgroundColumnSpanInfo` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt background column span info zurück (Parameter: tableID, tableElement, row, col, isFixedRowSection). |
| `widgetSystem.getColors` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt colors zurück. |
| `widgetSystem.getColumnSpanInfo` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt column span info zurück (Parameter: tableID, tableElement, row, col, isFixedRowSection). |
| `widgetSystem.getCurrentInterval` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt current interval zurück. |
| `widgetSystem.getCurrentMouseOverFont` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt current mouse over font zurück. |
| `widgetSystem.getCurrentMouseOverWidth` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt current mouse over width zurück. |
| `widgetSystem.getDropDownMousePosition` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt drop down mouse position zurück (Parameter: dropdownID). |
| `widgetSystem.getDropDownOptionByOptionAnarkElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt drop down option by option anark element zurück (Parameter: dropdownElement, optionElement). |
| `widgetSystem.getDropDownOptionIndexByAnarkElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt drop down option index by anark element zurück (Parameter: dropdownElement, anarkElement). |
| `widgetSystem.getEditBoxCursorPosFromMouse` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt edit box cursor pos from mouse zurück (Parameter: frameElement, editboxID, editboxElement). |
| `widgetSystem.getEditBoxMousePosition` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt edit box mouse position zurück (Parameter: frameElement, editboxID). |
| `widgetSystem.getElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt element zurück (Parameter: type). |
| `widgetSystem.getElementInternal` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt element internal zurück (Parameter: type, elements). |
| `widgetSystem.getFlowchartAbsoluteSlotOffset` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt flowchart absolute slot offset zurück (Parameter: flowchartData, row, col, slottype, slot). |
| `widgetSystem.getFlowchartElementByMousePick` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt flowchart element by mouse pick zurück (Parameter: anarkElement). |
| `widgetSystem.getFlowchartFirstVisibleCell` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt flowchart first visible cell zurück (Parameter: flowchartID). |
| `widgetSystem.getFlowchartNodeElementByAnarkElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt flowchart node element by anark element zurück (Parameter: elementType, anarkElement). |
| `widgetSystem.getFlowchartNodeExpandedFrameData` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt flowchart node expanded frame data zurück (Parameter: flowchartNodeID). |
| `widgetSystem.getFlowchartNumCellsToScroll` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt flowchart num cells to scroll zurück (Parameter: cellsizes, totalvisiblesize, firstvisibleindex, scrolldirection, step). |
| `widgetSystem.getFlowchartNumCellsToScrollPage` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt flowchart num cells to scroll page zurück (Parameter: cellsizes, totalvisiblesize, firstvisibleindex, scrolldirection). |
| `widgetSystem.getFlowchartScrollBarByAnarkElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt flowchart scroll bar by anark element zurück (Parameter: anarkElement). |
| `widgetSystem.getFlowchartSelectedCell` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt flowchart selected cell zurück (Parameter: flowchartID). |
| `widgetSystem.getFlowchartVisibleCellData` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt flowchart visible cell data zurück (Parameter: cellsizes, totalvisiblesize, firstvisibleindex). |
| `widgetSystem.getFontHeight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt font height zurück (Parameter: fontname, fontsize). |
| `widgetSystem.getFrameElementByAnarkStandardButtonElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt frame element by anark standard button element zurück (Parameter: anarkElement). |
| `widgetSystem.getFrameElementByFlowchartElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt frame element by flowchart element zurück (Parameter: flowchartElement). |
| `widgetSystem.getFrameElementByFlowchartNodeElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt frame element by flowchart node element zurück (Parameter: flowchartNodeElement). |
| `widgetSystem.getFrameElementByTableElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt frame element by table element zurück (Parameter: tableElement). |
| `widgetSystem.getGraphDataPointByDataPointAnarkElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt graph data point by data point anark element zurück (Parameter: graphElement, dataPointElement). |
| `widgetSystem.getGraphIconByIconAnarkElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt graph icon by icon anark element zurück (Parameter: graphElement, iconElement). |
| `widgetSystem.getHighlightedRowsCount` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt highlighted rows count zurück (Parameter: tableElement). |
| `widgetSystem.getHorizontalScrollBarSliderPosition` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt horizontal scroll bar slider position zurück (Parameter: anarkScrollBarElement). |
| `widgetSystem.getNextColumn` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt next column zurück (Parameter: startCol, minLimit, maxLimit, step, dir). |
| `widgetSystem.getNumAvailableTableRowElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt num available table row elements zurück. |
| `widgetSystem.getRenderTargetElementByAnarkElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt render target element by anark element zurück (Parameter: anarkElement). |
| `widgetSystem.getRenderTargetMousePosition` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt render target mouse position zurück (Parameter: renderTargetID). |
| `widgetSystem.getRenderTargetTexture` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt render target texture zurück (Parameter: renderTargetID). |
| `widgetSystem.getRootAnarkElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt root anark element zurück (Parameter: anarkElement). |
| `widgetSystem.getScrollBarSliderPosition` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt scroll bar slider position zurück (Parameter: anarkScrollBarElement). |
| `widgetSystem.getSelectableCellElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt selectable cell element zurück (Parameter: tableID, row, col, dir, limit). |
| `widgetSystem.getSelectedRows` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt selected rows zurück (Parameter: tableID). |
| `widgetSystem.getShapeElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt shape element zurück (Parameter: type). |
| `widgetSystem.getShiftStartEndRow` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt shift start end row zurück (Parameter: tableID). |
| `widgetSystem.getSliderCellBaseXPosition` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt slider cell base xposition zurück (Parameter: slidercellElement). |
| `widgetSystem.getSliderCellMousePosition` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt slider cell mouse position zurück (Parameter: frameElement, slidercellID). |
| `widgetSystem.getSliderCellValueFromXPosition` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt slider cell value from xposition zurück (Parameter: slidercellElement, x). |
| `widgetSystem.getSliderCellXPositionFromValue` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt slider cell xposition from value zurück (Parameter: slidercellElement, value). |
| `widgetSystem.getTableCellElementByAnarkElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt table cell element by anark element zurück (Parameter: type, anarkElement). |
| `widgetSystem.getTableElementByAnarkTableCellElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt table element by anark table cell element zurück (Parameter: type, anarkElement). |
| `widgetSystem.getTableElementByMousePick` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt table element by mouse pick zurück (Parameter: mousePickElement). |
| `widgetSystem.getTableElementByScrollBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt table element by scroll bar zurück (Parameter: scrollBarElement). |
| `widgetSystem.getTopRow` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt top row zurück (Parameter: tableID). |
| `widgetSystem.getUTF8CharacterPrevIndex` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt utf8 character prev index zurück (Parameter: text, pos). |
| `widgetSystem.getUsableTableWidth` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt usable table width zurück (Parameter: width, offsetx, numColumns, hasScrollBar). |
| `widgetSystem.getWidgetIDByAnarkElementEntry` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt widget idby anark element entry zurück (Parameter: anarkElementEntry). |
| `widgetSystem.getWidgetIDByElementEntry` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt widget idby element entry zurück (Parameter: elementEntry). |
| `widgetSystem.getWidgetSystemSize` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Gibt widget system size zurück. |
| `widgetSystem.hasNonFixedRows` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt has non fixed rows aus (Parameter: tableElement). |
| `widgetSystem.hideAllElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt all elements. |
| `widgetSystem.hideAllShapes` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt all shapes. |
| `widgetSystem.hideBoxText` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt box text (Parameter: boxtextElement). |
| `widgetSystem.hideButton` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt button (Parameter: buttonElement, iconActive, icon2Active, textActive, text2Active, hotkeyIconActive). |
| `widgetSystem.hideCheckBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt check box (Parameter: checkboxElement). |
| `widgetSystem.hideCircle` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt circle (Parameter: id). |
| `widgetSystem.hideCircles` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt circles. |
| `widgetSystem.hideDropDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt drop down (Parameter: dropdownElement, iconActive, hotykeyIconActive). |
| `widgetSystem.hideDropDownOptions` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt drop down options (Parameter: dropdownID, dropdownElement). |
| `widgetSystem.hideEditBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt edit box (Parameter: editboxElement, hotkeyIconActive). |
| `widgetSystem.hideFlowchart` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt flowchart (Parameter: frameElement, flowchartElement). |
| `widgetSystem.hideFlowchartContent` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt flowchart content (Parameter: frameElement, flowchartElement). |
| `widgetSystem.hideFlowchartEdge` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt flowchart edge (Parameter: frameElement, edge, flowchartEdgeElement). |
| `widgetSystem.hideFlowchartNode` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt flowchart node (Parameter: frameElement, flowchartNodeElement). |
| `widgetSystem.hideFrame` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt frame (Parameter: frameElement, keepMinimizedState). |
| `widgetSystem.hideGraph` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt graph (Parameter: graphElement). |
| `widgetSystem.hideHelpOverlay` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt help overlay (Parameter: keepsignals). |
| `widgetSystem.hideHelpOverlayID` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt help overlay id (Parameter: id). |
| `widgetSystem.hideHorizontalScrollBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt horizontal scroll bar (Parameter: scrollbar). |
| `widgetSystem.hideIcon` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt icon (Parameter: iconelement). |
| `widgetSystem.hideMinimizedMenuName` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt minimized menu name (Parameter: frameElement). |
| `widgetSystem.hideMouseOverText` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt mouse over text (Parameter: widgetID, ignorecount). |
| `widgetSystem.hideRect` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt rect (Parameter: id). |
| `widgetSystem.hideRects` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt rects. |
| `widgetSystem.hideRenderTarget` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt render target (Parameter: frameElement, renderTargetElement). |
| `widgetSystem.hideShieldHullBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt shield hull bar (Parameter: shieldHullBarElement). |
| `widgetSystem.hideSliderCell` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt slider cell (Parameter: slidercellElement). |
| `widgetSystem.hideStandardButtons` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt standard buttons (Parameter: frameElement). |
| `widgetSystem.hideStatusBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt status bar (Parameter: statusBarElement). |
| `widgetSystem.hideTable` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt table (Parameter: frameElement, tableElement). |
| `widgetSystem.hideTableCells` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt table cells (Parameter: frameElement, tableElement). |
| `widgetSystem.hideText` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt text (Parameter: text, hide). |
| `widgetSystem.hideTriangle` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt triangle (Parameter: id). |
| `widgetSystem.hideTriangles` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt triangles. |
| `widgetSystem.hideVerticalScrollBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Versteckt vertical scroll bar (Parameter: scrollbar). |
| `widgetSystem.highlightBorderTableRow` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt highlight border table row aus (Parameter: tableID, tableElement, row, col). |
| `widgetSystem.highlightTableRow` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt highlight table row aus (Parameter: tableID, tableElement, row, col). |
| `widgetSystem.highlightTableRows` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt highlight table rows aus (Parameter: tableID, tableElement, startrow, endrow). |
| `widgetSystem.initScale` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt init scale aus (Parameter: anchorElement). |
| `widgetSystem.initializeBoxTextElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize box text elements aus. |
| `widgetSystem.initializeButtonElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize button elements aus. |
| `widgetSystem.initializeCheckBoxElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize check box elements aus. |
| `widgetSystem.initializeDropDownElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize drop down elements aus. |
| `widgetSystem.initializeEditBoxElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize edit box elements aus. |
| `widgetSystem.initializeFlowchartElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize flowchart elements aus. |
| `widgetSystem.initializeFrameElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize frame elements aus. |
| `widgetSystem.initializeGraphElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize graph elements aus. |
| `widgetSystem.initializeHelpOverlayElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize help overlay elements aus. |
| `widgetSystem.initializeIconElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize icon elements aus. |
| `widgetSystem.initializeMasterElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize master elements aus. |
| `widgetSystem.initializeMiniWidgetSystemElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize mini widget system elements aus. |
| `widgetSystem.initializeRenderTarget` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize render target aus. |
| `widgetSystem.initializeShapeElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize shape elements aus. |
| `widgetSystem.initializeShieldHullBarElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize shield hull bar elements aus. |
| `widgetSystem.initializeSliderCellElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize slider cell elements aus. |
| `widgetSystem.initializeStatusBarElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize status bar elements aus. |
| `widgetSystem.initializeTableElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize table elements aus. |
| `widgetSystem.initializeTableRowElements` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt initialize table row elements aus. |
| `widgetSystem.interpolateColor` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt interpolate color aus (Parameter: color0, color1, value). |
| `widgetSystem.invertColor` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt invert color aus (Parameter: r, g, b). |
| `widgetSystem.moveAnarkElementBetweenFrameLayers` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Bewegt anark element between frame layers (Parameter: anarkElement, fromLayer, toLayer). |
| `widgetSystem.moveAnarkElementFrameLayer` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Bewegt anark element frame layer (Parameter: frameElement, anarkElement, direction). |
| `widgetSystem.moveDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Bewegt down (Parameter: tableID, tableElement, newCurRow, modified). |
| `widgetSystem.moveDropDownElementFrameLayer` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Bewegt drop down element frame layer (Parameter: frameElement, dropdownElement, direction). |
| `widgetSystem.moveDropDownSelection` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Bewegt drop down selection (Parameter: dropdownID, dropdownElement, step). |
| `widgetSystem.moveFlowchartElementFrameLayer` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Bewegt flowchart element frame layer (Parameter: frameElement, flowchartElement, direction). |
| `widgetSystem.moveFlowchartNodeBetweenFrameLayers` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Bewegt flowchart node between frame layers (Parameter: flowchartNodeElement, fromLayer, toLayer). |
| `widgetSystem.moveGraphElementFrameLayer` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Bewegt graph element frame layer (Parameter: frameElement, graphElement, direction). |
| `widgetSystem.moveLeft` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Bewegt left (Parameter: tableID, tableElement). |
| `widgetSystem.moveRight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Bewegt right (Parameter: tableID, tableElement). |
| `widgetSystem.moveTableElementFrameLayer` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Bewegt table element frame layer (Parameter: frameElement, tableElement, direction). |
| `widgetSystem.moveUp` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Bewegt up (Parameter: tableID, tableElement, newCurRow, modified). |
| `widgetSystem.onAutoClose` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on auto close aus. |
| `widgetSystem.onBack` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on back aus. |
| `widgetSystem.onBoxTextUpdate` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on box text update aus (Parameter: _, boxtextID). |
| `widgetSystem.onButtonUpdate` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on button update aus (Parameter: _, buttonID). |
| `widgetSystem.onCheckBoxUpdate` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on check box update aus (Parameter: _, checkboxID). |
| `widgetSystem.onClose` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on close aus. |
| `widgetSystem.onCopy` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on copy aus. |
| `widgetSystem.onCut` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on cut aus. |
| `widgetSystem.onDirectTextInput` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on direct text input aus (Parameter: _, char). |
| `widgetSystem.onDropDownUpdate` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on drop down update aus (Parameter: _, dropdownID). |
| `widgetSystem.onEditBoxTab` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on edit box tab aus. |
| `widgetSystem.onEditBoxUpdate` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on edit box update aus (Parameter: _, editboxID). |
| `widgetSystem.onEnd` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on end aus (Parameter: modified). |
| `widgetSystem.onEvent` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on event aus (Parameter: _, eventName, arg1). |
| `widgetSystem.onFlowchartEdgeUpdate` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on flowchart edge update aus (Parameter: _, flowchartEdgeID). |
| `widgetSystem.onFlowchartNodeUpdate` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on flowchart node update aus (Parameter: _, flowchartNodeID). |
| `widgetSystem.onFontStringUpdate` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on font string update aus (Parameter: _, fontstringID). |
| `widgetSystem.onFrameClose` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on frame close aus (Parameter: _, frameID). |
| `widgetSystem.onFrameMinimize` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on frame minimize aus (Parameter: _, frameID, text). |
| `widgetSystem.onFrameUpdate` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on frame update aus (Parameter: _, frame). |
| `widgetSystem.onGamepadTextInputCancelled` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on gamepad text input cancelled aus. |
| `widgetSystem.onGamepadTextInputEntered` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on gamepad text input entered aus (Parameter: _, text). |
| `widgetSystem.onHome` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on home aus (Parameter: modified). |
| `widgetSystem.onIconUpdate` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on icon update aus (Parameter: _, iconID). |
| `widgetSystem.onInputModeChanged` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on input mode changed aus (Parameter: _, mode). |
| `widgetSystem.onMouseClickButton` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse click button aus (Parameter: anarkElement, delayed, modified). |
| `widgetSystem.onMouseClickCheckBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse click check box aus (Parameter: anarkElement, delayed). |
| `widgetSystem.onMouseClickCommon` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse click common aus (Parameter: frameElement). |
| `widgetSystem.onMouseClickDropDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse click drop down aus (Parameter: anarkElement, delayed). |
| `widgetSystem.onMouseClickDropDownPageScroll` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse click drop down page scroll aus (Parameter: anarkElement, delayed). |
| `widgetSystem.onMouseClickEditBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse click edit box aus (Parameter: isdblclick, anarkElement, delayed, modified). |
| `widgetSystem.onMouseClickFlowchartBackground` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse click flowchart background aus (Parameter: anarkElement, delayed). |
| `widgetSystem.onMouseClickFlowchartNode` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse click flowchart node aus (Parameter: elementType, anarkElement, delayed). |
| `widgetSystem.onMouseClickFlowchartPageScroll` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse click flowchart page scroll aus (Parameter: anarkElement, delayed). |
| `widgetSystem.onMouseClickGraphDataPoint` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse click graph data point aus (Parameter: anarkElement, delayed). |
| `widgetSystem.onMouseClickHelpOverlay` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse click help overlay aus (Parameter: anarkElement, delayed). |
| `widgetSystem.onMouseClickPageScroll` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse click page scroll aus (Parameter: anarkElement, delayed). |
| `widgetSystem.onMouseClickSliderCellNumber` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse click slider cell number aus (Parameter: anarkElement, delayed). |
| `widgetSystem.onMouseClickStandardButton` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse click standard button aus (Parameter: type, anarkElement, delayed). |
| `widgetSystem.onMouseClickTableCell` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse click table cell aus (Parameter: isdblclick, anarkElement, delayed, modified). |
| `widgetSystem.onMouseDblClickButton` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse dbl click button aus (Parameter: anarkElement, delayed). |
| `widgetSystem.onMouseDblClickCheckBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse dbl click check box aus (Parameter: anarkElement, delayed). |
| `widgetSystem.onMouseDblClickDropDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse dbl click drop down aus (Parameter: anarkElement, delayed). |
| `widgetSystem.onMouseDownButton` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse down button aus (Parameter: anarkElement). |
| `widgetSystem.onMouseDownDropDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse down drop down aus (Parameter: anarkElement). |
| `widgetSystem.onMouseDownDropDownRemoveOption` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse down drop down remove option aus (Parameter: anarkElement). |
| `widgetSystem.onMouseDownEditBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse down edit box aus (Parameter: anarkElement, delayed, modified). |
| `widgetSystem.onMouseDownSliderCell` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse down slider cell aus (Parameter: anarkElement). |
| `widgetSystem.onMouseDownSliderCellArrowLeft` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse down slider cell arrow left aus (Parameter: anarkElement). |
| `widgetSystem.onMouseDownSliderCellArrowRight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse down slider cell arrow right aus (Parameter: anarkElement). |
| `widgetSystem.onMouseDownSliderCellArrowSkipLeft` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse down slider cell arrow skip left aus (Parameter: anarkElement). |
| `widgetSystem.onMouseDownSliderCellArrowSkipRight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse down slider cell arrow skip right aus (Parameter: anarkElement). |
| `widgetSystem.onMouseDownStandardButton` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse down standard button aus (Parameter: type, anarkElement). |
| `widgetSystem.onMouseEmulationActivated` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse emulation activated aus (Parameter: anarkElement). |
| `widgetSystem.onMouseEmulationDeactivated` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse emulation deactivated aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOut` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out aus (Parameter: _, anarkElement). |
| `widgetSystem.onMouseOutBoxText` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out box text aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutButton` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out button aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutCheckBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out check box aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutDropDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out drop down aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutDropDownRemoveOption` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out drop down remove option aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutDropDownScrollBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out drop down scroll bar aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutEditBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out edit box aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutFlowchart` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out flowchart aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutFlowchartNode` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out flowchart node aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutFlowchartNodeSlider` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out flowchart node slider aus (Parameter: anarkElement, elementType, barIndex). |
| `widgetSystem.onMouseOutFlowchartNodeSlider1` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out flowchart node slider1 aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutFlowchartNodeSlider2` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out flowchart node slider2 aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutFlowchartNodeStatusIcon` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out flowchart node status icon aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutFlowchartScrollBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out flowchart scroll bar aus (Parameter: anarkElement, delayed). |
| `widgetSystem.onMouseOutGraphDataPoint` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out graph data point aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutGraphIcon` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out graph icon aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutHelpOverlay` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out help overlay aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutPageScroll` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out page scroll aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutSliderCell` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out slider cell aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutSliderCellArrowLeft` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out slider cell arrow left aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutSliderCellArrowRight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out slider cell arrow right aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutSliderCellArrowSkipLeft` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out slider cell arrow skip left aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutSliderCellArrowSkipRight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out slider cell arrow skip right aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutSliderCellNumber` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out slider cell number aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutStandardButton` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out standard button aus (Parameter: type, anarkElement). |
| `widgetSystem.onMouseOutTable` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out table aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutTableCell` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out table cell aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOutTableScrollBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse out table scroll bar aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOver` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over aus (Parameter: _, _, anarkElement). |
| `widgetSystem.onMouseOverBoxText` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over box text aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverButton` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over button aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverCheckBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over check box aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverDropDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over drop down aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverDropDownRemoveOption` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over drop down remove option aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverDropDownScrollBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over drop down scroll bar aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverEditBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over edit box aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverFlowchart` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over flowchart aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverFlowchartNode` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over flowchart node aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverFlowchartNodeSlider` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over flowchart node slider aus (Parameter: anarkElement, elementType, barIndex). |
| `widgetSystem.onMouseOverFlowchartNodeSlider1` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over flowchart node slider1 aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverFlowchartNodeSlider2` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over flowchart node slider2 aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverFlowchartNodeStatusIcon` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over flowchart node status icon aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverFlowchartScrollBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over flowchart scroll bar aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverGraphDataPoint` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over graph data point aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverGraphIcon` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over graph icon aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverHelpOverlay` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over help overlay aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverPageScroll` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over page scroll aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverSliderCell` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over slider cell aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverSliderCellArrowLeft` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over slider cell arrow left aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverSliderCellArrowRight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over slider cell arrow right aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverSliderCellArrowSkipLeft` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over slider cell arrow skip left aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverSliderCellArrowSkipRight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over slider cell arrow skip right aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverSliderCellNumber` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over slider cell number aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverStandardButton` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over standard button aus (Parameter: type, anarkElement). |
| `widgetSystem.onMouseOverTable` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over table aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverTableCell` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over table cell aus (Parameter: anarkElement). |
| `widgetSystem.onMouseOverTableScrollBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse over table scroll bar aus (Parameter: anarkElement). |
| `widgetSystem.onMouseRenderTarget` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse render target aus (Parameter: event, anarkElement, delayed, modified). |
| `widgetSystem.onMouseStartDropDownScrollBarDrag` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse start drop down scroll bar drag aus (Parameter: anarkElement). |
| `widgetSystem.onMouseStartFlowchartNodeSliderDrag` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse start flowchart node slider drag aus (Parameter: anarkElement, elementType, barIndex). |
| `widgetSystem.onMouseStartFlowchartNodeSliderDrag1` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse start flowchart node slider drag1 aus (Parameter: anarkElement). |
| `widgetSystem.onMouseStartFlowchartNodeSliderDrag2` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse start flowchart node slider drag2 aus (Parameter: anarkElement). |
| `widgetSystem.onMouseStartFlowchartScrollBarDrag` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse start flowchart scroll bar drag aus (Parameter: anarkElement). |
| `widgetSystem.onMouseStartScrollBarDrag` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse start scroll bar drag aus (Parameter: anarkElement). |
| `widgetSystem.onMouseStopDropDownScrollBarDrag` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse stop drop down scroll bar drag aus (Parameter: anarkElement). |
| `widgetSystem.onMouseStopFlowchartNodeSliderDrag` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse stop flowchart node slider drag aus (Parameter: anarkElement, elementType, barIndex). |
| `widgetSystem.onMouseStopFlowchartNodeSliderDrag1` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse stop flowchart node slider drag1 aus (Parameter: anarkElement). |
| `widgetSystem.onMouseStopFlowchartNodeSliderDrag2` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse stop flowchart node slider drag2 aus (Parameter: anarkElement). |
| `widgetSystem.onMouseStopFlowchartScrollBarDrag` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse stop flowchart scroll bar drag aus (Parameter: anarkElement). |
| `widgetSystem.onMouseStopScrollBarDrag` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse stop scroll bar drag aus (Parameter: anarkElement). |
| `widgetSystem.onMouseUpButton` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse up button aus (Parameter: anarkElement). |
| `widgetSystem.onMouseUpDropDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse up drop down aus (Parameter: anarkElement). |
| `widgetSystem.onMouseUpDropDownRemoveOption` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse up drop down remove option aus (Parameter: anarkElement). |
| `widgetSystem.onMouseUpEditBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse up edit box aus (Parameter: anarkElement, delayed, modified). |
| `widgetSystem.onMouseUpSliderCell` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse up slider cell aus (Parameter: anarkElement). |
| `widgetSystem.onMouseUpSliderCellArrowLeft` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse up slider cell arrow left aus (Parameter: anarkElement). |
| `widgetSystem.onMouseUpSliderCellArrowRight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse up slider cell arrow right aus (Parameter: anarkElement). |
| `widgetSystem.onMouseUpSliderCellArrowSkipLeft` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse up slider cell arrow skip left aus (Parameter: anarkElement). |
| `widgetSystem.onMouseUpSliderCellArrowSkipRight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse up slider cell arrow skip right aus (Parameter: anarkElement). |
| `widgetSystem.onMouseUpStandardButton` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on mouse up standard button aus (Parameter: type, anarkElement). |
| `widgetSystem.onMoveDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on move down aus (Parameter: modified, _, widgetID). |
| `widgetSystem.onMoveUp` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on move up aus (Parameter: modified, _, widgetID). |
| `widgetSystem.onPageDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on page down aus (Parameter: _, widgetID). |
| `widgetSystem.onPageUp` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on page up aus (Parameter: _, widgetID). |
| `widgetSystem.onRemoveAllHelpOverlays` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on remove all help overlays aus. |
| `widgetSystem.onRemoveHelpOverlay` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on remove help overlay aus (Parameter: _, id). |
| `widgetSystem.onRightMouseClickButton` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on right mouse click button aus (Parameter: anarkElement, delayed). |
| `widgetSystem.onRightMouseClickEditBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on right mouse click edit box aus (Parameter: anarkElement, delayed). |
| `widgetSystem.onRightMouseClickSliderCell` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on right mouse click slider cell aus (Parameter: anarkElement, delayed). |
| `widgetSystem.onRightMouseClickTableCell` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on right mouse click table cell aus (Parameter: anarkElement, delayed). |
| `widgetSystem.onScrollDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on scroll down aus (Parameter: modified, _, step). |
| `widgetSystem.onScrollUp` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on scroll up aus (Parameter: modified, _, step). |
| `widgetSystem.onSelectAll` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on select all aus. |
| `widgetSystem.onShieldHullBarUpdate` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on shield hull bar update aus (Parameter: _, shieldhullbarid). |
| `widgetSystem.onShowHelpOverlay` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on show help overlay aus (Parameter: _, id). |
| `widgetSystem.onShowHighlightOverlay` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on show highlight overlay aus (Parameter: _, id). |
| `widgetSystem.onSliderCellUpdate` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on slider cell update aus (Parameter: _, slidercellID). |
| `widgetSystem.onSpace` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on space aus (Parameter: modified, _, widgetID). |
| `widgetSystem.onStartInteract` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on start interact aus (Parameter: _, widgetID). |
| `widgetSystem.onStartRemoveNextChar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on start remove next char aus (Parameter: _, widgetID). |
| `widgetSystem.onStartScrollLeft` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on start scroll left aus (Parameter: modified, _, widgetID). |
| `widgetSystem.onStartScrollRight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on start scroll right aus (Parameter: modified, _, widgetID). |
| `widgetSystem.onStartSelect` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on start select aus (Parameter: _, widgetID). |
| `widgetSystem.onStatusBarUpdate` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on status bar update aus (Parameter: _, statusbarid). |
| `widgetSystem.onStopInteract` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on stop interact aus (Parameter: _, widgetID). |
| `widgetSystem.onStopRemoveNextChar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on stop remove next char aus (Parameter: _, widgetID). |
| `widgetSystem.onStopScrollLeft` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on stop scroll left aus (Parameter: modified, _, widgetID). |
| `widgetSystem.onStopScrollRight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on stop scroll right aus (Parameter: modified, _, widgetID). |
| `widgetSystem.onStopSelect` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on stop select aus (Parameter: _, widgetID). |
| `widgetSystem.onTabInteractiveElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on tab interactive element aus. |
| `widgetSystem.onTabScrollLeft` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on tab scroll left aus. |
| `widgetSystem.onTabScrollRight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on tab scroll right aus. |
| `widgetSystem.onTableUpdate` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on table update aus (Parameter: _, tableID). |
| `widgetSystem.onToggleMouseOverText` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on toggle mouse over text aus (Parameter: _, value). |
| `widgetSystem.onUpdateColorMap` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on update color map aus. |
| `widgetSystem.onUpdateScenesDone` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on update scenes done aus. |
| `widgetSystem.onViewClose` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on view close aus. |
| `widgetSystem.onViewRemoved` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt on view removed aus. |
| `widgetSystem.pageDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt page down aus (Parameter: tableID, tableElement). |
| `widgetSystem.pageUp` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt page up aus (Parameter: tableID, tableElement). |
| `widgetSystem.performHorizontalScroll` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt perform horizontal scroll aus (Parameter: step). |
| `widgetSystem.performVerticalScroll` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt perform vertical scroll aus (Parameter: step). |
| `widgetSystem.prepareSize` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt prepare size aus. |
| `widgetSystem.processTableMousePick` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt process table mouse pick aus (Parameter: tableElement). |
| `widgetSystem.queueShapeDraw` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt queue shape draw aus (Parameter: type, ...). |
| `widgetSystem.raiseHideEvent` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt raise hide event aus (Parameter: frame, type). |
| `widgetSystem.refreshFlowchartEdgeData` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt refresh flowchart edge data aus (Parameter: flowchartEdgeID, edge). |
| `widgetSystem.refreshFlowchartNodeData` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt refresh flowchart node data aus (Parameter: flowchartNodeID, node). |
| `widgetSystem.removeFromAssociationList` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Entfernt from association list (Parameter: element). |
| `widgetSystem.removeHelpOverlay` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Entfernt help overlay (Parameter: id). |
| `widgetSystem.removeHelpOverlayID` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Entfernt help overlay id (Parameter: overlayID). |
| `widgetSystem.removeHighlightBorderTableRow` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Entfernt highlight border table row (Parameter: tableElement). |
| `widgetSystem.removeHighlightTableRow` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Entfernt highlight table row (Parameter: tableID, tableElement, highlightrow). |
| `widgetSystem.removeHighlightTableRows` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Entfernt highlight table rows (Parameter: tableID, tableElement, startrow, endrow). |
| `widgetSystem.removeNextEditBoxChar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Entfernt next edit box char (Parameter: editboxID, editboxElement). |
| `widgetSystem.returnElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt return element aus (Parameter: type, element). |
| `widgetSystem.runDeferredElementInitialization` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt run deferred element initialization aus. |
| `widgetSystem.runElementInitializer` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt run element initializer aus (Parameter: element, initdata, count). |
| `widgetSystem.scrollDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt scroll down aus (Parameter: tableID, tableElement, step). |
| `widgetSystem.scrollDownDropDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt scroll down drop down aus (Parameter: dropdownID, dropdownElement, steps). |
| `widgetSystem.scrollDownRenderTarget` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt scroll down render target aus (Parameter: renderTargetID). |
| `widgetSystem.scrollFlowchartHorizontally` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt scroll flowchart horizontally aus (Parameter: flowchartElement, direction, page, step). |
| `widgetSystem.scrollFlowchartVertically` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt scroll flowchart vertically aus (Parameter: flowchartElement, direction, page, step). |
| `widgetSystem.scrollLeft` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt scroll left aus (Parameter: sliderElement, step). |
| `widgetSystem.scrollPageDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt scroll page down aus (Parameter: tableID, tableElement). |
| `widgetSystem.scrollPageUp` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt scroll page up aus (Parameter: tableID, tableElement). |
| `widgetSystem.scrollRight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt scroll right aus (Parameter: sliderElement, step). |
| `widgetSystem.scrollSliderCell` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt scroll slider cell aus. |
| `widgetSystem.scrollUp` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt scroll up aus (Parameter: tableID, tableElement, step). |
| `widgetSystem.scrollUpDropDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt scroll up drop down aus (Parameter: dropdownID, dropdownElement, steps). |
| `widgetSystem.scrollUpRenderTarget` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt scroll up render target aus (Parameter: renderTargetID). |
| `widgetSystem.selectColumn` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Wählt column aus (Parameter: tableID, column). |
| `widgetSystem.selectGraphDataPoint` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Wählt graph data point aus (Parameter: graphID, recordIdx, dataIdx, selected). |
| `widgetSystem.selectInteractiveElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Wählt interactive element aus (Parameter: tableID, tableElement, row, col, alternateCol, direction, modified). |
| `widgetSystem.selectRow` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Wählt row aus (Parameter: tableID, row, modified, input, source). |
| `widgetSystem.selectRowExternal` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Wählt row external aus (Parameter: tableID, row, modified, input, source, settableinteractive). |
| `widgetSystem.selectRowInternal` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Wählt row internal aus (Parameter: tableID, tableElement, row, modified, input, source). |
| `widgetSystem.setActiveFrame` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt active frame (Parameter: frameElement, checked). |
| `widgetSystem.setButtonElementState` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt button element state (Parameter: buttonID, buttonElement, state, value). |
| `widgetSystem.setCheckBoxElementState` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt check box element state (Parameter: checkboxID, checkboxElement, state, value). |
| `widgetSystem.setDropDownElementState` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt drop down element state (Parameter: dropdownID, dropdownElement, state, value). |
| `widgetSystem.setDropDownRemoveOptionColor` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt drop down remove option color (Parameter: dropdownElement, removeOptionElement, colorMode). |
| `widgetSystem.setDropDownRemoveOptionState` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt drop down remove option state (Parameter: dropdownID, removeOptionElement, state, value). |
| `widgetSystem.setEditBoxColors` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt edit box colors (Parameter: editboxID, editboxElement). |
| `widgetSystem.setEditBoxText` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt edit box text (Parameter: editboxElement, text). |
| `widgetSystem.setElementColorAlpha` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt element color alpha (Parameter: anarkMaterial, color). |
| `widgetSystem.setElementPosition` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt element position (Parameter: anarkElement, x, y, xUseHalfPixel, yUseHalfPixel). |
| `widgetSystem.setElementPositionUnchecked` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt element position unchecked (Parameter: anarkElement, x, y). |
| `widgetSystem.setElementRotation` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt element rotation (Parameter: anarkElement, angle). |
| `widgetSystem.setElementScale` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt element scale (Parameter: anarkElement, x, y). |
| `widgetSystem.setElementTextColor` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt element text color (Parameter: anarkTextElement, color). |
| `widgetSystem.setFlowchartNodeSliderState` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt flowchart node slider state (Parameter: flowchartNodeElement, slideridx, state, value). |
| `widgetSystem.setHelpOverlayDisplayed` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt help overlay displayed (Parameter: displayed). |
| `widgetSystem.setHighlightColor` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt highlight color (Parameter: tableElement, row). |
| `widgetSystem.setInteractiveChildElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt interactive child element (Parameter: tableID, tableElement, row, col, childWidgetID, childTableElement). |
| `widgetSystem.setInteractiveElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt interactive element (Parameter: frameID, widgetID, allowregionchange, checked). |
| `widgetSystem.setMouseCursorOverride` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt mouse cursor override (Parameter: cursorIcon). |
| `widgetSystem.setMouseCursorOverrideInternal` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt mouse cursor override internal (Parameter: cursorIcon). |
| `widgetSystem.setMouseCursorOverrideInternalDrag` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt mouse cursor override internal drag (Parameter: cursorIcon). |
| `widgetSystem.setMouseOverOverride` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt mouse over override (Parameter: widgetID, override, forceHide). |
| `widgetSystem.setMouseOverPosition` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt mouse over position. |
| `widgetSystem.setRenderTargetNoise` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt render target noise (Parameter: renderTargetID, active). |
| `widgetSystem.setSceneState` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt scene state (Parameter: state, value). |
| `widgetSystem.setScrollBarState` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt scroll bar state (Parameter: scrollBarElement, state, value, callbackElement). |
| `widgetSystem.setSelectedRows` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt selected rows (Parameter: tableID, rows, curRow). |
| `widgetSystem.setSliderCellArrowState` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt slider cell arrow state (Parameter: slidercellID, leftRight, state, value). |
| `widgetSystem.setSliderCellCurValue` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt slider cell cur value (Parameter: slidercellElement, value, exceedmaxallowed, allowupdate, keepmaxfactor). |
| `widgetSystem.setSliderCellValue` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt slider cell value (Parameter: slidercellID, value, newmaxselect). |
| `widgetSystem.setStandardButtonState` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt standard button state (Parameter: frameID, frameElement, button, state, value). |
| `widgetSystem.setTableMousePickState` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt table mouse pick state (Parameter: table, tableElement, state, value, row). |
| `widgetSystem.setTableRowColor` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt table row color (Parameter: tableID, tableElement, row, col, rowcoloroverride, useRowColor). |
| `widgetSystem.setTopRow` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt top row (Parameter: tableID, row). |
| `widgetSystem.setUpBoxText` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up box text (Parameter: boxtextID, boxtextElement, parentx, parenty, parentwidth, parentHeight, parentBGWidth, isPrevColBGSpanned, isColBGSpanned). |
| `widgetSystem.setUpButton` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up button (Parameter: frameElement, buttonID, buttonElement, isSelected, parentx, parenty, parentwidth, parentheight, backgroundcolspanwidth). |
| `widgetSystem.setUpCheckBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up check box (Parameter: frameElement, checkboxID, checkboxElement, isSelected, parentx, parenty, parentwidth, parentheight, backgroundcolspanwidth). |
| `widgetSystem.setUpDataPointLine` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up data point line (Parameter: dataRecord, data, dataPointElement, diffX, diffY). |
| `widgetSystem.setUpDataPointMarker` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up data point marker (Parameter: dataRecord, dataPointElement, data). |
| `widgetSystem.setUpDropDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up drop down (Parameter: frameElement, dropdownID, dropdownElement, isSelected, parentx, parenty, parentwidth, parentheight, backgroundcolspanwidth). |
| `widgetSystem.setUpEditBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up edit box (Parameter: frameElement, editboxID, editboxElement, parentx, parenty, parentwidth, parentheight, backgroundcolspanwidth). |
| `widgetSystem.setUpFlowchart` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up flowchart (Parameter: frameElement, flowchartID, flowchartElement). |
| `widgetSystem.setUpFontString` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up font string (Parameter: fontstringID, textcomponent, textelement, activeSlide, inactiveSlide, parentx, parenty, parentwidth, parentXSubpixel, parentYSubpixel, frameElement, realparentx, realparenty, backgroundcolspanwidth). |
| `widgetSystem.setUpGraph` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up graph (Parameter: graphID, graphElement, parentx, parenty, parentwidth, parentheight, frameElement, backgroundcolspanwidth). |
| `widgetSystem.setUpGraphAxis` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up graph axis (Parameter: graphID, axisElement, accessor, axisData). |
| `widgetSystem.setUpHorizontalScrollBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up horizontal scroll bar (Parameter: scrollBar, posx, posy, scrollbarWidth, visibleParentWidth, fullParentWidth). |
| `widgetSystem.setUpIcon` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up icon (Parameter: frameElement, iconID, iconelement, cellelement, parentx, parenty, parentwidth, backgroundcolspanwidth). |
| `widgetSystem.setUpRenderTarget` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up render target (Parameter: frameElement, renderTargetID, renderTargetElement). |
| `widgetSystem.setUpShieldHullBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up shield hull bar (Parameter: shieldHullBarID, shieldHullBarElement, cellElement, parentx, parenty, parentwidth, parentheight). |
| `widgetSystem.setUpSliderCell` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up slider cell (Parameter: frameElement, slidercellID, slidercellElement, parentx, parenty, parentwidth, parentheight, backgroundcolspanwidth). |
| `widgetSystem.setUpStandardButtons` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up standard buttons (Parameter: frameID, frameElement). |
| `widgetSystem.setUpStatusBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up status bar (Parameter: statusBarID, statusBarElement, cellElement, parentx, parenty, parentwidth, parentheight, istitle). |
| `widgetSystem.setUpTable` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up table (Parameter: frameElement, tableID, tableElement). |
| `widgetSystem.setUpVerticalScrollBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Setzt up vertical scroll bar (Parameter: scrollBar, posx, posy, scrollbarHeight, visibleParentHeight, fullParentHeight). |
| `widgetSystem.showDropDownOptions` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeigt drop down options (Parameter: frameElement, dropdownID, dropdownElement). |
| `widgetSystem.showFlowchartJunction` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeigt flowchart junction (Parameter: frameElement, flowchartNodeID, flowchartNodeElement, x, y, xUseHalfPixel, yUseHalfPixel). |
| `widgetSystem.showFlowchartNode` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeigt flowchart node (Parameter: frameElement, flowchartNodeID, flowchartNodeElement, x, y, cellwidth, cellheight). |
| `widgetSystem.showHelpOverlay` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeigt help overlay. |
| `widgetSystem.showHelpOverlayID` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeigt help overlay id (Parameter: id, borderonly). |
| `widgetSystem.showHighlightOverlay` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeigt highlight overlay (Parameter: id). |
| `widgetSystem.showMinimizedMenuName` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeigt minimized menu name (Parameter: frameElement, text). |
| `widgetSystem.showMouseOverText` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Zeigt mouse over text (Parameter: widgetID, ignorecount, posOverride). |
| `widgetSystem.startDropDownScrollBarDrag` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Startet drop down scroll bar drag (Parameter: dropdownID, dropdownElement). |
| `widgetSystem.startFlowchartNodeSliderDrag` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Startet flowchart node slider drag (Parameter: flowchartNodeElement, slideridx). |
| `widgetSystem.startFlowchartScrollBarDrag` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Startet flowchart scroll bar drag (Parameter: flowchartElement, scrollbar). |
| `widgetSystem.startScrollBarDrag` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Startet scroll bar drag (Parameter: tableElement). |
| `widgetSystem.startScrollLeft` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Startet scroll left (Parameter: scrollingElement). |
| `widgetSystem.startScrollRight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Startet scroll right (Parameter: scrollingElement). |
| `widgetSystem.startSliderCellScroll` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Startet slider cell scroll (Parameter: slidercellElement, direction). |
| `widgetSystem.stopDropDownScrollBarDrag` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Stoppt drop down scroll bar drag (Parameter: dropdownID, dropdownElement). |
| `widgetSystem.stopFlowchartNodeSliderDrag` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Stoppt flowchart node slider drag (Parameter: flowchartNodeElement, slideridx). |
| `widgetSystem.stopFlowchartScrollBarDrag` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Stoppt flowchart scroll bar drag (Parameter: flowchartElement, scrollbar). |
| `widgetSystem.stopLeft` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Stoppt left (Parameter: tableID, tableElement). |
| `widgetSystem.stopRight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Stoppt right (Parameter: tableID, tableElement). |
| `widgetSystem.stopScroll` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Stoppt scroll. |
| `widgetSystem.stopScrollBarDrag` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Stoppt scroll bar drag (Parameter: tableElement). |
| `widgetSystem.stopSliderCellScroll` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Stoppt slider cell scroll (Parameter: slidercellElement). |
| `widgetSystem.summarize` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt summarize aus (Parameter: array). |
| `widgetSystem.swapButtonIcon` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt swap button icon aus (Parameter: buttonID, buttonElement). |
| `widgetSystem.swapButtonIcon2` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt swap button icon2 aus (Parameter: buttonID, buttonElement). |
| `widgetSystem.swapInteractiveRegion` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt swap interactive region aus (Parameter: tableID, tableElement). |
| `widgetSystem.switchFromMiniWidgetSystem` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt switch from mini widget system aus. |
| `widgetSystem.switchToMiniWidgetSystem` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt switch to mini widget system aus. |
| `widgetSystem.toggleCheckBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Schaltet check box um (Parameter: checkboxID, checkboxElement). |
| `widgetSystem.toggleHelpOverlay` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Schaltet help overlay um. |
| `widgetSystem.toggleHighlight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Schaltet highlight um (Parameter: tableID, tableElement, modified, input, source). |
| `widgetSystem.toggleHighlightedTableRow` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Schaltet highlighted table row um (Parameter: tableID, tableElement). |
| `widgetSystem.toggleMouseOverText` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Schaltet mouse over text um (Parameter: value). |
| `widgetSystem.truncateDropDownOptionText` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt truncate drop down option text aus (Parameter: dropdownElement, option). |
| `widgetSystem.unsetInteractiveChildElement` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Führt unset interactive child element aus (Parameter: tableElement, childWidgetID, childTableElement). |
| `widgetSystem.updateBoxText` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert box text (Parameter: boxtextID, boxtextElement). |
| `widgetSystem.updateButton` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert button (Parameter: buttonID, buttonElement). |
| `widgetSystem.updateButtonColor` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert button color (Parameter: buttonID, buttonElement, colorMode). |
| `widgetSystem.updateButtonState` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert button state (Parameter: buttonID, buttonElement). |
| `widgetSystem.updateCheckBox` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert check box (Parameter: checkboxID, checkboxElement). |
| `widgetSystem.updateCheckBoxColor` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert check box color (Parameter: checkbox, checkboxElement, colorMode). |
| `widgetSystem.updateCheckBoxState` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert check box state (Parameter: checkbox, checkboxElement). |
| `widgetSystem.updateDropDown` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert drop down (Parameter: dropdownID, dropdownElement). |
| `widgetSystem.updateDropDownColor` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert drop down color (Parameter: dropdownID, dropdownElement, colorMode). |
| `widgetSystem.updateDropDownOption` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert drop down option (Parameter: dropdownElement). |
| `widgetSystem.updateDropDownOptionState` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert drop down option state (Parameter: dropdownElement, oldhighlighted). |
| `widgetSystem.updateDropDownOptions` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert drop down options (Parameter: frameElement, dropdownID, dropdownElement, topOption, force). |
| `widgetSystem.updateDropDownScrollBarPos` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert drop down scroll bar pos (Parameter: dropdownID, dropdownElement). |
| `widgetSystem.updateDropDownState` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert drop down state (Parameter: dropdownID, dropdownElement). |
| `widgetSystem.updateEditBoxColor` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert edit box color (Parameter: editboxID, editboxElement, highlighted). |
| `widgetSystem.updateEditBoxCursor` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert edit box cursor (Parameter: editboxElement, curTime, scrolling). |
| `widgetSystem.updateEditBoxCursorPosition` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert edit box cursor position (Parameter: editboxElement). |
| `widgetSystem.updateEditBoxTextDisplay` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert edit box text display (Parameter: editboxElement). |
| `widgetSystem.updateEditBoxTextHighlight` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert edit box text highlight (Parameter: editboxElement). |
| `widgetSystem.updateEmulatedMouseCursorPosition` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert emulated mouse cursor position (Parameter: tableID, tableElement, row, col). |
| `widgetSystem.updateFlowchart` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert flowchart (Parameter: flowchartElement). |
| `widgetSystem.updateFlowchartEdge` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert flowchart edge (Parameter: flowchartEdgeID, edge). |
| `widgetSystem.updateFlowchartNode` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert flowchart node (Parameter: flowchartNodeID, flowchartNodeElement). |
| `widgetSystem.updateFlowchartNodeSliderColor` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert flowchart node slider color (Parameter: flowchartNodeElement, slideridx). |
| `widgetSystem.updateFlowchartNodeSliderPos` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert flowchart node slider pos. |
| `widgetSystem.updateFlowchartScrollBarPos` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert flowchart scroll bar pos (Parameter: flowchartElement, scrollbar). |
| `widgetSystem.updateFlowchartScrollBars` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert flowchart scroll bars (Parameter: flowchartElement). |
| `widgetSystem.updateFontString` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert font string (Parameter: fontstringID, textcomponent, textelement, activeSlide, inactiveSlide, curSlide). |
| `widgetSystem.updateFrame` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert frame (Parameter: frameID). |
| `widgetSystem.updateHelpOverlay` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert help overlay (Parameter: helpOverlayElement, overlayinfo). |
| `widgetSystem.updateHelpOverlayColor` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert help overlay color (Parameter: helpOverlayElement, highlight, iconsize, borderonly, curtime). |
| `widgetSystem.updateHelpStandardButton` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert help standard button. |
| `widgetSystem.updateHorizontalScrollBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert horizontal scroll bar (Parameter: scrollBar, relativePos). |
| `widgetSystem.updateIcon` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert icon (Parameter: iconID, iconelement, parentx, parenty, parentwidth). |
| `widgetSystem.updateMouseOverText` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert mouse over text (Parameter: widgetID). |
| `widgetSystem.updateSceneState` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert scene state. |
| `widgetSystem.updateScrollBarPos` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert scroll bar pos (Parameter: tableElement). |
| `widgetSystem.updateShapes` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert shapes. |
| `widgetSystem.updateShieldHullBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert shield hull bar (Parameter: shieldHullBarElement, shieldHullBarID). |
| `widgetSystem.updateSliderCellArrowSlide` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert slider cell arrow slide (Parameter: slidercellElement, leftRight). |
| `widgetSystem.updateSliderCellBackground` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert slider cell background (Parameter: slidercellElement). |
| `widgetSystem.updateSliderCellCursor` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert slider cell cursor (Parameter: slidercellElement, curTime). |
| `widgetSystem.updateSliderCellValue` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert slider cell value (Parameter: slidercellElement). |
| `widgetSystem.updateStandardButtonState` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert standard button state (Parameter: frameElement, button). |
| `widgetSystem.updateStatusBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert status bar (Parameter: statusBarElement, statusBarID). |
| `widgetSystem.updateTable` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert table (Parameter: tableID, tableElement, shiftRows, newRow, modified). |
| `widgetSystem.updateVerticalScrollBar` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert vertical scroll bar (Parameter: scrollBar, relativePos). |
| `widgetSystem.updateView` | 1 | `08/ui/widget/lua/widget_fullscreen.lua` | Aktualisiert view. |
