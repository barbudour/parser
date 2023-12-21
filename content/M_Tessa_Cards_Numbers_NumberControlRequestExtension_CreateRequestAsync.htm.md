# NumberControlRequestExtension.CreateRequestAsync - метод
Создаёт строготипизированный объект запроса для заданного хранилища или null,
если создание невозможно.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask<NumberControlRequest> CreateRequestAsync(
    	Dictionary<string, Object> storage,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function CreateRequestAsync ( 
    	storage As Dictionary(Of String, Object),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of NumberControlRequest)
C++ __Копировать
     protected:
    virtual ValueTask<NumberControlRequest^> CreateRequestAsync(
    	Dictionary<String^, Object^>^ storage, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract CreateRequestAsync : 
            storage : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<NumberControlRequest> 
    override CreateRequestAsync : 
            storage : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<NumberControlRequest> 
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
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[NumberControlRequest](T_Tessa_Cards_Numbers_NumberControlRequest.htm)>  
Строготипизированный объект запроса для заданного хранилища или null, если
создание невозможно.
## __См. также
#### Ссылки
[NumberControlRequestExtension -
](T_Tessa_Cards_Numbers_NumberControlRequestExtension.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
