# CardExtensions.AddDistinctFrom - метод
##  __Список перегрузок
[AddDistinctFrom(ICollection<CardTypeSchemeItem>,
ICollection<CardTypeSchemeItem>)](M_Tessa_Cards_CardExtensions_AddDistinctFrom.htm)|
Добавляет элементы схемы в текущую коллекцию из заданной коллекции
schemeItems, если таких же элементов уже не было в текущей коллекции.
Возвращает признак того, что хотя бы одна секция или колонка была добавлена.  
---|---  
[AddDistinctFrom(ICollection<CardTypeSchemeItem>,
ICollection<CardTypeSchemeItem>, CardMetadataSectionCollection,
Guid)](M_Tessa_Cards_CardExtensions_AddDistinctFrom_1.htm)|  Добавляет
элементы схемы в текущую коллекцию из заданной коллекции schemeItems, если
таких же элементов уже не было в текущей коллекции. Возвращает признак того,
что хотя бы одна секция или колонка была добавлена. Метод также добавляет в
колонки секций sections информацию по типу карточки cardTypeID. В расширениях
на метаинформации используйте эту перегрузку метода только в
[ModifyMetadata(ICardMetadataExtensionContext)](M_Tessa_Cards_Extensions_ICardMetadataExtension_ModifyMetadata.htm).  
## __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
