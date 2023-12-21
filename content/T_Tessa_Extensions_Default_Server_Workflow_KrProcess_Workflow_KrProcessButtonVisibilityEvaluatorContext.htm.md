# KrProcessButtonVisibilityEvaluatorContext - класс
Контекст используемый при определении видимости тайла вторичного процесса
работающего в режиме "Кнопка".
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrProcessButtonVisibilityEvaluatorContext : IKrProcessButtonVisibilityEvaluatorContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class KrProcessButtonVisibilityEvaluatorContext
    	Implements IKrProcessButtonVisibilityEvaluatorContext, IExtensionContext
C++ __Копировать
     public ref class KrProcessButtonVisibilityEvaluatorContext sealed : IKrProcessButtonVisibilityEvaluatorContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type KrProcessButtonVisibilityEvaluatorContext = 
        class
            interface IKrProcessButtonVisibilityEvaluatorContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrProcessButtonVisibilityEvaluatorContext
Implements
    [IKrProcessButtonVisibilityEvaluatorContext](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessButtonVisibilityEvaluatorContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Конструкторы
[KrProcessButtonVisibilityEvaluatorContext(IValidationResultBuilder,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessButtonVisibilityEvaluatorContext__ctor.htm)|
Инициализирует новый экземпляр класса
KrProcessButtonVisibilityEvaluatorContext. Конструктор используется для
инициализации контекста глобальных тайлов.  
---|---  
[KrProcessButtonVisibilityEvaluatorContext(IValidationResultBuilder,
IMainCardAccessStrategy, Nullable<Guid>, CardType, Nullable<Guid>,
Nullable<KrComponents>, Nullable<KrState>, ICardExtensionContext,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessButtonVisibilityEvaluatorContext__ctor_1.htm)|
Инициализирует новый экземпляр класса
KrProcessButtonVisibilityEvaluatorContext.  
## __Свойства
[CancellationToken](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessButtonVisibilityEvaluatorContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[CardContext](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessButtonVisibilityEvaluatorContext_CardContext.htm)|
Конекст расширения карточки.  
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessButtonVisibilityEvaluatorContext_CardID.htm)|
Идентификатор карточки.  
[CardType](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessButtonVisibilityEvaluatorContext_CardType.htm)|
Тип карточки.  
[DocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessButtonVisibilityEvaluatorContext_DocTypeID.htm)|
Идентификатор типа документа.  
[KrComponents](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessButtonVisibilityEvaluatorContext_KrComponents.htm)|
Включенные компоненты типового решения для текущей карточки.  
[MainCardAccessStrategy](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessButtonVisibilityEvaluatorContext_MainCardAccessStrategy.htm)|
Стратегия загрузки основной карточки.  
[State](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessButtonVisibilityEvaluatorContext_State.htm)|
Состояние карточки.  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessButtonVisibilityEvaluatorContext_ValidationResult.htm)|
Результат валидации.  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)
