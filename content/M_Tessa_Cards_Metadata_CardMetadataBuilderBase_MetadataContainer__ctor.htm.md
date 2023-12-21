# CardMetadataBuilderBase.MetadataContainer - конструктор
Создаёт экземпляр класса с указанием максимально допустимого числа типов
карточек, информацию о которых может содержать одна колонка.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public MetadataContainer(
    	int cardTypeCount,
    	IEnumerable<Guid> delayedSchemeCheckCardTypeIDs = null
    )
VB __Копировать
     Public Sub New ( 
    	cardTypeCount As Integer,
    	Optional delayedSchemeCheckCardTypeIDs As IEnumerable(Of Guid) = Nothing
    )
C++ __Копировать
     public:
    MetadataContainer(
    	int cardTypeCount, 
    	IEnumerable<Guid>^ delayedSchemeCheckCardTypeIDs = nullptr
    )
F# __Копировать
     new : 
            cardTypeCount : int * 
            ?delayedSchemeCheckCardTypeIDs : IEnumerable<Guid> 
    (* Defaults:
            let _delayedSchemeCheckCardTypeIDs = defaultArg delayedSchemeCheckCardTypeIDs null
    *)
    -> MetadataContainer
#### Параметры
cardTypeCount [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Максимально допустимое число типов карточек.
delayedSchemeCheckCardTypeIDs
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
(Optional)
     Идентификаторы типов карточек, проверка схемы для которых выполняется после выполнения всех расширений на метаинформацию. Если значение равно null, то считается, что список пуст. 
## __См. также
#### Ссылки
[CardMetadataBuilderBase.MetadataContainer -
](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_MetadataContainer.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
