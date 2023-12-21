# ConfigurationManager.CreateDefaultAsync - метод
Создает конфигурацию приложения
## __Definition
 **Пространство имён:**
[Chronos.Platform.Configuration](N_Chronos_Platform_Configuration.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<ConfigurationManager> CreateDefaultAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CreateDefaultAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ConfigurationManager)
C++ __Копировать
     public:
    static ValueTask<ConfigurationManager^> CreateDefaultAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CreateDefaultAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ConfigurationManager> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ConfigurationManager](T_Chronos_Platform_Configuration_ConfigurationManager.htm)>  
Асинхронная задача.
##  __См. также
#### Ссылки
[ConfigurationManager -
](T_Chronos_Platform_Configuration_ConfigurationManager.htm)
[Chronos.Platform.Configuration - пространство
имён](N_Chronos_Platform_Configuration.htm)
