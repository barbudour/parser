# IWorkflowSignal - интерфейс
Сигнал в Workflow API. Обеспечивает взаимодействие с подпроцессом в
произвольный момент времени.
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWorkflowSignal : ISealable
VB __Копировать
     Public Interface IWorkflowSignal
    	Inherits ISealable
C++ __Копировать
     public interface class IWorkflowSignal : ISealable
F# __Копировать
     type IWorkflowSignal = 
        interface
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[ID](P_Tessa_Cards_Workflow_IWorkflowSignal_ID.htm)| Идентификатор сигнала.  
---|---  
[Info](P_Tessa_Cards_Workflow_IWorkflowSignal_Info.htm)| Дополнительная
информация для расширений, связанная с сигналом.  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Name](P_Tessa_Cards_Workflow_IWorkflowSignal_Name.htm)|  Имя (алиас) сигнала,
с которым может быть связана произвольная логика обработки, т.е. сигналы
одного типа с разными именами могут обрабатываться по-разному.  
[Number](P_Tessa_Cards_Workflow_IWorkflowSignal_Number.htm)|  Номер сигнала,
по которому может определяться способ его прохождения. Можно задать совместно
или вместо имени сигнала [Tessa.Cards.Workflow.IWorkflowSignal.Name].  
[Parameters](P_Tessa_Cards_Workflow_IWorkflowSignal_Parameters.htm)| Параметры
поступившего сигнала в произвольном формате.  
[ProcessID](P_Tessa_Cards_Workflow_IWorkflowSignal_ProcessID.htm)|
Идентификатор подпроцесса, к которому относится сигнал, или null, если
подпроцесс определяется не по идентификатору, а по имени типа
[Tessa.Cards.Workflow.IWorkflowSignal.ProcessTypeName].  
[ProcessTypeName](P_Tessa_Cards_Workflow_IWorkflowSignal_ProcessTypeName.htm)|
Имя типа подпроцесса, на экземпляр которого отправляется сигнал. Имя должно
быть указано для любых экземпляров сигналов: как для подпроцессов с указанным
идентификатором, так и для подпроцессов, существующих в единственном
экземпляре для карточки. Если в текущий момент активно несколько подпроцессов
данного типа и не был указан идентификатор подпроцесса, то только один
экземпляр (случайный) получит сигнал для обработки.  
[Type](P_Tessa_Cards_Workflow_IWorkflowSignal_Type.htm)| Тип сигнала, влияет
на способ его обработки.  
##  __Методы
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
