# CardReader.ReadHeaderAsync - метод
Выполняет чтение заголовка из потока карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardHeader> ReadHeaderAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ReadHeaderAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardHeader)
C++ __Копировать
     public:
    Task<CardHeader^>^ ReadHeaderAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member ReadHeaderAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardHeader> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardHeader](T_Tessa_Cards_ComponentModel_CardHeader.htm)>  
Заголовок, прочитанный из потока карточки.
##  __Исключения
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)|
В потоке указан неверный размер заголовка.  
---|---  
##  __См. также
#### Ссылки
[CardReader - ](T_Tessa_Cards_ComponentModel_CardReader.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
