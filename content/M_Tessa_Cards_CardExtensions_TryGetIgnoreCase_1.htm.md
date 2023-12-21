# CardExtensions.TryGetIgnoreCase(CardMetadataSectionCollection, String) -
метод
Возвращает секцию из метаинформации, полученную без учёта регистра, или null,
если такая секция отсутствует.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardMetadataSection TryGetIgnoreCase(
    	this CardMetadataSectionCollection sections,
    	string sectionName
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetIgnoreCase ( 
    	sections As CardMetadataSectionCollection,
    	sectionName As String
    ) As CardMetadataSection
C++ __Копировать
     public:
    [ExtensionAttribute]
    static CardMetadataSection^ TryGetIgnoreCase(
    	CardMetadataSectionCollection^ sections, 
    	String^ sectionName
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetIgnoreCase : 
            sections : CardMetadataSectionCollection * 
            sectionName : string -> CardMetadataSection 
#### Параметры
sections
[CardMetadataSectionCollection](T_Tessa_Cards_Metadata_CardMetadataSectionCollection.htm)
    Коллекция секций в метаинформации.
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции без учёта регистра.
#### Возвращаемое значение
[CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)  
Секция из метаинформации, полученная без учёта регистра, или null, если такая
секция отсутствует.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[CardMetadataSectionCollection](T_Tessa_Cards_Metadata_CardMetadataSectionCollection.htm).
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
