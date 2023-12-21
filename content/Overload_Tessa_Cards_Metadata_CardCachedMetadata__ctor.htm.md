# CardCachedMetadata - конструктор
##  __Список перегрузок
[CardCachedMetadata(ICardTypeClientRepository,
String)](M_Tessa_Cards_Metadata_CardCachedMetadata__ctor.htm)|  Создаёт
экземпляр класса с указанием сервиса для управления типами карточек.
Независимо от того, защищён ли создаваемый объект от изменений методом
[Seal()](M_Tessa_Cards_Metadata_CardCachedMetadata_Seal.htm), метаинформация
будет получена из кэша, доступного через репозиторий типов карточек
cardTypeClientRepository.  
---|---  
[CardCachedMetadata(CardMetadataCache, ICardTypeServerRepository,
ICardMetadataBuilder, ISchemeService, IDbScope,
String)](M_Tessa_Cards_Metadata_CardCachedMetadata__ctor_1.htm)|  Создаёт
экземпляр класса с указанием сервиса для управления типами карточек, объекта,
выполняющего построение метаинформации по типам карточек, и объекта,
используемого для доступа к метаинформации по структуре базы данных.  
## __См. также
#### Ссылки
[CardCachedMetadata - ](T_Tessa_Cards_Metadata_CardCachedMetadata.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
