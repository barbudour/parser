# BusinessProcessCardHelper.FillVirtualSectionAsync - метод
Метод для заполнения виртуальной секции версий процесса из базы
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task FillVirtualSectionAsync(
    	IDbScope dbScope,
    	Card card,
    	CardSection virtualSection,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function FillVirtualSectionAsync ( 
    	dbScope As IDbScope,
    	card As Card,
    	virtualSection As CardSection,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    static Task^ FillVirtualSectionAsync(
    	IDbScope^ dbScope, 
    	Card^ card, 
    	CardSection^ virtualSection, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member FillVirtualSectionAsync : 
            dbScope : IDbScope * 
            card : Card * 
            virtualSection : CardSection * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект для доступа к базу
card [Card](T_Tessa_Cards_Card.htm)
    Карточка шаблона процесса
virtualSection [CardSection](T_Tessa_Cards_CardSection.htm)
    Виртуальная секция с версиями процесса
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[BusinessProcessCardHelper -
](T_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
