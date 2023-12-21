# CardValidationUniqueInfo - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardValidationUniqueInfo(
    	CardTypeValidator validator,
    	CardMetadataSection section,
    	CardMetadataColumn mainColumn,
    	IList<CardMetadataColumn> physicalColumns,
    	CardMetadataColumn orderColumn,
    	CardMetadataSection parentSection,
    	CardMetadataColumn parentMainColumn,
    	IList<CardMetadataColumn> parentPhysicalColumns,
    	CardType cardType,
    	Card instance,
    	CardStoreMode storeMode,
    	CardValidationMode validationMode,
    	bool removeDuplicates
    )
VB __Копировать
     Public Sub New ( 
    	validator As CardTypeValidator,
    	section As CardMetadataSection,
    	mainColumn As CardMetadataColumn,
    	physicalColumns As IList(Of CardMetadataColumn),
    	orderColumn As CardMetadataColumn,
    	parentSection As CardMetadataSection,
    	parentMainColumn As CardMetadataColumn,
    	parentPhysicalColumns As IList(Of CardMetadataColumn),
    	cardType As CardType,
    	instance As Card,
    	storeMode As CardStoreMode,
    	validationMode As CardValidationMode,
    	removeDuplicates As Boolean
    )
C++ __Копировать
     public:
    CardValidationUniqueInfo(
    	CardTypeValidator^ validator, 
    	CardMetadataSection^ section, 
    	CardMetadataColumn^ mainColumn, 
    	IList<CardMetadataColumn^>^ physicalColumns, 
    	CardMetadataColumn^ orderColumn, 
    	CardMetadataSection^ parentSection, 
    	CardMetadataColumn^ parentMainColumn, 
    	IList<CardMetadataColumn^>^ parentPhysicalColumns, 
    	CardType^ cardType, 
    	Card^ instance, 
    	CardStoreMode storeMode, 
    	CardValidationMode validationMode, 
    	bool removeDuplicates
    )
F# __Копировать
     new : 
            validator : CardTypeValidator * 
            section : CardMetadataSection * 
            mainColumn : CardMetadataColumn * 
            physicalColumns : IList<CardMetadataColumn> * 
            orderColumn : CardMetadataColumn * 
            parentSection : CardMetadataSection * 
            parentMainColumn : CardMetadataColumn * 
            parentPhysicalColumns : IList<CardMetadataColumn> * 
            cardType : CardType * 
            instance : Card * 
            storeMode : CardStoreMode * 
            validationMode : CardValidationMode * 
            removeDuplicates : bool -> CardValidationUniqueInfo
#### Параметры
validator [CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)
    Валидатор, инициировавший проверку.
section [CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
    Секция, в которой требуется проверить уникальность значения.
mainColumn [CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)
    Комплексная или физическая колонка, в которой требуется проверить уникальность значения.
physicalColumns
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)>
    Физические колонки, в которых требуется проверить уникальность значения.
orderColumn
[CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)
     Физическая колонка для сортировки в секции section или null, если колонка для сортировки не задана. 
parentSection
[CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
     Родительская секция или null, если родительская секция не задана. 
parentMainColumn
[CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)
     Колонка в родительской секции или null, если родительская секция не задана. 
parentPhysicalColumns
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)>
     Физические колонки в родительской секции или null, если родительская секция не задана. 
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточки, файла или задания, к которому принадлежит секция.
instance [Card](T_Tessa_Cards_Card.htm)
     Проверяемый объект, по которому могут быть получены секции и идентификатор. Может быть объектом карточки, файла или задания. 
storeMode [CardStoreMode](T_Tessa_Cards_CardStoreMode.htm)
     Режим сохранения карточки. Поскольку instance может быть заданием, то режим сохранения определяем отдельным свойством. 
validationMode
[CardValidationMode](T_Tessa_Cards_Validation_CardValidationMode.htm)
    Способ выполнения валидации.
removeDuplicates
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что дубликаты, найденные в коллекционной секции, должны быть автоматически удалены. 
## __См. также
#### Ссылки
[CardValidationUniqueInfo -
](T_Tessa_Cards_Validation_CardValidationUniqueInfo.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
