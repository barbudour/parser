# CardTypedRequestExtension<TRequest, TResponse>.CreateRequestAsync - метод
Создаёт строготипизированный объект запроса для заданного хранилища или null,
если создание невозможно.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask<TRequest> CreateRequestAsync(
    	Dictionary<string, Object> storage,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function CreateRequestAsync ( 
    	storage As Dictionary(Of String, Object),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of TRequest)
C++ __Копировать
     protected:
    virtual ValueTask<TRequest> CreateRequestAsync(
    	Dictionary<String^, Object^>^ storage, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract CreateRequestAsync : 
            storage : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<'TRequest> 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
     Хранилище, для которого требуется создать строготипизированный объект. Не равно null. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[TRequest](T_Tessa_Cards_Extensions_CardTypedRequestExtension_2.htm)>  
Строготипизированный объект запроса для заданного хранилища или null, если
создание невозможно.
## __См. также
#### Ссылки
[CardTypedRequestExtension<TRequest, TResponse> \-
](T_Tessa_Cards_Extensions_CardTypedRequestExtension_2.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
