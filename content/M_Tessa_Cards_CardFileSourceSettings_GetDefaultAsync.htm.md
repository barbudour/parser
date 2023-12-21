# CardFileSourceSettings.GetDefaultAsync - метод
Местоположение по умолчанию. Может быть равно null только в том случае, если в
системе не зарегистрировано ни одного местоположения.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<ICardFileSource> GetDefaultAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetDefaultAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ICardFileSource)
C++ __Копировать
     public:
    virtual ValueTask<ICardFileSource^> GetDefaultAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetDefaultAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ICardFileSource> 
    override GetDefaultAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ICardFileSource> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ICardFileSource](T_Tessa_Cards_ICardFileSource.htm)>  
Асинхронная задача.
#### Реализации
[ICardFileSourceSettings.GetDefaultAsync(CancellationToken)](M_Tessa_Cards_ICardFileSourceSettings_GetDefaultAsync.htm)  
##  __См. также
#### Ссылки
[CardFileSourceSettings - ](T_Tessa_Cards_CardFileSourceSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
