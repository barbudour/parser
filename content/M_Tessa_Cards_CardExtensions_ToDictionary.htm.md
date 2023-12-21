# CardExtensions.ToDictionary - метод
Создаёт хеш-таблицу, позволяющую быстро получить доступ к строкам
коллекционных и древовидных секций по имени секции. Строки
[CardRow](T_Tessa_Cards_CardRow.htm) не копируются.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Dictionary<string, CardRow> ToDictionary(
    	this IDictionary<string, CardRow> sectionRows
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ToDictionary ( 
    	sectionRows As IDictionary(Of String, CardRow)
    ) As Dictionary(Of String, CardRow)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Dictionary<String^, CardRow^>^ ToDictionary(
    	IDictionary<String^, CardRow^>^ sectionRows
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ToDictionary : 
            sectionRows : IDictionary<string, CardRow> -> Dictionary<string, CardRow> 
#### Параметры
sectionRows
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[CardRow](T_Tessa_Cards_CardRow.htm)>
    Строки коллекционных и древовидных секций, доступные по имени секции.
#### Возвращаемое значение
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[CardRow](T_Tessa_Cards_CardRow.htm)>  
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
