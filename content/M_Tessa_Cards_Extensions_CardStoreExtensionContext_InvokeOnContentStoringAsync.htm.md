# CardStoreExtensionContext.InvokeOnContentStoringAsync - метод
Вызывает обработку события [ICardStoreExtensionContext.OnContentStoring],
которое обычно наступает перед сохранением содержимого файла.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task InvokeOnContentStoringAsync(
    	CardOnContentStoringEventArgs e,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function InvokeOnContentStoringAsync ( 
    	e As CardOnContentStoringEventArgs,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ InvokeOnContentStoringAsync(
    	CardOnContentStoringEventArgs^ e, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract InvokeOnContentStoringAsync : 
            e : CardOnContentStoringEventArgs * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override InvokeOnContentStoringAsync : 
            e : CardOnContentStoringEventArgs * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
e
[CardOnContentStoringEventArgs](T_Tessa_Cards_CardOnContentStoringEventArgs.htm)
     Аргументы события. Не должны быть равны null. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardStoreExtensionContext.InvokeOnContentStoringAsync(CardOnContentStoringEventArgs,
CancellationToken)](M_Tessa_Cards_Extensions_ICardStoreExtensionContext_InvokeOnContentStoringAsync.htm)  
##  __См. также
#### Ссылки
[CardStoreExtensionContext -
](T_Tessa_Cards_Extensions_CardStoreExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
