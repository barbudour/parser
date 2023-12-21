# CardType.DepthFirstVisitAsync - метод
Выполняет посещение всех объектов текущего типа карточки в порядке, начиная с
наименее вложенных объектов.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask DepthFirstVisitAsync(
    	ICardTypeVisitor visitor,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DepthFirstVisitAsync ( 
    	visitor As ICardTypeVisitor,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    ValueTask DepthFirstVisitAsync(
    	ICardTypeVisitor^ visitor, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member DepthFirstVisitAsync : 
            visitor : ICardTypeVisitor * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
visitor [ICardTypeVisitor](T_Tessa_Cards_ICardTypeVisitor.htm)
    Объект, выполняющий посещение объектов типа карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardType - ](T_Tessa_Cards_CardType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
