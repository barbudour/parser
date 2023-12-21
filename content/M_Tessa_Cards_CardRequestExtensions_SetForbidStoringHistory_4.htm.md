# CardRequestExtensions.SetForbidStoringHistory(CardStoreRequest, Boolean) -
метод
Устанавливает запрет на сохранение данных о сохраняемой карточке в историю
действий с карточкой. Вызов метода в клиентских расширениях запрещён, это
приведёт к ошибке
[RequestFromClientCheckFailed](F_Tessa_Cards_CardValidationKeys_RequestFromClientCheckFailed.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetForbidStoringHistory(
    	this CardStoreRequest request,
    	bool forbidStoringHistory
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetForbidStoringHistory ( 
    	request As CardStoreRequest,
    	forbidStoringHistory As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetForbidStoringHistory(
    	CardStoreRequest^ request, 
    	bool forbidStoringHistory
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetForbidStoringHistory : 
            request : CardStoreRequest * 
            forbidStoringHistory : bool -> unit 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос к сервису карточек на сохранение карточки.
forbidStoringHistory
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Запрет на сохранение данных о сохраняемой карточке в историю действий с карточкой. 
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm). При
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
