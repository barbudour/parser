# ExtensionContainer - класс
Контейнер расширений. Все методы объекта являются потокобезопасными.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ExtensionContainer : IExtensionContainer
VB __Копировать
     Public NotInheritable Class ExtensionContainer
    	Implements IExtensionContainer
C++ __Копировать
     public ref class ExtensionContainer sealed : IExtensionContainer
F# __Копировать
     [<SealedAttribute>]
    type ExtensionContainer = 
        class
            interface IExtensionContainer
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ExtensionContainer
Implements
    [IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
##  __Конструкторы
[ExtensionContainer](M_Tessa_Extensions_ExtensionContainer__ctor.htm)| Создаёт
экземпляр класса с параметрами по умолчанию.  
---|---  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateInitialization<TExtension>](M_Tessa_Extensions_ExtensionContainer_InvalidateInitialization__1.htm)|
Принудительно устанавливает необходимость повторного выполнения этапов
инициализации и упорядочивания для заданного типа расширения. Вызывать метод
не требуется в случае, если была повторно зарегистрирована стратегия
инициализации.  
[InvalidateRegulation<TExtension>](M_Tessa_Extensions_ExtensionContainer_InvalidateRegulation__1.htm)|
Принудительно устанавливает необходимость повторного выполнения этапа
упорядочивания для заданного типа расширения. Вызывать метод не требуется в
случае, если была повторно зарегистрирована стратегия инициализации или
упорядочивания, или если для заданного типа расширения была выполнена
регистрация типа экземпляра расширения.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RegisterExtension<TExtension,
TConcreteExtension>](M_Tessa_Extensions_ExtensionContainer_RegisterExtension__2.htm)|
Регистрирует конкретное расширение в контейнере. Существующая регистрация
замещается.  
[RegisterStrategy](M_Tessa_Extensions_ExtensionContainer_RegisterStrategy.htm)|
Регистрирует стратегию в контейнере. Существующая регистрация замещается.  
[RegisterTraceListener<TExtension>](M_Tessa_Extensions_ExtensionContainer_RegisterTraceListener__1.htm)|
Регистрирует объект, выполняющий отслеживание событий, происходящих при
выполнении расширений заданного типа. Если для заданного типа расширения
TExtension уже был зарегистрирован такой объект, то он заменяется на указанный
объект traceListener.  
[RegisterType<TExtension>](M_Tessa_Extensions_ExtensionContainer_RegisterType__1.htm)|
Регистрирует тип расширения в контейнере. Существующая регистрация замещается.  
[RemoveTraceListener<TExtension>](M_Tessa_Extensions_ExtensionContainer_RemoveTraceListener__1.htm)|
Удаляет регистрацию объекта, выполняющего отслеживание событий, происходящих
при выполнении расширений заданного типа.  
[ResolveExecutorAsync<TExtension>(CancellationToken)](M_Tessa_Extensions_ExtensionContainer_ResolveExecutorAsync__1_1.htm)|
Возвращает объект, выполняющий расширения заданного типа и определяющий время
жизни экземпляров расширений. Метод никогда не возвращает null. Если тип
расширения не был зарегистрирован в контейнере, то метод не выбрасывает
исключение, а возвращает объект, не выполняющий действий.  
[ResolveExecutorAsync<TExtension>(Boolean,
CancellationToken)](M_Tessa_Extensions_ExtensionContainer_ResolveExecutorAsync__1.htm)|
Возвращает объект, выполняющий расширения заданного типа и определяющий время
жизни экземпляров расширений. Метод никогда не возвращает null.
Если тип расширения не был зарегистрирован в контейнере, то метод не
выбрасывает исключение, а возвращает объект, не выполняющий действий.
Обращение к созданному объекту запрещено из разных потоков, используйте
перегрузку с параметром synchronized, если выполнение цепочек расширений
возможно из разных потоков.  
[ResolveStrategy](M_Tessa_Extensions_ExtensionContainer_ResolveStrategy.htm)|
Возвращает стратегию, зарегистрированную на заданном этапе, или
[EmptyExtensionStrategy](T_Tessa_Extensions_EmptyExtensionStrategy.htm), если
стратегия не была зарегистрирована.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryResolveExecutorAsync<TExtension>(CancellationToken)](M_Tessa_Extensions_ExtensionContainer_TryResolveExecutorAsync__1_1.htm)|
Возвращает объект, выполняющий расширения заданного типа и определяющий время
жизни экземпляров расширений, или null, если тип расширений не был
зарегистрирован.  
[TryResolveExecutorAsync<TExtension>(Boolean,
CancellationToken)](M_Tessa_Extensions_ExtensionContainer_TryResolveExecutorAsync__1.htm)|
Возвращает объект, выполняющий расширения заданного типа и определяющий время
жизни экземпляров расширений, или null, если тип расширений не был
зарегистрирован.
Обращение к созданному объекту запрещено из разных потоков, используйте
перегрузку с параметром synchronized, если выполнение цепочек расширений
возможно из разных потоков.  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[RegisterApplicationExtensionTypes](M_Tessa_Platform_Runtime_RuntimeExtensions_RegisterApplicationExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений для API инициализации на
клиенте.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[RegisterApplicationsTraceListeners](M_Tessa_Platform_Runtime_RuntimeExtensions_RegisterApplicationsTraceListeners.htm)|
Выполняет регистрацию объектов, отслеживающих события, происходящие при
выполнении расширений на инициализацию приложения со стороны сервера, и
записывающие результат выполнения в
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm) как
информационное сообщение. Это полезно при отладке расширений, но сильно
нагружает любое взаимодействие с плитками, поэтому рекомендуется не выполнять
такую регистрацию в среде, с которой работают конечные пользователи.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[RegisterCardExtensionTypes](M_Tessa_Cards_CardExtensions_RegisterCardExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений для карточек.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[RegisterCardTraceListeners](M_Tessa_Cards_CardExtensions_RegisterCardTraceListeners.htm)|
Выполняет регистрацию объектов, отслеживающих события, происходящие при
выполнении расширений карточек, и записывающие результат выполнения в
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)
как информационное сообщение. Это полезно при отладке расширений, но сильно
нагружает любое взаимодействие с карточками, поэтому рекомендуется не
выполнять такую регистрацию в среде, с которой работают конечные пользователи.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[RegisterCardUIExtensionTypes](M_Tessa_UI_Cards_CardUIExtensions_RegisterCardUIExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений для плиток.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[RegisterCardUITraceListeners](M_Tessa_UI_Cards_CardUIExtensions_RegisterCardUITraceListeners.htm)|
Выполняет регистрацию объектов, отслеживающих события, происходящие при
выполнении расширений карточек в UI, и записывающие результат выполнения в
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)
как информационное сообщение. Это полезно при отладке расширений, но сильно
нагружает любое взаимодействие с плитками, поэтому рекомендуется не выполнять
такую регистрацию в среде, с которой работают конечные пользователи.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[RegisterClientConsoleExtensionTypes](M_Tessa_Platform_PlatformExtensions_RegisterClientConsoleExtensionTypes.htm)|
Выполняет регистрацию типов расширений для консольных клиентских приложений в
контейнере [IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm).  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RegisterClientExtensionTypes](M_Tessa_UI_UIExtensions_RegisterClientExtensionTypes.htm)|
Выполняет регистрацию клиентских типов расширений в контейнере
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm).  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
[RegisterClientInitializationExtensionTypes](M_Tessa_Platform_Initialization_InitializationExtensions_RegisterClientInitializationExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений для API инициализации на
клиенте.  
(Определяется
[InitializationExtensions](T_Tessa_Platform_Initialization_InitializationExtensions.htm))  
[RegisterDefaults](M_Tessa_Extensions_ExtensionExtensions_RegisterDefaults.htm)|
Регистрирует стратегии и политики по умолчанию для этапов
[Initialize](T_Tessa_Extensions_ExtensionStrategyStage.htm),
[Regulate](T_Tessa_Extensions_ExtensionStrategyStage.htm),
[Resolve](T_Tessa_Extensions_ExtensionStrategyStage.htm),
[Filter](T_Tessa_Extensions_ExtensionStrategyStage.htm),
[Execute](T_Tessa_Extensions_ExtensionStrategyStage.htm) и
[TearDown](T_Tessa_Extensions_ExtensionStrategyStage.htm).  
(Определяется
[ExtensionExtensions](T_Tessa_Extensions_ExtensionExtensions.htm))  
[RegisterFileConverterExtensionTypes](M_Tessa_FileConverters_FileConverterExtensions_RegisterFileConverterExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений для конвертеров файлов.  
(Определяется
[FileConverterExtensions](T_Tessa_FileConverters_FileConverterExtensions.htm))  
[RegisterFileExtensionTypes](M_Tessa_UI_Files_FileUIExtensions_RegisterFileExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений для API файлов.  
(Определяется [FileUIExtensions](T_Tessa_UI_Files_FileUIExtensions.htm))  
[RegisterFileTraceListeners](M_Tessa_UI_Files_FileUIExtensions_RegisterFileTraceListeners.htm)|
Выполняет регистрацию объектов, отслеживающих события, происходящие при
выполнении расширений файлов в UI, и записывающие результат выполнения в
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)
как информационное сообщение. Это полезно при отладке расширений, но сильно
нагружает любое взаимодействие с плитками, поэтому рекомендуется не выполнять
такую регистрацию в среде, с которой работают конечные пользователи.  
(Определяется [FileUIExtensions](T_Tessa_UI_Files_FileUIExtensions.htm))  
[RegisterFormUIExtensionTypes](M_Tessa_UI_UIExtensions_RegisterFormUIExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений для диалогов, построенных
по формам карточек [IFormUIExtension](T_Tessa_UI_IFormUIExtension.htm).  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
[RegisterInitializationTraceListenersOnClient](M_Tessa_Platform_Initialization_InitializationExtensions_RegisterInitializationTraceListenersOnClient.htm)|
Выполняет регистрацию объектов, отслеживающих события, происходящие при
выполнении расширений на инициализацию приложения со стороны клиента, и
записывающие результат выполнения в
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)
как информационное сообщение. Это полезно при отладке расширений, но сильно
нагружает любое взаимодействие с плитками, поэтому рекомендуется не выполнять
такую регистрацию в среде, с которой работают конечные пользователи.  
(Определяется
[InitializationExtensions](T_Tessa_Platform_Initialization_InitializationExtensions.htm))  
[RegisterInitializationTraceListenersOnServer](M_Tessa_Platform_Initialization_InitializationExtensions_RegisterInitializationTraceListenersOnServer.htm)|
Выполняет регистрацию объектов, отслеживающих события, происходящие при
выполнении расширений на инициализацию приложения со стороны сервера, и
записывающие результат выполнения в
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)
как информационное сообщение. Это полезно при отладке расширений, но сильно
нагружает любое взаимодействие с плитками, поэтому рекомендуется не выполнять
такую регистрацию в среде, с которой работают конечные пользователи.  
(Определяется
[InitializationExtensions](T_Tessa_Platform_Initialization_InitializationExtensions.htm))  
[RegisterKrEventExtensionTypes](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensions_RegisterKrEventExtensionTypes.htm)|  
(Определяется
[KrEventExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Events_KrEventExtensions.htm))  
[RegisterKrStageRowExtensionTypes](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtensions_RegisterKrStageRowExtensionTypes.htm)|  
(Определяется
[KrStageRowExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtensions.htm))  
[RegisterPdfStampExtensionTypes](M_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensions_RegisterPdfStampExtensionTypes.htm)|  
(Определяется
[PdfStampExtensions](T_Tessa_Extensions_Default_Client_Pdf_PdfStampExtensions.htm))  
[RegisterPlaceholderTypes](M_Tessa_Platform_Placeholders_PlaceholderExtensions_RegisterPlaceholderTypes.htm)|
Выполняет регистрацию стандартных типов расширений для конвертеров файлов.  
(Определяется
[PlaceholderExtensions](T_Tessa_Platform_Placeholders_PlaceholderExtensions.htm))  
[RegisterPluginExtensionTypes](M_Tessa_Platform_Plugins_PluginExtensions_RegisterPluginExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений плагинов
[IPluginExtension](T_Tessa_Platform_Plugins_IPluginExtension.htm).  
(Определяется
[PluginExtensions](T_Tessa_Platform_Plugins_PluginExtensions.htm))  
[RegisterScanningExtensionTypes](M_Tessa_Extensions_Platform_Client_Scanning_ScanningExtensions_RegisterScanningExtensionTypes.htm)|  
(Определяется
[ScanningExtensions](T_Tessa_Extensions_Platform_Client_Scanning_ScanningExtensions.htm))  
[RegisterServerExtensionTypes](M_Tessa_Platform_PlatformExtensions_RegisterServerExtensionTypes.htm)|
Выполняет регистрацию серверных типов расширений в контейнере
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm).  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RegisterServerInitializationExtensionTypes](M_Tessa_Platform_Initialization_InitializationExtensions_RegisterServerInitializationExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений для API инициализации на
сервере.  
(Определяется
[InitializationExtensions](T_Tessa_Platform_Initialization_InitializationExtensions.htm))  
[RegisterSettingsExtensionTypes](M_Tessa_Platform_Settings_SettingsExtensions_RegisterSettingsExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений для системы настроек
расширений. Расширения могут использоваться на клиенте или на сервере.  
(Определяется
[SettingsExtensions](T_Tessa_Platform_Settings_SettingsExtensions.htm))  
[RegisterSharedExtensionTypes](M_Tessa_Platform_PlatformExtensions_RegisterSharedExtensionTypes.htm)|
Выполняет регистрацию типов расширений, актуальных и на клиенте, и на сервере,
в контейнере
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm).  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RegisterTileExtensionTypes](M_Tessa_UI_Tiles_TileExtensions_RegisterTileExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений для API плиток.  
(Определяется [TileExtensions](T_Tessa_UI_Tiles_TileExtensions.htm))  
[RegisterTileTraceListeners](M_Tessa_UI_Tiles_TileExtensions_RegisterTileTraceListeners.htm)|
Выполняет регистрацию объектов, отслеживающих события, происходящие при
выполнении расширений плиток, и записывающие результат выполнения в
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)
как информационное сообщение. Это полезно при отладке расширений, но сильно
нагружает любое взаимодействие с плитками, поэтому рекомендуется не выполнять
такую регистрацию в среде, с которой работают конечные пользователи.  
(Определяется [TileExtensions](T_Tessa_UI_Tiles_TileExtensions.htm))  
[RemoveApplicationsTraceListeners](M_Tessa_Platform_Runtime_RuntimeExtensions_RemoveApplicationsTraceListeners.htm)|
Удаляет объекты, зарегистрированные методом
[RegisterApplicationsTraceListeners(IExtensionContainer,
ExtensionTraceListenerType,
Nullable<Int64>)](M_Tessa_Platform_Runtime_RuntimeExtensions_RegisterApplicationsTraceListeners.htm).
Частая регистрация с последующим удалением объектов значительно нагружает
память и CPU.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[RemoveCardTraceListeners](M_Tessa_Cards_CardExtensions_RemoveCardTraceListeners.htm)|
Удаляет объекты, зарегистрированные методом
[RegisterCardTraceListeners(IExtensionContainer, ExtensionTraceListenerType,
Nullable<Int64>)](M_Tessa_Cards_CardExtensions_RegisterCardTraceListeners.htm).
Частая регистрация с последующим удалением объектов значительно нагружает
память и CPU.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[RemoveCardUITraceListeners](M_Tessa_UI_Cards_CardUIExtensions_RemoveCardUITraceListeners.htm)|
Удаляет объекты, зарегистрированные методом
[RegisterCardUITraceListeners(IExtensionContainer, ExtensionTraceListenerType,
Nullable<Int64>)](M_Tessa_UI_Cards_CardUIExtensions_RegisterCardUITraceListeners.htm).
Частая регистрация с последующим удалением объектов значительно нагружает
память и CPU.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[RemoveFileTileTraceListeners](M_Tessa_UI_Files_FileUIExtensions_RemoveFileTileTraceListeners.htm)|
Удаляет объекты, зарегистрированные методом
[RegisterFileTraceListeners(IExtensionContainer, ExtensionTraceListenerType,
Nullable<Int64>)](M_Tessa_UI_Files_FileUIExtensions_RegisterFileTraceListeners.htm).
Частая регистрация с последующим удалением объектов значительно нагружает
память и CPU.  
(Определяется [FileUIExtensions](T_Tessa_UI_Files_FileUIExtensions.htm))  
[RemoveInitializationTraceListenersOnClient](M_Tessa_Platform_Initialization_InitializationExtensions_RemoveInitializationTraceListenersOnClient.htm)|
Удаляет объекты, зарегистрированные методом
[RegisterInitializationTraceListenersOnClient(IExtensionContainer,
ExtensionTraceListenerType,
Nullable<Int64>)](M_Tessa_Platform_Initialization_InitializationExtensions_RegisterInitializationTraceListenersOnClient.htm).
Частая регистрация с последующим удалением объектов значительно нагружает
память и CPU.  
(Определяется
[InitializationExtensions](T_Tessa_Platform_Initialization_InitializationExtensions.htm))  
[RemoveInitializationTraceListenersOnServer](M_Tessa_Platform_Initialization_InitializationExtensions_RemoveInitializationTraceListenersOnServer.htm)|
Удаляет объекты, зарегистрированные методом
[RegisterInitializationTraceListenersOnServer(IExtensionContainer,
ExtensionTraceListenerType,
Nullable<Int64>)](M_Tessa_Platform_Initialization_InitializationExtensions_RegisterInitializationTraceListenersOnServer.htm).
Частая регистрация с последующим удалением объектов значительно нагружает
память и CPU.  
(Определяется
[InitializationExtensions](T_Tessa_Platform_Initialization_InitializationExtensions.htm))  
[RemoveTileTraceListeners](M_Tessa_UI_Tiles_TileExtensions_RemoveTileTraceListeners.htm)|
Удаляет объекты, зарегистрированные методом
[RegisterTileTraceListeners(IExtensionContainer, ExtensionTraceListenerType,
Nullable<Int64>)](M_Tessa_UI_Tiles_TileExtensions_RegisterTileTraceListeners.htm).
Частая регистрация с последующим удалением объектов значительно нагружает
память и CPU.  
(Определяется [TileExtensions](T_Tessa_UI_Tiles_TileExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
