# CardFileSourceSettings.TryGetAsync - метод
Возвращает информацию по местоположению файлов для заданного типа
местоположения или null, если в системе не задано информации для заданного
типа.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<ICardFileSource> TryGetAsync(
    	CardFileSourceType type,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryGetAsync ( 
    	type As CardFileSourceType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ICardFileSource)
C++ __Копировать
     public:
    virtual ValueTask<ICardFileSource^> TryGetAsync(
    	CardFileSourceType type, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryGetAsync : 
            type : CardFileSourceType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ICardFileSource> 
    override TryGetAsync : 
            type : CardFileSourceType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ICardFileSource> 
#### Параметры
type [CardFileSourceType](T_Tessa_Cards_CardFileSourceType.htm)
    Тип местоположения, для которого возвращается информация по местоположению.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ICardFileSource](T_Tessa_Cards_ICardFileSource.htm)>  
Информация по местоположению файлов для заданного типа местоположения или
null, если в системе не задано информации для заданного типа.
#### Реализации
[ICardFileSourceSettings.TryGetAsync(CardFileSourceType,
CancellationToken)](M_Tessa_Cards_ICardFileSourceSettings_TryGetAsync.htm)  
##  __См. также
#### Ссылки
[CardFileSourceSettings - ](T_Tessa_Cards_CardFileSourceSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
