# WorkflowSignal - класс
Сигнал в Workflow API. Обеспечивает взаимодействие с подпроцессом в
произвольный момент времени.
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class WorkflowSignal : IWorkflowSignal, 
    	ISealable
VB __Копировать
     Public Class WorkflowSignal
    	Implements IWorkflowSignal, ISealable
C++ __Копировать
     public ref class WorkflowSignal : IWorkflowSignal, 
    	ISealable
F# __Копировать
     type WorkflowSignal = 
        class
            interface IWorkflowSignal
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowSignal
Implements
    [IWorkflowSignal](T_Tessa_Cards_Workflow_IWorkflowSignal.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Заметки
Наследники класса могут добавлять свойства и методы.
## __Конструкторы
[WorkflowSignal](M_Tessa_Cards_Workflow_WorkflowSignal__ctor.htm)|  Создаёт
экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[ID](P_Tessa_Cards_Workflow_WorkflowSignal_ID.htm)| Идентификатор сигнала.  
---|---  
[Info](P_Tessa_Cards_Workflow_WorkflowSignal_Info.htm)| Дополнительная
информация для расширений, связанная с сигналом.  
[IsSealed](P_Tessa_Cards_Workflow_WorkflowSignal_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
[Name](P_Tessa_Cards_Workflow_WorkflowSignal_Name.htm)|  Имя (алиас) сигнала,
с которым может быть связана произвольная логика обработки, т.е. сигналы
одного типа с разными именами могут обрабатываться по-разному.  
[Number](P_Tessa_Cards_Workflow_WorkflowSignal_Number.htm)|  Номер сигнала, по
которому может определяться способ его прохождения. Можно задать совместно или
вместо имени сигнала [Tessa.Cards.Workflow.IWorkflowSignal.Name].  
[Parameters](P_Tessa_Cards_Workflow_WorkflowSignal_Parameters.htm)| Параметры
поступившего сигнала в произвольном формате.  
[ProcessID](P_Tessa_Cards_Workflow_WorkflowSignal_ProcessID.htm)|
Идентификатор подпроцесса, к которому относится сигнал, или null, если
подпроцесс определяется не по идентификатору, а по имени типа
[Tessa.Cards.Workflow.IWorkflowSignal.ProcessTypeName].  
[ProcessTypeName](P_Tessa_Cards_Workflow_WorkflowSignal_ProcessTypeName.htm)|
Имя типа подпроцесса, на экземпляр которого отправляется сигнал. Имя должно
быть указано для любых экземпляров сигналов: как для подпроцессов с указанным
идентификатором, так и для подпроцессов, существующих в единственном
экземпляре для карточки. Если в текущий момент активно несколько подпроцессов
данного типа и не был указан идентификатор подпроцесса, то только один
экземпляр (случайный) получит сигнал для обработки.  
[Type](P_Tessa_Cards_Workflow_WorkflowSignal_Type.htm)| Тип сигнала, влияет на
способ его обработки.  
##  __Методы
[CheckSealed](M_Tessa_Cards_Workflow_WorkflowSignal_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
---|---  
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
[Seal](M_Tessa_Cards_Workflow_WorkflowSignal_Seal.htm)| Защищает объект от
изменений.  
[SealInternal](M_Tessa_Cards_Workflow_WorkflowSignal_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.  
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
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
