# ClipboardSafe - класс
Методы для работы с буфером обмена
[Clipboard](https://learn.microsoft.com/dotnet/api/system.windows.clipboard),
безопасные для исключений от COM.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ClipboardSafe
VB __Копировать
     Public NotInheritable Class ClipboardSafe
C++ __Копировать
     public ref class ClipboardSafe abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ClipboardSafe = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ClipboardSafe
##  __Заметки
Например, COM может выбрасывать исключение, когда другое приложение, такое как
RDP, заблокировало буфер обмена и удерживает его. Чтобы приложение не
отображало ошибок в таких случаях, рекомендуется использовать этот метод.
## __Методы
[Clear](M_Tessa_UI_ClipboardSafe_Clear.htm)|  
---|---  
[ClearAndSetData](M_Tessa_UI_ClipboardSafe_ClearAndSetData.htm)|  
[CreateDataObject](M_Tessa_UI_ClipboardSafe_CreateDataObject.htm)|  
[SetData](M_Tessa_UI_ClipboardSafe_SetData.htm)|  
[SetDataObject(Object)](M_Tessa_UI_ClipboardSafe_SetDataObject.htm)|  
[SetDataObject(Object,
Boolean)](M_Tessa_UI_ClipboardSafe_SetDataObject_1.htm)|  
[SetFileDropList](M_Tessa_UI_ClipboardSafe_SetFileDropList.htm)|  
[SetHtml](M_Tessa_UI_ClipboardSafe_SetHtml.htm)|  
[SetLink](M_Tessa_UI_ClipboardSafe_SetLink.htm)|  
[SetText(String)](M_Tessa_UI_ClipboardSafe_SetText.htm)|  
[SetText(String, TextDataFormat)](M_Tessa_UI_ClipboardSafe_SetText_1.htm)|  
[TryGetData](M_Tessa_UI_ClipboardSafe_TryGetData.htm)|  
[TryGetDataObject](M_Tessa_UI_ClipboardSafe_TryGetDataObject.htm)|  
## __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
