# Tessa.Cards.Metadata - пространство имён
API управления метаинформацией карточек, которая используется для связи между
экземплярами карточек, типами карточек и схемой данных.
##  __Классы
[CardCachedMetadata](T_Tessa_Cards_Metadata_CardCachedMetadata.htm)|  Содержит
метаинформацию, необходимую для использования типов карточек совместно с
пакетом карточек. Метаинформация запрашивается у сервиса при первом обращении.  
---|---  
[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm)|  Содержит
метаинформацию, необходимую для использования типов карточек совместно с
пакетом карточек.  
[CardMetadataAllTablesBuilder](T_Tessa_Cards_Metadata_CardMetadataAllTablesBuilder.htm)|
Объект, выполняющий построение метаинформации для всех таблиц, вне зависимости
от их использования в типах карточек, на основании информации, которая
описывается коллекцией [SchemeItems](P_Tessa_Cards_CardType_SchemeItems.htm).  
[CardMetadataBinder](T_Tessa_Cards_Metadata_CardMetadataBinder.htm)|
Вспомогательный класс, осуществляющий действия с карточкой, требующие наличие
метаинформации.  
[CardMetadataBuilder](T_Tessa_Cards_Metadata_CardMetadataBuilder.htm)|
Объект, выполняющий построение метаинформации по типам карточек
[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm) на основании
информации, которая описывается коллекцией
[SchemeItems](P_Tessa_Cards_CardType_SchemeItems.htm).  
[CardMetadataBuilderBase](T_Tessa_Cards_Metadata_CardMetadataBuilderBase.htm)|
Базовый класс для объектов, выполняющих построение метаинформации по типам
карточек [CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm).  
[CardMetadataBuilderBase.ColumnContainerInfo](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_ColumnContainerInfo.htm)|
Информация по физической или комплексной колонке, которая необходима для
построения объекта [CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm) в
методе [BuildAsync(CardTypeCollection, ISchemeService,
CancellationToken)](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_BuildAsync.htm).  
[CardMetadataBuilderBase.MetadataContainer](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_MetadataContainer.htm)|
Контейнер, в котором собирается информацию о секциях и колонках, необходимых
для построения объекта [CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm)
в методе [BuildAsync(CardTypeCollection, ISchemeService,
CancellationToken)](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_BuildAsync.htm).  
[CardMetadataBuilderBase.SectionContainerInfo](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_SectionContainerInfo.htm)|
Информация по колонкам секции, которая необходима для построения объекта
[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm) в методе
[BuildAsync(CardTypeCollection, ISchemeService,
CancellationToken)](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_BuildAsync.htm).  
[CardMetadataBuilderNames](T_Tessa_Cards_Metadata_CardMetadataBuilderNames.htm)|
Имена, используемые для регистрации реализаций
[ICardMetadataBuilder](T_Tessa_Cards_Metadata_ICardMetadataBuilder.htm) в
Unity.  
[CardMetadataCache](T_Tessa_Cards_Metadata_CardMetadataCache.htm)|
Потокобезопасный кэш типов карточек.  
[CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)|  Содержит
метаинформацию о колонке секции.  
[CardMetadataColumnCollection](T_Tessa_Cards_Metadata_CardMetadataColumnCollection.htm)|
Коллекция, содержащая объекты
[CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm).  
[CardMetadataCompletionOption](T_Tessa_Cards_Metadata_CardMetadataCompletionOption.htm)|
Содержит информацию о варианте завершения заданий.  
[CardMetadataCompletionOptionCollection](T_Tessa_Cards_Metadata_CardMetadataCompletionOptionCollection.htm)|
Коллекция, содержащая объекты
[CardMetadataCompletionOption](T_Tessa_Cards_Metadata_CardMetadataCompletionOption.htm).  
[CardMetadataEnumeration](T_Tessa_Cards_Metadata_CardMetadataEnumeration.htm)|
Содержит метаинформацию о перечислении.  
[CardMetadataEnumerationCollection](T_Tessa_Cards_Metadata_CardMetadataEnumerationCollection.htm)|
Коллекция, содержащая объекты
[CardMetadataEnumeration](T_Tessa_Cards_Metadata_CardMetadataEnumeration.htm).  
[CardMetadataEnumerationColumn](T_Tessa_Cards_Metadata_CardMetadataEnumerationColumn.htm)|
Содержит метаинформацию о колонке перечисления.  
[CardMetadataEnumerationColumnCollection](T_Tessa_Cards_Metadata_CardMetadataEnumerationColumnCollection.htm)|
Коллекция, содержащая объекты
[CardMetadataEnumerationColumn](T_Tessa_Cards_Metadata_CardMetadataEnumerationColumn.htm).  
[CardMetadataExtensions](T_Tessa_Cards_Metadata_CardMetadataExtensions.htm)|
Методы-расширения для пространства имён Tessa.Cards.Metadata.  
[CardMetadataForDialogBuilder](T_Tessa_Cards_Metadata_CardMetadataForDialogBuilder.htm)|
Объект, выполняющий построение метаинформации по типам карточек
[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm) на основании
информации, которая описывается коллекцией
[SchemeItems](P_Tessa_Cards_CardType_SchemeItems.htm), если типа карточки не
равен [Dialog](T_Tessa_Cards_CardInstanceType.htm) или основываясь на
коллекции [CardTypeSections](P_Tessa_Cards_CardType_CardTypeSections.htm) если
тип карточки равен [Dialog](T_Tessa_Cards_CardInstanceType.htm).  
[CardMetadataFunctionRole](T_Tessa_Cards_Metadata_CardMetadataFunctionRole.htm)|
Содержит информацию о функциональной роли задания.  
[CardMetadataFunctionRoleCollection](T_Tessa_Cards_Metadata_CardMetadataFunctionRoleCollection.htm)|
Коллекция, содержащая объекты
[CardMetadataFunctionRole](T_Tessa_Cards_Metadata_CardMetadataFunctionRole.htm).  
[CardMetadataHelper](T_Tessa_Cards_Metadata_CardMetadataHelper.htm)|
Вспомогательные методы для преобразования и хранения данных карточки.  
[CardMetadataRecord](T_Tessa_Cards_Metadata_CardMetadataRecord.htm)|  Содержит
метаинформацию о строке перечисления.  
[CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)|
Содержит метаинформацию о секции.  
[CardMetadataSectionCollection](T_Tessa_Cards_Metadata_CardMetadataSectionCollection.htm)|
Коллекция, содержащая объекты
[CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm).  
[CardMetadataSectionReference](T_Tessa_Cards_Metadata_CardMetadataSectionReference.htm)|
Содержит ссылку на секцию в метаинформации.  
[CardMetadataType](T_Tessa_Cards_Metadata_CardMetadataType.htm)|  Тип,
определяющий представление данных в карточке.  
[CardMetadataTypes](T_Tessa_Cards_Metadata_CardMetadataTypes.htm)|  Типы
[CardMetadataType](T_Tessa_Cards_Metadata_CardMetadataType.htm), определяющие
представление данных в карточке. Все типы защищены от изменений.  
[CardMetadataUsageBuilder](T_Tessa_Cards_Metadata_CardMetadataUsageBuilder.htm)|
Объект, выполняющий построение метаинформации по типам карточек
[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm) посредством анализа
всех действительно используемых для построения UI полей. Информация,
описываемая коллекцией [SchemeItems](P_Tessa_Cards_CardType_SchemeItems.htm),
игнорируется.  
## __Интерфейсы
[ICardMetadataBinder](T_Tessa_Cards_Metadata_ICardMetadataBinder.htm)|
Объект, осуществляющий действия с карточкой [Card](T_Tessa_Cards_Card.htm),
требующие наличие метаинформации
[ICardMetadata](T_Tessa_Cards_ICardMetadata.htm), такие как удаление строк
коллекционных секций с учётом всех дочерних строк.  
---|---  
[ICardMetadataBuilder](T_Tessa_Cards_Metadata_ICardMetadataBuilder.htm)|
Объект, выполняющий построение метаинформации по типам карточек
[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm).  
[IType](T_Tessa_Cards_Metadata_IType.htm)|  
## __Перечисления
[CardMetadataColumnType](T_Tessa_Cards_Metadata_CardMetadataColumnType.htm)|
Тип колонки в метаинформации.  
---|---  
[CardMetadataRuntimeType](T_Tessa_Cards_Metadata_CardMetadataRuntimeType.htm)|
Способ представления данных в карточке.  
[CardMetadataSectionFlags](T_Tessa_Cards_Metadata_CardMetadataSectionFlags.htm)|
Флаги секции карточки.
