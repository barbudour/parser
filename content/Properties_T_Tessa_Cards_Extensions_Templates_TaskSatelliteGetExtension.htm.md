# TaskSatelliteGetExtension - свойства
##  __Свойства
[CardGetStrategy](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_CardGetStrategy.htm)|
Стратегия низкоуровневой загрузки карточки, используемая при загрузке
виртуального задания.  
---|---  
[CardNewStrategy](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_CardNewStrategy.htm)|
Стратегия низкоуровневого создания структуры карточки, используемая при
загрузке виртуального задания.  
[CardTransactionStrategy](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_CardTransactionStrategy.htm)|
Стратегия обеспечения блокировок для взаимодействия с основной карточкой.  
[ExtendedRepository](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_ExtendedRepository.htm)|
Репозиторий для управления карточками с расширениями и транзакцией.  
[ExtendedRepositoryWithoutTransaction](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_ExtendedRepositoryWithoutTransaction.htm)|
Репозиторий для управления карточками с расширениями, но без транзакции.  
[FileIsExternalKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_FileIsExternalKey.htm)|
Имя уникального ключа, по которому в информации по файлу сателлита file.Info
будет указан признак того, что файл виртуальный и на самом деле относится к
основной карточке. Если в файле ключ не указан, то файл относится именно к
сателлиту, т.е. это невиртуальный файл.  
[MainCardDigestInVirtualSatelliteSectionFieldName](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_MainCardDigestInVirtualSatelliteSectionFieldName.htm)|
Имя поля с Digest основной карточки, которое содержится в виртуальной
строковой секции в карточке-сателлите.  
[SatelliteTypeID](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_SatelliteTypeID.htm)|
Идентификатор типа карточки-сателлита.  
[VirtualMainCardIDKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_VirtualMainCardIDKey.htm)|
Имя уникального ключа, по которому в карточке сателлита card.Info содержится
идентификатор основной карточки, если карточка-сателлит была открыта как
виртуальная, т.е. она не существовала на момент загрузки. Если в карточке ключ
не указан, то сателлит уже был создан ранее.  
[VirtualSatelliteSection](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_VirtualSatelliteSection.htm)|
Имя виртуальной строковой секции в карточке-сателлите, в которой содержится
Digest основной карточки.  
## __См. также
#### Ссылки
[TaskSatelliteGetExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
