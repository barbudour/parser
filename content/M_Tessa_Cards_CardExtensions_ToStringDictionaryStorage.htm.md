# CardExtensions.ToStringDictionaryStorage - метод
Создаёт объект StringDictionaryStorage<CardRow> по заданной хеш-таблице,
позволяющей получить доступ к строкам коллекционных и древовидных секций по
имени секции. Строки [CardRow](T_Tessa_Cards_CardRow.htm) копируются.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static StringDictionaryStorage<CardRow> ToStringDictionaryStorage(
    	this IDictionary<string, CardRow> rowsBySectionName
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ToStringDictionaryStorage ( 
    	rowsBySectionName As IDictionary(Of String, CardRow)
    ) As StringDictionaryStorage(Of CardRow)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static StringDictionaryStorage<CardRow^>^ ToStringDictionaryStorage(
    	IDictionary<String^, CardRow^>^ rowsBySectionName
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ToStringDictionaryStorage : 
            rowsBySectionName : IDictionary<string, CardRow> -> StringDictionaryStorage<CardRow> 
#### Параметры
rowsBySectionName
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[CardRow](T_Tessa_Cards_CardRow.htm)>
    Строки коллекционных и древовидных секций, доступные по имени секции.
#### Возвращаемое значение
[StringDictionaryStorage](T_Tessa_Platform_Storage_StringDictionaryStorage_1.htm)<[CardRow](T_Tessa_Cards_CardRow.htm)>  
Созданный объект.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[CardRow](T_Tessa_Cards_CardRow.htm)>. При вызове метода для экземпляра
следует опускать первый параметр. Дополнительные сведения см. в разделе
[Методы расширения (Visual Basic)](https://docs.microsoft.com/dotnet/visual-
basic/programming-guide/language-features/procedures/extension-methods) или
[Методы расширения (Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
