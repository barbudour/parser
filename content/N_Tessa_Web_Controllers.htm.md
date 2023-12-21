# Tessa.Web.Controllers - пространство имён
Контроллеры для взаимодействия с desktop-клиентом.
##  __Классы
[ApplicationsBinaryController](T_Tessa_Web_Controllers_ApplicationsBinaryController.htm)|
Предоставляет доступ для скачивания приложений в Tessa Applications (desktop-
клиент). Использует бинарную сериализацию. Доступен для совместимости со
старыми версиями Tessa Applications.  
---|---  
[ApplicationsController](T_Tessa_Web_Controllers_ApplicationsController.htm)|
Предоставляет доступ для скачивания приложений в Tessa Applications (desktop-
клиент).  
[CardsController](T_Tessa_Web_Controllers_CardsController.htm)|  Предоставляет
средства для работы с карточками.  
[CardTypesController](T_Tessa_Web_Controllers_CardTypesController.htm)|
Предоставляет средства для работы с типами карточек
[CardType](T_Tessa_Cards_CardType.htm) в desktop-клиенте. В качестве типов
могут выступать типы собственно карточек
[Card](T_Tessa_Cards_CardInstanceType.htm), типы файлов
[File](T_Tessa_Cards_CardInstanceType.htm), типы заданий
[Task](T_Tessa_Cards_CardInstanceType.htm) и типы диалогов
[Dialog](T_Tessa_Cards_CardInstanceType.htm).  
[CheckController](T_Tessa_Web_Controllers_CheckController.htm)|  Предоставляет
доступ к проверкам состояния веб-сервиса, если в конфигурации установлена
настройка HealthCheckIsEnabled равной true.  
[InitializationController](T_Tessa_Web_Controllers_InitializationController.htm)|
Предоставляет средства для инициализации приложений desktop-клиента.
Инициализация выполняется в момент запуска приложения.  
[LocalizationBinaryController](T_Tessa_Web_Controllers_LocalizationBinaryController.htm)|
Предоставляет доступ к библиотекам локализации для desktop-клиента,
используется для обратной совместимости с Tessa Applications предыдущих
версий.  
[LocalizationController](T_Tessa_Web_Controllers_LocalizationController.htm)|
Предоставляет доступ к библиотекам локализации.  
[LoginBinaryController](T_Tessa_Web_Controllers_LoginBinaryController.htm)|
Предоставляет методы открытия сессии для desktop-клиента. Используется для
обратной совместимости с Tessa Applications предыдущих версий. Методы этого
контроллера не требуют наличия токена сессии в HTTP-заголовке при обращении.  
[OperationsController](T_Tessa_Web_Controllers_OperationsController.htm)|
Предоставляет средства для создания, чтения, изменения и удаления активных
операций.  
[SchemeController](T_Tessa_Web_Controllers_SchemeController.htm)|
Предоставляет методы для взаимодействия со схемой данных со стороны desktop-
клиентов. Приложение TessaClient не взаимодействует напрямую с этим
контроллером, к нему обращаются TessaAdmin и консольная утилита tadmin.  
[SearchQueriesController](T_Tessa_Web_Controllers_SearchQueriesController.htm)|
Предоставляет средства для работы с поисковыми запросами.  
[SessionsBinaryController](T_Tessa_Web_Controllers_SessionsBinaryController.htm)|
Предоставляет методы закрытия сессии, а также изменения версии конфигурации
для desktop-клиента. Используется для обратной совместимости с Tessa
Applications предыдущих версий.  
[SessionsController](T_Tessa_Web_Controllers_SessionsController.htm)|
Предоставляет методы управления сессиями. Методы открытия сессии не требуют
наличия токена сессии в HTTP-заголовке при обращении.  
[ViewsBinaryController](T_Tessa_Web_Controllers_ViewsBinaryController.htm)|
Предоставляет средства взаимодействия с представлениями в desktop-клиенте.
Используется для обратной совместимости с Tessa Applications предыдущих
версий.  
[ViewsController](T_Tessa_Web_Controllers_ViewsController.htm)|  Предоставляет
средства для работы с представлениями.  
[WorkplacesController](T_Tessa_Web_Controllers_WorkplacesController.htm)|
Предоставляет средства взаимодействия с рабочими местами.
