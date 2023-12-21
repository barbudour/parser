# SyncHelper.CreateAndObtainMutexAsync - метод
Создаёт или захватывает мьютекс с указанным глобальным именем. Может
использоваться для синхронизации между процессами.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<IGlobalMutex> CreateAndObtainMutexAsync(
    	string mutexGlobalName,
    	int? millisecondsTimeout = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CreateAndObtainMutexAsync ( 
    	mutexGlobalName As String,
    	Optional millisecondsTimeout As Integer? = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IGlobalMutex)
C++ __Копировать
     public:
    static Task<IGlobalMutex^>^ CreateAndObtainMutexAsync(
    	String^ mutexGlobalName, 
    	Nullable<int> millisecondsTimeout = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CreateAndObtainMutexAsync : 
            mutexGlobalName : string * 
            ?millisecondsTimeout : Nullable<int> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _millisecondsTimeout = defaultArg millisecondsTimeout null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IGlobalMutex> 
#### Параметры
mutexGlobalName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Глобальное имя мьютекса, уникальное для системы.
millisecondsTimeout
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>
(Optional)
    Таймаут ожидания синхронизации между процессами. Если указан null>, то будет использоваться значение из конфигурационного файла app.json из настройки ChronosSyncTimeout.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IGlobalMutex](T_Chronos_Platform_IPC_IGlobalMutex.htm)>  
Мьютекс с указанным глобальным именем.
##  __См. также
#### Ссылки
[SyncHelper - ](T_Chronos_Platform_SyncHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
