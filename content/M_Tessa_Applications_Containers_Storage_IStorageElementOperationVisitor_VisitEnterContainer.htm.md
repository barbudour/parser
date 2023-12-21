# IStorageElementOperationVisitor.VisitEnterContainer - метод
Вызывается при обработке входа в контейнер хранилища
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void VisitEnterContainer(
    	[NotNullAttribute] IStorageElement container,
    	[NotNullAttribute] IOperationContext context
    )
VB __Копировать
     Sub VisitEnterContainer ( 
    	<NotNullAttribute> container As IStorageElement,
    	<NotNullAttribute> context As IOperationContext
    )
C++ __Копировать
     void VisitEnterContainer(
    	[NotNullAttribute] IStorageElement^ container, 
    	[NotNullAttribute] IOperationContext^ context
    )
F# __Копировать
     abstract VisitEnterContainer : 
            [<NotNullAttribute>] container : IStorageElement * 
            [<NotNullAttribute>] context : IOperationContext -> unit 
#### Параметры
container
[IStorageElement](T_Tessa_Applications_Containers_Storage_IStorageElement.htm)
     Контейнер элементов хранилища 
context
[IOperationContext](T_Tessa_Applications_Containers_IOperationContext.htm)
     Контекст операции 
## __См. также
#### Ссылки
[IStorageElementOperationVisitor -
](T_Tessa_Applications_Containers_Storage_IStorageElementOperationVisitor.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
