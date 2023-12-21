# CardRequestExtensions.SetSectionRows - метод
Устанавливает пустые строки коллекционных и древовидных секций в ответе на
универсальный запрос к карточке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetSectionRows(
    	this CardResponse response,
    	StringDictionaryStorage<CardRow> sectionRows
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetSectionRows ( 
    	response As CardResponse,
    	sectionRows As StringDictionaryStorage(Of CardRow)
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetSectionRows(
    	CardResponse^ response, 
    	StringDictionaryStorage<CardRow^>^ sectionRows
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetSectionRows : 
            response : CardResponse * 
            sectionRows : StringDictionaryStorage<CardRow> -> unit 
#### Параметры
response [CardResponse](T_Tessa_Cards_CardResponse.htm)
    Ответ на универсальный запрос к карточке.
sectionRows
[StringDictionaryStorage](T_Tessa_Platform_Storage_StringDictionaryStorage_1.htm)<[CardRow](T_Tessa_Cards_CardRow.htm)>
     Пустые строки коллекционных и древовидных секций, которые требуется установить в ответе на универсальный запрос к карточке. Если равен null, то информация удаляется. 
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
