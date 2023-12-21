# CardRequestExtensions.SetForbidStoringHistory(CardGetFileContentRequest,
Boolean) - метод
Устанавливает запрет на сохранение данных о загружаемом файле карточки в
историю действий с карточкой. Вызов метода в клиентских расширениях запрещён,
это приведёт к ошибке
[RequestFromClientCheckFailed](F_Tessa_Cards_CardValidationKeys_RequestFromClientCheckFailed.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetForbidStoringHistory(
    	this CardGetFileContentRequest request,
    	bool forbidStoringHistory
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetForbidStoringHistory ( 
    	request As CardGetFileContentRequest,
    	forbidStoringHistory As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetForbidStoringHistory(
    	CardGetFileContentRequest^ request, 
    	bool forbidStoringHistory
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetForbidStoringHistory : 
            request : CardGetFileContentRequest * 
            forbidStoringHistory : bool -> unit 
#### Параметры
request
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm)
    Запрос к сервису карточек на загрузку контента файла карточки.
forbidStoringHistory
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Запрет на сохранение данных о загружаемом файле карточки в историю действий с карточкой. 
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[SetForbidStoringHistory -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_SetForbidStoringHistory.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
