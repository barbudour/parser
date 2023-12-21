# ICardCachedMetadata.SetAsync - метод
Устанавливает заданную метаинформацию в кэше. При этом метаинформация
защищается от изменений, если кэш также защищён от изменений.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task SetAsync(
    	ICardMetadata metadata,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function SetAsync ( 
    	metadata As ICardMetadata,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ SetAsync(
    	ICardMetadata^ metadata, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract SetAsync : 
            metadata : ICardMetadata * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
metadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
     Устанавливаемая метаинформация. Не может быть равна null. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardCachedMetadata - ](T_Tessa_Cards_ICardCachedMetadata.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
