# CardFileSourceSettings.GetAsync - метод
Возвращает информацию по местоположению файлов для заданного типа
местоположения. Возвращённый объект гарантированно не равен null. Если
информации по местоположению не найдено, то выбрасывается исключение
[System.Collections.Generic.KeyNotFoundException].
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<ICardFileSource> GetAsync(
    	CardFileSourceType type,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetAsync ( 
    	type As CardFileSourceType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ICardFileSource)
C++ __Копировать
     public:
    virtual ValueTask<ICardFileSource^> GetAsync(
    	CardFileSourceType type, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetAsync : 
            type : CardFileSourceType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ICardFileSource> 
    override GetAsync : 
            type : CardFileSourceType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ICardFileSource> 
#### Параметры
type [CardFileSourceType](T_Tessa_Cards_CardFileSourceType.htm)
    Тип местоположения контента файла.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ICardFileSource](T_Tessa_Cards_ICardFileSource.htm)>  
Настройки по местоположению файлов для заданного типа местоположения.
#### Реализации
[ICardFileSourceSettings.GetAsync(CardFileSourceType,
CancellationToken)](M_Tessa_Cards_ICardFileSourceSettings_GetAsync.htm)  
##  __См. также
#### Ссылки
[CardFileSourceSettings - ](T_Tessa_Cards_CardFileSourceSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
