# StageTypeFormatterContext - конструктор
Инициализирует новый экземпляр класса
[StageTypeFormatterContext](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_StageTypeFormatterContext.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public StageTypeFormatterContext(
    	ISession session,
    	Dictionary<string, Object> info,
    	Card card,
    	CardRow stageRow,
    	IDictionary<string, Object> settings,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	session As ISession,
    	info As Dictionary(Of String, Object),
    	card As Card,
    	stageRow As CardRow,
    	settings As IDictionary(Of String, Object),
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    StageTypeFormatterContext(
    	ISession^ session, 
    	Dictionary<String^, Object^>^ info, 
    	Card^ card, 
    	CardRow^ stageRow, 
    	IDictionary<String^, Object^>^ settings, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            session : ISession * 
            info : Dictionary<string, Object> * 
            card : Card * 
            stageRow : CardRow * 
            settings : IDictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> StageTypeFormatterContext
#### Параметры
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя.
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Дополнительная информация.
card [Card](T_Tessa_Cards_Card.htm)
    Карточка содержащая этап.
stageRow [CardRow](T_Tessa_Cards_CardRow.htm)
    Строка содержащая этап.
settings
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Словарь содержащий настройки этапа.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
##  __См. также
#### Ссылки
[StageTypeFormatterContext -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_StageTypeFormatterContext.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)
