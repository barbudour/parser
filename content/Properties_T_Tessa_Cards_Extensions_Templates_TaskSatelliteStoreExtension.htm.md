# TaskSatelliteStoreExtension - свойства
##  __Свойства
[CardGetStrategy](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_CardGetStrategy.htm)|
Стратегия низкоуровневой загрузки карточки, используемая при загрузке
виртуального задания.  
---|---  
[CardTransactionStrategy](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_CardTransactionStrategy.htm)|
Стратегия обеспечения блокировок для взаимодействия с основной карточкой.  
[ContextCardInfoKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_ContextCardInfoKey.htm)|
Имя уникального ключа, по которому в контексте расширений context.Info между
методами расширений передаётся информация из сохраняемой карточки card.Info.  
[ContextFilesKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_ContextFilesKey.htm)|
Имя уникального ключа, по которому в контексте расширений context.Info между
методами расширений передаётся список файлов ListStorage<CardFile>.  
[ContextMainCardIDKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_ContextMainCardIDKey.htm)|
Имя уникального ключа, по которому в контексте расширений context.Info между
методами расширений передаётся идентификатор основной карточки.  
[ContextTasksKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_ContextTasksKey.htm)|
Имя уникального ключа, по которому в контексте расширений context.Info между
методами расширений передаётся список заданий ListStorage<CardTask>.  
[ExtendedRepository](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_ExtendedRepository.htm)|
Репозиторий для управления карточками с расширениями и с транзакцией.  
[ExtendedRepositoryWithoutTransaction](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_ExtendedRepositoryWithoutTransaction.htm)|
Репозиторий для управления карточками с расширениями, но без транзакции.  
[NextCardIDKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_NextCardIDKey.htm)|
Имя уникального ключа, по которому в ответе на запрос response.Info содержится
идентификатор карточки, которую надо открыть после сохранения сателлита. Если
в ответе на запрос ключ не указан, то после сохранения повторно открывается
сателлит.  
[NextCardTypeIDKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_NextCardTypeIDKey.htm)|
Имя уникального ключа, по которому в ответе на запрос response.Info содержится
идентификатор типа карточки, которую надо открыть после сохранения сателлита.
Если в ответе на запрос ключ не указан, то после сохранения повторно
открывается сателлит.  
[SatelliteTypeID](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_SatelliteTypeID.htm)|
Идентификатор типа карточки-сателлита.  
[VirtualMainCardIDKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_VirtualMainCardIDKey.htm)|
Имя уникального ключа, по которому в карточке сателлита card.Info содержится
идентификатор основной карточки, если карточка-сателлит была открыта как
виртуальная, т.е. она не существовала на момент загрузки. Если в карточке ключ
не указан, то сателлит уже был создан ранее.  
## __См. также
#### Ссылки
[TaskSatelliteStoreExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
