# CardRequestExtensions.TryGetSectionRows - метод
Возвращает пустые строки коллекционных и древовидных секций, заданные в ответе
на универсальный запрос к карточке, или null, если строки не были заданы.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static StringDictionaryStorage<CardRow> TryGetSectionRows(
    	this CardResponse response
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetSectionRows ( 
    	response As CardResponse
    ) As StringDictionaryStorage(Of CardRow)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static StringDictionaryStorage<CardRow^>^ TryGetSectionRows(
    	CardResponse^ response
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetSectionRows : 
            response : CardResponse -> StringDictionaryStorage<CardRow> 
#### Параметры
response [CardResponse](T_Tessa_Cards_CardResponse.htm)
    Ответ на универсальный запрос к карточке.
#### Возвращаемое значение
[StringDictionaryStorage](T_Tessa_Platform_Storage_StringDictionaryStorage_1.htm)<[CardRow](T_Tessa_Cards_CardRow.htm)>  
Пустые строки коллекционных и древовидных секций, заданные в ответе на
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
