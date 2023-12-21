# BusinessProcessCardHelper.GetNextVersionAsync - метод
Метод для получения следующего номера версии процесса
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<int> GetNextVersionAsync(
    	IDbScope dbScope,
    	Card card,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetNextVersionAsync ( 
    	dbScope As IDbScope,
    	card As Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Integer)
C++ __Копировать
     public:
    static Task<int>^ GetNextVersionAsync(
    	IDbScope^ dbScope, 
    	Card^ card, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetNextVersionAsync : 
            dbScope : IDbScope * 
            card : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<int> 
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект для доступа к базу
card [Card](T_Tessa_Cards_Card.htm)
    Карточка шаблона процесса
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>  
Возвращает следующий номер версии
##  __См. также
#### Ссылки
[BusinessProcessCardHelper -
](T_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
