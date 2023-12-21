# CardRequestExtensions.GetForbidStoringHistory(CardGetRequest) - метод
Возвращает запрет на сохранение данных о загружаемой карточке в историю
действий с карточкой.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool GetForbidStoringHistory(
    	this CardGetRequest request
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetForbidStoringHistory ( 
    	request As CardGetRequest
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool GetForbidStoringHistory(
    	CardGetRequest^ request
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetForbidStoringHistory : 
            request : CardGetRequest -> bool 
#### Параметры
request [CardGetRequest](T_Tessa_Cards_CardGetRequest.htm)
    Запрос к сервису карточек на загрузку карточки.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Запрет на сохранение данных о загружаемой карточке в историю действий с
карточкой или null, если признак запрета не был установлен.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardGetRequest](T_Tessa_Cards_CardGetRequest.htm). При вызове
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
[GetForbidStoringHistory -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_GetForbidStoringHistory.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
