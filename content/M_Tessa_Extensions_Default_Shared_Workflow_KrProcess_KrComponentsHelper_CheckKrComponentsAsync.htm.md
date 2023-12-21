# KrComponentsHelper.CheckKrComponentsAsync(Guid, Guid, Nullable<Guid>,
IDbScope, IKrTypesCache, KrComponents, CancellationToken) - метод
Проверяет наличие необходимых настроек у карточки типового решения.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<(bool IsSuccessful, string ErrorMessage)> CheckKrComponentsAsync(
    	Guid cardID,
    	Guid cardTypeID,
    	Guid? docTypeID,
    	IDbScope dbScope,
    	IKrTypesCache typesCache,
    	KrComponents required,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CheckKrComponentsAsync ( 
    	cardID As Guid,
    	cardTypeID As Guid,
    	docTypeID As Guid?,
    	dbScope As IDbScope,
    	typesCache As IKrTypesCache,
    	required As KrComponents,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of (IsSuccessful As Boolean, ErrorMessage As String))
C++ __Копировать
     public:
    static ValueTask<ValueTuple<bool, String^>> CheckKrComponentsAsync(
    	Guid cardID, 
    	Guid cardTypeID, 
    	Nullable<Guid> docTypeID, 
    	IDbScope^ dbScope, 
    	IKrTypesCache^ typesCache, 
    	KrComponents required, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CheckKrComponentsAsync : 
            cardID : Guid * 
            cardTypeID : Guid * 
            docTypeID : Nullable<Guid> * 
            dbScope : IDbScope * 
            typesCache : IKrTypesCache * 
            required : KrComponents * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValueTuple<bool, string>> 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, по которой будет определён идентификатор типа документа, если он не задан.
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки.
docTypeID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор типа документа или значение null, если он должен быть определён автоматически.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
Объект для взаимодействия с базой данных. Определяет область видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).
typesCache
[IKrTypesCache](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrTypesCache.htm)
Кэш по типам карточек и документов, содержащих информацию по типовому решению.
required
[KrComponents](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponents.htm)
    Проверяемые компоненты.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[String](https://learn.microsoft.com/dotnet/api/system.string)>>  
Кортеж содержащий: значение true, если все проверяемые компоненты активны,
иначе - false; строка содержащая информацию об ошибке, возникшей при
выполнении проверки.
##  __См. также
#### Ссылки
[KrComponentsHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper.htm)
[CheckKrComponentsAsync -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper_CheckKrComponentsAsync.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
