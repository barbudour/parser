# Tessa.Cards.Extensions - пространство имён
Расширения для карточек.
##  __Классы
[CardAnyFileTypePolicy](T_Tessa_Cards_Extensions_CardAnyFileTypePolicy.htm)|
Политика, определяющая допустимость любого имени типа файла для выполнения
методов расширения. Может быть использована для замещения другой политики
[ICardFileTypePolicy](T_Tessa_Cards_Extensions_ICardFileTypePolicy.htm).  
---|---  
[CardAnyMethodPolicy<TMethod>](T_Tessa_Cards_Extensions_CardAnyMethodPolicy_1.htm)|
Политика, определяющая для расширений допустимость любого метода выполнения
запроса к API карточек по его вхождению в список допустимых методов.  
[CardAnyRequestTypePolicy](T_Tessa_Cards_Extensions_CardAnyRequestTypePolicy.htm)|
Политика, определяющая допустимость любого имени универсального запроса к
сервису карточек для выполнения методов расширения. Может быть использована
для замещения другой политики
[ICardRequestTypePolicy](T_Tessa_Cards_Extensions_ICardRequestTypePolicy.htm).  
[CardAnyTaskTypePolicy](T_Tessa_Cards_Extensions_CardAnyTaskTypePolicy.htm)|
Политика, определяющая допустимость любого имени типа задания для выполнения
методов расширения. Может быть использована для замещения другой политики
[ICardTaskTypePolicy](T_Tessa_Cards_Extensions_ICardTaskTypePolicy.htm).  
[CardAnyTypePolicy](T_Tessa_Cards_Extensions_CardAnyTypePolicy.htm)|
Политика, определяющая допустимость любого имени типа карточки для выполнения
методов расширения. Может быть использована для замещения другой политики
[ICardTypePolicy](T_Tessa_Cards_Extensions_ICardTypePolicy.htm).  
[CardDeleteExtension](T_Tessa_Cards_Extensions_CardDeleteExtension.htm)|
Базовый класс расширений для процесса удаления карточки.  
[CardDeleteExtensionContext](T_Tessa_Cards_Extensions_CardDeleteExtensionContext.htm)|
Контекст процесса удаления карточки.  
[CardDeleteMethodFilterPolicy](T_Tessa_Cards_Extensions_CardDeleteMethodFilterPolicy.htm)|
Политика фильтрации расширений, использующая политику
[ICardMethodPolicy<TMethod>](T_Tessa_Cards_Extensions_ICardMethodPolicy_1.htm)
с типом [CardDeleteMethod](T_Tessa_Cards_CardDeleteMethod.htm) для того, чтобы
не выполнять методы расширений, для которых в контексте
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)
указан неподходящий метод
[Method](P_Tessa_Cards_Extensions_ICardDeleteExtensionContext_Method.htm).
Если требуемая политика не зарегистрирована, то метод в контексте проверяется
на равенство значению по умолчанию
[Default](T_Tessa_Cards_CardDeleteMethod.htm).  
[CardExtensionContext](T_Tessa_Cards_Extensions_CardExtensionContext.htm)|
Базовый класс для контекста процесса взаимодействия с карточкой.  
[CardExtensionContextExtensions](T_Tessa_Cards_Extensions_CardExtensionContextExtensions.htm)|
Методы-расширения для интерфейсов
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm),
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
и
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm).  
[CardExtensionHelper](T_Tessa_Cards_Extensions_CardExtensionHelper.htm)|
Вспомогательные методы для организации расширений в карточках.  
[CardFileExtensionContext](T_Tessa_Cards_Extensions_CardFileExtensionContext.htm)|
Контекст процесса взаимодействия с файлом карточки.  
[CardFileTypeFilterPolicy](T_Tessa_Cards_Extensions_CardFileTypeFilterPolicy.htm)|
Политика фильтрации расширений, использующая политику
[ICardFileTypePolicy](T_Tessa_Cards_Extensions_ICardFileTypePolicy.htm) для
того, чтобы не выполнять методы расширений, для которых в контексте
[ICardFileExtensionContext](T_Tessa_Cards_Extensions_ICardFileExtensionContext.htm)
использовано имя типа файла, запрещённое указанной политикой, или тип файла
неизвестен. Если политика
[ICardFileTypePolicy](T_Tessa_Cards_Extensions_ICardFileTypePolicy.htm) не
зарегистрирована, то метод расширения выполняется.  
[CardFileTypePolicy](T_Tessa_Cards_Extensions_CardFileTypePolicy.htm)|
Политика, определяющая допустимость любого из заданных имён или
идентификаторов типов файлов для выполнения методов расширения.  
[CardGetExtension](T_Tessa_Cards_Extensions_CardGetExtension.htm)|  Базовый
класс расширений для процесса получения карточки.  
[CardGetExtensionContext](T_Tessa_Cards_Extensions_CardGetExtensionContext.htm)|
Контекст процесса получения карточки.  
[CardGetFileContentExtension](T_Tessa_Cards_Extensions_CardGetFileContentExtension.htm)|
Базовый класс для расширения для процесса получения контента файла.  
[CardGetFileContentExtensionContext](T_Tessa_Cards_Extensions_CardGetFileContentExtensionContext.htm)|
Контекст процесса получения контента файла.  
[CardGetFileContentMethodFilterPolicy](T_Tessa_Cards_Extensions_CardGetFileContentMethodFilterPolicy.htm)|
Политика фильтрации расширений, использующая политику
[ICardMethodPolicy<TMethod>](T_Tessa_Cards_Extensions_ICardMethodPolicy_1.htm)
с типом [CardGetFileContentMethod](T_Tessa_Cards_CardGetFileContentMethod.htm)
для того, чтобы не выполнять методы расширений, для которых в контексте
[ICardGetFileContentExtensionContext](T_Tessa_Cards_Extensions_ICardGetFileContentExtensionContext.htm)
указан неподходящий метод
[Method](P_Tessa_Cards_Extensions_ICardGetFileContentExtensionContext_Method.htm).
Если требуемая политика не зарегистрирована, то метод в контексте проверяется
на равенство значению по умолчанию
[Default](T_Tessa_Cards_CardGetFileContentMethod.htm).  
[CardGetFileVersionsExtension](T_Tessa_Cards_Extensions_CardGetFileVersionsExtension.htm)|
Базовый класс расширений для процесса получения информации по версиям файла.  
[CardGetFileVersionsExtensionContext](T_Tessa_Cards_Extensions_CardGetFileVersionsExtensionContext.htm)|
Контекст загрузки версий для файла карточки.  
[CardGetFileVersionsMethodFilterPolicy](T_Tessa_Cards_Extensions_CardGetFileVersionsMethodFilterPolicy.htm)|
Политика фильтрации расширений, использующая политику
[ICardMethodPolicy<TMethod>](T_Tessa_Cards_Extensions_ICardMethodPolicy_1.htm)
с типом
[CardGetFileVersionsMethod](T_Tessa_Cards_CardGetFileVersionsMethod.htm) для
того, чтобы не выполнять методы расширений, для которых в контексте
[ICardGetFileVersionsExtensionContext](T_Tessa_Cards_Extensions_ICardGetFileVersionsExtensionContext.htm)
указан неподходящий метод
[Method](P_Tessa_Cards_Extensions_ICardGetFileVersionsExtensionContext_Method.htm).
Если требуемая политика не зарегистрирована, то метод в контексте проверяется
на равенство значению по умолчанию
[Default](T_Tessa_Cards_CardGetFileVersionsMethod.htm).  
[CardGetMethodFilterPolicy](T_Tessa_Cards_Extensions_CardGetMethodFilterPolicy.htm)|
Политика фильтрации расширений, использующая политику
[ICardMethodPolicy<TMethod>](T_Tessa_Cards_Extensions_ICardMethodPolicy_1.htm)
с типом [CardGetMethod](T_Tessa_Cards_CardGetMethod.htm) для того, чтобы не
выполнять методы расширений, для которых в контексте
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
указан неподходящий метод
[Method](P_Tessa_Cards_Extensions_ICardGetExtensionContext_Method.htm). Если
требуемая политика не зарегистрирована, то метод в контексте проверяется на
равенство значению по умолчанию [Default](T_Tessa_Cards_CardGetMethod.htm).  
[CardMetadataExtension](T_Tessa_Cards_Extensions_CardMetadataExtension.htm)|
Базовый класс для расширения, выполняемого при построении метаинформации по
типам карточек [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm). Для того,
чтобы использовать вспомогательные свойства и методы получения метаинформации
по типам карточек, используйте базовый класс
[CardTypeMetadataExtension](T_Tessa_Cards_Extensions_CardTypeMetadataExtension.htm).  
[CardMetadataExtensionContext](T_Tessa_Cards_Extensions_CardMetadataExtensionContext.htm)|
Контекст расширения, выполняемого при построении метаинформации по типам
карточек [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm).  
[CardMetadataExtensionExecutor](T_Tessa_Cards_Extensions_CardMetadataExtensionExecutor.htm)|
Объект, обеспечивающий выполнение расширений для метаинформации по типам
карточек
[ICardMetadataExtension](T_Tessa_Cards_Extensions_ICardMetadataExtension.htm).  
[CardMetadataWithoutExtensionExecutor](T_Tessa_Cards_Extensions_CardMetadataWithoutExtensionExecutor.htm)|
Объект, не выполняющий запуска расширений для метаинформации по типам карточек
[ICardMetadataExtension](T_Tessa_Cards_Extensions_ICardMetadataExtension.htm).
Экземпляр класса следует использовать везде, где не требуется выполнять
расширений.  
[CardMethodPolicy<TMethod>](T_Tessa_Cards_Extensions_CardMethodPolicy_1.htm)|
Политика, определяющая для расширений допустимость метода выполнения запроса к
API карточек по его вхождению в список допустимых методов.  
[CardNewExtension](T_Tessa_Cards_Extensions_CardNewExtension.htm)|  Базовый
класс расширений для процесса создания структуры карточки.  
[CardNewExtensionContext](T_Tessa_Cards_Extensions_CardNewExtensionContext.htm)|
Контекст процесса создания структуры карточки.  
[CardNewGetExtension](T_Tessa_Cards_Extensions_CardNewGetExtension.htm)|
Базовый класс расширений для расширений
[ICardNewExtension](T_Tessa_Cards_Extensions_ICardNewExtension.htm) для
процесса создания карточки (файла, задания) и
[ICardGetExtension](T_Tessa_Cards_Extensions_ICardGetExtension.htm) для
процесса загрузки карточки.  
[CardNewMethodFilterPolicy](T_Tessa_Cards_Extensions_CardNewMethodFilterPolicy.htm)|
Политика фильтрации расширений, использующая политику
[ICardMethodPolicy<TMethod>](T_Tessa_Cards_Extensions_ICardMethodPolicy_1.htm)
с типом [CardNewMethod](T_Tessa_Cards_CardNewMethod.htm) для того, чтобы не
выполнять методы расширений, для которых в контексте
[ICardNewExtensionContext](T_Tessa_Cards_Extensions_ICardNewExtensionContext.htm)
указан неподходящий метод
[Method](P_Tessa_Cards_Extensions_ICardNewExtensionContext_Method.htm). Если
требуемая политика не зарегистрирована, то метод в контексте проверяется на
равенство значению по умолчанию [Default](T_Tessa_Cards_CardNewMethod.htm).  
[CardRepairExtension](T_Tessa_Cards_Extensions_CardRepairExtension.htm)|
Базовый класс для расширения на исправление структуры карточки.  
[CardRepairExtensionContext](T_Tessa_Cards_Extensions_CardRepairExtensionContext.htm)|
Контекст расширений на исправление структуры карточки.  
[CardRequestExtension](T_Tessa_Cards_Extensions_CardRequestExtension.htm)|
Базовый класс расширений для процесса универсального взаимодействия с сервисом
карточек.  
[CardRequestExtensionContext](T_Tessa_Cards_Extensions_CardRequestExtensionContext.htm)|
Контекст универсального взаимодействия с сервисом карточек.  
[CardRequestFilterPolicy](T_Tessa_Cards_Extensions_CardRequestFilterPolicy.htm)|
Политика фильтрации расширений, использующая политики
[ICardRequestTypePolicy](T_Tessa_Cards_Extensions_ICardRequestTypePolicy.htm),
[ICardTypePolicy](T_Tessa_Cards_Extensions_ICardTypePolicy.htm),
[ICardFileTypePolicy](T_Tessa_Cards_Extensions_ICardFileTypePolicy.htm) и
[ICardTaskTypePolicy](T_Tessa_Cards_Extensions_ICardTaskTypePolicy.htm) для
того, чтобы не выполнять методы расширений, для которых в контексте
[ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm)
использованы типы запросов, карточек, файлов и заданий, запрещённые указанной
политикой, или типы неизвестны. Если политика
[ICardRequestTypePolicy](T_Tessa_Cards_Extensions_ICardRequestTypePolicy.htm)
не зарегистрирована, то выдаётся исключение. Если любая другая искомая
политика не зарегистрирована, то метод расширения выполняется.  
[CardRequestTypePolicy](T_Tessa_Cards_Extensions_CardRequestTypePolicy.htm)|
Политика, определяющая допустимость типа универсального запроса к сервису
карточек.  
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm)|
Базовый класс расширений для процесса сохранения карточки.  
[CardStoreExtensionContext](T_Tessa_Cards_Extensions_CardStoreExtensionContext.htm)|
Контекст процесса сохранения карточки.  
[CardStoreMethodFilterPolicy](T_Tessa_Cards_Extensions_CardStoreMethodFilterPolicy.htm)|
Политика фильтрации расширений, использующая политику
[ICardMethodPolicy<TMethod>](T_Tessa_Cards_Extensions_ICardMethodPolicy_1.htm)
с типом [CardStoreMethod](T_Tessa_Cards_CardStoreMethod.htm) для того, чтобы
не выполнять методы расширений, для которых в контексте
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
указан неподходящий метод
[Method](P_Tessa_Cards_Extensions_ICardStoreExtensionContext_Method.htm). Если
требуемая политика не зарегистрирована, то метод в контексте проверяется на
равенство значению по умолчанию [Default](T_Tessa_Cards_CardStoreMethod.htm).  
[CardStoreTaskExtension](T_Tessa_Cards_Extensions_CardStoreTaskExtension.htm)|
Базовый класс расширений для задания в процессе сохранения карточки.  
[CardStoreTaskExtensionContext](T_Tessa_Cards_Extensions_CardStoreTaskExtensionContext.htm)|
Контекст процесса сохранения задания.  
[CardTaskExtensionContext](T_Tessa_Cards_Extensions_CardTaskExtensionContext.htm)|
Контекст процесса взаимодействия с заданием.  
[CardTaskTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTaskTypeFilterPolicy.htm)|
Политика фильтрации расширений, использующая политику
[ICardTaskTypePolicy](T_Tessa_Cards_Extensions_ICardTaskTypePolicy.htm) для
того, чтобы не выполнять методы расширений, для которых в контексте
[ICardTaskExtensionContext](T_Tessa_Cards_Extensions_ICardTaskExtensionContext.htm)
использовано имя типа задания, запрещённое указанной политикой, или тип
задания неизвестен. Если политика
[ICardTaskTypePolicy](T_Tessa_Cards_Extensions_ICardTaskTypePolicy.htm) не
зарегистрирована, то метод расширения выполняется.  
[CardTaskTypePolicy](T_Tessa_Cards_Extensions_CardTaskTypePolicy.htm)|
Политика, определяющая допустимость любого из заданных имён или
идентификаторов типов заданий для выполнения методов расширения.  
[CardTypedRequestExtension<TRequest,
TResponse>](T_Tessa_Cards_Extensions_CardTypedRequestExtension_2.htm)|
Базовый класс расширений для процесса универсального взаимодействия с сервисом
карточек через строготипизированные объекты запроса TRequest и ответа на
запрос TResponse.  
[CardTypeFilterPolicy](T_Tessa_Cards_Extensions_CardTypeFilterPolicy.htm)|
Политика фильтрации расширений, использующая политику
[ICardTypePolicy](T_Tessa_Cards_Extensions_ICardTypePolicy.htm) для того,
чтобы не выполнять методы расширений, для которых в контексте
[ICardTypeExtensionContext](T_Tessa_Cards_Extensions_ICardTypeExtensionContext.htm)
использовано имя типа карточки, запрещённое указанной политикой, или тип
карточки неизвестен. Если политика
[ICardTypePolicy](T_Tessa_Cards_Extensions_ICardTypePolicy.htm) не
зарегистрирована, то метод расширения выполняется.  
[CardTypeMetadataExtension](T_Tessa_Cards_Extensions_CardTypeMetadataExtension.htm)|
Базовый класс для расширений на метаинформацию, который содержит
вспомогательные свойства и методы для получения метаинформации по типам
карточек. В классе-наследнике рекомендуется использовать оба конструктора для
разных регистраций: на клиенте (для предпросмотра карточек) и на сервере. Если
такие средства не требуются и вы хотите полностью управлять конструкторами
расширения, то используйте базовый класс
[CardMetadataExtension](T_Tessa_Cards_Extensions_CardMetadataExtension.htm).  
[CardTypePolicy](T_Tessa_Cards_Extensions_CardTypePolicy.htm)|  Политика,
определяющая допустимость любого из заданных имён или идентификаторов типов
карточек для выполнения методов расширения.  
[CardTypePolicyBase](T_Tessa_Cards_Extensions_CardTypePolicyBase.htm)|
Базовый класс для политик, определяющих допустимость любого из заданных имён
или идентификаторов типов карточек для выполнения методов расширения.  
## __Интерфейсы
[ICardDeleteExtension](T_Tessa_Cards_Extensions_ICardDeleteExtension.htm)|
Расширение для процесса удаления карточки.  
---|---  
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)|
Контекст процесса удаления карточки.  
[ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm)|  Расширение для
процесса взаимодействия с карточкой.  
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm)|
Контекст процесса взаимодействия с карточкой.  
[ICardFileExtensionContext](T_Tessa_Cards_Extensions_ICardFileExtensionContext.htm)|
Контекст процесса взаимодействия с файлом карточки.  
[ICardFileRequestExtensionContext<TRequest,
TResponse>](T_Tessa_Cards_Extensions_ICardFileRequestExtensionContext_2.htm)|
Контекст процесса взаимодействия с запросом на файл карточки.  
[ICardFileTypePolicy](T_Tessa_Cards_Extensions_ICardFileTypePolicy.htm)|
Политика, определяющая допустимость имени или идентификатора типа файла для
выполнения методов расширения.  
[ICardGetExtension](T_Tessa_Cards_Extensions_ICardGetExtension.htm)|
Расширение для процесса получения карточки.  
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)|
Контекст процесса получения карточки.  
[ICardGetFileContentExtension](T_Tessa_Cards_Extensions_ICardGetFileContentExtension.htm)|
Расширение для процесса получения контента файла.  
[ICardGetFileContentExtensionContext](T_Tessa_Cards_Extensions_ICardGetFileContentExtensionContext.htm)|
Контекст процесса получения контента файла.  
[ICardGetFileVersionsExtension](T_Tessa_Cards_Extensions_ICardGetFileVersionsExtension.htm)|
Расширение для процесса получения информации по версиям файла.  
[ICardGetFileVersionsExtensionContext](T_Tessa_Cards_Extensions_ICardGetFileVersionsExtensionContext.htm)|
Контекст загрузки версий для файла карточки.  
[ICardMetadataExtension](T_Tessa_Cards_Extensions_ICardMetadataExtension.htm)|
Расширение, выполняемое при построении метаинформации по типам карточек
[ICardMetadata](T_Tessa_Cards_ICardMetadata.htm).  
[ICardMetadataExtensionContext](T_Tessa_Cards_Extensions_ICardMetadataExtensionContext.htm)|
Контекст расширения, выполняемого при построении метаинформации по типам
карточек [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm).  
[ICardMetadataExtensionExecutor](T_Tessa_Cards_Extensions_ICardMetadataExtensionExecutor.htm)|
Объект, обеспечивающий выполнение расширений для метаинформации по типам
карточек
[ICardMetadataExtension](T_Tessa_Cards_Extensions_ICardMetadataExtension.htm).  
[ICardMethodPolicy<TMethod>](T_Tessa_Cards_Extensions_ICardMethodPolicy_1.htm)|
Политика, проверяющая допустимость метода выполнения запроса к API карточек
для расширений.  
[ICardNewExtension](T_Tessa_Cards_Extensions_ICardNewExtension.htm)|
Расширение для процесса создания структуры карточки.  
[ICardNewExtensionContext](T_Tessa_Cards_Extensions_ICardNewExtensionContext.htm)|
Контекст процесса создания структуры карточки.  
[ICardRepairExtension](T_Tessa_Cards_Extensions_ICardRepairExtension.htm)|
Расширение на исправление структуры карточки.  
[ICardRepairExtensionContext](T_Tessa_Cards_Extensions_ICardRepairExtensionContext.htm)|
Контекст расширений на исправление структуры карточки.  
[ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm)|
Расширение для процесса универсального взаимодействия с сервисом карточек.  
[ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm)|
Контекст универсального взаимодействия с сервисом карточек.  
[ICardRequestExtensionContext<TRequest,
TResponse>](T_Tessa_Cards_Extensions_ICardRequestExtensionContext_2.htm)|
Контекст процесса взаимодействия с запросом на карточку.  
[ICardRequestTypePolicy](T_Tessa_Cards_Extensions_ICardRequestTypePolicy.htm)|
Политика, определяющая допустимость имени универсального запроса к сервису
карточек.  
[ICardStoreExtension](T_Tessa_Cards_Extensions_ICardStoreExtension.htm)|
Расширение для процесса сохранения карточки.  
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)|
Контекст процесса сохранения карточки.  
[ICardStoreTaskExtension](T_Tessa_Cards_Extensions_ICardStoreTaskExtension.htm)|
Расширение для взаимодействия с заданием в процессе сохранения карточки.  
[ICardStoreTaskExtensionContext](T_Tessa_Cards_Extensions_ICardStoreTaskExtensionContext.htm)|
Контекст процесса сохранения задания.  
[ICardTaskExtensionContext](T_Tessa_Cards_Extensions_ICardTaskExtensionContext.htm)|
Контекст процесса взаимодействия с заданием.  
[ICardTaskTypePolicy](T_Tessa_Cards_Extensions_ICardTaskTypePolicy.htm)|
Политика, определяющая допустимость имени или идентификатора типа задания для
выполнения методов расширения.  
[ICardTypeExtensionContext](T_Tessa_Cards_Extensions_ICardTypeExtensionContext.htm)|
Контекст расширений, связанных с типами карточек.  
[ICardTypePolicy](T_Tessa_Cards_Extensions_ICardTypePolicy.htm)|  Политика,
определяющая допустимость имени или идентификатора типа карточки для
выполнения методов расширения.
