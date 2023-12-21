# Tessa.Platform - пространство имён
Вспомогательные классы общего назначения.
##  __Классы
[AssemblyHelper](T_Tessa_Platform_AssemblyHelper.htm)|  Предоставляет
вспомогательные методы для работы со сборками.  
---|---  
[AssemblyLoaderHelper](T_Tessa_Platform_AssemblyLoaderHelper.htm)|
Вспомогательные методы для поиска и загрузки любых сборок.  
[AsyncLazy<T>](T_Tessa_Platform_AsyncLazy_1.htm)|  Объект, поддерживающий
асинхронную ленивую инициализацию значения типа T в виде задачи Task<T>.
Пример: T value = await someLazy;  
[AsyncLock](T_Tessa_Platform_AsyncLock.htm)|  Класс, обеспечивающий блокировку
вида lock(resource) { ... } с возможностью выполнения асинхронных вызовов
внутри блока. Класс требует освобождение вызовом
[Dispose()](M_Tessa_Platform_AsyncLock_Dispose.htm).  
[AsyncReaderWriterLock](T_Tessa_Platform_AsyncReaderWriterLock.htm)|  Объект,
обеспечивающий блокировки на чтение и запись. Объект можно получить из Unity
как PerResolve зависимость.  
[AsyncSignatureProvider](T_Tessa_Platform_AsyncSignatureProvider.htm)|
Объект, предоставляющий криптографические средства для подписания и проверки
подписи асинхронным методом RSA с указанием открытого и закрытого ключей.  
[AsyncSynchronizedOneTimeRegistrator](T_Tessa_Platform_AsyncSynchronizedOneTimeRegistrator.htm)|
Позволяет выполнить отложенную одноразовую асинхронную регистрацию в
синхронизованном между потоками контексте.  
[BackgroundServiceQueue](T_Tessa_Platform_BackgroundServiceQueue.htm)|
Очередь, которая производит обработку доабвляемых действий в момент
добавления.  
[BackgroundServiceQueueProxy](T_Tessa_Platform_BackgroundServiceQueueProxy.htm)|
Очередь, которая переводит обработку действий в другую очередь.  
[BooleanBoxes](T_Tessa_Platform_BooleanBoxes.htm)|  Упакованные значения для
часто используемых
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean). Поля класса
можно использовать для оптимизации, чтобы не выполнялся лишний boxing при
преобразовании значения в
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
[BuildInfo](T_Tessa_Platform_BuildInfo.htm)|  Информация по версии сборки.  
[BuildInfoXmlObject](T_Tessa_Platform_BuildInfoXmlObject.htm)|  Информация по
версии сборки, сериализуемая в xml.  
[ButtonNames](T_Tessa_Platform_ButtonNames.htm)|  Имена стандартных кнопок,
создаваемых платформой.  
[Check](T_Tessa_Platform_Check.htm)|  Вспомогательные методы для проверки
некоторых стандартных условий.  
[CollectionRecord](T_Tessa_Platform_CollectionRecord.htm)|  Элемент
коллекционной секции.  
[CombSequentialGuidProvider](T_Tessa_Platform_CombSequentialGuidProvider.htm)|
Объект, выполняющий создание уникальный идентификаторов таким образом, чтобы
каждый следующий созданный идентификатор был последовательным, в соответствии
с правилами переданного объекта
[IGuidCombProvider](T_Tessa_Platform_GuidComb_IGuidCombProvider.htm).  
[ComparisonHelper](T_Tessa_Platform_ComparisonHelper.htm)|  Хэлперы для
сравнения значений и генерации хеш-кодов.  
[ConfigurationConnection](T_Tessa_Platform_ConfigurationConnection.htm)|
Объект, описывающий поставщик данных для строки подключения.  
[ConfigurationDataProvider](T_Tessa_Platform_ConfigurationDataProvider.htm)|
Объект, описывающий поставщик данных для строки подключения.  
[ConfigurationError](T_Tessa_Platform_ConfigurationError.htm)|  Ошибка,
возникшая при построении конфигурации. Вызовите метод
[ToString()](M_Tessa_Platform_ConfigurationError_ToString.htm), чтобы получить
подробное текстовое описание ошибки.  
[ConfigurationManager](T_Tessa_Platform_ConfigurationManager.htm)|  Объект,
управляющий конфигурацией приложений Tessa. К объекту возможно одновременное
обращение из нескольких потоков.  
[ConfigurationManagerContext](T_Tessa_Platform_ConfigurationManagerContext.htm)|
Контекст, переопределяющий текущий
[ConfigurationManager](T_Tessa_Platform_ConfigurationManager.htm).  
[ConfigurationManagerLazy](T_Tessa_Platform_ConfigurationManagerLazy.htm)|
Объект, управляющий конфигурацией приложений Tessa. В отличии от
[ConfigurationManager](T_Tessa_Platform_ConfigurationManager.htm) конфигурация
создается и инициализируется при первом обращении к свойствам
[IConfigurationManager](T_Tessa_Platform_IConfigurationManager.htm) или при
вызове
[InitializeAsync(CancellationToken)](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm).
К объекту возможно одновременное обращение из нескольких потоков.  
[ConfigurationObject](T_Tessa_Platform_ConfigurationObject.htm)|  Объект,
описывающий конфигурацию приложения Tessa.  
[ConversionHelper](T_Tessa_Platform_ConversionHelper.htm)|  Вспомогательные
методы для преобразования типов.  
[DbScopeSequentialGuidProvider](T_Tessa_Platform_DbScopeSequentialGuidProvider.htm)|
Объект, выполняющий создание уникальный идентификаторов таким образом, чтобы
каждый следующий созданный идентификатор был последовательным для СУБД,
которая является текущей в объекте
[IDbScope](T_Tessa_Platform_Data_IDbScope.htm).  
[DebugHelper](T_Tessa_Platform_DebugHelper.htm)|  Вспомогательные методы для
удобства отладки.  
[DefaultTessaPlatformDependencies](T_Tessa_Platform_DefaultTessaPlatformDependencies.htm)|
Зависимости платформы по умолчанию, которые зависят от операционной системы,
исполняющей среды .NET и др. В этом классе указываются значения, не связанные
с конкретной платформой. Рекомендуется использовать наследника этого класса,
который определяет зависимости для Windows, Linux и др. платформ.  
[DefaultTessaServerDependencies](T_Tessa_Platform_DefaultTessaServerDependencies.htm)|
Зависимости платформы по умолчанию, которые зависят от разновидности сервера
приложений, и определяет возможности такого сервера, требующие дополнительные
зависимости. В этом классе указываются значения, не связанные с конкретным
сервером.  
[DeferredCancelEventArgs](T_Tessa_Platform_DeferredCancelEventArgs.htm)|
Аргументы события, обеспечивающие асинхронное ожидание с отменой изменений.
Используйте метод [InvokeNullableAsync<T>(EventHandler<T>, Object, T,
CancellationToken)](M_Tessa_Platform_PlatformExtensions_InvokeNullableAsync__1.htm)
для ожидания обработчиков такого события.  
[DeferredEventArgs](T_Tessa_Platform_DeferredEventArgs.htm)|  Аргументы
события, обеспечивающие асинхронное ожидание. Используйте метод
[InvokeNullableAsync<T>(EventHandler<T>, Object, T,
CancellationToken)](M_Tessa_Platform_PlatformExtensions_InvokeNullableAsync__1.htm)
для ожидания обработчиков такого события.  
[DoubleBoxes](T_Tessa_Platform_DoubleBoxes.htm)|  Упакованные значения для
часто используемых
[Double](https://learn.microsoft.com/dotnet/api/system.double). Поля класса
можно использовать для оптимизации, чтобы не выполнялся лишний boxing при
преобразовании значения в
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
[EnvironmentHelper](T_Tessa_Platform_EnvironmentHelper.htm)|  Класс,
содержащий вспомогательную информацию о системе.  
[ExceptionHelper](T_Tessa_Platform_ExceptionHelper.htm)|  Вспоготальные методы
для работы с объектами исключений.  
[FakeDisposable](T_Tessa_Platform_FakeDisposable.htm)|  Реализация
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable),
которая ничего не делает в методе
[Dispose()](M_Tessa_Platform_FakeDisposable_Dispose.htm).  
[FakeSignatureProvider](T_Tessa_Platform_FakeSignatureProvider.htm)|
Реализация [ISignatureProvider](T_Tessa_Platform_ISignatureProvider.htm), не
выполняющая действий по подписыванию и проверке подписи. Метод
[Sign(Byte[])](M_Tessa_Platform_FakeSignatureProvider_Sign.htm) всегда
возвращает заданные данные без изменений, а метод [Verify(Byte[],
Byte[])](M_Tessa_Platform_FakeSignatureProvider_Verify.htm) всегда возвращает
true.  
[FakeSplash](T_Tessa_Platform_FakeSplash.htm)|  Объект, реализующий интерфейс
[ISplash](T_Tessa_Platform_ISplash.htm), но не выполняющий действий.  
[FormatingInfo](T_Tessa_Platform_FormatingInfo.htm)|  Описание формата вывода
элемента через [Format(String,
Object)](https://learn.microsoft.com/dotnet/api/system.string.format#system-
string-format\(system-string-system-object\))  
[FormatStringParser](T_Tessa_Platform_FormatStringParser.htm)|  Парсер строки
композитного формата  
[FormattingHelper](T_Tessa_Platform_FormattingHelper.htm)|  Вспомогательные
методы для форматирования данных в читаемом для пользователя виде.  
[GCHelper](T_Tessa_Platform_GCHelper.htm)|  Вспомогательные методы для
настройки сборщика мусора.  
[GuidBoxes](T_Tessa_Platform_GuidBoxes.htm)|  Упакованные значения для часто
используемых [Guid](https://learn.microsoft.com/dotnet/api/system.guid). Поля
класса можно использовать для оптимизации, чтобы не выполнялся лишний boxing
при преобразовании значения в
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
[GuidContext](T_Tessa_Platform_GuidContext.htm)|  Контекст операции, связанной
с заменой уникальных идентификаторов.  
[GuidReplacer](T_Tessa_Platform_GuidReplacer.htm)|  Объект, выполняющий
замещение идентификаторов на сгенерированные идентификаторы. Если
идентификатор уже был замещён, то для него возвращается такой же
идентификатор, какой был получен в прошлый раз. При этом идентификатор
[Empty](https://learn.microsoft.com/dotnet/api/system.guid.empty) не
заменяется, если объект создан конструктором по умолчанию.  
[HashSignatureProvider](T_Tessa_Platform_HashSignatureProvider.htm)|  Объект,
предоставляющий криптографические средства для вычисления хеша, использует
вычисленных хеш в методах подписания и проверки подписи.  
[HookableService<TService>](T_Tessa_Platform_HookableService_1.htm)|
Абстрактный объект сервиса, обеспечивающий расширяемость через коллекцию hook-
сервисов.  
[HookableServiceHook<TService>](T_Tessa_Platform_HookableServiceHook_1.htm)|
Абстрактный объект hook-сервиса, обеспечивающий расширяемость для объекта
[HookableService<TService>](T_Tessa_Platform_HookableService_1.htm).  
[HookableServiceProxy<TService>](T_Tessa_Platform_HookableServiceProxy_1.htm)|
Абстрактный прокси-объект для hook-сервиса, обеспечивающий расширяемость для
объекта [HookableService<TService>](T_Tessa_Platform_HookableService_1.htm) и
декорирующий другой объект
[HookableServiceHook<TService>](T_Tessa_Platform_HookableServiceHook_1.htm).  
[Int32Boxes](T_Tessa_Platform_Int32Boxes.htm)|  Упакованные значения для часто
используемых [Int32](https://learn.microsoft.com/dotnet/api/system.int32).
Поля класса можно использовать для оптимизации, чтобы не выполнялся лишний
boxing при преобразовании значения в
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
[Int64Boxes](T_Tessa_Platform_Int64Boxes.htm)|  Упакованные значения для часто
используемых [Int64](https://learn.microsoft.com/dotnet/api/system.int64).
Поля класса можно использовать для оптимизации, чтобы не выполнялся лишний
boxing при преобразовании значения в
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
[LazySplash](T_Tessa_Platform_LazySplash.htm)|  Объект, предоставляющий доступ
к окну с экраном загрузки, который создаётся отложенно при изменении свойства
[Text](P_Tessa_Platform_ISplash_Text.htm).  
[LdapSettings](T_Tessa_Platform_LdapSettings.htm)|  Настройки подключения к
LDAP.  
[LinkHelper](T_Tessa_Platform_LinkHelper.htm)|  Вспомогательные методы для
построения ссылок для клиентских и административных приложений Tessa.  
[LinuxTessaPlatformDependencies](T_Tessa_Platform_LinuxTessaPlatformDependencies.htm)|
Зависимости платформы для ОС Linux. Создайте экземпляр класса и установите в
свойстве [Dependencies](P_Tessa_Platform_TessaPlatform_Dependencies.htm).  
[NamedEntry](T_Tessa_Platform_NamedEntry.htm)|  Именованный объект с
идентификатором.  
[NamedObjectHelper](T_Tessa_Platform_NamedObjectHelper.htm)|  Вспомогательные
методы для [INamedObject](T_Tessa_Platform_Collections_INamedObject.htm)  
[NamedRegistry<T>](T_Tessa_Platform_NamedRegistry_1.htm)|  Потокобезопасный
реестр объектов, идентифицируемых по
[Guid](https://learn.microsoft.com/dotnet/api/system.guid) и по строковому
имени.  
[NamedResolver<TValue>](T_Tessa_Platform_NamedResolver_1.htm)|  Объект,
используемый для запросов типов сервисов по именам.  
[NotificationObject](T_Tessa_Platform_NotificationObject.htm)|  Объект,
уведомляющий об изменении свойств посредством реализации интерфейса
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged).  
[ObjectSealedException](T_Tessa_Platform_ObjectSealedException.htm)|  Была
произведена попытка изменения объекта, защищённого от изменений.  
[PlatformCacheNames](T_Tessa_Platform_PlatformCacheNames.htm)|  Кэши для
сброса, доступные в платформе.  
[PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm)|  Методы-
расширения для пространства имён Tessa.Platform, а также методы-расширения для
классов общего назначения из других библиотек.  
[ProcessNameResolver](T_Tessa_Platform_ProcessNameResolver.htm)|  Объект,
обеспечивающий получение отображаемого имени приложения по запускающему файлу
процесса, обычно по .exe.  
[Registry<TIdentifier, TItem>](T_Tessa_Platform_Registry_2.htm)|
Потокобезопасный реестр объектов, идентифицируемых по
[Guid](https://learn.microsoft.com/dotnet/api/system.guid).  
[RegistryItem<TIdentifier, TItem>](T_Tessa_Platform_RegistryItem_2.htm)|
Базовый класс для реализации интерфейса
[IRegistryItem<TIdentifier>](T_Tessa_Platform_IRegistryItem_1.htm), а также
для указания строкового представления объекта
[INamedItem](T_Tessa_Platform_Collections_INamedItem.htm).  
[Resolver<TKey, TValue>](T_Tessa_Platform_Resolver_2.htm)|  Объект,
используемый для запросов типов сервисов по ключу, например, по имени.  
[SerializationInfoExtensions](T_Tessa_Platform_SerializationInfoExtensions.htm)|
Вспомогательные методы для объекта
[SerializationInfo](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.serializationinfo),
который используется при сериализации.  
[SignatureProviderFactory](T_Tessa_Platform_SignatureProviderFactory.htm)|
Фабрика объектов
[ISignatureProvider](T_Tessa_Platform_ISignatureProvider.htm).  
[SignatureProviderNames](T_Tessa_Platform_SignatureProviderNames.htm)|  Имена
объектов [ISignatureProvider](T_Tessa_Platform_ISignatureProvider.htm),
которые регистрируются в Unity.  
[StaTaskScheduler](T_Tessa_Platform_StaTaskScheduler.htm)|  Provides a
scheduler that uses STA threads.  
[StringBuilderHelper](T_Tessa_Platform_StringBuilderHelper.htm)|
Вспомогательные методы для использования объектов
[StringBuilder](https://learn.microsoft.com/dotnet/api/system.text.stringbuilder)
для построения строк.  
[SynchronizedOneTimeRegistrator](T_Tessa_Platform_SynchronizedOneTimeRegistrator.htm)|
Позволяет выполнить отложенную одноразовую регистрацию в синхронизованном
между потоками контексте.  
[SyncSignatureProvider](T_Tessa_Platform_SyncSignatureProvider.htm)|  Объект,
предоставляющий криптографические средства для подписания и проверки подписи
синхронным методом
[HMACSHA256](https://learn.microsoft.com/dotnet/api/system.security.cryptography.hmacsha256)
с указанием ключа подписи.  
[TaskBoxes](T_Tessa_Platform_TaskBoxes.htm)|  Упакованные значения для часто
используемых
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task).
Поля класса можно использовать для оптимизации, чтобы не создавать объекты
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task) при
возврате из асинхронного метода типовых значений. Метод
[FromResult<TResult>(TResult)](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task.fromresult#system-
threading-tasks-task-fromresult-1\(-0\)) всегда возвращает новый объект
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task).  
[TessaClientSettings](T_Tessa_Platform_TessaClientSettings.htm)|  Настройки
Tessa на клиенте, которые выносятся в конфигурационный файл.  
[TessaExpressionHelper](T_Tessa_Platform_TessaExpressionHelper.htm)|
Вспомогательные методы для взаимодействия с выражениями LINQ.  
[TessaLoggers](T_Tessa_Platform_TessaLoggers.htm)|  Именованные объекты,
выполняющие логирование для различных API системы.  
[TessaPatchInfo](T_Tessa_Platform_TessaPatchInfo.htm)|  Информация по патчу,
установленному на сервер TESSA.  
[TessaPlatform](T_Tessa_Platform_TessaPlatform.htm)|  Обеспечивает доступ к
зависимостям платформы, используемым в Tessa.  
[TessaServerSettings](T_Tessa_Platform_TessaServerSettings.htm)|  Настройки
TESSA на сервере, которые выносятся в конфигурационный файл.  
[TextHelper](T_Tessa_Platform_TextHelper.htm)|  Вспомогательные методы для
работы с текстом.  
[TileNames](T_Tessa_Platform_TileNames.htm)|  Имена стандартных плиток,
которые создаются платформенными расширениями или расширениями типового
решения.  
[UnityDisposableContainer](T_Tessa_Platform_UnityDisposableContainer.htm)|
Контейнер, содержащий объекты
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable),
которые будут освобождены при закрытии контейнеров IUnityContainer.  
[WineRuntimeHelper](T_Tessa_Platform_WineRuntimeHelper.htm)|  
[WineTessaPlatformDependencies](T_Tessa_Platform_WineTessaPlatformDependencies.htm)|  
## __Структуры
[BeautifiedStackTrace](T_Tessa_Platform_BeautifiedStackTrace.htm)|
Используйте свойство
[Current](P_Tessa_Platform_BeautifiedStackTrace_Current.htm), чтобы получить
текущий стек-трейс без лишней информации, связанной с асинхронностью и другим
кодом, сгенерированным компилятором.  
---|---  
[EmbeddedResourcePath](T_Tessa_Platform_EmbeddedResourcePath.htm)|  Описывает
путь к встроенному ресурсу.  
[NullableObject<T>](T_Tessa_Platform_NullableObject_1.htm)|  Объект, который
может быть в состоянии "недоступен", даже если значение равно null. В этом
случае свойство [HasValue](P_Tessa_Platform_NullableObject_1_HasValue.htm)
вернёт false.  
[ReaderLockSlimWrapper](T_Tessa_Platform_ReaderLockSlimWrapper.htm)|
Структура, обеспечивающая синхронизацию доступа к ресурсу на чтение.  
[ReaderLockWrapper](T_Tessa_Platform_ReaderLockWrapper.htm)|  Структура,
обеспечивающая синхронизацию доступа к ресурсу на чтение.  
[WriterLockSlimWrapper](T_Tessa_Platform_WriterLockSlimWrapper.htm)|
Структура, обеспечивающая синхронизацию доступа к ресурсу на запись.  
[WriterLockWrapper](T_Tessa_Platform_WriterLockWrapper.htm)|  Структура,
обеспечивающая синхронизацию доступа к ресурсу на запись.  
## __Интерфейсы
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm)|  Интерфейс,
предоставляющий средства асинхронной инициализации объекта. Если объект
реализует интерфейс, то метод
[InitializeAsync(CancellationToken)](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm)
вызывается сразу после конструктора ровно один раз, он позволяет вынести
асинхронную часть конструктора в асинхронный метод. Интерфейс можно
задействовать в расширениях [IExtension](T_Tessa_Extensions_IExtension.htm) и
в ряде типовых сценариев, связанных с созданием объектов UI (контролов,
блоков, форм и др.), и их редакторов (для TessaAdmin).  
---|---  
[IAsyncReaderWriterLock](T_Tessa_Platform_IAsyncReaderWriterLock.htm)|
Объект, обеспечивающий блокировки на чтение и запись. Объект можно получить из
Unity как PerResolve зависимость.  
[IBackgroundServiceQueue](T_Tessa_Platform_IBackgroundServiceQueue.htm)|
Очередь асинхронной обработки действий в фоновом режиме.  
[IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm)|  Объект,
выполняющий свою сериализацию и десериализацию в бинарной форме посредством
классов
[BinaryWriter](https://learn.microsoft.com/dotnet/api/system.io.binarywriter)
и
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader).  
[IBsonSerializable](T_Tessa_Platform_IBsonSerializable.htm)|  Объект
поддерживает сериализацию и десериализацию в бинарный JSON. Используется
сериализация Tessa.Json.  
[ICollectionRecord](T_Tessa_Platform_ICollectionRecord.htm)|  Элемент
коллекционной секции.  
[IConfigurationManager](T_Tessa_Platform_IConfigurationManager.htm)|  Объект,
управляющий конфигурацией приложений Tessa. К объекту возможно одновременное
обращение из нескольких потоков.  
[IConfigurationManagerContext](T_Tessa_Platform_IConfigurationManagerContext.htm)|
Описывает контекст, переопределяющий текущий
[ConfigurationManager](T_Tessa_Platform_ConfigurationManager.htm).  
[ICurrentValueContainer](T_Tessa_Platform_ICurrentValueContainer.htm)|  Может
содержать текущее значение.  
[IGuidContext](T_Tessa_Platform_IGuidContext.htm)|  Контекст операции,
связанной с заменой уникальных идентификаторов.  
[IGuidReplacer](T_Tessa_Platform_IGuidReplacer.htm)|  Объект, выполняющий
замещение идентификаторов на сгенерированные идентификаторы.  
[IHashSignatureProvider](T_Tessa_Platform_IHashSignatureProvider.htm)|
Объект, предоставляющий криптографические средства для вычисления хеша,
использует вычисленных хеш в методах подписания и проверки подписи.  
[IJsonSerializable](T_Tessa_Platform_IJsonSerializable.htm)|  Объект
поддерживает сериализацию и десериализацию в JSON. Используется стандартная
сериализация Newtonsoft.Json.  
[ILdapAuthSettings](T_Tessa_Platform_ILdapAuthSettings.htm)|  Настройки
подключения к LDAP.  
[ILdapSettings](T_Tessa_Platform_ILdapSettings.htm)|  Настройки подключения к
LDAP.  
[INamedEntry](T_Tessa_Platform_INamedEntry.htm)|  Именованный объект с
идентификатором.  
[INamedRegistry<TItem>](T_Tessa_Platform_INamedRegistry_1.htm)|
Потокобезопасный реестр объектов, идентифицируемых по
[Guid](https://learn.microsoft.com/dotnet/api/system.guid) и по строковому
имени.  
[INotificationObject](T_Tessa_Platform_INotificationObject.htm)|  Объект,
поддерживающий уведомления об изменениях в своём состоянии.  
[IProcessNameResolver](T_Tessa_Platform_IProcessNameResolver.htm)|  Объект,
обеспечивающий получение отображаемого имени приложения по запускающему файлу
процесса, обычно по .exe.  
[IRegistry<TIdentifier, TItem>](T_Tessa_Platform_IRegistry_2.htm)|
Потокобезопасный реестр объектов, идентифицируемых по
[Guid](https://learn.microsoft.com/dotnet/api/system.guid).  
[IRegistryItem<TIdentifier>](T_Tessa_Platform_IRegistryItem_1.htm)|  Объект,
регистрируемый в реестре [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm).  
[IResolver<TKey, TValue>](T_Tessa_Platform_IResolver_2.htm)|  Объект,
используемый для запросов типов сервисов по ключу, например, по имени.  
[ISealable](T_Tessa_Platform_ISealable.htm)|  Поддерживает защиту от
изменений.  
[ISequentialGuidProvider](T_Tessa_Platform_ISequentialGuidProvider.htm)|
Объект, выполняющий создание уникальный идентификаторов таким образом, чтобы
каждый следующий созданный идентификатор был последовательным, как правило, в
отношении текущей используемой СУБД.  
[ISignatureProvider](T_Tessa_Platform_ISignatureProvider.htm)|  Объект,
предоставляющий криптографические средства для подписания и проверки подписи.  
[ISignatureProviderFactory](T_Tessa_Platform_ISignatureProviderFactory.htm)|
Фабрика объектов
[ISignatureProvider](T_Tessa_Platform_ISignatureProvider.htm).  
[ISplash](T_Tessa_Platform_ISplash.htm)|  Объект, предоставляющий доступ к
окну с экраном загрузки.  
[ITessaClientSettings](T_Tessa_Platform_ITessaClientSettings.htm)|  Настройки
Tessa на клиенте, которые выносятся в конфигурационный файл.  
[ITessaPatchInfo](T_Tessa_Platform_ITessaPatchInfo.htm)|  Информация по патчу,
установленному на сервер TESSA.  
[ITessaPlatformDependencies](T_Tessa_Platform_ITessaPlatformDependencies.htm)|
Зависимости платформы, которые зависят от операционной системы, исполняющей
среды .NET и др.  
[ITessaServerDependencies](T_Tessa_Platform_ITessaServerDependencies.htm)|
Зависимости платформы, которые зависят от разновидности сервера приложений, и
определяет возможности такого сервера, требующие дополнительные зависимости.  
[ITessaServerSettings](T_Tessa_Platform_ITessaServerSettings.htm)|  Настройки
TESSA на сервере, которые выносятся в конфигурационный файл.  
[IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm)|
Контейнер, содержащий объекты
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable),
которые будут освобождены при закрытии контейнеров IUnityContainer.  
## __Перечисления
[ComparisonHelper.ComparisonMode](T_Tessa_Platform_ComparisonHelper_ComparisonMode.htm)|
Способ сравнения объектов.  
---|---  
[PhotoOrientation](T_Tessa_Platform_PhotoOrientation.htm)|  Ориентация
фотографии. См. https://docs.microsoft.com/ru-
ru/windows/win32/properties/props-system-photo-orientation и
https://docs.microsoft.com/en-
us/uwp/api/windows.storage.fileproperties.photoorientation?view=winrt-22621.  
[SizeUnit](T_Tessa_Platform_SizeUnit.htm)|  Единица измерения размера
относительно размера в байтах.  
[TessaPlatformFeature](T_Tessa_Platform_TessaPlatformFeature.htm)|
Возможности текущей платформы (операционной системы, исполняющей среды).
Доступны в виде перечисления флагов.  
[TessaServerConfigFlags](T_Tessa_Platform_TessaServerConfigFlags.htm)|
Перечисление параметров загрузки настроек сервера TESSA
[TessaServerSettings](T_Tessa_Platform_TessaServerSettings.htm) из файла
конфигурации.  
[TileSize](T_Tessa_Platform_TileSize.htm)|  Размер плитки.
