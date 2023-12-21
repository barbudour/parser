# Tessa.Applications.Synchronization - пространство имён
API управления приложениями в части вычисления разницы по файлам между текущей
версией у пользователя и новой версией, опубликованной на сервере.
##  __Классы
[ApplicationAttributesResult](T_Tessa_Applications_Synchronization_ApplicationAttributesResult.htm)|
Результат выполнения запроса [TryGetModifiedAsync(String, Nullable<Boolean>,
CancellationToken)](M_Tessa_Applications_Services_TessaServer_IApplicationService_TryGetModifiedAsync.htm).
Используется для передачи информации, сериализованной в JSON, между клиентом и
сервером.  
---|---  
[ApplicationCardCreator](T_Tessa_Applications_Synchronization_ApplicationCardCreator.htm)|
Осуществляет создание карточки приложения  
[ApplicationCardQuery](T_Tessa_Applications_Synchronization_ApplicationCardQuery.htm)|
Запрос на получение карточки приложения  
[ApplicationPackageReader](T_Tessa_Applications_Synchronization_ApplicationPackageReader.htm)|
Осуществляет считываение пакета приложения из потока  
[ApplicationPackageWriter](T_Tessa_Applications_Synchronization_ApplicationPackageWriter.htm)|
The application package writer.  
[ApplicationPublisher](T_Tessa_Applications_Synchronization_ApplicationPublisher.htm)|
Осуществляет публикацию приложения  
[ApplicationSynchronizer](T_Tessa_Applications_Synchronization_ApplicationSynchronizer.htm)|
Объект осуществляющий синхронизацию файлов приложения  
[ApplicationUpdateChecker](T_Tessa_Applications_Synchronization_ApplicationUpdateChecker.htm)|
Осуществляет проверку наличия обновления приложения  
[AssemblySynchronizationSource](T_Tessa_Applications_Synchronization_AssemblySynchronizationSource.htm)|
Источник синхронизации в виде сборки приложения  
[AvailableApplicationsQueryFromApplicationService](T_Tessa_Applications_Synchronization_AvailableApplicationsQueryFromApplicationService.htm)|
Объект, выполняющий запросы к приложениям, доступным пользователю, запрашивая
доступ к сервису приложений
[IApplicationService](T_Tessa_Applications_Services_TessaServer_IApplicationService.htm).
Рекомендуется использовать на клиенте при подключении к новым версиям сервера.
Использование на сервере приведёт к рекурсии.  
[AvailableApplicationsQueryFromViewService](T_Tessa_Applications_Synchronization_AvailableApplicationsQueryFromViewService.htm)|
Объект, выполняющий запросы к приложениям, доступным пользователю, запрашивая
доступ к представлениям посредством
[IViewService](T_Tessa_Views_IViewService.htm). Рекомендуется использовать на
сервере или на клиенте при подключении к старым версиям сервера
[Binary3X](T_Tessa_Platform_Runtime_ServiceRoute.htm) или
[Legacy2X](T_Tessa_Platform_Runtime_ServiceRoute.htm).  
[EmptyInstallationProcessMonitor](T_Tessa_Applications_Synchronization_EmptyInstallationProcessMonitor.htm)|
Монитор процесса установки приложения не выполняющий никаких действий  
[FileSystemApplicationPackageFileEnumerable](T_Tessa_Applications_Synchronization_FileSystemApplicationPackageFileEnumerable.htm)|
The file system application package file enumerable.  
[FileSystemSynchronizationSource](T_Tessa_Applications_Synchronization_FileSystemSynchronizationSource.htm)|
Источник синхронизации файлов в виде файловой системы  
[FileSystemSynchronizationStrategy](T_Tessa_Applications_Synchronization_FileSystemSynchronizationStrategy.htm)|
The file system synchronization strategy.  
[FileSystemSynchronizationTarget](T_Tessa_Applications_Synchronization_FileSystemSynchronizationTarget.htm)|
Целевой объект синхронизации в виде файловой системы  
[LocalFileEntry](T_Tessa_Applications_Synchronization_LocalFileEntry.htm)|
Предоставлет информацию о доступном локально файле.  
[LocalFileEntryCollection](T_Tessa_Applications_Synchronization_LocalFileEntryCollection.htm)|
Коллекция локально доступных файлов.  
[LocalPackageHelper](T_Tessa_Applications_Synchronization_LocalPackageHelper.htm)|
Предоставляет методы для работы с локальными файлами приложения
[LocalPackageFile](F_Tessa_Applications_ApplicationCardConstants_LocalPackageFile.htm).  
[SourceConfigurationException](T_Tessa_Applications_Synchronization_SourceConfigurationException.htm)|
Исключение выдаваемое при возникновении ошибок конфигурирования источников
файлов.  
[StreamApplicationPackageFileEnumerable](T_Tessa_Applications_Synchronization_StreamApplicationPackageFileEnumerable.htm)|
Перечислитель файлов пакета приложения содержащихся в потоке  
[StreamApplicationPackageFileEnumerator](T_Tessa_Applications_Synchronization_StreamApplicationPackageFileEnumerator.htm)|
Перечислитель файлов пакета приложения из потока.  
[StreamSynchronizationSource](T_Tessa_Applications_Synchronization_StreamSynchronizationSource.htm)|
Класс реализующий источник синхронизации в виде потока содержащего приложение  
[UpdateCheckedValidationKeys](T_Tessa_Applications_Synchronization_UpdateCheckedValidationKeys.htm)|
Ключи валидации для проверки обновлений приложений.  
## __Интерфейсы
[IApplicationPackageFileEnumerable](T_Tessa_Applications_Synchronization_IApplicationPackageFileEnumerable.htm)|
Описание интерфейса перечислителя файлов  
---|---  
[IApplicationSynchronizationStrategy](T_Tessa_Applications_Synchronization_IApplicationSynchronizationStrategy.htm)|
Описание интерфейса стратегии синхронизации приложения  
[IApplicationSynchronizer](T_Tessa_Applications_Synchronization_IApplicationSynchronizer.htm)|
Описание интерфейса для объектов реализующих синхронизацию файлов приложений  
[IApplicationSynchronizerFactory](T_Tessa_Applications_Synchronization_IApplicationSynchronizerFactory.htm)|
The ApplicationSynchronizerFactory interface.  
[IApplicationUpdateChecker](T_Tessa_Applications_Synchronization_IApplicationUpdateChecker.htm)|
Осуществляет проверку наличия обновления приложения  
[IAssemblySynchronizationSource](T_Tessa_Applications_Synchronization_IAssemblySynchronizationSource.htm)|
Источник синхронизации сборка приложения  
[IAvailableApplicationsQuery](T_Tessa_Applications_Synchronization_IAvailableApplicationsQuery.htm)|
Объект, выполняющий запросы к приложениям, доступным пользователю.  
[ICardSynchronizationStrategy](T_Tessa_Applications_Synchronization_ICardSynchronizationStrategy.htm)|
Описание интерфейса стратегии синхронизации приложения с карточкой приложения  
[ICardSynchronizationTarget](T_Tessa_Applications_Synchronization_ICardSynchronizationTarget.htm)|
Описание интерфейса целевого объекта синхронизации приложения в виде карточки  
[IFileSystemSynchronizationSource](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationSource.htm)|
Описание интерфейса источника синхронизации файловой системы  
[IFileSystemSynchronizationStrategy](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationStrategy.htm)|
Описание интерфейса стратегии синхронизации файловой системы  
[IFileSystemSynchronizationTarget](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationTarget.htm)|
Описание интерфейса целевого объекта синхронизации приложения в виде файловой
системы  
[IInstallationProcessMonitor](T_Tessa_Applications_Synchronization_IInstallationProcessMonitor.htm)|
Описание интерфейса монитора процесса выполнения установки приложения  
[IStreamSynchronizationSource](T_Tessa_Applications_Synchronization_IStreamSynchronizationSource.htm)|
Описание интерфейса источника синхронизации в виде потока  
[ISynchronizationSource](T_Tessa_Applications_Synchronization_ISynchronizationSource.htm)|
Описание интерфейса источника синхронизации  
[ISynchronizationTarget](T_Tessa_Applications_Synchronization_ISynchronizationTarget.htm)|
Описание интерфейса целевого объекта синхронизации.  
## __Делегаты
[FileSystemSynchronizationStrategyFactory](T_Tessa_Applications_Synchronization_FileSystemSynchronizationStrategyFactory.htm)|
Фабрика создания стратегии синхронизации  
---|---
