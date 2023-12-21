# ICardContentStrategy.CopyAsync - метод
Выполняет копирование контента из исходного местоположения в целевое. Если
исходное и целевое местоположения совпадут, то метод завершится с ошибкой и
вернёт false.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<bool> CopyAsync(
    	CardContentContext sourceContext,
    	CardContentContext targetContext,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function CopyAsync ( 
    	sourceContext As CardContentContext,
    	targetContext As CardContentContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
    Task<bool>^ CopyAsync(
    	CardContentContext^ sourceContext, 
    	CardContentContext^ targetContext, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CopyAsync : 
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
    Исходное местоположение копируемого контента.
targetContext
[CardContentContext](T_Tessa_Cards_ComponentModel_CardContentContext.htm)
    Целевое местоположение копируемого контента. При наличии контента возникает ошибка валидации.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если контент успешно скопирован; false, если контент уже существует в
целевом местоположении.
## __См. также
#### Ссылки
[ICardContentStrategy -
](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
