# CardValidationUniqueInfo.PhysicalColumns - свойство
Физические колонки, в которых требуется проверить уникальность значения. Если
валидатор был связан с комплексной колонкой, то свойство содержит все ключевые
колонки внутри комплексной. В противном случае свойство содержит единственную
физическую колонку, с которой был связан валидатор.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ReadOnlyCollection<CardMetadataColumn> PhysicalColumns { get; }
VB __Копировать
     Public ReadOnly Property PhysicalColumns As ReadOnlyCollection(Of CardMetadataColumn)
    	Get
C++ __Копировать
     public:
    property ReadOnlyCollection<CardMetadataColumn^>^ PhysicalColumns {
    	ReadOnlyCollection<CardMetadataColumn^>^ get ();
    }
F# __Копировать
     member PhysicalColumns : ReadOnlyCollection<CardMetadataColumn> with get
#### Значение свойства
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)>
##  __См. также
#### Ссылки
[CardValidationUniqueInfo -
](T_Tessa_Cards_Validation_CardValidationUniqueInfo.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
