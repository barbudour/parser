# Tessa.Platform.Runtime - пространство имён
Среда выполнения для обеспечения работы сессий и связи между клиентом и
сервером.
##  __Классы
[ActionHistoryDescriptionContext](T_Tessa_Platform_Runtime_ActionHistoryDescriptionContext.htm)|
Контекст генерации описания для истории действий.  
---|---  
[ActionHistoryDescriptionProvider](T_Tessa_Platform_Runtime_ActionHistoryDescriptionProvider.htm)|
Объект, возвращающий текстовое описание действия с карточкой.  
[ActionHistoryRecord](T_Tessa_Platform_Runtime_ActionHistoryRecord.htm)|
Запись в истории действий карточки. Объект не сериализуется стандартными
средствами.  
[ActionHistoryStrategy](T_Tessa_Platform_Runtime_ActionHistoryStrategy.htm)|
Стратегия управления историей действий карточки и других действий в системе.  
[ActionType](T_Tessa_Platform_Runtime_ActionType.htm)|  Тип действия с
карточкой для записи в историю действий.  
[ActionTypeRegistry](T_Tessa_Platform_Runtime_ActionTypeRegistry.htm)|  Реестр
типов действий в истории
[ActionType](T_Tessa_Platform_Runtime_ActionType.htm).  
[ActionTypes](T_Tessa_Platform_Runtime_ActionTypes.htm)|  Стандартные типы
действий в истории [ActionType](T_Tessa_Platform_Runtime_ActionType.htm).  
[ApplicationAnyIDExtensionPolicy](T_Tessa_Platform_Runtime_ApplicationAnyIDExtensionPolicy.htm)|
Политика, определяющая допустимость любого типа приложения для выполнения
методов расширения. Может быть использована для замещения другой политики
[IApplicationExtensionPolicy](T_Tessa_Platform_Runtime_IApplicationExtensionPolicy.htm).  
[ApplicationAttribute](T_Tessa_Platform_Runtime_ApplicationAttribute.htm)|
Атрибут, описывающий свойства приложения Tessa. Применяется к сборке
[assembly: ApplicationAttribute(...)]. Имя приложения содержится в атрибуте
[assembly: AssemblyTitle(...)].  
[ApplicationClosingEventArgs](T_Tessa_Platform_Runtime_ApplicationClosingEventArgs.htm)|
Аргументы событий по управляемому закрытию окна приложения.  
[ApplicationCommand](T_Tessa_Platform_Runtime_ApplicationCommand.htm)|
Команда, выполняемая при запуске приложения. Обычно связана с аргументами
командной строки.  
[ApplicationCommandArguments](T_Tessa_Platform_Runtime_ApplicationCommandArguments.htm)|
Аргументы командной строки, соответствующие командам
[ApplicationCommands](T_Tessa_Platform_Runtime_ApplicationCommands.htm).  
[ApplicationCommandExecutor](T_Tessa_Platform_Runtime_ApplicationCommandExecutor.htm)|
Объект, выполняющий команды при запуске приложения. Наследники класса могут
переопределить выполнение одной из команд в методе
[Execute(IApplicationContext,
ICollection<IApplicationCommand>)](M_Tessa_Platform_Runtime_ApplicationCommandExecutor_Execute.htm).  
[ApplicationCommandParser](T_Tessa_Platform_Runtime_ApplicationCommandParser.htm)|
Объект, выполняющая разбор аргументов командной строки на команды
[IApplicationCommand](T_Tessa_Platform_Runtime_IApplicationCommand.htm).
Наследники класса могут переопределить разбор одного из аргументов командной
строки в методе [TryParseCommand(IApplicationContext, String,
String)](M_Tessa_Platform_Runtime_ApplicationCommandParser_TryParseCommand.htm).  
[ApplicationCommands](T_Tessa_Platform_Runtime_ApplicationCommands.htm)|  Типы
команд, доступные в командной строке приложения по умолчанию.  
[ApplicationContext](T_Tessa_Platform_Runtime_ApplicationContext.htm)|
Контекст, связанный с запуском или завершением приложения.  
[ApplicationContextDeferredEventArgs](T_Tessa_Platform_Runtime_ApplicationContextDeferredEventArgs.htm)|
Аргументы события, связанного с запуском или завершением приложения.  
[ApplicationDependencies](T_Tessa_Platform_Runtime_ApplicationDependencies.htm)|
Основные зависимости для объекта
[IApplication](T_Tessa_Platform_Runtime_IApplication.htm).  
[ApplicationDescriptor](T_Tessa_Platform_Runtime_ApplicationDescriptor.htm)|
Объект, описывающий текущее приложение, которое определяется по клиентской
сессии [ISession](T_Tessa_Platform_Runtime_ISession.htm). Объект недоступен на
сервере. Инициализация объекта при обращении к его свойствам является
потокобезопасной.  
[ApplicationDescriptorInitializingEventArgs](T_Tessa_Platform_Runtime_ApplicationDescriptorInitializingEventArgs.htm)|
Аргументы события
[Initializing](E_Tessa_Platform_Runtime_IApplicationDescriptor_Initializing.htm),
выполняющего инициализацию параметров приложения через свойства в аргументах
событий, в т.ч. на основании конфигурационных файлов и настроек, полученных от
Tessa Applications.  
[ApplicationEnvironment](T_Tessa_Platform_Runtime_ApplicationEnvironment.htm)|
Объект, предоставляющий доступ к переменным приложения. Объект использует
переменные окружения для текущего процесса в качестве средства хранения и
передачи переменных приложения.  
[ApplicationEnvironmentManager](T_Tessa_Platform_Runtime_ApplicationEnvironmentManager.htm)|
Объект, управляющий переменными приложения.  
[ApplicationExecutingCommandEventArgs](T_Tessa_Platform_Runtime_ApplicationExecutingCommandEventArgs.htm)|
Аргументы события, связанные с выполнением команды, полученной из командной
строки.  
[ApplicationExtension](T_Tessa_Platform_Runtime_ApplicationExtension.htm)|
Базовый класс для расширения, связанного с жизненным циклом приложения.  
[ApplicationExtensionContext](T_Tessa_Platform_Runtime_ApplicationExtensionContext.htm)|
Контекст расширений, связанных с жизненным циклом приложения.  
[ApplicationExtensionContextBase](T_Tessa_Platform_Runtime_ApplicationExtensionContextBase.htm)|
Базовый интерфейс для событий, связанных с приложением, таких как
открытие/закрытие приложения и его инициализация.  
[ApplicationExtensionFilterPolicy](T_Tessa_Platform_Runtime_ApplicationExtensionFilterPolicy.htm)|
Политика фильтрации расширений, использующая политику
[IApplicationExtensionPolicy](T_Tessa_Platform_Runtime_IApplicationExtensionPolicy.htm)
для того, чтобы не выполнять методы расширений, для которых в контексте
[IApplicationExtensionContextBase](T_Tessa_Platform_Runtime_IApplicationExtensionContextBase.htm)
использован идентификатор приложения, запрещённый указанной политикой. Если
политика
[IApplicationExtensionPolicy](T_Tessa_Platform_Runtime_IApplicationExtensionPolicy.htm)
не зарегистрирована, то метод расширения выполняется.  
[ApplicationFolders](T_Tessa_Platform_Runtime_ApplicationFolders.htm)|  Папки
приложений, используемые в системе.  
[ApplicationIdentifiers](T_Tessa_Platform_Runtime_ApplicationIdentifiers.htm)|
Стандартные идентификаторы приложений.  
[ApplicationIDExtensionPolicy](T_Tessa_Platform_Runtime_ApplicationIDExtensionPolicy.htm)|
Политика, определяющая допустимость любого из заданных идентификаторов типов
приложений для выполнения методов расширения.  
[ApplicationInitializer](T_Tessa_Platform_Runtime_ApplicationInitializer.htm)|
Объект, выполняющий инициализацию приложения заданного типа.  
[ApplicationInstance](T_Tessa_Platform_Runtime_ApplicationInstance.htm)|
Приложение Tessa.  
[ApplicationLaunchParameters](T_Tessa_Platform_Runtime_ApplicationLaunchParameters.htm)|
Параметры запуска приложения
[IApplication](T_Tessa_Platform_Runtime_IApplication.htm), которые были
указаны при запуске.  
[ApplicationParameters](T_Tessa_Platform_Runtime_ApplicationParameters.htm)|
Параметры запуска приложения
[IApplication](T_Tessa_Platform_Runtime_IApplication.htm), которые были
определены в ходе запуска.  
[ApplicationParsingCommandEventArgs](T_Tessa_Platform_Runtime_ApplicationParsingCommandEventArgs.htm)|
Аргументы события, связанные с разбором команды, полученной из командной
строки.  
[ApplicationShutdownException](T_Tessa_Platform_Runtime_ApplicationShutdownException.htm)|
Исключение, приводящиее к завершению приложения Tessa. Актуально для некоторых
видов приложений, таких как TessaApplication.  
[AuthenticationRequest](T_Tessa_Platform_Runtime_AuthenticationRequest.htm)|
Запрос на аутентификацию для сервиса
[IAuthenticationService](T_Tessa_Platform_Runtime_IAuthenticationService.htm).  
[AuthenticationResponse](T_Tessa_Platform_Runtime_AuthenticationResponse.htm)|
Ответ на запрос на аутентификацию для сервиса
[IAuthenticationService](T_Tessa_Platform_Runtime_IAuthenticationService.htm).  
[AuthenticationServiceProvider](T_Tessa_Platform_Runtime_AuthenticationServiceProvider.htm)|
Контейнер сервисов, предоставляющий доступ к сервисам в зависимости от типа
входа пользователя
[UserLoginType](T_Tessa_Platform_Runtime_UserLoginType.htm).  
[AuthenticationServiceResolver](T_Tessa_Platform_Runtime_AuthenticationServiceResolver.htm)|
Объект, используемый для запроса сервисов
[IAuthenticationService](T_Tessa_Platform_Runtime_IAuthenticationService.htm),
зарегистрированных по имени значения в
[UserLoginType](T_Tessa_Platform_Runtime_UserLoginType.htm).  
[ClientConfigurationInfoProvider](T_Tessa_Platform_Runtime_ClientConfigurationInfoProvider.htm)|
Объект, предоставляющий информацию по текущей конфигурации на клиенте,
полученной от сервера при инициализации из
[IInitializationContainer](T_Tessa_Platform_Initialization_IInitializationContainer.htm).  
[ClientConfigurationVersionProvider](T_Tessa_Platform_Runtime_ClientConfigurationVersionProvider.htm)|
Объект, обеспечивающий взаимодействие с версией конфигурации запросом к
серверу. Доступен на клиенте для администраторов.  
[ClientUserCipherInfoService](T_Tessa_Platform_Runtime_ClientUserCipherInfoService.htm)|
Сервис, обеспечивающий актуализированную информацию по ключам шифрования для
текущего пользователя. Используется со стороны клиента.  
[ConfigurationInfo](T_Tessa_Platform_Runtime_ConfigurationInfo.htm)|
Информация по текущей конфигурации.  
[ConfigurationSealedException](T_Tessa_Platform_Runtime_ConfigurationSealedException.htm)|
Была произведена попытка изменения конфигурации, когда система функционирует в
режиме защиты от изменений
[Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm).  
[ConfigurationStrictSecurityException](T_Tessa_Platform_Runtime_ConfigurationStrictSecurityException.htm)|
Была произведена попытка вызова функции, когда система функционирует в режиме
повышенной безопасности
[StrictSecurity](T_Tessa_Platform_Runtime_ConfigurationFlags.htm).  
[ConnectionSettings](T_Tessa_Platform_Runtime_ConnectionSettings.htm)|
Настройки для подключения к сервисам Tessa.  
[DefaultAuthenticationService](T_Tessa_Platform_Runtime_DefaultAuthenticationService.htm)|
Сервис аутентификации пользователя по паре логин/пароль, который, в
зависимости от типа входа
[UserLoginType](T_Tessa_Platform_Runtime_UserLoginType.htm) определяет
используемый сервис. Использует объект
[IAuthenticationServiceProvider](T_Tessa_Platform_Runtime_IAuthenticationServiceProvider.htm)
для поиска подходящего сервиса.  
[DefaultHttpClientFactory](T_Tessa_Platform_Runtime_DefaultHttpClientFactory.htm)|
Фабрика объектов
[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient),
которая использует настройки платформы по умолчанию
[ITessaPlatformDependencies](T_Tessa_Platform_ITessaPlatformDependencies.htm).  
[DefaultSessionLoginProvider](T_Tessa_Platform_Runtime_DefaultSessionLoginProvider.htm)|
Объект, предоставляющий информацию по входу сотрудника в систему с
использованием стандартного справочника сотрудников.  
[ErrorCategories](T_Tessa_Platform_Runtime_ErrorCategories.htm)|  Категории
ошибок [Category](P_Tessa_Platform_Runtime_IErrorDescription_Category.htm),
используемые в системе. Список категорий может не ограничиваться перечисленным
в этом классе.  
[ErrorDescription](T_Tessa_Platform_Runtime_ErrorDescription.htm)|  Описание
ошибки, которое задаётся при работе с сервисом
[IErrorManager](T_Tessa_Platform_Runtime_IErrorManager.htm).  
[ErrorDescriptionSerializer](T_Tessa_Platform_Runtime_ErrorDescriptionSerializer.htm)|
Объект, управляющий сериализацией описаний ошибок
[IErrorDescription](T_Tessa_Platform_Runtime_IErrorDescription.htm).  
[ErrorDetails](T_Tessa_Platform_Runtime_ErrorDetails.htm)|  Дополнительное
описание ошибки, которое задаётся при работе с сервисом
[IErrorManager](T_Tessa_Platform_Runtime_IErrorManager.htm).  
[ErrorFile](T_Tessa_Platform_Runtime_ErrorFile.htm)|  Файл, связанный с
ошибкой.  
[ErrorManager](T_Tessa_Platform_Runtime_ErrorManager.htm)|  Объект,
управляющий отправкой и получением ошибок. Получение информации по ошибкам
обычно доступно только на сервере.  
[FakeConfigurationInfoProvider](T_Tessa_Platform_Runtime_FakeConfigurationInfoProvider.htm)|
Реализация интерфейса
[IConfigurationInfoProvider](T_Tessa_Platform_Runtime_IConfigurationInfoProvider.htm),
не выполняющая действий и не имеющая зависимостей. В качестве объекта
конфигурации возвращается
[Unknown](P_Tessa_Platform_Runtime_ConfigurationInfo_Unknown.htm).  
[FakeConfigurationVersionProvider](T_Tessa_Platform_Runtime_FakeConfigurationVersionProvider.htm)|
Реализация интерфейса
[IConfigurationVersionProvider](T_Tessa_Platform_Runtime_IConfigurationVersionProvider.htm),
не выполняющая действий и не имеющая зависимостей.  
[FakeErrorDetailWriter](T_Tessa_Platform_Runtime_FakeErrorDetailWriter.htm)|
Объект, выполняющий запись объекта с деталями по возникшей ошибке. Не
выполняет действий для всех методов.  
[FakeLoginProvider](T_Tessa_Platform_Runtime_FakeLoginProvider.htm)|  Объект
[ILoginProvider](T_Tessa_Platform_Runtime_ILoginProvider.htm), всегда
отменяющий ввод логина/пароля.  
[FakeSessionHostInfoProvider](T_Tessa_Platform_Runtime_FakeSessionHostInfoProvider.htm)|
Реализация интерфейса
[ISessionHostInfoProvider](T_Tessa_Platform_Runtime_ISessionHostInfoProvider.htm),
не возвращающая действительных значений.  
[FakeTypeInfoResolver](T_Tessa_Platform_Runtime_FakeTypeInfoResolver.htm)|
Объект, получающий информацию по типу карточки. Реализация возвращает null для
всех методов.  
[HttpClientPool](T_Tessa_Platform_Runtime_HttpClientPool.htm)|  Пул объектов
[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient).  
[JobProcessManager](T_Tessa_Platform_Runtime_JobProcessManager.htm)|  Менеджер
процессов, использующий [ProcessJob](T_Tessa_Platform_Runtime_ProcessJob.htm)
для объединения процессов в группу. Позволяет запускать дочерние процессы и
управлять их временем жизни. Используйте класс
[WindowsProcessManagerFactory](T_Tessa_Platform_Runtime_WindowsProcessManagerFactory.htm),
чтобы создать экземпляр класса.  
[LazyProcessManager](T_Tessa_Platform_Runtime_LazyProcessManager.htm)|
Менеджер процессов, делегирующий все свои действия другому менеджеру
[IProcessManager](T_Tessa_Platform_Runtime_IProcessManager.htm), который
создаётся при первом обращении к методам.  
[LdapAuthenticationService](T_Tessa_Platform_Runtime_LdapAuthenticationService.htm)|
Сервис аутентификации пользователя в LDAP по паре логин/пароль.  
[LoggerMessageProvider](T_Tessa_Platform_Runtime_LoggerMessageProvider.htm)|
Объект, обеспечивающий вывод сообщений в лог без отображения их пользователю.
Используется, например, для вывода сообщений в
[IApplication](T_Tessa_Platform_Runtime_IApplication.htm). Подтверждение в
методе [ConfirmAsync(String, String,
CancellationToken)](M_Tessa_Platform_Runtime_LoggerMessageProvider_ConfirmAsync.htm),
запрашиваемое у пользователя, всегда возвращает true.  
[LoginBinaryWebProxy](T_Tessa_Platform_Runtime_LoginBinaryWebProxy.htm)|
Прокси для обращения к веб-сервису
[ILoginService](T_Tessa_Platform_Runtime_ILoginService.htm) с использованием
бинарной сериализации.  
[LoginParameters](T_Tessa_Platform_Runtime_LoginParameters.htm)|  Объект с
параметрами входа в окне логина (если используется диалог с UI).  
[LoginService](T_Tessa_Platform_Runtime_LoginService.htm)|  Сервис,
обеспечивающий аутентификацию пользователей.  
[LoginServiceBinaryClient](T_Tessa_Platform_Runtime_LoginServiceBinaryClient.htm)|
Сервис, обеспечивающий аутентификацию пользователей, доступный на клиенте.
Использует бинарную сериализацию.  
[LoginServiceClient](T_Tessa_Platform_Runtime_LoginServiceClient.htm)|
Сервис, обеспечивающий аутентификацию пользователей, доступный на клиенте.  
[LoginServiceLegacy2X](T_Tessa_Platform_Runtime_LoginServiceLegacy2X.htm)|
Реализация веб-сервиса
[ILoginService](T_Tessa_Platform_Runtime_ILoginService.htm) для маршрута
[Legacy2X](T_Tessa_Platform_Runtime_ServiceRoute.htm).  
[LoginServiceLegacyProxy](T_Tessa_Platform_Runtime_LoginServiceLegacyProxy.htm)|
Прокси-объект для сервиса, обеспечивающего аутентификацию пользователей.  
[LoginServiceRouter](T_Tessa_Platform_Runtime_LoginServiceRouter.htm)|
Реализация веб-сервиса
[ILoginService](T_Tessa_Platform_Runtime_ILoginService.htm), которая выполняет
маршрутизацию посредством объекта
[IServiceRouter](T_Tessa_Platform_Runtime_IServiceRouter.htm).  
[LoginWebProxy](T_Tessa_Platform_Runtime_LoginWebProxy.htm)|  Прокси для
обращения к веб-сервису
[ILoginService](T_Tessa_Platform_Runtime_ILoginService.htm).  
[MediaTypes](T_Tessa_Platform_Runtime_MediaTypes.htm)|  Часто используемые
типы MediaType для передачи запросов к сервисам Web API.  
[MessageInspectorEndpointBehavior](T_Tessa_Platform_Runtime_MessageInspectorEndpointBehavior.htm)|
Объект, который добавляет заданный
[IClientMessageInspector](https://learn.microsoft.com/dotnet/api/system.servicemodel.dispatcher.iclientmessageinspector)
для
[ClientRuntime](https://learn.microsoft.com/dotnet/api/system.servicemodel.dispatcher.clientruntime).  
[OpenSessionRequest](T_Tessa_Platform_Runtime_OpenSessionRequest.htm)|  Запрос
на открытие сессии. Содержит учётные данные для входа и параметры открываемой
сессии, включая информацию о приложении и о клиенте.  
[ProcessJob](T_Tessa_Platform_Runtime_ProcessJob.htm)|  Обёртка для
использования объекта WinAPI Job.  
[ProcessManager](T_Tessa_Platform_Runtime_ProcessManager.htm)|  Менеджер
процессов по умолчанию. Позволяет запускать дочерние процессы и управлять их
временем жизни.  
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm)|  Методы-
расширения для пространства имён Tessa.Platform.Runtime.  
[RuntimeHelper](T_Tessa_Platform_Runtime_RuntimeHelper.htm)|  Вспомогательные
методы для пространства имён Tessa.Platform.Runtime.  
[RuntimeSettings](T_Tessa_Platform_Runtime_RuntimeSettings.htm)|  Настройки,
связанные с исполняющей средой системы.  
[ServerConfigurationInfoProvider](T_Tessa_Platform_Runtime_ServerConfigurationInfoProvider.htm)|
Объект, предоставляющий информацию по текущей конфигурации на сервере из базы
данных.  
[ServerConfigurationVersionProvider](T_Tessa_Platform_Runtime_ServerConfigurationVersionProvider.htm)|
Объект, обеспечивающий взаимодействие с версией конфигурации. Доступен на
сервере.  
[ServerSecurityOptions](T_Tessa_Platform_Runtime_ServerSecurityOptions.htm)|
Объект с настройками безопасности сервера.  
[ServerSecurityProvider](T_Tessa_Platform_Runtime_ServerSecurityProvider.htm)|
Объект, предоставляющий доступ к настройкам безопасности сервера
[IServerSecurityOptions](T_Tessa_Platform_Runtime_IServerSecurityOptions.htm).  
[ServiceNotFoundException](T_Tessa_Platform_Runtime_ServiceNotFoundException.htm)|
Исключение, возникающее при невозможности найти требуемый веб-сервис,
например, если указан неправильный путь к веб-сервису.  
[ServiceRouter](T_Tessa_Platform_Runtime_ServiceRouter.htm)|  Объект,
выполняющий получение экземпляров сервисов, актуальных для текущего или
заданного маршрута. Используется на клиенте для некоторых сервисов, для
которых требуется обеспечить обратную совместимость.  
[ServiceRouteSettings](T_Tessa_Platform_Runtime_ServiceRouteSettings.htm)|
Настройки маршрута для взаимодействия с веб-сервисами на клиенте.  
[Session](T_Tessa_Platform_Runtime_Session.htm)|  Сессия пользователя.  
[SessionClient](T_Tessa_Platform_Runtime_SessionClient.htm)|  Объект,
обеспечивающий взаимодействие с сессиями на клиенте.  
[SessionClientParameters](T_Tessa_Platform_Runtime_SessionClientParameters.htm)|
Параметры сессии, полученные с клиента в процессе открытия сессии.  
[SessionContext](T_Tessa_Platform_Runtime_SessionContext.htm)|  Контекст,
переопределяющий токен для текущей сессии.  
[SessionCredentials](T_Tessa_Platform_Runtime_SessionCredentials.htm)|
Настройки входа, используемые для открытия сессии.  
[SessionException](T_Tessa_Platform_Runtime_SessionException.htm)|
Исключение, возникающее при взаимодействии с сессиями Tessa.  
[SessionHttpRequestHeader](T_Tessa_Platform_Runtime_SessionHttpRequestHeader.htm)|
Заголовки HTTP, используемые при обращении к веб-сервисам Tessa.  
[SessionLoginContext](T_Tessa_Platform_Runtime_SessionLoginContext.htm)|
Контекст операции по входу в систему.  
[SessionManager](T_Tessa_Platform_Runtime_SessionManager.htm)|  Объект для
управления клиентскими сессиями.  
[SessionMessageInspector](T_Tessa_Platform_Runtime_SessionMessageInspector.htm)|
Объект, устанавливающий токен
[ISessionToken](T_Tessa_Platform_Runtime_ISessionToken.htm) при вызове
серверных методов.  
[SessionsBinaryWebProxy](T_Tessa_Platform_Runtime_SessionsBinaryWebProxy.htm)|
Прокси для обращения к веб-сервису
[ISessionService](T_Tessa_Platform_Runtime_ISessionService.htm) с
использованием бинарной сериализации.  
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm)|
Сериализуемый объект, используемый в сессии Tessa.  
[SessionSerializationOptions](T_Tessa_Platform_Runtime_SessionSerializationOptions.htm)|
Настройки сериализации объектов
[ISessionSerializableObject](T_Tessa_Platform_Runtime_ISessionSerializableObject.htm).  
[SessionServer](T_Tessa_Platform_Runtime_SessionServer.htm)|  Объект,
обеспечивающий взаимодействие с сессиями на сервере.  
[SessionService](T_Tessa_Platform_Runtime_SessionService.htm)|  Сервис,
управляющий открытыми сессиями.  
[SessionServiceAttribute](T_Tessa_Platform_Runtime_SessionServiceAttribute.htm)|
Описывает интерфейс веб-сервиса Tessa.  
[SessionServiceBinaryClient](T_Tessa_Platform_Runtime_SessionServiceBinaryClient.htm)|
Сервис, обеспечивающий взаимодействие с сессиями, доступный на клиенте.
Использует бинарную сериализацию.  
[SessionServiceClient](T_Tessa_Platform_Runtime_SessionServiceClient.htm)|
Сервис, обеспечивающий взаимодействие с сессиями, доступный на клиенте.  
[SessionServiceLegacy2X](T_Tessa_Platform_Runtime_SessionServiceLegacy2X.htm)|
Реализация веб-сервиса
[ISessionService](T_Tessa_Platform_Runtime_ISessionService.htm) для маршрута
[Legacy2X](T_Tessa_Platform_Runtime_ServiceRoute.htm).  
[SessionServiceRouter](T_Tessa_Platform_Runtime_SessionServiceRouter.htm)|
Реализация веб-сервиса
[ISessionService](T_Tessa_Platform_Runtime_ISessionService.htm), которая
выполняет маршрутизацию посредством объекта
[IServiceRouter](T_Tessa_Platform_Runtime_IServiceRouter.htm).  
[SessionsWebProxy](T_Tessa_Platform_Runtime_SessionsWebProxy.htm)|  Прокси для
обращения к веб-сервису
[ISessionService](T_Tessa_Platform_Runtime_ISessionService.htm).  
[SessionToken](T_Tessa_Platform_Runtime_SessionToken.htm)|  Токен, содержащий
информацию по сессии.  
[SessionTokenHolder](T_Tessa_Platform_Runtime_SessionTokenHolder.htm)|
Объект, содержащий токен, связанный с текущей сессией. Используется на клиенте
для передачи данных между запросами.  
[SessionUserInfo](T_Tessa_Platform_Runtime_SessionUserInfo.htm)|  Информация
по пользователю, доступная из справочника сотрудников.  
[SessionVersionHolder](T_Tessa_Platform_Runtime_SessionVersionHolder.htm)|
Объект, содержащий версию платформы на сервере, связанную с текущей сессией.
Используется на клиенте после успешного логина.  
[TessaHttpContent](T_Tessa_Platform_Runtime_TessaHttpContent.htm)|
Вспомогательные методы для создания объектов
[HttpContent](https://learn.microsoft.com/dotnet/api/system.net.http.httpcontent).  
[User](T_Tessa_Platform_Runtime_User.htm)|  Пользователь системы.  
[UserBlockingManager](T_Tessa_Platform_Runtime_UserBlockingManager.htm)|
Объект, управляющий установкой и снятием блокировки сотрудника.  
[UserCipherInfoEncryptor](T_Tessa_Platform_Runtime_UserCipherInfoEncryptor.htm)|
Объект, обеспечивающий шифрование объекта
[UserCipherInfoObject](T_Tessa_Platform_Runtime_UserCipherInfoObject.htm) с
настройками по шифрованию клиентских данных.  
[UserCipherInfoManager](T_Tessa_Platform_Runtime_UserCipherInfoManager.htm)|
Объект, выполняющий ротацию ключей шифрования, используемых для шифрования
данных на компьютерах пользователей.  
[UserCipherInfoObject](T_Tessa_Platform_Runtime_UserCipherInfoObject.htm)|
Объект с настройками по шифрованию клиентских данных, сериализованный в JSON.
Поле можно сбросить null, чтобы очистить такую информацию, при следующем
запросе настроек поле будет заполнено.  
[UserCipherInfoProvider](T_Tessa_Platform_Runtime_UserCipherInfoProvider.htm)|
Объект, управляющий хранением объекта с настройками по шифрованию клиентских
данных в папках пользователя
[UserCipherInfoObject](T_Tessa_Platform_Runtime_UserCipherInfoObject.htm).  
[UserCipherInfoService](T_Tessa_Platform_Runtime_UserCipherInfoService.htm)|
Сервис, обеспечивающий актуализированную информацию по ключам шифрования для
текущего пользователя. Используется со стороны сервера.  
[UserLoginStrategy](T_Tessa_Platform_Runtime_UserLoginStrategy.htm)|  Объект,
определяющий правила блокировки сотрудника после успешного или неуспешного
логина / изменения пароля.  
[UserPasswordValidator](T_Tessa_Platform_Runtime_UserPasswordValidator.htm)|
Объект, выполняющий проверку пароля сотрудника на соответствие настройкам
безопасности.  
[UserSecurityLockingStrategy](T_Tessa_Platform_Runtime_UserSecurityLockingStrategy.htm)|
Объект, управляющий блокировками на параметры безопасности и шифрования
сотрудника.  
[UserSecurityObject](T_Tessa_Platform_Runtime_UserSecurityObject.htm)|  Объект
с настройками безопасности сотрудника, сериализованный в BSON. Содержит
информацию по предыдущим попыткам входа и по ранее заданным паролям. Поле
можно сбросить null, чтобы очистить такую информацию, при следующем входе в
систему поле будет заполнено.  
[UserSecurityProvider](T_Tessa_Platform_Runtime_UserSecurityProvider.htm)|
Объект, управляющий хранением объекта с настройками безопасности сотрудника
[UserSecurityObject](T_Tessa_Platform_Runtime_UserSecurityObject.htm).  
[WebProxy](T_Tessa_Platform_Runtime_WebProxy.htm)|  Веб-прокси для сервиса
ASP.NET Core.  
[WebProxy.Void](T_Tessa_Platform_Runtime_WebProxy_Void.htm)|  Тип значения,
возвращаемый методами, которые не возвращают значение void.  
[WebProxyFactory](T_Tessa_Platform_Runtime_WebProxyFactory.htm)|  Фабрика
объектов [IWebProxy](T_Tessa_Platform_Runtime_IWebProxy.htm) для обращения к
веб-сервисам системы.  
[WebProxyFactoryBase](T_Tessa_Platform_Runtime_WebProxyFactoryBase.htm)|
Базовый класс для фабрики объектов
[IWebProxy](T_Tessa_Platform_Runtime_IWebProxy.htm) для обращения к веб-
сервисам системы.  
[WindowsAuthenticationService](T_Tessa_Platform_Runtime_WindowsAuthenticationService.htm)|
Сервис аутентификации пользователя в Active Directory по паре логин/пароль.
Сервер должен находится в том же домене или в доверенном домене, что и
пользователь. Работает только для сервера на Windows.  
[WindowsImpersonationContext](T_Tessa_Platform_Runtime_WindowsImpersonationContext.htm)|
Контекст имперсонализации Windows, содержащий информацию об учётной записи
[WindowsIdentity](https://learn.microsoft.com/dotnet/api/system.security.principal.windowsidentity),
от имени которой выполняется код.  
[WindowsProcessManagerFactory](T_Tessa_Platform_Runtime_WindowsProcessManagerFactory.htm)|
Вспомогательные методы для создания объектов
[IProcessManager](T_Tessa_Platform_Runtime_IProcessManager.htm) с
использованием WinAPI. Используйте методы этого класса только на ОС Windows.  
## __Структуры
[DeviceType](T_Tessa_Platform_Runtime_DeviceType.htm)|  Тип устройства,
указанный в сессии.  
---|---  
## __Интерфейсы
[IActionHistoryDescriptionContext](T_Tessa_Platform_Runtime_IActionHistoryDescriptionContext.htm)|
Контекст генерации описания для истории действий.  
---|---  
[IActionHistoryDescriptionProvider](T_Tessa_Platform_Runtime_IActionHistoryDescriptionProvider.htm)|
Объект, возвращающий текстовое описание действия с карточкой.  
[IActionHistoryStrategy](T_Tessa_Platform_Runtime_IActionHistoryStrategy.htm)|
Стратегия управления историей действий карточки и других действий в системе.  
[IActionTypeRegistry](T_Tessa_Platform_Runtime_IActionTypeRegistry.htm)|
Реестр типов действий в истории
[ActionType](T_Tessa_Platform_Runtime_ActionType.htm).  
[IApplication](T_Tessa_Platform_Runtime_IApplication.htm)|  Приложение Tessa.  
[IApplicationCommand](T_Tessa_Platform_Runtime_IApplicationCommand.htm)|
Команда, выполняемая при запуске приложения. Обычно связана с аргументами
командной строки.  
[IApplicationCommandExecutor](T_Tessa_Platform_Runtime_IApplicationCommandExecutor.htm)|
Объект, выполняющий команды при запуске приложения.  
[IApplicationCommandParser](T_Tessa_Platform_Runtime_IApplicationCommandParser.htm)|
Объект, выполняющая разбор аргументов командной строки на команды
[IApplicationCommand](T_Tessa_Platform_Runtime_IApplicationCommand.htm).  
[IApplicationContext](T_Tessa_Platform_Runtime_IApplicationContext.htm)|
Контекст, связанный с запуском или завершением приложения.  
[IApplicationDependencies](T_Tessa_Platform_Runtime_IApplicationDependencies.htm)|
Основные зависимости для объекта
[IApplication](T_Tessa_Platform_Runtime_IApplication.htm).  
[IApplicationDescriptor](T_Tessa_Platform_Runtime_IApplicationDescriptor.htm)|
Объект, описывающий текущее приложение, которое определяется по клиентской
сессии [ISession](T_Tessa_Platform_Runtime_ISession.htm). Объект недоступен на
сервере.  
[IApplicationEnvironment](T_Tessa_Platform_Runtime_IApplicationEnvironment.htm)|
Объект, предоставляющий доступ к переменным приложения.  
[IApplicationEnvironmentManager](T_Tessa_Platform_Runtime_IApplicationEnvironmentManager.htm)|
Объект, управляющий переменными приложения.  
[IApplicationExtension](T_Tessa_Platform_Runtime_IApplicationExtension.htm)|
Расширение, связанное с жизненным циклом приложения.  
[IApplicationExtensionContext](T_Tessa_Platform_Runtime_IApplicationExtensionContext.htm)|
Контекст расширений, связанных с жизненным циклом приложения.  
[IApplicationExtensionContextBase](T_Tessa_Platform_Runtime_IApplicationExtensionContextBase.htm)|
Базовый интерфейс для событий, связанных с приложением, таких как
открытие/закрытие приложения и его инициализация.  
[IApplicationExtensionPolicy](T_Tessa_Platform_Runtime_IApplicationExtensionPolicy.htm)|
Политика, определяющая допустимость идентификатора типа приложения для
выполнения методов расширения.  
[IApplicationFolders](T_Tessa_Platform_Runtime_IApplicationFolders.htm)|
Папки приложений, используемые в системе.  
[IApplicationInitializer](T_Tessa_Platform_Runtime_IApplicationInitializer.htm)|
Объект, выполняющий инициализацию приложения заданного типа.  
[IApplicationLaunchParameters](T_Tessa_Platform_Runtime_IApplicationLaunchParameters.htm)|
Параметры запуска приложения
[IApplication](T_Tessa_Platform_Runtime_IApplication.htm), которые были
указаны при запуске.  
[IApplicationParameters](T_Tessa_Platform_Runtime_IApplicationParameters.htm)|
Параметры запуска приложения
[IApplication](T_Tessa_Platform_Runtime_IApplication.htm), которые были
определены в ходе запуска.  
[IApplicationPublisher](T_Tessa_Platform_Runtime_IApplicationPublisher.htm)|
Объект, выполняющий публикацию приложения.  
[IAuthenticationRequest](T_Tessa_Platform_Runtime_IAuthenticationRequest.htm)|
Запрос на аутентификацию для сервиса
[IAuthenticationService](T_Tessa_Platform_Runtime_IAuthenticationService.htm).  
[IAuthenticationResponse](T_Tessa_Platform_Runtime_IAuthenticationResponse.htm)|
Ответ на запрос на аутентификацию для сервиса
[IAuthenticationService](T_Tessa_Platform_Runtime_IAuthenticationService.htm).  
[IAuthenticationService](T_Tessa_Platform_Runtime_IAuthenticationService.htm)|
Сервис аутентификации пользователя по паре логин/пароль. Регистрируется в
Unity по типу пользователя
[UserLoginType](T_Tessa_Platform_Runtime_UserLoginType.htm).  
[IAuthenticationServiceProvider](T_Tessa_Platform_Runtime_IAuthenticationServiceProvider.htm)|
Контейнер сервисов, предоставляющий доступ к сервисам в зависимости от типа
входа пользователя
[UserLoginType](T_Tessa_Platform_Runtime_UserLoginType.htm).  
[IAuthenticationServiceResolver](T_Tessa_Platform_Runtime_IAuthenticationServiceResolver.htm)|
Объект, используемый для запроса сервисов
[IAuthenticationService](T_Tessa_Platform_Runtime_IAuthenticationService.htm),
зарегистрированных по имени значения в
[UserLoginType](T_Tessa_Platform_Runtime_UserLoginType.htm).  
[IConfigurationInfo](T_Tessa_Platform_Runtime_IConfigurationInfo.htm)|
Информация по текущей конфигурации.  
[IConfigurationInfoProvider](T_Tessa_Platform_Runtime_IConfigurationInfoProvider.htm)|
Объект, предоставляющий информацию по текущей конфигурации.  
[IConfigurationVersionProvider](T_Tessa_Platform_Runtime_IConfigurationVersionProvider.htm)|
Объект, обеспечивающий взаимодействие с версией конфигурации.  
[IConnectionSettings](T_Tessa_Platform_Runtime_IConnectionSettings.htm)|
Настройки для подключения к сервисам Tessa.  
[IErrorDescription](T_Tessa_Platform_Runtime_IErrorDescription.htm)|  Описание
ошибки, которое задаётся при работе с сервисом
[IErrorManager](T_Tessa_Platform_Runtime_IErrorManager.htm).  
[IErrorDescriptionSerializer](T_Tessa_Platform_Runtime_IErrorDescriptionSerializer.htm)|
Объект, управляющий сериализацией описаний ошибок
[IErrorDescription](T_Tessa_Platform_Runtime_IErrorDescription.htm).  
[IErrorDetails](T_Tessa_Platform_Runtime_IErrorDetails.htm)|  Дополнительное
описание ошибки, которое задаётся при работе с сервисом
[IErrorManager](T_Tessa_Platform_Runtime_IErrorManager.htm).  
[IErrorDetailWriter](T_Tessa_Platform_Runtime_IErrorDetailWriter.htm)|
Объект, выполняющий запись объекта с деталями по возникшей ошибке. Обычно это
карточка ошибки.  
[IErrorFile](T_Tessa_Platform_Runtime_IErrorFile.htm)|  Файл, связанный с
ошибкой.  
[IErrorManager](T_Tessa_Platform_Runtime_IErrorManager.htm)|  Объект,
управляющий отправкой и получением ошибок.  
[IHttpClientFactory](T_Tessa_Platform_Runtime_IHttpClientFactory.htm)|
Фабрика объектов
[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient).  
[IHttpClientPool](T_Tessa_Platform_Runtime_IHttpClientPool.htm)|  Пул объектов
[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient).  
[IImpersonationContext](T_Tessa_Platform_Runtime_IImpersonationContext.htm)|
Контекст имперсонализации, содержащий информацию об учётной записи, от имени
которой выполняется код.  
[ILoginParameters](T_Tessa_Platform_Runtime_ILoginParameters.htm)|  Объект с
параметрами входа в окне логина (если используется диалог с UI).  
[ILoginProvider](T_Tessa_Platform_Runtime_ILoginProvider.htm)|  Объект,
обеспечивающий получение информации по логину/паролю. Например, объект может
запросить параметры у пользователя, показав ему диалог. Объект зарегистрирован
на клиенте.  
[ILoginService](T_Tessa_Platform_Runtime_ILoginService.htm)|  Сервис,
обеспечивающий аутентификацию пользователей.  
[ILoginServiceLegacy](T_Tessa_Platform_Runtime_ILoginServiceLegacy.htm)|
Сервис, обеспечивающий аутентификацию пользователей.  
[IMessageProvider](T_Tessa_Platform_Runtime_IMessageProvider.htm)|  Объект,
обеспечивающий вывод сообщений. Сообщения могут выводиться как в виде
диалоговых окон для пользователя, так и в лог. Используется, например, для
вывода сообщений в [IApplication](T_Tessa_Platform_Runtime_IApplication.htm).
Зарегистрирован на клиенте и на сервере.  
[IProcessManager](T_Tessa_Platform_Runtime_IProcessManager.htm)|  Менеджер
процессов. Позволяет запускать дочерние процессы и управлять их временем
жизни.  
[IRuntimeSettings](T_Tessa_Platform_Runtime_IRuntimeSettings.htm)|  Настройки,
связанные с исполняющей средой системы.  
[IServerSecurityOptions](T_Tessa_Platform_Runtime_IServerSecurityOptions.htm)|
Объект с настройками безопасности сервера.  
[IServerSecurityProvider](T_Tessa_Platform_Runtime_IServerSecurityProvider.htm)|
Объект, предоставляющий доступ к настройкам безопасности сервера
[IServerSecurityOptions](T_Tessa_Platform_Runtime_IServerSecurityOptions.htm).  
[IServiceRouter](T_Tessa_Platform_Runtime_IServiceRouter.htm)|  Объект,
выполняющий получение экземпляров сервисов, актуальных для текущего или
заданного маршрута. Используется на клиенте для некоторых сервисов, для
которых требуется обеспечить обратную совместимость.  
[IServiceRouteSettings](T_Tessa_Platform_Runtime_IServiceRouteSettings.htm)|
Настройки маршрута для взаимодействия с веб-сервисами на клиенте.  
[ISession](T_Tessa_Platform_Runtime_ISession.htm)|  Сессия пользователя.  
[ISessionClient](T_Tessa_Platform_Runtime_ISessionClient.htm)|  Объект,
обеспечивающий взаимодействие с сессиями на клиенте.  
[ISessionContext](T_Tessa_Platform_Runtime_ISessionContext.htm)|  Контекст,
переопределяющий токен для текущей сессии.  
[ISessionCredentials](T_Tessa_Platform_Runtime_ISessionCredentials.htm)|
Настройки входа, используемые для открытия сессии.  
[ISessionHostInfoProvider](T_Tessa_Platform_Runtime_ISessionHostInfoProvider.htm)|
Объект, предоставляющий информацию по компьютеру, который обратился к
серверным компонентам Tessa.  
[ISessionLoginContext](T_Tessa_Platform_Runtime_ISessionLoginContext.htm)|
Контекст операции по входу в систему.  
[ISessionLoginProvider](T_Tessa_Platform_Runtime_ISessionLoginProvider.htm)|
Объект, предоставляющий информацию по входу сотрудника в систему.  
[ISessionManager](T_Tessa_Platform_Runtime_ISessionManager.htm)|  Объект для
управления клиентскими сессиями.  
[ISessionSerializableObject](T_Tessa_Platform_Runtime_ISessionSerializableObject.htm)|
Сериализуемый объект, используемый в сессии Tessa.  
[ISessionServer](T_Tessa_Platform_Runtime_ISessionServer.htm)|  Объект,
обеспечивающий взаимодействие с сессиями на сервере.  
[ISessionService](T_Tessa_Platform_Runtime_ISessionService.htm)|  Сервис,
управляющий открытыми сессиями.  
[ISessionServiceLegacy](T_Tessa_Platform_Runtime_ISessionServiceLegacy.htm)|
Сервис, управляющий открытыми сессиями.  
[ISessionToken](T_Tessa_Platform_Runtime_ISessionToken.htm)|  Токен,
содержащий информацию по сессии.  
[ISessionTokenHolder](T_Tessa_Platform_Runtime_ISessionTokenHolder.htm)|
Объект, содержащий токен, связанный с текущей сессией. Используется на клиенте
для передачи данных между запросами.  
[ISessionUserInfo](T_Tessa_Platform_Runtime_ISessionUserInfo.htm)|  Информация
по пользователю, доступная из справочника сотрудников.  
[ISessionVersionHolder](T_Tessa_Platform_Runtime_ISessionVersionHolder.htm)|
Объект, содержащий версию платформы на сервере, связанную с текущей сессией.
Используется на клиенте после успешного логина.  
[ITypeInfoResolver](T_Tessa_Platform_Runtime_ITypeInfoResolver.htm)|  Объект,
получающий информацию по типу карточки. Зарегистрирован в Unity только в том
случае, если зарегистрированы карточки.  
[IUser](T_Tessa_Platform_Runtime_IUser.htm)|  Пользователь системы.  
[IUserBlockingManager](T_Tessa_Platform_Runtime_IUserBlockingManager.htm)|
Объект, управляющий установкой и снятием блокировки сотрудника.  
[IUserCipherInfoEncryptor](T_Tessa_Platform_Runtime_IUserCipherInfoEncryptor.htm)|
Объект, обеспечивающий шифрование объекта
[UserCipherInfoObject](T_Tessa_Platform_Runtime_UserCipherInfoObject.htm) с
настройками по шифрованию клиентских данных.  
[IUserCipherInfoManager](T_Tessa_Platform_Runtime_IUserCipherInfoManager.htm)|
Объект, выполняющий ротацию ключей шифрования, используемых для шифрования
данных на компьютерах пользователей.  
[IUserCipherInfoProvider](T_Tessa_Platform_Runtime_IUserCipherInfoProvider.htm)|
Объект, управляющий хранением объекта с настройками по шифрованию клиентских
данных в папках пользователя
[UserCipherInfoObject](T_Tessa_Platform_Runtime_UserCipherInfoObject.htm).  
[IUserCipherInfoService](T_Tessa_Platform_Runtime_IUserCipherInfoService.htm)|
Сервис, обеспечивающий актуализированную информацию по ключам шифрования для
текущего пользователя.  
[IUserLoginStrategy](T_Tessa_Platform_Runtime_IUserLoginStrategy.htm)|
Объект, определяющий правила блокировки сотрудника после успешного или
неуспешного логина / изменения пароля.  
[IUserPasswordValidator](T_Tessa_Platform_Runtime_IUserPasswordValidator.htm)|
Объект, выполняющий проверку пароля сотрудника на соответствие настройкам
безопасности.  
[IUserSecurityLockingStrategy](T_Tessa_Platform_Runtime_IUserSecurityLockingStrategy.htm)|
Объект, управляющий блокировками на параметры безопасности и шифрования
сотрудника.  
[IUserSecurityProvider](T_Tessa_Platform_Runtime_IUserSecurityProvider.htm)|
Объект, управляющий хранением объекта с настройками безопасности сотрудника
[UserSecurityObject](T_Tessa_Platform_Runtime_UserSecurityObject.htm).  
[IWebProxy](T_Tessa_Platform_Runtime_IWebProxy.htm)|  Веб-прокси для сервиса
ASP.NET Core.  
[IWebProxyFactory](T_Tessa_Platform_Runtime_IWebProxyFactory.htm)|  Фабрика
объектов [IWebProxy](T_Tessa_Platform_Runtime_IWebProxy.htm) для обращения к
веб-сервисам системы.  
## __Делегаты
[ApplicationCommandExecuteFunc](T_Tessa_Platform_Runtime_ApplicationCommandExecuteFunc.htm)|
Выполняет заданную команду. Возвращает признак того, что обработчик команды
был найден и выполнен.  
---|---  
[ApplicationCommandParseFunc](T_Tessa_Platform_Runtime_ApplicationCommandParseFunc.htm)|
Выполняет разбор заданного аргумента командной строки. Возвращает команду,
соответствующую аргументу, или null, если подходящая команда не найдена.  
## __Перечисления
[ApplicationLaunchResult](T_Tessa_Platform_Runtime_ApplicationLaunchResult.htm)|
Режим запуска приложения
[IApplication](T_Tessa_Platform_Runtime_IApplication.htm).  
---|---  
[ApplicationLicenseType](T_Tessa_Platform_Runtime_ApplicationLicenseType.htm)|
Тип лицензии, потребляемый приложением.  
[ConfigurationFlags](T_Tessa_Platform_Runtime_ConfigurationFlags.htm)|
Специальные режимы конфигурации, настраиваемые в конфигурационном файле
сервера.  
[LogonProvider](T_Tessa_Platform_Runtime_LogonProvider.htm)|  
[LogonType](T_Tessa_Platform_Runtime_LogonType.htm)|  
[ServiceRoute](T_Tessa_Platform_Runtime_ServiceRoute.htm)|  Маршрут
взаимодействия с веб-сервисами на клиенте.  
[SessionExceptionCode](T_Tessa_Platform_Runtime_SessionExceptionCode.htm)|
Код ошибки для исключения
[SessionException](T_Tessa_Platform_Runtime_SessionException.htm).  
[SessionLicenseType](T_Tessa_Platform_Runtime_SessionLicenseType.htm)|  Тип
лицензии для сессии.  
[SessionLoginType](T_Tessa_Platform_Runtime_SessionLoginType.htm)|  Тип
авторизации в системе.  
[SessionSerializationMode](T_Tessa_Platform_Runtime_SessionSerializationMode.htm)|
Способ сериализации объектов
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm).  
[SessionServiceType](T_Tessa_Platform_Runtime_SessionServiceType.htm)|  Тип
сессии, который определяется типом веб-приложения: для desktop- или для web-
клиентов, или веб-сервис неизвестен.  
[SessionType](T_Tessa_Platform_Runtime_SessionType.htm)|  Тип сессии,
определяющей место выполнения кода.  
[UserAccessLevel](T_Tessa_Platform_Runtime_UserAccessLevel.htm)|  Уровень
доступа пользователя [IUser](T_Tessa_Platform_Runtime_IUser.htm) к системе.  
[UserLoginType](T_Tessa_Platform_Runtime_UserLoginType.htm)|  Тип
аутентификации, доступный для пользователя.  
[WebProxy.RequestFlags](T_Tessa_Platform_Runtime_WebProxy_RequestFlags.htm)|
Параметры отправки запроса через прокси.
