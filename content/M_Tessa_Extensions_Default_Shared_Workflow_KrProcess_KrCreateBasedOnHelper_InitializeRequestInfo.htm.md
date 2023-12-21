# KrCreateBasedOnHelper.InitializeRequestInfo(Dictionary<String, Object>,
Guid, Boolean, KrToken) - метод
Инициализирует информацию по запросу на создание карточки
[CardNewRequest](T_Tessa_Cards_CardNewRequest.htm).Info на основании заданной
карточки с идентификатором baseCardID.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void InitializeRequestInfo(
    	Dictionary<string, Object> requestInfo,
    	Guid baseCardID,
    	bool copyFiles = false,
    	KrToken baseCardToken = null
    )
VB __Копировать
     Public Shared Sub InitializeRequestInfo ( 
    	requestInfo As Dictionary(Of String, Object),
    	baseCardID As Guid,
    	Optional copyFiles As Boolean = false,
    	Optional baseCardToken As KrToken = Nothing
    )
C++ __Копировать
     public:
    static void InitializeRequestInfo(
    	Dictionary<String^, Object^>^ requestInfo, 
    	Guid baseCardID, 
    	bool copyFiles = false, 
    	KrToken^ baseCardToken = nullptr
    )
F# __Копировать
     static member InitializeRequestInfo : 
            requestInfo : Dictionary<string, Object> * 
            baseCardID : Guid * 
            ?copyFiles : bool * 
            ?baseCardToken : KrToken 
    (* Defaults:
            let _copyFiles = defaultArg copyFiles false
            let _baseCardToken = defaultArg baseCardToken null
    *)
    -> unit 
#### Параметры
requestInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
     Информация по запросу на создание карточки [CardNewRequest](T_Tessa_Cards_CardNewRequest.htm).Info на основании заданной карточки с идентификатором baseCardID. 
baseCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, на основании которой создаётся другая карточка.
copyFiles [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что должны быть скопированы файлы из основной карточки.
baseCardToken
[KrToken](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken.htm)
(Optional)
     Токен с правами на чтение базовой карточки baseCardID или null, если права будут вычислены на сервере. 
## __См. также
#### Ссылки
[KrCreateBasedOnHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCreateBasedOnHelper.htm)
[InitializeRequestInfo -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCreateBasedOnHelper_InitializeRequestInfo.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
