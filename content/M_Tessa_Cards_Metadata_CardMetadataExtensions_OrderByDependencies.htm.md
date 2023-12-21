# CardMetadataExtensions.OrderByDependencies - метод
Упорядочивает секции метаданных карточек с учётом зависимостей между секциями
в порядке, который необходим для выполнения запросов на вставку записей. Для
удаления записей необходим обратный порядок.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardMetadataSection[] OrderByDependencies(
    	this IEnumerable<CardMetadataSection> sections
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function OrderByDependencies ( 
    	sections As IEnumerable(Of CardMetadataSection)
    ) As CardMetadataSection()
C++ __Копировать
     public:
    [ExtensionAttribute]
    static array<CardMetadataSection^>^ OrderByDependencies(
    	IEnumerable<CardMetadataSection^>^ sections
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member OrderByDependencies : 
            sections : IEnumerable<CardMetadataSection> -> CardMetadataSection[] 
#### Параметры
sections
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)>
    Секции метаданных карточек, которые требуется упорядочить.
#### Возвращаемое значение
[CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)[]  
Упорядоченные секции метаданных карточек.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)>.
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardMetadataExtensions - ](T_Tessa_Cards_Metadata_CardMetadataExtensions.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
