# CardTypeInfoResolver.TryGetNameAsync - метод
Возвращает имя типа карточки или null, если тип карточки не найден.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<string> TryGetNameAsync(
    	Guid typeID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryGetNameAsync ( 
    	typeID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of String)
C++ __Копировать
     public:
    virtual ValueTask<String^> TryGetNameAsync(
    	Guid typeID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryGetNameAsync : 
            typeID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<string> 
    override TryGetNameAsync : 
            typeID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<string> 
#### Параметры
typeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Имя типа карточки или null, если тип карточки не найден.
#### Реализации
[ITypeInfoResolver.TryGetNameAsync(Guid,
CancellationToken)](M_Tessa_Platform_Runtime_ITypeInfoResolver_TryGetNameAsync.htm)  
##  __См. также
#### Ссылки
[CardTypeInfoResolver - ](T_Tessa_Cards_CardTypeInfoResolver.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
