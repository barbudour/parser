# CardRequestExtensions.HasTypeIDList - метод
Возвращает признак того, что список идентификаторов типов карточек был
установлен в ответе на запрос к сервису карточек
[CardResponse](T_Tessa_Cards_CardResponse.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool HasTypeIDList(
    	this CardResponse response
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function HasTypeIDList ( 
    	response As CardResponse
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool HasTypeIDList(
    	CardResponse^ response
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member HasTypeIDList : 
            response : CardResponse -> bool 
#### Параметры
response [CardResponse](T_Tessa_Cards_CardResponse.htm)
    Ответ на запрос к сервису карточек.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что список идентификаторов типов карточек был установлен в
ответе на запрос к сервису карточек.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardResponse](T_Tessa_Cards_CardResponse.htm). При вызове метода
для экземпляра следует опускать первый параметр. Дополнительные сведения см. в
разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
