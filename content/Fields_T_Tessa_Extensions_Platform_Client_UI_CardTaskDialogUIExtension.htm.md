# CardTaskDialogUIExtension - поля
##  __Поля
[DialogNonTaskCompletionOptionSettingsKey](F_Tessa_Extensions_Platform_Client_UI_CardTaskDialogUIExtension_DialogNonTaskCompletionOptionSettingsKey.htm)|
Ключ, по которому в [Info](P_Tessa_UI_Cards_ICardEditorModel_Info.htm)
содержатся параметры диалога, переопределяющие параметры заданные в задании
диалога. Тип значения:
[CardTaskCompletionOptionSettings](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm).  
---|---  
[OnDialogButtonPressedKey](F_Tessa_Extensions_Platform_Client_UI_CardTaskDialogUIExtension_OnDialogButtonPressedKey.htm)|
Ключ, по которому в [Info](P_Tessa_UI_Cards_ICardEditorModel_Info.htm)
содержится функция, выполняемая при нажатии на кнопку в диалоге, отправляющей
запрос на сервер ([Cancel](P_Tessa_Cards_CardTaskDialogButtonInfo_Cancel.htm)
= false). Тип значения:
Func<[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm),
[CardTaskCompletionOptionSettings](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm),
[String](https://learn.microsoft.com/dotnet/api/system.string)?,
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>.  
## __См. также
#### Ссылки
[CardTaskDialogUIExtension -
](T_Tessa_Extensions_Platform_Client_UI_CardTaskDialogUIExtension.htm)
[Tessa.Extensions.Platform.Client.UI - пространство
имён](N_Tessa_Extensions_Platform_Client_UI.htm)
