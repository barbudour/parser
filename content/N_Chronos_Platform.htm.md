# Chronos.Platform - пространство имён
Вспомогательные классы, используемые в Chronos.Platform.dll.
##  __Классы
[Check](T_Chronos_Platform_Check.htm)|  Вспомогательные методы для проверки
некоторых стандартных условий.  
---|---  
[ChronosLoggers](T_Chronos_Platform_ChronosLoggers.htm)|  Именованные объекты,
выполняющие логирование для различных API системы.  
[ChronosPlatform](T_Chronos_Platform_ChronosPlatform.htm)|  Обеспечивает
доступ к зависимостям платформы, используемым в Chronos.  
[ChronosSerializationException](T_Chronos_Platform_ChronosSerializationException.htm)|
Исключение при сериализации или десериализации объектов посредством
[ChronosSerializer](T_Chronos_Platform_ChronosSerializer.htm).  
[ChronosSerializer](T_Chronos_Platform_ChronosSerializer.htm)|  
[CommonHelper](T_Chronos_Platform_CommonHelper.htm)|  Хэлперы общего
назначения.  
[ConsoleHelper](T_Chronos_Platform_ConsoleHelper.htm)|  Хэлперы для
взаимодействия с консолью.  
[DefaultChronosPlatformDependencies](T_Chronos_Platform_DefaultChronosPlatformDependencies.htm)|
Зависимости платформы по умолчанию, которые зависят от операционной системы,
исполняющей среды .NET и др. В этом классе указываются значения, не связанные
с конкретной платформой. Рекомендуется использовать наследника этого класса,
который определяет зависимости для Windows, Linux и др. платформ.  
[EmptyHolder<T>](T_Chronos_Platform_EmptyHolder_1.htm)|  Содержит кэш значений
для массивов и коллекций, доступных только для чтения.  
[FileHelper](T_Chronos_Platform_FileHelper.htm)|  Вспомогательные методы для
взаимодействия с файлами.  
[IOExtensions](T_Chronos_Platform_IOExtensions.htm)|  
[IsolatedStorageHelper](T_Chronos_Platform_IsolatedStorageHelper.htm)|
Хэлперы по работе с изолированным хранилищем.  
[LinuxChronosPlatformDependencies](T_Chronos_Platform_LinuxChronosPlatformDependencies.htm)|
Зависимости платформы для ОС Windows. Создайте экземпляр класса и установите в
свойстве [Dependencies](P_Chronos_Platform_ChronosPlatform_Dependencies.htm).  
[PlatformExtensions](T_Chronos_Platform_PlatformExtensions.htm)|  Методы-
расширения для пространства имён Chronos.Platform.  
[PluginConfigHelper](T_Chronos_Platform_PluginConfigHelper.htm)|  Хэлперы для
работы с конфигурационным файлом, описывающим плагин.  
[PluginIncludeConfigHelper](T_Chronos_Platform_PluginIncludeConfigHelper.htm)|
Хэлперы для работы с конфигурационным файлом, описывающим сборки с плагинами.  
[PluginSchedulingHelper](T_Chronos_Platform_PluginSchedulingHelper.htm)|
Хэлперы для диспетчеризации плагинов.  
[ProcessLogger](T_Chronos_Platform_ProcessLogger.htm)|  Средства логирования
для жизненного цикла процессов.  
[ProcessRefHelper](T_Chronos_Platform_ProcessRefHelper.htm)|  Хэлперы для
работы с объектами [ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm).  
[RuntimeHelper](T_Chronos_Platform_RuntimeHelper.htm)|  Вспомогательные методы
для пространства имён Chronos.Platform.  
[StorageHelper](T_Chronos_Platform_StorageHelper.htm)|  Хэлперы для
взаимодействия с хранилищем.  
[SyncHelper](T_Chronos_Platform_SyncHelper.htm)|  Хэлперы для синхронизации
между потоками или процессами.  
[TaskBoxes](T_Chronos_Platform_TaskBoxes.htm)|  Упакованные значения для часто
используемых
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task).
Поля класса можно использовать для оптимизации, чтобы не создавать объекты
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task) при
возврате из асинхронного метода типовых значений. Метод
[FromResult<TResult>(TResult)](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task.fromresult#system-
threading-tasks-task-fromresult-1\(-0\)) всегда возвращает новый объект
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task).  
[WindowsConsoleHelper](T_Chronos_Platform_WindowsConsoleHelper.htm)|  Хэлперы
для взаимодействия с консолью, которые специфичны для платформы Windows.  
[XmlHelper](T_Chronos_Platform_XmlHelper.htm)|  Хэлперы для работы с LINQ to
XML.  
## __Структуры
[BeautifiedStackTrace](T_Chronos_Platform_BeautifiedStackTrace.htm)|
Используйте свойство
[Current](P_Chronos_Platform_BeautifiedStackTrace_Current.htm), чтобы получить
текущий стек-трейс без лишней информации, связанной с асинхронностью и другим
кодом, сгенерированным компилятором.  
---|---  
## __Интерфейсы
[IAsyncInitializable](T_Chronos_Platform_IAsyncInitializable.htm)|  Интерфейс,
предоставляющий средства асинхронной инициализации объекта. Если объект
реализует интерфейс, то метод
[InitializeAsync(CancellationToken)](M_Chronos_Platform_IAsyncInitializable_InitializeAsync.htm)
вызывается сразу после конструктора ровно один раз, он позволяет вынести
асинхронную часть конструктора в асинхронный метод.  
---|---  
[IChronosPlatformDependencies](T_Chronos_Platform_IChronosPlatformDependencies.htm)|
Зависимости платформы, которые зависят от операционной системы, исполняющей
среды .NET и др.  
## __Перечисления
[FileSpecialFolder](T_Chronos_Platform_FileSpecialFolder.htm)|  Тип
специальной папки, используемой в системе.  
---|---
