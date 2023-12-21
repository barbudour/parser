# ICardStoreExtensionContext.InvokeContentStoreCompletedAsync - метод
Вызывает обработку события [ICardStoreExtensionContext.ContentStoreCompleted],
которое обычно наступает при завершении сохранения содержимого файлов.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task InvokeContentStoreCompletedAsync(
    	CardContentStoreCompletedEventArgs e,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function InvokeContentStoreCompletedAsync ( 
    	e As CardContentStoreCompletedEventArgs,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ InvokeContentStoreCompletedAsync(
    	CardContentStoreCompletedEventArgs^ e, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract InvokeContentStoreCompletedAsync : 
            e : CardContentStoreCompletedEventArgs * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
e
[CardContentStoreCompletedEventArgs](T_Tessa_Cards_CardContentStoreCompletedEventArgs.htm)
     Аргументы события. Не должны быть равны null. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardStoreExtensionContext -
](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
