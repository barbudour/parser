# CardCachedMetadata(ICardTypeClientRepository, String) - конструктор
Создаёт экземпляр класса с указанием сервиса для управления типами карточек.
Независимо от того, защищён ли создаваемый объект от изменений методом
[Seal()](M_Tessa_Cards_Metadata_CardCachedMetadata_Seal.htm), метаинформация
будет получена из кэша, доступного через репозиторий типов карточек
cardTypeClientRepository.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardCachedMetadata(
    	[NotNullAttribute] ICardTypeClientRepository cardTypeClientRepository,
    	string builderName = "Default"
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> cardTypeClientRepository As ICardTypeClientRepository,
    	Optional builderName As String = "Default"
    )
C++ __Копировать
     public:
    CardCachedMetadata(
    	[NotNullAttribute] ICardTypeClientRepository^ cardTypeClientRepository, 
    	String^ builderName = L"Default"
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] cardTypeClientRepository : ICardTypeClientRepository * 
            ?builderName : string 
    (* Defaults:
            let _builderName = defaultArg builderName "Default"
    *)
    -> CardCachedMetadata
#### Параметры
cardTypeClientRepository
[ICardTypeClientRepository](T_Tessa_Cards_ICardTypeClientRepository.htm)
    Репозиторий для управления типами карточек на клиенте.
builderName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
    Имя, по которому будет резолвиться [ICardMetadataBuilder](T_Tessa_Cards_Metadata_ICardMetadataBuilder.htm).
##  __См. также
#### Ссылки
[CardCachedMetadata - ](T_Tessa_Cards_Metadata_CardCachedMetadata.htm)
[CardCachedMetadata -
перегрузка](Overload_Tessa_Cards_Metadata_CardCachedMetadata__ctor.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
