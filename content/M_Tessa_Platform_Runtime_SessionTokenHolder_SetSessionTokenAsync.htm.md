# SessionTokenHolder.SetSessionTokenAsync - метод
Устанавливает токен для текущей сессии. Может быть равен null, если считается,
что токен ещё не был задан.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask SetSessionTokenAsync(
    	ISessionToken value,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function SetSessionTokenAsync ( 
    	value As ISessionToken,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask SetSessionTokenAsync(
    	ISessionToken^ value, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract SetSessionTokenAsync : 
            value : ISessionToken * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override SetSessionTokenAsync : 
            value : ISessionToken * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
value [ISessionToken](T_Tessa_Platform_Runtime_ISessionToken.htm)
    Новое значение токена.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
#### Реализации
[ISessionTokenHolder.SetSessionTokenAsync(ISessionToken,
CancellationToken)](M_Tessa_Platform_Runtime_ISessionTokenHolder_SetSessionTokenAsync.htm)  
##  __См. также
#### Ссылки
[SessionTokenHolder - ](T_Tessa_Platform_Runtime_SessionTokenHolder.htm)
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
