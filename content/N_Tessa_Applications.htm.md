# Tessa.Applications - пространство имён
API управления приложениями.
##  __Классы
[ApplicationApiVersionNames](T_Tessa_Applications_ApplicationApiVersionNames.htm)|
Имена объектов, регистрируемых в Unity для различных версий API.  
---|---  
[ApplicationCardConstants](T_Tessa_Applications_ApplicationCardConstants.htm)|
Константы для карточки приложения  
[ApplicationCardConstants.ApplicationSection](T_Tessa_Applications_ApplicationCardConstants_ApplicationSection.htm)|
Константы для секции приложения  
[ApplicationInstanceManager](T_Tessa_Applications_ApplicationInstanceManager.htm)|
Предоставляет методы для определения, является ли текущий экземпляр приложения
первым запущенным в системе  
[ApplicationLaunchingException](T_Tessa_Applications_ApplicationLaunchingException.htm)|
Исключение возникающее при ошибке запуска приложения.  
[ApplicationLaunchingStrategy](T_Tessa_Applications_ApplicationLaunchingStrategy.htm)|
Стратегия запуска приложения.  
[ApplicationModel](T_Tessa_Applications_ApplicationModel.htm)|  Модель
приложения  
[ApplicationsInstallationPathSettings](T_Tessa_Applications_ApplicationsInstallationPathSettings.htm)|
Описание интерфейса предоставляющего доступ к настройке пути по которому
осуществляется установка приложений  
[ApplicationsRegistrator](T_Tessa_Applications_ApplicationsRegistrator.htm)|
Осуществляет регистрацию зависимостей необходимых для работы приложения  
[ApplicationState](T_Tessa_Applications_ApplicationState.htm)|  Состояние
приложения  
[CatalogApplicationsQuery](T_Tessa_Applications_CatalogApplicationsQuery.htm)|
Возвращает список приложений для каталога приложений  
[ClientSessionController](T_Tessa_Applications_ClientSessionController.htm)|
Контроллер сессий  
[ClientTessaViewModelRepositoryImplementer](T_Tessa_Applications_ClientTessaViewModelRepositoryImplementer.htm)|
Клиентский репозиторий для обращения к сервису представлений  
[ClientViewServiceImplementer](T_Tessa_Applications_ClientViewServiceImplementer.htm)|
Клиентская реализация сервиса представлений  
[CurrentUserDataProtectionService](T_Tessa_Applications_CurrentUserDataProtectionService.htm)|
Сервис шифрования данных связанных с текущим пользователем  
[DataProtectionServiceExtender](T_Tessa_Applications_DataProtectionServiceExtender.htm)|
Методы расширения для сервиса шифрования данных  
[FakeWorkplaceService](T_Tessa_Applications_FakeWorkplaceService.htm)|  The
fake workplace service.  
[GenericExtensions](T_Tessa_Applications_GenericExtensions.htm)|  The generic
extensions.  
[HashHelper](T_Tessa_Applications_HashHelper.htm)|  Вспомогательные методы для
работы с контрольными суммами  
[LocalizationConstants](T_Tessa_Applications_LocalizationConstants.htm)|  The
localization constants.  
[LocalizationConstants.ApplicationCatalogEditor](T_Tessa_Applications_LocalizationConstants_ApplicationCatalogEditor.htm)|
The application catalog editor.  
[LocalizationConstants.ApplicationCatalogManagerConstants](T_Tessa_Applications_LocalizationConstants_ApplicationCatalogManagerConstants.htm)|
The application catalog manager constants.  
[LocalizationConstants.ApplicationServiceConstants](T_Tessa_Applications_LocalizationConstants_ApplicationServiceConstants.htm)|
The application service constants.  
[LocalizationConstants.AppManagerUpdateConstants](T_Tessa_Applications_LocalizationConstants_AppManagerUpdateConstants.htm)|
Контстанты для локализации процесса обновления диспетчера приложений  
[LocalizationConstants.ShellConstants](T_Tessa_Applications_LocalizationConstants_ShellConstants.htm)|
The shell constants.  
[PathHelper](T_Tessa_Applications_PathHelper.htm)|  Вспомогательные методы для
работы c путями файлов  
[ServerSessionController](T_Tessa_Applications_ServerSessionController.htm)|
Серверный контроллер сессий. Не выполняет создание сессии, поскольку на
сервере уже есть сессия, пришедшая с клиента.  
[StandardApplicationAliases](T_Tessa_Applications_StandardApplicationAliases.htm)|
Список алиасов (псевдонимов) стандартных приложений платформы.  
[StorageSchemaConstants](T_Tessa_Applications_StorageSchemaConstants.htm)|
Константы для каталогов приложений  
[StorageSchemaConstants.ApplicationCatalogSchemeConstants](T_Tessa_Applications_StorageSchemaConstants_ApplicationCatalogSchemeConstants.htm)|
Константы схемы каталогов приложений  
[StorageSchemaConstants.ApplicationCatalogsSchemeConstants](T_Tessa_Applications_StorageSchemaConstants_ApplicationCatalogsSchemeConstants.htm)|
Константы схемы каталога приложений  
[StorageSchemaConstants.ApplicationPackageSchemeConstants](T_Tessa_Applications_StorageSchemaConstants_ApplicationPackageSchemeConstants.htm)|
Константы схемы структуры приложения  
[TessaSpecialFoldersConstants](T_Tessa_Applications_TessaSpecialFoldersConstants.htm)|
Список контстант конфигуратора приложения  
[ValidationHelper](T_Tessa_Applications_ValidationHelper.htm)|
Вспомогательные методы для проверки данных  
## __Интерфейсы
[IApplicationCatalog](T_Tessa_Applications_IApplicationCatalog.htm)|  Описание
интерфейса каталога приложений  
---|---  
[IApplicationCatalogRegistry](T_Tessa_Applications_IApplicationCatalogRegistry.htm)|
Описание интерфейса сервиса каталогов приложений  
[IApplicationCatalogSaver](T_Tessa_Applications_IApplicationCatalogSaver.htm)|
Описание интерфейса объекта осуществляющего сохранение хранилища каталогов
приложений  
[IApplicationCatalogStorageLoader](T_Tessa_Applications_IApplicationCatalogStorageLoader.htm)|
Описание интерфейса загрузчика хранилища каталога приложений  
[IApplicationCatalogVisitor](T_Tessa_Applications_IApplicationCatalogVisitor.htm)|
Описание интерфейса операции над каталогом приложений  
[IApplicationCollectionUpdater](T_Tessa_Applications_IApplicationCollectionUpdater.htm)|
Описание интерфейса осуществляющего обновление коллекции приложений  
[IApplicationLaunchingStrategy](T_Tessa_Applications_IApplicationLaunchingStrategy.htm)|
Описание интерфейса стратегии запуска приложения  
[IApplicationModel](T_Tessa_Applications_IApplicationModel.htm)|  Описание
интерфейса модели приложения  
[IApplicationsInstallationPathSettings](T_Tessa_Applications_IApplicationsInstallationPathSettings.htm)|
Описание интерфейса предоставляющего доступ к настройке пути по которому
осуществляется установка приложений  
[IAppManagerApplication](T_Tessa_Applications_IAppManagerApplication.htm)|
Описание интерфейса первого экземпляра приложения  
[IDataProtectionService](T_Tessa_Applications_IDataProtectionService.htm)|
Описание интерфейса сервиса шифрования данных  
[IErrorLog](T_Tessa_Applications_IErrorLog.htm)|  Описание интерфейса
глобального лога ошибок  
[ISessionController](T_Tessa_Applications_ISessionController.htm)|  Описание
интерфейса контроллера сессий приложения  
## __Делегаты
[ApplicationCatalogFactoryDelegate](T_Tessa_Applications_ApplicationCatalogFactoryDelegate.htm)|
Делегат фабрики создания каталога приложений  
---|---  
[ApplicationModelFactoryDelegate](T_Tessa_Applications_ApplicationModelFactoryDelegate.htm)|
Фабрика создания модели приложения  
[ContainerInitializationDelegate](T_Tessa_Applications_ContainerInitializationDelegate.htm)|
Осуществляет инициализацию контейнера  
[GetCatalogApplicationsDelegateAsync](T_Tessa_Applications_GetCatalogApplicationsDelegateAsync.htm)|
Делегат получения списка моделей приложений, содержащихся в каталоге catalog.  
[GetCatalogContainerDelegateAsync](T_Tessa_Applications_GetCatalogContainerDelegateAsync.htm)|
Возвращает контейнер получения зависимостей для каталога приложений  
[GetTessaSpecialFolderDelegate](T_Tessa_Applications_GetTessaSpecialFolderDelegate.htm)|
Делегат экземпляры которого возвращают путь к специальным папкам Tessa  
[HashCalculateDelegateAsync](T_Tessa_Applications_HashCalculateDelegateAsync.htm)|
Осуществляет расчет контрольной суммы для потока  
[LaunchStrategyFactoryDelegate](T_Tessa_Applications_LaunchStrategyFactoryDelegate.htm)|
Делегат экземпляры которого осуществляют создание стратегии запуска приложения  
[ProcessCatalogExceptionDelegateAsync](T_Tessa_Applications_ProcessCatalogExceptionDelegateAsync.htm)|
Делегат обработки исключения возникшего при загрузке приложений из каталога  
[ShellActivatorDelegate](T_Tessa_Applications_ShellActivatorDelegate.htm)|
Делегат активации основого окна программы  
## __Перечисления
[ApplicationArchitecture](T_Tessa_Applications_ApplicationArchitecture.htm)|
Архитектура приложения, предпочитаемая для сотрудника.  
---|---  
[ApplicationsLoadingState](T_Tessa_Applications_ApplicationsLoadingState.htm)|
Признаки обозначающие состояние загрузки приложений каталога  
[TessaSpecialFolder](T_Tessa_Applications_TessaSpecialFolder.htm)|
Перечесление содержащее специальные папки приложения
