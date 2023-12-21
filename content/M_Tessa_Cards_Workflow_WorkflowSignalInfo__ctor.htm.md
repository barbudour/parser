# WorkflowSignalInfo - конструктор
Создаёт информацию по сигналу, поступившему в подпроцесс, с указанием его
свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public WorkflowSignalInfo(
    	IWorkflowSignal signal,
    	IWorkflowProcessInfo processInfo
    )
VB __Копировать
     Public Sub New ( 
    	signal As IWorkflowSignal,
    	processInfo As IWorkflowProcessInfo
    )
C++ __Копировать
     public:
    WorkflowSignalInfo(
    	IWorkflowSignal^ signal, 
    	IWorkflowProcessInfo^ processInfo
    )
F# __Копировать
     new : 
            signal : IWorkflowSignal * 
            processInfo : IWorkflowProcessInfo -> WorkflowSignalInfo
#### Параметры
signal [IWorkflowSignal](T_Tessa_Cards_Workflow_IWorkflowSignal.htm)
    Сигнал, отправленный для подпроцесса.
processInfo
[IWorkflowProcessInfo](T_Tessa_Cards_Workflow_IWorkflowProcessInfo.htm)
    Информация по подпроцессу, в пределах которого отправлен сигнал.
##  __См. также
#### Ссылки
[WorkflowSignalInfo - ](T_Tessa_Cards_Workflow_WorkflowSignalInfo.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
