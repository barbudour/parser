# Chronos.Platform.Scheduling - пространство имён
Инструменты для диспетчеризации плагинов Chronos.
##  __Классы
[PluginFacade](T_Chronos_Platform_Scheduling_PluginFacade.htm)|  Фасад для
управления жизненными циклами хоста и дочерних процессов, предназначенных для
запуска плагинов.  
---|---  
[PluginFacade.StartChildInfo](T_Chronos_Platform_Scheduling_PluginFacade_StartChildInfo.htm)|  
[PluginFacade.StartHostInfo](T_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo.htm)|
Параметры запуска метода [StartHostAsync(PluginFacade.StartHostInfo,
CancellationToken)](M_Chronos_Platform_Scheduling_PluginFacade_StartHostAsync.htm).  
[PluginFactory](T_Chronos_Platform_Scheduling_PluginFactory.htm)|  Хэлперы для
создания экземпляров плагинов.  
[PluginFinderFactory](T_Chronos_Platform_Scheduling_PluginFinderFactory.htm)|
Хэлперы для создания объекта, позволяющий осуществлять поиск плагинов.  
[PluginGracefulLauncher](T_Chronos_Platform_Scheduling_PluginGracefulLauncher.htm)|
Запускает плагины с поддержкой отслеживания плагинов, поддерживающих вежливую
остановку, если в
[ShutdownMode](P_Chronos_Platform_Scheduling_PluginRemoteCreationInfo_ShutdownMode.htm)
задано [GracefulStop](T_Chronos_Platform_Scheduling_PluginShutdownMode.htm).  
[PluginGracefulStopEventToken](T_Chronos_Platform_Scheduling_PluginGracefulStopEventToken.htm)|
Токен, позволяющий определить состояние плагина из метода его вежливой
остановки посредством события
[ManualResetEvent](https://learn.microsoft.com/dotnet/api/system.threading.manualresetevent).  
[PluginGracefulStopExceptionEventArgs](T_Chronos_Platform_Scheduling_PluginGracefulStopExceptionEventArgs.htm)|
Аргументы события, возникающего при возникновении исключения в процессе
вежливой остановки плагина методом
[StopAsync(IGracefulStopToken)](M_Chronos_Contracts_ISupportGracefulStop_StopAsync.htm).  
[PluginGracefulStopTokenAdapter](T_Chronos_Platform_Scheduling_PluginGracefulStopTokenAdapter.htm)|
Адаптер для интерфейса
[IGracefulStopToken](T_Chronos_Contracts_IGracefulStopToken.htm),
инкапсулирующий все его доступные возможности, кроме тех, что определены в
интерфейсе.  
[PluginHostLauncher](T_Chronos_Platform_Scheduling_PluginHostLauncher.htm)|
Запускает плагины, вызывая создание дочернего процесса для
[IProcessHost](T_Chronos_Platform_Processes_IProcessHost.htm), которому в виде
аргументов командной строки передаются параметры запуска
[PluginRemoteCreationInfo](T_Chronos_Platform_Scheduling_PluginRemoteCreationInfo.htm).  
[PluginImporter](T_Chronos_Platform_Scheduling_PluginImporter.htm)|  Хранит
список плагинов и при необходимости обновляет его, дополняя список новыми
плагинами.  
[PluginImportEventArgs](T_Chronos_Platform_Scheduling_PluginImportEventArgs.htm)|
Аргументы события, содержащие информацию об импортированном плагине.  
[PluginImportingItem](T_Chronos_Platform_Scheduling_PluginImportingItem.htm)|
Информация об импортируемом плагине.  
[PluginImportingResult](T_Chronos_Platform_Scheduling_PluginImportingResult.htm)|
Результат импортирования плагинов, выполненный с помощью метода
[Import(IPluginFinder)](M_Chronos_Platform_Scheduling_PluginImporter_Import.htm).  
[PluginLauncherKey](T_Chronos_Platform_Scheduling_PluginLauncherKey.htm)|
Ключ зарегистрированного объекта
[IPluginLauncher](T_Chronos_Platform_Scheduling_IPluginLauncher.htm).  
[PluginLauncherResolver](T_Chronos_Platform_Scheduling_PluginLauncherResolver.htm)|
Контейнер, осуществляющий хранение объектов
[IPluginLauncher](T_Chronos_Platform_Scheduling_IPluginLauncher.htm).  
[PluginLaunchingData](T_Chronos_Platform_Scheduling_PluginLaunchingData.htm)|
Информация о плагине, запущенном с помощью метода
[LaunchAsync(PluginRemoteCreationInfo,
CancellationToken)](M_Chronos_Platform_Scheduling_IPluginLauncher_LaunchAsync.htm).  
[PluginLaunchingEventArgs](T_Chronos_Platform_Scheduling_PluginLaunchingEventArgs.htm)|
Аргументы события для запуска плагина в дочернем процессе.  
[PluginRemoteCreationInfo](T_Chronos_Platform_Scheduling_PluginRemoteCreationInfo.htm)|
Информация для создания плагина, которая может быть использована из другого
процесса.  
[PluginSyncLauncher](T_Chronos_Platform_Scheduling_PluginSyncLauncher.htm)|
Запускает плагин на выполнение, предварительно выполнив синхронизацию между
процессами плагинов.  
[SchedulingExtensions](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm)|
Методы-расширения для интерфейсов пространства имён Chronos.Scheduling.  
## __Интерфейсы
[IPluginFinder](T_Chronos_Platform_Scheduling_IPluginFinder.htm)|  Позволяет
выполнять поиск плагинов.  
---|---  
[IPluginLauncher](T_Chronos_Platform_Scheduling_IPluginLauncher.htm)|
Предоставляет возможность запустить плагин.  
## __Перечисления
[PluginShutdownMode](T_Chronos_Platform_Scheduling_PluginShutdownMode.htm)|
Способ завершения процесса хоста или плагина.  
---|---
