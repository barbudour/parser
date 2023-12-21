# CardExtensions.GetOrAddTable(StringDictionaryStorage<CardSection>, String,
CardTableType) - метод
Возвращает коллекционную или древовидную секцию с заданным именем. Если секция
отсутствовала, то создаёт её. Если требуется создать строковую секцию, то
используйте метод GetOrAddEntry.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardSection GetOrAddTable(
    	this StringDictionaryStorage<CardSection> sections,
    	string sectionName,
    	CardTableType tableType = CardTableType.Collection
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetOrAddTable ( 
    	sections As StringDictionaryStorage(Of CardSection),
    	sectionName As String,
    	Optional tableType As CardTableType = CardTableType.Collection
    ) As CardSection
C++ __Копировать
     public:
    [ExtensionAttribute]
    static CardSection^ GetOrAddTable(
    	StringDictionaryStorage<CardSection^>^ sections, 
    	String^ sectionName, 
    	CardTableType tableType = CardTableType::Collection
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetOrAddTable : 
            sections : StringDictionaryStorage<CardSection> * 
            sectionName : string * 
            ?tableType : CardTableType 
    (* Defaults:
            let _tableType = defaultArg tableType CardTableType.Collection
    *)
    -> CardSection 
#### Параметры
sections
[StringDictionaryStorage](T_Tessa_Platform_Storage_StringDictionaryStorage_1.htm)<[CardSection](T_Tessa_Cards_CardSection.htm)>
    Секции карточки.
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции. Не должно быть равно null.
tableType [CardTableType](T_Tessa_Cards_CardTableType.htm) (Optional)
    Тип коллекционной или древовидной секции.
#### Возвращаемое значение
[CardSection](T_Tessa_Cards_CardSection.htm)  
Секция карточки с заданными параметрами, которая была получена или создана.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[StringDictionaryStorage](T_Tessa_Platform_Storage_StringDictionaryStorage_1.htm)<[CardSection](T_Tessa_Cards_CardSection.htm)>.
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
[GetOrAddTable -
перегрузка](Overload_Tessa_Cards_CardExtensions_GetOrAddTable.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
