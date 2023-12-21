# CardRequestExtensions.TryGetRows - метод
Возвращает строки коллекционной или древовидной секции, заданные в ответе на
универсальный запрос к карточке, или null, если строки не были заданы.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ListStorage<CardRow> TryGetRows(
    	this CardResponse response
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetRows ( 
    	response As CardResponse
    ) As ListStorage(Of CardRow)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static ListStorage<CardRow^>^ TryGetRows(
    	CardResponse^ response
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetRows : 
            response : CardResponse -> ListStorage<CardRow> 
#### Параметры
response [CardResponse](T_Tessa_Cards_CardResponse.htm)
    Ответ на универсальный запрос к карточке.
#### Возвращаемое значение
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardRow](T_Tessa_Cards_CardRow.htm)>  
Строки коллекционной или древовидной секции, заданные в ответе на
универсальный запрос к карточке, или null, если строки не были заданы.
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
