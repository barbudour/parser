# CardMetadata(HashSet<String, CardSerializableObject>,
CardMetadataSectionCollection, CardMetadataEnumerationCollection,
CardTypeCollection, SealableList<Guid>, IValidationResultBuilder) -
конструктор
Создаёт экземпляр класса с указанием списка секций, перечислений и типов
карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadata(
    	HashSet<string, CardSerializableObject> globalReferences,
    	CardMetadataSectionCollection sections,
    	CardMetadataEnumerationCollection enumerations,
    	CardTypeCollection cardTypes,
    	SealableList<Guid> damagedCardTypeIDList,
    	IValidationResultBuilder validationResult = null
    )
VB __Копировать
     Public Sub New ( 
    	globalReferences As HashSet(Of String, CardSerializableObject),
    	sections As CardMetadataSectionCollection,
    	enumerations As CardMetadataEnumerationCollection,
    	cardTypes As CardTypeCollection,
    	damagedCardTypeIDList As SealableList(Of Guid),
    	Optional validationResult As IValidationResultBuilder = Nothing
    )
C++ __Копировать
     public:
    CardMetadata(
    	HashSet<String^, CardSerializableObject^>^ globalReferences, 
    	CardMetadataSectionCollection^ sections, 
    	CardMetadataEnumerationCollection^ enumerations, 
    	CardTypeCollection^ cardTypes, 
    	SealableList<Guid>^ damagedCardTypeIDList, 
    	IValidationResultBuilder^ validationResult = nullptr
    )
F# __Копировать
     new : 
            globalReferences : HashSet<string, CardSerializableObject> * 
            sections : CardMetadataSectionCollection * 
            enumerations : CardMetadataEnumerationCollection * 
            cardTypes : CardTypeCollection * 
            damagedCardTypeIDList : SealableList<Guid> * 
            ?validationResult : IValidationResultBuilder 
    (* Defaults:
            let _validationResult = defaultArg validationResult null
    *)
    -> CardMetadata
#### Параметры
globalReferences
[HashSet](T_Tessa_Platform_Collections_HashSet_2.htm)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm)>
    Список глобальных объектов ([CardTypeForm](T_Tessa_Cards_CardTypeForm.htm), [CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm), [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)), совместно использующиеся в типах карточек.
sections
[CardMetadataSectionCollection](T_Tessa_Cards_Metadata_CardMetadataSectionCollection.htm)
    Список секций, ссылка на который даётся в создаваемом объекте.
enumerations
[CardMetadataEnumerationCollection](T_Tessa_Cards_Metadata_CardMetadataEnumerationCollection.htm)
    Список перечислений, ссылка на который даётся в создаваемом объекте.
cardTypes [CardTypeCollection](T_Tessa_Cards_CardTypeCollection.htm)
    Список типов карточек, ссылка на который даётся в создаваемом объекте.
damagedCardTypeIDList
[SealableList](T_Tessa_Platform_Collections_SealableList_1.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Идентификаторы повреждённых типов карточек. Собственно типы карточек можно получить посредством сервиса типов карточек. 
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
(Optional)
    Результат валидации метаинформации или null, если результат отсутствует.
##  __См. также
#### Ссылки
[CardMetadata - ](T_Tessa_Cards_Metadata_CardMetadata.htm)
[CardMetadata -
перегрузка](Overload_Tessa_Cards_Metadata_CardMetadata__ctor.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
