# CardRequestExtensions.SetRows - метод
Устанавливает строки коллекционной или древовидной секции в ответе на
универсальный запрос к карточке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetRows(
    	this CardResponse response,
    	ListStorage<CardRow> rows
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetRows ( 
    	response As CardResponse,
    	rows As ListStorage(Of CardRow)
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetRows(
    	CardResponse^ response, 
    	ListStorage<CardRow^>^ rows
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetRows : 
            response : CardResponse * 
            rows : ListStorage<CardRow> -> unit 
#### Параметры
response [CardResponse](T_Tessa_Cards_CardResponse.htm)
    Ответ на универсальный запрос к карточке.
rows
[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[CardRow](T_Tessa_Cards_CardRow.htm)>
     Строки коллекционной или древовидной секции, которые требуется установить в ответе на универсальный запрос к карточке. 
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
