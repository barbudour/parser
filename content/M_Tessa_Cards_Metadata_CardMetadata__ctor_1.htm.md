# CardMetadata(CardMetadataSectionCollection, CardType, HashSet<String,
CardSerializableObject>, IValidationResultBuilder) - конструктор
Создаёт экземпляр класса с указанием списка секций и типа карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadata(
    	CardMetadataSectionCollection sections,
    	CardType cardType,
    	HashSet<string, CardSerializableObject> globalReferences,
    	IValidationResultBuilder validationResult = null
    )
VB __Копировать
     Public Sub New ( 
    	sections As CardMetadataSectionCollection,
    	cardType As CardType,
    	globalReferences As HashSet(Of String, CardSerializableObject),
    	Optional validationResult As IValidationResultBuilder = Nothing
    )
C++ __Копировать
     public:
    CardMetadata(
    	CardMetadataSectionCollection^ sections, 
    	CardType^ cardType, 
    	HashSet<String^, CardSerializableObject^>^ globalReferences, 
    	IValidationResultBuilder^ validationResult = nullptr
    )
F# __Копировать
     new : 
            sections : CardMetadataSectionCollection * 
            cardType : CardType * 
            globalReferences : HashSet<string, CardSerializableObject> * 
            ?validationResult : IValidationResultBuilder 
    (* Defaults:
            let _validationResult = defaultArg validationResult null
    *)
    -> CardMetadata
#### Параметры
sections
[CardMetadataSectionCollection](T_Tessa_Cards_Metadata_CardMetadataSectionCollection.htm)
    Список секций, ссылка на который даётся в создаваемом объекте.
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточки, добавляемый в создаваемый объект.
globalReferences
[HashSet](T_Tessa_Platform_Collections_HashSet_2.htm)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm)>
    Список глобальных объектов ([CardTypeForm](T_Tessa_Cards_CardTypeForm.htm), [CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm), [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)), совместно использующиеся в типах карточек.
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
