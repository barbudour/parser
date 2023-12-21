# CardRequestExtensions.SetForbidStoringHistory(CardGetResponse, Boolean) -
метод
Устанавливает запрет на сохранение данных о загруженной карточке в историю
действий с карточкой.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetForbidStoringHistory(
    	this CardGetResponse response,
    	bool forbidStoringHistory
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetForbidStoringHistory ( 
    	response As CardGetResponse,
    	forbidStoringHistory As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetForbidStoringHistory(
    	CardGetResponse^ response, 
    	bool forbidStoringHistory
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetForbidStoringHistory : 
            response : CardGetResponse * 
            forbidStoringHistory : bool -> unit 
#### Параметры
response [CardGetResponse](T_Tessa_Cards_CardGetResponse.htm)
    Ответ на запрос к сервису карточек на получение карточки.
forbidStoringHistory
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Запрет на сохранение данных о загруженной карточке в историю действий с карточкой. 
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardGetResponse](T_Tessa_Cards_CardGetResponse.htm). При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
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
