# CardSourceContentStrategy.GetContentStrategyAsync - метод
Возвращает стратегию для взаимодействия с указанным местоположением контента
файлов.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<ICardContentStrategy> GetContentStrategyAsync(
    	CardFileSourceType sourceType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetContentStrategyAsync ( 
    	sourceType As CardFileSourceType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ICardContentStrategy)
C++ __Копировать
     public:
    ValueTask<ICardContentStrategy^> GetContentStrategyAsync(
    	CardFileSourceType sourceType, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member GetContentStrategyAsync : 
            sourceType : CardFileSourceType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ICardContentStrategy> 
#### Параметры
sourceType [CardFileSourceType](T_Tessa_Cards_CardFileSourceType.htm)
    Местоположение контента файлов.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ICardContentStrategy](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)>  
Стратегия для взаимодействия с указанным местоположением контента файлов.
##  __См. также
#### Ссылки
[CardSourceContentStrategy -
](T_Tessa_Cards_ComponentModel_CardSourceContentStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
