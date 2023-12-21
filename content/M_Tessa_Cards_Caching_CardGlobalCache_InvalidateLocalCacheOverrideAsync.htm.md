# CardGlobalCache.InvalidateLocalCacheOverrideAsync - метод
Метод, реализующий сброс кэша в текущем экземпляре. Метод является
потокобезопасным и может обращаться к кэшу без дополнительной синхронизации.
Любые необработанные исключения, возникшие внутри делегата, игнорируются с
записью в лог.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override Task InvalidateLocalCacheOverrideAsync(
    	CardCacheEventArgs e,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function InvalidateLocalCacheOverrideAsync ( 
    	e As CardCacheEventArgs,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     protected:
    virtual Task^ InvalidateLocalCacheOverrideAsync(
    	CardCacheEventArgs^ e, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract InvalidateLocalCacheOverrideAsync : 
            e : CardCacheEventArgs * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override InvalidateLocalCacheOverrideAsync : 
            e : CardCacheEventArgs * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
e [CardCacheEventArgs](T_Tessa_Cards_Caching_CardCacheEventArgs.htm)
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
[CardGlobalCache - ](T_Tessa_Cards_Caching_CardGlobalCache.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
