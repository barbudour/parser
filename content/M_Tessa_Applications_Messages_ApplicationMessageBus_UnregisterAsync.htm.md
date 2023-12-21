# ApplicationMessageBus.UnregisterAsync - метод
Выполняет отмену регистрации приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Messages](N_Tessa_Applications_Messages.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask UnregisterAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function UnregisterAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask UnregisterAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract UnregisterAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override UnregisterAsync : 
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
#### Реализации
[IApplicationMessageBus.UnregisterAsync(CancellationToken)](M_Tessa_Applications_Messages_IApplicationMessageBus_UnregisterAsync.htm)  
##  __См. также
#### Ссылки
[ApplicationMessageBus -
](T_Tessa_Applications_Messages_ApplicationMessageBus.htm)
[Tessa.Applications.Messages - пространство
имён](N_Tessa_Applications_Messages.htm)
