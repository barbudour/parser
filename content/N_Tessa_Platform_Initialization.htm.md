# Tessa.Platform.Initialization - пространство имён
API для загрузки данных с сервера при инициализации приложения.
##  __Классы
[ClientInitializationCacheProvider](T_Tessa_Platform_Initialization_ClientInitializationCacheProvider.htm)|
Объект, предоставляющий средства для сохранения информации по инициализации в
локальном кэше приложения и для загрузки этой информации из кэша.  
---|---  
[ClientInitializationExtension](T_Tessa_Platform_Initialization_ClientInitializationExtension.htm)|
Базовый класс для расширения для инициализации приложений со стороны клиента.  
[ClientInitializationExtensionContext](T_Tessa_Platform_Initialization_ClientInitializationExtensionContext.htm)|
Контекст расширений для инициализации приложений со стороны клиента.  
[ClientInitializer](T_Tessa_Platform_Initialization_ClientInitializer.htm)|
Объект, выполняющий инициализацию клиента по данным, полученным с сервера.  
[DefaultColors](T_Tessa_Platform_Initialization_DefaultColors.htm)|  Цвета
палитры, настроенные по умолчанию для всех пользователей.  
[FakeClientInitializationCacheProvider](T_Tessa_Platform_Initialization_FakeClientInitializationCacheProvider.htm)|
Объект, не выполняющий действий для методов интерфейса
[IClientInitializationCacheProvider](T_Tessa_Platform_Initialization_IClientInitializationCacheProvider.htm).  
[FakeClientInitializer](T_Tessa_Platform_Initialization_FakeClientInitializer.htm)|
Объект, не выполняющий инициализацию клиента по данным, полученным с сервера,
и возвращающий пустой результат валидации, как и при успешной инициализации.
Рекомендуется использовать как зависимость при вызове конструкторов сервисов
вручную, когда не требуется обеспечивать корректную инициализацию посредством
таких сервисов.  
[FakeServerInitializer](T_Tessa_Platform_Initialization_FakeServerInitializer.htm)|
Объект, возвращающий пустые данные для инициализации клиента. Рекомендуется
использовать как зависимость при вызове конструкторов сервисов вручную, когда
не требуется обеспечивать корректную инициализацию посредством таких сервисов.  
[InitializationContainer](T_Tessa_Platform_Initialization_InitializationContainer.htm)|
Объект, содержащий информацию, заполняемую при инициализации приложения.  
[InitializationExtensionContext](T_Tessa_Platform_Initialization_InitializationExtensionContext.htm)|
Базовый класс для контекста расширений для инициализации приложений.  
[InitializationExtensions](T_Tessa_Platform_Initialization_InitializationExtensions.htm)|
Методы-расширения для пространства имён Tessa.Platform.Initialization.  
[InitializationReader](T_Tessa_Platform_Initialization_InitializationReader.htm)|
Объект, выполняющий чтение из потока данных по инициализации.  
[InitializationRequest](T_Tessa_Platform_Initialization_InitializationRequest.htm)|
Запрос на инициализацию приложения.  
[InitializationResponse](T_Tessa_Platform_Initialization_InitializationResponse.htm)|
Ответ на запрос на инициализацию приложения. Содержит структурированную
информацию по инициализации.  
[InitializationService](T_Tessa_Platform_Initialization_InitializationService.htm)|
Сервис для инициализации приложения с передачей приложению всех данных,
требуемых для его работы.  
[InitializationServiceClient](T_Tessa_Platform_Initialization_InitializationServiceClient.htm)|
Сервис для инициализации приложения, доступный на клиенте.  
[InitializationWebProxy](T_Tessa_Platform_Initialization_InitializationWebProxy.htm)|
Прокси для обращения к веб-сервису
[IInitializationService](T_Tessa_Platform_Initialization_IInitializationService.htm).  
[InitializationWriter](T_Tessa_Platform_Initialization_InitializationWriter.htm)|
Объект, выполняющий запись в поток данных по инициализации.  
[ServerInitializationExtension](T_Tessa_Platform_Initialization_ServerInitializationExtension.htm)|
Базовый класс для расширения для инициализации приложений со стороны сервера.  
[ServerInitializationExtensionContext](T_Tessa_Platform_Initialization_ServerInitializationExtensionContext.htm)|
Контекст расширений для инициализации приложений со стороны сервера.  
[ServerInitializer](T_Tessa_Platform_Initialization_ServerInitializer.htm)|
Объект, возвращающий данные для инициализации клиента. Такие данные обычно
собираются на сервере.  
[StorageDefaultColors](T_Tessa_Platform_Initialization_StorageDefaultColors.htm)|
Цвета палитры, настроенные по умолчанию для всех пользователей, которые
сериализованы в хранилище Dictionary<string, object>.  
[WorkplaceInitializationContext](T_Tessa_Platform_Initialization_WorkplaceInitializationContext.htm)|
Контекст инициализации рабочих мест. Правило инициализации может скрыть
некоторые узлы рабочего места в зависимости от любых условий, например, от
того, в какие роли входит сотрудник.  
[WorkplaceInitializationRule](T_Tessa_Platform_Initialization_WorkplaceInitializationRule.htm)|
Базовый класс для правила инициализации рабочих мест. Правило вызывается для
каждого доступного узла рабочего места и может скрыть узел в зависимости от
любых условий, например, от того, в какие роли входит сотрудник.  
## __Интерфейсы
[IClientInitializationCacheProvider](T_Tessa_Platform_Initialization_IClientInitializationCacheProvider.htm)|
Объект, предоставляющий средства для сохранения информации по инициализации в
локальном кэше приложения и для загрузки этой информации из кэша.  
---|---  
[IClientInitializationExtension](T_Tessa_Platform_Initialization_IClientInitializationExtension.htm)|
Расширение для инициализации приложений со стороны клиента.  
[IClientInitializationExtensionContext](T_Tessa_Platform_Initialization_IClientInitializationExtensionContext.htm)|
Контекст расширений для инициализации приложений со стороны клиента.  
[IClientInitializer](T_Tessa_Platform_Initialization_IClientInitializer.htm)|
Объект, выполняющий инициализацию клиента по данным, полученным с сервера.  
[IDefaultColors](T_Tessa_Platform_Initialization_IDefaultColors.htm)|  Цвета
палитры, настроенные по умолчанию для всех пользователей.  
[IInitializationContainer](T_Tessa_Platform_Initialization_IInitializationContainer.htm)|
Объект, содержащий информацию, заполняемую при инициализации приложения.  
[IInitializationExtensionContext](T_Tessa_Platform_Initialization_IInitializationExtensionContext.htm)|
Контекст расширений для инициализации приложений.  
[IInitializationService](T_Tessa_Platform_Initialization_IInitializationService.htm)|
Сервис для инициализации приложения с передачей приложению всех данных,
требуемых для его работы.  
[IServerInitializationExtension](T_Tessa_Platform_Initialization_IServerInitializationExtension.htm)|
Расширение для инициализации приложений со стороны сервера.  
[IServerInitializationExtensionContext](T_Tessa_Platform_Initialization_IServerInitializationExtensionContext.htm)|
Контекст расширений для инициализации приложений со стороны сервера.  
[IServerInitializer](T_Tessa_Platform_Initialization_IServerInitializer.htm)|
Объект, возвращающий данные для инициализации клиента. Такие данные обычно
собираются на сервере.  
[IWorkplaceInitializationContext](T_Tessa_Platform_Initialization_IWorkplaceInitializationContext.htm)|
Контекст инициализации рабочих мест. Правило инициализации может скрыть
некоторые узлы рабочего места в зависимости от любых условий, например, от
того, в какие роли входит сотрудник.  
## __Делегаты
[ReadFromStreamInitializationActionAsync](T_Tessa_Platform_Initialization_ReadFromStreamInitializationActionAsync.htm)|
Метод, выполняющий чтение из потока инициализации. Метод может освобождать
переданный ему поток.  
---|---  
[WriteToStreamInitializationActionAsync](T_Tessa_Platform_Initialization_WriteToStreamInitializationActionAsync.htm)|
Метод, выполняющий запись в поток инициализации. Метод не должен освобождаться
переданный ему поток. Если данные не записываются, то информация по
обработчику будет отсутствовать в потоке инициализации.  
## __Перечисления
[InitializationAddHandlerMode](T_Tessa_Platform_Initialization_InitializationAddHandlerMode.htm)|
Способ добавления обработчика в поток инициализации.  
---|---
