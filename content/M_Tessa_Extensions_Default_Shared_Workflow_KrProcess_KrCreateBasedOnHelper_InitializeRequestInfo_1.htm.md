# KrCreateBasedOnHelper.InitializeRequestInfo(Dictionary<String, Object>,
Card, Boolean) - метод
Инициализирует информацию по запросу на создание карточки
[CardNewRequest](T_Tessa_Cards_CardNewRequest.htm).Info на основании заданной
карточки baseCard.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void InitializeRequestInfo(
    	Dictionary<string, Object> requestInfo,
    	Card baseCard,
    	bool copyFiles = false
    )
VB __Копировать
     Public Shared Sub InitializeRequestInfo ( 
    	requestInfo As Dictionary(Of String, Object),
    	baseCard As Card,
    	Optional copyFiles As Boolean = false
    )
C++ __Копировать
     public:
    static void InitializeRequestInfo(
    	Dictionary<String^, Object^>^ requestInfo, 
    	Card^ baseCard, 
    	bool copyFiles = false
    )
F# __Копировать
     static member InitializeRequestInfo : 
            requestInfo : Dictionary<string, Object> * 
            baseCard : Card * 
            ?copyFiles : bool 
    (* Defaults:
            let _copyFiles = defaultArg copyFiles false
    *)
    -> unit 
#### Параметры
requestInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
     Информация по запросу на создание карточки [CardNewRequest](T_Tessa_Cards_CardNewRequest.htm).Info на основании заданной карточки baseCard. 
baseCard [Card](T_Tessa_Cards_Card.htm)
    Карточка, на основании которой создаётся другая карточка.
copyFiles [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что должны быть скопированы файлы из основной карточки.
##  __См. также
#### Ссылки
[KrCreateBasedOnHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCreateBasedOnHelper.htm)
[InitializeRequestInfo -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCreateBasedOnHelper_InitializeRequestInfo.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
