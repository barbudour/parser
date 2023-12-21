# CardReader.ReadCardStoreRequestAsync - метод
Выполняет чтение запроса на сохранение карточки из потока карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardStoreRequest> ReadCardStoreRequestAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ReadCardStoreRequestAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardStoreRequest)
C++ __Копировать
     public:
    Task<CardStoreRequest^>^ ReadCardStoreRequestAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member ReadCardStoreRequestAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardStoreRequest> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)>  
Запрос на сохранение карточки, прочитанный из потока карточки.
##  __Исключения
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)|
В потоке указан неверный размер сериализуемого объекта.  
---|---  
##  __См. также
#### Ссылки
[CardReader - ](T_Tessa_Cards_ComponentModel_CardReader.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
