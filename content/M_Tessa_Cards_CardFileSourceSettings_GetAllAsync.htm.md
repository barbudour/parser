# CardFileSourceSettings.GetAllAsync - метод
Все доступные местоположения.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<ReadOnlyCollection<ICardFileSource>> GetAllAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetAllAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ReadOnlyCollection(Of ICardFileSource))
C++ __Копировать
     public:
    virtual ValueTask<ReadOnlyCollection<ICardFileSource^>^> GetAllAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetAllAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ReadOnlyCollection<ICardFileSource>> 
    override GetAllAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ReadOnlyCollection<ICardFileSource>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[ICardFileSource](T_Tessa_Cards_ICardFileSource.htm)>>  
Асинхронная задача.
#### Реализации
[ICardFileSourceSettings.GetAllAsync(CancellationToken)](M_Tessa_Cards_ICardFileSourceSettings_GetAllAsync.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[CardFileSourceSettings - ](T_Tessa_Cards_CardFileSourceSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
