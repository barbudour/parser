# CardExtensions.TryGetIgnoreCase(CardMetadataColumnCollection, String,
Boolean) - метод
Возвращает колонку из метаинформации, полученную без учёта регистра, или null,
если такая колонка отсутствует.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardMetadataColumn TryGetIgnoreCase(
    	this CardMetadataColumnCollection columns,
    	string columnName,
    	bool physicalColumnOnly = false
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetIgnoreCase ( 
    	columns As CardMetadataColumnCollection,
    	columnName As String,
    	Optional physicalColumnOnly As Boolean = false
    ) As CardMetadataColumn
C++ __Копировать
     public:
    [ExtensionAttribute]
    static CardMetadataColumn^ TryGetIgnoreCase(
    	CardMetadataColumnCollection^ columns, 
    	String^ columnName, 
    	bool physicalColumnOnly = false
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetIgnoreCase : 
            columns : CardMetadataColumnCollection * 
            columnName : string * 
            ?physicalColumnOnly : bool 
    (* Defaults:
            let _physicalColumnOnly = defaultArg physicalColumnOnly false
    *)
    -> CardMetadataColumn 
#### Параметры
columns
[CardMetadataColumnCollection](T_Tessa_Cards_Metadata_CardMetadataColumnCollection.htm)
    Коллекция колонок в метаинформации.
columnName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя колонки без учёта регистра.
physicalColumnOnly
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
    Признак того, что проверяются только физические колонки.
#### Возвращаемое значение
[CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)  
Колонка из метаинформации, полученная без учёта регистра, или null, если такая
колонка отсутствует.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[CardMetadataColumnCollection](T_Tessa_Cards_Metadata_CardMetadataColumnCollection.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[TryGetIgnoreCase -
перегрузка](Overload_Tessa_Cards_CardExtensions_TryGetIgnoreCase.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
