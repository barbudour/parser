# CardTaskDialogUIExtension.OnDialogButtonPressedKey - поле
Ключ, по которому в [Info](P_Tessa_UI_Cards_ICardEditorModel_Info.htm)
содержится функция, выполняемая при нажатии на кнопку в диалоге, отправляющей
запрос на сервер ([Cancel](P_Tessa_Cards_CardTaskDialogButtonInfo_Cancel.htm)
= false). Тип значения:
Func<[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm),
[CardTaskCompletionOptionSettings](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm),
[String](https://learn.microsoft.com/dotnet/api/system.string)?,
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI](N_Tessa_Extensions_Platform_Client_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public const string OnDialogButtonPressedKey = ".CardEditorCompletionOptionSettingsOnButtonPressed"
VB __Копировать
     Public Const OnDialogButtonPressedKey As String = ".CardEditorCompletionOptionSettingsOnButtonPressed"
C++ __Копировать
     public:
    literal String^ OnDialogButtonPressedKey = ".CardEditorCompletionOptionSettingsOnButtonPressed"
F# __Копировать
     static val mutable OnDialogButtonPressedKey: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[CardTaskDialogUIExtension -
](T_Tessa_Extensions_Platform_Client_UI_CardTaskDialogUIExtension.htm)
[Tessa.Extensions.Platform.Client.UI - пространство
имён](N_Tessa_Extensions_Platform_Client_UI.htm)
