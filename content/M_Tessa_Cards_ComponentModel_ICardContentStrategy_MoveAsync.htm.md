# ICardContentStrategy.MoveAsync - метод
Перемещает контент файла (но не записи по файлу) из исходного местоположения
sourceContext в целевое местоположение targetContext. При этом файл может
перемещаться между карточками и между разными файловыми хранилищами (если
текущая стратегия поддерживает разные хранилища). Если исходное и целевое
местоположения совпадают, то метод не выполняет действий и возвращает true.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<bool> MoveAsync(
    	CardContentContext sourceContext,
    	CardContentContext targetContext,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function MoveAsync ( 
    	sourceContext As CardContentContext,
    	targetContext As CardContentContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
    Task<bool>^ MoveAsync(
    	CardContentContext^ sourceContext, 
    	CardContentContext^ targetContext, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract MoveAsync : 
            sourceContext : CardContentContext * 
            targetContext : CardContentContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
sourceContext
[CardContentContext](T_Tessa_Cards_ComponentModel_CardContentContext.htm)
    Исходное местоположение перемещаемого контента.
targetContext
[CardContentContext](T_Tessa_Cards_ComponentModel_CardContentContext.htm)
    Целевое местоположение перемещаемого контента. При наличии контента возникает ошибка валидации.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если контент успешно перемещён; false в противном случае.
## __См. также
#### Ссылки
[ICardContentStrategy -
](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
