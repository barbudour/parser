# CardStoreExtensionContext.InvokeContentStoreCompletedAsync - метод
Вызывает обработку события [ICardStoreExtensionContext.ContentStoreCompleted],
которое обычно наступает при завершении сохранения содержимого файлов.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task InvokeContentStoreCompletedAsync(
    	CardContentStoreCompletedEventArgs e,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function InvokeContentStoreCompletedAsync ( 
    	e As CardContentStoreCompletedEventArgs,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ InvokeContentStoreCompletedAsync(
    	CardContentStoreCompletedEventArgs^ e, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract InvokeContentStoreCompletedAsync : 
            e : CardContentStoreCompletedEventArgs * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override InvokeContentStoreCompletedAsync : 
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
#### Реализации
[ICardStoreExtensionContext.InvokeContentStoreCompletedAsync(CardContentStoreCompletedEventArgs,
CancellationToken)](M_Tessa_Cards_Extensions_ICardStoreExtensionContext_InvokeContentStoreCompletedAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreExtensionContext -
](T_Tessa_Cards_Extensions_CardStoreExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
