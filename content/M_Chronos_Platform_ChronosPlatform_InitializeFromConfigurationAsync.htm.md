# ChronosPlatform.InitializeFromConfigurationAsync - метод
Выполняет инициализацию зависимостей от платформы в соответствии со
значениями, указанными в конфигурации. Рекомендуется вызвать метод до того,
как будут вызваны другие методы платформы. Также выполняет асинхронную
инициализацию конфигурации по умолчанию
[GetDefaultAsync(CancellationToken)](M_Chronos_Platform_Configuration_ConfigurationManager_GetDefaultAsync.htm),
если configurationManager равен null и если инициализация ещё не выполнена.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask InitializeFromConfigurationAsync(
    	bool runInitialization = true,
    	IConfigurationManager configurationManager = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function InitializeFromConfigurationAsync ( 
    	Optional runInitialization As Boolean = true,
    	Optional configurationManager As IConfigurationManager = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    static ValueTask InitializeFromConfigurationAsync(
    	bool runInitialization = true, 
    	IConfigurationManager^ configurationManager = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member InitializeFromConfigurationAsync : 
            ?runInitialization : bool * 
            ?configurationManager : IConfigurationManager * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _runInitialization = defaultArg runInitialization true
            let _configurationManager = defaultArg configurationManager null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
runInitialization
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что для зависимостей [IChronosPlatformDependencies](T_Chronos_Platform_IChronosPlatformDependencies.htm) необходимо выполнить инициализацию. Если в конфигурации отсутствуют зависимости, то инициализация выполняется для ранее заданного объекта зависимостей (для объекта по умолчанию, если не был задан). 
configurationManager
[IConfigurationManager](T_Chronos_Platform_Configuration_IConfigurationManager.htm)
(Optional)
     Объект, управляющий конфигурацией, который используется для инициализации настроек, или null, если используется объект по умолчанию. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ChronosPlatform - ](T_Chronos_Platform_ChronosPlatform.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
