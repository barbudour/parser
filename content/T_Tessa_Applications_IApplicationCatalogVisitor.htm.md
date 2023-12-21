# IApplicationCatalogVisitor - интерфейс
Описание интерфейса операции над каталогом приложений
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationCatalogVisitor : IOperationVisitor
VB __Копировать
     Public Interface IApplicationCatalogVisitor
    	Inherits IOperationVisitor
C++ __Копировать
     public interface class IApplicationCatalogVisitor : IOperationVisitor
F# __Копировать
     type IApplicationCatalogVisitor = 
        interface
            interface IOperationVisitor
        end
Implements
    [IOperationVisitor](T_Tessa_Applications_Containers_IOperationVisitor.htm)
##  __Методы
[EnterApplicationCatalog](M_Tessa_Applications_IApplicationCatalogVisitor_EnterApplicationCatalog.htm)|
Производит операцию над катлогом приложений catalog  
---|---  
[LeaveApplicationCatalog](M_Tessa_Applications_IApplicationCatalogVisitor_LeaveApplicationCatalog.htm)|
Производит операцию над катлогом приложений catalog  
[VisitApplication](M_Tessa_Applications_IApplicationCatalogVisitor_VisitApplication.htm)|
Вызывает операцию над моделью model с контекстом operationContext  
##  __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
