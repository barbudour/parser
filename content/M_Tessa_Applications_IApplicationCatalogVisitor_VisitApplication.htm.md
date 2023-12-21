# IApplicationCatalogVisitor.VisitApplication - метод
Вызывает операцию над моделью model с контекстом operationContext
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void VisitApplication(
    	[NotNullAttribute] IApplicationModel model,
    	[NotNullAttribute] IOperationContext operationContext
    )
VB __Копировать
     Sub VisitApplication ( 
    	<NotNullAttribute> model As IApplicationModel,
    	<NotNullAttribute> operationContext As IOperationContext
    )
C++ __Копировать
     void VisitApplication(
    	[NotNullAttribute] IApplicationModel^ model, 
    	[NotNullAttribute] IOperationContext^ operationContext
    )
F# __Копировать
     abstract VisitApplication : 
            [<NotNullAttribute>] model : IApplicationModel * 
            [<NotNullAttribute>] operationContext : IOperationContext -> unit 
#### Параметры
model [IApplicationModel](T_Tessa_Applications_IApplicationModel.htm)
     Обрабатываемая модель 
operationContext
[IOperationContext](T_Tessa_Applications_Containers_IOperationContext.htm)
     Контекст операции 
## __См. также
#### Ссылки
[IApplicationCatalogVisitor -
](T_Tessa_Applications_IApplicationCatalogVisitor.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
