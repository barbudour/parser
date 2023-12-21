# GlobalMutexBase.CleanCoreAsync - метод
Освобождает ресурсы мьютекса, делая невозможным его дальнейшее использование,
и удаляет связанный с ним файл при его наличии. В реализации по умолчанию
выполняет работу по очистке на Linux и игнорируется на Windows.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask CleanCoreAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function CleanCoreAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask CleanCoreAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CleanCoreAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override CleanCoreAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[GlobalMutexBase - ](T_Tessa_Platform_IPC_GlobalMutexBase.htm)
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
