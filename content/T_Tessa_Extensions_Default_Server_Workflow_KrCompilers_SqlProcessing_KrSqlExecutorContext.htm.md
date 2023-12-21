# KrSqlExecutorContext - класс
Контекст
[IKrSqlExecutor](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutor.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.SqlProcessing](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrSqlExecutorContext : IKrSqlExecutorContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class KrSqlExecutorContext
    	Implements IKrSqlExecutorContext, IExtensionContext
C++ __Копировать
     public ref class KrSqlExecutorContext sealed : IKrSqlExecutorContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type KrSqlExecutorContext = 
        class
            interface IKrSqlExecutorContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrSqlExecutorContext
Implements
    [IKrSqlExecutorContext](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_IKrSqlExecutorContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Конструкторы
[KrSqlExecutorContext(Stage, IValidationResultBuilder,
Func<IKrSqlExecutorContext, String, Object[], String>, IKrSecondaryProcess,
Nullable<Guid>, Nullable<Guid>, Nullable<Guid>, KrState, Nullable<Guid>,
String,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext__ctor_3.htm)|
Инициализирует новый экземпляр класса для пересчета SQL-исполнителей в этапе.  
---|---  
[KrSqlExecutorContext(String, IValidationResultBuilder,
Func<IKrSqlExecutorContext, String, Object[], String>, IKrSecondaryProcess,
Nullable<Guid>, Nullable<Guid>, Nullable<Guid>, Nullable<KrState>,
Nullable<Guid>, String,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext__ctor_2.htm)|
Инициализирует новый экземпляр класса.  
[KrSqlExecutorContext(String, IValidationResultBuilder,
Func<IKrSqlExecutorContext, String, Object[], String>, IKrExecutionUnit,
IKrSecondaryProcess, Nullable<Guid>, Nullable<Guid>, Nullable<Guid>, KrState,
Nullable<Guid>, String,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext__ctor.htm)|
Инициализирует новый экземпляр класса для вычисления условий этапов, шаблонов,
групп.  
[KrSqlExecutorContext(String, IValidationResultBuilder,
Func<IKrSqlExecutorContext, String, Object[], String>, IKrSecondaryProcess,
Guid, Guid, Guid, Guid, Nullable<Guid>, String, Nullable<Guid>,
Nullable<Guid>, Nullable<Guid>, Nullable<KrState>, String, String, String,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext__ctor_1.htm)|
Инициализирует новый экземпляр класса.  
## __Свойства
[CancellationToken](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_CardID.htm)|
Идентификатор карточки.  
[CardTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_CardTypeID.htm)|
Идентификатор типа карточки.  
[DocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_DocTypeID.htm)|
Идентификатор типа документа.  
[GetErrorTextFunc](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_GetErrorTextFunc.htm)|
Функция, формирующая сообщение об ошибке.  
[GroupName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_GroupName.htm)|
Название группы этапов.  
[Query](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_Query.htm)|
Выполняемый запрос.  
[SecondaryProcess](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_SecondaryProcess.htm)|
Текущий вторичный процесс кнопки.  
[StageGroupID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_StageGroupID.htm)|
Идентификатор группы этапов.  
[StageName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_StageName.htm)|
Название этапа.  
[StageRowID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_StageRowID.htm)|
Идентификатор строки этапа.  
[StageTemplateID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_StageTemplateID.htm)|
Идентификатор шаблона этапов.  
[StageTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_StageTypeID.htm)|
Идентификатор типа этапа.  
[State](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_State.htm)|
Состояние карточки.  
[TemplateName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_TemplateName.htm)|
Название шаблона этапов.  
[TypeID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_TypeID.htm)|
Эффективный идентификатор типа. Если тип использует типы документов, то это
тип документа. Иначе это тип карточки.  
[UserID](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_UserID.htm)|
Идентификатор пользователя  
[UserName](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_UserName.htm)|
Имя пользователя.  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing_KrSqlExecutorContext_ValidationResult.htm)|  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.SqlProcessing -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_SqlProcessing.htm)
