# IApplicationCatalogVisitor.LeaveApplicationCatalog - метод
Производит операцию над катлогом приложений catalog
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void LeaveApplicationCatalog(
    	[NotNullAttribute] IApplicationCatalog catalog,
    	[NotNullAttribute] IOperationContext context
    )
VB __Копировать
     Sub LeaveApplicationCatalog ( 
    	<NotNullAttribute> catalog As IApplicationCatalog,
    	<NotNullAttribute> context As IOperationContext
    )
C++ __Копировать
     void LeaveApplicationCatalog(
    	[NotNullAttribute] IApplicationCatalog^ catalog, 
    	[NotNullAttribute] IOperationContext^ context
    )
F# __Копировать
     abstract LeaveApplicationCatalog : 
            [<NotNullAttribute>] catalog : IApplicationCatalog * 
            [<NotNullAttribute>] context : IOperationContext -> unit 
#### Параметры
catalog [IApplicationCatalog](T_Tessa_Applications_IApplicationCatalog.htm)
     Каталог приложений над которым производится операция 
context
[IOperationContext](T_Tessa_Applications_Containers_IOperationContext.htm)
     Контекст операции 
## __См. также
#### Ссылки
[IApplicationCatalogVisitor -
](T_Tessa_Applications_IApplicationCatalogVisitor.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
