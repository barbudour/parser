#
CardExtensions.GetOrAddTable(StringDictionaryStorage<CardSectionPermissionInfo>,
String) - метод
Возвращает объект с разрешениями на коллекционную или древовидную секцию с
заданным именем. Если секция отсутствовала, то создаёт её. Если требуется
создать объект для строковой секции, то используйте метод GetOrAddEntry.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardSectionPermissionInfo GetOrAddTable(
    	this StringDictionaryStorage<CardSectionPermissionInfo> sections,
    	string sectionName
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetOrAddTable ( 
    	sections As StringDictionaryStorage(Of CardSectionPermissionInfo),
    	sectionName As String
    ) As CardSectionPermissionInfo
C++ __Копировать
     public:
    [ExtensionAttribute]
    static CardSectionPermissionInfo^ GetOrAddTable(
    	StringDictionaryStorage<CardSectionPermissionInfo^>^ sections, 
    	String^ sectionName
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetOrAddTable : 
            sections : StringDictionaryStorage<CardSectionPermissionInfo> * 
            sectionName : string -> CardSectionPermissionInfo 
#### Параметры
sections
[StringDictionaryStorage](T_Tessa_Platform_Storage_StringDictionaryStorage_1.htm)<[CardSectionPermissionInfo](T_Tessa_Cards_CardSectionPermissionInfo.htm)>
    Разрешения на секции карточки.
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции. Не должно быть равно null.
#### Возвращаемое значение
[CardSectionPermissionInfo](T_Tessa_Cards_CardSectionPermissionInfo.htm)  
Разрешения на секцию карточки с заданными параметрами, которые были получены
или созданы.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[StringDictionaryStorage](T_Tessa_Platform_Storage_StringDictionaryStorage_1.htm)<[CardSectionPermissionInfo](T_Tessa_Cards_CardSectionPermissionInfo.htm)>.
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
