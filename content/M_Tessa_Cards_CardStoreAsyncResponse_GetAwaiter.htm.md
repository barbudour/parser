# CardStoreAsyncResponse.GetAwaiter - метод
Возвращает объект, выполняющий ожидание результата задачи
[ICardStoreAsyncResponse.Task].
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public TaskAwaiter<CardStoreResponse> GetAwaiter()
VB __Копировать
     Public Function GetAwaiter As TaskAwaiter(Of CardStoreResponse)
C++ __Копировать
     public:
    virtual TaskAwaiter<CardStoreResponse^> GetAwaiter() sealed
F# __Копировать
     abstract GetAwaiter : unit -> TaskAwaiter<CardStoreResponse> 
    override GetAwaiter : unit -> TaskAwaiter<CardStoreResponse> 
#### Возвращаемое значение
[TaskAwaiter](https://learn.microsoft.com/dotnet/api/system.runtime.compilerservices.taskawaiter-1)<[CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm)>  
Результат ожидания.
#### Реализации
[ICardStoreAsyncResponse.GetAwaiter()](M_Tessa_Cards_ICardStoreAsyncResponse_GetAwaiter.htm)  
##  __См. также
#### Ссылки
[CardStoreAsyncResponse - ](T_Tessa_Cards_CardStoreAsyncResponse.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
