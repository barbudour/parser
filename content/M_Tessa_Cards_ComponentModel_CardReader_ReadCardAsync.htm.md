# CardReader.ReadCardAsync - метод
Выполняет чтение пакета карточки из потока карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<Card> ReadCardAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ReadCardAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Card)
C++ __Копировать
     public:
    Task<Card^>^ ReadCardAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member ReadCardAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<Card> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Card](T_Tessa_Cards_Card.htm)>  
Пакет карточки, прочитанный из потока карточки.
##  __Исключения
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)|
В потоке указан неверный размер сериализуемого объекта.  
---|---  
##  __См. также
#### Ссылки
[CardReader - ](T_Tessa_Cards_ComponentModel_CardReader.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
