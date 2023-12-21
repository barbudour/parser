# CardMetadataCache.InvalidateLocalCacheOverrideAsync - метод
Метод, реализующий сброс кэша в текущем экземпляре. Метод является
потокобезопасным и может обращаться к кэшу без дополнительной синхронизации.
Любые необработанные исключения, возникшие внутри делегата, игнорируются с
записью в лог.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override Task InvalidateLocalCacheOverrideAsync(
    	SharedEventArgs e,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function InvalidateLocalCacheOverrideAsync ( 
    	e As SharedEventArgs,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     protected:
    virtual Task^ InvalidateLocalCacheOverrideAsync(
    	SharedEventArgs^ e, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract InvalidateLocalCacheOverrideAsync : 
            e : SharedEventArgs * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override InvalidateLocalCacheOverrideAsync : 
            e : SharedEventArgs * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
e [SharedEventArgs](T_Tessa_Platform_IPC_SharedEventArgs.htm)
    Аргументы события, сериализуемые между процессами.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardMetadataCache - ](T_Tessa_Cards_Metadata_CardMetadataCache.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
