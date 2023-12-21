# KrChangeStateActionUIHandler - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Client_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrChangeStateActionUIHandler : WorkflowActionUIHandlerBase
VB __Копировать
     Public NotInheritable Class KrChangeStateActionUIHandler
    	Inherits WorkflowActionUIHandlerBase
C++ __Копировать
     public ref class KrChangeStateActionUIHandler sealed : public WorkflowActionUIHandlerBase
F# __Копировать
     [<SealedAttribute>]
    type KrChangeStateActionUIHandler = 
        class
            inherit WorkflowActionUIHandlerBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm) __ KrChangeStateActionUIHandler
##  __Конструкторы
[KrChangeStateActionUIHandler](M_Tessa_Extensions_Default_Client_Workflow_WorkflowEngine_KrChangeStateActionUIHandler__ctor.htm)|
Инициализирует новый экземпляр класса KrChangeStateActionUIHandler  
---|---  
##  __Свойства
[Group](P_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_Group.htm)|
Возвращает имя группы.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
---|---  
[Icon](P_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_Icon.htm)|
Возвращает имя иконки данного действия на левой панели.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
[ID](P_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_ID.htm)|
Идентификатор объекта, по которому выполняется регистрация в реестре.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
[IsStandAlone](P_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_IsStandAlone.htm)|
Возвращает флаг, обозначающий, что данное действие может быть только
единственным действием в узле.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
[Order](P_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_Order.htm)|
Возвращает порядок вывода.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
##  __Методы
[AddLinkBinding(WorkflowEngineBindingContext,
String[])](M_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_AddLinkBinding.htm)|
Создаёт новую привязку для связи.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
---|---  
[AddLinkBinding(WorkflowEngineBindingContext, String[],
String[])](M_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_AddLinkBinding_1.htm)|
Создаёт новую привязку для связи.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
[AttachEntrySectionAsync](M_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_AttachEntrySectionAsync.htm)|
Создаёт привязку строковой секции карточки к хешу.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
[AttachFieldAsync](M_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_AttachFieldAsync.htm)|
Создаёт привязку поля строковой секции к хешу.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
[AttachFieldToTemplateAsync](M_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_AttachFieldToTemplateAsync.htm)|
Создаёт привязку поля строковой секции к шаблону действия.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
[AttachRowAsync](M_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_AttachRowAsync.htm)|
Создаёт привязку строки табличной секции к хешу.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
[AttachTableSectionAsync](M_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_AttachTableSectionAsync.htm)|
Создаёт привязку табличной секции карточки к хешу.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
[AttachTableSectionToTemplateAsync](M_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_AttachTableSectionToTemplateAsync.htm)|
Производит привязку табличной секции по указанному пути к шаблону действия.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
[AttachToCardAsync](M_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_AttachToCardAsync.htm)|
Привязывает параметры действия к объекту карточки редактора действия.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
[AttachToCardCoreAsync](M_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_AttachToCardCoreAsync.htm)|
Создаёт привязку данных действия к объекту карточки (с учетом привязки к хешу
узла или процесса).  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
[CreateNode](M_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_CreateNode.htm)|
Создаёт узел.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetDescriptor](M_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_GetDescriptor.htm)|
Возвращает дескриптор текущего действия.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
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
[InvalidateFormAsync](M_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_InvalidateFormAsync.htm)|
Выполняет действия связанные с обработкой завершения жизненного цикла
редактора действия.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
[InvalidateFormCore](M_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_InvalidateFormCore.htm)|
Выполняет действия связанные с очисткой ресурсов при завершении жизни
редактора действия.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateFormAsync](M_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_UpdateFormAsync.htm)|
Обновляет форму редактора действия при его открытии.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
[UpdateFormCoreAsync](M_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase_UpdateFormCoreAsync.htm)|
Обновляет форму редактора действия при ее первом открытии.  
(Унаследован от
[WorkflowActionUIHandlerBase](T_Tessa_UI_WorkflowViewer_Actions_WorkflowActionUIHandlerBase.htm))  
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
[Tessa.Extensions.Default.Client.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Client_Workflow_WorkflowEngine.htm)
