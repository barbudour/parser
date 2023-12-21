# WfResolutionParentAction - перечисление
Действие родительской резолюции по отношению к текущей, в результате которого
текущая резолюция была создана.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Workflow.Wf](N_Tessa_Extensions_Default_Client_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public enum WfResolutionParentAction
VB __Копировать
     Public Enumeration WfResolutionParentAction
C++ __Копировать
     public enum class WfResolutionParentAction
F# __Копировать
     type WfResolutionParentAction
##  __Члены
None| 0|  Действие не определено или родительская резолюция отсутствует.  
---|---|---  
SendToPerformer| 1|  Резолюция была создана в результате отправки родительской
резолюции исполнителю.  
SendControl| 2|  Резолюция была создана как контроль исполнения в результате
завершения родительской резолюции.  
CreateChild| 3|  Резолюция была создана как дочерняя по отношению к
родительской резолюции.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Client_Workflow_Wf.htm)
