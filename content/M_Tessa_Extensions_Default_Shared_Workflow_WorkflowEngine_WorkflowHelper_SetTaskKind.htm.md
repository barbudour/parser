# WorkflowHelper.SetTaskKind - метод
Устанавливает вид задания.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValidationResult SetTaskKind(
    	CardTask cardTask,
    	Guid? kindID,
    	string kindCaption,
    	Object objectName = null
    )
VB __Копировать
     Public Shared Function SetTaskKind ( 
    	cardTask As CardTask,
    	kindID As Guid?,
    	kindCaption As String,
    	Optional objectName As Object = Nothing
    ) As ValidationResult
C++ __Копировать
     public:
    static ValidationResult^ SetTaskKind(
    	CardTask^ cardTask, 
    	Nullable<Guid> kindID, 
    	String^ kindCaption, 
    	Object^ objectName = nullptr
    )
F# __Копировать
     static member SetTaskKind : 
            cardTask : CardTask * 
            kindID : Nullable<Guid> * 
            kindCaption : string * 
            ?objectName : Object 
    (* Defaults:
            let _objectName = defaultArg objectName null
    *)
    -> ValidationResult 
#### Параметры
cardTask [CardTask](T_Tessa_Cards_CardTask.htm)
    Задание в котором надо установить вид.
kindID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор вида задания.
kindCaption [String](https://learn.microsoft.com/dotnet/api/system.string)
    Отображаемое имя вида задания.
objectName [Object](https://learn.microsoft.com/dotnet/api/system.object)
(Optional)
    Текущий объект this для задания имени объекта вызвавшего ошибку. Можно также передать тип объекта, строку с именем объекта или null, если имя остаётся неизвестным.
#### Возвращаемое значение
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)  
Результат выполнения.
##  __Заметки
Для задания значения необходимо, что бы тип карточки задания содержал
комплексную колонку TaskCommonInfo.Kind.
##  __См. также
#### Ссылки
[WorkflowHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
