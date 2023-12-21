# CardExtensions.GetOrAddEntry(StringDictionaryStorage<CardSection>, String) -
метод
Возвращает строковую секцию с заданным именем. Если секция отсутствовала, то
создаёт её. Если требуется создать коллекционную или древовидную секцию, то
используйте метод GetOrAddTable.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardSection GetOrAddEntry(
    	this StringDictionaryStorage<CardSection> sections,
    	string sectionName
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetOrAddEntry ( 
    	sections As StringDictionaryStorage(Of CardSection),
    	sectionName As String
    ) As CardSection
C++ __Копировать
     public:
    [ExtensionAttribute]
    static CardSection^ GetOrAddEntry(
    	StringDictionaryStorage<CardSection^>^ sections, 
    	String^ sectionName
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetOrAddEntry : 
            sections : StringDictionaryStorage<CardSection> * 
            sectionName : string -> CardSection 
#### Параметры
sections
[StringDictionaryStorage](T_Tessa_Platform_Storage_StringDictionaryStorage_1.htm)<[CardSection](T_Tessa_Cards_CardSection.htm)>
    Секции карточки.
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции. Не должно быть равно null.
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
[GetOrAddEntry -
перегрузка](Overload_Tessa_Cards_CardExtensions_GetOrAddEntry.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
