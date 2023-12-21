# CardValidationUniqueInfo.ParentPhysicalColumns - свойство
Физические колонки в родительской секции или пустая коллекция, если
родительская секция не задана. Если валидатор был связан с комплексной
колонкой, то свойство содержит все ключевые колонки внутри комплексной. В
противном случае свойство содержит единственную физическую колонку, с которой
был связан валидатор.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ReadOnlyCollection<CardMetadataColumn> ParentPhysicalColumns { get; }
VB __Копировать
     Public ReadOnly Property ParentPhysicalColumns As ReadOnlyCollection(Of CardMetadataColumn)
    	Get
C++ __Копировать
     public:
    property ReadOnlyCollection<CardMetadataColumn^>^ ParentPhysicalColumns {
    	ReadOnlyCollection<CardMetadataColumn^>^ get ();
    }
F# __Копировать
     member ParentPhysicalColumns : ReadOnlyCollection<CardMetadataColumn> with get
#### Значение свойства
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)>
##  __См. также
#### Ссылки
[CardValidationUniqueInfo -
](T_Tessa_Cards_Validation_CardValidationUniqueInfo.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
